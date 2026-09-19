#!/usr/bin/env python3
"""Measure delivery-oriented audio properties from mono/stereo PCM WAV files."""

from __future__ import annotations

import argparse
import json
import math
import wave
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT.parent / "director-storyboard-integrated" / "references" / "runtime-contract.json"
EPS = 1e-15


def db(value: float) -> float:
    return 20.0 * math.log10(max(float(value), EPS))


def power_db(value: float) -> float:
    return 10.0 * math.log10(max(float(value), EPS))


def decode_pcm(raw: bytes, sample_width: int) -> np.ndarray:
    if sample_width == 1:
        return (np.frombuffer(raw, dtype=np.uint8).astype(np.float64) - 128.0) / 128.0
    if sample_width == 2:
        return np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    if sample_width == 3:
        data = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3)
        values = data[:, 0].astype(np.int32) | (data[:, 1].astype(np.int32) << 8) | (data[:, 2].astype(np.int32) << 16)
        values = np.where(values & 0x800000, values - 0x1000000, values)
        return values.astype(np.float64) / 8388608.0
    if sample_width == 4:
        return np.frombuffer(raw, dtype="<i4").astype(np.float64) / 2147483648.0
    raise ValueError(f"unsupported PCM sample width: {sample_width}")


def read_pcm_wav(path: Path) -> tuple[np.ndarray, int, int]:
    with wave.open(str(path), "rb") as handle:
        if handle.getcomptype() != "NONE":
            raise ValueError("compressed WAV is not supported")
        channels = handle.getnchannels()
        sample_rate = handle.getframerate()
        width = handle.getsampwidth()
        frames = handle.getnframes()
        raw = handle.readframes(frames)
    if channels not in (1, 2):
        raise ValueError("only mono or stereo PCM WAV is supported")
    samples = decode_pcm(raw, width)
    if samples.size % channels:
        raise ValueError("PCM frame data is not divisible by channel count")
    return samples.reshape(-1, channels), sample_rate, width


def biquad(signal: np.ndarray, b: tuple[float, float, float], a: tuple[float, float, float]) -> np.ndarray:
    output = np.empty_like(signal, dtype=np.float64)
    for channel in range(signal.shape[1]):
        x1 = x2 = y1 = y2 = 0.0
        for index, x0 in enumerate(signal[:, channel]):
            y0 = b[0] * x0 + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2
            output[index, channel] = y0
            x2, x1 = x1, x0
            y2, y1 = y1, y0
    return output


def k_weight(signal: np.ndarray, sample_rate: int) -> np.ndarray:
    shelf_gain = 3.999843853973347
    shelf_q = 0.7071752369554196
    shelf_fc = 1681.974450955533
    k = math.tan(math.pi * shelf_fc / sample_rate)
    vh = 10.0 ** (shelf_gain / 20.0)
    vb = vh ** 0.4996667741545416
    norm = 1.0 + k / shelf_q + k * k
    shelf_b = (
        (vh + vb * k / shelf_q + k * k) / norm,
        2.0 * (k * k - vh) / norm,
        (vh - vb * k / shelf_q + k * k) / norm,
    )
    shelf_a = (1.0, 2.0 * (k * k - 1.0) / norm, (1.0 - k / shelf_q + k * k) / norm)

    hp_q = 0.5003270373238773
    hp_fc = 38.13547087602444
    k = math.tan(math.pi * hp_fc / sample_rate)
    norm = 1.0 + k / hp_q + k * k
    hp_b = (1.0 / norm, -2.0 / norm, 1.0 / norm)
    hp_a = (1.0, 2.0 * (k * k - 1.0) / norm, (1.0 - k / hp_q + k * k) / norm)
    return biquad(biquad(signal, shelf_b, shelf_a), hp_b, hp_a)


