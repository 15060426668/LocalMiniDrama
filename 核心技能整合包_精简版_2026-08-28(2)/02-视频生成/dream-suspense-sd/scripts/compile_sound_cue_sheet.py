#!/usr/bin/env python3
"""Compile Dream SD A blocks into a post-production sound cue sheet."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from calculate_sound_mix import analyze_manifest, render_markdown

import json


RANGE_RE = re.compile(r"第\s*(\d+)\s*[-~至]\s*(\d+)\s*秒[^\n]*")
FIELD_RE = re.compile(r"^([^：\n]{2,32})：\s*(.*)$")


def collect_unique(fields: dict[str, str], names: tuple[str, ...]) -> str:
    values = []
    for name in names:
        value = fields.get(name, "")
        if value and value not in values:
            values.append(value)
    return "；".join(values)


def parse(text: str) -> list[dict]:
    start = text.find("【A区块")
    end_positions = [
        text.find(marker, start)
        for marker in ("【制作审核附件", "【E区块", "【声音后期表", "【自审报告")
    ]
    end_positions = [position for position in end_positions if position != -1]
    end = min(end_positions) if end_positions else -1
    section = text[start:] if end == -1 else text[start:end]
    matches = list(RANGE_RE.finditer(section))
    rows = []
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        fields = {}
        for raw in section[match.end() : block_end].splitlines():
            line = raw.strip().strip("*")
            field = FIELD_RE.match(line)
            if field:
                fields[field.group(1).strip()] = field.group(2).strip()
        shot = re.search(r"源镜头(?:号)?\s*[:：]?\s*([0-9A-Za-z._-]+)", match.group(0))
        rows.append(
            {
                "time": f"{match.group(1)}-{match.group(2)}秒",
                "shot": shot.group(1) if shot else "",
                "sound": collect_unique(
                    fields,
                    ("声光与转场触发", "声光与转场", "声音与声画触发", "声音设计"),
                ),
                "reaction": collect_unique(
                    fields,
                    (
                        "主体动作与表演",
                        "关系/物件/环境反馈",
                        "镜头与主体动作",
                        "分层运动与反馈",
                        "物件/环境/物理反馈",
                        "运动生态/层级交互",
                        "画面内容",
                    ),
                ),
                "bridge": collect_unique(
                    fields,
                    ("声光与转场触发", "声光与转场", "转场"),
                ),
                "tail": fields.get("落点与继承", "") or fields.get("尾帧与连续性", "") or fields.get("镜间变化/尾帧", ""),
            }
        )
    return rows


def escape(value: str) -> str:
    return value.replace("|", "｜").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("master", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mix-manifest", type=Path)
    args = parser.parse_args()

    rows = parse(args.master.read_text(encoding="utf-8"))
    if not rows:
        raise SystemExit("A segments not found")
    lines = [
        "| 时间 | 源镜头 | 声音设计 | 可见反应/声画触发 | 转场/声桥 | 尾帧状态 |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(escape(row[key]) for key in ("time", "shot", "sound", "reaction", "bridge", "tail")) + " |"
        )
    payload = "\n".join(lines) + "\n"
    if args.mix_manifest:
        report = analyze_manifest(json.loads(args.mix_manifest.read_text(encoding="utf-8")))
        payload += "\n" + render_markdown(report)
        if report["status"] != "pass":
            raise SystemExit("sound mix manifest validation failed")
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
