#!/usr/bin/env python3
"""Build labeled review montages from verified animation scene sheets."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def fit_image(source: Image.Image, width: int, height: int) -> Image.Image:
    image = source.convert("RGB")
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), "#111111")
    x = (width - image.width) // 2
    y = (height - image.height) // 2
    canvas.paste(image, (x, y))
    return canvas


def build_episode(
    episode_dir: Path,
    output_dir: Path,
    columns: int,
    rows: int,
    cell_width: int,
    cell_height: int,
) -> int:
    sheets = sorted((episode_dir / "scene_index").glob("scene_*.jpg"))
    if not sheets:
        return 0

    label_height = 34
    page_size = columns * rows
    pages = math.ceil(len(sheets) / page_size)
    font = ImageFont.load_default()

    for page_index in range(pages):
        page_sheets = sheets[page_index * page_size : (page_index + 1) * page_size]
        canvas = Image.new(
            "RGB",
            (columns * cell_width, rows * (cell_height + label_height)),
            "#181818",
        )
        draw = ImageDraw.Draw(canvas)
        for index, path in enumerate(page_sheets):
            row, column = divmod(index, columns)
            x = column * cell_width
            y = row * (cell_height + label_height)
            with Image.open(path) as source:
                tile = fit_image(source, cell_width, cell_height)
            canvas.paste(tile, (x, y))
            draw.rectangle(
                (x, y + cell_height, x + cell_width, y + cell_height + label_height),
                fill="#000000",
            )
            draw.text(
                (x + 8, y + cell_height + 8),
                path.stem,
                fill="#ffffff",
                font=font,
            )

        output = output_dir / f"{episode_dir.name}_review_{page_index + 1:02d}.jpg"
        canvas.save(output, quality=92, subsampling=0)

    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--rows", type=int, default=3)
    parser.add_argument("--cell-width", type=int, default=800)
    parser.add_argument("--cell-height", type=int, default=450)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    total_pages = 0
    total_sheets = 0
    for episode_dir in sorted(path for path in args.root.glob("ep*" ) if path.is_dir()):
        sheets = list((episode_dir / "scene_index").glob("scene_*.jpg"))
        total_sheets += len(sheets)
        total_pages += build_episode(
            episode_dir,
            args.output,
            args.columns,
            args.rows,
            args.cell_width,
            args.cell_height,
        )

    print(f"Built {total_pages} review pages from {total_sheets} scene sheets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