def block_powers(weighted: np.ndarray, sample_rate: int, window_s: float, hop_s: float) -> list[tuple[float, float]]:
    window = max(1, int(round(window_s * sample_rate)))
    hop = max(1, int(round(hop_s * sample_rate)))
    if len(weighted) < window:
        padded = np.pad(weighted, ((0, window - len(weighted)), (0, 0)))
        channel_powers = np.mean(np.square(padded), axis=0)
        return [(0.0, float(np.sum(channel_powers)))]
    result = []
    for start in range(0, len(weighted) - window + 1, hop):
        channel_powers = np.mean(np.square(weighted[start : start + window]), axis=0)
        result.append((start / sample_rate, float(np.sum(channel_powers))))
    return result


def loudness_from_power(power: float) -> float:
    return -0.691 + power_db(power)


def integrated_lufs(weighted: np.ndarray, sample_rate: int) -> float:
    blocks = block_powers(weighted, sample_rate, 0.4, 0.1)
    absolute = [power for _, power in blocks if loudness_from_power(power) > -70.0]
    if not absolute:
        return -150.0
    relative_gate = loudness_from_power(float(np.mean(absolute))) - 10.0
    gate = max(-70.0, relative_gate)
    gated = [power for power in absolute if loudness_from_power(power) > gate]
    return loudness_from_power(float(np.mean(gated))) if gated else -150.0


def short_term_lufs(weighted: np.ndarray, sample_rate: int) -> list[dict]:
    return [
        {"start_s": round(start, 3), "lufs_s": round(loudness_from_power(power), 2)}
        for start, power in block_powers(weighted, sample_rate, 3.0, 1.0)
    ]


def oversampled_peak(signal: np.ndarray, factor: int = 4) -> float:
    chunk = max(2048, 48000)
    peak = 0.0
    for channel in range(signal.shape[1]):
        data = signal[:, channel]
        for start in range(0, len(data), chunk):
            part = data[start : start + chunk]
            if not len(part):
                continue
            spectrum = np.fft.rfft(part)
            upsampled = np.fft.irfft(spectrum, n=len(part) * factor) * factor
            peak = max(peak, float(np.max(np.abs(upsampled))))
    return peak


def window_rms_db(signal: np.ndarray, sample_rate: int, window_s: float = 0.1) -> np.ndarray:
    window = max(1, int(round(window_s * sample_rate)))
    values = []
    for start in range(0, len(signal), window):
        part = signal[start : start + window]
        if len(part):
            values.append(db(math.sqrt(float(np.mean(np.square(part))))))
    return np.asarray(values, dtype=np.float64)


