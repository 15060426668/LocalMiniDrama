# Episode Visual Rhythm Bible

用途：锁定AIGC悬疑短剧的整集/多场戏视觉节奏、钩子链、问题链和SD分段承接。  
目标：防止单镜头强但整段散、15秒没有新钩子、30秒没有问题转向、场景之间像断片。

---

## 1. 什么时候启用

启用条件：

- 开头、预告、整集或连续多场戏超过30秒。
- 用户说节奏平、太慢、短剧不够快准狠、缺高留存、没有钩子链。
- 分镜将拆成多个SD/Seedance段落。
- 场景之间需要门框、物件、声音、颜色、尾帧连续承接。
- 单场画面好看，但不知道下一场为什么必须看。

不要替代单镜头字段。它只管段落级节奏；每个镜头仍必须通过构图、机位、光影、质感、摄影证据、画面内容、声音、转场的正式字段。

---

## 2. 段落节奏骨架

| 时间 | 必须完成 | 画面载体 | 失败表现 |
|---:|---|---|---|
| 0-3s | 一个视觉问题 | 动作、异常物、门缝、声音来源、反常空间 | 空镜铺氛围、旁白解释 |
| 3-8s | 一个可见目标 | 逃、找、藏、读、开门、按住物件、盯住对方 | 只说设定，没有身体任务 |
| 8-15s | 第一钩子 | 规则碎片、物件反应、空间变形、第三方声音、关系裂缝 | 跑/说了15秒但认知不变 |
| 15-30s | 第一次转向 | 安全变陷阱、出口变入口、证据改义、声音撒谎 | 只是换景，没有问题升级 |
| 30-60s | 任务锁定 | 主目标、代价、限制、敌我关系、倒计时 | 观众只觉得画面新，不知道要追什么 |
| 每15s | 新信息/新风险/新选择 | 新物件状态、新站位、新声音位置、新光色归属 | 同类镜头重复、情绪原地踏步 |

整集不是一直加速。正确节奏是：快钩子进入，短暂停顿让观众读懂，再用新问题推进。

---

## 3. 钩子链字段

多段分镜先内部填写：

```text
视觉钩子：
规则钩子：
声音钩子：
物件钩子：
关系钩子：
空间钩子：
问题链：
尾帧钩子：
下一段继承：
```

字段要求：

- `视觉钩子`：观众第一眼看到什么反常动作或画面。
- `规则钩子`：哪条规则开始约束角色身体，而不是只被朗读。
- `声音钩子`：哪个声音先于画面出现，或改变声源方位。
- `物件钩子`：哪个物件状态变了，下一段必须继承。
- `关系钩子`：人物之间的权力、亲密、背叛或隐瞒如何改变。
- `空间钩子`：门、走廊、窗、屏幕、镜子、楼梯、舰桥等空间是否改义。
- `问题链`：观众每15-30秒脑中追问的问题是什么。
- `尾帧钩子`：本段最后一帧留给下一段的视觉/声音/物件。
- `下一段继承`：下一段开头必须拿走的图像锚点、声音尾巴、道具状态。

---

## 4. 15秒段落模板

```text
段落目标：
观众问题：
角色目标：
主悬念载体：
0-3s：视觉问题
3-8s：身体任务
8-12s：信息变化
12-15s：尾帧钩子
下一段继承：
SD段落边界：
```

合格标准：

- 15秒内只做一个主目标，最多两个辅助信息。
- 每个镜头必须推动：位置、规则、关系、物件、声音、危险中至少一项变化。
- 结尾不能是“黑场结束”。结尾要有能接下一段的门缝、眼神、物件、声音、光源或动作。

---

## 5. 60秒开场模板

```text
0-3s：第一眼问题，观众还不知道设定但必须想看。
3-15s：主角身体任务，身份通过动作/服装/反应露出。
15-30s：规则或异常压到主角身上，出口/物件/声音第一次反向。
30-45s：主角做出选择，选择带来更深层空间或更坏代价。
45-60s：正式任务落地，尾帧留下下一场必须处理的物件/声音/人脸/门。
```

短剧开头优先级：

1. 先让身体动起来。
2. 再用声音/物件补设定。
3. 最后用门、屏幕、床、卡片、蜡烛或人脸把主任务钉住。

---

## 6. 多场戏转场链模板

