---
name: director-storyboard-integrated
description: Direct animation or live-action scenes through story-readiness checks, scheme design, detailed storyboards, 4-30 second timing, dialogue-action scheduling, camera/blocking, continuity, animation-performance routing, pure-text SD handoff, and generated-result repair. Use for 分镜方案, 分镜细则, 动画分镜, 最长30秒单段动画, 运镜, 构图, 调度, 台词时间, 情景喜剧节奏, 对标拉片, 连续性, SD承接, or 视频生成结果修复.
---

# Director Storyboard Integrated

Runtime contract: `v6.0 / 2026-08-08`

本技能是六步创作链的Step 5和动画生产流程总调度。它决定故事怎样被观看，不替代上游编剧，也不替代下游SD编译。

## 每次必读

1. `references/runtime-contract.json`
2. `references/animation-production-pipeline.md`
3. `references/core-workflow.md`

动画项目再读 `../animation-suspense-performance/SKILL.md`。非动画项目按下方专项路由读取；不得批量加载参考库。

## 媒介路由

### 动画

2D、动漫、手书、Q版、混合媒介、动画角色进入真人底片，或项目已锁定为动画时：

```text
导演层：因果 / 信息权限 / 空间轴线 / 时长 / 台词窗口 / 镜头目的 / 连续性
-> 动画层：表演 / timing-spacing / 离模归模 / 画层换权 / 全画面运动
-> 合并为一份正式动画分镜
```

- 画面中承担主要表演的主体决定媒介路由；真人背景不自动把2D主角改成非动画。
- 动画正式分镜不强制写实拍摄影证据、胶片或真人材质术语。
- 2D主体进入真人底片时，动画技能读取 `../animation-suspense-performance/references/2d-live-action-handdrawn-integration.md`，只从真人侧导入透视、光向、景深、遮挡、摄影机和接触表面事实。

### 非动画

真人、实拍、拟真实拍、物理片场或真人承担主要表演时，由本技能主导。根据具体问题最多读取三份普通专项或四份复杂专项。

当真人场景需要逐镜核对世界坐标、机位朝向、画面左右、入画/出画、过肩几何或可视化沙盘时，先调用 `../live-action-spatial-previs/SKILL.md` 建立并确认空间基准，再回到本技能写正式分镜。空间沙盘不得改写剧情事实、台词或表演任务。

When a user supplies an existing video, still sequence, cut sheet, subtitle/ASR, or production artifact for reference, route evidence collection and shot-by-shot reverse analysis to ../video-story-analysis/SKILL.md before using the result as a storyboard source. A finished video, storyboard, and prompt are different evidence layers; never treat an intended plan as proof of the cut.

When a scene reference image, plan, elevation, section, or asset board must be converted into traceable environment modules before blocking, route to ../scene-asset-decomposition/SKILL.md, then pass its locked spatial master to ../live-action-spatial-previs/SKILL.md. Asset decomposition may not invent hidden geometry or actors.

### 歧义

继承当前项目已确认媒介。只有项目没有媒介锁且选择会改变产出时才询问。

## 六步权限

按 `animation-production-pipeline.md` 执行：

```text
story-framework -> script-writing -> script-roundtable -> dialogue-doctor
-> director storyboard + animation performance -> dream-suspense-sd
```

本技能可以发现上游问题，但不能静默接管：

- 项目命题、人物核心或世界规则有问题：返回 `story-framework`。
- 场景目标、行动节拍、转折或结局有问题：返回 `script-writing`。
- 用户要多视角诊断而非改稿：使用 `script-roundtable`。
- 台词声纹、潜台词或具体句子需要修改：返回 `dialogue-doctor`。
- 只有局部台词时间调度属于本技能；不得擅改已批准台词。

## 用户阶段状态机

每轮只交付用户当前请求的阶段：

```text
项目/剧本就绪
-> 场景可拍闸门
-> 分镜方案
-> 用户选择或组合
-> 分镜细则
-> 用户批准
-> 纯文本SD承接
-> 结果修复或下一段
```

