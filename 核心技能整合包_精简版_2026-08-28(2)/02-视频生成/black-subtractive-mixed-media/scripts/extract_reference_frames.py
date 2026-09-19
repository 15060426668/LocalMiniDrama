#!/usr/bin/env python3
"""Extract timeline samples and visual-change frames from a reference video."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--sample-seconds", type=float, default=1.0)
    parser.add_argument("--cut-threshold", type=float, default=0.42)
    parser.add_argument("--min-cut-gap", type=float, default=0.45)
    parser.add_argument("--sheet-columns", type=int, default=6)
    return parser.parse_args()


def frame_metrics(
    frame: np.ndarray, previous_gray: np.ndarray | None
) -> tuple[float, float, float, float, float]:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray], [0], None, [32], [0, 256])
    cv2.normalize(histogram, histogram)
    difference = 0.0
    if previous_gray is not None:
        previous_histogram = cv2.calcHist([previous_gray], [0], None, [32], [0, 256])
        cv2.normalize(previous_histogram, previous_histogram)
        difference = float(cv2.compareHist(previous_histogram, histogram, cv2.HISTCMP_BHATTACHARYYA))
    brightness = float(np.mean(gray))
    edges = cv2.Canny(gray, 80, 160)
    edge_density = float(np.count_nonzero(edges) / edges.size)
    black_ratio = float(np.count_nonzero(gray <= 12) / gray.size)
    bright_ratio = float(np.count_nonzero(gray >= 220) / gray.size)
    return difference, brightness, edge_density, black_ratio, bright_ratio


def save_frame(frame: np.ndarray, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ok, encoded = cv2.imencode(path.suffix or ".jpg", frame)
    if not ok:
        raise RuntimeError(f"Could not encode frame: {path}")
    encoded.tofile(path)


def make_sheet(paths: list[Path], output: Path, columns: int, label_prefix: str) -> None:
    if not paths:
        return
    tile_width, tile_height = 240, 150
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (tile_width * columns, tile_height * rows), "#111111")
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGB")
        image.thumbnail((tile_width - 8, tile_height - 24))
        x = (index % columns) * tile_width + (tile_width - image.width) // 2
        y = (index // columns) * tile_height + 4
        sheet.paste(image, (x, y))
        draw.text(((index % columns) * tile_width + 5, (index // columns + 1) * tile_height - 18),
                  f"{label_prefix}{path.stem}", fill="white")
    sheet.save(output, quality=92)


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    samples_dir = args.output / "samples"
    cuts_dir = args.output / "cuts"
    samples_dir.mkdir(exist_ok=True)
    cuts_dir.mkdir(exist_ok=True)

    capture = cv2.VideoCapture(str(args.video))
    if not capture.isOpened():
        raise SystemExit(f"Could not open video: {args.video}")
    fps = float(capture.get(cv2.CAP_PROP_FPS) or 0.0)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    duration = frame_count / fps if fps else 0.0

    timeline: list[dict[str, object]] = []
    sample_paths: list[Path] = []
    cut_paths: list[Path] = []
    next_sample = 0.0
    last_cut_time = -args.min_cut_gap
    previous_gray = None
    frame_index = 0

    while True:
        ok, frame = capture.read()
        if not ok:
            break
        timestamp = frame_index / fps if fps else 0.0
        difference, brightness, edge_density, black_ratio, bright_ratio = frame_metrics(frame, previous_gray)
        kind = ""
        if timestamp + 1e-9 >= next_sample:
            sample_path = samples_dir / f"{timestamp:07.2f}s.jpg"
            save_frame(frame, sample_path)
            sample_paths.append(sample_path)
            kind = "sample"
            next_sample += args.sample_seconds
        if difference >= args.cut_threshold and timestamp - last_cut_time >= args.min_cut_gap:
            cut_path = cuts_dir / f"{timestamp:07.2f}s.jpg"
            save_frame(frame, cut_path)
            cut_paths.append(cut_path)
            last_cut_time = timestamp
            kind = "cut" if not kind else "sample+cut"
        timeline.append({
            "frame": frame_index,
            "time_seconds": round(timestamp, 4),
            "kind": kind,
            "histogram_difference": round(difference, 6),
            "brightness": round(brightness, 4),
            "edge_density": round(edge_density, 6),
            "black_pixel_ratio": round(black_ratio, 6),
            "bright_pixel_ratio": round(bright_ratio, 6),
        })
        previous_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_index += 1
    capture.release()

    with (args.output / "timeline.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(timeline[0]) if timeline else ["frame"])
        writer.writeheader()
        writer.writerows(timeline)
    metadata = {
        "video": str(args.video),
        "fps": fps,
        "frame_count": frame_count,
        "decoded_frames": frame_index,
        "width": width,
        "height": height,
        "duration_seconds": duration,
        "sample_seconds": args.sample_seconds,
        "cut_threshold": args.cut_threshold,
        "cut_count": len(cut_paths),
        "sample_count": len(sample_paths),
    }
    (args.output / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=True, indent=2), encoding="utf-8")
    make_sheet(sample_paths, args.output / "contact-sheet-samples.jpg", args.sheet_columns, "S ")
    make_sheet(cut_paths, args.output / "contact-sheet-cuts.jpg", args.sheet_columns, "C ")
    print(json.dumps(metadata, ensure_ascii=True))


if __name__ == "__main__":
    main()
