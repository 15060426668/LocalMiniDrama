# Visual Tone And Image Texture

Use this file when the user mentions `画面基调`, `画面质感`, `影像质感`, `画质`, `视觉基调`, `风格质感`, `实拍感`, `摄影证据`, `真实摄影感`, `AIGC摄影真实感`, `每帧像摄影`, `光源证据`, `材质证据`, `镜头缺陷`, `空气层`, `胶片感`, `数字感`, `CG质感`, `厚涂`, `3DCG`, `写实`, `半写实`, `颗粒`, `锐度`, `柔焦`, `镜头质感`, `材质质感`, `胶片型号`, `Kodak`, `IMAX`, `65mm`, `35mm`, `16mm`, `黑位`, `LUT`, `bleach bypass`, `留银`, `Technicolor`, `特艺彩色`, or asks whether tone/texture is separate from lighting.

## 1. Boundary

Keep these fields separate:

```text
光影/色彩 = how the shot is lit and colored.
画面基调 = what emotional/genre world the image belongs to.
画面质感 = what capture/rendering surface the image feels like.
```

`光影/色彩` answers:

- light source.
- direction.
- brightness/exposure.
- contrast and light ratio.
- shadow share.
- color temperature and color cast.
- key/fill/rim/practical logic.
- shot-specific lighting change.

`画面基调` answers:

- suspense, dream, domestic unease, procedural coldness, fantasy, romance, violence, absurdity, melancholy, ritual, fairy-tale, documentary.
- realism/stylization level.
- cleanliness vs dirtiness.
- warm-safe, warm-trapped, cold-clinical, neon-surreal, muted-memory, high-contrast-noir, soft-dream, sharp-evidence.
- emotional density: restrained, oppressive, floating, feverish, elegant, raw, uncanny.

`画面质感` answers:

- medium: live-action film, digital cinema, 3DCG, game-engine cinematic, painterly semi-thick paint, anime/illustration, surveillance, phone video, documentary.
- rendering/capture: PBR material, ACES color management, film grain, digital sharpness, soft diffusion, bloom, halation, chromatic aberration, lens breathing, motion blur, compression, scanline, VHS, clean commercial, dirty handheld.
- material rendering: skin, cloth, glass, metal, wood, liquid, dust, smoke, wet wall, paper fiber, mirror reflection.
- image surface: clean, glossy, matte, damp, dusty, greasy, frosted, grainy, noisy, polished, tactile.
- suspense texture parameters: film stock family, grain strength, sharpness, black-level behavior, lens character, LUT/color-process label, surface state, and suspense detail elements.

## 2. Writing Order

Use this order when the field is required:

```text
genre/emotional tone -> realism/stylization degree -> medium/rendering type -> surface texture -> lens/image artifacts -> material rendering priorities -> consistency rule
```

Example:

```text
画面基调/质感：压抑悬疑的独居室内基调，现实空间里带轻微梦境异样；中低饱和、干净但不舒适，数字电影质感，暗部有细节但不脏；皮肤和布料保留柔和真实纹理，镜面与金属反光偏冷，轻微柔焦和极淡颗粒，整体不走复古胶片，保持克制、冷静、可触摸。
```

## 3. Style Families

Use these as parameter bundles, not labels.

### Clean Digital Suspense

- tone: cold, controlled, serious, evidence-driven.
- texture: clean digital cinema, sharp detail, low saturation, fine shadow detail.
- artifacts: minimal grain, controlled highlight, precise edges.
- best for: procedural, investigation, surveillance, system pressure.

### Dirty Domestic Unease

- tone: familiar but wrong, warm-trapped or gray-green domestic.
- texture: lived-in surfaces, fabric wrinkles, fingerprints, dust, slightly greasy kitchen or bedroom materials.
- artifacts: mild grain, soft corners, imperfect practical light.
- best for: family suspense, apartment/bedroom tension, ordinary horror.

### Dream Softness

- tone: floating, unstable, memory-like, seductive or uncanny.
- texture: soft diffusion, blooming highlights, shallow focus, edges slightly breathing.
- artifacts: haze, gentle halation, slow motion blur, color bleed.
- best for: dream, hallucination, false safety, memory.

### Mythic 3DCG / Game-Engine Cinema

- tone: grand, clean, stylized, heightened reality.
- texture: UE5-like real-time cinematic render, PBR materials, ACES color, polished surfaces, precise volumetric light.
- artifacts: clean high resolution, controlled bloom, detailed cloth/skin/metal/glass/liquid.
- best for: fantasy, epic interiors/exteriors, stylized heroine shots, magic artifacts.

