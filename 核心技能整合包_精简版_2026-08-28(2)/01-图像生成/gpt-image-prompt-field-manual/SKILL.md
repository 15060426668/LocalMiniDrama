---
name: gpt-image-prompt-field-manual
description: Use when the user asks to learn, apply, optimize, rewrite, or diagnose GPT/DALL-E/Nano Banana style image-generation prompts using the 草帽小蔡 GPT 生图提示词手册 principles. This skill converts negative constraints into positive targets, adds cinematic texture base packs, controls over-sharpening/detail clutter/fragmented textures, preserves identity during image edits, and recommends two-step GPT base image plus Banana/Nano Banana refine workflows.
---

# GPT Image Prompt Field Manual

Use this skill for GPT-series image prompts, DALL-E prompts, Nano Banana/Banana 2 redraw prompts, and any user request like "按生图手册优化", "学习这个生图技能", "提示词别写不要", "画面太锐/太碎/太AI", or "保持人物不漂移".

## Core Rules

1. Rewrite every negative instruction into a positive visual target.
2. Favor concrete image outcomes over tag piles.
3. Add a stable cinematic texture base when the user wants premium/film-like images.
4. For edits/redraws, preserve identity, pose, composition, scene, color tone, and framing before changing texture.
5. For fragile visuals, use contrastive anchors: "like X, rather than Y".
6. When a model keeps failing, split the workflow: GPT creates layout/subject/story information; Banana/Nano Banana img2img refines texture and edges.

## Negative To Positive Reframe

Convert forbidden wording into affirmative visual goals:

- "不要过度锐化" -> "柔和边缘过渡，胶片柔光，模拟质感而非数码锐利"
- "不要堆砌细节" -> "克制细节，大色块优先，单一焦点，视觉层级分明"
- "不要 HDR / 假质感" -> "自然对比度，胶片柔光，统一材质，真实材质反应"
- "不要网红脸 / 塑料感" -> "真实皮肤纹理，自然不对称五官，柔和但保留身份特征"
- "不要背景塞满" -> "留白，主体突出，背景简洁，焦点层级清楚"

When the user explicitly asks for "不要..." wording, explain briefly that GPT-style image models often activate the forbidden concept, then provide the positive replacement.

## Cinematic Base Pack

Use these as optional prompt wrappers when the user wants film/premium texture.

Chinese prefix:

```text
电影摄影质感，胶片柔光，克制细节，大色块构图，材质统一，自然光主导，浅景深，胶片化学调色，模拟质感而非数码锐利，
```

English prefix:

```text
cinematic photograph, soft film-like aesthetic, restrained detail, large color shapes, unified material palette, natural light dominance, shallow depth of field, photochemical color grade, analog softness over digital sharpness,
```

Chinese universal tail:

```text
画面风格要求：柔焦边缘，克制的细节表达，大色块优先，材质统一干净，整体通透高级。参考电影摄影质感：浅景深柔光、自然胶片颗粒、Kodak Portra 400 色调，像一张精心打光的电影剧照，而不是高清数码照片。
```

English universal tail:

```text
Style: soft focus edges, restrained detail, large color blocks prioritized, unified clean material, overall translucent and premium. Cinematic reference: shallow depth of field, soft natural light, organic film grain, Kodak Portra 400 tones, like a carefully-lit film still rather than a high-resolution digital photo.
```

## Texture Control Pack

Use when the image is too sharp, noisy, busy, plastic, or AI-like.

```text
柔焦边缘，柔和边缘过渡，胶片柔光，高光自然晕染，化学冲印柔度，克制细节，大色块，留白，化繁为简，主体突出，单一焦点，视觉层级分明，统一材质，平滑表面，干净渲染，哑光质感，材质语言一致，弱化微观细节
```

For English:

```text
soft focus edges, gentle edge falloff, film-like softness, halation on highlights, photochemical softness, restrained detail, minimalist texture, large color blocks, negative space, graphic simplicity, hierarchy of focus, single focal point, unified material, smooth surfaces, clean rendering, matte finish, cohesive texture language, subdued micro-detail
```

Avoid putting these high-risk words into GPT prompts unless the user explicitly needs them as subject facts: 精细, 复杂, 繁复, 浓郁, HDR, 高细节, 8K锐利, hyper-detailed, intricate, ultra sharp, HDR photography. If the user asks for "8K", preserve it only when it means output polish; pair it with "film softness / restrained detail" to reduce over-sharpening.

## Contrastive Anchor

Use sparingly when the image style keeps drifting:

```text
画面应该像胶片电影剧照，而不是手机HDR照片。
像 Kodak Portra 400 拍摄的生活瞬间，而不是 iPhone 夜景模式。
像被精心打光的电影一帧，而不是高清壁纸。
像真实材质的 carefully-lit moment，而不是堆满细节的CG渲染图。
```

English:

```text
The image should look like a film-still cinematography frame, not a smartphone HDR photo. Like a Kodak Portra 400 captured moment, not an iPhone night-mode shot. Like a carefully-lit cinema frame, not a crisp digital wallpaper. Like a real-material photograph, not a detail-heavy CGI render.
```

## Image Reset / Redraw

For existing images that need texture improvement without identity drift:

Compact Chinese:

```text
保留这张图的构图、色调、主体一切信息不变。仅优化画面质感：柔焦边缘，克制细节，弱化碎纹理，整体更通透胶片化。像一张电影剧照，而不是高清数码照片。
```

Full Chinese:

```text
请完整保留这张图的人物、构图、场景、色调、主体动作与信息。不改变人物身份、五官、姿态与镜头。

仅对画面质感做优化：
- 边缘更柔和，消除数码锐利感
- 细节表达克制，不堆砌碎纹理
- 材质语言统一干净，哑光感
- 高光自然晕染，胶片柔光
- 整体更通透、更高级

参考：精心打光的电影剧照，而不是高清数码照片。保留必要的结构细节，但让画面更耐看，不刺眼，不嘈杂。
```

Identity add-on:

```text
人物的五官、脸型、发型、肤色必须和原图完全一致，这是同一个人，只是画面质感更柔和了。
```

## Nano Banana / Banana 2 Workflow

Use natural-language redraw instructions, not tag piles:

```text
请完整识别这张图里的所有信息：人物长相、姿态、表情、服装、配饰、场景、道具、光源方向、色彩基调、镜头景别与构图。

保持以上一切不变，只重绘画面的质感：让线条更柔和、边缘不锐利、材质更统一、细节不堆砌、整体更通透。

参考：一张精心打光的电影剧照，而不是高清数码照片。
```

If the user asks GPT to "call Banana 2", state the practical truth: prompts cannot make one image model call another during generation. Use a two-step workflow instead:

1. GPT generates the base image: layout, character, scene, narrative information.
2. Banana/Nano Banana img2img refines edges, texture, and cinematic softness.

## Output Pattern

When optimizing a prompt, respond with:

1. A concise diagnosis of the failure risk.
2. A rewritten positive prompt.
3. Optional style tail or identity add-on.
4. If needed, a split workflow recommendation.

For the user's ongoing video/storyboard prompts, keep their required style and continuity constraints, but apply this skill's positive-reframe and texture-control rules without weakening action clarity.
