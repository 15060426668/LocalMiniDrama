# High Intensity Suspense Training Loop

用途：高强度悬疑电影专项训练流程。  
目标：多投、多喂、多吃，但不跑偏、不堆垃圾、不让技能臃肿；每一批训练都必须沉淀为可触发、可调用、可自检的能力。

---

## 目录

- [1. 训练边界](#1-训练边界)
- [2. 每批训练结构](#2-每批训练结构)
- [3. 高强度训练批次规划](#3-高强度训练批次规划)
  - [Batch A–G：基础画面、光影、声音、节奏、结构、SD与审查](#batch-a画面可视化纠偏)
  - [Batch H–N：结果修复、连续性、表演、整集节奏与复合场景](#batch-h生成结果反修压测)
  - [Batch O–S：运动生态、因果、台词、生成校准与语法移植](#batch-o逐镜运动生态压测)
  - [Batch T：摄影机、剪辑与转场组合语法](#batch-t摄影机剪辑与转场组合语法压测)
  - [Batch U：预告片节奏与短剧波形](#batch-u预告片节奏与短剧波形压测)
- [4. 单批训练流程](#4-单批训练流程)
- [5. 精简原则](#5-精简原则)
- [6. 自我迭代闭环](#6-自我迭代闭环)

---

## 1. 训练边界

只训练：

- 悬疑电影
- 惊悚化悬疑
- 心理悬疑
- 科幻悬疑
- 密闭空间
- 调查推理
- 梦境幻觉
- 规则/收容
- 异常/不可见威胁
- 仪式/群体压迫
- 社会伪装恐惧
- AIGC悬疑短剧分镜转译

悬疑主训练池不吸收：

- 泛商业广告
- 与悬疑机制无关的普通甜宠、喜剧和古偶素材
- 无悬疑目的的动作爽片
- 只看美术不服务悬念的纯视觉风格
- 无法转译成分镜字段的空泛影评
- 血腥展示、猎奇特写、贴脸巨响、虐杀奇观、为刺激而刺激的惊吓片段

主动训练池优先使用 `censorship-safe-suspense-training-batches.md`。经典片段如果包含不适合短剧审查的画面，只拆信息控制、遮挡、反应镜头、声音留白、空间调度、物件状态和事件痕迹。

用户明确请求爱情、浪漫喜剧、生活流、职场、青春或温情家庭时，素材进入 `genre-expansion-router.md` 对应的独立类型库，不污染悬疑主动训练池。

---

## 2. 每批训练结构

每批训练必须包含：

```text
训练批次：
专项方向：
目标失败点：
代表素材：
素材可信度等级：A / B / C
拆解字段：
提炼结果：
写入模块：
验证方式：
```

标准拆解字段：

```text
场景类型：
片段时长：仅A级视频、时间码或用户明确锁定时填写
每个可见节拍发生了什么：未核验来源按动作阶段记录，不伪造逐秒事实
镜头表：
构图画面：
机位与运镜：
光影/色彩：
画面基调/质感：
实拍摄影证据：
画面内容：
运动生态/层级交互：
声音设计：
转场：
复刻保留项：
当前场景替换项：
SD承接锚点：
```

标准提炼结果：

```text
可复用规则：
反例边界：
可迁移镜头模板：
应写入哪个模块：
触发关键词：
质量门槛：
```

每批必须写出 `SD承接锚点`。没有锚点的素材只能作为口头参考，不能沉淀进正式技能库。

Every accepted training sample must also answer:

```text
为什么是这个焦段：
为什么是这个机位：
为什么在这里切：
最脆弱的构图层：
最脆弱的动作细节：
光源/材质证据：
声音触发：
尾帧状态：
源分镜镜头号 -> A区块时间段 -> E区块索引：
```

If these answers are missing, repair the training decomposition before depositing it. The downstream SD layer must not invent missing blocking, camera, light, material, sound, transition, or continuity logic.

For large generated training tables, first audit the claimed batch count, actual section count, declared field/layer count versus enumerated contents, whether a duration describes a shot/beat/scene, and repeated rows or templated parameters. Treat invented focal lengths, light percentages, Hz, dB, exact durations and micro-actions as C-grade named-film facts. Retain only mechanisms that survive removal of those parameters, then rewrite them as a compact rule, failure boundary, transferable template and SD anchor.

### Source Normalization Gate

Use `counterpart-source-register.md` as the canonical evidence policy. Large existing film pools default to B-grade mechanism recall until the current task verifies the clip, frame, transcript or production source.

Classify every supplied or researched scene detail before depositing it:

| Grade | Meaning | Deposit rule |
|---|---|---|
| A: observed/verified | visible or audible in the supplied clip/frame/transcript, or confirmed by a reliable production source | may remain attached to the named film scene |
| B: mechanism-level reliable | the scene mechanism is reliable, but exact timing, prop, light, sound or background detail is not verified | deposit only the general mechanism; remove exact invented detail and soften attribution |
| C: interpretive/invented | symbolic reading, imagined set dressing, fabricated micro-action, unsupported timing or merged scene detail | do not store as film fact; convert only into an original generic template when useful |

Required normalization pass:

```text
observed fact
-> inferred mechanism
-> unsupported embellishment removed
-> censorship-safe transferable rule
-> short-form timing adaptation
-> SD-positive execution anchor
```

### Story-World Contamination Firewall

Film worldbuilding is a donor variable, not a reusable storyboard rule. Before depositing any mechanism, remove:

- franchise mythology, supernatural explanation, historical lore or named organization.
- specific character identity, relationship, dialogue, costume, weapon or iconic production design.
- plot-resolution facts such as who the killer is, why the universe split, what monster rule explains the scene or how the film ends.
- donor-specific moral slogan when the reusable function is actually power, access, secrecy, guilt, care, class, institutional control or group permission.

Preserve only:

```text
dramatic function
/ spatial relation and information permission
/ camera and blocking mechanism
/ object or material proof
/ rhythm, sound and transition logic
/ failure boundary
/ current-story replacement variables
```

Anonymous-card test: remove the film title and every proper noun. If the card no longer explains a shootable mechanism, it is plot memory rather than training material and must be rewritten or rejected.

Examples:

```text
comet + parallel universes + colored glow sticks
-> crossing an unlit threshold changes version
-> a carried color/object tag records route identity
-> object ownership or person count proves the wrong version

armored safe room + intruders
-> protected threshold also creates confinement
-> inside and outside parties compete for lock, air, vision, communication and exit permission
```

Keep the dramatic relationship but replace the donor explanation. “Everyone knows except the protagonist” may become performed normality and delayed information permission; it must not carry the donor cult, conspiracy, race, family or ritual plot into an unrelated scene.

Do not treat absolute claims as universal laws. Normalize them:

- sound may lead, coincide with or follow the visible action; choose the causal owner per beat.
- background cycles may continue, be interrupted or change state when the main action physically reaches them.
- NPC knowledge distribution is scene-specific; do not use a fixed percentage of unaware people.
- stillness baseline in short-form is usually 1-3 seconds or established by repetition across earlier shots, not a feature-film-length hold.
- camera height may track bodily/status descent only when the spatial and emotional axis supports it.
- an unrelated intrusion works only when the object/person/system was already plausible in the environment.

---

## 3. 高强度训练批次规划

### Batch A：画面可视化纠偏

目标失败点：构图只有功能解释，画面内容像阅读理解。  
主调库：`complaint-driven-correction-library.md` C01/C03。  
素材方向：走廊追逐、规则物特写、门后恐怖、家庭房间、审问对峙。  
验收：删除抽象词后仍能画出镜头。

### Batch B：光影质感纠偏

目标失败点：冷色调三个字、电影感空泛、实拍证据不足。  
主调库：`visual-tone-texture.md`, `photographic-evidence-training.md`, `scene-family-realism-router.md`。  
素材方向：雨夜、病房、舰桥、家庭房间、工业走廊、白昼仪式。  
验收：每镜有光源、方向、材质、黑位、颗粒/镜头特性。

### Batch C：声音与声画关系

目标失败点：声音只有环境音/紧张音乐。  
主调库：`sound-design-grammar.md`, `complaint-driven-correction-library.md` C04。  
素材方向：画外脚步、电话、规则声、静音钩子、仪式声、机械低频。  
验收：每镜至少有声源、距离、层次、变化、触发表演反应。

### Batch D：短剧节奏压缩

目标失败点：电影节奏太慢，单镜头停太久。  
主调库：`aigc-short-drama-rhythm-library.md`, `suspense-quality-gate.md`。  
素材方向：开场3秒钩子、15秒认知改写、快剪规则交代、追逐开场。  
验收：0-3秒有钩子，8-15秒有认知变化，固定镜头1-4秒刷新。

### Batch E：结构与对标强化

目标失败点：没有对标、结构空、只套风格。  
主调库：`suspense-specialty-router.md`, `structural-suspense-benchmark-library.md`, `advanced-suspense-scene-mechanism-library.md`。  
素材方向：循环、身份反转、密闭群像、背景慢速威胁、礼貌压迫、不可见巨物。  
验收：先自适应拆段；针对当前场景提供0-6个有实际帮助的电影分镜机制，不凑数，不要求等时或单片绑定。人物、认知、环境、道具和剧情变量允许替换；用户可选择或组合机制，随后按当前短片重新定时并形成统一导演方案。

### Batch F：SD无损转译

目标失败点：分镜细节在SD里丢失。  
主调库：`dream-suspense-sd`, `suspense-quality-gate.md`, `complaint-driven-correction-library.md` C06。  
素材方向：分镜转A/E、转场特效正向词、声音轨同步、15秒分段。  
验收：A区块逐镜继承，不超过15秒，只正向词。

### Batch G：审查友好悬疑训练池

目标失败点：素材越喂越杂，主动训练口味偏向血腥、贴脸、重刺激。  
主调库：`censorship-safe-suspense-training-batches.md`, `suspense-scene-motif-index.md`。  
素材方向：走廊追逐、门/阈限、家庭对峙、规则物、声音先导、梦境错位、事件痕迹、系统锁定。  
验收：每条素材都有单一片段来源、复刻保留项、当前场景替换项和SD承接锚点；主动模板只保留心理压力、信息差、空间压迫、声音和物件证据。

### Batch H：生成结果反修压测

目标失败点：分镜和SD都写了，但出图/视频仍然不对，只会盲目重写提示词。  
主调库：`generation-feedback-repair-loop.md`, `storyboard-sd-compiler-contract.md`, `suspense-quality-gate.md`。  
素材方向：出图不像实拍、动作丢失、空间方向错、光源漂移、人物连续性崩、转场没兑现、声画不同步、15秒段落过载。  
验收：每个失败案例必须定位失败层：分镜源表 / A区块编译 / 模型执行 / 连续性 / 真实度 / 节奏 / 声画 / VFX；并给出回修字段、正向执行锚点、是否拆段、是否需要参考图或尾帧继承。

### Batch I：连续性设计总线压测

目标失败点：单镜头漂亮，但跨镜头后空间、服装、道具、光源、色彩和声音像不同场戏。  
主调库：`continuity-design-bible.md`, `storyboard-sd-compiler-contract.md`, `photographic-evidence-training.md`。  
素材方向：走廊追逐跨门转场、病房醒来接规则物、家庭争吵从客厅到门口、太空舰桥多屏幕对话、梦境坍塌接现实落地、多人围绕证据物。  
验收：每个训练样本必须给出连续性总线：空间地图、屏幕方向、主光方向、色彩剧本、场景陈设、关键道具状态链、服装/妆发/身体状态链、声音尾巴、尾帧继承、SD稳定锚点。

### Batch J：角色表演圣经压测

目标失败点：角色每个镜头都像临时表演，只会写害怕、生气、冷静，缺少稳定身体语言和SD可继承动作。  
主调库：`character-performance-bible.md`, `screen-action-breakdown.md`, `director-core-shot-language.md`。  
素材方向：克制式恐惧、礼貌式恐惧、冷静压迫、家庭争吵升级、专业角色醒来/追逐/调查、反应镜头、崩溃前重复动作。  
验收：每个主要角色必须给出表演指纹：身体基准、眼神习惯、手部习惯、步态/站姿、压力反应、职业动作、关系动作、情绪升级链、崩溃边界、SD角色动作锚点。

### Batch K：整集视觉节奏与钩子链压测

目标失败点：单镜头漂亮，但整段散；15秒没有新钩子，30秒没有问题转向，多SD段之间尾帧断裂。  
主调库：`episode-visual-rhythm-bible.md`, `aigc-short-drama-rhythm-library.md`, `continuity-design-bible.md`, `storyboard-sd-compiler-contract.md`。  
素材方向：高留存开场、预告快剪、走廊追逐接房间醒来、病房规则接第一次试探、家庭争吵接物件反转、舰桥锁定接地面危机、梦境坍塌接现实落地。  
验收：每个样本必须给出段落目标、观众问题、角色目标、主悬念载体、0-3秒视觉问题、3-8秒身体任务、8-15秒信息变化、尾帧钩子、下一段继承、SD段落边界。

### Batch L：心理恐怖压抑环境压测

目标失败点：场景有雨夜、旅馆、病房、走廊、房间等元素，但环境只是背景，没有持续压迫人物认知。  
主调库：`psychological-atmosphere-benchmark-library.md`, `structural-suspense-benchmark-library.md`, `scene-family-realism-router.md`, `sound-design-grammar.md`。  
素材方向：`Identity / 致命ID` 雨夜旅馆密闭群像，`Memento / 记忆碎片` 失忆证据物，`Shutter Island` 机构空间和真相层级，`The Machinist` 身体/工业噪声，`Cure` 静态感染，`The Others` 光线禁忌，`Coherence` 餐桌现实分叉；第二批重点补 `The Babadook` 家庭空间污染，`Relic` 老屋记忆污染，`Repulsion` 独居房间裂变，`Rosemary's Baby` 邻里礼貌压迫，`The Invitation` 晚餐聚会出口控制，`Saint Maud` 独居仪式焦虑，`Take Shelter` 预感风暴，`Safe` 现代空间身体焦虑，`Burning` 日常缺席悬念，`The Vanishing` 消失证据链；第三批重点补 `The Conversation` 偏执监听，`Cache` 监控固定机位，`The Tenant` 公寓邻里偏执，`The Innocents` 儿童视角，`Lake Mungo` 伪纪录影像证据，`The Father` 认知布景漂移，`I'm Thinking of Ending Things` 车内时间泄漏，`Martha Marcy May Marlene` 创伤闪回无缝错接，`The Night House` 建筑负形，`Picnic at Hanging Rock` 白昼自然缺席。  
验收：每个样本必须给出空间压迫、错位物件、环境声变化、人物身体微反应、认知改写点、尾帧证据物、SD承接锚点。主动训练只保留心理压力、环境证据、声音层次和结构认知，不训练血腥展示、贴脸惊吓或猎奇结果。

### Batch M：复合场景多片机制检索压测

目标失败点：面对一句复合场景或一张画面时，候选来源混杂，筛选后仍把多部电影拼进同一运镜。  
主调库：`counterpart-signature-retrieval-atlas.md`, `counterpart-radar-shot-index.md`, `classic-film-lens-reference.md`, `suspense-quality-gate.md`。  
素材方向：多人阵营变化、跨切镜声音透视、整段焦段连续、强调色回收、微动作触发运镜/剪点、前景主戏与背景第二叙事。  
验收：先自适应拆段，不套固定数字模板；为当前场景生成五轴指纹，返回0-6个有用电影机制，每项包含构图、运镜、调度、节奏、声音、转场、替换变量、风险和AIGC可执行性。零命中不补位；用户可单选或组合，随后统一导演语法并按当前短片重新定时。下一段通过连续性总线承接。

### Batch N：对话并发与身体/物体交互压测

目标失败点：人物边说边走时口型、手势、听者和背景动作互相抢占；递物缺少重量转移；跌撞急停只有动作标签；门、墙、楼梯、地面和车辆缺少真实阻力。  
主调库：`dialogue-physical-interaction-grammar.md`, `counterpart-execution-risk-atlas.md`, `character-performance-bible.md`, `cinematography-execution.md`。  
素材方向：坐姿对话、walk-and-talk、争吵越界、工作中对话、三人谈话、电话交互、递物；起跑、急停、打滑、撞墙、挤门、上下楼、搬重物、车辆惯性、狭窄空间。  
验收：对话节拍分出口型窗口、主路线、手部、听者、背景、摄影机和声音七轨；物件交接写接触和重量转移；碰撞写力源、接触、阻力、惯性、恢复、残留与下一动作后果。

### Batch O：逐镜运动生态压测

目标失败点：分镜像静态构图说明；只有主角在动；NPC死站；风、雨、水滴、植物、门窗、布料、机械和光影各自随机运动；镜头结束后没有残留状态。  
主调库：`active-frame-background-state.md`, `motion-ecology-counterpart-atlas.md`, `dialogue-physical-interaction-grammar.md`, `screen-action-breakdown.md`, `sound-design-grammar.md`。  
素材方向：多人家庭对话、办公室/医院群像、街道/商场人流、风雨外景、交通工具、追逐穿越活场景、安静房间中的风扇/窗帘/植物/水滴、机械设备与灯光周期。  
验收：十组ME-A至ME-J每组至少命中一个机制；每镜给注意力所有者、信息权限/知情状态、主运动、1-2个反应层、一个环境力家族、NPC状态、道具/机械后果、光影摄影机变化、声音触发、残留和尾帧；所有运动共享因果来源并保持注意力层级。

### Batch P：故事规则与因果权限压测

目标失败点：角色提前知道信息；规则触发者和外力边界不清；物件能力为镜头临时改变；动作结束后没有后果。  
主调库：`story-rule-causality-gate.md`, `continuity-design-bible.md`, `shot-object-language-library.md`。  
素材方向：规则物试探、梦境层级切换、收容操作、门锁权限、火焰/灯光反馈、身份误认、旧证据回收。  
验收：每个样本写清角色已知/未知、触发主体、允许动作、外力边界、第一反馈、直接后果、残留状态和下一步选择；镜头机制不得创造新规则。

### Batch Q：中文台词时间与口型并发压测

目标失败点：15秒台词塞满；口型、走位、递物、听者和镜头互相抢占；争吵只有音量升级。  
主调库：`dialogue-timing-scheduler.md`, `dialogue-physical-interaction-grammar.md`, `character-performance-bible.md`。  
素材方向：克制审问、边走边谈、家庭争吵、规则音、电话对话、工作中对话、三人阵营变化。  
验收：按中文语速估算口型窗口；标出起句准备、重音、停顿、尾音；重大转身、递物和碰撞落在停顿或独立节拍；每次升级改变行动权限而不只是提高音量。

### Batch R：真实模型生成校准压测

目标失败点：理论提示词完整，但不同模型仍出现动作丢失、转场随机、口型错乱、空间漂移或低照度纯黑。  
主调库：`aigc-execution-risk-calibration.md`, `generation-feedback-repair-loop.md`，以及下游 `dream-suspense-sd` 的 [generation calibration ledger](../../dream-suspense-sd/references/generation-calibration-ledger.md)。  
素材方向：同一分镜在目标模型上的原始输出、一次修复、二次输出；图生视频和文生视频分开记录。  
验收：记录模型版本、输入模式、复杂度、第一失败层和修复字段；单次成功不升级规则，同类三次稳定成功后才进入模型配置。

### Batch S：分镜语法移植压测

目标失败点：把对标误解为剧情、身份和人物认知必须一致，导致《盗梦空间》《红辣椒》等可用分镜因语义不同被错误排除；或只看题材相似而忽略摄影机与调度根本搬不动。  
主调库：`counterpart-signature-retrieval-atlas.md`, `counterpart-radar-shot-index.md`, `counterpart-source-register.md`。  
验收：每个候选分别写清 `保留的分镜语法` 与 `替换的故事变量`；至少四项分镜轴可搬用才进入候选，人物身份、是否知情、环境、道具、台词和剧情原因不作为淘汰条件。

重复醒来、运动中关联换景、跨空间同步触发和旋转重力统一读取 `dream-reality-motion-mechanisms.md`；此处不再重复长镜头表。

| 训练片段 | 保留的分镜语法 | 可替换变量 |
|---|---|---|
| `The Shining` 走廊移动 | 中轴纵深、低位持续前进、转角延迟、重复空间增压 | 儿童、酒店、交通工具、走廊陈设与威胁 |
| `The Others` 门与光线边界 | 门缝信息控制、开门节奏、暗区保留、声源先行 | 老宅、人物关系、门后内容与规则原因 |
| `Memento` 汽车旅馆证据盘点 | 醒后身体检查、物件扫描、焦点交接、信息逐项落地 | 失忆设定、照片/纹身、房间类型与线索意义 |
| `The Silence of the Lambs` 初见汉尼拔 | 走廊进入、正面凝视、景别权力变化、玻璃边界 | 警探/囚犯身份、谈话目的、制度空间与台词 |
| `The Invitation` 晚餐控制出口 | 群像中广景、门位负空间、主人移动封路、背景微反应 | 聚会关系、威胁原因、餐桌道具与出口类型 |
| `It Follows` 背景慢速接近 | 前景日常任务、背景单点移动、焦点延迟、距离递减 | 超自然设定、追逐者身份、公共空间与主角任务 |
| `Parasite` 桌下/客厅躲藏 | 广角空间图、前中后景并行、声音先行、身体按层收缩 | 阶级剧情、住宅、藏身人物、回家者身份与道具 |

### Batch T：摄影机、剪辑与转场组合语法压测

目标失败点：只会罗列“推、拉、摇、移、环绕、闪切、闪回、希区柯克变焦”等名称；或把每个新术语单独建库、单独路由，却没有主运动、次运动、光学变化、焦点路线、剪辑接口和落点之间的组合规则。  
主调库：`cinematography-execution.md`, `classic-film-lens-reference.md`, `counterpart-source-register.md`。  
素材方向：轴向推拉、横移、跟随、领先、平行移动、升降、摇移修正、环绕/弧线、滚转、焦点转移、光学变焦、闪帧侵入、动作峰值闪切、物件/声音触发闪回、dolly zoom、crash zoom、whip pan、match cut、遮挡擦镜、环绕转场、反应蒙太奇，以及两至三种算子的可控组合。  
验收：每条样本归一化为 `戏剧任务 -> 主运动 -> 次级方向/光学算子 -> 焦点路线 -> 剪辑或转场耦合 -> 落幅 -> 信息变化 -> 声音桥 -> 尾帧`；区分机内连续动作与剪辑拼接；记录组合负载和失败边界。新术语只能补充既有算子或组合模板，不得自动生成新的场景路线或独立文件。

### Batch U：预告片节奏与短剧波形压测

目标失败点：把预告片理解为随机快剪，或把电影慢节奏原样搬进短剧；音乐一停画面就失去结构。  
主调库：`aigc-short-drama-rhythm-library.md`, `episode-visual-rhythm-bible.md`, `sound-design-grammar.md`。  
素材方向：慢燃先导、强节拍快剪、慢—快—静—爆发、倒计时、声音骤停、反应镜头粘合、重复意象、标题卡、最后一击。  
验收：记录宏观节奏块、微观镜头长度曲线、每块观众问题、重复锚点、声音节拍、静默位置、标题卡功能和最终尾钩；只迁移节奏机制，当前短剧重新设计因果与时间。

---

## 4. 单批训练流程

```text
1. 选定专项方向，不混太多目标。
2. 优先从 `censorship-safe-suspense-training-batches.md` 选一个场景族群，再搜/读 8-10 个同类悬疑电影片段。
3. 每个片段按标准字段拆解。
4. 合并重复机制，删除片名堆砌。
5. 抽出 5-8 条规则和 5-8 条反例边界，并给出 SD 承接锚点。
6. 写入已有 reference；如果已有库能承载，不新建文件。
7. 更新 SKILL.md 入口或 training-protocol 编号。
8. 用 Select-String 验证引用链。
9. 用一个微型分镜任务反向测试是否触发。
```

### 项目专项训练覆盖层

当当前任务明确命名某个项目，并且该项目存在专项训练章程时：

1. 先读取项目设定，再读取专项训练章程；章程决定当前缺口、批次优先级和停止条件。
2. 项目文件只保存人物、规则、场景位置和当前应用约束；匿名可迁移机制写入通用参考库。
3. 同一素材分别回答“对当前项目有什么用”和“删除项目名后还能留下什么”。后者不成立时，不进入通用技能。
4. 不因为项目出现新地点、新运镜或新物件就创建新技能。优先路由到既有对话、声音、物件、结构、运动生态或连续性模块。
5. 专项批次连续两个新样本没有产生新规则、失败边界、组合模板或SD锚点时，关闭主动扩张，只登记覆盖证据。

《残烛》当前专项章程：`canzhu-targeted-training-charter.md`。

### 规模化阅片与切换规则

海量训练采用三层结构，不把逐部视频精拉当成主库建设方式：

| 层级 | 规模与材料 | 作用 | 停止条件 |
|---|---|---|---|
| 广度机制池 | 大量片名、场景描述、预告片、剧本信息、文字拉片、截图组和二手检索；默认B/C级 | 扩大环境、场景功能、导演解法和机制召回 | 形成可检索的场景指纹与机制候选即可，不要求逐部核验 |
| 机制比较样本 | 每个机制优先积累8-12个不同影片/环境/导演解法；可用简洁镜头笔记或6-16张关键画面接触表 | 比较构图、调度、运镜、声音、转场和失败边界的差异 | 连续两个样本不再产生新规则、新失败边界或新组合模板时切换机制 |
| A级校准锚点 | 每个高频或高风险机制只选1-3个代表性片段、连续截图或可靠制作资料 | 校准物理关系、空间连续性、表演节拍、声音位置或特殊镜头执行 | 足以纠正通用模板即可；A级不是影片库的覆盖率目标 |

默认不要求用户持续提供完整视频。优先接受和自主整理：

- `片名/场景功能/核心机制/可替换变量/失败边界`的短卡。
- 能看清起幅、变化过程和落幅的少量连续截图或接触表。
- 只记录构图、摄影机路线、人物调度、声音触发和转场落点的文字拆解。
- 真实生成失败或特殊物理镜头所需的局部验证材料。

阅片切换纪律：

1. 一部电影默认只沉淀1-3个真正不同的机制，不做全片百科式穷举。
2. 一个场景抽出规则、失败边界、迁移模板和SD锚点后立即切换，不围绕同一片段无限润色。
3. 同一机制主动轮换年代、地区、导演、场景环境和制作规模，避免风格单一化。
4. 新样本若只重复已有规则，只登记为覆盖证据，不增加技能正文。
5. 只有用户要求复刻、逐帧审计，或某个物理/声音/连续性问题反复失败时，才进入深度片段核验。

---

## 5. 精简原则

新增内容必须满足至少一个条件：

- 修复明确失败点。
- 增加一个悬疑子类型能力。
- 增加一个可转译成镜头字段的机制。
- 增加一个SD/视频输出稳定锚点。
- 增加一个质量门槛。

不满足则不写入。

删除或合并：

- 重复片单。
- 只讲观后感的段落。
- 不含构图/机位/光影/声音/转场的素材。
- 已被现有库覆盖且没有新增机制的条目。
- 只更换地点、角色或影片名称，机制字段完全相同的项目卡。
- 已有主模块和项目章程都能完整承载、却重复建立的独立技能入口。

---

## 6. 自我迭代闭环

```text
用户反馈/失败输出
-> 对应 C01-C10 投诉类型
-> 对应悬疑子类型
-> 对应训练批次 A-L
-> 如果是生成后失败，先用 generation-feedback-repair-loop 判定失败层
-> 如果是跨镜头漂移，先用 continuity-design-bible 锁连续性总线
-> 如果是人物像临时表演，先用 character-performance-bible 锁角色表演指纹
-> 如果是单镜头好但整段散，先用 episode-visual-rhythm-bible 锁钩子链、问题链和尾帧继承
-> 如果是环境有氛围但不压迫，先用 psychological-atmosphere-benchmark-library 锁空间证据、错位物件、环境声和认知改写点
-> 重写规则/模板/门槛
-> 接入路由
-> 验证
-> 下次输出前自动检查
```