| 前一场尾帧 | 转场桥 | 下一场开头 | 适用 |
|---|---|---|---|
| 门框遮满画面 | 同方向门线/墙线继承 | 新房间同方向打开 | 走廊到病房、梦到现实 |
| 物件特写占满画面 | 纹理匹配 | 新场景同纹理表面 | 卡片纹路到屏幕地图、床单到走廊裂缝 |
| 声音先行 | 声音不断但声源改变 | 新空间找到声源 | 电话、规则声、脚步、舰桥低频 |
| 光源爆白/爆暗 | 同色光残留 | 新场景同色高光落在物件上 | 梦醒、闪回、记忆断层 |
| 角色眼神定住 | 眼神方向继承 | 新场景目标出现在同侧 | 对峙、发现线索、反转 |
| 屏幕/投影填满画面 | 图像刷新/像素扩展 | 新场景成为屏幕中的地点 | 舰桥、监控、系统锁定 |

---

## 7. SD分段承接模板

每个SD段最多30秒。16-30秒默认保持为一份连续提示词，内部按2-4秒自然动作拍组织，并在12-18秒附近完成一次有因果的信息刷新；只有总时长超过30秒或单段任务明显过载时才进入下一段。段与段之间必须写清：

```text
上一段尾帧：
上一段未消失的声音：
上一段未完成动作：
上一段道具状态：
下一段第一帧如何继承：
下一段第一秒的信息变化：
```

SD A区块必须保留：

- 源镜头号。
- 时间段。
- 钩子类型。
- 尾帧锚点。
- 下一段继承锚点。

不要把“高留存、强钩子、节奏快”写进SD正面词。要写具体画面：门缝亮光、手指按住规则卡、远处脚步贴近左耳、投影山谷红点扩大、桌面水杯震出一圈波纹。

---

## 8. 十个可借节奏机制样本

这些是机制训练，不是照搬剧情、角色或商标视觉。

| 样本类型 | 可借机制 | 转译用途 | 不能照搬 |
|---|---|---|---|
| 密闭房间醒来开场 | 先给身体异常，再给空间限制，最后给规则物 | 病房/卧室/收容室第一分钟 | 不要让角色坐着读完整规则 |
| 走廊追逐开场 | 第一眼进入运动，中段用门框/灯带/声音刷新信息，尾帧进门反转 | 规则悬疑冷开场、特工追逐、梦境坍塌 | 不要连续跑15秒没有新空间信息 |
| 屏幕系统锁定 | 大尺度屏幕先压人，再切到指尖/眼神/目标红点 | 舰桥、监控室、调查系统 | 不要把屏幕当静态背景板 |
| 电话/耳语诱导 | 声音先行，角色不回应，手部动作差点违规则 | 不可见威胁、母亲声音、规则试探 | 不要用旁白替代角色反应 |
| 规则物特写 | 物件状态变化先于角色理解，观众读到一半被打断 | 卡片、蜡烛、钥匙、屏幕提示 | 不要拍成产品展示 |
| 家庭争吵爆发 | 每句话都有距离、手势、物件、站位变化，尾帧留下无法收回的动作 | 离婚戏、亲密关系破裂 | 不要让两人原地对喊 |
| 梦境变形 | 一个物理逻辑贯穿变形，旧空间残留在新空间里 | 红辣椒式/盗梦式空间转场 | 不要多种特效混成视觉噪音 |
| 调查发现不对 | 证据先是普通物，第二次出现时改义 | 推理、线索、身份怀疑 | 不要用台词直接说“这里不对” |
| 躲藏屏息 | 近景身体控制，远景危险移动，声音决定剪点 | 床下、门后、柜内、桌下 | 不要靠贴脸吓人解决张力 |
| 结尾反转尾帧 | 回收第一场物件/构图，给出新意义后留空白 | 最后一个镜头、闭环、开放结局 | 不要用解释性台词替代画面回收 |

---

## 9. 虚假安全回收节奏

适用于危险层之后的家庭、生日、病房探视、重逢或日常恢复。目标不是突然吓人，而是让一个旧不变量重写安全场景。

```text
可信的日常安全基线
-> 上一危险层的一项不变量自然留存
-> 普通动作无意激活不变量
-> 声场和注意力收窄
-> 关系意义翻转
-> 尾帧留下可行动的矛盾
```

15秒建议：

```text
0-4s  建立真实任务、稳定空间和放松身体节奏
4-8s  让不变量处在画面内但不抢注意
8-11s 普通动作触发，不使用解释台词
11-14s 人物或观众完成重新理解，声音逐层减少
14-15s 钉住物件、视线、门、火焰或关系距离的矛盾
```

只继承一项：火焰状态、卡片朝向、手上痕迹、熟悉短句、声音方位、缺失物或房间方向。暖色、笑声和慢动作本身不能证明安全；结尾黑场也不能代替回收。

