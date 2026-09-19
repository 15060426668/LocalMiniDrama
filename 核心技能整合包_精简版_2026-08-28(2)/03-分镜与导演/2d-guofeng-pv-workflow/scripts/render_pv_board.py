#!/usr/bin/env python3
"""Render a deterministic, dependency-free HTML board for a 2D PV plan."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


GROUP_ORDER = ["opening", "hero", "relationship", "conflict", "ensemble", "outro"]
CLASS_ORDER = [
    "character",
    "costume",
    "weapon",
    "prop",
    "fg",
    "mg",
    "bg",
    "fx",
    "text",
    "sound",
]


def esc(value: Any) -> str:
    return html.escape(str(value if value not in (None, "") else "U"), quote=True)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def label_list(value: Any) -> str:
    items = [esc(item) for item in as_list(value)]
    return ", ".join(items) if items else "U"


def read_board(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("input root must be a JSON object")
    shots = data.get("shots", [])
    assets = data.get("assets", [])
    if not isinstance(shots, list) or not isinstance(assets, list):
        raise ValueError("shots and assets must be arrays")
    clean_shots: list[dict[str, Any]] = []
    clean_assets: list[dict[str, Any]] = []
    for index, shot in enumerate(shots, 1):
        if not isinstance(shot, dict):
            raise ValueError(f"shots[{index}] must be an object")
        shot = dict(shot)
        shot.setdefault("id", f"S{index:02d}")
        shot.setdefault("group", "unclassified")
        shot.setdefault("time", "U")
        shot.setdefault("purpose", "U")
        shot.setdefault("subject", [])
        shot.setdefault("layers", [])
        clean_shots.append(shot)
    for index, asset in enumerate(assets, 1):
        if not isinstance(asset, dict):
            raise ValueError(f"assets[{index}] must be an object")
        asset = dict(asset)
        asset.setdefault("id", f"asset_{index:03d}")
        asset.setdefault("class", "unclassified")
        asset.setdefault("name", asset["id"])
        asset.setdefault("status", "U")
        asset.setdefault("shots", [])
        clean_assets.append(asset)
    return data, clean_shots, clean_assets


def sort_group(name: str) -> tuple[int, str]:
    try:
        return GROUP_ORDER.index(name), name
    except ValueError:
        return len(GROUP_ORDER), name


def sort_class(name: str) -> tuple[int, str]:
    try:
        return CLASS_ORDER.index(name), name
    except ValueError:
        return len(CLASS_ORDER), name


def shot_card(shot: dict[str, Any]) -> str:
    risk = label_list(shot.get("risk"))
    return f"""
    <article class="shot-card">
      <header><span class="id">{esc(shot['id'])}</span><span class="time">{esc(shot['time'])}</span></header>
      <h3>{esc(shot.get('purpose'))}</h3>
      <dl>
        <dt>主体</dt><dd>{label_list(shot.get('subject'))}</dd>
        <dt>动作</dt><dd>{esc(shot.get('action'))}</dd>
        <dt>相机</dt><dd>{esc(shot.get('camera'))}</dd>
        <dt>图层</dt><dd>{label_list(shot.get('layers'))}</dd>
        <dt>声音</dt><dd>{esc(shot.get('sound'))}</dd>
        <dt>尾帧</dt><dd>{esc(shot.get('tail'))}</dd>
        <dt>风险</dt><dd class="risk">{risk}</dd>
      </dl>
    </article>"""


def asset_card(asset: dict[str, Any]) -> str:
    status = str(asset.get("status", "U"))
    return f"""
    <article class="asset-card status-{esc(status)}">
      <header><span class="id">{esc(asset['id'])}</span><span class="status">{esc(status)}</span></header>
      <h3>{esc(asset.get('name'))}</h3>
      <dl>
        <dt>来源</dt><dd>{esc(asset.get('source'))}</dd>
        <dt>ROI</dt><dd>{esc(asset.get('roi'))}</dd>
        <dt>证据</dt><dd>{esc(asset.get('evidence'))}</dd>
        <dt>深度</dt><dd>{esc(asset.get('depth'))}</dd>
        <dt>镜头</dt><dd>{label_list(asset.get('shots'))}</dd>
        <dt>复用</dt><dd>{esc(asset.get('reuse'))}</dd>
      </dl>
    </article>"""


def render(data: dict[str, Any], shots: list[dict[str, Any]], assets: list[dict[str, Any]]) -> str:
    project = data.get("project", data.get("title", "2D Guofeng PV"))
    groups: dict[str, list[dict[str, Any]]] = {}
    for shot in shots:
        groups.setdefault(str(shot.get("group", "unclassified")), []).append(shot)
    asset_groups: dict[str, list[dict[str, Any]]] = {}
    for asset in assets:
        asset_groups.setdefault(str(asset.get("class", "unclassified")), []).append(asset)
    warnings = []
    for shot in shots:
        if shot.get("group") == "unclassified":
            warnings.append(f"{shot['id']} has no group")
    for asset in assets:
        if asset.get("evidence", "U") == "U":
            warnings.append(f"{asset['id']} has unknown evidence state")
    warning_html = "".join(f"<li>{esc(item)}</li>" for item in warnings) or "<li>没有结构性警告</li>"
    shot_html = "".join(
        f"<section class=\"group\"><h2>{esc(group)}</h2><div class=\"shot-grid\">{''.join(shot_card(s) for s in sorted(items, key=lambda x: str(x['id'])) )}</div></section>"
        for group, items in sorted(groups.items(), key=lambda pair: sort_group(pair[0]))
    ) or "<p class=\"empty\">还没有镜头。</p>"
    asset_html = "".join(
        f"<section class=\"group\"><h2>{esc(asset_class)}</h2><div class=\"asset-grid\">{''.join(asset_card(a) for a in sorted(items, key=lambda x: str(x['id'])) )}</div></section>"
        for asset_class, items in sorted(asset_groups.items(), key=lambda pair: sort_class(pair[0]))
    ) or "<p class=\"empty\">还没有资产。</p>"
    character_items = [a for a in assets if a.get("class") == "character"]
    character_html = "".join(
        f"<li><strong>{esc(item['id'])}</strong> {esc(item.get('name'))} <span>{label_list(item.get('shots'))}</span></li>"
        for item in sorted(character_items, key=lambda x: str(x["id"]))
    ) or "<li>还没有角色资产。</li>"
    css = """
      :root { color-scheme: dark; font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif; background: #101318; color: #e8e9ed; }
      body { max-width: 1480px; margin: 0 auto; padding: 32px 40px 64px; background: #101318; }
      h1 { margin: 0 0 8px; font-size: 28px; letter-spacing: 0; }
      h2 { margin: 32px 0 12px; font-size: 16px; text-transform: uppercase; color: #d9ae72; letter-spacing: .08em; }
      h3 { margin: 10px 0 14px; font-size: 15px; line-height: 1.4; }
      .meta { color: #a9adb8; margin-bottom: 22px; }
      .stats { display: flex; gap: 8px; flex-wrap: wrap; margin: 18px 0 26px; }
      .pill { border: 1px solid #343944; padding: 6px 10px; border-radius: 999px; color: #c9ccd4; font-size: 12px; }
      .group { border-top: 1px solid #2a2e37; padding-top: 2px; }
      .shot-grid, .asset-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 12px; }
      .shot-card, .asset-card { border: 1px solid #303641; background: #171b22; padding: 16px; border-radius: 6px; min-width: 0; }
      .shot-card header, .asset-card header { display: flex; justify-content: space-between; gap: 12px; color: #a9adb8; font-size: 12px; }
      .id { color: #e7c38c; font-family: ui-monospace, monospace; }
      .time, .status { white-space: nowrap; }
      dl { display: grid; grid-template-columns: 52px minmax(0, 1fr); gap: 6px 10px; margin: 0; font-size: 12px; line-height: 1.5; }
      dt { color: #808795; } dd { margin: 0; overflow-wrap: anywhere; }
      .risk { color: #e6a5a5; } .status-approved { border-color: #52694f; } .status-rejected { opacity: .55; }
      .index { background: #151920; border: 1px solid #2c313b; padding: 14px 18px; border-radius: 6px; }
      .index ul, .warnings ul { margin: 8px 0 0; padding-left: 20px; line-height: 1.6; font-size: 13px; }
      .index span { color: #9ca2b0; margin-left: 8px; }
      .warnings { margin-top: 32px; color: #c8b58d; }
      .empty { color: #8d929e; }
      @media (max-width: 720px) { body { padding: 24px 16px 48px; } .shot-grid, .asset-grid { grid-template-columns: 1fr; } }
    """
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(project)} - PV Board</title><style>{css}</style></head>
<body>
  <h1>{esc(project)}</h1>
  <div class="meta">2D 国风 PV production board · 稳定排序 · 证据状态与分组可追踪</div>
  <div class="stats"><span class="pill">镜头 {len(shots)}</span><span class="pill">资产 {len(assets)}</span><span class="pill">角色 {len(character_items)}</span><span class="pill">未知证据 {sum(1 for a in assets if a.get('evidence', 'U') == 'U')}</span></div>
  <section class="index"><strong>角色索引</strong><ul>{character_html}</ul></section>
  <h2>Shot ledger / 按功能分组</h2>{shot_html}
  <h2>Asset board / 按资产类分组</h2>{asset_html}
  <section class="warnings"><strong>Board warnings</strong><ul>{warning_html}</ul></section>
</body></html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="board JSON")
    parser.add_argument("output", type=Path, help="output HTML")
    args = parser.parse_args()
    data, shots, assets = read_board(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(data, shots, assets), encoding="utf-8", newline="\n")
    print(f"rendered {len(shots)} shots and {len(assets)} assets -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
