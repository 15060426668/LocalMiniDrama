# Effects And Transition Prompting

Use this file when the user mentions `反推提示词`, `视频反推`, `特效提示词`, `转场提示词`, `无缝转场`, `梦境转场`, `幻觉崩塌`, `空间折叠`, `空间旋转`, `重力变化`, `镜面转场`, `遮挡转场`, `匹配转场`, `红辣椒`, `盗梦空间`, or says the storyboard transition idea must be translated into SD / Seedance language.

## 1. Core Rule

SD / Seedance reads visible time-based changes more reliably than abstract transition intention.

Translate every storyboard transition into:

```text
start image -> physical/visual process -> camera relation -> continuity anchor -> end image
```

Abstract labels are only planning tags:

```text
梦境崩塌转场 / 红辣椒式转场 / 盗梦空间式空间变化 / 高级特效 / 无缝切换
```

Write the visible mechanism:

```text
镜头贴近卡片背面的蓝色纸纹，纸纹铺满全画面，纹路像墨水沿纤维扩散，2秒内纸纹变成走廊墙面的剥落漆纹，焦点重新落到墙面裂缝，保留同一条竖向裂缝作为连续锚点。
```

## 2. Source-Informed Prompting Principles

Use these practical rules distilled from current video-model prompt guides and the local video reverse-prompt agent:

- Separate camera movement, establishing scene, subject/action, lighting, and transition process.
- Use positive phrasing: describe what appears, changes, and remains anchored.
- For image-to-video, describe the motion or transformation required; re-describe still-image detail only when continuity needs it.
- Complex transitions need simple physical steps. One strong transformation beats several simultaneous transformations.
- Describe motion explicitly: camera direction, subject movement, environment movement, speed, and timing.
- Use one main camera move per short segment unless the movement is deliberately compound and easy to read.
- Anchor hands, faces, and important props to physical contact during complex effects to reduce unwanted warping.
- For reverse prompting, treat the source video/frame as the only truth: subject, action, scene, camera, light, color, style, time change, and motion rhythm come first.

## 3. Reverse-Prompt Workflow

When reverse-engineering a video, reference, or effect clip into SD language:

1. Identify visible source facts:
   - subject.
   - action and motion rhythm.
   - scene and foreground/midground/background.
   - camera shot, angle, movement, and speed.
   - lighting source, color tone, shadow, reflection, material texture.
   - start frame, middle change, end frame.
2. Identify the transition mechanism:
   - occlusion.
   - graphic match.
   - texture morph.
   - light match.
   - focus melt.
   - reflection/mirror portal.
   - material-state morph: liquid, fragments, sand, smoke, digital glitch, biological growth, cloth/paper tear, fold/mirror.
   - space fold.
   - gravity rotation.
   - hyperspeed travel.
   - object transformation.
   - time freeze / slow-motion debris.
3. Convert into positive SD phrasing:
   - name the anchor.
   - describe the visible process frame by frame.
   - state the camera relation.
   - state what stays continuous.
   - state the ending frame.
4. Keep uncertainty neutral. If a material, place, identity, or mechanism is unclear, use general wording instead of inventing detail.

## 4. Transition Translation Templates

### Occlusion Wipe

Use when a body, doorframe, wall, curtain, darkness, object, or foreground pass hides the cut.

```text
转场：前景门框黑影从左向右吞没全画面，镜头继续同方向移动，黑影退开时露出新空间；保留同一条移动方向和同一侧光线，像一次连续横移穿过门缝。
```

Good anchors:

- doorframe.
- shoulder passing lens.
- curtain.
- wall corner.
- hand covering lens.
- black hallway.
- hair/fabric sweeping across frame.

### Graphic Match / Shape Match

Use for Paprika-like dream logic: two different spaces connect through the same shape, position, or motion.

```text
转场：特写中的圆形怀表占满画面，金色表圈保持在画面中央；表盘反光逐渐变亮，圆形轮廓在同一位置变成病房天花板的圆形灯罩，镜头从灯罩慢慢下移进入新空间。
```

Common matches:

- clock face -> ceiling lamp / moon / plate / eye.
- candle flame -> street lamp / monitor glow / birthday candle.
- card rectangle -> door plaque / hospital sign / phone screen.
- eye -> peephole / camera lens / mirror spot.
- corridor vanishing point -> drawer gap / mouth / tunnel.

### Texture Morph

Use when two surfaces share texture, grain, crack, fiber, wrinkle, water, rust, or shadow.

```text
转场：镜头贴近床单褶皱，布料纹理填满画面；褶皱阴影变深，纤维逐渐变成剥落墙皮和潮湿裂纹，焦点从布面滑到墙面，床单的波浪线保留为走廊墙面的裂缝。
```

