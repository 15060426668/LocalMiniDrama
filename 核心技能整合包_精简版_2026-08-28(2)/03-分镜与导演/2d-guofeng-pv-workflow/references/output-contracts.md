# Output Contracts

这些是最小字段，不限制用户使用 Markdown、CSV 或 JSON。缺失信息写 `U`，不要编造。

## PV brief

```yaml
project: "原创江湖人物PV"
duration_sec: 8
format: "16:9 / 24fps"
logline: "一句话冲突"
protagonist: "主角及当前欲望"
relationship_change: "镜头前后关系变化"
visible_objects: ["兵器", "门派印记"]
ending_state: "动作后停在哪里，下一段如何接"
style_dna: ["旧纸", "铁雨", "粗墨轮廓"]
forbidden: ["角色卡轮播", "无因果墨效"]
evidence: "I"
```

## Asset board JSON

```json
{
  "project": "jianghu-pv-01",
  "assets": [
    {
      "id": "char_shenyi_identity_v02",
      "class": "character",
      "name": "沉衣身份立绘",
      "source": "refs/shenyi.png",
      "roi": "U",
      "evidence": "I",
      "version": "v02",
      "depth": "mg",
      "shots": ["S01", "S03"],
      "reuse": "可换景，不镜像",
      "status": "approved"
    }
  ]
}
```

## Shot ledger

```yaml
shots:
  - id: S01
    group: hero
    time: "0.00-4.00"
    purpose: "让观众先认出兵器和主角，再看眼神选择"
    subject: ["char_shenyi_identity_v02", "weapon_shortblade_draw_action_v01"]
    action: "预备 -> 拔刀 -> 顿帧 -> 余势归位"
    camera: "中近景，沿刀背轻推，保持屏幕右侧出势"
    layers: ["fg_doorframe_v01", "char_shenyi_identity_v02", "bg_qinghe_gate_establish_v03"]
    sound: "衣料/金属触发，冲击帧落 impact，尾音留 12f"
    tail: "刀尖停在画面右下，视线指向下一镜"
    risk: ["兵器轨迹", "角色脸部一致性"]
```

## Sound cue sheet

```yaml
cues:
  - id: C01
    shot: S01
    trigger: "拔刀开始"
    source: "metal_draw"
    from_frame: 18
    duration_frames: 22
    role: "action"
    tail: "自然衰减，不盖下一镜对白"
    evidence: "I"
```

## QA 结论

每次 QA 最少写：

```text
pass: yes/no
evidence: 镜头/帧号/字段
largest_problem: 只能选一个
next_change: 下一轮只改一件事
blocked_by: 缺失素材、未知证据或工具限制
```
