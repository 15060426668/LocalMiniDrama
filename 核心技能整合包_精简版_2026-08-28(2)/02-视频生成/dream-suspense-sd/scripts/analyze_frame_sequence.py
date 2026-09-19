#!/usr/bin/env python3
"""Analyze an extracted frame sequence for technical continuity drift."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".ppm"}


def metrics(path: Path) -> dict:
    with Image.open(path) as image:
        rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    luminance = 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]
    gradient_x = np.abs(np.diff(luminance, axis=1)).mean() if luminance.shape[1] > 1 else 0.0
    gradient_y = np.abs(np.diff(luminance, axis=0)).mean() if luminance.shape[0] > 1 else 0.0
    thumb = np.asarray(Image.fromarray(rgb.astype(np.uint8)).resize((32, 18)), dtype=np.float32)
    return {
        "path": str(path),
        "width": int(rgb.shape[1]),
        "height": int(rgb.shape[0]),
        "aspect_ratio": round(rgb.shape[1] / rgb.shape[0], 5),
        "luminance_mean": round(float(luminance.mean()), 3),
        "luminance_contrast": round(float(luminance.std()), 3),
        "sharpness_proxy": round(float(gradient_x + gradient_y), 3),
        "mean_rgb": [round(float(value), 3) for value in rgb.mean(axis=(0, 1))],
        "thumbnail": thumb,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    paths = sorted(path for path in args.directory.iterdir() if path.suffix.lower() in SUPPORTED)
    if len(paths) < 2:
        raise SystemExit("frame QA requires at least two images")

    raw = [metrics(path) for path in paths]
    findings = []
    base_aspect = raw[0]["aspect_ratio"]
    previous = None
    for index, item in enumerate(raw):
        if abs(item["aspect_ratio"] - base_aspect) > 0.001:
            findings.append({"frame": index, "level": "ERROR", "issue": "aspect_ratio_drift"})
        if item["luminance_contrast"] < 2.0 and (
            item["luminance_mean"] < 3.0 or item["luminance_mean"] > 252.0
        ):
            findings.append({"frame": index, "level": "ERROR", "issue": "blank_or_solid_frame"})
        if item["sharpness_proxy"] < 1.0:
            findings.append({"frame": index, "level": "WARNING", "issue": "very_low_detail"})
        if previous is not None:
            frame_diff = float(np.abs(item["thumbnail"] - previous["thumbnail"]).mean())
            luminance_jump = abs(item["luminance_mean"] - previous["luminance_mean"])
            color_jump = float(np.linalg.norm(np.array(item["mean_rgb"]) - np.array(previous["mean_rgb"])))
            if frame_diff < 0.3:
                findings.append({"frame": index, "level": "WARNING", "issue": "near_duplicate_frame"})
            if luminance_jump > 35.0:
                findings.append({"frame": index, "level": "WARNING", "issue": "abrupt_luminance_jump"})
            if color_jump > 55.0:
                findings.append({"frame": index, "level": "WARNING", "issue": "abrupt_color_jump"})
        previous = item

    frames = [{key: value for key, value in item.items() if key != "thumbnail"} for item in raw]
    result = {
        "directory": str(args.directory),
        "frame_count": len(frames),
        "frames": frames,
        "findings": findings,
        "manual_checks_required": [
            "character_identity",
            "face_and_hand_geometry",
            "prop_ownership",
            "screen_direction",
            "light_source_motivation",
            "tail_frame_story_continuity"
        ]
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    return 1 if any(item["level"] == "ERROR" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