## 9A. Silent Aftermath Rhythm

Use after an irreversible choice, failed rule test, escape, argument, recognition or containment event. The aftermath must show consequence without restarting exposition.

```text
primary action stops
-> body systems recover in an uneven order
-> one object/material residue continues moving or settling
-> uninvolved environment/NPC routine persists or resumes
-> one expected sound fails to return
-> tail frame changes the next objective or relationship
```

For a short beat, preserve one body residue, one object/space residue and one sound absence. Do not add a new twist unless the residue itself is the hook.

### Silent Aftermath Counterpart Recall

Evidence status: B-grade mechanism recall. Use aftermath composition and consequence hierarchy, not exact film timing or plot outcome.

| Film / scene situation | Aftermath frame | Body / object residue | Ambient world behavior | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `No Country for Old Men` - threat or violence leaves a quiet practical space | Hold on room, doorway, vehicle or object relation after the decisive act | Breath, blood/mark, spent object, disturbed lock or abandoned position remains | Air-conditioning, traffic, insects or distant room sound continues without commentary | Let practical environment outlast the dramatic act | Do not use silence as emptiness; retain source-based room tone and evidence |
| `Zodiac` - investigation encounters leave obsession rather than resolution | Stable observation of desk, file, face or ordinary location after information fails to close | Notes, handwriting, watch/time, unfinished document or fixed gaze remains | Office/home routines continue around the unresolved investigator | Aftermath may convert danger into a new long-term objective | Avoid montage summary; one unresolved object must own the tail |
| `Memories of Murder` - return to an ordinary place after years | Keep landscape/field/road ordinary and let the character's gaze carry history | Posture, stopped walk, face direction and empty site act as residue | Everyday passersby/weather continue, indifferent to the old event | Revisit the same composition so absence becomes evidence | Do not rely on audience memory without one repeated place/object anchor |
| `Marriage Story` - argument collapse leaves bodies and room altered | Hold the room after shouting stops; keep both people and damaged distance readable | Red palm, wall contact, broken breath, tears, displaced furniture or unfinished task | Household objects and outside life remain, making rupture more painful | Conflict ends when bodies cannot continue, not when dialogue explains it | Do not immediately add another line that erases the physical consequence |
| `The Godfather` - irreversible action produces a blank behavioral delay | Frame the character with the object/door/people affected by the decision | Hand, face, clothing, weapon/object placement or seated stillness records the crossing | Public environment continues or closes around the new role | A short pause after action can establish identity change | Strip crime plot; avoid heroic slow motion or celebratory scoring |
| `Burning` - absence and uncertain evidence dominate the aftermath | Use empty apartment, landscape, object or long observation instead of a solved reveal | Missing person/object, altered room, stopped routine or unresolved body tension remains | City/country routine continues without confirming the character's theory | Let absence become the primary visual object | Do not add explanatory insert shots that resolve the ambiguity |
| `The Zone of Interest` - domestic routine continues beside excluded consequence | Keep daily task and off-screen evidence in separate but simultaneous channels | Clothing, garden, meal, smoke/light or distant sound carries moral residue | Family/worker routine continues with controlled non-reaction | The world continuing normally can be the most severe aftermath | Do not sensationalize the off-screen event or make everyone visibly react |
| `The Wailing` - family/ritual crisis leaves space and relationships emptied | Hold house, threshold, vehicle or landscape after action has failed | Wetness, ash, clothing, open door, abandoned object or missing voice remains | Weather, insects, distant village or room sound returns unevenly | Let sound recovery order show what the event removed | Strip religious/supernatural resolution; preserve residue, absence and failed return |

## 10. 失败边界

- 不能每15秒只是换一个漂亮画面；必须换观众的问题。
- 不能把所有设定塞进第一段；第一段只负责钩住主问题。
- 不能只用剪辑速度制造紧张；剪辑必须携带信息。
- 不能让尾帧没有承接；下一段开头必须接住一个视觉/声音/物件残留。
- 不能让每段都同一情绪强度；需要短促读懂点，否则观众只会疲劳。
- 不能让SD段落各自为政；角色状态、道具状态、光源方向、声音尾巴必须连续。

---

## 11. Runtime Routing

模块名：整集视觉节奏 / 钩子链。  
位置：生产层，位于短剧节奏之后、正式分镜/SD拆段之前。  
触发词：整集节奏、多场戏、钩子链、问题链、15秒段落、30秒转向、60秒开场、预告节奏、高留存、场景串联、尾帧钩子、SD分段承接。
