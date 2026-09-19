# Screen Action Breakdown

Use this file when the user mentions `画面内容`, `动作拆解`, `神态`, `微表情`, `拉片`, `逐镜`, `逐镜拉片`, `客观记录`, `专业拉片`, `画面太粗浅`, or says the storyboard reads like plot summary / reading comprehension.

## Table Of Contents

1. Core definition
2. Boundary with composition
3. Required observation layers
4. Beat-level writing method
5. Sound-synced visual action
6. Anti-patterns and repairs
7. Output templates
8. Training deposit

## 1. Core Definition

`画面内容` is the objective record of what happens inside the frame. It is not theme analysis, plot explanation, mood labeling, or director commentary.

Write only visible or audible facts:

- what the character does.
- how the body changes: posture, head angle, shoulders, breath, hands, fingers, feet.
- how the face changes: gaze direction, blink, eyelid tension, mouth, jaw, cheek, throat, skin reaction.
- what objects do: position, state, movement, reflection, vibration, liquid, dust, fabric, paper, metal, screen, light.
- what the background does: people, curtains, appliances, rain, smoke, shadows, doors, screens, vehicles, hallway movement.
- what remains still, if the stillness is visible and meaningful.
- what sound happens at the same beat and what visible action answers it.

The test:

```text
Can a storyboard artist, animator, actor, camera operator, sound designer, or video model recreate this shot from the words alone?
```

If the answer is no, the `画面内容` is too shallow.

## 2. Boundary With Composition

Do not merge `构图画面` and `画面内容`.

`构图画面` answers:

```text
Where is everything in the frame?
Foreground -> midground -> background -> subject placement -> empty/blocked area -> geometry -> scale/visual weight -> frame function.
```

`画面内容` answers:

```text
What visibly happens inside that frame, beat by beat?
Body action -> facial action -> hand/foot detail -> object state/change -> background activity -> micro physical effect -> sound-linked reaction.
```

Example distinction:

- 构图画面: `前景是半开的门框遮住左侧1/3，中景女主坐在床右侧边缘，背景镜子和衣柜形成两层框中框，门缝黑区占画面右上角。`
- 画面内容: `女主先低头看自己右手，拇指反复摩擦掌心红印；她听到门外一声轻响后停止呼吸，眼睛从手掌移到门缝，嘴唇微张，左脚慢慢踩到地板但没有完全落稳。`

Keep `画面内容` separate from `运动生态/层级交互`:

- `画面内容` records exactly what each visible action looks like.
- `运动生态/层级交互` records which layer owns attention, who can see/hear/know or must perform ignorance, any public/private behavior split, what force/trigger connects the layers, how NPCs/props/environment respond, what continues moving and what remains at the tail frame.

Example:

- 画面内容：`她把钥匙放到桌面，男方眼睛落向钥匙，背景孩子仍在折衣服。`
- 运动生态/层级交互：`钥匙落桌为主运动；男方手停和孩子折衣动作中断为反应层；窗风持续推动窗帘与植物叶片；钥匙声触发冰箱底噪停下；尾帧保留钥匙、水纹和孩子悬停的双手。`

## 3. Required Observation Layers

For formal storyboard rows, `画面内容` must cover the layers that are present in the shot. Do not force irrelevant layers, but never reduce the field to a plot sentence.

### Character Body

Record:

- start posture and end posture.
- weight shift, leaning, recoil, step, turn, freeze, collapse, reach, pull, grip, release.
- shoulder, neck, jaw, back, knees, feet, fingers when readable.
- breath as visible movement: chest lift, throat swallow, mouth opening, nostril flare.

### Face And Gaze

Record:

- gaze start and landing point.
- blink, eyelid tension, pupil/gaze delay when visible.
- mouth corner, lip pressure, jaw tightening, cheek tremor, forced smile, smile collapse.
- when the character avoids looking at something.

### Hands And Props

Hands often carry suspense better than dialogue. Record:

