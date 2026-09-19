# Continuity Design Bible

用途：锁定跨镜头、跨30秒SD段落、跨场景的设计连续性。  
目标：让分镜不只是单帧好看，而是人物、空间、道具、服装、光源、色彩、声音和尾帧能稳定延续，避免AIGC短片出现“镜头都漂亮但不是同一场戏”的断裂。

---

## 1. 什么时候必须启用

遇到以下情况，正式分镜前先写一版“连续性总线”：

- 同一角色连续奔跑、争吵、躲藏、醒来、开门、调查、对峙。
- 同一空间内有多个门、走廊、床、桌、窗、控制台、屏幕、镜子。
- 关键物件有状态变化：卡片、规则火源、戒指、钥匙、电话、箱子、录音、证据袋。
- 服装、头发、汗、水、灰、伤痕、污渍、破损会跨镜头继承。
- 光源方向会影响真实度：门缝光、屏幕光、烛光、荧光灯、车灯、投影。
- 需要转SD/Seedance，且段落超过一个A区块。
- 用户反馈“像拼图、脸变了、衣服变了、空间跳、光不连、道具不见了”。

---

## 2. 连续性总线字段

正式分镜不用每次全部展开，但内部必须能回答：

```text
场景连续性：
空间地图：
屏幕方向：
主光方向：
色彩剧本：
场景陈设：
关键道具状态链：
服装/妆发/身体状态链：
多人站位与权力线：
声音连续性：
尾帧继承：
SD稳定锚点：
```

### 短剧压缩写法

```text
连续性总线：走廊由左后向右前延伸，出口始终在画面深处；冷白荧光从顶左扫下，门缝暖光只在尽头出现；逃跑者右肩汗湿、左手有墙灰、鞋底水痕跨镜继承；规则火源每次压低都触发墙面靠近；尾帧门框黑影继承到封闭房间醒来。
```

---

## 3. 色彩剧本连续性

色彩剧本不是单镜头“冷色调”，而是颜色在段落里承担信息变化。

| 类型 | 起始色彩 | 变化方式 | 回收方式 |
|---|---|---|---|
| 走廊追逐 | 冷白/青灰 | 暖光只作为出口诱饵出现 | 醒来后暖光归属于规则火源，证明规则 |
| 病房醒来 | 冷白荧光 + 监护绿 | 蜡烛暖色打破机构冷光 | 规则物被暖光照亮 |
| 家庭争吵 | 暖黄家居光 | 冷屏幕/走廊光切入关系裂缝 | 门口冷光吞掉一方 |
| 太空舰桥 | 冷蓝投影 + 黑金属 | 红/琥珀警示只在高能目标出现 | 目标归属反转时暖色极细出现 |
| 梦境坍塌 | 现实色彩先稳定 | 色相错位、饱和度短暂失控 | 新空间保留旧空间一条色彩残痕 |
| 规则物特写 | 环境色压低 | 物件拥有唯一强调色 | 结尾用同色回收伏笔 |

规则：

- 一个段落最多一个主色系统，一个强调色。
- 强调色必须有信息功能：出口、规则、危险、谎言、记忆、系统警示。
- 色彩变化必须绑定动作、声音、光源或物件状态。
- 转SD时，稳定色彩规则进入 `BASE LOCK`，逐拍色彩变化及其声画触发进入A区块 `声光与转场触发`。

---

## 4. 场景陈设连续性

场景陈设不是装饰，是空间地图和真实质感的证据。

| 场景 | 必锁陈设 | 作用 |
|---|---|---|
| 走廊 | 门牌、灯格、墙脚线、尽头门、地面反光、管线/扶手 | 证明方向、速度、距离 |
| 病房 | 床头、床栏、输液架、监护仪、窗帘、门、规则物位置 | 证明醒来位置和逃离路线 |
| 家庭客厅 | 沙发、茶几、门、鞋柜、餐桌、手机/戒指/钥匙 | 证明关系距离和离开方向 |
| 太空舰桥 | 投影墙、控制台、星图、指挥者站位、AI光体位置 | 证明权力和目标信息 |
| 门/阈限 | 门把、门框、门缝光、门牌、门内外色温差 | 证明信息阀门 |
| 梦境变形 | 旧空间核心材质、新空间目标材质、残留物 | 证明无缝变形不是随机跳转 |