### Painterly Semi-Thick Paint + 3DCG Volume

- tone: romantic, fantastical, elegant, slightly unreal.
- texture: painterly edges, semi-thick paint color layering, 3DCG volume and lighting, detailed but not photographic skin.
- artifacts: soft brush-like gradients, polished highlights, gentle rim separation.
- best for: fantasy character, dream room, stylized props, elegant mystery.

### Retro Film / Old Secret

- tone: memory, hidden past, old case, nostalgia with rot.
- texture: film grain, lower clarity in shadows, warm/green/brown color contamination.
- artifacts: halation, gate weave only if intentional, soft contrast roll-off.
- best for: flashback, old photo, family secret, decayed archive.

### Surveillance / Evidence Feed

- tone: detached, cold, institutional, non-human observation.
- texture: flat compression, low dynamic range, scanline/noise, timestamp-like framing only if needed.
- artifacts: jitter, frame delay, harsh digital edge.
- best for: CCTV, phone footage, screen evidence, unreliable record.

## 4. Suspense Tone Quick Table

Use one as the scene `画面基调`, then tune shot-level texture.

| Tone type | Core feeling | Texture direction | Best use |
|---|---|---|---|
| 雨夜封闭型 | trapped, wet, cold, no exit | wet surfaces, high-speed 35mm grain, blue-green shadow detail, dirty reflections | motel, highway, old apartment, exterior night |
| 梦境超现实型 | familiar but wrong, drifting logic | soft edges, bloom/halation, warm-to-cold mismatch, texture slippage | hallucination, dream layer, reality leak |
| 时间循环型 | fate, loneliness, mechanical return | retro-future surfaces, repeated object texture, faded photo or clean sterile contrast | time loop, recursive room, identity paradox |
| 冷硬推理型 | clinical, precise, system pressure | clean digital or fine 35mm grain, sharp evidence detail, cold black levels | investigation, police, institution, evidence |
| 黑色电影型 | smoke, fate, neon, moral shadow | high contrast, noir grain, warm brown or black-and-white blacks, vintage lens softness | bar, confession, betrayal, old city |
| 风格化冲突型 | ritualized rupture, stylized impact | saturated accent red, clean iconic grain, hard warm light | delayed confrontation, revenge mood, showdown pressure |
| 精神分裂型 | broken, subjective, unreliable | mixed stock, focus drift, jumpy texture, Polaroid/VHS/fragmented inserts | unreliable POV, memory fracture |
| 日常诡异型 | normal but wrong, daylight dread | bright hard sun or warm domestic surface, deep shadows, subtle vintage softness | suburb, diner, bedroom, ordinary horror |

## 5. Color And LUT Ownership

Keep this separate from lighting. Use it to describe the grade or color-processing family:

| Process | Use | Texture note |
|---|---|---|
| teal and orange grade | modern suspense, Nolan/Fincher-adjacent contrast | keep skin controlled; avoid candy saturation |
| noir contrast grade | black film / moral trap | high contrast, strong black shape, readable faces |
| faded vintage grade | old memory, flashback, unreliable past | lower saturation, softened contrast, aged paper feeling |
| bleach bypass grade / 留银 | grim crime, industrial pressure | low saturation, high contrast, silver-heavy blacks |
| technicolor grade / 特艺彩色 | Hitchcock/old Hollywood/Kill Bill stylization | rich reds, theatrical color, clean color separation |
| warm tungsten grade | bar, old room, motel, domestic trap | amber/brown warmth with shadow pressure |
| cool fluorescent grade | office, hospital, police, sterile system | green/cyan coldness, flat institutional discomfort |

Color ownership rule:

```text
主色不超过3个；阴影色、高光色、唯一高饱和强调色要各自属于明确物体或光源。
```

## 6. Film Stock / Grain / Black-Level Table

Use film stock labels only when they help tone and texture. They belong in `画面基调/质感`, not in lighting.

