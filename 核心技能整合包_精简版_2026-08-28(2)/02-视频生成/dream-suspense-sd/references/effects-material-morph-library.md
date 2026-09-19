# Effects Material Morph Library

Use this reference for continuous matter-based deformation and transformation. Read `effects-transition-prompting.md` for ordinary occlusion, match, light, focus, mirror, space-fold, gravity-roll, hyperspeed, or time-freeze transition grammar.

Every material process follows:

```text
source surface/object -> trigger -> moving change boundary -> material behavior -> old-to-new inheritance -> new state -> residual trace -> sound/light sync -> landing frame
```

## 1. Material-State Morph Library

Use this when the user asks for spatial deformation, dream collapse, surreal transition, or a VFX transition that must feel continuous. Choose one dominant material logic per transition. Combine multiple morph types only when the sequence is deliberately chaotic and the user has requested instability.

Core chain:

```text
old space/object -> material breakdown state -> motion behavior -> re-aggregation logic -> new space/object -> residual trace
```

Required variables:

- `origin surface`: wall, floor, ceiling, mirror, card, photo, bed sheet, shadow, screen, doorway.
- `breakdown trigger`: heat, water, crack, wind, smoke, signal error, biological growth, hand pull, fold line, shadow movement.
- `matter behavior`: flow, rotate, drift, evaporate, glitch, grow, tear, fold, reflect.
- `camera relation`: locked-off observation, slow push, orbit, POV pull-in, macro push, tracking with the material.
- `continuity anchor`: shape, crack line, light edge, color, object position, motion direction, sound, or central point.
- `end state`: new wall, new room, new object, new light source, new corridor, new landscape.
- `residual trace`: water mark, seam, dust, smoke, crack, shadow edge, digital artifact, leaf, paper scrap, frost, paint mark.

### 1.1 Liquid Dissolve

Use when solid space melts, flows, pools, and re-solidifies.

```text
转场/特效：墙角和地板边缘先软化，墙皮像蜡一样下垂，木质家具变成琥珀色黏稠液体，金属边缘变成水银般的银色流体；所有液体顺着同一个坡度流向画面中央，在地面形成旋涡，镜头低角度贴着液面慢慢推进；旋涡速度放缓后液体从中心向上凝固，像3D打印一样堆出新的地面、墙体和家具，最后表面硬化成新空间，只留下流动过的波纹和湿亮高光。
```

Best anchors:

- candle wax, water puddle, mirror surface, melting wall paint, spilled drink, rain reflection.

Use for:

- dream melt.
- memory softening.
- room becoming another room.
- object proof liquefying into environment proof.

### 1.2 Fragment Reassembly

Use when solid space cracks into pieces, floats, rotates, and rebuilds.

```text
转场/特效：墙面先出现细裂纹，裂纹像蛛网一样爬满墙、地板和天花板；整个空间碎成大小不一的石块、木片和玻璃片，碎块失去重力悬在空中缓慢旋转，边缘反射冷光；镜头从碎块之间穿过，碎块按新的坐标一块块移动、翻转、卡入位置，拼出新的墙线、门框和家具轮廓，最后一块碎片咔哒合上，接缝逐渐消失，新空间完整成型。
```

Best anchors:

- cracked mirror, broken tile, shattered glass, fractured concrete, puzzle-like floor.

Use for:

- rule-based world reset.
- evidence room rearrangement.
- reality breaking but remaining physically readable.

### 1.3 Particle / Sand Drift

Use when objects weather into dust, sand, ash, pixels, or small particles, then drift and re-form.

```text
转场/特效：旧空间从边缘开始风化，墙面、床、门框表层一层层剥成细沙，沙粒被画面右侧的风卷起，原本的家具轮廓逐渐变薄直至消散；空气里充满漂浮颗粒，镜头顺着风向缓慢横移；风速下降后颗粒在新位置落下并堆积，先形成地面线，再形成墙面和物体边缘，沙粒逐渐凝硬成石材、木材和金属，新空间清晰起来，空气中还剩少量浮尘慢慢落下。
```

