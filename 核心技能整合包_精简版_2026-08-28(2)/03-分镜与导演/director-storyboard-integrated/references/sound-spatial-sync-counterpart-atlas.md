# Sound Spatial And Sync Counterpart Atlas

用途：当场景依赖画外声、监听、主观听觉、声源误导、声画分离、声音规则、空间声学或声画同步时，用本库快速选择机制。基础声轨结构读取 `sound-design-grammar.md`，计量读取 `sound-mix-metering.md`；本文件只保存对标机制，不重复基础规则。

证据声明：以下均按 `counterpart-source-register.md` 的B级机制使用。可以借片段的声音逻辑，不声称精确秒数、焦段、逐镜顺序或原始混音参数。需要精确拉片时必须重新核对正片或可靠制作资料。

## 1. Retrieval Axes

拿到场景后先判断五轴：

```text
信息关系：观众先听 / 角色先听 / 同时听 / 角色误听
声源状态：画内 / 画外 / 主观 / 结构性
空间关系：近身 / 隔门墙 / 走廊纵深 / 电话广播 / 开放空间
同步关系：严格动作同步 / 延迟反应 / J-cut / L-cut / 声画错位
叙事任务：定位 / 误导 / 规则 / 证据 / 压迫 / 认知崩塌 / 转场
```

## 2. Twelve Mechanism-Different Counterparts