| Stock / process | Grain | Sharpness | Color / black behavior | Best use |
|---|---|---|---|---|
| IMAX 65mm / 70mm | ultra fine, almost invisible | extremely sharp | high dynamic range, solid deep blacks | architecture, epic rules, Nolan-like scale |
| 35mm Kodak Vision3 50D | very fine | high | daylight accuracy, clean cool detail | daylight realism, modern exterior |
| 35mm Kodak Vision3 200T | fine | high | tungsten warmth, rich but controlled color | interior night, warm practical spaces |
| 35mm Kodak Vision2/3 500T | medium to heavy | medium | low-light grain, blue/cyan night tendency | rain night, motel, dirty city |
| 16mm Kodak 500T | heavy | medium-low, soft | faded color, home-video unease | Lynch-like memory, home video, intimate dread |
| Kodak Tri-X black and white | heavy | medium | high-contrast black/white | noir, archive, hard memory |
| bleach bypass / 留银 | medium | high | low saturation, hard contrast, silver blacks | crime, industrial pressure, grim urban |
| Technicolor / 特艺彩色 | fine | medium | rich saturated primaries, strong reds | Hitchcock, old Hollywood, stylized violence |

Grain strength phrasing:

```text
ultra fine 65mm film grain, almost invisible
natural 35mm film grain, fine in highlights and heavier in shadows
heavy 35mm high speed film grain, visible throughout, gritty texture
heavy 16mm home video grain, soft focus and faded colors
heavy black and white Tri-X grain, high contrast
```

Black-level phrasing:

```text
deep crushed blacks with retained critical detail
shadows with blue-green tint, dark but readable
warm brown soft blacks
dirty green-black shadows, never pure black
milky faded blacks and washed-out shadow detail
```

## 7. Lens And Image Character

Lens character belongs in `画面基调/质感` when it changes image surface:

| Lens character | Texture effect | Best use |
|---|---|---|
| anamorphic lens flare | horizontal streaks, cinematic breadth | Nolan/Kubrick-like scale, night light, action |
| vintage anamorphic lens | soft edges, oval bokeh | 70s noir, bar, old city |
| sharp modern lens | edge-to-edge clarity, controlled distortion | Fincher/Nolan, evidence, architecture |
| vintage prime lens | soft focus, highlight halation | Lynch, old Hollywood, dream, memory |
| shallow depth image surface | isolated skin/prop detail, background softness | private fear, clue, voyeur close-up |
| deep focus image surface | whole-space readability | architecture, room horror, background threat |

## 8. Surface State And Suspense Detail Bank

Surface states:

| State | Keywords | Best use |
|---|---|---|
| wet | water sheen, rain streaks, wet asphalt reflections, droplets on glass | rain night, humid rooms, bathroom, street |
| worn | peeling paint, rusted metal, faded fabric, chipped porcelain | motel, old house, abandoned place |
| dirty | grime, soot, mud, cigarette ash, stained walls | dirty city, police, basement, evidence scene |
| cold/hard | concrete, brushed metal, frosted glass, ice, snow, polished marble | institutional, Nolan/FIncher, time agency |
| soft/warm | velvet, worn leather, wood paneling, wool, cigarette smoke | bar, memory, Lynch, old home |

Suspense detail elements:

```text
rain streaks in headlights; neon reflection in puddles; venetian blind shadows moving across a wall; swinging bare bulb shadow; breath fog on glass; thin light leaking through a door crack; mirror silhouette; endlessly turning fan or spinning top; windshield wipers moving back and forth; smoke visible in light beams; chipped door number; rusted doorknob; cracked old wallpaper; white wall blood trail; coffee ring stain; cigarette butts in an ashtray; flickering neon sign; lightning briefly revealing darkness.
```

Use only details that fit the space; do not sprinkle all of them.

## 9. One-Line Texture Template

Use this fill-in template when the user wants a direct prompt fragment:

```text
画面基调/质感：[悬疑子类基调]，[现实/梦境/风格化程度]，[胶片/数字/CG/监控/厚涂媒介]，[颗粒强度]，[锐度/柔焦]，[LUT/调色处理]，[黑位表现]，[镜头特性]，[表面状态和2-3个空间细节]，[材质渲染优先级]，[一致性规则]。
```

Example:

```text
画面基调/质感：雨夜封闭型悬疑，现实但带精神困局压迫感，35mm Kodak 500T高感夜戏质感，暗部粗颗粒明显、亮部颗粒细，中等锐度，bleach bypass低饱和高对比处理，阴影发蓝绿且保留脏细节，轻微手持雨夜镜头感，湿柏油反光、玻璃雨痕、掉漆门牌号，皮肤水膜和旧墙霉斑优先渲染，全场保持湿冷脏旧一致性。
```