Best anchors:

- ash, dust, desert sand, wall powder, snow-like particles, pixel grains.

Use for:

- memory erasure.
- ancient/fantasy space change.
- dry decay, abandonment, evidence disintegration.

### 1.4 Smoke / Vapor Condensation

Use when space evaporates into smoke, fog, shadow vapor, or heat distortion, then condenses.

```text
转场/特效：墙角冒出白雾，雾气沿地面扩散并爬上家具，所有被雾包住的边缘开始透明化，像干冰一样慢慢气化；房间被浓雾吞没，只剩几条门框和灯光轮廓，镜头保持慢推穿过雾层；雾气在前方收缩变密，从中心凝结出新的墙面、地板和门，最后一缕烟贴着门缝消失，新空间完全露出，空气里保留薄薄的雾和冷光晕。
```

Best anchors:

- breath, cigarette smoke, dry ice, foggy mirror, black shadow tide, steam.

Use for:

- ghostly transition.
- dream conceal/reveal.
- low-budget seamless scene swap.
- shadow swallowing a room.

### 1.5 Digital Glitch / Refresh

Use when the image itself is a screen/signal/data layer.

```text
转场/特效：画面边缘出现彩色色带，墙面和人物轮廓轻微错位，随后横向雪花条纹从上到下扫过；家具和门框像卡带一样拉伸、压扁、跳帧，短暂出现重影和乱码色块；屏幕中心出现一次清晰刷新波，旧画面被逐行擦除，新空间从低清像素块开始加载，分辨率逐渐升高，色块合并成稳定的新房间，最后画面恢复干净连续的运动。
```

Best anchors:

- phone screen, monitor, surveillance feed, TV static, digital clock, camera viewfinder.

Use for:

- surveillance unreliability.
- AI/system illusion.
- memory recording.
- procedural or cyber suspense.

### 1.6 Biological Growth

Use when plants, mold, tissue, roots, veins, hair, or organic matter grows over the old space and becomes the new structure.

```text
转场/特效：地板裂缝里伸出细藤，藤蔓沿墙面快速爬升，叶片覆盖旧墙纸，旧空间的边缘被绿色植物遮住；藤蔓变粗成木质枝干，枝干互相缠绕成新的门框、墙线和家具支架，镜头跟着藤蔓向上移动；叶片逐渐变密，遮住最后一块旧墙，随后植物结构硬化成新的房间轮廓，叶片仍轻轻颤动，墙角保留几根细根作为残痕。
```

Variant:

```text
霉菌从墙角扩散成黑色绒毛，腐蚀旧材质，随后硬化成岩洞般的新结构。
```

Use for:

- uncanny living room.
- infection / contamination.
- fairy-tale or forest dream transition.
- body horror when using tissue, veins, or membrane.

### 1.7 Cloth / Paper Tear

Use when the old space behaves like a printed cloth, wallpaper, paper layer, curtain, or stage backdrop.

```text
转场/特效：旧房间的墙面边角翘起，露出纸张厚度，整面墙像贴纸一样被风掀开；纸面印着旧空间的图案，门和家具只是纸上的平面图像，纸张被一层层吹走，碎纸在镜头前翻飞；每撕开一层，后面露出更多新空间的真实墙面和光线，最后一张旧墙纸飞出画面，新空间完整显现，只剩几片纸屑贴在地角。
```

Best anchors:

- wallpaper, curtain, bedsheet, photo paper, card surface, stage drape.

Use for:

- theatrical reveal.
- dream set illusion.
- childhood/memory paper world.
- fast but elegant seamless reveal.

### 1.8 Fold / Mirror Flip

Use when space folds like paper, flips like a book page, or reflection becomes reality.

