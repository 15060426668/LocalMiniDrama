#!/usr/bin/env python3
"""Validate a storyboard sound manifest and estimate simultaneous digital levels."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT.parent / "director-storyboard-integrated" / "references" / "runtime-contract.json"


def energy_sum_db(levels: list[float]) -> float:
    return 10.0 * math.log10(sum(10.0 ** (level / 10.0) for level in levels))


def coherent_peak_db(levels: list[float]) -> float:
    return 20.0 * math.log10(sum(10.0 ** (level / 20.0) for level in levels))


def require_number(value: Any, label: str, errors: list[str]) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        errors.append(f"{label} must be numeric")
        return None
    return float(value)


def analyze_manifest(manifest: dict, contract: dict | None = None) -> dict:
    contract = contract or json.loads(CONTRACT.read_text(encoding="utf-8"))
    sound_contract = contract["sound_mix"]
    profiles = sound_contract["delivery_profiles"]
    buses = set(sound_contract["stem_buses"])
    profile_name = manifest.get("delivery_profile", sound_contract["default_delivery_profile"])
    errors: list[str] = []
    warnings: list[str] = []

    if profile_name not in profiles:
        errors.append(f"unknown delivery_profile: {profile_name}")
        profile = profiles[sound_contract["default_delivery_profile"]]
    else:
        profile = profiles[profile_name]

    segments = manifest.get("segments")
    if not isinstance(segments, list) or not segments:
        return {
            "status": "fail",
            "delivery_profile": profile_name,
            "errors": ["segments must be a non-empty list"],
            "warnings": warnings,
            "segments": [],
        }

    reports = []
    previous_end = None
    for index, segment in enumerate(segments, start=1):
        prefix = f"segment[{index}]"
        if not isinstance(segment, dict):
            errors.append(f"{prefix} must be an object")
            continue
        segment_id = str(segment.get("id", f"S{index}"))
        start = segment.get("start_s")
        end = segment.get("end_s")
        if not isinstance(start, int) or not isinstance(end, int) or end <= start:
            errors.append(f"{prefix} requires integer start_s/end_s with end_s > start_s")
        elif previous_end is not None and start != previous_end:
            warnings.append(f"{prefix} starts at {start}s after previous end {previous_end}s")
        if isinstance(end, int):
            previous_end = end

        target_lufs_s = require_number(segment.get("target_lufs_s"), f"{prefix}.target_lufs_s", errors)
        stems = segment.get("stems")
        if not isinstance(stems, list) or not stems:
            errors.append(f"{prefix}.stems must be a non-empty list")
            continue
        if len(stems) > 5:
            warnings.append(f"{prefix} has {len(stems)} active stems; verify that one source still owns attention")

        ids: set[str] = set()
        valid_stems = []
        for stem_index, stem in enumerate(stems, start=1):
            stem_prefix = f"{prefix}.stems[{stem_index}]"
            if not isinstance(stem, dict):
                errors.append(f"{stem_prefix} must be an object")
                continue
            stem_id = str(stem.get("id", "")).strip()
            if not stem_id:
                errors.append(f"{stem_prefix}.id is required")
                continue
            if stem_id in ids:
                errors.append(f"{prefix} has duplicate stem id {stem_id}")
            ids.add(stem_id)
            bus = stem.get("bus")
            if bus not in buses:
                errors.append(f"{stem_prefix}.bus must be one of {sorted(buses)}")
            for key in ("source", "status", "position"):
                if not str(stem.get(key, "")).strip():
                    errors.append(f"{stem_prefix}.{key} is required")
            distance = require_number(stem.get("distance_m"), f"{stem_prefix}.distance_m", errors)
            rms = require_number(stem.get("rms_dbfs"), f"{stem_prefix}.rms_dbfs", errors)
            peak = require_number(stem.get("peak_dbfs"), f"{stem_prefix}.peak_dbfs", errors)
            if distance is not None and distance < 0:
                errors.append(f"{stem_prefix}.distance_m cannot be negative")
            if rms is not None and rms > 0:
                errors.append(f"{stem_prefix}.rms_dbfs cannot exceed 0 dBFS")
            if peak is not None and peak > 0:
                errors.append(f"{stem_prefix}.peak_dbfs cannot exceed 0 dBFS")
            if rms is not None and peak is not None and peak < rms:
                errors.append(f"{stem_prefix}.peak_dbfs must be at least rms_dbfs")
            if rms is not None and peak is not None:
                valid_stems.append({**stem, "id": stem_id, "rms_dbfs": rms, "peak_dbfs": peak})

        primary_id = str(segment.get("primary_source", "")).strip()
        primary = next((stem for stem in valid_stems if stem["id"] == primary_id), None)
        if not primary:
            errors.append(f"{prefix}.primary_source must match an active stem id")
        if not valid_stems:
            continue

        primary_rms = primary["rms_dbfs"] if primary else max(stem["rms_dbfs"] for stem in valid_stems)
        stem_reports = []
        for stem in valid_stems:
            actual_relative = stem["rms_dbfs"] - primary_rms
            declared_relative = stem.get("relative_to_primary_db")
            if declared_relative is not None:
                declared = require_number(
                    declared_relative,
                    f"{prefix}.{stem['id']}.relative_to_primary_db",
                    errors,
                )
                if declared is not None and abs(declared - actual_relative) > 0.6:
                    warnings.append(
                        f"{prefix}.{stem['id']} relative level declares {declared:.1f} dB but RMS values imply {actual_relative:.1f} dB"
                    )
            if primary and stem["id"] != primary_id and actual_relative > 1.0:
                warnings.append(f"{prefix}.{stem['id']} is louder than primary source {primary_id}")
            stem_reports.append(
                {
                    "id": stem["id"],
                    "bus": stem.get("bus"),
                    "source": stem.get("source"),
                    "rms_dbfs": round(stem["rms_dbfs"], 2),
                    "peak_dbfs": round(stem["peak_dbfs"], 2),
                    "relative_to_primary_db": round(actual_relative, 2),
                }
            )

        combined_rms = energy_sum_db([stem["rms_dbfs"] for stem in valid_stems])
        worst_peak = coherent_peak_db([stem["peak_dbfs"] for stem in valid_stems])
        digital_headroom = -worst_peak
        ceiling_headroom = float(profile["dbtp"]) - worst_peak
        if worst_peak > 0:
            warnings.append(f"{prefix} worst-case coherent peak exceeds 0 dBFS by {worst_peak:.2f} dB")
        elif ceiling_headroom < 0:
            warnings.append(
                f"{prefix} worst-case coherent peak is {abs(ceiling_headroom):.2f} dB above the {profile_name} true-peak ceiling; actual render requires metering/limiting"
            )
        reports.append(
            {
                "id": segment_id,
                "start_s": start,
                "end_s": end,
                "primary_source": primary_id,
                "target_lufs_s": target_lufs_s,
                "estimated_combined_rms_dbfs": round(combined_rms, 2),
                "worst_coherent_peak_dbfs": round(worst_peak, 2),
                "headroom_to_0_dbfs": round(digital_headroom, 2),
                "headroom_to_profile_dbtp": round(ceiling_headroom, 2),
                "stems": stem_reports,
            }
        )

    return {
        "status": "pass" if not errors else "fail",
        "delivery_profile": profile_name,
        "target_lufs_i": profile["lufs_i"],
        "target_dbtp": profile["dbtp"],
        "measurement_note": "Combined RMS and coherent peak are estimates. Final LUFS-I and dBTP require measurement after EQ, dynamics, panning, reverb and limiting.",
        "errors": errors,
        "warnings": warnings,
        "segments": reports,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Sound Mix Analysis",
        "",
        f"- Status: `{report['status']}`",
        f"- Delivery: `{report['delivery_profile']}` / `{report.get('target_lufs_i')} LUFS-I` / `{report.get('target_dbtp')} dBTP`",
        "",
        "| Segment | Time | Primary | Target LUFS-S | Estimated RMS dBFS | Worst coherent peak dBFS | Headroom to profile dBTP |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for segment in report["segments"]:
        lines.append(
            f"| {segment['id']} | {segment['start_s']}-{segment['end_s']}s | {segment['primary_source']} | "
            f"{segment['target_lufs_s']} | {segment['estimated_combined_rms_dbfs']} | "
            f"{segment['worst_coherent_peak_dbfs']} | {segment['headroom_to_profile_dbtp']} |"
        )
    if report["warnings"]:
        lines.extend(["", "## Warnings", *[f"- {item}" for item in report["warnings"]]])
    if report["errors"]:
        lines.extend(["", "## Errors", *[f"- {item}" for item in report["errors"]]])
    lines.extend(["", report["measurement_note"], ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    report = analyze_manifest(manifest)
    payload = render_markdown(report) if args.format == "markdown" else json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 1 if args.strict and report["status"] != "pass" else 0


if __name__ == "__main__":
    raise SystemExit(main())
