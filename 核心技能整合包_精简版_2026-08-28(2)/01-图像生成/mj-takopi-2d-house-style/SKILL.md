---
name: mj-takopi-2d-house-style
description: >-
  Compile parameter-free Midjourney still-image descriptions for a unified hand-drawn 2D house style derived from the user's verified 章鱼P/章鱼噼 visual evidence. For every human character, compile detailed age-relative body construction, support and weight, face and eye grammar, hair masses, full line hierarchy and pressure behavior, broken/overlapped/retraced marks, matte fills, cel-shadow placement, clothing, hand/prop contact, motivated light response, and paper/capture texture. For scene concepts, live-action/2D composites, cinematic key frames, posters, or environment frames, also compile execution-complete image structure with aspect, shot size, camera position, foreground/midground/background, focal length, aperture, focus plane, motivated multi-source light, photographic evidence, and cross-medium binding. Use for 章鱼P画风, 章鱼噼画风, MJ生图, 2D统一画风, 国漫日漫统一定调, 角色设定图, 人物立绘, 表情设定, 场景概念图, 动画关键帧, 海报插画, 参考图画风提炼, or repairing generic glossy anime outputs. Return descriptive prompt prose only and omit all Midjourney parameters. Do not use for video timing, camera movement over time, storyboards, SD/Seedance A blocks, or final raster generation with another image tool.
---

# MJ Takopi 2D House Style

Build reusable Midjourney still-image descriptions from visible drawing evidence. Treat the source label as an internal retrieval key; model-facing text must describe the drawing rather than naming a work, artist, studio, or character.

## Required Reads

- Read `references/style-bible.md` for every task.
- Read `references/mj-description-contract.md` before producing a final MJ description.
- Read `references/character-performance.md` for any frame containing a person, mascot, hand, pose, gaze, expression, or group relationship.
- Read `references/detailed-character-description-contract.md` for every frame containing a human performance-bearing character; its detailed character fields are mandatory unless the user explicitly requests brevity.
- Read `references/detailed-scene-description-contract.md` for every scene concept, environment frame, cinematic key frame, spatial poster, photoreal plate, or 2D-character/live-action composite.
- Read `references/evidence-register.md` only when auditing provenance, resolving contradictory references, or expanding the house style.

Stop reading when the frozen moment, subject identities, cultural setting, composition, character construction, line hierarchy, cel-shadow behavior, light, color, background density, texture, and expression are executable.

## Ownership Boundary

This skill owns:

- the stable 2D house-style baseline for Midjourney still images;
- detailed character body construction, face/eye/hair grammar, pose, hands, feet, clothing, prop ownership, line system, fills, shadows, light response, and texture;
- execution-complete static scene composition, camera/lens description, depth architecture, motivated light, photographic evidence, and 2D/live-action binding;
- parameter-free Chinese MJ description prose;
- style continuity across character sheets, scene concepts, key frames, posters, and series look development.

This skill does not own:

- plot, shot order, seconds, camera paths, transitions, lip-sync schedules, or tail-frame continuity;
- SD/Seedance video prompt architecture;
- Midjourney flags, version tokens, aspect-ratio flags, style-reference flags, image weights, seeds, or negative parameters;
- actual image generation unless another explicitly invoked tool performs it.

## House-Style Default

Use this profile as the default still-image look-development route for the user's future 2D projects unless the user explicitly selects another style. Preserve the same drawing family across Chinese-animation and Japanese-animation settings. Change culture through architecture, clothing, props, signage, landscape, social behavior, and production context; do not change the house linework, face grammar, cel-shadow logic, texture hierarchy, or acting standard merely because the setting changes country.

Stable baseline:

```text
soft age-appropriate silhouette
-> hand-drawn charcoal contour with controlled pressure variation
-> large coherent hair masses
-> pale matte face with sparse features and large wet irises
-> restrained one-step cel shadow
-> localized cheek/under-eye hatching
-> simple but weighted clothing folds and hand contacts
-> painterly, materially denser environment
-> ordinary light that does not automatically imitate the character's emotion
-> faint paper and animation-photography texture
```

