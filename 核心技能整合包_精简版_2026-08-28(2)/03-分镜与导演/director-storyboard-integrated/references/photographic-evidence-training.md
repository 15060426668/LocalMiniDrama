# Photographic Evidence Training Library

Use this file when the user asks for 画面质感训练, 实拍感训练, 摄影证据, 单帧真实度, AIGC真实摄影感, or wants training material for rain-night, hospital-room, corridor-depth, or close-up realism.

This is a training library, not a replacement for `visual-tone-texture.md`. Use it to strengthen the `摄影证据/实拍感` field in storyboard rows and the positive anchors in SD / video A blocks.

## 1. Seven-Dimension Single-Frame Realism Gate

Before writing or accepting a frame, answer all seven dimensions. A frame that cannot answer at least five is likely a clean AI poster rather than a filmed moment.

| Dimension | Required proof | Typical anchors |
|---|---|---|
| 摄影机物理证据 | camera height, distance, focal length, perspective distortion, aperture/DOF, shutter blur, lens artifact | 24mm edge stretch, 35mm eye-level, 85mm compression, f/1.4 shallow focus, ISO grain, motion blur, vignetting, chromatic aberration, lens breathing |
| 光源叙事证据 | every important light has a motivated source and falloff | window daylight, fluorescent tube, candle, phone screen, street lamp, car headlight, emergency lamp, neon tube, reflected wall light, puddle reflection, shadow edge |
| 物理材质证据 | each material has distinct roughness, reflection, transparency, or wear | skin pores, oil sheen, veins, fabric weave, leather cracks, peeling paint, tile gaps, wet asphalt, fingerprints on glass, brushed metal, rust, paper fiber, wax, aerosol dust |
| 三维空间证据 | frame has foreground, midground, background, depth, air, and occlusion | doorframe occlusion, foreground object, hallway depth, wall corner, mist, dust beam, parallax, background door line, depth-of-field falloff |
| 人物动态瞬间证据 | body physics and physiology show an unfinished action | foot impact, hand grip pressure, cloth inertia, eye focus landing, breath rise, facial muscle tension, sweat, hair movement, swallow, jaw tightening |
| 画面瑕疵证据 | imperfect captured surface prevents plastic perfection | stains, scratches, fingerprints, worn edges, sensor noise, film grain, soft corners, slight overexposure roll-off, color shift, micro camera drift |
| 跨帧连续性证据 | video sequence keeps physical constants stable | same light angle, same black level, same grain, stable skin tone, same wardrobe wrinkles, same prop dirt, same DOF logic, same flare behavior |

## 2. Beauty-Word Deletion Test

Delete every outcome word:

```text
photorealistic / cinematic / 电影级 / 高级质感 / 细腻画质 / 唯美光影 / 大片质感 / 史诗氛围
```

If the remaining text still lets the reader see a physical camera capturing a dramatic moment in a real 3D space, the frame passes. If the remaining text collapses into mood, it fails.

## 3. Standard Training Breakdown Fields

Use this field order for photographic evidence training:

```text
镜头 | 时长 | 景别/焦段 | 构图画面 | 机位与运镜 | 光影/色彩 | 画面基调/质感 | 实拍摄影证据 | 画面内容 | 运动生态/层级交互 | 声音设计 | 转场 | 可借机制
```

`实拍摄影证据` must explicitly list:

```text
摄影机 / 光源 / 材质 / 空间 / 人物瞬间 / 瑕疵 / 连续性
```

## 4. Layered Positive Prompt Stack

When converting to SD / Seedance, keep the structure positive-only unless the user explicitly asks for negative prompts.

```text
【镜头物理层】焦段、光圈、快门、运动模糊、镜头瑕疵、ISO、颗粒。
【光源实体层】主灯位置、实用光源种类、反光、阴影、光衰减。
【空间纵深层】前景遮挡、空气尘埃、远近分层、透视关系。
【材质细节层】皮肤、布料、地面、墙体、玻璃、金属、纸、蜡、水、灰尘的状态。
【人物动态层】肢体发力、衣料摆动、眼神落点、呼吸、微表情。
【画面瑕疵层】颗粒、暗角、指纹、划痕、磨边、轻微色偏、柔和边角。
【连续性约束】固定光源方向、统一黑位、统一肤色基准、统一材质老化和道具状态。
```

