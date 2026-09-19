# Output Templates

Use this file when the user wants a formal storyboard, opening options, critique, reverse engineering, single-shot design, or a training deposit.

## 0. Full Decomposition Rule

Do not reduce shot design to one technique. For `拆分镜`, `镜头怎么拍`, `怎么运镜`, `构图怎么做`, or similar requests, include the whole audiovisual mechanism unless the user explicitly asks for a quick one-line answer.

Minimum complete decomposition:

- shot purpose / suspense task.
- composition image: describe the visible frame first, including frame owner, foreground, midground, background, screen position, negative space or occlusion if used.
- screen action: objective visible action inside the frame, including body movement, gaze/face, hands/feet, prop state, background activity, micro physical detail, and sound-linked reaction.
- lens and focus: focal family and focus route when relevant.
- lighting and color: scene master light plus shot-specific execution; include six lighting parameters, color temperature/tone, source logic, texture, and what changes in this exact shot.
- visual tone and image texture: genre/emotional tone, realism/stylization degree, medium/rendering type, grain/sharpness/bloom/diffusion, material rendering priorities, and consistency rule. Keep it separate from light source and exposure.
- camera movement: start, route, speed, end, function.
- sound field: primary source, active `ENV/BODY/OBJ/VOX/FX/INT/MUS` buses, source status, spatial direction/distance, frequency/occlusion/reverb, RMS/peak/relative level, ducking, shot LUFS-S, delivery LUFS-I/dBTP, visible reaction, and beat-by-beat tail bridge.
- transition: continuity anchor, change, hidden or revealed information.
- narrative purpose: what the shot changes in audience knowledge, character state, emotion, or rhythm.
- failure boundary: what would make the shot flat, confusing, cheap, or unshootable.

## 1. Standard Storyboard Output

Use this structure by default for substantial scene design:

```markdown
**核心判断**
- 悬念引擎：
- 观众知道：
- 角色知道：
- 隐藏/不稳定元素：
- 悬念载体：

**电影分镜参考池**
| 影片/场景 | 构图与运镜机制 | 调度与信息释放 | 节奏/声音/转场 | 可复用规则 | 替换项 | 优点/失败边界 |
|---|---|---|---|---|---|---|

**批准的导演综合方案**
- 当前段落/目标时长：
- 采用的参考机制：
- 统一导演语法：
- 为当前短片重新设计：镜头顺序 / 时长 / 摄影机路径 / 调度 / 焦点 / 声音 / 转场

**电影分镜机制细拆**
| 影片/场景 | 构图画面 | 机位与运镜 | 调度/表演/物件 | 信息释放与节奏 | 光影/质感 | 声音设计 | 转场 | 可复用规则 | 失败边界/当前场景替换项 |
|---|---|---|---|---|---|---|---|---|---|

**空间与调度**
- 空间布局：
- 人物/道具位置：
- 光源：
- 声源：
- 运动路线：

**全场视听母版**
- 构图母题：
- 焦段/机位策略：
- 光影母版：
- 画面基调/质感母版：
- 声音母版：delivery profile + 主声音任务 + 七类总线审查/启用规则 + 全场声源地图 + 环境底噪 + 近景拟音主导物 + 画外压力源 + 主观心理音规则 + 静音/冲击使用点 + 镜头LUFS-S范围 + 母版LUFS-I/dBTP + 声音转场母题。
- 转场母题：

**分镜表**
| 镜头号 | 时长 | 景别/焦段 | 构图画面 | 机位与运镜 | 光影/色彩 | 画面基调/质感 | 实拍摄影证据 | 画面内容 | 运动生态/层级交互 | 声音设计 | 转场 | 叙事目的 | 镜间变化/尾帧 |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|

**逐镜声音执行表**
| 时间/镜头 | 主声源 | 启用总线/具体声源 | 方位/距离/权限 | RMS dBFS / peak dBFS / 相对电平 | 频段/遮挡/RT60/dry-wet | 闪避/掩蔽 | 镜头LUFS-S/估算能量和 | 母版LUFS-I/dBTP | 声画触发 | 尾音/声桥 |
|---|---|---|---|---|---|---|---|---|---|---|

**SD/Seedance 转写准备**
- 分镜表是下游 SD 输出的源表；转写时不得丢失任何镜头行。
- SD/Seedance 转写是无损编译，不是再创作摘要。A区块必须能逐项追踪回源分镜的具体名词、位置、构图层次、动作节拍、道具/背景变化、微物理细节、声音触发反应和转场锚点；如果一行太密，拆成多个A段，不能删细节。
- 默认模型载荷为精简 `BASE LOCK + A区块`。E、完整混音计量和自审属于按需制作附件，不混入可复制的模型执行词。
- `空间与调度/全场母版` -> `BASE LOCK`，只保存稳定人物、空间、固定道具、全局光色质感、跨镜关系和声音母版。
- `景别/焦段 + 构图画面 + 机位与运镜` -> A区块 `镜头与构图`，保留焦段/景深、前中后景、遮挡/负空间、屏幕方向、机位高度/角度/距离、设备、路线、速度、起落点。
- `画面内容`中的人物动作与表演 -> `主体动作与表演`；保留动作顺序、姿态、眼神、呼吸、手脚、口型、微表情和落点。
- `运动生态/层级交互 + 实拍摄影证据`中的听者、道具、NPC、环境力、接触和材质因果 -> `关系/物件/环境反馈`。
- `光影/色彩 + 画面基调/质感 + 声音设计 + 转场` -> A区块 `声光与转场触发`：只写本拍相对BASE发生的光色/材质差量、可听声源、方位、先后、主观权限、可见反应、声桥和完整转场过程；RMS/peak/LUFS/dBTP/EQ/RT60/ducking -> 独立声音后期附件。
- `镜间变化/尾帧 + SD承接锚点 + 连续性校验` -> 单一 `尾帧与连续性` 字段：起始继承 / 本镜差量 / 落点状态 / 易丢锚点 / 下一镜继承。
- 上游 `SD承接锚点`仍可作为源数据，但下游把它嵌入所属的动作、物件、机位、光、声音或转场字段，不再独立复述。
- E只在无损母版、剪辑索引或程序审计时输出；存在时必须与A时间一致。
- 电影参考只属于上游创作过程，不进入SD来源锁或校验和。

**关键记忆点**

**风险修正**

**自检评分**
| 维度 | 分数 | 判断 |
|---|---:|---|
```

