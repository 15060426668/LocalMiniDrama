#!/usr/bin/env python3
"""Validate formal storyboards and Dream SD execution/master markdown output."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "references" / "runtime-contract.json"
RANGE_RE = re.compile(r"第?\s*(\d+)\s*[-~至]\s*(\d+)\s*秒")
A_HEADER_RE = re.compile(r"(?m)^\s*第?\s*(\d+)\s*[-~至]\s*(\d+)\s*秒(?:\s*[｜|].*)?\s*$")
DECIMAL_TIME_RE = re.compile(r"\d+\.\d+\s*秒", re.IGNORECASE)
SHOT_SOURCE_RE = re.compile(r"源镜头(?:号)?\s*[:：]?\s*([0-9A-Za-z._-]+)")

CAMERA_CATEGORIES = {
    "track": r"tracking|跟拍|跟随",
    "pan": r"\bpan\b|whip pan|摇镜|甩镜",
    "truck": r"truck|slide|横移|侧移",
    "dolly": r"dolly|push in|pull out|推近|拉远",
    "orbit": r"orbit|arc|环绕|弧形",
    "crane": r"crane|升降|摇臂",
    "handheld": r"handheld|手持",
    "focus": r"rack focus|focus pull|焦点交接|拉焦",
}
ACTION_CATEGORIES = {
    "run": r"奔跑|冲刺|逃跑|running|sprinting",
    "walk": r"行走|迈步|走向|walking",
    "turn": r"回头|转身|扭头|turning|look back",
    "fall": r"跌倒|摔倒|踉跄|falling|stumbling",
    "impact": r"碰撞|撞击|急停|刹车|impact|collision|brak",
    "handoff": r"递出|交还|交接|handoff|passes",
    "threshold": r"开门|关门|推门|拉门|door opens|door closes",
    "contact": r"扶腰|拥抱|接吻|抓住|握住|hug|kiss|grabs",
    "sit_stand": r"坐下|起身|站起|sit|stand",
    "speak": r"台词|口型|说出|喊出|whisper|speaks|dialogue",
}

ANIMATION_MARKER_RE = re.compile(
    r"动画|手绘|厚涂|二维|赛璐璐|定格关键帧|anime|animation|cel\s+animation",
    re.IGNORECASE,
)
USER_FACING_JSON_RE = re.compile(
    r"^\s*(?:```json\s*)?\{|\"performance_timeline\"\s*:|\"camera_phase_schedule\"\s*:",
    re.IGNORECASE,
)
LOCAL_ASSET_PATH_RE = re.compile(
    r"(?:[A-Za-z]:[\\/]|file://|(?:^|\s)/(?:Users|home|mnt|tmp|var|opt|workspace)/)",
    re.IGNORECASE | re.MULTILINE,
)
HIGH_INTENSITY_ACTION_RE = re.compile(
    r"冲锋|冲刺|奔跑|跃|跳|坠|扑|砍|挥|刺|格挡|撞|翻越|翻滚|滑过|追赶|"
    r"击|抓|撕|踢|攻击|打斗|闪避|躲开|急停"
)
SUBJECT_PERFORMANCE_DIMENSIONS = {
    "sequence": r"先|随后|接着|再|同时|最后|瞬间|之后|继而|->|→",
    "body_mechanics": r"重心|支点|肩|肘|腕|脊柱|腰|胯|髋|膝|脚|足|胸|背|颈",
    "force_or_speed": r"发力|压低|蹬|踩|踏|推|拉|挥|甩|撞|冲|加速|减速|急停|突然|缓慢|步幅|速度|惯性|借力",
    "contact_or_consequence": r"接触|碰|撞|击|抓|扣|压|挡|格|刺|砍|撕|弹|震|滑|失衡|后仰|回弹|拖|反作用|阻力",
    "recovery_or_landing": r"落定|落地|停住|停在|站稳|恢复|归模|收回|支撑|尾帧|定住|稳住",
    "intent_or_expression": r"视线|眼|眉|嘴|呼吸|表情|咬牙|注视|锁定",
    "face_body_synchronization": r"视线|眼|眉|嘴|呼吸|表情|咬牙|注视|锁定|吞咽|眨眼",
    "secondary_motion_or_material": r"衣|发|裙摆|布料|道具|剑|枪|纸|碎片|雪块|尘|雨|延迟|慢半拍|震颤|材质",
    "reaction_or_environment_relay": r"对手|敌人|听者|NPC|路人|人群|环境|背景|地面|窗|树|物件.{0,8}(?:响应|反应|继续|延迟)|后仰|滑动",
    "sound_or_light_cue": r"声|静音|重音|尾音|声桥|光|闪|阴影|曝光|色温|触发",
}

SUPPLEMENTAL_PERFORMANCE_DIMENSIONS = {
    "secondary_motion_or_material",
    "reaction_or_environment_relay",
    "sound_or_light_cue",
}

PERCEPTUAL_SOUND_RE = re.compile(
    r"声|呼吸|脚步|台词|静默|音乐|撞击|摩擦|水|风|门|玻璃|耳压|"
    r"说|喊|问|答|念|低语|金属|刀|锅|炉|木|铃|钟|气泡|咕嘟|嘶|破风|碰响|跳响|爆响"
)

SOUND_MARKERS = {
    "主声源": r"主声源|primary\s+source",
    "启用总线": r"\b(?:ENV|BODY|OBJ|VOX|FX|INT|MUS)\b",
    "RMS dBFS": r"RMS\s*dBFS",
    "peak dBFS": r"peak\s*dBFS",
    "相对电平": r"相对(?:主声源)?|relative\s*(?:level|dB)",
    "空间处理": r"RT60|dry.?wet|遮挡|occlusion|LPF|HPF|混响",
    "闪避/掩蔽": r"闪避|掩蔽|duck|mask",
    "镜头响度": r"LUFS-S",
    "母版响度": r"LUFS-I",
    "真峰值": r"dBTP",
    "声画反应": r"触发|可见反应|visible\s+reaction",
    "尾音/声桥": r"声桥|尾音|J-cut|L-cut|延续到下一镜|tail\s+bridge",
}


@dataclass
class Finding:
    level: str
    message: str


def normalize_cell(value: str) -> str:
    return re.sub(r"\s+", "", value.strip().replace("`", ""))


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    cells = split_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0
    while index + 1 < len(lines):
        if lines[index].lstrip().startswith("|") and is_separator(lines[index + 1]):
            header = split_row(lines[index])
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                row = split_row(lines[index])
                if len(row) < len(header):
                    row.extend([""] * (len(header) - len(row)))
                rows.append(row[: len(header)])
                index += 1
            tables.append((header, rows))
            continue
        index += 1
    return tables


def parse_duration_seconds(value: str) -> int | None:
    if DECIMAL_TIME_RE.search(value):
        return None
    range_match = RANGE_RE.search(value)
    if range_match:
        return int(range_match.group(2)) - int(range_match.group(1))
    match = re.search(r"(?<![.\d])(\d+)\s*(?:秒|s\b)", value, re.IGNORECASE)
    if match:
        return int(match.group(1))
    if value.strip().isdigit():
        return int(value.strip())
    return None


def validate_metered_sound(value: str, owner: str) -> list[Finding]:
    findings: list[Finding] = []
    missing = [label for label, pattern in SOUND_MARKERS.items() if not re.search(pattern, value, re.IGNORECASE)]
    if missing:
        findings.append(Finding("ERROR", f"{owner}声音设计缺少可执行计量项: {', '.join(missing)}"))
    for bare_db in re.finditer(r"-?\d+(?:\.\d+)?\s*dB(?!FS|TP)", value, re.IGNORECASE):
        context = value[max(0, bare_db.start() - 16) : bare_db.end() + 16]
        if re.search(r"相对|闪避|掩蔽|duck|mask|余量|headroom", context, re.IGNORECASE):
            continue
        findings.append(Finding("ERROR", f"{owner}声音设计存在未声明口径的dB值: {bare_db.group(0)}"))
        break
    return findings


def validate_perceptual_sound(value: str, owner: str) -> list[Finding]:
    findings: list[Finding] = []
    if len(normalize_cell(value)) < 8:
        return [Finding("ERROR", f"{owner}声音与声画触发过于空泛。")]
    if not PERCEPTUAL_SOUND_RE.search(value):
        findings.append(Finding("ERROR", f"{owner}未写明具体可听声源。"))
    if not re.search(r"左|右|前|后|近|远|中央|上方|下方|画内|画外|主观|方向|距离|贴近|来自", value):
        findings.append(Finding("WARNING", f"{owner}未写明声源方位、距离或主观权限。"))
    if not re.search(r"触发|反应|转场|剪|衰减|延续|进入|落点|尾音|声桥|J-cut|L-cut|回头|抬眼|僵|动作", value, re.IGNORECASE):
        findings.append(Finding("WARNING", f"{owner}未写明可见反应、剪点或尾音声桥。"))
    return findings


def validate_subject_performance(
    value: str,
    owner: str,
    gate: dict,
    context: str = "",
    relation_context: str = "",
    tail_context: str = "",
) -> list[Finding]:
    if not gate.get("enabled", False):
        return []
    if gate.get("high_intensity_only", True) and not HIGH_INTENSITY_ACTION_RE.search(value):
        return []

    findings: list[Finding] = []
    severity = str(gate.get("summary_action_severity", "ERROR"))
    character_count = len(normalize_cell(value))
    minimum_characters = int(gate.get("minimum_characters", 80))
    if character_count < minimum_characters:
        findings.append(
            Finding(
                severity,
                f"{owner}主体动作与表演仅{character_count}字，未展开高强度动作的完整姿势链。",
            )
        )

    dimensions = {
        name
        for name, pattern in SUBJECT_PERFORMANCE_DIMENSIONS.items()
        if re.search(pattern, value, re.IGNORECASE)
    }
    if context:
        dimensions.update(
            name
            for name in SUPPLEMENTAL_PERFORMANCE_DIMENSIONS
            if re.search(SUBJECT_PERFORMANCE_DIMENSIONS[name], context, re.IGNORECASE)
        )
    if len(normalize_cell(relation_context)) >= 16 and re.search(
        r"震|摆|晃|落|停|抬|转|移|散|冒|滴|弹|回|变|增|减|推|卷|掠|延迟|"
        r"慢半拍|继续|维持|保持|触发|压|稳|受|被|使",
        relation_context,
    ):
        dimensions.add("reaction_or_environment_relay")
    # The v6 five-field schema assigns an inheritable result to the tail field.
    # Count that owned field instead of forcing a duplicate recovery sentence
    # into the subject-performance field.
    if normalize_cell(tail_context):
        dimensions.add("recovery_or_landing")
    mandatory = set(gate.get("mandatory_dimensions", []))
    missing_mandatory = sorted(mandatory - dimensions)
    if missing_mandatory:
        findings.append(
            Finding(severity, f"{owner}主体动作与表演缺少硬维度: {', '.join(missing_mandatory)}")
        )
    minimum_dimensions = int(gate.get("minimum_dimensions", 4))
    if len(dimensions) < minimum_dimensions:
        findings.append(
            Finding(
                severity,
                f"{owner}主体动作与表演仅覆盖{len(dimensions)}个执行维度，至少需要{minimum_dimensions}个。",
            )
        )
    return findings


def find_storyboard_table(text: str, required_fields: list[str]):
    required = {normalize_cell(field) for field in required_fields}
    best = None
    best_score = -1
    for header, rows in parse_tables(text):
        normalized = {normalize_cell(cell) for cell in header}
        score = len(required & normalized)
        if score > best_score:
            best = (header, rows)
            best_score = score
    return best, best_score


def validate_storyboard(text: str, contract: dict, require_sd_anchor: bool) -> list[Finding]:
    findings: list[Finding] = []
    live_required = list(contract["formal_storyboard_fields"])
    if require_sd_anchor:
        live_required.append("SD承接锚点")
    animation_required = list(contract.get("animation_formal_storyboard_fields", []))

    live_table, live_score = find_storyboard_table(text, live_required)
    animation_table, animation_score = find_storyboard_table(text, animation_required)
    is_animation = bool(animation_required) and (
        animation_score > live_score or (ANIMATION_MARKER_RE.search(text) and animation_score >= 4)
    )
    required = animation_required if is_animation else live_required
    table = animation_table if is_animation else live_table
    score = animation_score if is_animation else live_score
    minimum_score = 4 if is_animation else 5
    if not table or score < minimum_score:
        return [Finding("ERROR", "未找到正式分镜表。")]

    header, rows = table
    normalized_header = {normalize_cell(cell): index for index, cell in enumerate(header)}
    missing = [field for field in required if normalize_cell(field) not in normalized_header]
    if missing:
        findings.append(Finding("ERROR", f"正式分镜缺少字段: {', '.join(missing)}"))

    duration_index = normalized_header.get(
        normalize_cell("镜号与整秒时间" if is_animation else "时长")
    )
    camera_index = normalized_header.get(
        normalize_cell("镜头与构图" if is_animation else "机位与运镜")
    )
    content_index = normalized_header.get(
        normalize_cell("主体与关系表演" if is_animation else "画面内容")
    )
    sound_index = normalized_header.get(
        normalize_cell("声音与台词" if is_animation else "声音设计")
    )
    refresh_limit = int(contract["timing"]["fixed_shot_refresh_max_seconds"])

    if not rows:
        findings.append(Finding("ERROR", "正式分镜表没有镜头行。"))
        return findings

    for row_number, row in enumerate(rows, start=1):
        if duration_index is None or duration_index >= len(row):
            continue
        duration_text = row[duration_index]
        if DECIMAL_TIME_RE.search(duration_text):
            findings.append(Finding("ERROR", f"镜头行{row_number}使用了非整秒时长: {duration_text}"))
            continue
        duration = parse_duration_seconds(duration_text)
        if duration is None or duration <= 0:
            findings.append(Finding("ERROR", f"镜头行{row_number}时长无法识别: {duration_text}"))
            continue

        camera = row[camera_index] if camera_index is not None and camera_index < len(row) else ""
        content = row[content_index] if content_index is not None and content_index < len(row) else ""
        sound = row[sound_index] if sound_index is not None and sound_index < len(row) else ""
        fixed = re.search(r"固定|locked|static", camera, re.IGNORECASE)
        internal_refresh = re.search(r"\d+\s*[-~至]\s*\d+|焦点|灯光|前景|声音|重新构图|reframe", content)
        if fixed and duration > refresh_limit and not internal_refresh:
            findings.append(
                Finding(
                    "WARNING",
                    f"镜头行{row_number}为{duration}秒固定机位，但未发现1-{refresh_limit}秒内的信息刷新证据。",
                )
            )

        if sound:
            if is_animation:
                findings.extend(validate_perceptual_sound(sound, f"镜头行{row_number}"))
            else:
                findings.extend(validate_metered_sound(sound, f"镜头行{row_number}"))

        for field, index in normalized_header.items():
            if index < len(row) and not row[index].strip():
                findings.append(Finding("ERROR", f"镜头行{row_number}字段为空: {header[index]}"))

    return findings


def extract_a_section(text: str) -> str:
    start = text.find("【A区块")
    if start == -1:
        return text
    end_positions = [
        text.find(marker, start)
        for marker in ("【制作审核附件", "【E区块", "【声音后期表", "【自审报告")
    ]
    end_positions = [position for position in end_positions if position != -1]
    end = min(end_positions) if end_positions else -1
    return text[start:] if end == -1 else text[start:end]


def mask_quoted_dialogue(text: str) -> str:
    """Remove approved spoken lines before scanning prompt-writing constraints."""
    return re.sub(r'[“"][^”"\n]*[”"]', "", text)


def split_a_segments(a_text: str) -> list[tuple[tuple[int, int], str]]:
    matches = list(A_HEADER_RE.finditer(a_text))
    segments: list[tuple[tuple[int, int], str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(a_text)
        segments.append(((int(match.group(1)), int(match.group(2))), a_text[match.start() : end]))
    return segments


def complexity_score(block: str) -> dict:
    camera = [name for name, pattern in CAMERA_CATEGORIES.items() if re.search(pattern, block, re.IGNORECASE)]
    actions = [name for name, pattern in ACTION_CATEGORIES.items() if re.search(pattern, block, re.IGNORECASE)]
    vfx = len(
        {
            name
            for name, pattern in {
                "liquid": r"液体|融化|水化",
                "fragment": r"碎裂|碎块|破碎",
                "particle": r"颗粒化|化为颗粒|颗粒聚合|风沙|粉尘聚合",
                "smoke": r"烟雾|气化|雾化",
                "digital": r"故障|花屏|乱码|刷新",
                "fold": r"折叠|翻折|镜像翻转",
                "morph": r"变形|重组|凝结|生长",
            }.items()
            if re.search(pattern, block, re.IGNORECASE)
        }
    )
    transition_count = len(re.findall(r"match cut|遮挡转场|甩镜转场|匹配剪辑|动作匹配|空间转场", block, re.IGNORECASE))
    score = len(camera) + len(actions) + min(vfx, 2) * 2 + min(transition_count, 2)
    return {
        "score": score,
        "camera_categories": camera,
        "action_categories": actions,
        "vfx_families": vfx,
        "transition_markers": transition_count,
    }


def parse_e_ranges(text: str) -> list[tuple[int, int]]:
    e_start = text.find("【E区块")
    if e_start == -1:
        return []
    ranges: list[tuple[int, int]] = []
    for header, rows in parse_tables(text[e_start:]):
        normalized = [normalize_cell(cell) for cell in header]
        if normalize_cell("时间") not in normalized:
            continue
        time_index = normalized.index(normalize_cell("时间"))
        for row in rows:
            if time_index >= len(row):
                continue
            match = RANGE_RE.search(row[time_index])
            if match:
                ranges.append((int(match.group(1)), int(match.group(2))))
        break
    return ranges


def validate_sd(
    text: str,
    contract: dict,
    strict_complexity: bool = False,
    require_e: bool = False,
) -> list[Finding]:
    findings: list[Finding] = []
    if USER_FACING_JSON_RE.search(text):
        findings.append(Finding("ERROR", "用户侧SD交付必须使用纯文本BASE LOCK+A，禁止JSON载荷。"))
    if LOCAL_ASSET_PATH_RE.search(text):
        findings.append(
            Finding(
                "ERROR",
                "用户侧SD载荷含本地文件路径；请转换为模型可见的参考图/附件槽位名。",
            )
        )
    base_count = text.count("【BASE LOCK】")
    if base_count > 1:
        findings.append(Finding("ERROR", f"单条SD提示词出现{base_count}个BASE LOCK；4-30秒整段只能有一个。"))
    a_text = extract_a_section(text)
    if DECIMAL_TIME_RE.search(a_text):
        findings.append(Finding("ERROR", "A区块出现非整秒时间。"))

    forbidden = contract["positive_only_forbidden_phrases"]
    lowered = f" {mask_quoted_dialogue(a_text).lower()} "
    for phrase in forbidden:
        target = phrase.lower()
        if target in lowered:
            findings.append(Finding("ERROR", f"A区块出现非正向表达: {phrase.strip()}"))

    segments = split_a_segments(a_text)
    if not segments:
        return findings + [Finding("ERROR", "未找到A区块整秒时间段。")]

    max_seconds = int(contract["timing"]["sd_segment_max_seconds"])
    execution_labels = list(contract["sd_a_fields"])
    compatibility_labels = list(contract.get("compatibility_sd_a_fields", []))
    legacy_labels = list(contract.get("legacy_sd_a_fields", []))
    animation_schema = contract.get("sd_animation_a_fields", {})
    animation_required = list(animation_schema.get("required", []))
    animation_optional = list(animation_schema.get("optional", []))
    animation_labels = animation_required + animation_optional
    is_animation_prompt = bool(ANIMATION_MARKER_RE.search(text))
    performance_gate = contract.get("subject_performance_detail_gate", {})
    previous_end = None
    a_ranges: list[tuple[int, int]] = []
    total_duration = 0

    for index, ((start, end), block) in enumerate(segments, start=1):
        a_ranges.append((start, end))
        if end <= start:
            findings.append(Finding("ERROR", f"A段{index}时间范围无效: {start}-{end}秒"))
        else:
            total_duration += end - start
        if end - start > max_seconds:
            findings.append(Finding("ERROR", f"A段{index}超过{max_seconds}秒: {start}-{end}秒"))
        if previous_end is not None and start != previous_end:
            findings.append(Finding("ERROR", f"A段{index}与前段不连续: 前段止于{previous_end}秒，本段始于{start}秒"))
        previous_end = end

        if animation_labels and (
            "关系/物件/环境反馈" in block
            or "声光与转场触发" in block
            or (is_animation_prompt and sum(label in block for label in animation_labels) >= 4)
        ):
            schema_name = "animation_text_v6"
            required_labels = animation_required
        else:
            execution_hits = sum(label in block for label in execution_labels)
            compatibility_hits = sum(label in block for label in compatibility_labels)
            legacy_hits = sum(label in block for label in legacy_labels)
            if execution_hits >= max(compatibility_hits, legacy_hits):
                schema_name = "animation_text_v6"
                required_labels = execution_labels
            elif compatibility_hits >= legacy_hits:
                schema_name = "execution_expanded"
                required_labels = compatibility_labels
            else:
                schema_name = "legacy"
                required_labels = legacy_labels
        missing = [label for label in required_labels if label not in block]
        if missing:
            findings.append(Finding("ERROR", f"A段{index}缺少字段: {', '.join(missing)}"))

        if schema_name == "animation_text_v6":
            sound_match = re.search(
                r"声光与转场触发：\s*(.*?)(?=\n尾帧与连续性：|\Z)",
                block,
                re.DOTALL,
            )
            if sound_match:
                findings.extend(validate_perceptual_sound(sound_match.group(1), f"A段{index}"))
            else:
                findings.append(Finding("ERROR", f"A段{index}未找到可解析的声光与转场触发字段。"))
        else:
            sound_label = "声音与声画触发" if schema_name == "execution_expanded" else "声音设计"
            tail_labels = "转场|尾帧与连续性|镜间变化/尾帧|SD承接锚点|连续性校验"
            sound_match = re.search(
                rf"{re.escape(sound_label)}：\s*(.*?)(?=\n(?:{tail_labels})：|\Z)",
                block,
                re.DOTALL,
            )
            if sound_match:
                if schema_name == "execution_expanded":
                    findings.extend(validate_perceptual_sound(sound_match.group(1), f"A段{index}"))
                else:
                    findings.extend(validate_metered_sound(sound_match.group(1), f"A段{index}"))
            else:
                findings.append(Finding("ERROR", f"A段{index}未找到可解析的{sound_label}字段。"))

        if schema_name == "animation_text_v6" and is_animation_prompt:
            action_match = re.search(
                r"主体动作与表演：\s*(.*?)(?=\n(?:关系/物件/环境反馈|声光与转场触发|尾帧与连续性)：|\Z)",
                block,
                re.DOTALL,
            )
            relation_match = re.search(
                r"关系/物件/环境反馈：\s*(.*?)(?=\n(?:声光与转场触发|尾帧与连续性)：|\Z)",
                block,
                re.DOTALL,
            )
            tail_match = re.search(
                r"尾帧与连续性：\s*(.*?)(?=\Z)",
                block,
                re.DOTALL,
            )
            if action_match:
                relation_context = relation_match.group(1) if relation_match else ""
                supporting_context = "\n".join(
                    match.group(1)
                    for match in (relation_match, sound_match)
                    if match is not None
                )
                findings.extend(
                    validate_subject_performance(
                        action_match.group(1),
                        f"A段{index}",
                        performance_gate,
                        context=supporting_context,
                        relation_context=relation_context,
                        tail_context=tail_match.group(1) if tail_match else "",
                    )
                )

        load = complexity_score(block)
        level = "ERROR" if strict_complexity and load["score"] >= contract["complexity"]["split_min"] else "WARNING"
        if load["score"] >= contract["complexity"]["split_min"]:
            findings.append(
                Finding(
                    level,
                    f"A段{index}复杂度预计为{load['score']}，达到拆段线；"
                    f"camera={load['camera_categories']}, actions={load['action_categories']}, "
                    f"vfx={load['vfx_families']}, transitions={load['transition_markers']}",
                )
            )
        if len(load["camera_categories"]) >= contract["complexity"]["always_split_camera_paths"]:
            findings.append(
                Finding(
                    level,
                    f"A段{index}检测到多类摄影机操作: {', '.join(load['camera_categories'])}",
                )
            )

    if total_duration > max_seconds:
        findings.append(
            Finding(
                "ERROR",
                f"单个用户可见提示词的A区块总时长为{total_duration}秒，超过{max_seconds}秒上限；"
                "内部A节拍可以连续拆分，但超出上限后必须进入下一条提示词。",
            )
        )

    if 16 <= total_duration <= max_seconds:
        refresh_start, refresh_end = contract["timing"]["animation_midpoint_refresh_window_seconds"]
        boundaries = {point for start, end in a_ranges for point in (start, end)}
        if not any(refresh_start <= point <= refresh_end for point in boundaries):
            findings.append(
                Finding(
                    "WARNING",
                    f"{total_duration}秒长段在{refresh_start}-{refresh_end}秒附近没有A拍边界；"
                    "请确认中段信息/状态刷新已在跨窗A拍内明确执行。",
                )
            )

    e_ranges = parse_e_ranges(text)
    if require_e and not e_ranges:
        findings.append(Finding("ERROR", "未找到可解析的E区块时间表。"))
    elif e_ranges and e_ranges != a_ranges:
        findings.append(Finding("ERROR", f"A/E时间不一致: A={a_ranges}, E={e_ranges}"))
    if (
        e_ranges
        and "【A区块·模型执行词" in text
        and "【制作审核附件" not in text
    ):
        findings.append(Finding("ERROR", "E区块必须置于“制作审核附件”中，不能混入模型执行载荷。"))

    return findings


def source_storyboard_rows(text: str, contract: dict) -> list[dict]:
    live_required = list(contract["formal_storyboard_fields"])
    animation_required = list(contract.get("animation_formal_storyboard_fields", []))
    live_table, live_score = find_storyboard_table(text, live_required)
    animation_table, animation_score = find_storyboard_table(text, animation_required)
    if animation_required and animation_score > live_score:
        table, score, shot_field = animation_table, animation_score, "镜号与整秒时间"
        minimum_score = 4
    else:
        table, score, shot_field = live_table, live_score, "镜头"
        minimum_score = 5
    if not table or score < minimum_score:
        return []
    header, rows = table
    normalized = [normalize_cell(cell) for cell in header]
    shot_key = normalize_cell(shot_field)
    if shot_key not in normalized:
        return []
    shot_index = normalized.index(shot_key)
    anchor_index = normalized.index(normalize_cell("SD承接锚点")) if normalize_cell("SD承接锚点") in normalized else None
    result = []
    for row in rows:
        if shot_index >= len(row) or not row[shot_index].strip():
            continue
        raw_id = row[shot_index].strip()
        id_match = re.match(r"([0-9A-Za-z._-]+)", raw_id)
        shot_id = id_match.group(1) if id_match else raw_id
        anchors = row[anchor_index].strip() if anchor_index is not None and anchor_index < len(row) else ""
        result.append({"id": shot_id, "anchors": anchors})
    return result


def validate_source_mapping(
    source_text: str,
    sd_text: str,
    contract: dict,
    strict_source_coverage: bool = True,
) -> list[Finding]:
    source_rows = source_storyboard_rows(source_text, contract)
    if not source_rows:
        return [Finding("ERROR", "源分镜中未找到可映射的镜头号。")]
    a_text = extract_a_section(sd_text)
    mapped_ids = set(SHOT_SOURCE_RE.findall(a_text))
    missing = [row["id"] for row in source_rows if row["id"] not in mapped_ids]
    findings = []
    if missing:
        findings.append(Finding("ERROR", f"源分镜镜头未映射到A区块: {', '.join(missing)}"))

    blocks_by_id = {}
    for _, block in split_a_segments(a_text):
        match = SHOT_SOURCE_RE.search(block)
        if match:
            blocks_by_id.setdefault(match.group(1), "")
            blocks_by_id[match.group(1)] += block
    for row in source_rows:
        anchor_terms = [
            normalize_cell(term)
            for term in re.split(r"[、,，;；/|]", row["anchors"])
            if len(normalize_cell(term)) >= 2
        ]
        if not anchor_terms or row["id"] not in blocks_by_id:
            continue
        normalized_block = normalize_cell(blocks_by_id[row["id"]])
        hits = [term for term in anchor_terms if term in normalized_block]
        coverage = len(hits) / len(anchor_terms)
        minimum_coverage = 1.0 if strict_source_coverage else 0.5
        if coverage < minimum_coverage:
            level = "ERROR" if strict_source_coverage else "WARNING"
            findings.append(
                Finding(
                    level,
                    f"源镜头{row['id']}的SD承接锚点覆盖率为{coverage:.0%}，"
                    f"要求至少{minimum_coverage:.0%}: "
                    f"命中{hits}, 源锚点{anchor_terms}",
                )
            )
    return findings


def validate_continuity_manifest(manifest: dict, sd_text: str, contract: dict) -> list[Finding]:
    findings = []
    missing_keys = [key for key in contract["continuity_manifest_required"] if key not in manifest]
    if missing_keys:
        findings.append(Finding("ERROR", f"连续性清单缺少字段: {', '.join(missing_keys)}"))
        return findings
    normalized_text = normalize_cell(sd_text)
    missing_anchors = [
        anchor
        for anchor in manifest.get("fragile_anchors", [])
        if normalize_cell(str(anchor)) not in normalized_text
    ]
    if missing_anchors:
        findings.append(Finding("ERROR", f"连续性脆弱锚点未进入SD输出: {', '.join(missing_anchors)}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--mode", choices=("auto", "storyboard", "sd"), default="auto")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--require-sd-anchor", action="store_true")
    parser.add_argument("--source-storyboard", type=Path)
    parser.add_argument("--continuity-manifest", type=Path)
    parser.add_argument("--strict-complexity", action="store_true")
    parser.add_argument(
        "--strict-source-coverage",
        action="store_true",
        default=True,
        help="Require 100%% source-anchor coverage (default).",
    )
    parser.add_argument(
        "--allow-partial-source-coverage",
        action="store_false",
        dest="strict_source_coverage",
        help="Diagnostic opt-out: downgrade coverage below 100%% to a warning.",
    )
    parser.add_argument("--require-e", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    mode = args.mode
    if mode == "auto":
        mode = "sd" if "【A区块" in text or "【E区块" in text else "storyboard"

    findings = (
        validate_storyboard(text, contract, args.require_sd_anchor)
        if mode == "storyboard"
        else validate_sd(text, contract, args.strict_complexity, args.require_e)
    )
    if mode == "sd" and args.source_storyboard:
        source_text = args.source_storyboard.read_text(encoding="utf-8")
        findings.extend(
            validate_source_mapping(
                source_text,
                text,
                contract,
                args.strict_source_coverage,
            )
        )
    if mode == "sd" and args.continuity_manifest:
        manifest = json.loads(args.continuity_manifest.read_text(encoding="utf-8"))
        findings.extend(validate_continuity_manifest(manifest, text, contract))
    errors = [finding for finding in findings if finding.level == "ERROR"]

    if args.as_json:
        print(
            json.dumps(
                {
                    "path": str(args.path),
                    "mode": mode,
                    "ok": not errors,
                    "findings": [finding.__dict__ for finding in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"[{mode}] {args.path}")
        if not findings:
            print("PASS")
        for finding in findings:
            print(f"{finding.level}: {finding.message}")
        print("PASS" if not errors else "FAIL")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