def analyze_arrays(
    signal: np.ndarray,
    sample_rate: int,
    profile_name: str,
    profiles: dict,
    qa_config: dict,
    dialogue: np.ndarray | None = None,
) -> dict:
    profile = profiles[profile_name]
    weighted = k_weight(signal, sample_rate)
    integrated = integrated_lufs(weighted, sample_rate)
    short_term = short_term_lufs(weighted, sample_rate)
    sample_peak = float(np.max(np.abs(signal))) if signal.size else 0.0
    estimated_true_peak = oversampled_peak(signal)
    total_rms = math.sqrt(float(np.mean(np.square(signal)))) if signal.size else 0.0
    windows = window_rms_db(signal, sample_rate)
    noise_floor = float(np.percentile(windows, 10)) if windows.size else -150.0
    silence_ratio = float(np.mean(windows < -60.0)) if windows.size else 1.0
    clipped = int(np.sum(np.abs(signal) >= float(qa_config["clip_threshold_full_scale"])))
    dc = [float(np.mean(signal[:, channel])) for channel in range(signal.shape[1])]
    correlation = None
    stereo_balance = None
    if signal.shape[1] == 2:
        left = signal[:, 0] - np.mean(signal[:, 0])
        right = signal[:, 1] - np.mean(signal[:, 1])
        denominator = math.sqrt(float(np.sum(left * left) * np.sum(right * right)))
        correlation = float(np.sum(left * right) / denominator) if denominator > EPS else 1.0
        left_rms = math.sqrt(float(np.mean(np.square(signal[:, 0]))))
        right_rms = math.sqrt(float(np.mean(np.square(signal[:, 1]))))
        stereo_balance = db(left_rms) - db(right_rms)

    dialogue_margin = None
    if dialogue is not None:
        if dialogue.shape != signal.shape:
            raise ValueError("dialogue stem must match mix shape")
        residual = signal - dialogue
        dialogue_rms = math.sqrt(float(np.mean(np.square(dialogue))))
        residual_rms = math.sqrt(float(np.mean(np.square(residual))))
        dialogue_margin = power_db((dialogue_rms * dialogue_rms) / max(residual_rms * residual_rms, EPS))

    warnings = []
    loudness_delta = integrated - float(profile["lufs_i"])
    if abs(loudness_delta) > float(qa_config["loudness_tolerance_lu"]):
        warnings.append(f"integrated loudness differs from profile by {loudness_delta:+.2f} LU")
    peak_db = db(estimated_true_peak)
    if peak_db > float(profile["dbtp"]):
        warnings.append(f"oversampled peak estimate is {peak_db - float(profile['dbtp']):.2f} dB above profile ceiling")
    if clipped:
        warnings.append(
            f"{clipped} samples are at or above {qa_config['clip_threshold_full_scale']} full scale"
        )
    if sample_rate != int(qa_config["recommended_sample_rate_hz"]):
        warnings.append(
            f"sample rate is {sample_rate} Hz; workflow reference is {qa_config['recommended_sample_rate_hz']} Hz"
        )
    if any(abs(value) > 0.01 for value in dc):
        warnings.append("DC offset exceeds 0.01 on at least one channel")
    if correlation is not None and correlation < -0.2:
        warnings.append("stereo correlation is strongly negative; verify mono compatibility")
    if stereo_balance is not None and abs(stereo_balance) > float(qa_config["stereo_balance_warning_db"]):
        warnings.append(f"left/right RMS balance differs by {stereo_balance:+.2f} dB")
    if dialogue_margin is not None and dialogue_margin < 0:
        warnings.append("dialogue stem energy is below the residual mix")

    return {
        "status": "pass" if not warnings else "review",
        "delivery_profile": profile_name,
        "target_lufs_i": profile["lufs_i"],
        "target_dbtp": profile["dbtp"],
        "sample_rate": sample_rate,
        "channels": signal.shape[1],
        "duration_s": round(len(signal) / sample_rate, 3),
        "integrated_lufs": round(integrated, 2),
        "loudness_delta_lu": round(loudness_delta, 2),
        "short_term_lufs_min": round(min(item["lufs_s"] for item in short_term), 2),
        "short_term_lufs_max": round(max(item["lufs_s"] for item in short_term), 2),
        "short_term_range_lu": round(
            max(item["lufs_s"] for item in short_term) - min(item["lufs_s"] for item in short_term), 2
        ),
        "short_term_lufs_timeline": short_term,
        "rms_dbfs": round(db(total_rms), 2),
        "sample_peak_dbfs": round(db(sample_peak), 2),
        "oversampled_peak_estimate_dbfs": round(peak_db, 2),
        "crest_factor_db": round(db(sample_peak) - db(total_rms), 2),
        "noise_floor_proxy_dbfs": round(noise_floor, 2),
        "silence_ratio": round(silence_ratio, 4),
        "clipped_sample_count": clipped,
        "dc_offset": [round(value, 6) for value in dc],
        "stereo_correlation": None if correlation is None else round(correlation, 4),
        "stereo_balance_db": None if stereo_balance is None else round(stereo_balance, 2),
        "dialogue_to_background_db": None if dialogue_margin is None else round(dialogue_margin, 2),
        "warnings": warnings,
        "measurement_note": "Integrated loudness uses K-weighting and gated blocks. Oversampled peak is an FFT estimate, not a certified true-peak meter.",
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Audio Delivery Analysis",
        "",
        f"- Status: `{report['status']}`",
        f"- Profile: `{report['delivery_profile']}` / `{report['target_lufs_i']} LUFS-I` / `{report['target_dbtp']} dBTP`",
        f"- Format: `{report['sample_rate']} Hz` / `{report['channels']} ch` / `{report['duration_s']} s`",
        f"- Integrated: `{report['integrated_lufs']} LUFS-I` (`{report['loudness_delta_lu']:+} LU`)",
        f"- Short-term: `{report['short_term_lufs_min']}..{report['short_term_lufs_max']} LUFS-S`",
        f"- RMS / sample peak / oversampled peak: `{report['rms_dbfs']} / {report['sample_peak_dbfs']} / {report['oversampled_peak_estimate_dbfs']} dBFS`",
        f"- Noise floor proxy / silence ratio: `{report['noise_floor_proxy_dbfs']} dBFS` / `{report['silence_ratio']}`",
    ]
    if report["stereo_correlation"] is not None:
        lines.append(f"- Stereo correlation: `{report['stereo_correlation']}`")
    if report["dialogue_to_background_db"] is not None:
        lines.append(f"- Dialogue to background: `{report['dialogue_to_background_db']} dB`")
    if report["warnings"]:
        lines.extend(["", "## Review", *[f"- {warning}" for warning in report["warnings"]]])
    lines.extend(["", report["measurement_note"], ""])
    return "\n".join(lines)