Common morphs:

- bedsheet wrinkles -> corridor wall cracks.
- card paper fiber -> peeling paint.
- water reflection -> ceiling light reflection.
- hair strands -> tree branches / wires.
- curtain folds -> stairwell shadows.
- ash / dust -> snow / hospital powder / screen noise.

### Light Match / Exposure Bloom

Use when bright light hides the spatial change.

```text
转场：台灯灯泡突然变亮，暖黄色光晕扩散到全画面，边缘过曝成白；白光慢慢降回曝光，变成医院冷白顶灯，色温从3200K暖黄滑到6500K冷白，灯具位置保持画面中央。
```

Use sparingly. The light source must be visible or motivated.

### Focus Melt / Blur Resolve

Use when focus loss turns one surface into another.

```text
转场：焦点从女主指尖离开，整个画面软化成一片蓝灰色模糊；模糊中保留一条竖向亮线，亮线逐渐锐化成走廊门缝，焦点重新落到门缝边缘。
```

Best for:

- waking from dream.
- losing consciousness.
- hallucination layer shift.
- object proof becoming room proof.

### Reflection / Mirror Portal

Use when reflection becomes the next space.

```text
转场：镜子里的房间反射比现实慢半拍，女主转头后反射仍然看向门；镜面冷光加深，反射中的门缝扩大并填满画面，镜头推进镜面，镜面纹理消失后进入反射里的走廊。
```

Rules:

- reflection must start as a visible surface.
- reflected space must have a clear anchor.
- keep one stable object or light position across the transformation.

### Space Fold

Use for Inception-like architectural transformation. Describe geometry, hinges, gravity, and object reaction.

```text
转场/特效：房间远端墙面像铰链一样向上折起，地板透视线弯成垂直面，书桌上的杯子和纸张先向墙面滑动，窗帘向新的重力方向垂落；镜头保持低角度慢推，人物仍站在原地，背景墙面翻成天花板后露出下一层走廊。
```

For `space folds`, write:

- which plane folds.
- fold direction.
- hinge line.
- how props react.
- how light/shadow changes.
- where the camera stays.
- what the new space is.

### Rotating Room / Gravity Roll

Use for rotating hallway or dream gravity shift.

```text
转场/特效：走廊开始缓慢顺时针旋转，墙灯跟着空间一起转动，地毯从地面变成左侧墙面；人物手掌按住墙面保持身体，钥匙从桌面滑向画面上方，重力方向在3秒内旋转90度，镜头与走廊同速旋转保持人物居中。
```

Rules:

- show fixed environmental lines rotating.
- show objects responding to gravity.
- keep camera relation clear: camera rotates with room, or camera stays level while room rolls.

### Hyperspeed / FPV Portal

Use for fast dream traversal through doors, tunnels, windows, screens, or corridors.

```text
转场：第一人称镜头快速冲向半开的门缝，门缝光线拉成长条，墙面纹理被速度拖成线状残影；镜头穿过门缝后残影变成雨夜街道的霓虹线，速度逐渐减慢，落到街道中央的稳定广角画面。
```

Best when:

- the transition is spatial travel.
- the viewer should feel pulled into another layer.
- the next space has strong linear perspective.

### Time Freeze / Suspended Debris

Use for dream shock, explosion, memory rupture, or impossible pause.

```text
特效：杯子破裂的瞬间时间变慢，水珠、玻璃碎片和纸屑悬在空中，边缘高光清晰可见；镜头从碎片之间缓慢穿过，远处人物动作几乎静止，只有水滴在空中轻微旋转。
```

For suspended impact effects, list:

- debris types.
- direction.
- speed.
- scale.
- light hits.
- camera path through debris.

### Object Transformation

Use for card, book, candle, photo, watch, phone, door, medicine, or clue transformation.

```text
特效：卡片背面的蓝色宝石纹路开始发光，光沿金色线条游走，空白规则区浮现细小墨迹；墨迹不是突然出现，而是像液体渗入纸纤维一样一笔一笔扩散，最后形成清晰文字。
```

Rules:

- transformation starts from a visible material.
- preserve object silhouette unless the story requires morphing.
- describe step-by-step surface behavior.

### Dream Collapse Environment

Use when a normal room degrades into another reality.

```text
特效/转场：卧室暖色逐渐褪成灰绿色，墙纸边缘卷起，潮湿痕迹从墙角向上蔓延；床头台灯闪烁三次后熄灭，窗外夕光被冷白顶灯替代，家具轮廓保留原位置但材质逐渐变成废弃病房的铁床、瓷砖和剥落墙面。
```

