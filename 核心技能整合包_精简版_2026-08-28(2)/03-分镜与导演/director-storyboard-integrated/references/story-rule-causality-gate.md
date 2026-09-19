# Story Rule And Causality Gate

用途：在对标和分镜之前锁死故事规则，防止镜头漂亮但角色提前知道信息、道具规则失效、动作没有后果或为转场强改剧情。

## Runtime Use

重要场景先内部建立一张因果卡。普通场景只保留必要行；规则物、梦境、收容、身份反转和连续追逐必须完整执行。

```text
场景目标：
角色当前目标：
角色已知：
角色未知：
观众额外知道：
不可改写的世界规则：
可触发规则的主体/动作：
不能触发规则的外力：
物件初始状态与所有者：
动作原因 -> 可见动作 -> 直接后果 -> 残留状态 -> 下一步选择：
```

## Six Gates

1. **知识门**：角色只能对已看见、听见、触碰或合理推断的信息作反应。
2. **权限门**：规则必须写清谁能触发、什么动作能触发、外力是否有效、反馈是否延迟。
3. **物件门**：物件身份、所有者、位置、朝向和状态变化必须连续。
4. **后果门**：每个关键动作至少改变风险、信息、身体、物件、空间或关系中的一项。
5. **选择门**：动作后果必须迫使角色继续、停下、改道、隐瞒、试探或承担代价。
6. **回收门**：规则证据需要埋设、反馈、误认或回收，不能只在对白中声明一次。

## Rule Feedback Chain

```text
正常状态
-> 角色主动试探或误触
-> 环境/物件出现第一可见反馈
-> 角色确认或误判
-> 角色采取新行动
-> 规则产生更大代价或提供可利用窗口
-> 尾帧保留物理证据
```

规则反馈优先通过火焰、门锁、灯、设备、倒影、声音距离、物件温度、表面痕迹或身体阻力表现。对白只补充画面无法证明的限制。

## Competing Permissions At A Split Threshold

Use when a loved voice/person and a survival rule demand incompatible actions at the same moment.

```text
two readable options occupy different spatial or object channels
-> each option has a distinct permitted action and trigger cost
-> intimate cue produces an involuntary body bias toward one side
-> character tests or recalls one rule proof before committing
-> choice crosses one permission boundary
-> the unchosen option leaves a physical, relational or sound residue
```

Separate `hear`, `answer`, `touch`, `cross`, `carry`, `look` and `extinguish`; they cannot be treated as one generic “interaction.” The choice must be readable before it is made. Put the relationship carrier and rule carrier in different frame zones, sound positions, hand routes or threshold sides.

### Split-Threshold Counterpart Recall

Evidence status: B-grade mechanism recall. Preserve the competing permission design; strip donor mythology and exact plot outcomes.

| Film / scene situation | Competing permissions | Spatial / blocking proof | Trigger and cost | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `Pan's Labyrinth` - intimate desire conflicts with an explicit task rule | Trust/care for a loved one versus obeying a precise object/threshold instruction | Character, doorway/object and threatened loved one occupy separate action routes | Taking, opening, eating or using the wrong object changes access | Give each choice a physical verb and visible carrier | Do not import fantasy creatures or make the rule arbitrary after the choice |
| `A Quiet Place` - helping family conflicts with the silence rule | Reach/call/save versus preserve silence and group survival | Eyeline, hand gesture, distance and sound-producing objects show who can act | A small sound has an immediate spatial consequence | Let love create bodily pressure toward the forbidden action before the choice | Do not turn silence into no sound; keep room tone, breath and object risk |
| `Talk to Me` - social/intimate contact requires spoken invitation | Hold/touch/speak permission opens access while familiar voices encourage continuation | Handheld object, seated group and watcher reactions separate public game from private contact | Spoken invitation and maintained touch define entry/exit | Permission scenes need a clear phrase/action threshold and a witness state | Strip possession ritual design; do not let entry happen before the invitation |
| `The Others` - protecting family conflicts with door/light/house rules | Open/close, believe/disbelieve and approach/keep distance carry different risks | Doors, curtains, rooms and family grouping make rule zones visible | Breaking a domestic protection rule changes who may enter or be seen | Domestic rules become dramatic when care motivates the breach | Do not import photosensitivity or identity resolution |
| `The Orphanage` - following a child's familiar game conflicts with physical safety | Continue the private ritual/search versus stop and return to ordinary space | Counting route, doorways and off-screen child sound create two directions of trust | Completing the ritual locates/admits a presence | A relationship-specific routine may be the threshold key | Strip ghost lore; preserve game sequence, sound direction and choice residue |
| `The Babadook` - caregiving requires approach while the house/voice demands avoidance | Comfort/hold the child versus respond to a threatening voice/object/door | Bed, doorway, book/object and parent-child distance define permissions | Reading, opening, answering or approaching changes the room's pressure | Let caregiving duties make total avoidance impossible | Do not import monster-book design; keep family action and threshold conflict |
| `The Blair Witch Project` - familiar cries pull the group toward a dangerous structure | Follow/respond to a companion or child-like voice versus maintain group route and orientation | Handheld light, staircase/rooms and off-screen sound position define the lure | Calling back, entering or separating changes route permission | Familiar sound should alter navigation before any source is shown | Preserve spatial cues; do not use darkness and shouting to hide all direction |
| `Pontypool` - communication is necessary while ordinary language carries risk | Speak to coordinate/help versus avoid the infected response pattern | Microphone, headphones, glass and separate listener spaces show who can hear what | Repetition/understanding/answering changes the communication state | Distinguish speaking, repeating, naming and understanding as separate permissions | Strip language-infection lore; keep the need to communicate under a verbal threshold |

## Director Rejection Conditions

- 角色无信息来源却提前回头、逃跑或知道真相。
- 为了转场临时改变物件能力或世界规则。
- 威胁凭空出现，没有画外区、遮挡、门窗、反射、声音或系统证据。
- 动作完成后人物、空间、道具和背景立即复位。
- 规则只解释，不反馈；反馈只吓人，不改变角色选择。

## SD Handoff

只把可见、可听、可执行的规则事实写入SD：

```text
触发主体 + 接触动作 + 第一反馈 + 传播方向 + 人物反应 + 尾帧残留
```

抽象规则解释留在上游，不让下游模型自行发明权限。