## Still-Image Workflow

1. Lock the asset: character sheet, relationship sheet, expression sheet, scene concept, key frame, poster, environment frame, prop sheet, or repair.
2. Assign every input image one role: identity, style evidence, composition, palette, environment, costume/prop, or edit target.
3. Freeze one drawable moment. Convert sequential action into pose, weight, gaze, cloth delay, hand contact, object state, and visible consequence.
4. Lock the culture layer separately from the drawing layer. State country/period, architecture, clothes, furniture, school or household objects, and legible social behavior.
5. Choose one primary rendering lane:
   - `clean key art`: clean white or simple graphic field, crisp silhouettes, promotional clarity;
   - `broadcast still`: restrained cel rendering, ordinary background, slight capture grain;
   - `lived-in scene`: high-angle or wide environment with dense ordinary objects and a clear subject island;
   - `intimate close-up`: face, eyelids, mouth, blush, hair shadow, breath, and one relationship cue;
   - `bright emotional peak`: large readable eyes or mouth, clean graphic accents, warm or saturated light;
   - `psychological pressure`: ordinary world retained, local eye/neck shadow, sparse hatching, compressed posture and space.
6. Choose one composition owner: character, relationship geometry, environment, object, or simple mascot. Do not let every element demand equal attention.
7. For every human character, complete `references/detailed-character-description-contract.md`: identity/age, body proportions, pose/support/weight, face, eyes, hair, line hierarchy and defects, matte fills, cel shadow, clothing, hands/feet, prop contact, light response, and surface texture.
8. For every scene-scale asset, complete `references/detailed-scene-description-contract.md`: aspect, shot size, camera position, subject scale, focal length, aperture, focus target, foreground/midground/background, light architecture, material/capture evidence, and hybrid binding when applicable.
9. Keep an owned or operated key prop inside the character composition unless the user requests an isolated prop sheet. Lock each hand, finger pressure, wrist route, support, and object angle.
10. Apply the house style in this order: age/body shape -> pose/support -> face/eyes -> hair masses -> line hierarchy -> fill/cel shadow -> clothing/prop contact -> motivated light -> environment paint -> finish texture.
11. Assemble one continuous positive description using `references/mj-description-contract.md`; preserve every approved character and scene fact inside the copy-ready paragraph.
12. Remove source names, parameters, negative prompt language, video grammar, and unsupported exact text.
13. Validate saved prompt text with `scripts/validate_mj_description.py`; use `--profile detailed-character`, `--profile detailed-scene`, or `--profile hybrid-scene` as appropriate.

## Reference Priority

```text
current user locks
-> identity/edit references
-> approved composition and moment
-> house-style baseline
-> culture and environment evidence
-> lane-specific variation
-> restrained inference
```

Reference images may contribute different layers. One image can own identity while another owns linework and a third owns composition. Never average conflicting faces, outfits, ages, or environments into a vague hybrid.

## Output Contract

Detailed character output is mandatory for every human character unless the user explicitly requests a concise result. A source label, `rough 2D line art`, `cute healing style`, or another adjective bundle never counts as character construction.

For character sheets, expression sheets, relationship stills, key art, and every scene containing a human character, return a compact character lock plus one self-contained copy-ready `MJ描述` paragraph. The final paragraph repeats every pixel-changing character fact.

```markdown
**人物执行锁**
人物身份与比例：...
姿势 / 支点 / 重心：...
脸型与五官：...
眼睛与表情：...
头发结构：...
线稿系统：...
平涂 / 阴影 / 色彩：...
服装 / 手脚 / 道具：...
光线响应与表面质感：...
```

For scene concepts, environment frames, cinematic key frames, spatial posters, and 2D/live-action composites, detailed scene output is also mandatory unless the user explicitly requests brevity. Return a compact scene execution lock followed by the character lock when a person is present, then one independent copy-ready paragraph containing both.

