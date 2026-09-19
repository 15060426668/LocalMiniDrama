#!/usr/bin/env python3
"""Compile a Dream SD execution/master artifact into a target-model field order."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "references" / "model-output-profiles.json"
RANGE_RE = re.compile(r"第\s*(\d+)\s*[-~至]\s*(\d+)\s*秒[^\n]*")
FIELD_RE = re.compile(r"^([^：\n]{2,32})：\s*(.*)$")

# The first label in each list is the v6 owner. Remaining labels are
# compatibility-only inputs that are always recompiled into the five v6 fields.
FIELD_MAP = {
    "camera": [
        "镜头与构图",
        "景别/焦段/景深",
        "构图画面",
        "机位与运镜",
    ],
    "action": [
        "主体动作与表演",
        "镜头与主体动作",
        "画面内容",
    ],
    "relation_environment": [
        "关系/物件/环境反馈",
        "物件/环境/物理反馈",
        "分层运动与反馈",
        "运动生态/层级交互",
        "实拍摄影证据 / 生成可信证据",
        "实拍摄影证据/生成可信证据",
    ],
    "sound_light_transition": [
        "声光与转场触发",
        "声光与转场",
        "声音与声画触发",
        "声音设计",
        "光影/色彩/质感",
        "光影/色彩",
        "画面基调/质感",
        "转场",
    ],
    "tail": [
        "落点与继承",
        "尾帧与连续性",
        "镜间变化/尾帧",
        "SD承接锚点",
        "连续性校验",
    ],
}

OUTPUT_LABELS = {
    "camera": "镜头与构图",
    "action": "主体动作与表演",
    "relation_environment": "关系/物件/环境反馈",
    "sound_light_transition": "声光与转场触发",
    "tail": "尾帧与连续性",
}

ATTACHMENT_MARKERS = ("【制作审核附件", "【E区块", "【声音后期表", "【自审报告")


def first_attachment_start(text: str, start: int) -> int | None:
    positions = [text.find(marker, start) for marker in ATTACHMENT_MARKERS]
    positions = [position for position in positions if position != -1]
    return min(positions) if positions else None


def a_section(text: str) -> str:
    start = text.find("【A区块")
    if start == -1:
        raise ValueError("A section not found")
    end = first_attachment_start(text, start)
    return text[start:] if end is None else text[start:end]


def global_preamble(text: str) -> str:
    start = text.find("【A区块")
    if start == -1:
        raise ValueError("A section not found")
    return text[:start].strip()


def compile_base_lock(text: str) -> str:
    preamble = global_preamble(text)
    if not preamble:
        return "【BASE LOCK】"
    marker = "【BASE LOCK】"
    if marker in preamble:
        return preamble[preamble.index(marker) :].strip()
    flattened = re.sub(r"(?m)^【([^】]+)】\s*$", r"\1：", preamble).strip()
    return f"{marker}\n{flattened}"


def attachment_section(text: str) -> str:
    start = text.find("【A区块")
    if start == -1:
        return ""
    attachment_start = first_attachment_start(text, start)
    return "" if attachment_start is None else text[attachment_start:].strip()


def parse_segments(text: str) -> list[dict]:
    section = a_section(text)
    matches = list(RANGE_RE.finditer(section))
    segments = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[match.end() : end]
        fields: dict[str, str] = {}
        for raw_line in block.splitlines():
            line = raw_line.strip().strip("*")
            field_match = FIELD_RE.match(line)
            if field_match:
                fields[field_match.group(1).strip()] = field_match.group(2).strip()
        segments.append(
            {
                "heading": match.group(0).strip(),
                "start": int(match.group(1)),
                "end": int(match.group(2)),
                "fields": fields,
            }
        )
    if not segments:
        raise ValueError("A time segments not found")
    return segments


def collect(fields: dict[str, str], semantic: str) -> list[str]:
    values = []
    for field_name in FIELD_MAP.get(semantic, []):
        value = fields.get(field_name)
        if value and value not in values:
            values.append(value)
    return values


def compile_text(master: str, profile_name: str, profile_data: dict) -> str:
    segments = parse_segments(master)
    order = profile_data["field_order"]
    lines = [
        compile_base_lock(master),
        "",
        "【A区块·模型执行词】",
    ]
    known_fields = {field for aliases in FIELD_MAP.values() for field in aliases}
    for segment in segments:
        lines.append(segment["heading"])
        missing_semantics = []
        for semantic in order:
            values = collect(segment["fields"], semantic)
            if values:
                label = OUTPUT_LABELS.get(semantic, semantic)
                lines.append(f"{label}：{'；'.join(values)}")
            else:
                missing_semantics.append(OUTPUT_LABELS.get(semantic, semantic))
        if missing_semantics:
            raise ValueError(
                f"{segment['heading']} cannot compile the required v6 fields: "
                f"{', '.join(missing_semantics)}"
            )
        unknown = sorted(
            field_name
            for field_name, value in segment["fields"].items()
            if value and field_name not in known_fields
        )
        if unknown:
            raise ValueError(
                f"{segment['heading']} contains unmapped source fields: {', '.join(unknown)}"
            )
        lines.append("")
    if profile_data.get("include_attachments"):
        attachments = attachment_section(master)
        if attachments:
            lines.extend(
                [
                    "【PRODUCTION ATTACHMENTS｜OUTSIDE MODEL PAYLOAD】",
                    attachments,
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("master", type=Path)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    registry = json.loads(PROFILES.read_text(encoding="utf-8"))
    profiles = registry["profiles"]
    if args.profile not in profiles:
        raise SystemExit(f"unknown plain-text profile: {args.profile}")
    profile = dict(profiles[args.profile])
    if profile.get("output_format") != "plain_text":
        raise SystemExit(f"profile {args.profile} is not a permitted user-facing plain-text profile")
    profile["evidence_status"] = registry["evidence_status"]
    result = compile_text(args.master.read_text(encoding="utf-8"), args.profile, profile)
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