Shot table fields must be concrete:

- `时长`: seconds or range.
- For AIGC short drama / vertical suspense, static single-camera shots default to `1-4s`; do not exceed `4s` unless there is internal motion or information change. Long camera moves may exceed `4s` only when split into micro-beats.
- `景别/焦段`: shot size + focal family + perspective effect + emotional/information reason. Do not write only "medium shot" or "35mm"; say whether it gives room geography, human observation, compression, voyeur distance, subjective distortion, or object proof.
- `构图画面`: describe what the audience literally sees before explaining function. Include frame owner, foreground, midground, background, subject placement, frame edges, empty/blocked area, occlusion, geometry owner, scale/visual weight, screen direction, and information function. Do not write only abstract labels such as "power relation", "negative space", "symmetry", "Nolan geometry", "Hitchcock voyeur frame", or "Fincher control"; make the frame drawable from text.
- `机位与运镜`: camera height, angle, distance, movement device, start/end, route, speed, axis/coverage if dialogue, and movement purpose. The field must show how to shoot it, not only what the movement symbolizes.
- `光影/色彩`: use parameterized lighting language, not vague atmosphere. Include brightness/exposure, contrast, light ratio, light quality, light position, shadow share, color temperature/K, tone shift, saturation, mixed-color logic, accent owner, and practical source.
- `光影/色彩` is shot-specific. It must state what this camera angle sees: main source direction, subject/object lit area, shadowed area, background brightness/color, practical source position, key/fill/negative fill/rim logic, and what changes from the previous shot. Scene master tone is allowed above the table, but cannot replace this field.
- `光影/色彩` must describe the whole photographic look, not a tiny local note. Include global color palette, color temperature, key/fill/backlight logic, contrast curve, shadow share, background separation, skin/material texture, highlight/shadow detail, practical-light motivation, and how the look changes with tension. Do not write weak fragments such as "eye shadow is heavy" unless they sit inside a full lighting scheme.
- `光影/色彩` must avoid the common failure set unless intentionally used: flat-light face, dead-black shadow, blown-out highlight, chaotic color temperature, wrong light position, cheap oversaturation, contrast with no midtones, and light/emotion mismatch.
- `画面基调/质感`: keep separate from `光影/色彩`. Include genre/emotional tone, realism/stylization degree, medium/rendering type, surface texture, grain/sharpness/bloom/diffusion, lens or digital artifacts, material rendering priorities, and consistency rule. Do not write only "电影质感", "高级质感", "3D质感", or "写实质感"; specify what the image surface actually feels like.
- `实拍摄影证据`: state camera placement, motivated source, strongest material response, foreground/midground/background depth, captured human action moment, natural imperfection, and continuity/post evidence. Use at least five relevant proofs; omit irrelevant technical padding.
- `画面内容`: objective screen-action record, not plot summary or emotion label. Write what visibly happens inside the frame in beat order: start posture/action -> trigger -> reaction -> prop/background change -> tail frame. Include the layers present in the shot: body movement, gaze direction, facial micro-change, breath, hand/finger/foot behavior, prop position/state/movement/texture, background movement or stillness, micro physical details such as liquid, dust, fabric, reflection, metal glint, screen flicker, flame, shadow, and the visible reaction caused by sound. Do not write only "女主害怕", "两人继续争吵", "房间压抑", or "桌上有卡片"; make the action drawable and performable.
- `声音设计`: write a routed and metered sound field, not one or two environment sounds. Name one primary source; list active `ENV/BODY/OBJ/VOX/FX/INT/MUS` stems; state visible/off-screen/subjective/structural status, who hears or ignores it, direction/distance, frequency focus, occlusion/EQ, RT60/dry-wet, per-stem RMS dBFS and peak dBFS, relative level, ducking/masking, shot LUFS-S, delivery LUFS-I/dBTP, visible reaction and tail bridge. Bare `-20 dB` is invalid. Combined dB uses logarithmic summation from `sound-mix-metering.md`.
- `转场`: continuity anchor, cut/match/occlusion/focus/light/sound logic, what changes at the edit.
- `叙事目的`: what the shot changes in information, emotion, character state, rhythm, or foreshadowing. If this is empty, delete or redesign the shot.
- `镜间变化/尾帧`: state what changes from the previous shot or beat, why the cut/move happens now, and the exact body/object/light/sound state inherited by the next shot. If no controlled variable changes, merge or redesign the shot.

