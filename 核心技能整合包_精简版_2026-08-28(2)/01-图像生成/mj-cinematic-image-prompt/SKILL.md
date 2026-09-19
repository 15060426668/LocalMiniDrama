---
name: mj-cinematic-image-prompt
description: Use when the user asks to create, train, refine, or standardize Midjourney image prompts with cinematic detail, MJ生图提示词, 电影级生图, 精细化提示词, 场景拆解, 画面层次, 光影关系, 机位构图, 风格标准, or converting story/world/shot concepts into dense MJ-ready prompts.
---

# MJ Cinematic Image Prompt

This skill converts visual concepts into high-density scene descriptions and Midjourney prompts with film-level composition, spatial hierarchy, material detail, lighting logic, and style control.

## Required Read

Read `references/mj-prompt-standard.md` before producing a full prompt, training note, or reusable prompt template.

## Dedicated 2D House-Style Router

When the user asks for 章鱼P/章鱼噼画风, the unified 2D house style, 2D character look development, Chinese-animation/Japanese-animation shared art direction, or parameter-free MJ descriptions in that family, read `../mj-takopi-2d-house-style/SKILL.md` and let it own character rendering, linework, cel shading, color, texture, cultural adaptation, and final prompt shape. Use this general skill only to supply scene hierarchy or spatial construction that the dedicated profile does not already cover.

The dedicated profile's source-name-free and parameter-free contract overrides generic output fields for those tasks.

## Core Principle

Do not write a loose visual description. Build the prompt as a designed image:

1. Lock the image function: hook, atmosphere, story information, or asset reference.
2. Choose the camera first: viewpoint, shot size, lens feeling, depth, and frame ratio.
3. Build the scene by layers: foreground, subject zone, midground, background, ceiling/floor when relevant.
4. Define light sources and shadow behavior, not just mood words.
5. Specify materials, weathering, scale cues, color palette, and negative space.
6. End with a stable style and rendering finish. Add Midjourney parameters only when the user has provided or approved them, and keep avoid guidance outside the model-facing prompt.

## Workflow

1. Extract fixed facts from the user: subject, setting, style, era, mood, required objects, forbidden reveals.
2. If facts conflict, preserve the newest user decision.
3. If the user asks for "描述场景", "场景设定", "画面文案", or is training prompt density, produce a full scene-description draft first, not a short keyword prompt.
4. Produce a short breakdown when useful:
   - `画面目标`
   - `镜头与构图`
   - `空间层次`
   - `光影关系`
   - `材质与细节`
   - `MJ风险控制`
5. Then produce one complete MJ prompt in Chinese unless the user only asked for scene prose.
6. Do not add MJ parameters unless the user has provided or approved them for this task. If parameters are not locked, output pure prompt text only.
7. Write positive target language only. Do not add negative constraint phrases such as "不要/避免/no/without" in the generated prompt. Control undesired outcomes by specifying the desired medium, style, rendering engine, subject scope, and composition positively.
8. Respect prompt mode strictly:
   - `纯场景 / 场景 / 环境图 / 空间设定`: write only architecture, furniture, props, light, texture, atmosphere, and spatial composition.
   - `角色图 / 人物图 / 镜头图 / 分镜图`: include characters only when the user explicitly asks for them in that output.
   - Do not import protagonist actions from story context into a pure scene prompt.
9. Keep style separate from writing rules. Do not force the learned Ghost-Blade / Final Fantasy / UE5 style into every prompt. Use it only when the user requests that style or the current project has locked it.

## Scene Description Standard

When the user asks for a scene, write complete visual prose before prompt syntax:

1. Start from the overall spatial impression and camera feeling.
2. Move through ceiling/walls/floor/foreground/midground/background.
3. Describe material, aging, dampness, damage, texture, smell-implied traces, and scale cues.
4. Describe light as behavior: where it originates, what it touches, where it fails, and what it hides.
5. Keep the prose dense and precise. Do not collapse the scene into a few keyword phrases.
6. Do not introduce characters, body parts, plot actions, or extra story elements into pure scene prompts. A room can imply that someone may wake there through bed shape, bedding, objects, and light, but the prompt must stay environmental unless the user requests a character.

## MJ Prompt Constraint Rules

These rules are fixed:

- Output a single continuous prompt paragraph by default.
- Do not split into analysis sections unless the user asks for拆解.
- Start with the style field, then scene identity, then region-by-region spatial description.
- Move through the image naturally: overall space, main area, walls, floor, window, door, furniture, props, lighting, materials, atmosphere.
- Use positive target language only.
- Do not add negative constraint words.
- Do not add Midjourney parameters unless the user has provided or approved them.
- Do not add characters to pure scene prompts.
- Do not add plot actions to pure scene prompts.
- Do not add unrelated story reveals.
- Treat `画风` as a replaceable field, not as a permanent default.

## Prompt Field Order

Use this order for scene prompts:

1. `画风`: the requested style, rendering medium, texture, and art direction.
2. `场景身份`: what the space is.
3. `整体空间`: scale, layout, atmosphere, composition.
4. `主体区域`: the main visual area or room feature.
5. `区域推进`: walls, ceiling, floor, window, door, furniture, props.
6. `光影结构`: light source, direction, cold/warm relation, shadow behavior.
7. `材质细节`: fabric, wood, metal, glass, paper, dust, moisture, wear.
8. `整体氛围`: the final emotional and genre impression.

## Output Shape

For a finished MJ prompt, output:

```markdown
**拆解**
- 画面目标：
- 镜头与构图：
- 空间层次：
- 光影关系：
- 材质与细节：
- MJ风险控制：

**MJ提示词**
...

```

## Quality Bar

The prompt is not complete until it answers:

- What dominates the first read of the image?
- What does the viewer notice second and third?
- Where is the light coming from?
- What proves scale, depth, and texture?
- What should Midjourney avoid misreading?
- Which details must remain hidden for story suspense?