## 10. Shot-Level Variation

A scene can have one visual-tone master, but each shot may vary:

- close-up: skin texture, eye highlight, hand surface, shallow focus behavior.
- wide shot: environment cleanliness/dirtiness, architectural texture, air density.
- insert: paper fiber, metal glint, liquid surface, screen texture, prop finish.
- dream transition: texture of the old space transforms into texture of the new space.
- dialogue: texture may sharpen as conflict becomes cruel, or soften as memory/lie takes over.

Every shot-level `画面基调/质感` should answer:

```text
What does this shot feel like as an image surface, and what texture must remain consistent or change?
```

## 11. Failure Boundaries

- Do not use `画面质感` to replace lighting. "电影感" is not a light source.
- Do not use `光影/色彩` to hide missing tone/texture. A 6500K key light does not tell us whether the image is clean digital, dirty domestic, retro film, or painterly CG.
- Do not write only "高级质感", "电影质感", "3D质感", "写实质感"; specify surface, medium, grain/sharpness, material priorities, and consistency.
- Do not mix too many surface languages: VHS + polished UE5 + oil painting + documentary phone video in one shot usually fights itself.
- Do not let style words override story readability. The viewer must still read character, space, object, and action.
- Do not over-grain, over-bloom, or over-sharpen unless the style specifically calls for it.
- Do not use negative-prompt wording inside positive storyboard or SD A fields. Turn risks into positive surface anchors.
- Negative prompt banks are optional downstream assets only. Use them only when the user explicitly asks for negative prompts; otherwise express texture control through positive anchors such as `natural skin texture`, `shadow detail retained`, `low saturation`, `physically motivated light`, `film-like grain`, and `stable material surfaces`.

## 12. SD Mapping

When converting to SD / Seedance:

- scene `画面基调/质感母版` -> `【画面基调与质感锁定】`.
- shot `画面基调/质感` -> A block `画面基调/质感`.
- `STYLE LOCK` holds broad rendering quality and medium safety.
- `主色板锁定` holds color ownership.
- `光影/色彩` holds light behavior.
- `画面基调/质感` holds image surface and visual mood.

## 13. Reusable Rule Deposit

Training type: 画面基调/画面质感专项

Training target: separate visual tone and image surface from lighting; make style and texture controllable without weakening shot-level light execution.

**可复用规则**

- Separate lighting physics from image tone and texture.
- Write tone/texture as a parameter bundle: genre tone, realism/stylization, medium, surface, artifacts, material priorities, consistency.
- Use quick tables for suspense sub-tone, LUT/process, film stock, grain, black level, lens character, and surface detail.
- Scene-level tone can unify the sequence, but shot-level tone/texture must still state what changes or stays consistent.
- SD output needs a dedicated tone/texture lock so STYLE LOCK does not become a vague quality slogan.

**反例边界**

- Do not write only "电影质感" or "高级质感".
- Do not let tone/texture replace light source, exposure, contrast, or shadow logic.
- Do not mix incompatible media surfaces without narrative reason.
- Do not over-process the image until performance, props, and space become unreadable.

**可迁移镜头模板**

- 模板名：画面基调/质感锁定模板
- 基调：genre/emotional tone.
- 风格化程度：realistic / semi-real / stylized / surreal.
- 媒介：live-action / digital cinema / 3DCG / painterly / surveillance / phone / documentary.
- 质感：grain, sharpness, diffusion, bloom, halation, noise, compression, polish, dirt.
- 材质优先级：skin, cloth, metal, glass, wood, liquid, paper, smoke, dust.
- 一致性：what must remain stable across shots.

**应写入哪个模块**

- 输出层 - 分镜表字段: 画面基调/质感.
- SD输出层 - 画面基调与质感锁定 + A区块逐镜头字段.

## 14. Photographic Evidence / Live-Action Frame Realism

Use this section when the target is AIGC short-film realism: every frame should look like a camera found a real physical moment, not like a clean generated poster.

Separate the three layers:

```text
光影/色彩：source, direction, exposure, contrast, shadow, color temperature.
画面基调/质感：genre tone, medium, grain, black level, lens character, material rendering style.
摄影证据/实拍感：camera proof, motivated light proof, material proof, space proof, human moment, imperfection, continuity/post proof.
```

### Photographic Evidence Checklist

