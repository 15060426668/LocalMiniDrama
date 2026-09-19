#!/usr/bin/env python3
"""Validate parameter-free, source-name-free MJ still-image descriptions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_FORBIDDEN_TERMS = (
    "章鱼P", "章鱼p", "章鱼噼", "章鱼噼的原罪", "Takopi", "takopi", "タコピー",
)

PARAMETER_PATTERNS = (
    (r"(?<!\w)--[a-zA-Z][\w-]*", "Midjourney flag"),
    (r"(?<!:)::(?!:)", "Midjourney weighting syntax"),
    (r"\b(?:stylize|chaos|seed|quality|weird|style raw|style reference)\s*[:=]?\s*\d+", "numeric MJ control"),
)

SOURCE_STYLE_PATTERNS = (
    (r"\bin\s+the\s+style\s+of\b", "named-style phrase"),
    (r"\binspired\s+by\b", "named-source phrase"),
    (r"[\u4e00-\u9fffA-Za-z0-9·・]+(?:式|风格|画风)复刻", "source-style replication phrase"),
)

VIDEO_PATTERNS = (
    (r"第\s*\d+(?:\.\d+)?\s*秒", "video timestamp"),
    (r"\d+(?:\.\d+)?\s*(?:-|至|到|~)\s*\d+(?:\.\d+)?\s*秒", "video time range"),
    (r"(?:运镜|推镜|拉镜|摇镜|跟拍|环绕镜头|镜头移动|镜头从.+到|转场|尾帧)", "time-based camera or transition language"),
    (r"(?:BASE\s*LOCK|A区块|E区块|SD承接|Seedance)", "video-prompt structure"),
)

NEGATIVE_PATTERNS = (
    (r"(?:不要|避免|禁止|不能|负面提示词|负向提示词)", "negative instruction"),
    (r"\b(?:no|without|avoid|exclude)\b", "negative instruction"),
)

COVERAGE_GROUPS = {
    "linework": ("线", "轮廓", "line", "contour"),
    "cel shading": ("赛璐璐", "平涂", "阴影", "cel", "shadow"),
    "texture": ("质感", "颗粒", "纸张", "哑光", "texture", "grain", "matte"),
    "composition": ("构图", "前景", "中景", "背景", "远景", "俯视", "近景", "全景", "composition", "foreground", "background"),
}

DETAILED_CHARACTER_GROUPS = {
    "character identity and age": r"(?:成年|青年|中年|老年|儿童|少女|女性|男性|角色身份)",
    "age-relative body proportions": r"(?:头身|肩宽|肩胯|颈部长度|颈长|手掌比例|身体比例|成年身高|四肢比例)",
    "pose support and weight": r"(?:重心|重量|支点|承重|踩实|坐凳|臀部|脚底|沉入|骨盆)",
    "face and jaw construction": r"(?:脸型|颅骨|上宽下短|下颌|脸颊|面部平面)",
    "eyelid construction": r"眼睑",
    "iris construction": r"虹膜",
    "catchlight construction": r"(?:高光|反光点|眼内反射)",
    "brow construction": r"眉",
    "nose construction": r"鼻",
    "mouth construction": r"(?:嘴|唇|口形)",
    "cheek or under-eye marks": r"(?:脸颊.*(?:短线|排线|笔触|红晕)|眼下.*(?:短线|排线|阴影|笔触))",
    "hair outer mass": r"(?:头发|黑发|发型).*(?:外轮廓|外部轮廓|整体剪影|大块剪影|块面|发量)",
    "hair clumps": r"(?:发束|发块|方向块|主要发片|大块发片)",
    "hair edge strands": r"(?:碎发|边缘发丝|边缘发束|发梢)",
    "line tool and color": r"(?:(?:铅笔|炭笔|石墨|墨线|干笔).*(?:深灰|灰褐|深棕|蓝灰|黑)|(?:深灰|灰褐|深棕|蓝灰|黑).*(?:铅笔|炭笔|石墨|墨线|干笔))",
    "line hierarchy": r"(?:外轮廓|轮廓线).*(?:内部线|面部线|五官线|接触线|发丝线|衣褶线)",
    "line pressure and taper": r"(?:线压|压力变化|粗细变化|收笔|渐细|锥形收尾|轻重变化)",
    "line breaks overlaps retracing": r"(?:断线|搭线|复描|重描|重复描线|双线修正|没有完全闭合|未完全闭合)",
    "matte fill boundary": r"(?:哑光平涂|平涂色块|哑光色块|填色边缘|手工偏移|轻微越界)",
    "one-step cel shadow": r"(?:一组|一层|单层|一步).*(?:赛璐璐阴影|阴影色块)|赛璐璐阴影",
    "clothing construction and force folds": r"(?:服装|旗袍|衣服|外套|衬衫|裙|裤|披肩).*(?:衣褶|褶皱|折痕|压缩|垂坠|布料重量)",
    "hand finger wrist performance": r"(?:左手|右手|双手|手掌).*(?:手指|拇指|指节|压力|压紧|手腕|腕部)",
    "feet or seated support": r"(?:脚|鞋|膝|坐姿|站姿).*(?:支撑|踩实|承重|收拢|抬起|落地)",
    "prop ownership or contact": r"(?:道具|琵琶|琴|箱|伞|杯|手机|书|包|花|刀).*(?:握|按|抱|压|靠|接触|承托|归属|持有)",
    "motivated light response": r"(?:主光|天光|灯光|环境光|逆光).*(?:脸|头发|发梢|手|服装|道具|轮廓|阴影)",
    "paper or animation capture texture": r"(?:纸张颗粒|纸面纹理|扫描颗粒|扫描噪声|动画摄影|传统动画|广播帧颗粒)",
}

DETAILED_SCENE_GROUPS = {
    "frame orientation or aspect": r"(?:\d+\s*:\s*\d+|横向|竖幅|竖向|方形|画幅)",
    "camera position": r"(?:摄影机|机位|视点|镜头位于)",
    "shot size": r"(?:大远景|远景|全景|中远景|中景|中近景|近景|特写|景别)",
    "focal length": r"(?:焦段|焦距|\d+(?:\.\d+)?\s*(?:毫米|mm))",
    "aperture or depth behavior": r"(?:光圈|f\s*/?\s*\d+(?:\.\d+)?|景深)",
    "focus target": r"(?:对焦|焦点|焦平面|清晰落在)",
    "foreground": r"前景",
    "midground": r"中景",
    "background or distance": r"(?:远景|背景)",
    "key light": r"主光",
    "fill or bounce": r"(?:辅光|补光|反射光|环境反射|天光|反射色)",
    "edge or negative fill": r"(?:逆光|边缘光|轮廓光|负补光|深色遮挡)",
    "practical light": r"(?:实用光|油灯|灯火|灯光|窗光|烛光|屏幕光|顶灯)",
    "exposure hierarchy": r"(?:曝光|高光|中间调|暗部|亮度层次|明暗层次)",
    "material evidence": r"(?:材质|木纹|石缝|纤维|磨损|水痕|积水|漆面|金属|玻璃|布料|纹理)",
    "capture evidence": r"(?:真实拍摄|摄影底片|纪录片|颗粒|噪声|压缩|镜头潮气|水滴虚化|自然曝光)",
}

HYBRID_SCENE_GROUPS = {
    "explicit live-action plate": r"(?:真实拍摄|实拍环境|摄影底片|纪录片摄影|真人实拍)",
    "explicit 2D subject": r"(?:二维|2D|手绘人物|手绘角色)",
    "perspective agreement": r"(?:透视|视平线|消失点)",
    "support or contact shadow": r"(?:接触影|脚底|坐凳|压紧|收紧|支点)",
    "occlusion or atmosphere crossing": r"(?:遮挡|穿过|前方经过|人物前后|前后两层)",
    "reflection or parallax": r"(?:倒影|反射|视差)",
    "shared environmental light": r"(?:环境色|反射色|色溢|共享.*光|服从.*光|响应.*光)",
}


def extract_description(text: str) -> str:
    marker = re.search(r"(?:\*\*)?MJ描述(?:\*\*)?\s*[:：]?", text, re.IGNORECASE)
    if marker:
        text = text[marker.end() :]
    text = text.replace("```text", "").replace("```markdown", "").replace("```", "")
    return text.strip()


def find_matches(text: str, patterns: tuple[tuple[str, str], ...]) -> list[str]:
    findings: list[str] = []
    for pattern, label in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            findings.append(f"{label}: {match.group(0)!r}")
    return findings


def require_groups(text: str, groups: dict[str, str]) -> list[str]:
    return [f"missing required {label}" for label, pattern in groups.items() if not re.search(pattern, text, re.IGNORECASE | re.DOTALL)]


def validate(text: str, forbidden_terms: list[str], profile: str = "base") -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    description = extract_description(text)

    minimum_lengths = {"base": 80, "detailed-character": 350, "detailed-scene": 500, "hybrid-scene": 900}
    minimum_length = minimum_lengths[profile]
    if len(description) < minimum_length:
        errors.append(f"description is too short for {profile} profile: {len(description)} < {minimum_length} characters")

    seen_forbidden: set[str] = set()
    for term in (*DEFAULT_FORBIDDEN_TERMS, *forbidden_terms):
        normalized = term.casefold().strip()
        if not normalized or normalized in seen_forbidden:
            continue
        seen_forbidden.add(normalized)
        if normalized in description.casefold():
            errors.append(f"forbidden source term: {term!r}")

    errors.extend(find_matches(description, PARAMETER_PATTERNS))
    errors.extend(find_matches(description, SOURCE_STYLE_PATTERNS))
    errors.extend(find_matches(description, VIDEO_PATTERNS))
    errors.extend(find_matches(description, NEGATIVE_PATTERNS))

    lower = description.casefold()
    for label, terms in COVERAGE_GROUPS.items():
        if not any(term.casefold() in lower for term in terms):
            warnings.append(f"missing explicit {label} coverage")

    if profile in {"detailed-character", "hybrid-scene"}:
        errors.extend(require_groups(description, DETAILED_CHARACTER_GROUPS))
    if profile in {"detailed-scene", "hybrid-scene"}:
        errors.extend(require_groups(description, DETAILED_SCENE_GROUPS))
    if profile == "hybrid-scene":
        errors.extend(require_groups(description, HYBRID_SCENE_GROUPS))

    paragraphs = [part.strip() for part in re.split(r"(?:\r?\n){2,}", description) if part.strip()]
    if len(paragraphs) > 1:
        warnings.append("final MJ description contains multiple paragraphs")

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="UTF-8 prompt file")
    parser.add_argument("--text", help="description text supplied directly")
    parser.add_argument("--forbidden-term", action="append", default=[])
    parser.add_argument("--profile", choices=("base", "detailed-character", "detailed-scene", "hybrid-scene"), default="base")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if bool(args.file) == bool(args.text):
        print("ERROR: provide exactly one prompt file or --text", file=sys.stderr)
        return 2

    if args.file:
        try:
            text = args.file.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: cannot read {args.file}: {exc}", file=sys.stderr)
            return 2
    else:
        text = args.text

    errors, warnings = validate(text, args.forbidden_term, args.profile)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