For each target scene or segment, return zero to six useful film-reference mechanisms when they materially help. Do not require equal duration, timestamps, exact shot numbers or one-film binding. After the user approves one option or a combination, include `批准的导演综合方案` before the formal segment shot table. If no reference helps or the user declines references, use an approved original director scheme. For formal training, user-fed reference material, or any request to "拆对标", include `电影分镜机制细拆`:

```text
影片/场景 | 构图画面 | 机位与运镜 | 调度/表演/物件 | 信息释放与节奏 | 光影/质感 | 声音设计 | 转场 | 可复用规则 | 失败边界/当前场景替换项
```

- Each returned film option must provide at least one concrete camera, staging, rhythm, sound, transition, performance, object or background mechanism; candidate count is never padded.
- The user may choose one option or combine named mechanisms from several options. Before formal storyboarding, state one unifying director grammar and resolve conflicts.
- `当前场景替换项` states the identities, props, dialogue, setting, knowledge and rule variables replaced for the current story.
- Do not report film timestamps, rough locations or exact shot numbers unless the user explicitly requests an audit of supplied footage.
- The formal storyboard retimes and redesigns every shot for the target short; it does not preserve source-film pacing.
- `电影分镜机制细拆` must not become plot summary. It must describe drawable frames, audible layers, reusable rules and failure boundaries.

For professional cinematography tasks, also enforce:

- composition must choose 1-3 tools only and render them visibly: symmetry, one-point perspective, repeated array, frame-within-frame, leading lines, negative space, foreground occlusion, centered ritual frame, Dutch angle, mirror split, silhouette, evidence plane, or scale contrast.
- lens/focus must include focal length effect, aperture/depth choice, and focus route when information shifts.
- movement must include the physical device: handheld, gimbal/steadicam, dolly/track, jib/crane, slider, drone/aerial, locked-off tripod, or CCTV/fixed.
- dialogue coverage must state the axis, two-shot/OTS/single/insert/reaction logic, and whether power changes through shot size, camera height, or screen direction.
- lighting execution must state practical source plus add/subtract/block/bounce logic when the shot needs production feasibility.

## 2. High-Retention Opening Options

When the user asks for openings or first-shot concepts, give multiple options. Each option must include visual hook, information question, retention reason, and risk.

```markdown
**开场方案 A：标题**
- 第一眼画面：
- 观众立刻想问的问题：
- 10 秒内的信息释放：
- 机位/构图：
- 光影/声音：
- 转场进入正戏：
- 停留率优势：
- 风险：
```

High-retention opening principles:

- first frame must contain a visual contradiction, urgent question, beautiful threat, impossible action, or emotionally charged object.
- do not spend the first seconds on neutral exterior beauty unless the exterior itself contains a mystery.
- rules can appear early, but must be visually staged, not only read.
- if the hook is calm, the composition must be unusually controlled: partial face, impossible shadow, overhead layout, text/prop conflict, or sound-image mismatch.
- if the hook is intense, the next beat must clarify the rule fast enough that the viewer does not feel cheated.

## 3. Single-Shot Design Template

Use when the user asks "这个镜头怎么拍". This template is mandatory for single-shot answers unless the user explicitly asks for only one narrow item.