| Proof layer | Must answer | Useful positive anchors |
|---|---|---|
| camera evidence | where the camera physically is and what perspective it produces | 21:9 frame, floor-level camera, shoulder-height handheld, 35mm perspective, shallow depth of field, natural motion blur, soft corner falloff |
| light evidence | where the light comes from and how it falls | motivated practical light, visible fluorescent tube, candle source, side-back light, window spill, falloff across wall, shadow detail retained |
| material evidence | what surfaces prove physical reality | natural skin texture, pores, fabric weave, damp peeling wall, scuffed floor, rusted metal, fingerprints on glass, paper fiber, wax edge, dust in light beam |
| space evidence | how the frame has depth and air | foreground occlusion, midground subject, background door line, parallax, hallway depth, haze layer, visible corner, practical clutter |
| human moment | what unfinished action the camera caught | hand gripping, weight shifting, breath visible, hair stuck to cheek, cloth swinging, foot contacting floor, eyes refocusing, jaw tightening |
| imperfection evidence | what prevents sterile synthetic perfection | tiny stain, uneven paint, scratches, worn edges, slight asymmetry, smeared reflection, subtle grain, halation, lens breathing |
| continuity/post proof | what stays stable across shots | stable black level, consistent grain, consistent skin tone, same light direction, same material aging, same wardrobe texture |

Mandatory Chinese seven-dimension wording for training:

```text
摄影机物理证据 / 光源叙事证据 / 物理材质证据 / 三维空间证据 / 人物动态瞬间证据 / 画面瑕疵证据 / 跨帧连续性证据
```

For formal training rows, do not merge these into one vague sentence. `实拍摄影证据` must list all seven labels, even briefly.

Beauty-word deletion test:

```text
删除 photorealistic / cinematic / 电影级 / 高级质感 / 细腻画质 / 唯美光影 / 大片质感 / 史诗氛围 后，剩余文字仍能靠摄影机、光源、材质、空间、人物瞬间、瑕疵、连续性完整成像，才算合格。
```

### Positive Prompt Translation Bank

Use positive anchors instead of empty labels:

```text
photographed live-action frame, physically motivated light, visible practical light source, natural skin texture, imperfect pores, fabric weave, damp peeling paint, scratched metal, fingerprints on glass, scuffed floor, paper fiber, candle wax texture, dust floating in light beam, subtle film grain, stable black level, retained shadow detail, soft corner falloff, slight lens breathing, natural motion blur, foreground occlusion, layered hallway depth, real room clutter, tactile surfaces, consistent light direction
```

For Chinese storyboard rows:

```text
摄影证据/实拍感：21:9横幅构图，摄影机贴近真实地面高度，走廊荧光灯是主要动机光，光线从画面上方一格格落在地砖和脚背上；地砖有磨损、水迹和灰尘，墙面掉漆，玻璃门上有指纹，空气里有细微浮尘；人物脚掌落地、衣料摆动、手指抓紧道具，画面带自然运动模糊和轻微颗粒，全段保持同一光源方向和同一脏旧材质。
```

### Failure Boundaries

- Do not use only "photorealistic", "cinematic", "真实摄影感", or "高级质感". These are outcomes, not evidence.
- Do not make faces, fabric, walls, floors, glass, metal, and paper too clean unless sterility is the story point.
- Do not use unmotivated rim lights, random beauty highlights, or floating glow when the space has no source.
- Do not leave backgrounds empty. Real photographed frames have depth, corners, surfaces, clutter, air, or absence with a reason.
- Do not forget the human action moment. A real frame usually catches a body mid-breath, mid-step, mid-grip, mid-turn, or mid-hesitation.
- Do not let SD or video prompt conversion drop camera, light, material, space, and human-moment evidence from the storyboard.

### Transferable Template

- 模板名：摄影证据/实拍感锁定模板
- 摄影机证据：aspect ratio, camera height, focal family, perspective, DOF, motion blur, lens behavior.
- 光源证据：motivated source, source position, falloff, shadow texture, highlight/specular behavior.
- 材质证据：skin, cloth, wall, floor, glass, metal, paper, liquid, dust/smoke, wax, prop surface.
- 空间证据：foreground/midground/background, occlusion, scale, air volume, depth, background behavior.
- 人物瞬间：body weight, gaze route, facial micro-change, hand/foot contact, cloth/hair movement.
- 瑕疵证据：stains, scratches, fingerprints, worn edges, asymmetry, grain, halation, soft corners.
- 连续性：same grade, same black level, same light direction, same material aging, same wardrobe/prop state.