```text
转场/特效：空间沿画面中央的垂直线产生折痕，左右墙面像纸页一样向内翻折；翻折时能看到薄薄的空间厚度，旧房间印在纸页背面逐渐暗下去，新空间的走廊纹理出现在正面；镜头保持居中慢推，折线始终在画面中央，最后两侧页面啪地展开成新的房间，折线消失，只保留一条极细的光痕。
```

Mirror variant:

```text
镜面先像水面一样起波纹，反射里的房间慢慢变成另一个空间；反射空间向外鼓起，镜面玻璃变薄并消失，镜中走廊和现实地面无缝接上，镜头推进镜面后进入新空间。
```

Use for:

- Nolan-like spatial logic.
- dream layer shift.
- impossible room.
- mirror hallucination.

## 2. Director-Specific Morph Grammars

Use director names as transformation logic through visible matter behavior.

### Hitchcock: Shadow Swallow

```text
转场/特效：百叶窗影子从墙面慢慢爬下来，影线变长变宽，像黑布一样覆盖桌面、门框和人物边缘；被影子盖住的物体逐渐消失在纯黑里，整个画面只剩几条硬边光；影子随后像退潮一样缩回，退去处露出布局相似的新空间，但中央多出一个不该出现的物件，或原来的人已经不在。
```

### Lynch: Everyday Wrongness Creep

```text
转场/特效：房间没有突然变化，日常物件先一个接一个变得不对；咖啡颜色变成油亮黑色，墙上的画中人物眨眼，灯罩边缘像橡皮一样下垂，墙面软到留下指痕；颜色褪成旧照片黄，空气浮出16mm胶片颗粒，物件在观众还没完全察觉时换成另一个房间的物件，最后新房间已经成立。
```

### Fincher: Cold Corrosion Reveal

```text
转场/特效：所有材质温度下降，玻璃和金属先结出薄霜，霜覆盖颜色并让空间变成青灰低饱和；霜层下出现锈迹和酸蚀边缘，旧空间从边缘开始半透明地消失，新的墙、桌面和证据物像照片显影一样从模糊到清晰，冷白顶光保持稳定，空气里有可见冷雾。
```

### Nolan: Physical Space Fold

```text
转场/特效：远端地平线向上弯起，墙面和地面像有真实重量的巨大纸面沿一条铰链线折叠；家具牢牢附着在各自平面，重力在每个面上保持局部正常，人物站在中心作为尺度锚点；折叠的街道/走廊从头顶翻过来，空间最终闭合成新的方向，接缝消失，新空间以完整几何关系展开。
```

## 3. Single-Object Morphs

Use when only one prop or person transforms. Keep silhouette continuity unless the story needs identity instability.

### Face / Person Morph

```text
特效：人物脸部像隔着热水一样起波纹，五官边缘软化但表情方向保持一致；眉骨、下巴和脸型缓慢调整，皮肤色调、发型和衣料纹理跟随波纹改变，2秒后波纹停止，新人物的眼神和上一帧表情无缝接上。
```

### Weapon To Flower

```text
特效：金属表面先出现绿色氧化痕，枪管边缘长出细芽，枪身逐渐软化成花茎，枪管收缩成花苞；花苞在手心啪地绽开成红色花瓣，金属反光消失，花瓣上保留几滴露水。
```

### Photo Becomes Living Space

```text
特效：墙上照片里的画面先动起来，照片玻璃向外鼓起，像透明薄膜被内部顶住；照片中的手穿过玻璃，脚落到现实地面，照片背景逐渐变空白，镜头跟随人物从照片平面进入真实房间。
```

## 4. Stability Add-On

Add the meaning of this stability line when the user asks for a complex VFX transition, keeping it as positive phrasing inside A:

```text
整个变形过程连续流畅，物质变化有清晰起点、运动方向和终点，边缘过渡自然，变形速度均匀，新空间结构完整，光影方向随新空间稳定下来。
```

Use this as a finishing sentence after the actual process has been described. The visible process remains the main prompt.

