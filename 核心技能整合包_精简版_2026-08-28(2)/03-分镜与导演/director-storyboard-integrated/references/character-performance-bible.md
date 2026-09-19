# Character Performance Bible

用途：锁定角色跨镜头、跨场景、跨SD段落的表演连续性。  
目标：让人物不是“每个镜头临时害怕/生气/逃跑”，而是拥有稳定的身体语言、压力反应、职业习惯、关系动作和可继承的表演指纹。

---

## 1. 什么时候必须启用

遇到以下情况，正式分镜前先建立角色表演圣经：

- 同一角色连续出现超过3个镜头。
- 追逐、争吵、审问、醒来、躲藏、发现规则物、心理崩溃、梦境回落。
- 用户给过人物参考图，服装/气质/体态不能随意漂移。
- SD/视频生成时出现脸变、表演僵、动作丢失、情绪断层。
- 角色身份重要：收容员、特工、首领、AI、医生、母亲、伴侣。

---

## 2. 角色表演指纹

每个主要角色至少锁定：

```text
角色身份：
身体基准：
眼神习惯：
手部习惯：
步态/站姿：
压力反应：
说话时动作：
听别人说话时动作：
恐惧/愤怒/撒谎/克制的表现：
崩溃边界：
SD角色锚点：
```

短剧压缩写法：

```text
规则调查者表演指纹：职业性克制，先观察再行动；受惊时先屏息、确认出口和物件，再允许情绪进入动作；奔跑时保留任务习惯；听见熟悉声音时先出现身体反射，再执行训练过的校验动作。
```

---

## 3. 表演状态链

情绪不能跳变，要写成可见状态链。

```text
基准状态 -> 第一刺激 -> 压制反应 -> 身体泄露 -> 行动选择 -> 代价/残留
```

| 场景 | 状态链写法 |
|---|---|
| 追逐 | 正常奔跑 -> 听见画外声 -> 呼吸断拍 -> 回头但不完全停 -> 手扶墙稳住 -> 步幅乱 |
| 醒来 | 猛睁眼 -> 胸口快速起伏 -> 手摸床单确认质感 -> 眼神找门/物件 -> 坐起失败一次 -> 再坐稳 |
| 规则物发现 | 看见物件 -> 手悬停 -> 先看环境 -> 再触碰边角 -> 指尖收紧 -> 读到信息后呼吸变浅 |
| 夫妻争吵 | 克制说话 -> 道具动作变重 -> 眼神避开 -> 身体逼近或后撤 -> 说出伤人句 -> 留下静止尾帧 |
| 审问对峙 | 坐稳 -> 眼神不逃 -> 手指在桌下泄露压力 -> 听到关键词停顿 -> 反问或沉默 |
| 崩溃 | 否认 -> 重复动作 -> 眼神失焦 -> 呼吸失控 -> 抓住物件/身体支点 -> 突然安静 |

---

## 4. 五类悬疑表演机制

| 表演机制 | 可见动作 | 适用场景 |
|---|---|---|
| 克制式恐惧 | 不喊，先屏息、眼神找出口、手指发白、步幅变短 | 专业角色、收容员、调查者 |
| 礼貌式恐惧 | 面部维持社交表情，身体慢慢背向出口 | 日常恐怖、陌生人对话 |
| 冷静式压迫 | 动作少、语速稳、眼神不躲、手部动作精确 | 反派、首领、系统人物 |

### Self-Anchor / Identity Verification

Use when memory, room identity, costume, voice or authority may be unreliable.

```text
stable personal routine
-> one external cue contradicts it
-> body begins the familiar response
-> character verifies body, object, route and private memory in that order
-> one proof fails or belongs to someone else
-> character keeps one surviving anchor and changes strategy
```

The anchor must be executable: touch sequence, phrase rhythm, pocket object, scar, handedness, route mark, breathing count or professional check. Repeating a name without testing anything is exposition, not self-anchoring.