- `先走流程`、`先讨论方案`：停在当前阶段。
- `进入分镜细则`：只输出正式分镜，不自动附SD。
- `进入SD承接`：调用 `dream-suspense-sd`，只输出纯文本 `BASE LOCK + A`。
- 用户描述完整流程只是更新工作方式，不代表一次输出所有阶段。
- 已确认方案不重开方案池；已批准分镜不在SD层重写。

## 场景可拍闸门

方案前内部确认：场景功能、入口状态、角色目标、阻力、策略、触发、节拍链、段内转折、退出变化和下一段债务。

以下任一成立时先修上游：

- 人物没有信息来源却提前反应。
- 角色行动只为配合镜头或笑点。
- 情景喜剧靠角色突然失智，包袱没有铺垫和反应。
- 台词只解释设定，不改变听者或行动。
- 转折靠偶然闯入且没有前置证据。
- 本段删除后剧情、关系、物件或观众认知没有损失。

规则、身份、梦境、循环、道具能力或知情差容易漂移时，追加 `story-rule-causality-gate.md`。

## 30秒段落设计

- `4-30秒`可作为一份完整方案、一份正式分镜和一条下游SD文本。
- `16-30秒`不在15秒自动切断；全段只保留一个主戏剧事务。
- 内部动作拍通常为`2-4秒`，按动作完成、台词停顿、信息改变、遮挡或镜头落点划分。
- `12-18秒`附近安排一次有因果的信息、策略、关系、物件、声音或空间刷新。
- 时间增加用于准备、听者反应、环境接力、后果和恢复，不用于并发堆动作。
- 超过30秒才按自然尾态拆新段；电影对标时长不拥有当前分段权。

## 方案阶段

返回零到六个真正不同的方案。每案写：

```text
主戏剧事务与观众体验
类型节拍和时间骨架
画面所有者变化
空间调度与摄影机主语法
动画表达主引擎或现实法则
声音/物件/环境因果
兑现尾态
AIGC风险
```

不在方案阶段输出镜头表、A区块或提示词。对标只借可迁移机制，不复制角色、剧情、台词、时长和商标视觉；不为凑数给同义方案。

### 实拍证据姿态

For live-action references, keep observation separate from inference:

- E0: title, synopsis, memory, or script; no shot, sound, or exact continuity claim.
- E1: still image; composition and visible relation only.
- E2: unordered frames; state differences only, not complete movement or cut boundaries.
- E3: continuous timed audio-video; shot, blocking, performance, edit, and listened sound within scope.
- E4: frame-verified source video; native frame and motion-phase claims within scope.

Keep method evidence separate: MTH0 impression, MTH1 public record, MTH2 interview/article, MTH3 cross-checked project artifacts, MTH4 authorized production record review. Do not infer exact lens, camera model, author intent, sound mix, or a whole-film rule from weaker evidence. Use OBS/INF/ALT/RULE labels when transferring reference observations into a formal storyboard.

## 正式分镜

用户批准方案后，重排镜头顺序并按当前故事独立计时。正式动画分镜必须包含：

```text
段级事实锁：任务 / 类型脊柱 / 入口 / 退出 / 信息权限 / 空间 / 参考 / 台词
镜号与整秒时间
戏剧变化
镜头与构图
主体与关系表演
物件/环境/NPC
动画表达
声音与台词
转场与尾帧
```

复杂动作或一镜到底再附逐拍运动台账；简单镜头不重复抄写。镜头切换或移动必须由信息、动作、空间、关系权力、反应或节奏触发，绝不因为“谁开口就切谁”。

正式分镜设计顺序：

1. 锁入口和退出变化。
2. 先做调度、轴线、屏幕方向、物件归属和画外区。
3. 再确定画面所有者、景别、机位、焦点和运动路径。
4. 通过 `dialogue-timing-scheduler.md` 分配口型、停顿、听者反应与动作并发。
5. 交给动画技能深化姿势、受力、timing/spacing、离模归模和环境接力。
6. 锁定每镜尾帧并证明下一镜第一动作如何继承。

## 专项参考路由

只在命中明确问题时读取：