```markdown
**场景执行锁**
画幅与构图：...
机位与景别：...
焦段与景深：...
近景 / 中景 / 远景：...
光影结构：...
实拍材质与摄影证据：...
实拍融合：...

**人物执行锁**
人物身份与比例：...
姿势 / 支点 / 重心：...
脸型与五官：...
眼睛与表情：...
头发结构：...
线稿系统：...
平涂 / 阴影 / 色彩：...
服装 / 手脚 / 道具：...
光线响应与表面质感：...

**MJ描述**
...
```

Never answer a character or scene task with one sentence, a short generic paragraph, or style adjectives that omit execution facts. The user must not reconstruct the final prompt by merging the execution locks.

## IP-Free Translation Gate

Internal notes and evidence registers may use source labels. The final MJ description contains:

- only visible shape, proportion, line, shade, color, light, material, composition, expression, and texture;
- no title, franchise, studio, artist, director, production-company, or named-source style phrase;
- no `in the style of`, `inspired by`, `某某风`, or source-character names;
- no Midjourney flags beginning with `--`, no `::` weighting syntax, and no numeric style controls.

## Positive Description Gate

Write the target directly. Replace prohibitions with affirmative visual locks:

- glossy 3D drift -> `matte flat skin, broad hair masses, one-step cel shadows, hand-drawn contour variation`;
- generic anime drift -> `soft short jaw, sparse nose and mouth marks, large dark iris, uneven cheek hatching, contact-driven folds`;
- empty background -> `three readable depth planes, ordinary furniture and lived-in objects, material clusters, one protected subject island`;
- excessive cuteness -> `age-appropriate adult proportions, soft jaw, coherent wet iris, warm cheek hatching, relaxed support and restrained local light`;
- cultural drift -> describe the intended local architecture, clothes, furniture, writing system, and daily objects positively.

## Animation Handoff

For animation look development, produce a still-style checksum containing:

```text
character silhouette and proportions
face/eye/mouth grammar
hair mass and line hierarchy
baseline cel-shadow family
skin/hair/environment palette roles
background detail ratio
paper/capture finish
culture layer
approved deviations by emotional lane
```

Pass this checksum upstream to `animation-suspense-performance`. That skill owns motion and timing; this skill continues to own the appearance of all static reference frames.

## Validation

For a saved description:

```powershell
python scripts/validate_mj_description.py <prompt.txt>
python scripts/validate_mj_description.py <prompt.txt> --profile detailed-character
python scripts/validate_mj_description.py <prompt.txt> --profile detailed-scene
python scripts/validate_mj_description.py <prompt.txt> --profile hybrid-scene
```

Add `--forbidden-term` for any additional source, artist, studio, franchise, or character name present in the current request.

## Hard Rules

- Describe the style; never depend on the source name to produce it.
- Preserve one coherent drawing family across genres and cultures.
- For every human character, explicitly describe age/body proportions, pose/support/weight, face, eyelids/iris/catchlights, hair mass/clumps/edge strands, line tool/color/hierarchy/pressure/taper/breaks/overlaps/retracing, fill boundaries, one-step cel-shadow placement, clothing force folds, hands/feet, prop contact, motivated light response, and paper/capture finish.
- Never collapse a human character to one sentence, a source label, `rough 2D`, `cute`, `healing`, or another generic style phrase unless the user explicitly requests brevity.
- Keep character surfaces cleaner than backgrounds, skin matte, hair grouped, shadows graphic, and line width visibly human.
- Let emotion change pose, eyelids, mouth, hands, spacing, local hatching, and local color before replacing the entire style.
- Make group relationships readable from distance, height, occlusion, gaze, and hand/object ownership.
- Treat the mascot as a simple high-chroma silhouette against a richer human world.
- Use one dominant rendering lane per image and at most one local supporting lane.
- Freeze motion into one decisive state; remove timelines and camera moves.
- For every scene-scale asset, include explicit frame geometry, shot size, camera position, focal length, aperture/depth, focus target, foreground/midground/background, motivated light structure, exposure hierarchy, material/capture evidence, subject/prop action, and cross-medium evidence when applicable.
- Never collapse a scene-scale answer to one sentence or a generic short paragraph unless the user explicitly requests brevity.
- Output descriptive prose only. Never append Midjourney parameters.