#### Self-Anchor Counterpart Recall

Evidence status: B-grade mechanism recall. Use the verification relation and performance sequence only; exact film blocking and dialogue require source verification.

| Film / scene situation | Anchor system | Performance and camera proof | Failure / contradiction | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `Memento` - photographs, notes and body writing guide action | External written/photo anchors replace unreliable recent memory | Hands sort, read, compare and act; camera links text, ownership and next choice rather than treating notes as inserts | An anchor may be true, incomplete or planted by the same person | Self-anchoring must include a trust test and a visible action consequence | Do not import reverse chronology or make every clue equally important |
| `The Machinist` - body decline and notes challenge self-story | Weight, injury, handwriting, apartment objects and repeated routes | Body condition is visible before explanation; gaze and touch compare current evidence with remembered identity | Physical state contradicts what the character believes he has been doing | Let the body be an anchor that cannot be argued away | Avoid copying guilt plot or using emaciation as generic horror styling |
| `Black Swan` - professional routine meets mirror/body mismatch | Rehearsal sequence, costume, foot position, injury and reflection | Repeat a trained movement under a readable mirror plane; camera holds long enough to compare body and image | One movement, mark or reflection fails while the professional routine continues | A trained routine is strongest when one precise component breaks | Do not stack mirror lag, face change, wound and double in the same beat |
| `The Father` - watch, room and caregiver identity drift | Watch, bag, chair, apartment layout and care routine | Performance moves from confident correction to dependency through repeated object checks | Each anchor may transfer owner or location, leaving only emotional need stable | Let anchors fail one at a time and preserve one surviving bodily/relational truth | Avoid changing every room and face simultaneously |
| `Moon` - recordings and duplicate bodies challenge identity | Recorded messages, scars, workstation access and identical bodies | Frame present body beside archived evidence or another body with the same marker | Institutional record and embodied identity disagree | Identity verification strengthens when private body proof and system record conflict | Strip clone/corporate lore; keep record ownership and body comparison |
| `Possessor` - identity ritual uses personal objects and gestures | Personal item, practiced phrase, face/voice rehearsal and body sensation | Character performs a controlled return ritual; micro hesitation or wrong gesture reveals incomplete ownership | The routine succeeds externally but fails at one private emotional response | A self-anchor may expose who is controlling the body by one private error | Do not import possession technology or rely on graphic body imagery |
| `Jacob's Ladder` - pain, hospital fragments and family memory compete | Wound/pain, military/medical image, family face and repeated environmental sound | Body reacts before the scene explains which reality owns the pain | Multiple realities claim the same body evidence | Preserve one physical symptom across transitions so memory remains testable | Do not use a rapid flashback collage without an invariant symptom |
| `Identity` - names, rooms and personal objects lose stable ownership | Name, room number, key, luggage and personal history | Group or individual behavior repeatedly assigns identity through objects and location | Evidence belongs to another identity or cannot coexist in one timeline | Identity drift becomes readable when ownership moves through concrete props | Strip the original psychological solution; keep only ownership contradiction |

### Recognition Reversal

Use when a familiar person or relationship becomes the final truth carrier.

```text
familiar voice/gesture/object enters before the full face
-> protagonist shows recognition before fear
-> camera protects part of the face while the relationship remains readable
-> one private gesture or phrase confirms identity
-> the same proof reclassifies the scene as danger, loss or impossible reunion
-> reaction lands on changed distance, touch permission or object ownership
```

Tenderness, restraint and delayed comprehension carry the reversal. A face reveal without a relationship-specific proof is only appearance; a jump scare erases the emotional recognition window.

#### Recognition Reversal Counterpart Recall

Evidence status: B-grade mechanism recall. Use the dramatic and audiovisual relation only; do not claim exact shot order, timing, lens or dialogue without source verification.

