#!/usr/bin/env python3
"""Validate static image-generation prompts for this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


VIDEO_PATTERNS = {
    "timeline seconds": r"(?:第\s*\d+\s*[-至到]\s*\d+\s*秒|\b\d+\s*[-–]\s*\d+\s*seconds?\b)",
    "SD block": r"(?:BASE\s*LOCK|A区块|E区块|SD输出|Seedance)",
    "camera movement": r"(?:运镜|镜头运动|camera\s+(?:moves?|movement|path)|dolly\s+(?:in|out)|tracking\s+shot|whip\s+pan)",
    "transition": r"(?:转场|尾帧|下一镜|transition\s+to|tail\s+frame)",
}

NAME_STYLE_PATTERNS = {
    "style-of phrase": r"\b(?:in\s+the\s+style\s+of|inspired\s+by|\w+[\s-]style)\b",
    "Chinese named-style phrase": r"(?:模仿|仿照|致敬|同款|风格像|风格的|式画风)",
}

STATIC_SIGNALS = {
    "subject": ("subject", "subjects", "character", "child", "girl", "boy", "人物", "角色", "女孩", "男孩", "孩子"),
    "composition": ("composition", "foreground", "midground", "background", "close-up", "wide frame", "构图", "前景", "中景", "背景", "近景", "特写"),
    "linework": ("linework", "outline", "charcoal line", "hand-drawn", "线稿", "轮廓线", "手绘"),
    "shading": ("cel shading", "cel-shaded", "shadow", "hatching", "赛璐璐", "阴影", "排线"),
    "color": ("color", "palette", "cyan", "green", "grey", "pink", "色彩", "配色", "青", "绿", "灰", "粉"),
    "texture": ("paper grain", "grain", "painted background", "texture", "纸面颗粒", "颗粒", "背景绘制", "质感"),
}


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt is not None:
        return args.prompt.strip()
    return Path(args.file).read_text(encoding="utf-8").strip()


def validate(prompt: str, forbidden_terms: list[str]) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    if not prompt:
        return {"ok": False, "errors": ["Prompt is empty."], "warnings": []}

    lower = prompt.lower()

    for label, pattern in VIDEO_PATTERNS.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            errors.append(f"Video/storyboard leakage detected: {label}.")

    for label, pattern in NAME_STYLE_PATTERNS.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            errors.append(f"Named-style language detected: {label}.")

    for term in forbidden_terms:
        term = term.strip()
        if term and term.lower() in lower:
            errors.append(f"Forbidden source term appears in prompt: {term}")

    if re.search(r"(?:^|\s)--(?:v|ar|s|c|no|raw)\b", prompt, re.IGNORECASE):
        errors.append("Midjourney parameter syntax detected in an image_gen prompt.")

    present_signals: list[str] = []
    for label, terms in STATIC_SIGNALS.items():
        if any(term.lower() in lower for term in terms):
            present_signals.append(label)
        else:
            warnings.append(f"Missing or weak static-image layer: {label}.")

    if not re.search(r"(?:exactly\s+\d+|one\s+|two\s+|three\s+|four\s+|five\s+|six\s+|恰好\s*[一二三四五六七八九十\d]+|[一二三四五六七八九十\d]+名|一个|两名)", prompt, re.IGNORECASE):
        warnings.append("Subject count may be ambiguous.")

    if re.search(r"\b(?:glossy\s+3d|photorealistic\s+skin|ultra\s+realistic\s+skin)\b", lower):
        warnings.append("The prompt may conflict with the matte hand-drawn cel baseline.")

    word_count = len(re.findall(r"\b[\w'-]+\b", prompt))
    if word_count > 500:
        warnings.append(f"Prompt is long ({word_count} word-like tokens); consider compression.")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "signals": present_signals,
        "word_count": word_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt", help="Prompt text to validate.")
    source.add_argument("--file", help="UTF-8 file containing the prompt.")
    parser.add_argument(
        "--forbidden-term",
        action="append",
        default=[],
        help="Source name that must not appear in the model prompt. Repeat as needed.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    result = validate(read_prompt(args), args.forbidden_term)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["ok"] else "FAIL")
        print(f"word_count={result['word_count']}")
        for item in result["errors"]:
            print(f"ERROR: {item}")
        for item in result["warnings"]:
            print(f"WARNING: {item}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