Failure boundaries are recorded in analysis/training, but SD output should translate them into wanted positive anchors. Example: instead of saying the wall must not be smooth, write `peeling plaster wall, water stains, chipped paint edge, uneven concrete texture`.

## 5. Scene Family A: Rain-Night Suspense

Core: wet surfaces, practical lamps, reflections, rain aerosol, lens moisture, and clothing weight make the frame feel photographed.

| # | Setup | Camera | Light | Material / space / human proof | Transfer template |
|---:|---|---|---|---|---|
| 1 | person hesitates outside residential entrance | 35mm, f/2.0, 160cm eye-level, slight handheld vertical jitter | street lamp at 45 degrees, 4200K cool-blue, puddle bounce | foreground doorframe covers 1/3 frame, soaked cotton coat, asphalt water film, glass door water streaks and fingerprints, foot presses into puddle, eyelashes hold droplets, ISO2500 grain | 雨夜入户门犹豫人物镜 |
| 2 | woman crosses empty road | 24mm, f/2.8, 30cm ground-level lateral track | street lamps plus car headlights, cool-blue and warm-yellow reflections | gravel foreground, wet asphalt mirror, rusted guardrail, rain jacket matte plastic, high heel splashes water, rain fog separates three layers, 35mm coarse grain | 雨夜马路广角低机位横移镜 |
| 3 | woman inside car looks out | 85mm, f/1.4, fixed close-up, focus on one eye | street lamp backlight outside wet car window, weak water bounce | misted window foreground, wet hair on cheek, skin pores filled with rainwater, vertical glass streaks, circular bokeh, ISO3600 noise | 车内雨夜长焦人物特写镜 |
| 4 | old commercial street after closing | 28mm, f/4, second-floor fixed high angle | neon shop signs reflected by rain, mixed cold/warm practicals | wet shop signs, large puddles, tiny walker under umbrella, multi-layer rain haze, wall stains, chromatic edge | 雨夜商业街俯拍远景镜 |
| 5 | hand gripping wet umbrella | 100mm macro, f/2.0, fixed | narrow street-lamp spill from eave | fingertip water drops in focus, rusted umbrella handle, concrete ledge stains, skin wrinkles, dripping water, dark noise | 雨夜手部微距特写镜 |
| 6 | man crosses apartment greenery | 40mm, f/2.2, slow push | cold outdoor street lamp plus warm stairwell window | rain-covered leaves foreground, muddy ground, wet back of coat, foot sinking into mud, moldy wall, parallax through trees | 小区绿化带雨夜推镜中景 |
| 7 | person stops before stairwell door | 50mm, f/1.8, handheld near shot | warm-white sensor lamp snaps on, wet stair reflection | worn concrete steps, wet trouser cuff, fogged glass door fingerprints, brief highlight roll-off, body pauses mid-step | 楼道台阶雨夜犹豫近景 |
| 8 | riverside dock in rain | 20mm, f/3.2, slow tilt | cold searchlight across river surface | warped wet wood planks, moss, raincoat folds filled with water, foot makes dock shift, river mist layers, lens droplet blur | 江边码头雨夜超广角镜 |
| 9 | motel sign reflected in puddle | 70mm, f/2.0, low fixed insert | red/blue sign reflection and passing car spill | puddle ripples, cigarette butt, oil film, chipped curb, reflection trembles when a foot passes, visible grain | 雨夜水坑霓虹反射特写镜 |
| 10 | umbrella silhouette in alley | 35mm, f/2.4, slow follow from behind | single back street lamp, side wall bounce | wet brick walls, trash-bag shine, umbrella rib silhouette, coat hem dripping, foreground pipe occlusion, rain haze | 雨夜巷道背影跟拍镜 |

## 6. Scene Family B: Sealed Hospital / Sickroom Low Light

Core: weak motivated medical light, plastic/metal/linen surfaces, institutional color, breathing bodies, and machine noise.