| Film / scene situation | Composition and camera mechanism | Performance and information release | Sound / object carrier | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `The Sixth Sense` - child gives his mother a private proof in the car | Keep both faces in one constrained shared space; favor reaction continuity over coverage variety | The listener begins in practical disbelief, receives one relationship-specific fact, then belief arrives through breath, eyes and softened distance before explanation finishes | Traffic/vehicle ambience remains ordinary; the private message is the proof | Let an intimate fact change the relationship before any supernatural conclusion is stated | Do not copy the afterlife explanation or turn the beat into a speech-only close-up exchange |
| `The Others` - domestic evidence reclassifies family identity | Hold house geometry and family grouping stable while outside observers or physical evidence contradict the family's self-image | Recognition spreads unevenly: one person understands, another resists, children read the adult reaction | Household objects, doors and room tone remain familiar as meaning flips | Keep the world visually continuous while one fact changes who belongs to it | Do not rely on the original identity twist or make every family member react simultaneously |
| `Arrival` - intimate images are reclassified as future memory | Repeat one gesture, face angle, touch or object across separated contexts with controlled visual rhyme | Emotion appears before chronology is understood; the later context changes the earlier image rather than replacing it | Recurring phrase, breath, hand contact or tonal motif carries the association | Recognition can be created by repeated fragments whose ownership changes at the reveal | Avoid rapid sentimental montage; one repeated anchor must remain readable |
| `Relic` - care gesture survives bodily estrangement | Stay physically close and allow touch, skin, cloth and weight to remain visible; camera observes rather than attacks | The daughter recognizes the mother through care behavior and touch permission even when appearance is unstable | Clothing removal, skin contact and breathing become relational proof | A familiar care action can confirm identity more strongly than face accuracy | Do not let body-horror texture overpower the relationship or use touch without prior intimacy |
| `The Orphanage` - a familiar game locates the missing child | Use doorways, negative space and repeated room positions; reveal follows the game's spatial rule | The parent commits to the familiar ritual before seeing the child, so recognition is earned by shared behavior | Counting, knocks, footsteps or a childhood game precede the body | A private routine may function as both identity test and reveal path | Strip the original ghost rules; avoid turning the routine into arbitrary magic |
| `Lake Mungo` - family images reveal a presence only after reinspection | Keep photographs/video and the viewer's face in a stable inspection relation; use a slow attention transfer rather than a scare cut | Recognition is delayed because the family first sees an ordinary record, then notices what was always present | Image noise, room tone, cursor/handling sound and silence support re-reading | A familiar face or body may be revealed through delayed attention to an unchanged record | Static media must change the next action; do not use a long image hold without a discovery route |
| `The Father` - familiar people and rooms lose stable identity | Repeat entrances, seating and care gestures while faces or ownership shift; preserve one room or object invariant | The character recognizes need, dependency or tenderness before reliably identifying the person | Watch, bag, chair, medication or repeated phrase acts as a fragile anchor | Recognition may survive identity drift through an emotional or bodily routine | Preserve one invariant or the scene becomes general confusion rather than relational loss |
| `A Tale of Two Sisters` - domestic repetition exposes a false family relation | Reuse table, corridor or bedroom compositions so the same family action acquires another owner | A familiar household gesture is first accepted as normal, then re-read when another person's reaction or absence becomes visible | Table setting, clothing, medicine or room placement carries the contradiction | Repeat ordinary family blocking and change one participant/owner to create relational reclassification | Do not import the original family diagnosis or stack multiple identity reversals in one short beat |
| 关系式爆发 | 不是一直吼，而是物件动作越来越重、距离越来越短 | 夫妻争吵、家庭冲突 |
| 失控式确认 | 发现证据后先愣住，再用重复动作确认，不立刻解释 | 规则物、身份反转、梦境落地 |

---

## 5. 角色职业动作

职业身份必须进入身体动作，而不是只靠台词。

