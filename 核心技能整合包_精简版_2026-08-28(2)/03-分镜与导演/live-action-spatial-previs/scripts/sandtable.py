#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""俯视沙盘图生成器 —— live-action-spatial-previs skill 附属工具。

用法:
    python sandtable.py input.json [-o output.html]

输入 JSON 格式见 references/sandtable-contract.md。
世界坐标: x 东为正, y 北为正。角度: 东=0°, 北=90°(逆时针)。
纯标准库, 无第三方依赖。
"""
import argparse
import html
import json
import math
import sys

DIR_ANGLES = {"N": 90.0, "S": -90.0, "E": 0.0, "W": 180.0,
              "NE": 45.0, "NW": 135.0, "SE": -45.0, "SW": -135.0}
DIR_NAMES = ["东", "东北", "北", "西北", "西", "西南", "南", "东南"]


CN_ANGLES = {"北": 90.0, "南": -90.0, "东": 0.0, "西": 180.0,
             "东北": 45.0, "西北": 135.0, "东南": -45.0, "西南": -135.0}


def ang(v):
    """朝向 → 角度(度)。接受八向字母、中文八向或数字。"""
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip()
    if s in CN_ANGLES:
        return CN_ANGLES[s]
    u = s.upper()
    if u in DIR_ANGLES:
        return DIR_ANGLES[u]
    try:
        return float(u)
    except ValueError:
        raise SystemExit(f"错误: 朝向 '{s}' 无法识别。请用 N/S/E/W/NE/NW/SE/SW、"
                         f"中文八向(东/南/西/北/东北/东南/西北/西南)或角度数字(东=0, 北=90)。")


def dir_name(deg):
    """角度 → 最近的八向中文名。"""
    i = int(((deg % 360.0) + 22.5) // 45.0) % 8
    return DIR_NAMES[i]


def norm180(deg):
    """归一到 (-180, 180]。"""
    d = deg % 360.0
    if d > 180.0:
        d -= 360.0
    return d


def facing_desc(char_facing, cam_x, cam_y, cx, cy):
    """摄影机看到人物的哪一面。"""
    to_cam = math.degrees(math.atan2(cam_y - cy, cam_x - cx))
    off = abs(norm180(to_cam - char_facing))
    if off <= 30:
        return "接近正脸"
    if off <= 70:
        return "四分之三正面"
    if off <= 110:
        return "侧面"
    if off <= 150:
        return "四分之三背面"
    return "背影"


def in_frame(cam, ch):
    """人物是否落在摄影机视野扇形内(仅按方向角, 不含遮挡)。"""
    dx, dy = ch["x"] - cam["x"], ch["y"] - cam["y"]
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return False  # 与机位重合视为不入画
    bearing = math.degrees(math.atan2(dy, dx))
    off = abs(norm180(bearing - ang(cam["facing"])))
    return off <= float(cam.get("fov", 40)) / 2.0


def esc(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- SVG 绘制

def shot_svg(shot, scene, size=340):
    """按场景长宽比绘制: 长边=size, 短边等比缩放, 不失真。"""
    w, d = float(scene["bounds"]["w"]), float(scene["bounds"]["d"])
    margin = 18
    scale = (size - 2 * margin) / max(w, d)
    sw = w * scale + 2 * margin
    sh = d * scale + 2 * margin

    def p(x, y):
        return margin + (x + w / 2.0) * scale, margin + (d / 2.0 - y) * scale

    parts = []
    parts.append(f'<svg viewBox="0 0 {sw:.0f} {sh:.0f}" width="{sw:.0f}" height="{sh:.0f}" '
                 f'xmlns="http://www.w3.org/2000/svg" style="background:#fafaf7;border:1px solid #ccc;border-radius:6px">')
    # 场景边框与指北
    parts.append(f'<rect x="{margin}" y="{margin}" width="{sw-2*margin:.1f}" height="{sh-2*margin:.1f}" '
                 f'fill="none" stroke="#bbb"/>')
    parts.append(f'<text x="{sw-26:.0f}" y="{margin+14}" font-size="11" fill="#888">北↑</text>')
    # 固定物
    for lm in scene.get("landmarks", []):
        cx, cy = p(float(lm["x"]), float(lm["y"]))
        w_px = float(lm.get("w", 2)) * scale
        h_px = float(lm.get("h", 2)) * scale
        parts.append(f'<rect x="{cx-w_px/2:.1f}" y="{cy-h_px/2:.1f}" width="{w_px:.1f}" height="{h_px:.1f}" '
                     f'fill="#d8d2c4" stroke="#a89f8c"/>')
        parts.append(f'<text x="{cx:.1f}" y="{cy+3:.1f}" font-size="10" text-anchor="middle" fill="#6b6353">{esc(lm["name"])}</text>')
    # 区域(点阵)
    for z in scene.get("zones", []):
        zx, zy = float(z["x"]), float(z["y"])
        zw, zh = float(z.get("w", 2)), float(z.get("h", 6))
        cols = max(1, int(zw // 1.2)); rows = max(2, int(zh // 2))
        for r in range(rows):
            for c in range(cols):
                px_, py_ = p(zx - zw / 2 + (c + 0.5) * zw / cols,
                             zy - zh / 2 + (r + 0.5) * zh / rows)
                parts.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="2.6" fill="#9a938a"/>')
        lx, ly = p(zx, zy + zh / 2 + 1.2)
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10" text-anchor="middle" fill="#77706a">{esc(z["name"])}</text>')
    # 摄影机视野扇形
    cam = shot["camera"]
    cx, cy = p(float(cam["x"]), float(cam["y"]))
    cam_deg = ang(cam["facing"])
    fov = float(cam.get("fov", 40))
    reach = max(sw, sh) * 0.95
    a1 = math.radians(cam_deg - fov / 2.0)
    a2 = math.radians(cam_deg + fov / 2.0)
    # 注意 SVG y 轴向下, 世界角度→SVG: dx=cos, dy=-sin
    x1, y1 = cx + reach * math.cos(a1), cy - reach * math.sin(a1)
    x2, y2 = cx + reach * math.cos(a2), cy - reach * math.sin(a2)
    parts.append(f'<path d="M{cx:.1f},{cy:.1f} L{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} Z" '
                 f'fill="#2f7fd0" opacity="0.14"/>')
    # 人物
    for ch in shot.get("chars", []):
        hx, hy = p(float(ch["x"]), float(ch["y"]))
        f_deg = ang(ch.get("facing", "N"))
        fx, fy = hx + 15 * math.cos(math.radians(f_deg)), hy - 15 * math.sin(math.radians(f_deg))
        main = ch.get("main", False)
        color = "#c85a28" if main else "#444"
        parts.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{6 if main else 5}" '
                     f'fill="{color if main else "none"}" stroke="{color}" stroke-width="1.8"/>')
        parts.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{fx:.1f}" y2="{fy:.1f}" '
                     f'stroke="{color}" stroke-width="2"/>')
        parts.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="2.2" fill="{color}"/>')
        parts.append(f'<text x="{hx+9:.1f}" y="{hy+13:.1f}" font-size="11" fill="{color}">{esc(ch["name"])}</text>')
    # 摄影机(最后画, 保持在最上层)
    t = 8
    parts.append(f'<path d="M{cx-t:.1f},{cy-t:.1f} L{cx+t:.1f},{cy-t:.1f} L{cx:.1f},{cy+t*0.9:.1f} Z" '
                 f'transform="rotate({-cam_deg+(-90)} {cx:.1f} {cy:.1f})" fill="#2f7fd0"/>')
    parts.append(f'<text x="{cx+10:.1f}" y="{cy-8:.1f}" font-size="10" fill="#2f7fd0">机位</text>')
    parts.append("</svg>")
    return "".join(parts)


# ---------------------------------------------------------------- 汇总页

def build_html(data):
    scene = data["scene"]
    cards = []
    for shot in data.get("shots", []):
        sid = shot.get("id", "?")
        if "camera" not in shot:
            raise SystemExit(f"错误: {sid} 缺少 camera 字段。")
        for k in ("x", "y", "facing"):
            if k not in shot["camera"]:
                raise SystemExit(f"错误: {sid} 的 camera 缺少 {k} 字段。")
        for ch in shot.get("chars", []):
            for k in ("name", "x", "y"):
                if k not in ch:
                    raise SystemExit(f"错误: {sid} 的人物 {ch.get('name', '?')} 缺少 {k} 字段。")
        cam = shot["camera"]
        cam_deg = ang(cam["facing"])
        left, right = dir_name(cam_deg + 90.0), dir_name(cam_deg - 90.0)
        deep = dir_name(cam_deg)
        ins, outs = [], []
        for ch in shot.get("chars", []):
            d = math.hypot(ch["x"] - cam["x"], ch["y"] - cam["y"])
            face = facing_desc(ang(ch.get("facing", "N")), cam["x"], cam["y"], ch["x"], ch["y"])
            entry = f'{esc(ch["name"])}（{face}，距机位 {d:.1f}）'
            (ins if in_frame(cam, ch) else outs).append(entry)
        info = [
            f'<b>机位</b>：{esc(cam.get("label", ""))}｜朝{dir_name(cam_deg)}｜视野 {cam.get("fov", 40)}°',
            f'<b>画面</b>：左＝{left}｜右＝{right}｜深处＝{deep}',
            f'<b>画框内</b>：{"、".join(ins) if ins else "无人物"}',
        ]
        if outs:
            info.append(f'<b>画框外</b>：{"、".join(outs)}')
        if shot.get("note"):
            info.append(f'<b>备注</b>：{esc(shot["note"])}')
        cards.append(
            '<div class="card">'
            f'<h3>{esc(shot.get("id", "?"))}<span>{esc(shot.get("time", ""))}</span></h3>'
            + shot_svg(shot, scene)
            + '<div class="info">' + "".join(f"<div>{line}</div>" for line in info) + "</div></div>"
        )
    risks = data.get("risks", [])
    risk_html = ""
    if risks:
        risk_html = ('<div class="risks"><h2>风险与建议（仅提示，由用户裁决）</h2><ol>'
                     + "".join(f"<li>{esc(r)}</li>" for r in risks) + "</ol></div>")
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8">
<title>{esc(data.get("title", "沙盘"))}</title>
<style>
body{{font-family:"Microsoft YaHei",system-ui,sans-serif;margin:24px;background:#f4f2ee;color:#222}}
h1{{font-size:20px}} .grid{{display:flex;flex-wrap:wrap;gap:18px}}
.card{{background:#fff;border:1px solid #ddd;border-radius:8px;padding:12px;width:360px}}
.card h3{{margin:0 0 8px;font-size:15px;display:flex;justify-content:space-between}}
.card h3 span{{font-weight:normal;color:#888;font-size:12px}}
.info{{margin-top:8px;font-size:12.5px;line-height:1.7}}
.risks{{margin-top:24px;background:#fff7ef;border:1px solid #e0c9ae;border-radius:8px;padding:8px 20px;max-width:780px}}
.risks h2{{font-size:15px}} .risks li{{font-size:13px;line-height:1.7}}
</style></head><body>
<h1>{esc(data.get("title", "沙盘"))}</h1>
<div class="grid">{"".join(cards)}</div>
{risk_html}
</body></html>"""


def main():
    ap = argparse.ArgumentParser(description="俯视沙盘图生成器")
    ap.add_argument("input", help="输入 JSON 文件")
    ap.add_argument("-o", "--output", default=None, help="输出 HTML 文件(默认同名 .html)")
    args = ap.parse_args()
    with open(args.input, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    out = args.output or (args.input.rsplit(".", 1)[0] + ".html")
    with open(out, "w", encoding="utf-8-sig") as f:
        f.write(build_html(data))
    print(f"OK {out} ({len(data.get('shots', []))} shots)")


if __name__ == "__main__":
    sys.exit(main())