| # | Setup | Camera | Light | Material / space / human proof | Transfer template |
|---:|---|---|---|---|---|
| 1 | patient bed in old ward | 35mm, f/1.8, static mid shot | bedside monitor green-blue light plus weak fluorescent overhead | cracked wall paint, yellowed bed rail, linen wrinkles, IV tube reflection, patient chest rise, dust in monitor glow | 病房床边弱光中景 |
| 2 | hand beside IV needle | 100mm macro, f/2.0 | small monitor glow and corridor spill | translucent tape edge, skin veins, needle metal glint, cotton fibers, tiny air bubbles in tube, fingertip twitch | 输液手背微距特写 |
| 3 | empty bed after waking | 24mm, f/2.8, low wide | flickering ceiling tube | wrinkled sheets, pillow dent, chipped bed frame, floor scuffs, curtain edge sways, cold institutional green | 破旧病房醒来空床镜 |
| 4 | face under medical top light | 85mm, f/1.6, fixed portrait | hard overhead examination lamp | eye sockets shadowed, sweat on temple, blue veins, dry lips, hair stuck to skin, high ISO dark noise | 病房顶光人物压迫特写 |
| 5 | medicine tray insert | 90mm macro, f/2.2 | side fluorescent strip reflected on metal tray | scratched stainless steel, pill powder, paper label fiber, water droplet ring, latex glove edge | 医疗托盘证据特写 |
| 6 | curtain gap watching | 50mm, f/2.0, through foreground curtain | corridor light leaking through curtain slit | woven curtain texture, dust, bed rail silhouette, figure partially blocked, room depth through gap | 病房帘缝窥视镜 |
| 7 | monitor waveform in dark | 70mm, f/2.0, fixed | monitor self-light | glass screen fingerprints, scanline, green reflection on cheek, plastic shell scratches, waveform pulse | 监护仪光源特写 |
| 8 | old ward doorway | 28mm, f/3.2, slow push | cold corridor light and dim room interior | doorframe chipped paint, tile gaps, metal plate scratches, patient bed in background, air haze | 病房门口推镜 |
| 9 | nurse call button | 100mm macro, f/2.0 | lamp spill across plastic button | yellowed plastic, worn red symbol, thumb pressure turns skin pale, dust in button seam | 呼叫按钮手指特写 |
| 10 | fluorescent tube flickers over bed | 35mm, f/2.2, static with light change | visible tube light overhead | light flicker changes sheet shadow, wall water stains, bed wheel rust, body flinches to buzz | 病房荧光灯闪烁镜 |

## 7. Scene Family C: Narrow Corridor Depth

Core: perspective lines, foreground occlusion, repeated practical lights, worn walls/floors, dust beams, and controlled continuity.

| # | Setup | Camera | Light | Material / space / human proof | Transfer template |
|---:|---|---|---|---|---|
| 1 | empty office corridor, person walks to sealed door | 24mm, f/2.8, eye-level slow push, slight handheld horizontal jitter | continuous ceiling fluorescent tubes, 4800K | fire hydrant foreground, scratched plastic floor, yellow mold on latex wall, rusted metal doorframe, dust aerosol, coat swing with steps | 办公楼走廊纵深广角推镜 |
| 2 | person stops mid-corridor to listen | 35mm, f/1.8, fixed | overhead fluorescent downlight | sharp figure with blurred corridor, dented wall, worn metal handrail fingerprints, dust in light column, arm stops mid-swing | 走廊中段驻足中景 |
| 3 | distant closed door | 85mm, f/1.4, fixed compression | small emergency lamp above door | chipped wood door, scratched handle, thin door-crack light, long dust beam, circular lamp bokeh | 走廊尽头房门长焦特写 |
| 4 | overhead corridor from stair landing | 28mm, f/3.2, slow tilt down | repeated fluorescent strips, stairwell shadow | dirty floor footprints, faded fire sign, repair tape on wall, tiny walker below, coarse grain | 楼梯平台俯拍走廊远景 |
| 5 | hand on corridor handrail | 70mm, f/2.0, fixed close-up | vertical fluorescent reflection on rail | polished fingerprints on metal, new finger mark, scuffed floor reflection, dust column, color noise | 走廊扶手手部近景 |
| 6 | basement corridor retreat | 20mm, f/4.0, slow dolly back | bare bulbs in intervals, alternating light/dark | cracked concrete, leaking pipes, rust drops, heavy damp haze, foot disturbs dust, lens water speck | 地下室走廊超广角后退镜 |
| 7 | half-hidden walking figure through side fire door | 40mm, f/2.2, lateral move | cool corridor tube plus weak warm side-room light | worn fire door fabric, dusty tile gaps, doorframe occlusion, fabric compression at step, ISO3200 noise | 侧门框架横移走廊镜 |
| 8 | corridor tile floor insert | 90mm, f/1.6, macro slow push | fluorescent bar reflected on tile | yellowed tile, black grout dust, sand particles, lens breathing, reflection shimmer | 走廊地面瓷砖微距推镜 |
| 9 | power-out emergency corridor | 24mm, f/2.8, slow push | low green emergency lights only | large shadow fields, plastic floor fading into dark, metal doorframe glint, silhouette rim, ISO4000 color noise | 断电应急走廊纵深镜 |
| 10 | shoulder silhouette walking along wall | 60mm, f/2.0, slight handheld | one-sided fluorescent sidelight | half shoulder lit, half shadow, worn coat fabric, glue residue on wall, vertical dust beam, long tube flare | 走廊侧影分割光影近景 |