陈设规则：

- 每个空间至少锁定3个不变锚点。
- 每次切镜至少保留1个锚点，帮助观众知道仍在同一空间。
- 陈设可以变化，但变化必须有触发原因和残留痕迹。
- 道具位置改变必须写“谁移动、怎么移动、移动后在哪里”。

---

## 5. 关键道具状态链

所有规则物、证据物、身份物、尾帧物都必须有状态链。

```text
初始状态 -> 首次被看见 -> 被谁触碰 -> 物理变化 -> 意义变化 -> 是否回收 -> 尾帧状态
```

| 道具类型 | 状态必须写什么 |
|---|---|
| 规则卡/纸张 | 位置、正反面、边角、潮湿/折痕、文字/纹路可见性、手指遮挡 |
| 规则火源 | 火苗高度、蜡油流向、风压、明暗反馈、是否由主角主动影响 |
| 戒指/钥匙/手机 | 归属、放置位置、反光、震动/响声、被拿起/放下/避开 |
| 证据袋/照片/录音 | 封口、标签、画面/声音内容是否可读、谁先知道 |
| 控制台/屏幕 | UI方向、目标点、刷新状态、警示色、人物反光 |
| 门把/锁 | 开合方向、磨损、手部压力、锁舌声音、门缝变化 |

### 5A. Continuity Priority Hierarchy

Not every visible asset receives the same continuity burden. Classify it before storyboarding:

| Tier | Function | Continuity rule | Permitted change |
|---|---|---|---|
| A: core anchor | survival rule, identity, primary objective, ownership or final payoff | preserve owner, position, state and meaning across every cut/scene; any transfer, concealment or transformation must be visible and motivated | only through an authored action or transition that owns the beat |
| B: authored clue | lets the audience or character detect a wrong reality, false account or changed permission | establish a readable baseline, change one variable, provide independent confirmation, then affect a decision or payoff | controlled mutation with trigger, observer and residue |
| C: ambient support | establishes place, use, social routine, material realism or depth | preserve layout family, traffic direction, light logic and interaction availability; item-level matching may be softened by depth, occlusion or framing | non-narrative variation that cannot alter route, ownership, rule or character knowledge |

Use this mutation ledger for Tier B clues:

```text
asset:
baseline state:
single permitted mutation:
trigger / transition:
who can observe it:
independent confirmation:
decision or payoff changed:
tail state:
```

Hard rule: an accidental disappearance is not a clue. If a Tier A asset disappears, the disappearance becomes the scene's primary event and must show cause, observer, consequence and residue. If a Tier B asset changes but nobody can compare it to a baseline or use the result, treat it as a continuity error and remove it.

SD承接时，把状态链压缩为最容易丢的3个锚点：

```text
物件位置 + 物理状态 + 尾帧状态
```

---

## 6. 服装/妆发/身体状态链

人物连续性不只靠“同一个人”，还靠身体和服饰被事件留下痕迹。

| 状态 | 分镜写法 |
|---|---|
| 汗 | 额角、锁骨、衣领、后背、手心；随奔跑/争吵/恐惧增加 |
| 水 | 鞋底水痕、裤脚吸水、发梢滴水、衣料贴身 |
| 灰尘 | 手掌墙灰、膝盖灰、袖口蹭痕、脸颊细灰 |
| 破损 | 衣摆拉扯、纽扣松动、袖口裂线、鞋带散开 |
| 火光影响 | 脸侧暖斑、瞳孔火点、蜡油味、袖口被暖光描边 |
| 精神状态 | 眨眼频率、吞咽、肩颈僵硬、手指发白、步幅变短 |

规则：

- 服装锁定优先级高于临时美化。用户给过角色图时，默认沿用，不主动换服饰。
- 状态只能随事件累积或被明确动作改变，不能镜头间自动复原。
- 近景/特写必须保留至少一个上镜状态锚点：汗、灰、水、褶皱、发丝、手指压力。
- SD多段输出时，每段开头重复最关键的服装/身体状态锚点。