| 身份 | 身体动作证据 |
|---|---|
| 收容员/调查者 | 先扫空间出口，再看物件；触碰前停顿；听声音先定位方向；习惯用短句自我确认 |
| 特工/追捕者 | 贴墙移动、压低重心、手先到门把/武器/通讯器；眼神扫死角 |
| 首领/权力人物 | 站位稳定，手少动，视线先看大屏再看人；说话时不急转身 |
| AI/系统化角色 | 几乎无身体动作，信息变化通过光、屏幕、脉络、声音节拍体现 |
| 伴侣/家庭角色 | 熟悉空间里的无意识动作：拿杯、整理相框、捡钥匙、摸戒指、避开视线 |
| 医生/机构角色 | 手部动作干净、程序化，物件摆放精准；情绪藏在停顿里 |

---

## 6. 关系动作

两个人的关系不只靠台词，要靠距离、手、眼神、物件归属。

| 关系状态 | 画面动作 |
|---|---|
| 仍想挽回 | 一方靠近，手伸出但停在半空，不直接触碰 |
| 已经厌倦 | 眼神不看对方，手忙着整理无关物件 |
| 权力不平等 | 一人站，一人坐；一人靠出口，一人被家具堵住 |
| 互相伤害 | 物件被推到中间：钥匙、戒指、手机、账单、相框 |
| 秘密暴露 | 听者先看物件，再看说话者；说话者回避视线 |
| 决裂 | 身体方向先分开，台词后到；最后物件留在两人之间 |

---

## 6.1 Information Permission And Dual-Channel Performance

For concealment, social pressure, undercover behavior, false intimacy or performed ignorance, design five tracks:

```text
public face/voice
public body task
private leak or signal
who can perceive the private signal
residual state after the performance
```

| Mechanism | Public layer | Private layer | Perception rule |
|---|---|---|---|
| performed ignorance | routine continues, gaze stays on the expected task | breath catches, fingertip pressure changes, one note or step slips | audience sees the leak; other characters accept the performance |
| false intimacy | smile, embrace, shared public posture | hidden grip, fixed dry eyes, whispered phrase, foot blocking the exit | private signal is visible/audible only at close distance |
| social fear | polite tone and still face | body angles toward exit, hand protects object, foot shortens stance | target may notice late; surrounding group remains unaware |
| controlled authority | minimal gesture, stable voice and posture | gaze checks a subordinate, one finger stops machinery, prop ownership never changes | the smallest private action redirects the room |
| status collapse | verbal denial and upright posture | knees soften, support hand seeks furniture, body height drops in stages | camera height may follow only when vertical loss is the scene's main axis |

Do not write two unrelated personalities. Both channels belong to one intention: preserve the public story while protecting, threatening, escaping, testing or controlling through the private layer.

Use qualitative reaction timing: immediate, one beat later, after reading another face, or remains unaware. Do not force universal subsecond numbers into integer-second storyboards.

---

## 7. 镜头如何记录表演

| 景别 | 记录重点 |
|---|---|
| 全景 | 身体距离、出口方向、站位权力、谁移动谁不动 |
| 中景 | 肩颈、手臂、身体前倾/后撤、道具操作 |
| 近景 | 眼神、嘴角、下颌、吞咽、呼吸、手入画 |
| 特写 | 手指、眼睛、物件接触、汗、水、纸边、火苗 |
| 反应镜头 | 不拍事件本身，拍角色如何知道/误解/压住反应 |

规则：

- 每句关键台词至少配一个身体动作或听者反应。
- 表演不是越大越好，悬疑常常需要“想压住但压不住”。
- 角色专业性越强，表演越应克制；泄露点放在手、呼吸、眼神延迟。
- 崩溃前要有重复动作，崩溃后要有安静尾帧。

Dialogue plus active blocking uses five tracks:

```text
speaking mouth window
main body route
one supporting hand/prop action
listener reaction window
one background event
```