```markdown
**镜头目的 / 悬念任务**
- 观众此刻知道：
- 角色此刻知道：
- 这个镜头要隐藏：
- 这个镜头要释放：

**画面设计**
- frame owner：
- foreground：
- midground：
- background：
- screen position / negative space：
- geometry / scale / visual weight：
- camera height：
- lens/focus：focal length family -> perspective effect -> aperture/DOF -> focus start/delay/rack/landing proof

**画面内容 / 表演与物件**
- 起始姿态：
- 眼神/表情：
- 手部/脚步：
- 道具状态：
- 背景动静态：
- 微物理细节：
- 声音触发的可见反应：
- 尾帧：

**光影**
- scene lighting master：
- shot-specific lighting change：
- current camera angle sees：
- brightness/exposure：
- contrast：
- light ratio：
- light quality：
- light position relative to subject/camera：
- shadow share：
- key / fill / negative fill：
- rim / practical：
- background separation：
- color temperature / tone shift / saturation：
- mixed-color logic：
- texture and detail：

**运镜**
- device：
- camera height / angle / distance：
- start：
- route：
- speed：
- end：
- function：
- axis / coverage if dialogue：

**声音**
- sound task：
- delivery profile：
- primary sound source / narrative owner：
- active buses：ENV / BODY / OBJ / VOX / FX / INT / MUS
- source status / who hears / who ignores：
- screen position / distance：
- frequency focus / occlusion EQ：
- RT60 / pre-delay / dry-wet：
- per-stem RMS dBFS / peak dBFS / relative dB：
- ducking / masking：
- shot LUFS-S / estimated energy sum / peak headroom：
- master LUFS-I / dBTP：
- visible reaction：
- sound change / transition bridge / tail：

**转场**
- continuity anchor：
- change：
- hidden/revealed information：

**叙事目的**
- 信息变化：
- 情绪变化：
- 节奏位置：

**可复用规则**
- 

**反例边界**
- 

**可迁移镜头模板**
- 

**风险与修正**
```

## 4. Reverse Engineering Template

Use when the user supplies a film scene, screenshot, PDF analysis, or weak generated result.

```markdown
**整体悬念判断**

**任务层**
- 观众信息：
- 角色信息：
- 情绪目标：
- 信息释放点：

**结构层**
- 构图：
- 光影：
- 运镜：
- 分镜/剪辑：
- 声音：
- VFX/转场：

**语言层**
- 可复用镜头模板：
- 可迁移规则：
- 反例风险：
- 应写入模块：

**对当前项目/场景的迁移**
```

Do not summarize only motifs. Extract the machine: what camera, light, sound, rhythm, and information timing are doing.

## 5. Training Deposit Template

Use when the user says to write into MD, train the skill, or deposit a new rule.

Every training extraction must produce exactly these four deposits before any optional commentary:

1. 可复用规则
2. 反例边界
3. 可迁移镜头模板
4. 应写入哪个模块

```markdown
## YYYY-MM-DD - Training Entry

Source:
Use case:
Training type:
Training target:

Reusable rules:
- 

Failure boundaries:
- 

Transferable shot template:
- Name:
- Task:
- Foreground:
- Midground:
- Background:
- Camera:
- Lighting:
- Sound:
- Duration:
- Best use:

Target module:
- 

When to invoke:
- 
```

Do not deposit unconfirmed story settings as permanent rules. Mark uncertain ideas as `candidate`, not `locked`.

## 6. Six-Dimension Self-Audit

Use this scoring for final storyboard answers:

| Dimension | Weight | Check |
|---|---:|---|
| Suspense | 25% | information gap, expectation, withheld/released proof |
| Emotion | 20% | all elements point to the same feeling |
| Visual logic | 20% | composition, light, lens, movement have reasons |
| Shootability | 15% | camera path, blocking, light, and VFX are physically executable |
| Rhythm | 10% | setup, delay, threshold, reveal, aftermath are proportionate |
| Detail/foreshadowing | 10% | object, sound, light, or repeated frame carries future meaning |
| Screen action detail | required gate | `画面内容` records body, gaze/face, hands/feet, props, background, micro physical detail, and sound-linked reaction instead of plot summary |

Passing target:

- total score `8+`.
- no single dimension below `6`.
- if a score is weak, name one concrete repair instead of vague advice.

## 7. Common Failure Repairs

- Suspense weak: define audience vs character knowledge and add one physical carrier.
- Too flat: add foreground/midground/background or change camera height.
- Too bright: motivate shadow and decide what darkness hides.
- Too many cuts: make each cut reveal new information or replace with movement.
- Hard cut feels cheap: use object, light, sound, texture, focus, or occlusion continuity.
- Dialogue dead: add listener action, prop handling, background behavior, and off-screen pressure.
- Screen action shallow: rewrite `画面内容` as objective visible action with start posture, trigger, reaction, prop/background change, micro physical detail, sound-linked response, and tail frame.
- VFX generic: attach transformation to wall, fabric, flame, screen, reflection, paper, or sound.
- Director style soup: choose one primary grammar and cut decorative references.