---

## 7. 多人站位与权力线

多人戏最容易散。先锁站位，再写对白。

```text
谁靠近出口：
谁占据中心：
谁被前景挡住：
谁拥有关键物件：
谁看谁：
谁不看谁：
谁移动后改变权力：
```

常用权力调度：

| 调度 | 画面效果 | 适用场景 |
|---|---|---|
| 门口分裂 | 一人靠门，一人留屋内 | 离婚争吵、离开/挽留 |
| 桌面对峙 | 桌子切开两人，物件在中间 | 审讯、谈判、夫妻摊牌 |
| 三角站位 | 第三人/屏幕/物件让对话失衡 | 指挥者-AI-目标投影 |
| 一人坐一人站 | 高低关系压迫 | 权力人物、审问、家庭训斥 |
| 背景旁观 | 背景人不动，前景人崩溃 | 群体压力、社会伪装 |
| 物件中心 | 所有人视线压向一个道具 | 规则物、证据、检测物 |

剪辑规则：

- 反打必须保持视线方向和屏幕左右关系。
- 越轴需要过渡镜头：移动镜头、正面中轴、物件特写、门框遮挡。
- 群像里每个人必须有一个可疑动作或立场动作，不能只站着听。

---

## 8. 光源与声音连续性

### 光源连续

```text
主光来源：
主光方向：
补光或反光：
强调色来源：
阴影方向：
跨镜头是否改变：
改变触发：
```

规则：

- 光源漂移会直接破坏实拍感。
- 梦境/幻觉可以改变光，但要给触发点：灯闪、门开、火苗压低、屏幕刷新、声音刺入。
- 强调色必须来自可见或可理解的光源：烛火、屏幕、门缝、警报、投影、霓虹。

### 声音连续

```text
底噪：
角色近景拟音：
关键物件声：
画外压力：
主观声：
静音点：
声桥：
尾音继承：
```

规则：

- 声音不能每镜重启，要有声桥或尾音继承。
- 声音触发必须对应可见反应：回头、停步、手抖、灯闪、焦点变、转场发生。
- 若声音用于规则交代，必须贴合物件或空间来源，避免空旁白感。

---

## 9. 尾帧继承到SD

尾帧是AIGC视频段落最重要的连续性钉子。

每个A段结尾要回答：

```text
最后画面是什么？
主体在画面哪个位置？
关键物件在什么状态？
主光方向是什么？
声音尾巴是什么？
下一段继承哪个视觉/声音锚点？
```

例：

```text
尾帧继承：门框黑影遮满画面，主体右手掌心有墙灰，冷白灯嗡鸣未断；黑影退开后接封闭房间同方向冷白荧光，手掌灰仍在。
```

规则：

- 不能让下一段重新开局像另一条视频。
- 转场段必须至少继承一个视觉锚点和一个声音锚点。
- 角色脸、服装、道具、光源中至少两个要跨段稳定。

---

## 9A. Active Route-Memory Proof

Use when an intelligent character tests a looping, reversed or unreliable space.

```text
readable route baseline
-> character deliberately leaves one marker with known owner/orientation/material
-> camera preserves departure direction and expected return relation
-> expected landmark fails to appear or appears on the wrong side
-> the same marker returns with one impossible but verifiable change
-> character updates the route model and next action
```

Markers may be chalk, wax, water, thread, door angle, moved furniture, recorded sound, footprint or a small tear. Keep one primary marker and one independent spatial check. Random repeated corridors without a deliberate test make the character passive and the anomaly unverifiable.

### Active Route-Memory Counterpart Recall

Evidence status: B-grade mechanism recall. Use these as topology and verification patterns, not as verified shot lists.

