# MJ Prompt Standard

## Prompt Density Standard

Use the user's long fantasy landscape sample as the density benchmark: a strong prompt must break the image into camera, sky/ceiling, ground/floor, subject, foreground, midground, background, light, atmosphere, material, and scale cues.

Do not rely on a pile of adjectives. Every adjective should attach to a visible object, light behavior, material surface, or composition function.

When the user asks for scene description rather than final MJ syntax, write in full descriptive prose. Follow the user's benchmark style: macro impression first, then layered sections, then light/material refinement. Do not answer with short prompt fragments.

Use region-by-region scene construction for complex environments. Divide the image into visual territories such as overall composition, upper frame/ceiling/sky, main wall or horizon, ground plane, foreground anchor, midground path, background depth, and light structure. Describe what each territory contains, how it connects directionally to the next territory, and how scale, texture, and lighting change across the frame.

Do not force every image into "core prop" language. If the user asks for a scene, the scene itself is the subject. Props should be described only as part of their region and spatial function.

## Fixed MJ Prompt Constraints

Use these constraints for all MJ prompt writing:

- Default to one continuous paragraph.
- Do not output breakdown sections unless requested.
- Keep the prompt as positive target description.
- Do not write negative constraints.
- Do not add MJ parameters without user approval.
- Do not add characters to pure scene prompts.
- Do not add character actions to pure scene prompts.
- Separate `画风` from scene rules. A style module is a replaceable opening field, not a fixed default.

## Style Field

Start prompts with a style field when style is known. Keep it modular:

```text
{画风与媒介}，{渲染质感}，{光影/材质方向}，{类型气质}
```

Examples:

- `暗色梦幻半厚涂幻想写实画风，电影级3DCG现代室内场景质感，最终幻想式精致但克制的美术设计，虚幻引擎5级材质与光影渲染`
- `写实电影摄影风格，冷色现代悬疑剧质感，自然光与室内实用光，克制低饱和调色`
- `日系动画背景美术，干净色块与柔和边缘，温暖黄昏光，生活化乡村场景`
- `黑暗幻想游戏概念设计，半厚涂笔触，潮湿材质，低位火光与冷蓝阴影`

## Required Breakdown Fields

### 画面目标

State what the image is for:

- retention hook
- story reveal
- character asset
- environmental concept art
- establishing shot
- close psychological horror shot

Also state what must remain hidden.

### 镜头与构图

Specify:

- viewpoint: high-angle, low-angle, overhead, floor-level, POV, surveillance-like, symmetrical, Dutch tilt
- shot size: extreme wide, wide, medium, close-up, detail shot
- lens feeling: 24mm wide, 35mm natural, 50mm restrained, 85mm compressed, macro detail
- composition logic: frame-within-frame, leading lines, negative space, vanishing point, occlusion, silhouette, off-center subject
- aspect ratio: cinematic wide, vertical poster, square concept, etc.

### 空间层次

Describe at least three layers:

- foreground: object, obstruction, wall edge, floor texture, hand, candle, doorframe, cliff, smoke
- subject zone: main person/object/building/room feature
- midground: route, furniture, secondary object, corridor, light path
- background: exit, wall text, skyline, window, mountains, ceiling, shadow mass

For interiors, always include floor and ceiling if they carry story information.

### 光影关系

Specify:

- main light source and direction
- secondary/practical light sources
- shadow density and shape
- highlight behavior
- color temperature contrast
- volumetric effect if present
- whether light reveals, conceals, divides, or traps the subject

Avoid generic "cinematic lighting" unless followed by concrete light behavior.

### 色彩与材质

Specify:

- dominant palette
- accent color
- surface materials: damp concrete, oxidized metal, old paint, frosted glass, wax, dust, fabric, skin, hair
- texture scale: rough, smooth, peeling, cracked, polished, soot-stained
- saturation and contrast level

### 叙事道具

Make key objects visible and functional:

- location of object
- scale
- contact with character/environment
- light interaction
- story meaning

For suspense scenes, the object should feel real and ordinary before it feels symbolic.

## MJ Prompt Assembly Order

Use this order unless the user requests another structure:

1. Main subject and scene identity
2. Camera and composition
3. Foreground / subject / midground / background
4. Light and atmosphere
5. Materials and micro-details
6. Style and rendering quality
7. Parameters

## Prompt Style Rules

- Prefer concrete nouns and visible relationships.
- Do not flood with unrelated styles.
- Use one primary style family and one supporting style family at most.
- Keep horror psychological, environmental, and spatial when requested.
- Do not introduce story reveals that the user has forbidden.
- When generating concept art for a film, include "film still", "production design concept", or "cinematic concept art" depending on target.

## Positive-Only Control

Write only what the image should contain and how it should look. Do not add negative constraint phrases inside the prompt.

Control failure cases through positive specification:

- medium/style: `3DCG cinematic concept art`, `Final Fantasy style`, `Unreal Engine 5 rendering quality`
- subject scope: `empty sealed room`, `single candle-lit concrete chamber`, `environment concept with no characters implied by omission`
- mood source: `psychological horror from architecture, rule text, darkness, and candlelight`
- material target: `damp concrete, rusted iron, peeling paint, wax residue`
- composition target: `region-by-region vertical oppressive composition`

## Ghost-Blade Fantasy 3DCG Hybrid Style

