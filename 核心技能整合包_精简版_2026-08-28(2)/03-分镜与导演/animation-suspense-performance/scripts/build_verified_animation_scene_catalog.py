#!/usr/bin/env python3
"""Build the broad 214-sheet animation scene catalog used before source rescans."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = SKILL_ROOT.parents[1]
FRAME_ROOT = WORKSPACE / "research" / "星空兔的救赎" / "takopi_full"
OUTPUT = SKILL_ROOT / "references" / "verified-animation-scene-catalog.json"
SCENE_RE = re.compile(r"scene_(\d{4})_(\d{2})\.jpg$")


CATEGORY_DEFS = {
    "classroom_group": {
        "label": "教室与群体关系",
        "aliases": ["教室", "课堂", "班级", "课桌", "同学", "群体注视", "全班转头", "孤立", "排斥", "站位拓扑"],
    },
    "threshold_door": {
        "label": "门与阈限",
        "aliases": ["开门", "关门", "门板", "拉门", "滑门", "门框", "门缝", "门槛", "玄关", "窗框", "进入", "离开"],
    },
    "pressure_composition": {
        "label": "压迫构图与尺度",
        "aliases": ["俯视", "俯拍", "高位", "鸟瞰", "低机位", "仰拍", "负空间", "人物缩小", "环境吞没", "前景遮挡", "几何压迫"],
    },
    "partial_evidence": {
        "label": "局部证据链",
        "aliases": ["局部", "手", "脚", "鞋", "物件", "证据", "递进揭示", "完整身体后给", "地面证据", "反应确认"],
    },
    "restrained_acting": {
        "label": "克制表演与低反应",
        "aliases": ["微表情", "低反应", "眼神", "停顿", "失焦", "手指", "呼吸", "表演性静止", "延迟反应"],
    },
    "expression_break": {
        "label": "颜艺与认知击穿",
        "aliases": ["颜艺", "崩坏", "恐慌", "鱼眼", "广角", "强制透视", "黑眼", "大嘴", "离模", "表情突变"],
    },
    "cute_dark_conflict": {
        "label": "可爱图形与黑暗事实冲突",
        "aliases": ["可爱", "星光", "爱心", "粉色", "天真误读", "错误幸福", "图形污染现实", "反差"],
    },
    "style_mutation": {
        "label": "画风与绘画系统突变",
        "aliases": ["换画风", "平面化", "白场", "黑场", "粗线", "简笔画", "抽帧", "图形层", "线条替换", "空间抽象"],
    },
    "force_action": {
        "label": "动作受力与全身夸张",
        "aliases": ["动作", "受力", "碰撞", "推搡", "抓扯", "跳跃", "跑动", "压缩回弹", "拖拽", "惯性"],
    },
    "environment_aftermath": {
        "label": "环境接管与余波",
        "aliases": ["空镜", "余波", "静音", "低声压", "环境继续", "漂亮环境", "空场", "世界没有停", "声音撤走"],
    },
    "memory_time": {
        "label": "记忆、主观与时间改写",
        "aliases": ["回忆", "记忆", "主观", "时间回溯", "时间重置", "视角切换", "眼睛进入", "照片", "白化"],
    },
    "object_transition": {
        "label": "物件语言与转场",
        "aliases": ["物件", "道具", "匹配转场", "动作匹配", "形状匹配", "遮挡转场", "擦屏", "声音尾桥", "蒙太奇"],
    },
    "family_pressure": {
        "label": "家庭空间与成人压力",
        "aliases": ["家庭", "父亲", "母亲", "成人", "儿童视角", "房间", "餐桌", "住宅", "暖光压迫"],
    },
    "public_route": {
        "label": "公共空间与移动路线",
        "aliases": ["街道", "车站", "人潮", "旅行", "道路", "公园", "夜路", "移动", "路灯", "公共空间"],
    },
}


BLOCK_ROUTES = {
    ("ep01", "0000"): (["public_route", "cute_dark_conflict", "style_mutation"], "公园初遇、外星来历和开场图形语法"),
    ("ep01", "0300"): (["classroom_group", "public_route", "object_transition"], "群体关系、公园对话、道具说明与日常蒙太奇"),
    ("ep01", "0600"): (["restrained_acting", "cute_dark_conflict", "public_route"], "夜路交流、天真承诺与情绪误读"),
    ("ep01", "0900"): (["family_pressure", "memory_time", "threshold_door"], "家庭内部、门窗遮挡与时间道具"),
    ("ep01", "1200"): (["classroom_group", "pressure_composition", "restrained_acting"], "校园群体、明亮环境与人物孤立"),
    ("ep01", "1500"): (["classroom_group", "threshold_door", "partial_evidence"], "校园走廊、厕所阈限与局部身体证据"),
    ("ep01", "1800"): (["partial_evidence", "environment_aftermath", "restrained_acting"], "悲剧后果、空场和低反应余波"),
    ("ep01", "2100"): (["classroom_group", "environment_aftermath", "pressure_composition"], "教室孤立与结尾社会空间"),
    ("ep02", "0000"): (["classroom_group", "cute_dark_conflict", "public_route"], "教室群体注视、开场图形与公园关系"),
    ("ep02", "0300"): (["public_route", "force_action", "restrained_acting"], "森林与公园冲突、逼近和身体关系"),
    ("ep02", "0600"): (["family_pressure", "threshold_door", "environment_aftermath"], "夜路、家庭门槛和无法介入"),
    ("ep02", "0900"): (["partial_evidence", "cute_dark_conflict", "environment_aftermath"], "死亡确认、地面证据和天真误读"),
    ("ep02", "1200"): (["environment_aftermath", "memory_time"], "事件余波与结尾回收"),
    ("ep03", "0000"): (["expression_break", "restrained_acting", "public_route"], "见证者崩坏、普通空间与开场关系"),
    ("ep03", "0300"): (["public_route", "force_action", "object_transition"], "森林关系、道具交换和全身动作"),
    ("ep03", "0600"): (["family_pressure", "threshold_door", "restrained_acting"], "家庭尺度、门框与儿童观看权限"),
    ("ep03", "0900"): (["memory_time", "style_mutation", "classroom_group"], "金色关系插图、平面化和校园关系"),
    ("ep03", "1200"): (["memory_time", "partial_evidence", "family_pressure"], "主观自我、他人扫描和家庭反应"),
    ("ep03", "1500"): (["environment_aftermath", "object_transition"], "关系后果与结尾物件回收"),
    ("ep04", "0000"): (["classroom_group", "cute_dark_conflict", "style_mutation"], "教室关系、图形入侵与开场视觉语法"),
    ("ep04", "0300"): (["classroom_group", "partial_evidence", "family_pressure"], "考试压力、纸面证据和家庭行为"),
    ("ep04", "0600"): (["family_pressure", "classroom_group", "restrained_acting"], "儿童与成人尺度、校园表演和日常压力"),
    ("ep04", "0900"): (["force_action", "style_mutation", "cute_dark_conflict"], "粗线动作、星形主观层和高强度接触"),
    ("ep04", "1200"): (["environment_aftermath", "memory_time"], "冲突后的情绪落地与结尾"),
    ("ep05", "0000"): (["public_route", "threshold_door", "partial_evidence", "pressure_composition"], "旅行、人潮、住宅门槛与他人证据扫描"),
    ("ep05", "0300"): (["public_route", "cute_dark_conflict", "object_transition"], "公共空间、错误幸福和关系移动"),
    ("ep05", "0600"): (["family_pressure", "classroom_group", "expression_break"], "家庭对话、校园尴尬与短促画风切换"),
    ("ep05", "0900"): (["family_pressure", "force_action", "cute_dark_conflict", "environment_aftermath"], "暖光暴力、死亡现场、天真覆盖与静音余波"),
    ("ep05", "1200"): (["style_mutation", "memory_time", "object_transition"], "外星图形世界、抽象念头与现实回落"),
    ("ep06", "0000"): (["threshold_door", "cute_dark_conflict", "classroom_group", "memory_time"], "门缝观看、关系图形、夜间回忆与群体拓扑"),
    ("ep06", "0300"): (["memory_time", "partial_evidence", "force_action"], "时间回溯、地面物件和暴力证据链"),
    ("ep06", "0600"): (["memory_time", "object_transition", "environment_aftermath", "restrained_acting"], "共同旅行、消失、材质型哭泣和时间重置"),
    ("ep06", "0900"): (["classroom_group", "restrained_acting", "object_transition", "environment_aftermath"], "新时间线、教室孤立、群体移动和记忆残留"),
    ("ep06", "1200"): (["object_transition", "public_route", "memory_time"], "普通生活、商店物件选择和结尾落地"),
}


OVERRIDES = {
    "ep01/scene_index/scene_0000_04.jpg": {
        "categories": ["classroom_group", "pressure_composition", "style_mutation"],
        "tags": ["教室高位", "课桌阵列", "倾斜构图", "人物缩小", "飞行前景", "群体几何"],
        "summary": "开场教室段以倾斜人体切片和极高位课桌阵列改变观看尺度。",
    },
    "ep02/scene_index/scene_0000_01.jpg": {
        "categories": ["classroom_group", "restrained_acting"],
        "tags": ["全班转头", "群体注视", "学生回望", "眼睛先动", "头部后转", "视线级联", "不同反应幅度"],
        "summary": "教室谈话被新信息打断，学生按座位与注意路径分批回头，反应方向和幅度不统一。",
    },
    "ep05/scene_index/scene_0000_08.jpg": {
        "categories": ["threshold_door", "family_pressure", "partial_evidence"],
        "tags": ["开门", "门内暖光", "门外孩子", "家庭阈限", "脚步先行", "完整人物后给"],
        "summary": "门内家庭先以脚步、身体和婴儿出现，门外孩子被冷色走廊留在边界之外。",
    },
    "ep06/scene_index/scene_0600_07.jpg": {
        "categories": ["memory_time", "public_route", "classroom_group"],
        "tags": ["重复早晨", "学校入口", "人群经过", "时间线变化", "同构重拍"],
        "summary": "重置后的早晨复用旧镜头顺序，以学校入口和人群路线证明时间线改变。",
    },
    "ep06/scene_index/scene_0900_01.jpg": {
        "categories": ["classroom_group", "pressure_composition", "restrained_acting"],
        "tags": ["教室中心孤立", "课桌包围", "群体正常化", "人物被人群吞没", "公开空间压力"],
        "summary": "主体处于教室中心却被桌椅与同学包围，群体继续日常任务，孤立由空间密度完成。",
    },
    "ep06/scene_index/scene_0900_03.jpg": {
        "categories": ["classroom_group", "pressure_composition", "restrained_acting"],
        "tags": ["固定低机位", "前景同学腿", "背景孤立者", "群聊移动", "表演性静止"],
        "summary": "前景同学的腿和群聊路线反复遮挡背景孤立者，摄影机固定，排斥由群体运动完成。",
    },
}


def parse_scene(path: Path) -> tuple[str, int]:
    match = SCENE_RE.match(path.name)
    if not match:
        raise ValueError(f"Unexpected scene sheet name: {path}")
    return match.group(1), int(match.group(2))


def build_catalog(root: Path) -> dict[str, object]:
    scenes: list[dict[str, object]] = []
    for episode_dir in sorted(root.glob("ep[0-9][0-9]")):
        episode = episode_dir.name
        for path in sorted((episode_dir / "scene_index").glob("scene_*.jpg")):
            window, page = parse_scene(path)
            route_categories, route_summary = BLOCK_ROUTES.get(
                (episode, window),
                (["environment_aftermath"], "未专项标注的连续场景页"),
            )
            relative = path.relative_to(root).as_posix()
            override = OVERRIDES.get(relative, {})
            categories = override.get("categories", route_categories)
            tags = list(override.get("tags", []))
            for category in categories:
                tags.extend(CATEGORY_DEFS[category]["aliases"][:3])
            scenes.append(
                {
                    "id": f"SC-{episode[2:]}-{window}-{page:02d}",
                    "episode": episode.upper(),
                    "window": window,
                    "page": page,
                    "categories": categories,
                    "tags": list(dict.fromkeys(tags)),
                    "summary": override.get("summary", route_summary),
                    "curation": "verified_override" if override else "bucket_route",
                    "frame_path": str(path),
                }
            )
    return {
        "version": "2026-07-16.1",
        "source": "six locally verified episodes",
        "scene_sheet_count": len(scenes),
        "category_definitions": CATEGORY_DEFS,
        "scenes": scenes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=FRAME_ROOT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--expected-count", type=int, default=214)
    args = parser.parse_args()

    catalog = build_catalog(args.root)
    count = int(catalog["scene_sheet_count"])
    if count != args.expected_count:
        raise SystemExit(f"Expected {args.expected_count} scene sheets, found {count}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {count} scene sheets to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
