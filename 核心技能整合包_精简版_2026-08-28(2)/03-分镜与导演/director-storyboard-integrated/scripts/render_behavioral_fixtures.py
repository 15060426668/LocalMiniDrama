#!/usr/bin/env python3
"""Render deterministic registered storyboard and Dream SD fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_PAYLOADS = ROOT / "behavioral-fixture-payloads.json"
DEFAULT_OUTPUT = ROOT / "fixtures" / "behavioral"


def metered_sound(description: str) -> str:
    return (
        f"主声源[BODY-01]{description}，画内或画外2m，-24 RMS dBFS/-12 peak dBFS；"
        "ENV-01空间底床-36 RMS dBFS/-26 peak dBFS，相对主声源-12dB；"
        "LPF 3.2kHz，RT60 0.9s，dry-wet 18%；主声源起音时ENV闪避3dB；"
        "镜头-19 LUFS-S，母版social_balanced -14 LUFS-I/-1 dBTP；"
        "主声源触发可见反应，尾音L-cut形成声桥。"
    )


def render(case_id: str, item: dict) -> str:
    duration = int(item["duration"])
    sound = metered_sound(item["sound"])
    return f"""# {case_id} {item['title']}

| 镜头 | 时长 | 景别/焦段 | 构图画面 | 机位与运镜 | 光影/色彩 | 画面基调/质感 | 实拍摄影证据 | 画面内容 | 运动生态/层级交互 | 声音设计 | 转场 | 叙事目的 | 镜间变化/尾帧 | SD承接锚点 |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {duration}秒 | {item['lens']} | {item['composition']} | {item['camera']} | {item['light']} | {item['texture']} | {item['evidence']} | {item['content']} | {item['ecology']} | {sound} | {item['transition']} | {item['purpose']} | {item['tail']} | {item['anchors']} |

【STYLE LOCK】
21:9写实数字电影，角色身份、服装、空间方向和物件状态连续。

【画面基调与质感锁定】
保留皮肤、衣料、金属、墙面、地面与空气层的真实材质响应和稳定黑位。

【主色板锁定】
沿用源分镜的实用光源、色温所有权与强调色变化。

【空间与方向锁定】
沿用源分镜的前景、中景、后景、人物路线、屏幕方向、声源位置和尾帧状态。

【完整声音轨】
social_balanced母版-14 LUFS-I/-1 dBTP，第0-{duration}秒镜头-19 LUFS-S，主声源、环境底床、可见反应和L-cut声桥按源分镜执行。

【A区块·正向提示词】

第0-{duration}秒｜源镜头1

景别/焦段/景深：{item['lens']}。
构图画面：{item['composition']}。
机位与运镜：{item['camera']}。
光影/色彩：{item['light']}。
画面基调/质感：{item['texture']}。
实拍摄影证据 / 生成可信证据：{item['evidence']}。
画面内容：{item['content']}。
运动生态/层级交互：{item['ecology']}。
声音设计：{sound}
转场：{item['transition']}。
镜间变化/尾帧：{item['tail']}。
SD承接锚点：{item['anchors']}。
连续性校验：起始状态继承源分镜；本段差量按动作、摄影机、光影、声音和物件变化执行；尾帧状态为{item['tail']}；下一段继承全部残留状态。

【E区块·分镜时间轴】

| 序号 | 时间 | 景别/机位 | 焦段/景深 | 主要动作 | 构图/空间变化 | 声音/转场 | 尾帧 |
|---:|---|---|---|---|---|---|---|
| 1 | 第0-{duration}秒 | {item['camera']} | {item['lens']} | {item['content']} | {item['composition']} | {item['sound']}；{item['transition']} | {item['tail']} |
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payloads", type=Path, default=DEFAULT_PAYLOADS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    payloads = json.loads(args.payloads.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    for case_id, item in payloads.items():
        (args.output / f"{case_id}.md").write_text(render(case_id, item), encoding="utf-8")
    print(f"Rendered {len(payloads)} behavioral fixtures to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
