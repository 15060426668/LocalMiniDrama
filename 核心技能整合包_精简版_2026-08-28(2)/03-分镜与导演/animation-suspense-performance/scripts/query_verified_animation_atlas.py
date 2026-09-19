#!/usr/bin/env python3
"""Rank and compose verified animation counterpart hits without rescanning episodes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
ATLAS = SKILL_ROOT / "references" / "verified-animation-shot-atlas.md"
CATALOG = SKILL_ROOT / "references" / "verified-animation-scene-catalog.json"
ROW_RE = re.compile(r"^\|\s*(VA-\d{3})\s*\|")
PATH_RE = re.compile(r"[A-Za-z]:\\[^`<>|]+?\.(?:jpg|jpeg|png)", re.IGNORECASE)
ATLAS_FIELDS = (
    "id",
    "tags",
    "mechanisms",
    "shot_phrase",
    "animation_facts",
    "sound_relation",
    "time",
    "frame_path",
)


TERM_ALIASES = {
    "教室": ["课堂", "班级", "课桌", "学校", "学生", "同学"],
    "开门": ["门打开", "门板", "拉门", "滑门", "门框", "门缝", "门槛", "阈限", "玄关"],
    "关门": ["门板", "拉门", "滑门", "遮挡", "闭合", "阈限", "离开"],
    "俯视": ["俯拍", "高位", "极高位", "鸟瞰", "顶视", "上方", "人物缩小", "地面证据"],
    "仰视": ["仰拍", "低机位", "地面高度", "向上看", "成人尺度", "建筑压迫"],
    "群体转头": ["全班转头", "群体注视", "全班注视", "同学转头", "学生回望", "视线级联", "眼睛先动", "头部后转"],
    "群体注视": ["群体转头", "全班转头", "全班注视", "学生回望", "视线级联", "围观", "群体反应"],
    "孤立": ["排斥", "教室孤立", "中心孤立", "群体边界", "成员边界", "人物被人群吞没"],
    "压迫": ["几何压迫", "尺度压迫", "空间压力", "环境吞没", "前景遮挡", "负空间", "人物缩小"],
    "低反应": ["克制反应", "表演性静止", "延迟反应", "只动眼睛", "轻抬头", "微反应"],
    "颜艺": ["表情突变", "离模", "崩坏", "大嘴", "黑眼", "粗线脸", "认知击穿"],
    "鱼眼": ["恐慌广角", "强制透视", "近端放大", "边缘弯曲", "透视突变"],
    "转场": ["匹配转场", "动作匹配", "形状匹配", "遮挡转场", "擦屏", "尾桥", "硬切"],
    "静音": ["低声压", "声音撤走", "空场", "环境余波", "无专属音乐"],
    "星光": ["星形高光", "星轨", "发光轮廓", "亮星", "星形"],
    "天真误读": ["错误幸福", "可爱反差", "图形污染现实", "星光", "粉色", "主观命题"],
    "局部证据": ["证据链", "脚", "手", "鞋", "物件", "完整身体后给", "地面证据", "递进揭示"],
    "画风突变": ["换画风", "图形层", "平面化", "白场", "粗线", "简笔画", "线条替换", "抽帧"],
    "效果接力": ["环境接力", "动作匹配", "形状匹配", "声音尾桥", "图形侵入", "接触点", "落回现实", "余波"],
    "物件接力": ["物件", "道具", "地图", "硬币", "照片", "文具", "动作匹配", "形状匹配", "声音尾桥"],
    "环境换手": ["环境接力", "环境余波", "空场", "空位", "人物退出", "环境底", "文具架取得画面", "环境吞没"],
    "日常动画": ["日常对话", "普通生活", "做饭", "等待", "吃饭", "重复姿势", "物件记忆", "短停顿"],
    "母题腐化": ["重复地点", "重复姿势", "记忆残留", "图形污染现实", "错误幸福", "物件转场", "关系重写"],
}


def clean(value: str) -> str:
    return value.strip().strip("`").replace("<br>", " ")


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(item for item in values if item))


def load_atlas(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not ROW_RE.match(line):
            continue
        cells = [clean(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(ATLAS_FIELDS):
            raise ValueError(
                f"Malformed atlas row {cells[0]}: expected {len(ATLAS_FIELDS)} cells, got {len(cells)}"
            )
        row: dict[str, object] = dict(zip(ATLAS_FIELDS, cells))
        row.update(
            {
                "source_kind": "atlas",
                "categories": [],
                "summary": f"{row['shot_phrase']} {row['animation_facts']}",
                "curation": "verified_atlas",
            }
        )
        rows.append(row)
    return rows


def load_catalog(path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    if not path.exists():
        return [], {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows: list[dict[str, object]] = []
    for scene in payload.get("scenes", []):
        row = dict(scene)
        row.update(
            {
                "source_kind": "scene",
                "mechanisms": "",
                "shot_phrase": row.get("summary", ""),
                "animation_facts": "",
                "sound_relation": "",
                "time": f"{row.get('episode', '')} {row.get('window', '')} page {row.get('page', '')}",
            }
        )
        rows.append(row)
    return rows, payload.get("category_definitions", {})


def split_terms(query: str) -> list[str]:
    return [term.casefold() for term in re.split(r"[\s,，、]+", query) if term]


def related(term: str, candidate: str) -> bool:
    term = term.casefold()
    candidate = candidate.casefold()
    return term == candidate or term in candidate or candidate in term


def expand_term(term: str, category_defs: dict[str, object]) -> list[str]:
    phrases = [term]
    for key, aliases in TERM_ALIASES.items():
        pool = [key, *aliases]
        if related(term, key):
            phrases.extend(pool)
    for category, raw_definition in category_defs.items():
        definition = dict(raw_definition)
        label = str(definition.get("label", ""))
        aliases = [str(item) for item in definition.get("aliases", [])]
        if related(term, category) or related(term, label):
            phrases.extend([category, label, *aliases])
    return [item.casefold() for item in unique(phrases)]


def field_text(row: dict[str, object], field: str) -> str:
    value = row.get(field, "")
    if isinstance(value, list):
        return " ".join(str(item) for item in value).casefold()
    return str(value).casefold()


def match_group(row: dict[str, object], term: str, aliases: list[str]) -> tuple[bool, float, str]:
    weighted_fields = (
        ("tags", 7.0),
        ("categories", 6.0),
        ("summary", 5.0),
        ("shot_phrase", 4.5),
        ("animation_facts", 4.0),
        ("sound_relation", 3.0),
        ("mechanisms", 2.0),
        ("time", 1.0),
    )
    best_score = 0.0
    best_phrase = ""
    for field, weight in weighted_fields:
        text = field_text(row, field)
        for phrase in aliases:
            if phrase and phrase in text:
                exact_bonus = 2.0 if term in text else 0.0
                score = weight + exact_bonus + min(len(phrase), 8) * 0.05
                if score > best_score:
                    best_score = score
                    best_phrase = phrase
    return bool(best_phrase), best_score, best_phrase


def score_row(
    row: dict[str, object],
    terms: list[str],
    groups: dict[str, list[str]],
) -> dict[str, object]:
    matched: list[str] = []
    matched_via: dict[str, str] = {}
    score = 0.0
    for term in terms:
        hit, term_score, phrase = match_group(row, term, groups[term])
        if hit:
            matched.append(term)
            matched_via[term] = phrase
            score += term_score
    curation = str(row.get("curation", ""))
    if row.get("source_kind") == "atlas":
        score += 5.0
    elif curation == "verified_override":
        score += 3.0
    elif curation == "bucket_route":
        score -= 2.0
    if terms and len(matched) == len(terms):
        score += 8.0
    enriched = dict(row)
    enriched["score"] = round(score, 2)
    enriched["matched_terms"] = matched
    enriched["matched_via"] = matched_via
    enriched["missing_terms"] = [term for term in terms if term not in matched]
    return enriched


def select_coverage(rows: list[dict[str, object]], terms: list[str], limit: int) -> list[dict[str, object]]:
    if not rows or limit <= 0:
        return []
    if not terms:
        return sorted(rows, key=lambda row: float(row["score"]), reverse=True)[:limit]
    uncovered = set(terms)
    remaining = list(rows)
    selected: list[dict[str, object]] = []
    while uncovered and remaining and len(selected) < limit:
        def confidence_tier(row: dict[str, object]) -> int:
            if row.get("source_kind") == "atlas":
                return 3
            if row.get("curation") == "verified_override":
                return 2
            return 1

        remaining.sort(
            key=lambda row: (
                confidence_tier(row) if uncovered.intersection(row["matched_terms"]) else 0,
                len(uncovered.intersection(row["matched_terms"])),
                len(row["matched_terms"]),
                float(row["score"]),
            ),
            reverse=True,
        )
        best = remaining.pop(0)
        new_terms = uncovered.intersection(best["matched_terms"])
        if not new_terms:
            break
        selected.append(best)
        uncovered.difference_update(new_terms)
    return selected


def existing_paths(row: dict[str, object]) -> list[tuple[str, bool]]:
    paths = PATH_RE.findall(str(row.get("frame_path", "")))
    return [(item, Path(item).exists()) for item in paths]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Functional terms separated by spaces/commas")
    parser.add_argument("--id", default="", help="Exact VA or SC id")
    parser.add_argument("--mechanism", default="", help="Mechanism ID such as SA-15")
    parser.add_argument("--category", default="", help="Category id, label or alias")
    parser.add_argument("--source", choices=("all", "atlas", "scene"), default="all")
    parser.add_argument("--strict", action="store_true", help="Require one row to cover every query term")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument("--list-categories", action="store_true")
    parser.add_argument("--atlas", type=Path, default=ATLAS)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    args = parser.parse_args()

    atlas_rows = load_atlas(args.atlas)
    scene_rows, category_defs = load_catalog(args.catalog)
    if args.list_categories:
        print(json.dumps(category_defs, ensure_ascii=False, indent=2))
        return 0

    rows = atlas_rows + scene_rows
    if args.source != "all":
        rows = [row for row in rows if row.get("source_kind") == args.source]
    if args.id:
        rows = [row for row in rows if str(row.get("id", "")).casefold() == args.id.casefold()]
    if args.mechanism:
        rows = [row for row in rows if args.mechanism.casefold() in field_text(row, "mechanisms")]
    if args.category:
        category_group = expand_term(args.category.casefold(), category_defs)
        rows = [row for row in rows if match_group(row, args.category.casefold(), category_group)[0]]

    terms = split_terms(args.query)
    groups = {term: expand_term(term, category_defs) for term in terms}
    scored = [score_row(row, terms, groups) for row in rows]
    scored = [row for row in scored if not terms or row["matched_terms"]]
    if args.strict and terms:
        scored = [row for row in scored if len(row["matched_terms"]) == len(terms)]
    scored.sort(key=lambda row: (len(row["matched_terms"]), float(row["score"])), reverse=True)

    selected = scored[: max(args.limit, 0)] if args.strict else select_coverage(scored, terms, max(args.limit, 0))
    if args.check_files:
        for row in selected:
            row["path_checks"] = existing_paths(row)

    covered = unique([term for row in selected for term in row["matched_terms"]])
    missing = [term for term in terms if term not in covered]
    if args.as_json:
        print(
            json.dumps(
                {"query": args.query, "covered_terms": covered, "missing_terms": missing, "results": selected},
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"coverage: {', '.join(covered) or '(none)'}")
        if missing:
            print(f"missing: {', '.join(missing)}")
        for row in selected:
            print(f"[{row['id']}] score={row['score']} source={row['source_kind']} tags={field_text(row, 'tags')}")
            print(f"  covers: {', '.join(row['matched_terms'])}")
            print(f"  via: {row['matched_via']}")
            print(f"  categories: {field_text(row, 'categories')}")
            print(f"  shot: {row.get('shot_phrase', '')}")
            print(f"  animation: {row.get('animation_facts', '')}")
            print(f"  sound: {row.get('sound_relation', '')}")
            print(f"  time: {row.get('time', '')}")
            print(f"  frame: {row.get('frame_path', '')}")
            if args.check_files:
                print(f"  path_checks: {row['path_checks']}")

    if not selected:
        print("No verified animation index entries matched.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