Use this module when the user mentions 鬼刀画风, 鬼刀式梦幻半厚涂, 最终幻想3DCG, UE5质感, 半厚涂加3DCG建模, or asks for this learned hybrid style.

### Style Thesis

Combine dreamy CG illustration with painterly semi-impasto edges, Final Fantasy-like elegant volume, and Unreal Engine material lighting used only as support. The image should feel like a high-end fantasy illustration / game cinematic key art, not a photoreal room render: refined, airy, luminous, romantic, slightly melancholic, and materially rich.

### General Style Block

```text
梦幻CG插画质感，半厚涂边缘与精修CG主体结合，最终幻想式唯美奇幻美术，虚幻引擎级材质与光影作为空间体积辅助，柔和逆光，冷蓝灰空气透视，局部浅金与青绿色高光，细腻体积光，漂浮尘粒与光斑，丝绸、金属、宝石、湿润材质形成高级材质对比，主体结构具有3D建模般的体积与空间，边缘和背景保留绘画笔触、雾化层次和梦幻留白，整体空灵、精致、浪漫、带轻微忧伤的幻想电影感
```

### Character Block

```text
角色具有最终幻想式唯美比例，五官精致但保留绘画柔度，眼睛清透有湿润高光，皮肤呈柔和半透明质感，鼻梁、唇峰、锁骨、肩颈以细腻散射光塑形；发丝轻薄飘散，局部发束有手绘般的虚化边缘；服饰带有幻想礼服、轻甲、机能外套或精致泳装结构，丝绸、薄纱、羽饰、金属片、宝石、链饰形成材质对比，整体优雅、克制、空灵
```

### Environment Block

```text
场景采用梦幻CG插画式空间设计，建筑、家具与自然环境具有优雅的3DCG体积感，远景以雾化层次和冷色空气透视拉开空间，中景保留清晰结构与装饰细节，前景用织物、金属、花瓣、水面、尘粒或光斑形成视觉锚点；空间不堆满写实杂物，而是用大块冷灰蓝、银白、浅金、淡青色建立高级感，再用局部宝石色或暖光点亮视觉中心
```

### Lighting Block

```text
柔和逆光与侧逆光为主，光源从画面上方或斜后方穿透空间，形成头发边缘光、肩颈轮廓光、金属高光和薄纱透光；暗部带有蓝灰、青灰、紫灰的空气层次；高光带轻微晕染，颗粒、雪点、尘埃、花瓣或水汽在光束中漂浮，营造梦幻电影感
```

### Material Block

```text
丝绸材质柔软流动，边缘带半透明光泽；金属材质锐利、冷亮、反射干净；宝石呈现青绿、湖蓝、银蓝或浅金色微光；皮肤光滑但不塑料，带柔和次表面散射；背景建筑和器物保留3DCG体积结构，边缘用半厚涂笔触弱化，形成建模与绘画融合的质感
```

### Brushwork Block

```text
主体与关键材质精修，边缘区域保留半厚涂笔刷痕迹；背景使用大色块概括，局部用刮擦感笔触、雾化笔触和轻微颗粒纹理处理；服装褶皱、羽饰、发丝、光斑、床品和窗帘用松动笔触制造流动感；整体不是照片级写实渲染，也不是平面插画，而是精修CG基础上的高级绘画化处理
```

### Dark Suspense Adaptation

Use for 《残烛》 or psychological horror settings:

```text
暗色梦幻CG插画质感，半厚涂边缘与精修3DCG空间结合，最终幻想式精致但克制的美术设计，虚幻引擎级潮湿材质与低位烛光作为辅助，冷蓝灰阴影，局部暖橙火光，空气中细微尘粒，墙面、织物、床品与地面保留绘画笔触和雾化层次，金属、玻璃与积水具备克制反射质感，整体空灵、压迫、精致、冷峻，像一帧高质量黑暗幻想游戏概念插画
```

### Avoid Photoreal Drift By Positive Style Lock

When this style becomes too realistic, strengthen the opening field with:

```text
梦幻CG插画质感，绘画化边缘，半厚涂笔触，精修CG主体，幻想游戏概念插画，柔化真实室内渲染感，空间以大色块和雾化层次组织
```

## Parameter Rule

Do not output Midjourney parameters by default. Only include parameters after the user provides or approves them for the task.

Never output a Midjourney version parameter such as `--v` unless the user explicitly names the target MJ version.

When the user asks for a pure scene or environment image, do not add characters, body parts, faces, hands, or implied protagonist presence unless the user requests them. Build the image from architecture, props, light, texture, and composition.

## Example Density Pattern

For a large fantasy landscape:

- lock high aerial viewpoint
- make sky the dominant upper-half force
- define extraordinary celestial phenomenon with color, texture, scale, and motion feel
- place city/kingdom on ground with architectural hierarchy
- add river/road/forest/mountain depth cues
- use foreground rock or cliff as frame and scale anchor
- specify side light, rim light, cloud edge glow, and material highlights

For a psychological horror room:

- lock whether the camera is subjective, floor-level, or surveillance-like
- identify the room geometry first
- use one strong foreground anchor
- place the survival object where the eye can find it instantly
- make the rule text visible through light or composition, but avoid too much readable wall text if MJ cannot render exact writing
- use practical light to carve the room into visible and invisible zones
- keep the horror in absence, spatial pressure, damp texture, sound-implied objects, and incomplete information
