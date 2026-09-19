---
name: psychological-anime-imagegen
description: "Generate or edit static raster images with a hand-drawn psychological childhood-anime look derived from user-supplied visual references: rounded child proportions, slightly uneven fine linework, restrained cel shading, ordinary daylight contrasted with emotionally dense close-ups, group-pressure composition, and bright simple mascot forms. Use for 单张图片生成, 静态关键帧, 人物立绘, 场景概念图, 参考图画风迁移, 校园日常, 儿童关系压迫, 心理近景, or requests to analyze supplied images and iteratively generate still-image variants. Call the image-generation tool by default. Do not use for storyboards, shot timing, camera movement over time, SD/Seedance video prompts, A/E blocks, or animation-sequence compilation."
---

# Psychological Anime Image Generation

Create or edit still images only. Keep this skill separate from director storyboarding and SD/Seedance video compilation.

## Required boundaries

1. Call the built-in image-generation tool by default after compiling the prompt. Return prompt text only when the user explicitly asks for prompt-only output.
2. Treat supplied images as style, identity, composition, palette, or edit references. Label each role before generating.
3. Keep every model-facing prompt free of IP titles, franchise names, director names, studio names, artist names, and named characters. Translate references into visible traits.
4. Keep video language outside this skill. Route seconds, beats, camera paths, transitions, lip-sync timing, A/E blocks, tail frames, and continuity buses to the relevant storyboard or video-prompt skill.
5. Keep depictions of children non-sexualized. Keep conflict and bullying non-graphic unless a policy-compliant user request clearly requires another treatment.
6. Preserve user-supplied identity and story facts. Style inference may refine rendering; it may not invent a different character, relationship, or event.

## Progressive reads

- Read [references/style-evidence.md](references/style-evidence.md) for every task using this house style or the bundled evidence images.
- Read [references/control-matrix.md](references/control-matrix.md) to select one rendering lane and compatible composition controls.
- Read [references/cinematic-foundations.md](references/cinematic-foundations.md) for scene, framing, spatial hierarchy, and frozen-story-moment design.
- Read [references/color-systems.md](references/color-systems.md) when palette, time of day, emotion, or color drift matters.
- Read [references/texture-systems.md](references/texture-systems.md) when linework, cel shading, paper grain, psychological hatching, or synthetic-looking output matters.
- Read [references/prompt-assembly.md](references/prompt-assembly.md) before generating or repairing an image.
- Read [references/evaluation.md](references/evaluation.md) for inspection and iteration.
- Read [references/examples.md](references/examples.md) only when a concrete prompt pattern helps.

## Input classification

Assign every image one role:

- `identity reference`: face, hair, body, clothing, or prop identity must remain stable.
- `style evidence`: line, shape, shading, color, texture, and emotional rendering only.
- `composition reference`: framing, depth, subject placement, or group geometry only.
- `edit target`: preserve the original image except for requested changes.
- `supporting reference`: environment, object, costume, or palette contribution.

When several images conflict, use this precedence:

```text
current user locks
-> edit target or identity reference
-> approved composition
-> majority style evidence
-> secondary palette or texture evidence
-> tasteful inference
```

## Style lanes

Choose one primary lane. Add at most one supporting lane.

- `DAYLIGHT-ORDINARY`: bright ordinary childhood life, rounded shapes, restrained cel shadows, natural greens and sky cyan, socially believable environments.
- `RELATIONAL-PRESSURE`: group geometry, unequal visual weight, blocked exits, foreground bodies, school objects, polite or playful expressions carrying social threat.
- `PSYCHO-CLOSE`: tight face or body-fragment framing, heavier eye shadows, sparse hatching, muted brown-green or grey-violet shadow color, compressed background, visible fatigue.
- `SURREAL-CONTRAST`: a simple high-chroma rounded mascot form placed against a more materially detailed human environment; clean silhouette and minimal facial marks.

Use `DAYLIGHT-ORDINARY + RELATIONAL-PRESSURE` for bullying or exclusion scenes. Use `DAYLIGHT-ORDINARY + PSYCHO-CLOSE` for emotional reaction images. Use `SURREAL-CONTRAST` only when the simple mascot or impossible object carries the frame.

## Static-image workflow

1. Lock the asset type, aspect ratio, subject identities, frozen narrative moment, and required output count.
2. Inspect all reference images and assign roles.
3. Choose one primary style lane and one composition grammar.
4. Build the frame in this order: story moment -> subject hierarchy -> environment -> composition -> character design -> linework -> shading -> color -> light -> material/air texture -> constraints.
5. Convert named references into descriptive execution language. Remove all names from the model payload.
6. Generate one image per requested asset or variant with the built-in image-generation tool.
7. Inspect the result for identity, group count, hand/prop ownership, composition, style lane, line density, palette, and unwanted video/IP leakage.
8. Repair the first failed layer only. Keep the remaining prompt stable and generate the next iteration.
9. For project-bound output, save the selected image in the workspace and report its path. For preview-only output, show it inline.

## Prompt contract

Use the user's language by default. Keep the prompt model-facing and concrete:

```text
Use case and asset type
Reference-image roles
Frozen story moment
Subjects and identity locks
Environment and spatial map
Composition and framing
Character shape language and expression
Linework and cel-shading behavior
Lighting and color script
Surface, paper, and optical texture
Exact invariants and exclusions
```

Static camera terms such as high angle, low angle, wide lens impression, close-up, depth, foreground, or focus are allowed. Time-based camera operations belong upstream.

## IP-free payload gate

Before calling image generation, verify that the model prompt contains:

- zero titles, franchise names, studios, artists, directors, or named characters;
- zero phrases such as `in the style of`, `inspired by <name>`, or `<name>-style`;
- only visible shape, line, shade, palette, texture, composition, and emotional evidence;
- zero storyboard/SD structures such as `BASE LOCK`, `A区块`, `第X秒`, `运镜`, `转场`, or `尾帧`.

Internal reference notes may record source provenance. Never copy provenance into the generation prompt.

## Iteration contract

Treat “training” as an in-task evidence and repair loop, not background model training:

```text
reference evidence
-> prompt hypothesis
-> generated still
-> visual inspection
-> first failed layer
-> one targeted prompt change
-> regenerated still
-> retain or reject
```

When network research is requested, use accessible public sources and record only verified visual-production facts in `references/style-evidence.md`. If network access fails, state that clearly and rely on user-supplied evidence without inventing research.

## Validation

For reusable prompt files, run:

```powershell
python scripts/validate_prompt.py --file <prompt.txt> --forbidden-term <user-named-source>
```

Add one `--forbidden-term` per named source, studio, artist, director, or character supplied during the task.

## Output discipline

- For direct generation: call the image tool, show the result, then report the final prompt and saved path when applicable.
- For prompt-only requests: return one copy-ready prompt plus up to two controlled variants when useful.
- Keep variants isolated: change one of composition, palette, line density, or psychological intensity at a time.
- Do not output a storyboard, video prompt, timeline, or shot list from this skill.