def self_test(profiles: dict, qa_config: dict) -> dict:
    sample_rate = 48000
    duration = 4
    time = np.arange(sample_rate * duration, dtype=np.float64) / sample_rate
    tone = 0.20 * np.sin(2.0 * math.pi * 1000.0 * time)
    room = 0.008 * np.sin(2.0 * math.pi * 80.0 * time)
    stereo = np.column_stack((tone + room, tone * 0.98 + room))
    report = analyze_arrays(stereo, sample_rate, "social_balanced", profiles, qa_config)
    if not math.isfinite(report["integrated_lufs"]):
        raise RuntimeError("self-test integrated loudness is not finite")
    if report["channels"] != 2 or report["duration_s"] != 4.0:
        raise RuntimeError("self-test format metrics failed")
    if not (-30.0 < report["integrated_lufs"] < -10.0):
        raise RuntimeError(f"self-test loudness is outside the expected range: {report['integrated_lufs']}")
    if report["sample_peak_dbfs"] > 0.0:
        raise RuntimeError("self-test sample peak exceeded digital full scale")
    if report["status"] != "pass":
        raise RuntimeError(f"self-test produced review warnings: {report['warnings']}")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("wav", type=Path, nargs="?")
    parser.add_argument("--dialogue", type=Path)
    parser.add_argument("--profile", default="social_balanced")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    profiles = contract["sound_mix"]["delivery_profiles"]
    qa_config = contract["sound_mix"]["audio_delivery_qa"]
    if args.profile not in profiles:
        raise SystemExit(f"unknown delivery profile: {args.profile}")
    if args.self_test:
        report = self_test(profiles, qa_config)
    else:
        if not args.wav:
            raise SystemExit("wav path is required unless --self-test is used")
        signal, sample_rate, _ = read_pcm_wav(args.wav)
        dialogue = None
        if args.dialogue:
            dialogue, dialogue_rate, _ = read_pcm_wav(args.dialogue)
            if dialogue_rate != sample_rate:
                raise SystemExit("dialogue stem sample rate must match mix")
        report = analyze_arrays(signal, sample_rate, args.profile, profiles, qa_config, dialogue)

    payload = render_markdown(report) if args.format == "markdown" else json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 1 if args.strict and report["status"] != "pass" else 0


if __name__ == "__main__":
    raise SystemExit(main())