## 8. Scene Family D: Close Human Detail

Core: long lens/macro, shallow focus, local practical light, skin and cloth physiology, breath, touch, and imperfection.

| # | Setup | Camera | Light | Material / space / human proof | Transfer template |
|---:|---|---|---|---|---|
| 1 | single eye avoids looking forward | 100mm macro, f/1.4, fixed | desk lamp narrow warm beam at 45 degrees | iris in focus, eyelid tremble, red vessels, pores, hair strand foreground, dust in beam, ISO3600 color noise | 人物眼部微距长焦特写 |
| 2 | hands grip leather armrest | 135mm, f/2.0, fixed | cold dawn window strip | knuckle focus, palm dust in creases, nail hangnail, leather scratches, fingers press white, dust beam | 手部发力抓握长焦特写 |
| 3 | lips in phone light | 85mm, f/1.6, slight handheld | phone screen cold-blue close source | cracked lips, skin dryness, screen reflection strip, surrounding cheeks out of focus, ISO3200 noise | 手机光嘴唇局部特写 |
| 4 | throat swallow | 90mm, f/1.8, slow micro push | corridor fluorescent side top light | neck veins, fine hair, worn shirt collar, scratched necklace, throat rolls once, dust column | 脖颈吞咽长焦特写 |
| 5 | fingertips pinch old paper | 100mm macro, f/2.0, fixed | desk lamp warm side beam | paper fiber, fold stain, fingertip oil, nail wear, wood desk scratches, paper bends under pressure | 指尖捏纸微距特写 |
| 6 | sweat beads on forehead | 135mm, f/2.2, fixed | weak cool top light | sweat in pores, water bead highlight, hair stuck to forehead, wall blur, ISO high noise | 额头汗珠紧张特写 |
| 7 | ear listening by candle | 100mm macro, f/1.4, fixed | candle warm narrow source | ear skin texture, tiny hair, earring scratches, smoke aerosol, candle bokeh, heavy shadow | 蜡烛光耳廓微距特写 |
| 8 | arm scar turns into light | 85mm, f/1.8, slow lateral move | rainy window cool-blue bounce | scabbed scratch, arm hair, frayed sleeve, puddle bounce, mist in air, ISO3000 noise | 手臂伤口长焦微移特写 |
| 9 | jaw tightens in monitor light | 90mm, f/2.0, slight handheld | computer screen blue sidelight | jaw muscle line, stubble, compressed lip wrinkles, screen reflection on skin, dust beam | 下颌紧绷长焦特写 |
| 10 | finger taps wooden table | 100mm macro, f/1.6, fixed | low bedside lamp vertical warm beam | knuckle callus, table dents, pencil scratches, finger impact deformation, dust lit by lamp, circular bokeh | 指节敲击桌面微距特写 |

## 9. Training Deposit Protocol

For each new photographic evidence training sample, deposit five assets:

1. 可复用规则：physical formula only, no abstract beauty words.
2. 反例边界：record in training as failure signs; do not auto-copy as SD negatives.
3. 可迁移镜头模板：name the scene type and camera/light/material package.
4. SD / 视频正面词转译：turn proof layers into positive anchors.
5. 归档模块：rain-night realism, sealed ward low light, corridor depth realism, close-up realism, or a new scene family.

Acceptance line:

```text
删除所有美化词后，仅靠摄影机、光源、材质、空间、人物瞬间、瑕疵、连续性，仍能完整成像。
```