Protect the speaking mouth during dense lines. Place larger turns, handoffs, door actions and listener reactions in phrase gaps or immediately after the line. Use `dialogue-physical-interaction-grammar.md` for execution and `counterpart-execution-risk-atlas.md` for mechanism examples.

---

## 8. SD承接角色表演

A区块必须把表演写成可见动作，不写抽象性格。

| 抽象写法 | SD可承接写法 |
|---|---|
| 她很害怕 | 她屏住呼吸，眼神先扫向出口，右手指节压白，左脚后撤半步 |
| 他很冷漠 | 他站在原地不转身，只用眼睛看向屏幕反光，手指轻点控制台一次 |
| 两人争吵激烈 | 他把钥匙推到桌中央，她用戒指压住账单，双方身体前倾又同时停住 |
| 她意识到不对 | 她的眼睛停在卡片边角，呼吸断一下，指尖离纸面两厘米停住 |
| 他在追她 | 他的脚步稳定贴近墙线，手先触碰门框，目光扫过前方转角 |

SD角色锚点最少包含：

```text
脸/发型/服装基准 + 身体姿态 + 一个手部习惯 + 一个压力反应 + 当前状态残留
```

---

## 9. 对标训练种子

这些不是片名堆砌，只拆表演机制：

| 对标片段 | 可借机制 | 不能照搬 |
|---|---|---|
| The Silence of the Lambs - Clarice and Lecter | 直视、眨眼、停顿和坐姿建立心理权力 | 不照搬牢房和台词 |
| Zodiac - basement scene | 礼貌表情下身体找出口 | 不照搬地下室情节 |
| Prisoners - interrogation | 逼近、撑桌、突然收手制造失控边界 | 不照搬暴力逼供 |
| Hereditary - dinner confrontation | 家庭争吵先压住，再从嘴角/眼泪/餐具声泄露 | 不走失控吼叫到底 |
| Gone Girl - public/private face | 表情切换展示伪装和控制 | 不照搬婚姻骗局 |
| No Country for Old Men - coin toss | 冷静压迫和小物件让对方先不明白 | 不照搬硬币设定 |
| Mulholland Drive - diner fear | 白天日常里身体逐渐僵硬 | 不照搬怪物露面 |
| Black Swan - mirror/body anxiety | 自我异化通过眼神、皮肤、手部小动作表现 | 不照搬身体恐怖展示 |
| Parasite - table hiding | 屏息、身体压缩、脚步距离决定危险 | 不照搬桌下躲藏剧情 |
| The Babadook - exhausted mother | 疲惫重复动作比尖叫更能表现崩溃 | 不照搬母子设定 |

---

## 10. 输出模板

### 角色表演圣经

```text
角色：
身份/关系：
身体基准：
眼神习惯：
手部习惯：
步态/站姿：
压力反应：
情绪升级链：
关系动作：
职业动作：
崩溃边界：
SD角色锚点：
```

### 分镜行内压缩

```text
画面内容：按角色表演指纹写起始姿态、触发点、压制反应、泄露动作、道具动作、尾帧。
SD承接锚点：脸/发型/服装基准 + 手部习惯 + 压力反应 + 当前状态残留。
```

---

## 11. 反例边界

- 不能只写“害怕、生气、冷静、崩溃”，必须转成身体动作。
- 不能每个角色都用同一种恐惧表演。
- 不能让专业角色一惊就失去职业判断，除非故事明确击穿他的专业性。
- 不能让争吵从第一秒吼到最后，没有升级坡度。
- 不能让台词说完后画面没有听者反应。
- 不能让SD只继承脸和服装，不继承身体姿态和压力动作。

---

## 12. Runtime Rules

应写入模块：

- 工具层 - 画面内容 / 表演微动作 / 反应镜头。
- 工具层 - 连续性总线 / 服装身体状态。
- 工具层 - 对话对峙 / 追逐 / 规则物发现 / 梦境醒来。
- 输出层 - SD A区块角色动作锚点。