| 问题 | 参考 |
|---|---|
| 台词、走位、递物、争吵、包袱停顿 | `dialogue-timing-scheduler.md`, `dialogue-physical-interaction-grammar.md` |
| 构图、焦点、轴线、复合运镜 | `composition-grammar.md`, `cinematography-execution.md`, `advanced-shot-control-gates.md` |
| 人物微表演与关系距离 | `character-performance-bible.md`, `live-action-performance-parameters.md` |
| 真人空间沙盘、机位几何、画面左右与入画状态 | `../live-action-spatial-previs/SKILL.md` |
| Existing video, cut sheet, frames, ASR, or production artifact as reference | ../video-story-analysis/SKILL.md |
| Scene image, plan, elevation, section, or asset board before blocking | ../scene-asset-decomposition/SKILL.md |
| 声源、画外声、声画错位 | `sound-design-grammar.md`, `sound-spatial-sync-counterpart-atlas.md` |
| 物件、背景、群众运动 | `active-frame-background-state.md`, `shot-object-language-library.md` |
| 连续性与段间承接 | `continuity-design-bible.md`, `episode-visual-rhythm-bible.md` |
| 悬疑结构、梦境、规则空间 | `suspense-specialty-router.md`, `dream-reality-motion-mechanisms.md` |
| 爱情、喜剧、生活、职场、青春、温情 | `genre-expansion-router.md`, `romance-shortform-counterpart-library.md` |
| 对标检索与执行风险 | `counterpart-signature-retrieval-atlas.md`, `counterpart-execution-risk-atlas.md` |
| 实拍光影、材质、摄影证据 | `photographic-evidence-training.md`, `visual-tone-texture.md` |
| SD边界与生成失败 | `storyboard-sd-compiler-contract.md`, `generation-feedback-repair-loop.md` |

停止条件：镜头已经可执行、问题已有答案时停止读参考。参考库不是完成度表。

## 动画技能协作

导演层向动画层只交付事实锁和镜头目的。动画层拥有动作因果、表演、全画面运动和表现形式；不得改剧情、台词或镜头戏剧任务。动画层发现镜头不可执行时返回具体冲突，由导演层修正后重新深化。

动画正式产物通过后，合并结果就是批准候选，不再额外生成一份“导演版”和一份“动画版”。

## SD承接

用户明确进入SD后：

1. 把当前批准正式分镜作为唯一来源。
2. 建立内部 `源镜头号 -> 时间 -> 必须事实 -> 易丢锚点 -> 尾态` 映射。
3. 调用 `dream-suspense-sd`，不手写第二套提示词框架。
4. 用户侧只交付纯文本 `BASE LOCK + A区块`；JSON仅供内部配置和验证，永不作为交付。
5. 对标作品名、来源时间、内部评分和推理不进入SD。

## 结果修复

按首个失败层返工：故事/台词 -> 正式分镜 -> 动画执行 -> SD覆盖/时序 -> 模型偏差 -> 后期。只改受影响事实，保留其他已批准内容。

## 硬规则

- 不用风格词、情绪词或镜头名替代可见动作。
- 不把中性风景介绍当作情景喜剧开场，除非景物本身制造事件。
- 不机械正反打；优先动作、反应、空间和多线群戏调度。
- 不让所有NPC同拍同幅反应，不让环境冻结等台词。
- 不用特效遮盖表演、空间或连续性错误。
- 不擅改用户已确认的人设、台词、参考绑定、尾态和时长。
- 不因精简丢失因果；精简只删除重复归属、重复形容和不变事实。
- 不输出用户侧JSON SD。

## 验证

```powershell
python scripts/validate_storyboard_sd.py <storyboard.md> --mode storyboard
python scripts/validate_storyboard_sd.py <execution.md> --mode sd --source-storyboard <approved-storyboard.md>
powershell -ExecutionPolicy Bypass -File scripts/run_static_regression.ps1 -Python <python.exe>
```

结构通过不等于导演成立。最终仍检查：场景有损可删性、行动因果、台词功能、镜头触发、动画归还、30秒中段刷新、尾帧继承和来源100%覆盖。
