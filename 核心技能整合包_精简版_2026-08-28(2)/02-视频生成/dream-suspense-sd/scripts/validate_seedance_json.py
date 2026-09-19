#!/usr/bin/env python3
"""Validate legacy/internal Seedance JSON fixtures; never generate user-facing SD output."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any


ROOT_KEYS = {
    "shot_type",
    "estimated_duration",
    "camera_phase_schedule",
    "style_lock",
    "keyframe_first_frame",
    "reference_images",
    "audio",
    "performance_timeline",
    "negative_prompt",
}
STYLE_KEYS = {"medium", "aesthetic", "lighting", "aspect_ratio"}
KEYFRAME_KEYS = {"description", "reference_id"}
AUDIO_KEYS = {"environment", "voices", "music"}
TIMELINE_KEYS = {"time", "frame", "camera", "beat", "sfx", "dialogue"}

MAX_DURATION_SECONDS = 30.0
DURATION_RE = re.compile(r"^(\d+(?:\.\d+)?)s$")
TIME_RE = re.compile(r"^(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)s$")
ID_RE = re.compile(r"@\[[^\]\r\n]+\]")
CJK_RE = re.compile(r"[\u3400-\u9fff]")
CAMERA_OPERATOR_RE = re.compile(
    r"\b(?:hold|lock|pan|tilt|push|pull|dolly|truck|pedestal|orbit|arc|roll|"
    r"crane|whip|track|tracking|zoom|dive|rise|drop|follow|reframe|handheld|"
    r"top-down|fisheye|rack focus)\b",
    re.I,
)
SFX_RE = re.compile(r"^(?:【[\x20-\x7e]+】)+$")
NEGATIVE_FORBIDDEN = set("不无没非的了在从被还再又后向朝")


def exact_keys(value: Any, expected: set[str], owner: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{owner} must be an object")
        return
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        errors.append(f"{owner} missing keys: {', '.join(missing)}")
    if extra:
        errors.append(f"{owner} has custom keys: {', '.join(extra)}")


def require_string(value: Any, owner: str, errors: list[str], allow_empty: bool = False) -> None:
    if not isinstance(value, str):
        errors.append(f"{owner} must be a string")
    elif not allow_empty and not value.strip():
        errors.append(f"{owner} must not be empty")


def strings_in(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(strings_in(item))
        return result
    if isinstance(value, dict):
        result = []
        for item in value.values():
            result.extend(strings_in(item))
        return result
    return []


def validate(path: Path, max_chars: int | None) -> tuple[list[str], list[str], int, int]:
    errors: list[str] = []
    warnings: list[str] = []
    raw = path.read_text(encoding="utf-8")
    payload_text = raw.strip()
    if "\n" in payload_text or "\r" in payload_text:
        errors.append("payload must be compact single-line JSON")
    try:
        data = json.loads(payload_text)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"], warnings, len(payload_text), max_chars or 0

    exact_keys(data, ROOT_KEYS, "root", errors)
    if not isinstance(data, dict):
        return errors, warnings, len(payload_text), max_chars or 0

    require_string(data.get("shot_type"), "shot_type", errors)
    if isinstance(data.get("shot_type"), str) and CJK_RE.search(data["shot_type"]):
        errors.append("shot_type must be a short English phrase")
    require_string(data.get("estimated_duration"), "estimated_duration", errors)
    duration_match = (
        DURATION_RE.fullmatch(data.get("estimated_duration", ""))
        if isinstance(data.get("estimated_duration"), str)
        else None
    )
    duration = float(duration_match.group(1)) if duration_match else 0.0
    if not duration_match:
        errors.append("estimated_duration must use forms such as 30s or 6.5s")
    elif duration > MAX_DURATION_SECONDS:
        errors.append(f"estimated_duration must not exceed {MAX_DURATION_SECONDS:g}s")
    require_string(data.get("camera_phase_schedule"), "camera_phase_schedule", errors)

    style = data.get("style_lock")
    exact_keys(style, STYLE_KEYS, "style_lock", errors)
    if isinstance(style, dict):
        for key in STYLE_KEYS:
            require_string(style.get(key), f"style_lock.{key}", errors)

    keyframe = data.get("keyframe_first_frame")
    exact_keys(keyframe, KEYFRAME_KEYS, "keyframe_first_frame", errors)
    if isinstance(keyframe, dict):
        require_string(keyframe.get("description"), "keyframe_first_frame.description", errors)
        require_string(
            keyframe.get("reference_id"),
            "keyframe_first_frame.reference_id",
            errors,
            allow_empty=True,
        )

    references = data.get("reference_images")
    if not isinstance(references, dict):
        errors.append("reference_images must be an object")
        references = {}
    else:
        for key, value in references.items():
            if not isinstance(key, str) or not ID_RE.fullmatch(key) or key != key.strip():
                errors.append(f"invalid reference_images key: {key!r}")
            require_string(value, f"reference_images[{key!r}]", errors)

    audio = data.get("audio")
    exact_keys(audio, AUDIO_KEYS, "audio", errors)
    voices: dict[str, Any] = {}
    if isinstance(audio, dict):
        require_string(audio.get("environment"), "audio.environment", errors, allow_empty=True)
        require_string(audio.get("music"), "audio.music", errors, allow_empty=True)
        if not isinstance(audio.get("voices"), dict):
            errors.append("audio.voices must be an object")
        else:
            voices = audio["voices"]
            for speaker, voice in voices.items():
                require_string(speaker, "audio.voices speaker", errors)
                require_string(voice, f"audio.voices[{speaker!r}]", errors)

    timeline = data.get("performance_timeline")
    ranges: list[tuple[float, float]] = []
    has_dialogue = False
    if not isinstance(timeline, list) or not timeline:
        errors.append("performance_timeline must be a non-empty array")
        timeline = []
    for index, item in enumerate(timeline, 1):
        owner = f"performance_timeline[{index}]"
        exact_keys(item, TIMELINE_KEYS, owner, errors)
        if not isinstance(item, dict):
            continue
        for key in ("time", "frame", "camera", "beat"):
            require_string(item.get(key), f"{owner}.{key}", errors)
        for key in ("sfx", "dialogue"):
            require_string(item.get(key), f"{owner}.{key}", errors, allow_empty=True)

        time_value = item.get("time", "")
        match = TIME_RE.fullmatch(time_value) if isinstance(time_value, str) else None
        if not match:
            errors.append(f"{owner}.time must use forms such as 0-2s")
        else:
            start, end = float(match.group(1)), float(match.group(2))
            if end <= start:
                errors.append(f"{owner}.time must have end > start")
            ranges.append((start, end))

        camera = item.get("camera", "")
        if isinstance(camera, str):
            if CJK_RE.search(camera):
                errors.append(f"{owner}.camera must contain English operators only")
            if camera and not CAMERA_OPERATOR_RE.search(camera):
                errors.append(f"{owner}.camera has no recognized camera operator")

        sfx = item.get("sfx", "")
        if isinstance(sfx, str) and sfx and not SFX_RE.fullmatch(sfx):
            errors.append(f"{owner}.sfx must use full-width brackets around English cues")

        dialogue = item.get("dialogue", "")
        if isinstance(dialogue, str) and dialogue:
            has_dialogue = True
            if "{" not in dialogue or "}" not in dialogue:
                errors.append(f"{owner}.dialogue must wrap spoken text in braces")

    if ranges:
        if not math.isclose(ranges[0][0], 0.0, abs_tol=1e-6):
            errors.append("timeline must start at 0s")
        for previous, current in zip(ranges, ranges[1:]):
            if not math.isclose(previous[1], current[0], abs_tol=1e-6):
                errors.append(
                    f"timeline gap/overlap between {previous[0]:g}-{previous[1]:g}s "
                    f"and {current[0]:g}-{current[1]:g}s"
                )
        if duration and not math.isclose(ranges[-1][1], duration, abs_tol=1e-6):
            errors.append("timeline end must equal estimated_duration")

    if voices and not has_dialogue:
        errors.append("audio.voices must be empty when all dialogue fields are empty")
    if has_dialogue and not voices:
        warnings.append("dialogue exists but audio.voices is empty")

    negatives = data.get("negative_prompt")
    if not isinstance(negatives, list):
        errors.append("negative_prompt must be an array")
    else:
        for index, token in enumerate(negatives, 1):
            if not isinstance(token, str) or not token.strip():
                errors.append(f"negative_prompt[{index}] must be a non-empty string")
                continue
            if len(token) > 5:
                errors.append(f"negative_prompt[{index}] exceeds 5 characters")
            if any(char in NEGATIVE_FORBIDDEN for char in token):
                errors.append(f"negative_prompt[{index}] contains a forbidden function/negation character")

    used_ids = set(ID_RE.findall("\n".join(strings_in(data))))
    known_ids = set(references)
    unknown = sorted(used_ids - known_ids)
    if unknown:
        errors.append("IDs missing from reference_images: " + ", ".join(unknown))
    unused = sorted(known_ids - used_ids)
    if unused:
        warnings.append("unused reference_images IDs: " + ", ".join(unused))

    budget = max_chars if max_chars is not None else math.floor(duration * 333)
    if budget and len(payload_text) > budget:
        errors.append(f"payload length {len(payload_text)} exceeds character budget {budget}")

    return errors, warnings, len(payload_text), budget


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Maintainer-only validator for internal JSON regression fixtures."
    )
    parser.add_argument("payload", type=Path)
    parser.add_argument("--max-chars", type=int)
    args = parser.parse_args()

    errors, warnings, length, budget = validate(args.payload, args.max_chars)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {args.payload} | chars={length} | budget={budget}")
        return 1
    print(f"PASS: {args.payload} | chars={length} | budget={budget}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