Rules:

- preserve layout anchors first.
- transform material second.
- change color temperature third.
- reveal new space last.

## 5. Material Morph Routing

For liquid dissolve, fragment reassembly, particle/sand drift, smoke condensation, digital refresh, biological growth, cloth/paper tear, fold/mirror flip, director-specific matter behavior, or single-object transformation, read `effects-material-morph-library.md`.

Use one dominant material family per short beat and preserve source surface, trigger, moving boundary, inheritance, residual trace, sound/light sync and landing frame.

## 6. A-Block Translation Rule

In SD A blocks, `转场` must include:

```text
transition type + visual anchor + start frame + process over time + camera relation + continuity anchor + end frame
```

If the transition contains VFX, also include:

```text
surface/plane/object affected + physical behavior + light/color change + object reaction + final readable state
```

If it is a material-state morph, also include:

```text
old space/object -> material breakdown state -> motion behavior -> re-aggregation logic -> new space/object -> residual trace
```

Example A-block wording:

```text
转场：纹理匹配转场；镜头贴近床单褶皱，布料纹理铺满画面，褶皱阴影逐渐加深并变成走廊墙皮裂纹，焦点从布料纤维重新落到墙面裂缝，同一条S形褶皱保留为新空间的裂缝锚点。
```

Example E-block wording:

```text
床单褶皱 -> 墙皮裂纹，纹理匹配转场，焦点融化后重新落焦。
```

## 7. Positive Execution Anchors

- Abstract effect labels pair with a physical anchor: surface, object, light edge, crack, shadow, reflection, or doorway.
- One short segment uses one dominant transformation family.
- Material-state morphs follow one readable pathway: melt, crack, drift, evaporate, glitch, grow, tear, fold, reflect, or flood.
- Fast 3-second shots keep one main camera move, one main subject action, and one readable VFX process.
- Character identity remains continuous through stable face, stable costume, and stable body silhouette when identity stability matters.
- Seamless transitions use occlusion, match, texture, light, focus, reflection, or motion continuity.
- Spatial continuity uses a visible anchor: same shadow edge, same light position, same crack line, same object silhouette, same movement direction, or same central shape.
- A blocks express every control as positive visible/audible facts.

## 8. Compact Phrase Bank

Use these as building blocks inside complete prompts:

- `the camera moves through a foreground shadow, revealing the next room`
- `the circular object stays centered and becomes a ceiling lamp`
- `paper fibers dissolve into peeling wall paint`
- `warm lamp bloom overexposes the frame and resolves into cold fluorescent light`
- `focus melts from fingertips into a vertical door slit`
- `the mirror reflection lags behind reality, then becomes the main space`
- `the far wall folds upward like a hinged plane`
- `the room rotates 90 degrees while props slide toward the new gravity direction`
- `suspended water droplets and glass fragments float in slow motion`
- `ink spreads through paper fibers and forms readable symbols`
- `the camera flies through the door crack, motion streaks become neon lines`
- `the same shadow edge continues across the transition`
- `the walls soften like wax, flow into a floor puddle, then harden into a new room`
- `the room fractures into floating concrete and glass pieces, then reassembles into a new corridor`
- `furniture weathers into dust and sand, drifts with the wind, then settles into new solid forms`
- `dense fog swallows the old room, then condenses into new walls and a new doorway`
- `the image glitches into horizontal color bands, refreshes line by line into a new scene`
- `vines grow from floor cracks, cover the old walls, and harden into a new room structure`
- `the wallpaper peels away like printed paper, revealing the real room behind it`
- `the space folds along a central crease like a page turning into another room`

## 9. Source Basis

This module distills:

- local `视频反推提示词.cw-agent.json`: visible-source-first reverse prompting, subject/action/scene/camera/light/color/style/time-change analysis, and prompt consistency checks.
- local `空间变形转场连续过程提示词库.md`: eight material-state transformation chains, director-specific morph processes, single-object morph processes, and continuity/stability wording.
- Runway Gen-3 guide: structured scene/subject/camera prompting, positive phrasing, direct image-to-video movement prompts, and iteration for complex transitions.
- Luma Dream Machine guide: camera motion, pan/orbit/crane/move controls, keyframes, extension, and transition toward a visual target.
- Kling prompt guidance: shot type, camera movement direction, speed/timing, subject action, context, and storyboard-first planning.
- Satoshi Kon / Paprika analysis: match cuts, graphic matches, imaginative wipes, and dream/reality slippage through visual continuity.
- Inception VFX analysis: physicalized space, folding architecture, rotating corridors, gravity shifts, practical contact, and prop reaction as realism anchors.