- what the hand touches, misses, hides, presents, grips, drops, folds, wipes, slides, opens, closes.
- finger-level detail when it changes the beat: knuckle whitening, nail scraping, ring turning, thumb hovering, trembling, delayed release.
- prop state before and after: cup full/empty, card face/back, phone screen on/off, door locked/unlocked, flame upright/shaking, medicine bubble rising.

### Objects And Micro-Physics

Record visible small events:

- water path, droplet, steam, condensation, ash, dust, hair, curtain, paper edge, cloth wrinkle, reflection, screen flicker, metal glint.
- object motion caused by off-screen force: cup tremor, hanging lamp sway, shadow shift, door gap widening, dust falling from ceiling.
- material response: wet fabric clings, glass fogs, metal catches a thin highlight, paper fibers lift, candle wax runs.

### Background And Environment

Record whether the background is alive or unnaturally still:

- hallway light flicker, appliance vibration, rain on window, TV glow, curtain draft, elevator number, distant figure, open door gap, moving shadow.
- secondary people: who enters, leaves, watches, stops, pretends not to watch, repeats an action.
- stillness as fact: `all background movement stops after the sound`, not `the room becomes scary`.

### Screen / Text / Evidence

When screen, text, card, photo, note, monitor, or evidence appears:

- write exactly what is visible enough to read or partially read.
- write how it enters the viewer's attention: focus rack, hand reveals, reflection catches, light turns on, foreground moves away.
- write whether the character reads it before, after, or at the same time as the viewer.

## 4. Beat-Level Writing Method

For shots longer than 2 seconds, split the `画面内容` into micro-beats inside one row.

Use this compact internal order:

```text
起始动作 -> 触发点 -> 反应 -> 物件/背景变化 -> 结束姿态/尾帧
```

For dense shots, use beat marks:

```text
0-1s: ...
1-2s: ...
2-4s: ...
```

Do this especially for:

- waking up.
- discovering a rule/object.
- dialogue reaction.
- violent action.
- dream collapse.
- object transformation.
- a character listening to off-screen sound.
- AIGC short drama shots where a static camera must refresh every 1-4 seconds.

## 5. Sound-Synced Visual Action

Sound design and `画面内容` must talk to each other.

When a sound occurs, write the visible response:

- `门外轻响` -> eyes stop, fingers freeze, shoulder tightens.
- `phone vibration` -> hand moves toward it, stops before touching, screen reflection pulses on face.
- `room tone drops` -> character's breath becomes visible, background appliance stops, curtain stills.
- `off-screen footstep` -> gaze shifts upward, head tilts, foot withdraws from floor.
- `sudden silence` -> actor's body stillness and micro-movement become the shot.

When the image changes, write the sound consequence:

- door gap opens -> hinge creak moves from right channel to center.
- candle flame bends -> small flame flutter rises in the mix.
- hand grips glass -> skin squeak and glass tick become near foley.
- light flickers -> electrical buzz cuts or stutters.

## 6. Anti-Patterns And Repairs

### Anti-pattern: emotion label

Weak:

```text
女主害怕地看向门。
```

Repair:

```text
女主的眼睛先停在床头电子钟上，听到门外轻响后迅速移向门缝；她嘴唇张开但没有出声，右手还抓着被角，指节慢慢发白，肩膀向内缩紧。
```

### Anti-pattern: plot summary

Weak:

```text
夫妻继续争吵，丈夫很生气，妻子很伤心。
```

Repair:

```text
丈夫把钥匙推到桌中央，钥匙撞到杯底停住；妻子没有看他，只用食指把戒指转了一圈又按住，眼眶泛红但没有落泪。丈夫说话时身体前倾，妻子向后退半步，后背碰到餐边柜，柜上的相框轻轻晃了一下。
```

### Anti-pattern: vague object mention

Weak:

```text
桌上有一张卡片。
```

Repair:

```text
卡片背面朝上压在水杯旁，边角被水汽浸湿微微翘起；台灯闪一下时，卡背纹路短暂显出蓝色反光，女主的指尖停在卡片上方两厘米处迟迟没有落下。
```

### Anti-pattern: background dead

Weak:

```text
背景是卧室。
```

Repair:

```text
背景衣柜门留着一条细缝，缝里没有亮光；窗帘被空调风轻轻吹起，墙上的日历边角拍打墙面，镜子只反出床尾和半盏台灯。
```

### Anti-pattern: action without tail frame

Weak:

```text
她起床走向门。
```

Repair:

```text
她先把左脚探到地板上，脚尖碰到拖鞋又缩回；第二次落脚时手扶住床沿，床单被指尖拖出一道皱褶。她站起后没有立刻走，先回头看枕边空处，随后朝门走两步，停在门把手前，右手悬在把手上方。
```

## 7. Output Templates

### Storyboard Row Field

Use this rule inside every formal storyboard table:

```text
画面内容：客观可见动作记录；按起始动作 -> 触发点 -> 反应 -> 物件/背景变化 -> 结束姿态写。必须包含本镜头存在的角色动作、神态/眼神、手部/脚步细节、道具状态、背景动静态、微物理变化、声音同步反应。禁止只写情绪标签、剧情摘要或导演解读。
```

### Single-Shot Answer Field

For a single-shot design, include:

```markdown
**画面内容 / 表演与物件**
- 起始姿态：
- 眼神/表情：
- 手部/脚步：
- 道具状态：
- 背景动静态：
- 微物理细节：
- 声音触发的可见反应：
- 尾帧：
```

### Reverse Engineering Field

When doing professional shot-by-shot reverse engineering, record:

```text
timecode/duration -> shot size/camera movement -> visible body action -> face/gaze -> hand/foot -> object/background detail -> sound layer change -> cut/transition.
```

For high-density action or montage, timing may go down to 0.3-0.5 seconds if the source or training task demands it.

## 8. Training Deposit

Training type: 画面内容专项 - 专业逐镜拉片客观记录

Training target: upgrade `画面内容` from plot summary to visible screen-action logging; make every shot production-readable and drawable.

**可复用规则**

- `画面内容` must be objective visible action, not interpretation.
- Separate frame layout from frame action: composition locates elements; screen action records what they do.
- Character action must include posture, gaze, face, hands, feet, breath, and end state when readable.
- Props and environment must have state and behavior, not just names.
- Sound events must have visible reactions, and visible actions should have foley or sound consequences when relevant.
- Shots longer than 2 seconds should be internally broken into micro-beats if the image changes.
- In AIGC short drama, every 1-4 seconds needs a visible/audible information refresh unless a designed long movement carries multiple micro-beats.

**反例边界**

- Do not write emotion labels instead of visible behavior.
- Do not write plot summary in `画面内容`.
- Do not let dialogue freeze the body, hands, props, background, light, or sound.
- Do not mention props without state, position, texture, or change when the prop matters.
- Do not leave background empty unless the emptiness/stillness is itself described as visible fact.
- Do not use micro-detail randomly; it must clarify suspense, performance, evidence, rhythm, or continuity.

**可迁移镜头模板**

- 模板名：逐镜画面内容客观记录模板
- 前景：record blocking object, hand, prop, fabric, door edge, reflection, shadow, or empty frame area and whether it moves.
- 中景：record actor posture, route, gaze, facial micro-change, hand/foot action, and reaction to sound or object.
- 背景：record secondary movement, stillness, screens, practical lights, weather, doors, corridor, furniture, and texture changes.
- 机位/景别/焦段：wide shots prioritize spatial actions and background behavior; close shots prioritize face, hands, object surface, and breath.
- 运镜/时长：for shots over 2 seconds, write internal beats; for montage/action, record 0.3-0.5 second actions when needed.
- 光影：record visible light behavior on body, object, background, reflection, shadow, and material surface.
- 声音：pair every important sound with a visible response or visible source.
- 适用场景：formal storyboard rows, reverse engineering, SD A block, animation direction, actor blocking, suspense openings, dialogue scenes, dream/hallucination transitions.

**应写入哪个模块**

- 输出层 - 画面内容字段硬性规范.
- 训练层 - 专业拉片客观记录.
- SD输出层 - A区块逐时间段画面内容规范.