| ID | 对标片段/影片 | 核心声音机制 | 声源与空间执行 | 时间与动态执行 | 可迁移场景 | 不能照搬 | SD/后期承接锚点 |
|---|---|---|---|---|---|---|---|
| SS01 | `The Conversation` 监听录音 | 同一句话随着监听位置和处理方式改变可懂度，声音本身成为证据 | VOX经远距、遮挡和设备中介进入；环境与人群掩蔽关键词 | 先给残缺语句，反复回听时逐步抬出关键词；角色理解晚于录音存在 | 监听、录音证据、重复语句改义、偏执调查 | 不能直接复制原台词或把所有信息一次听清 | 麦克风/录音机位置、关键词时间窗、频段恢复、角色反应延迟、第二次回听差量 |
| SS02 | `Blow Out` 声音重建事件 | 画面与录音逐步对齐，声音从背景变成因果证据 | OBJ冲击、机械声与ENV空间底床分轨；录音设备拥有独立声像 | 先听异常，再逐帧匹配可见事件；关键瞬态取得主位 | 事故调查、监控证据、枪声/机械误认、声画校验 | 不能把重建过程变成台词说明 | 可见事件帧、瞬态cue、时间偏移量、匹配落点、重建后新的行动选择 |
| SS03 | `The Zone of Interest` 画外世界 | 画面保持日常，远处声音持续证明被排除在画外的现实 | 远距ENV/VOX/OBJ构成另一空间；画内日常BODY保持克制 | 画外事件不抢成jump scare，而以重复、距离和持续性污染日常 | 机构压迫、家庭日常背后的灾难、观众知道角色装作不知道 | 不能把画外声音做成猎奇展示或突然巨响 | 画内/画外双世界总线、距离、遮挡、角色不反应权限、观众持续可听、声尾跨镜 |
| SS04 | `A Quiet Place` 声音生存规则 | 每个物件的可发声风险决定人物路线和动作幅度 | BODY与OBJ被极近放大；ENV稀薄；危险声有明确触发权限 | 动作前先给声风险，接触时控制包络，微响后全身冻结并等待后果 | 规则空间、潜行、不能回应、脆弱物件、呼吸控制 | 不能把“安静”写成真空；仍需room tone和身体声 | 发声物件、接触点、预计声量、角色规避动作、微响触发、全层静止与尾音 |
| SS05 | `No Country for Old Men` 旅馆/门外压力 | 极少声源和明确方位让门外空间变成威胁 | 门锁、脚步、电话或走廊底床经遮挡进入；近身呼吸保持干声 | 主声源逼近时ENV退后；停声本身成为位置不确定性 | 门后恐惧、躲藏、追兵接近、室内外对峙 | 不能用持续配乐替代空间距离 | 门墙LPF、走廊RT60、脚步间隔、距离自动化、停声点、人物视线与重心反应 |
| SS06 | `The Lives of Others` 耳机监听 | 一个角色通过设备拥有另一空间的信息，但身体仍困在当前空间 | VOX/ENV经过耳机变窄、变近；监听室本地BODY和设备OBJ保持可见 | 远端对话与监听者微反应错开；摘下耳机时声场突然回到本地 | 电话、监控、审讯监听、远程指挥、秘密共情 | 不能让设备声和现场声使用同一混响 | 设备滤波、双空间底床、耳机戴/摘触点、谁可听、监听者私下信号、声场切换 |
| SS07 | `The Shining` 走廊骑行 | 地面材质变化直接改变声音节奏，空间通过轮声被测量 | BODY/OBJ轮胎在硬地和软地间切换；走廊反射建立纵深 | 重复节奏在材质边界突然被吸收或恢复，形成预期与中断 | 长走廊、轮椅/推车/脚步、材质线索、儿童主观空间 | 不能只贴一个循环轮声 | 材质分区、接触周期、硬/软表面频谱差、边界同步、纵深反射、下一区域预告 |
| SS08 | `Berberian Sound Studio` 拟音与画面分离 | 制造声音的现实动作与被暗示的银幕事件产生心理错位 | 画内OBJ/BODY拟音清楚，所服务的画面可被遮挡或延后 | 先看制造动作再听结果，或只听结果让观众脑补画外事件 | 暗示式暴力、录音棚、幕后操控、声音不可信 | 不能依靠血腥或夸张惨叫 | 拟音物材质、手部动作、同步点、画外结果、听者微反应、声音残留的意义转换 |
| SS09 | `Sound of Metal` 主观听觉变化 | 外界与角色听觉版本交替，听觉损失/设备处理改变现实判断 | ENV/VOX从全频切到低通、骨传导感或设备压缩；INT拥有明确入口 | 通过接触、摘戴设备或身体状态触发，不随机失真 | 耳鸣、创伤、惊醒、幻觉、角色认知收窄 | 不能用“水下音”一招覆盖所有主观状态 | 主客观切换触点、滤波曲线、动态范围变化、外界残留、身体反应、恢复点 |
| SS10 | `The Guilty` 电话构建画外世界 | 观众只通过通话声、呼吸、线路噪声和主角反应想象不可见空间 | VOX电话带宽与远端ENV共同建空间；本地房间声保持现实压力 | 远端声音先给线索，主角解释可能错误；后续声音重新改义 | 电话求救、看不见的人、远程指挥、声音误导 | 不能用配图或对白把画外空间解释完 | 电话带宽、远端背景线索、主角误判、关键词让位、线路中断、反应镜头 |
| SS11 | `The Vast of Night` 广播/电话异常 | 声音媒介本身成为未知入口，持续倾听比展示来源更紧张 | VOX经广播/电话窄带进入；电流、静电与本地夜间ENV分离 | 长段倾听中只改变细节可懂度、底噪和人物姿态，不靠频繁惊吓 | 规则广播、神秘信号、系统音、夜间调查 | 不能让噪声一直同强度或堆满神秘音效 | 载波底噪、语句断裂、静电遮蔽、人物接近设备、旁人延迟反应、信号尾音 |
| SS12 | `Memoria` 无法定位的冲击声 | 单一异常声音没有可见来源，人物不断寻找空间解释 | FX/INT边界保持不确定；冲击拥有重量、频谱和衰减，但无立即画面证明 | 声音突入后保留足够余韵；后续重复时改变距离、清晰度或角色准备程度 | 梦境裂缝、记忆触发、不可定位声源、安静日常异化 | 不能频繁重复成jump scare，也不能立刻揭示来源 | 冲击频段、声像不确定范围、空间衰减、角色定位动作、环境恢复顺序、重复差量 |

