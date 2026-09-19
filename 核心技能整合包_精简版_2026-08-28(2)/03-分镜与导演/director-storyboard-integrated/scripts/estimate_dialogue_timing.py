#!/usr/bin/env python3
"""Estimate Chinese dialogue duration and phrase windows for short-form storyboards."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "references" / "runtime-contract.json"
MODE_KEYS = {
    "restrained": "restrained_chars_per_second",
    "normal": "normal_chars_per_second",
    "heated": "heated_chars_per_second",
    "system": "system_voice_chars_per_second",
}


def visible_units(text: str) -> int:
    chinese = re.findall(r"[\u3400-\u9fff]", text)
    words = re.findall(r"[A-Za-z0-9]+", text)
    return len(chinese) + len(words)


def punctuation_pause(text: str, timing: dict) -> float:
    comma_count = len(re.findall(r"[，、,;；:：]", text))
    sentence_count = len(re.findall(r"[。！？!?…]", text))
    return (
        comma_count * float(timing["comma_pause_seconds"])
        + sentence_count * float(timing["sentence_pause_seconds"])
    )


def phrase_windows(text: str) -> list[dict]:
    phrases = [part.strip() for part in re.split(r"(?<=[，。！？!?；;：:…])", text) if part.strip()]
    return [{"text": phrase, "units": visible_units(phrase)} for phrase in phrases]


def estimate(text: str, mode: str, contract: dict) -> dict:
    timing = contract["dialogue_timing"]
    cps_low, cps_high = timing[MODE_KEYS[mode]]
    units = visible_units(text)
    pause = punctuation_pause(text, timing)
    fastest = round(units / float(cps_high) + pause, 2) if units else 0.0
    slowest = round(units / float(cps_low) + pause, 2) if units else 0.0
    windows = phrase_windows(text)
    for window in windows:
        window["fast_seconds"] = round(window["units"] / float(cps_high), 2)
        window["slow_seconds"] = round(window["units"] / float(cps_low), 2)
    return {
        "mode": mode,
        "units": units,
        "punctuation_pause_seconds": round(pause, 2),
        "estimated_seconds": {"fast": fastest, "slow": slowest},
        "phrase_windows": windows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="?")
    parser.add_argument("--file", type=Path)
    parser.add_argument("--mode", choices=tuple(MODE_KEYS), default="normal")
    parser.add_argument("--available-seconds", type=float)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    if bool(args.text) == bool(args.file):
        parser.error("provide dialogue text or --file")
    text = args.file.read_text(encoding="utf-8").strip() if args.file else args.text.strip()
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    result = estimate(text, args.mode, contract)

    if args.available_seconds is not None:
        fast = result["estimated_seconds"]["fast"]
        slow = result["estimated_seconds"]["slow"]
        if args.available_seconds < fast:
            fit = "overloaded"
        elif args.available_seconds < slow:
            fit = "tight"
        else:
            fit = "comfortable"
        result["available_seconds"] = args.available_seconds
        result["fit"] = fit

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"mode: {result['mode']}")
        print(f"visible units: {result['units']}")
        print(
            "estimated seconds: "
            f"{result['estimated_seconds']['fast']}-{result['estimated_seconds']['slow']}"
        )
        if "fit" in result:
            print(f"window fit: {result['fit']} ({result['available_seconds']}s available)")
        for index, window in enumerate(result["phrase_windows"], start=1):
            print(
                f"phrase {index}: {window['text']} "
                f"[{window['fast_seconds']}-{window['slow_seconds']}s]"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
