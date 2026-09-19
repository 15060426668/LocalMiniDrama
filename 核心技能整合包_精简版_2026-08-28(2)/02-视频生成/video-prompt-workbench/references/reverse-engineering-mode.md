# Video Reverse-Engineering Mode

Use this mode when the user uploads a video and asks to analyze, extract, reverse, restore, or generate a prompt from it.

## Core Principle

Treat the uploaded video as the sole source of truth. Reverse-engineering is not creative rewriting.

Do not invent:

- unseen subjects
- unseen scenes
- unseen actions
- unseen camera movements
- unseen style
- unseen emotion or story background
- precise brands, locations, ages, or materials that cannot be verified

## Visibility Rules

- Clearly visible information may be written directly.
- High-probability inference may be written conservatively.
- Unclear details should use neutral descriptions.
- If uncertain, mark it in Chinese analysis and keep it out of the English prompt.

Examples:

- Use `a young woman wearing a dark dress`, not a precise age/brand.
- Use `a modern car on a busy city street`, not a specific model/location unless visible.
- Use `a reflective tabletop`, not `marble with gold decoration` unless visible.

## Analysis Dimensions

Analyze the full video, not a single frame:

- 主体: type, count, appearance, placement, consistency
- 动作: direction, speed, range, rhythm, natural/mechanical/continuous/repeated
- 场景: indoor/outdoor, location type, foreground/midground/background, props
- 镜头: shot size, angle, camera movement, aspect, composition, depth of field
- 光线: source, direction, intensity, shadow/highlight/reflection
- 色彩: palette, warm/cool relation, saturation, contrast, grade
- 风格: real footage, mobile, cinematic, ad, documentary, animation, 3D/CG, game
- 时间变化: opening/mid/end, cuts, transition, loop, continuity
- 画面质量: clarity, stability, motion blur, compression, text/watermark/logo

## Positive Prompt Requirements

Use 100-220 English words. Include:

- subject
- action
- scene
- camera shot
- camera angle
- camera movement
- lighting
- color tone
- visual style
- motion rhythm
- consistency requirements

Add by video type:

- people: `consistent face, natural body movement, realistic hands`
- product: `stable product shape, accurate details, clean reflections`
- animal: `consistent animal anatomy, natural movement`
- landscape: `stable environment, natural environmental motion, atmospheric continuity`
- animation: `consistent character design, clean animation motion`

## Negative Prompt

Use:

```text
low quality, blurry, out of focus, flickering, jitter, frame skipping, unstable motion, distorted body, bad anatomy, extra limbs, deformed hands, inconsistent face, changing identity, warped objects, duplicated subject, unnatural motion, camera shake, overexposed, underexposed, noise, artifacts, text, watermark, logo
```

If the source video contains text, watermark, or logo, mention that in the analysis, but do not ask the model to recreate it unless the user explicitly requests that.

## Output Format

```markdown
【视频内容概述】

【反推准确性判断】
- 明确可见：
- 合理推断：
- 无法确认：

【深度分析】
- 主体：
- 动作：
- 场景：
- 镜头：
- 光线：
- 色彩：
- 风格：
- 时间变化：
- 画面质量：

【反推思路】
- 核心保留：
- 谨慎处理：
- 避免偏差：

【通用视频英文正向提示词】

【负向提示词】

【镜头与运动拆解】
- Camera shot:
- Camera angle:
- Camera movement:
- Subject motion:
- Environmental motion:
- Motion rhythm:

【推荐生成参数】
- aspect ratio:
- duration:
- fps:
- motion strength:
- guidance / creativity strength:
- style strength:
- seed:
- consistency priority:

【最终可复制版本】
Positive Prompt:
Negative Prompt:
Camera / Motion:
Suggested Settings:
```

## Final Self-Check

Before final output, verify:

- only source video content is used
- no invented details are added
- original video type and style are preserved
- subject, action, scene, camera, light, color, and rhythm are covered
- stability and consistency requirements are included