## 3. Scene Router

| 用户场景 | Primary | Secondary | 核心检查 |
|---|---|---|---|
| 隔墙听见追兵 | SS05 | SS07 | 距离、遮挡、材质、停声后的空间不确定性 |
| 电话里的人可能撒谎 | SS10 | SS01 | 远端环境线索、语句可懂度、角色误判与二次改义 |
| 监控录音成为证据 | SS02 | SS01 | 声画时间对齐、关键词恢复、证据触发行动 |
| 梦里听见无来源巨响 | SS12 | SS09 | 主客观边界、定位失败、身体反应、重复差量 |
| 规则要求保持安静 | SS04 | SS05 | 发声物件、规避动作、微响后果和room tone |
| 日常空间背后有更大事件 | SS03 | SS11 | 画内外双世界、角色权限、持续污染而非巨响 |
| 戴耳机监听另一房间 | SS06 | SS01 | 双空间声场、设备滤波、摘戴触点和私下反应 |
| 空间变形需要动画音 | SS09 | SS12 | 可见边界、FX物质逻辑、INT入口、落地残留 |
| 空房里看不见的人通过声音和物件反应现形 | `sound-design-grammar.md` Invisible-Presence template | SS05 | 精确声源位置、身体重量、接触点、物件响应、连续路线和残留证据 |
| 群体逐渐被同一节拍或话语同步 | `sound-design-grammar.md` Behavioral Entrainment template | SS11 | 中性声源、分阶段身体同步、权限改变、破节拍动作和心理残留 |

## 4. Transfer Template

```text
场景声音任务：
Primary counterpart / borrowed mechanism：
Secondary counterpart / borrowed mechanism：
主声源与叙事权限：
画内/画外/主观/结构性：
空间与设备中介：
正常声场基线：
第一次变化：
角色感知与可见反应：
第二次改义或落地：
计量与闪避：读取sound-mix-metering.md
尾音/声桥：
不能照搬：
```

## 5. Response Threshold Grammar

Use when hearing is allowed but answering grants identity, location, access, or hallucination permission.

```text
plausible familiar voice enters from a readable off-screen direction
-> listener shows involuntary motor preparation to answer
-> mode A: breath/jaw/hand/foot action is inhibited and replaced by a non-addressed action
   or mode B: one familiar name produces a minimal reflex acknowledgement
-> sound position, room permission, or spatial state changes only after the answer threshold
-> listener recognizes the causal sequence and changes strategy
```

Execution requirements:

- Keep the source ordinary and intimate; spatial accuracy is more useful than “scary voice” processing.
- Show the near-response physically: intake of breath, jaw release, tongue movement, head turn, hand loosening, or first step toward the source.
- In inhibition mode, give the character an intelligent substitute action such as object testing, self-counting, gesture, route change, or writing.
- In accidental-response mode, use one short acknowledgement. The escalation must occur after it, so the rule remains legible.
- Across repetitions, change at least one of source direction, intimacy, knowledge, distance, or the listener's countermeasure.

Failure boundaries:

- Hearing alone cannot secretly count as answering.
- A reflex response with no established personal trigger feels arbitrary.
- Repeated calls without a changing bodily decision are sound wallpaper.
- Do not make every borrowed voice distorted; familiar normality carries the temptation.

## 6. Failure Boundaries

- 电影名只负责检索机制，不能替代当前场景的声源、距离、权限和动作。
- 画外声必须属于可解释物理空间、角色主观规则或明确结构装置。
- 主观滤波必须有入口和退出触点。
- 声音误导必须留下可二次理解的真实线索，不能事后随意改口。
- 动画/VFX声必须跟随可见变化边界、材质和落地残留。
- 声音先行或延续必须改变预期、空间或转场，不作为固定装饰。
