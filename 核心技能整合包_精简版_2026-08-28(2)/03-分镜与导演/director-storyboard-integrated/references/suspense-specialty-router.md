# Suspense Specialty Router

用途：作为悬疑电影分镜技能的第一层专项路由，防止每次都把所有导演库、结构库、质感库一股脑加载。  
目标：先判断“这到底是哪一类悬疑场景”，再进入结构机制、场景机制、导演语法和输出字段。

---

## 目录

- [0. Task Mode And Read Budget](#0-task-mode-and-read-budget)
- [1. 四段路由](#1-四段路由)
- [2. 悬疑子类型速查](#2-悬疑子类型速查)
- [3. 选库规则](#3-选库规则)
- [4. 正式设计前的路由句](#4-正式设计前的路由句)
- [5. 反例边界](#5-反例边界)

---

## 0. Task Mode And Read Budget

Route by task mode before scene subtype. Do not load reference files because they sound generally relevant.

| Task mode | Base reads | Specialist budget | Stop condition |
|---|---|---:|---|
| 方案池 / 场景讨论 | `runtime-contract.json` + `core-workflow.md` + this router | 2-3 | 返回0-6个有实际帮助的多电影分镜机制方案，不凑数；不要求时间码、等时或单片绑定；零命中时进入原创方案 |
| 正式细致分镜 | above + `suspense-quality-gate.md` + `output-templates.md` | 3-4 | Full shot fields and continuity are covered |
| 对标拉片 | `counterpart-radar-shot-index.md`; add `counterpart-signature-retrieval-atlas.md` for mixed scenes/visual frames | 2 | One broad pool plus one precision mechanism pool is enough |
| SD / Seedance 转写 | `storyboard-sd-compiler-contract.md` + continuity reference | 1 repair library when needed | Every storyboard row maps to BASE or the five-field A beats without loss; E stays internal/attachment-only |
| 生成结果回修 | `generation-feedback-repair-loop.md` | 1 failure-specific library | Failure layer is located and repaired at source |
| 非悬疑类型场景 | `genre-expansion-router.md` | 1 genre library + 1 execution library | Genre engine and physical carrier are clear |

Hard budget rules:

- Ordinary scene design: load no more than 3 specialist references after the base reads.
- Important multi-scene or spatially complex work: no more than 4 specialist references unless the user explicitly requests a comprehensive audit.
- Prefer one reference that directly solves the failure over three references that repeat the same advice.
- Stop reading when composition, camera, light, texture, action, sound, transition, continuity, and narrative purpose are all executable.

---

## 1. 四段路由

```text
悬疑子类型 -> 结构机制 -> 场景执行机制 -> 导演语法
```

- 悬疑子类型：这场属于哪一种悬疑电影任务。
- 结构机制：故事如何隐藏/改写信息。
- 场景执行机制：镜头如何在这一场制造压力。
- 导演语法：选择哪一种风格和视听控制方式。

当任务属于爱情、喜剧、生活、职场、青春或温情家庭，先切换到 `genre-expansion-router.md`，再复用摄影、表演、声音、连续性和SD承接层。

---

## 2. 悬疑子类型速查

| 子类型 | 核心问题 | 优先读取 | 禁止误区 |
|---|---|---|---|
| 密闭规则悬疑 | 角色如何理解空间规则并尝试逃离 | `structural-suspense-benchmark-library.md`, `scene-family-realism-router.md`, `canzhu-counterpart-library.md` if Residual Candle | 不要先解释规则，先拍规则证据 |
| 走廊追逐/空间压迫 | 跑动中如何让空间越来越不可信 | `advanced-suspense-scene-mechanism-library.md`, `structural-suspense-benchmark-library.md`, `cinematography-execution.md` | 不要只写奔跑，要写空间变化和身体消耗 |
| 心理对峙/审问 | 谁掌控话语、眼神和沉默 | `advanced-suspense-scene-mechanism-library.md`, `director-dispatch.md`, `sound-design-grammar.md` | 不要只有台词，手、眼、杯子、出口都要参与 |
| 规则物/证据物 | 小物件如何承载世界规则 | `scene-family-realism-router.md`, `composition-grammar.md`, `photographic-evidence-training.md` | 不要只写物件名称，要写材质、接触和状态变化 |
| 梦境/幻觉/现实错位 | 空间如何物理化精神状态 | `dream-reality-motion-mechanisms.md`, `structural-suspense-benchmark-library.md`, `visual-tone-texture.md` | 不要说“梦境感”，要写不变量、触发、变形过程、身体接触和残留 |
| 异常收容/不可见威胁 | 看不见或不确定的威胁如何被确认 | `advanced-suspense-scene-mechanism-library.md`, `scene-family-realism-router.md`, `sound-design-grammar.md` | 不要急着露出威胁全貌，先拍环境和设备反应 |
| 社会伪装/礼貌压迫 | 正常关系如何变成控制 | `advanced-suspense-scene-mechanism-library.md`, `screen-action-breakdown.md`, `sound-design-grammar.md` | 不要把威胁写成大喊，礼貌和微笑也能压迫 |
| 仪式/群体压迫 | 群体如何吞掉个人 | `advanced-suspense-scene-mechanism-library.md`, `visual-tone-texture.md`, `sound-design-grammar.md` | 不要只写“邪教感”，要写队形、同步动作、声音 |
| 调查/推理/系统压迫 | 证据如何排列，系统如何压人 | `top-director-suspense-shot-training-library.md`, `suspense-composition-benchmark-library.md`, `composition-grammar.md` | 不要只讲线索，要拍证据平面和程序压力 |
| 结尾反转/身份覆写 | 最后一镜如何改写前文 | `structural-suspense-benchmark-library.md`, `advanced-shot-control-gates.md`, `episode-visual-rhythm-bible.md` | 不要新增真相，必须回收旧证据 |
| 字段完整但镜头仍平 | 注意力和镜间变化如何被控制 | `advanced-shot-control-gates.md`, `suspense-quality-gate.md` | 不要继续堆风格词或无理由加镜头 |
| 材质/物件/天气/制度证据 | 物理表面和日常物件如何改变信息、权力与行动 | `material-social-story-language.md`, `shot-object-language-library.md` | 不要把材质和制度物件写成布景装饰 |
| 复合场景/单幅画面反推 | 一个画面同时包含动作、空间、信息差、载体与节奏时，哪些电影分镜机制能帮助当前设计 | `counterpart-signature-retrieval-atlas.md`, `counterpart-radar-shot-index.md` | 先做五轴指纹，返回0-6个可复用机制；允许用户组合，正式分镜重新定时并统一导演语法 |
| 对话同时走位/操作道具 | 如何保护口型、主路线、听者反应和背景动作 | `dialogue-physical-interaction-grammar.md`, `counterpart-execution-risk-atlas.md`, `character-performance-bible.md` | 不要让说话、走路、手部、听者和背景在同一秒都成为主动作 |
| 跌撞/急停/挤门/障碍接触 | 身体受力、镜头反应和恢复状态如何连续 | `dialogue-physical-interaction-grammar.md`, `counterpart-execution-risk-atlas.md`, `cinematography-execution.md` | 不要只写踉跄或撞墙，要写力、接触、惯性、恢复和痕迹 |
| 多人/NPC/道具/环境运动生态 | 主体、陪体、背景人物、物件、机械、天气、植物、光影、摄影机和声音如何形成因果运动链；谁看见、听见、知道、误判或装作不知道 | `active-frame-background-state.md`; add `motion-ecology-counterpart-atlas.md` ME-A to ME-J for film matching | 不要让背景死站，也不要让所有层随机乱动、同步抢戏或提前知道信息 |
| 规则权限/剧情因果风险 | 谁能触发规则、角色凭什么反应、动作造成什么后果 | `story-rule-causality-gate.md` | 不要为了漂亮转场临时改变规则、物件能力或角色知识 |
| 台词时长/口型并发 | 中文台词、停顿、重音、动作和听者反应是否塞得下 | `dialogue-timing-scheduler.md`, `dialogue-physical-interaction-grammar.md` | 不要只按字面台词排时间；标点、吸气、打断和动作都占窗口 |
| 高风险AIGC镜头 | 导演最优方案如何拆成模型可执行版本 | `aigc-execution-risk-calibration.md`, `storyboard-sd-compiler-contract.md` | 不要用删细节解决过载；先分轨、拆段或改用稳定覆盖机制 |

---

## 3. 选库规则

最少读取原则：

- 普通分镜：`core-workflow.md` + 本路由 + 相关1-3个专项库。
- 《残烛》：当前任务明确命名项目时，在工作区定位并读取 `残烛_故事设定.md`，再根据场景读取 `canzhu-counterpart-library.md`。
- 用户要求“SD输出”：先完成分镜，再交给 `dream-suspense-sd`。
- 用户点名某种运镜、组合运镜、剪辑或转场技法：仍按当前场景的悬疑子类型路由，执行层统一读取 `cinematography-execution.md`；需要电影例证时再加 `classic-film-lens-reference.md`，不得为环绕、甩镜、闪切、闪回、变焦或某种转场单开场景路线。

避免重复：

- `structural-suspense-benchmark-library.md` 管结构，不管场景质感细节。
- `advanced-suspense-scene-mechanism-library.md` 管场景执行，不管故事反转设定。
- `top-director-suspense-shot-training-library.md` 管导演风格，不管所有场景都必须像五位导演。
- `scene-family-realism-router.md` 管实拍质感，不替代构图、剧情和声音。
- `suspense-composition-benchmark-library.md` 管构图骨架，不替代结构悬疑。

---

## 4. 正式设计前的路由句

任何重要分镜前先内部回答：

```text
悬疑子类型：
结构机制：
场景执行机制：
主导演语法：
需要读取的专项库：
不读取的库及原因：
```

输出给用户时可压缩为：

```text
主控判断：这场是 X 型悬疑，主结构是 Y，场景机制用 Z，导演语法选 N。
```

---

## 5. 反例边界

- 不要因为用户说“悬疑”就加载所有悬疑库。
- 每个4-30秒段定版后只保留一份批准的正式分镜作为执行来源。上游可参考多部电影，但电影不绑定秒数、镜头顺序或SD来源；下一段继承连续性总线。
- 不要让结构库、场景机制库、质感库互相替代。
- 不要在正式分镜中省略路由结果，否则后续SD转译容易丢重点。
- 不要跑向泛影视、商业广告、奇幻大片训练；本路由只服务悬疑电影/悬疑短剧分镜。