| Film / scene situation | Spatial baseline and camera | Marker / independent check | Rule discovery | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `1408` - hotel exit returns to the same room/threshold | Establish door, corridor and room orientation before attempting escape; return to the same visual anchor | Door number, window, telephone or room damage can serve as repeated checks | Escape action changes distance but not permission; the room owns the return | Repeat one threshold with a changed consequence rather than changing the entire set | Do not copy the room mythology or use resets without preserving body/object residue |
| `Grave Encounters` - hospital layout stops matching expected exits | Use long corridor depth, signs and group movement to create a practical map before it fails | Exit sign, door destination, clock/daylight expectation and group count cross-check the error | Institutional wayfinding systems disagree with physical space | Use two independent systems so the anomaly is not blamed on bad memory | Avoid found-footage chaos that makes left/right and ownership unreadable |
| `Triangle` - the same ship accumulates evidence from previous passes | Keep key ship zones and movement direction recognizable while duplicate objects accumulate | Note, body/object pile, locket or wound state proves prior traversal | Repetition leaves material residue instead of resetting cleanly | Let repeated routes accumulate evidence until the character's model must change | Do not import the time-loop explanation; preserve only accumulation and route proof |
| `Cube` - numbered modular rooms form a testable navigation system | Frame each threshold and room grid consistently so entry/exit relations can be compared | Number sequence, door face, trap result and group memory provide checks | Space becomes legible through rule testing, not intuition | Treat room labels as data only when a physical test changes route choice | Avoid puzzle exposition and keep one calculation/test readable per beat |
| `Vivarium` - identical houses defeat visual navigation | Use repeated centered streets/houses and stable horizon to prove sameness | Sun position, roof color, smoke, food package, dug ground or body fatigue becomes the independent check | Visual sameness is exposed by material and bodily change | When architecture repeats, let weather, residue or fatigue prove movement occurred | Do not rely on identical-production-design alone; add a deliberate test and consequence |
| `The Endless` - routes and actions repeat across zones | Establish landscape landmark and travel direction, then let another person's repeated action contradict elapsed movement | Rope, photograph, recorded message, sky event or repeated behavior confirms the zone | Different spaces may obey different repetition permissions | Route failure can be proven by behavior and time evidence, not only returning scenery | Remove cosmic lore; do not combine multiple time rules in one short segment |
| `As Above, So Below` - descent returns motifs in altered orientation | Preserve stair, tunnel and descent direction while architecture mirrors or reverses | Personal object, inscription, wound or repeated obstacle confirms correspondence | Movement continues forward while symbolic/spatial orientation inverts | Keep body direction stable and invert one environmental relation | Avoid carrying religious mythology; a mirror/inversion must affect route choice |
| `The Shining` - maze and hotel use repeated geometry as pressure | Use centered paths, repeated wall/hedge rhythm and readable junctions; camera maintains directional tension | Footprints, weather, sound, child/parent route or remembered junction acts as check | Repetition creates uncertainty, but survival still depends on physical navigation | Repeated geometry works only when junction decisions and traces remain legible | Do not treat symmetry as proof by itself; give the character a route decision and a trace |

## 10. 正式分镜中的使用方式

长版分镜可单独列：

```text
连续性总线：
```

短版分镜可写进每行：

```text
实拍摄影证据：...；连续性：...
SD承接锚点：...
```

若用户只要思路，不必展开表格，但导演内部必须先检查连续性。  
若用户要SD输出，把稳定连续性压缩进 `BASE LOCK`，把逐镜差量与尾帧压进A区块 `尾帧与连续性`。E只在无损母版或审核附件中出现。

---

## 11. 反例边界

- 不能每个镜头都换一个好看的色调。
- 不能让角色衣服、发型、汗水、灰尘、水痕自动复原。
- 不能让关键道具上一镜在手里，下一镜无解释出现在桌上。
- 不能让门、窗、出口、人物左右关系随剪辑漂移。
- 不能让光源方向跨镜头乱跳，除非有明确梦境/系统/灯闪触发。
- 不能让多人戏只靠台词互吵，站位和物件必须改变权力。
- 不能让SD每段重新描述角色，必须继承上一段尾帧状态。

---

## 12. Runtime Rules

应写入模块：

- 工具层 - 空间连续性 / 场面调度 / 轴线控制。
- 工具层 - 画面基调/质感 / 实拍摄影证据。
- 工具层 - 物件语言 / 伏笔链 / 状态链。
- 输出层 - 分镜到SD无损承接。
- 质量门槛 - 生成结果反修 / 连续性失败。
