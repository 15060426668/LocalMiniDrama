# AIGC Execution Risk Calibration

用途：在导演最优方案与模型可执行性之间做明确判断。复杂镜头保留创意，但必须知道何时拆段、降载或准备稳定替代方案。

## Risk Score

| 系统 | 分值 |
|---|---:|
| 单一摄影机路径 | 1 |
| 每个主要人物动作 | 1 |
| 关键道具交互 | 1 |
| 明显背景事件 | 1 |
| 对话口型叠加大动作 | 1 |
| 环境/VFX连续变化 | 2 |
| 第二种材质或空间变化逻辑 | 2 |
| 身份、服装或身体变形 | 2 |
| 多人同时独立走位 | 2 |

判定：`0-3`直接执行；`4-5`分轨并保护落点；`6+`拆段。两条摄影机路径、两次转场或两个说话口型同时竞争时直接拆分。

## Two-Version Design

高风险镜头内部准备两个版本：

```text
导演最优版：保留最强空间、表演或转场机制。
AIGC稳定版：保持同一叙事结果，改用遮挡、门框、灯灭、动作匹配、声桥、焦点交接或分镜覆盖。
```

稳定版不是降低美学，而是降低模型同时理解的运动系统数量。

## Common Risk Repairs

| 风险 | 优先修复 |
|---|---|
| 人物动作被镜头运动吞掉 | 主体与摄影机分轨；降低其中一条幅度 |
| 多人对话口型错乱 | 一次只保留一个可见说话口；反方用反应和画外声 |
| 梦境变形随机 | 一镜只保留一种物质逻辑和一条移动边界 |
| 道具跳手或消失 | 锁所有者、手、朝向、接触顺序和尾帧位置 |
| 空间方向漂移 | 锁门窗方位、屏幕方向、摄影机侧和落幅 |
| 低照度变成纯黑 | 增加可信实用光、材质反光和可读中间调 |
| 背景人物冻结 | 赋予持续任务和延迟反应，不增加第二主戏 |
| 背景过度活跃 | 只保留一个环境力家族和一个注意力所有者 |

## Cross-Mechanism Collision Calibration

When two strong mechanisms share one 4-30 second segment, assign one dramatic owner and sequence the other as proof, pressure, midpoint turn or tail residue rather than simultaneous competition.

| Combination | Primary owner | Supporting layer | Split line | Stable coverage translation |
|---|---|---|---|---|
| recognition reveal + rule/threshold choice | hand/contact distance or response permission | familiar voice/gesture and one rule object | split when full face, lip-sync, object change and doorway motion compete | locked two-zone frame -> close hand/object choice; one speaking mouth, one camera path |
| route verification + identity/self-anchor failure | route marker and its wrong-side return | one body/private anchor | split when moving route, marker creation, spatial inversion and object-ownership failure occur together | mark-and-depart beat -> return/retest/new-door beat with identical marker defect and screen direction |
| institutional debrief + custody breach | evidence handoff/checkpoint | official explanation and witness knowledge states | split when more than one visible speaker, screen change, handoff and door event overlap | intake/handoff -> checkpoint/second system -> custody/door landing |
| ensemble cover story + silent aftermath | premature reaction or repair action | public routine, object transfer and missing sound | split when three or more background reactions become independently important | group baseline/contradiction -> ownership change -> quiet consequence frame |

Hard collision rules:

- Two primary camera paths never share one beat.
- One beat may contain one visible speaking mouth and one major hand/object action; move the other line off-screen or into the next beat.
- Face reveal, identity change and spatial deformation are three different high-risk systems. Keep at most one active.
- A background clue remains subordinate until the camera/focus hands it ownership.
- Tail residue is not a second climax. It records consequence and prepares the next objective.

## Calibration Record

每次真实生成失败记录：

```text
模型/版本：
输入类型：文生视频 / 图生视频 / 首尾帧 / 多镜头
源分镜号：
复杂度分数：
预期关键动作：
实际失败：
第一失败层：分镜 / 编译 / 模型 / 连续性 / 真实度 / 声画 / VFX
修复字段：
是否拆段：
第二次结果：
可沉淀规则：
```

没有实际结果证据时，只能写“预计风险”，不能写成模型成功结论。
