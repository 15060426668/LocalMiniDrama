---
name: cinematic-composition-coach
description: Dedicated composition training and case-library skill. Use only when the user explicitly asks to train, feed, archive, reverse-engineer, score, or reuse movie-level composition cases: 构图训练, 投喂电影构图, 构图案例库, 电影截图分析, 神级构图案例, 构图案例复刻, 构图技能沉淀. For ordinary storyboard work, shot design, 镜头画面怎么设计, 构图, 光影, lighting, camera, blocking, lens, movement, and sound logic, prefer `director-storyboard-integrated` instead.
---

# Cinematic Composition Coach

This skill turns film composition examples into reusable shot-design knowledge. Use it mainly to ingest user-fed movie frames, scene descriptions, or reference sequences and deposit them into a composition case library. Routine storyboard composition is handled by `..\director-storyboard-integrated\SKILL.md`.

## Required Reads

Always read `references/composition-training-manual.md` before using this skill.

Read `references/composition-scoring-and-workflow.md` when producing a shot plan, SD/Seedance prompt, or quality diagnosis.

Read `references/composition-case-library.md` when the user is feeding a film case, asking for reverse-engineering, or asking to reuse a previously learned composition pattern.

Read `references/researched-composition-expansion.md` when the user asks to search the web for best film compositions, wants new reference cases beyond the current library, or asks for higher-standard case breakdowns modeled on film criticism.

Read `references/five-director-composition-expansion.md` when the user asks for top-director composition, five-director storyboard skill training, director-level composition benchmarking, or broad web-researched composition systems related to Hitchcock, David Lynch, David Fincher, Christopher Nolan, or Quentin Tarantino.

Read `references/training-progress.md` before claiming a style, film, director, or case family has been trained.

For long-term SD/Seedance or storyboard work, use this skill only when a new composition case must be analyzed or deposited. For normal scene design, call `director-storyboard-integrated`.

## Core Principle

Composition is not decoration. Treat every frame as a narrative machine:

1. What information does the audience need now?
2. Which character, object, or absence owns the frame?
3. How do geometry, depth, light, color, lens, and motion force the viewer's eye?
4. Why is this shot better than a flatter or more obvious version?
5. How can this be reproduced in SD/Seedance without ambiguity?

## Workflow

1. Lock facts first: scene space, character positions, foreground/midground/background, visible light sources, camera height, angle, shot size, and screen direction.
2. Run the three-layer analysis:
   - Narrative layer: emotion, relationship, power, story information.
   - Visual layer: composition rule, lens, camera position, light, color, depth, movement.
   - Language layer: how to express it as storyboard fields or AIGC prompt text.
3. Choose 1-3 dominant composition tools. Do not stack every known rule.
4. Explain why this choice works, what it prevents, and where it should be used.
5. Translate into usable output:
   - Film analysis
   - Shot design
   - SD/Seedance prompt
   - Training note for the case library
6. Self-audit with the six weighted dimensions before finalizing.

## Mandatory Granularity

When the user feeds film-composition examples, do not answer with a coarse "composition motif summary" as the main output. Analyze each selected case at the level of a reusable training sample.

Every formal case analysis must include:

- `叙事层`: emotion tone, character relationship, plot node, narrative function.
- `视觉层`: shot size, camera position, composition rules, lighting, color, spatial layers.
- `语言层`: prompt sentence, keyword extraction, and visible AIGC anchors.
- `复刻方法`: why this method works, how to apply it, where to use it, what failure to avoid.

Only after the detailed case analyses may you add a short cross-case mother-pattern summary.

## Case Intake Protocol

When the user feeds a film frame, screenshot, or sequence, extract:

- source identity if known, but mark uncertainty if not verified
- scene function and emotional beat
- composition rule and geometry
- shot size, camera height, viewing angle, focal length estimate, depth of field
- blocking and spatial hierarchy
- foreground, midground, background layers
- light direction, light quality, contrast ratio, practical light sources
- color palette, saturation, temperature contrast, symbolic color anchors
- camera movement, edit entry/exit, sound or public-space ambience when relevant
- why it works
- how to reuse it in the user's current project
- AIGC prompt anchors and common failure risks
- one reusable knowledge entry for `composition-case-library.md`

If the user asks to "train" the skill with a case, update `references/composition-case-library.md` and `references/training-progress.md`.

## Output Formats

For a single composition analysis, use:

1. `叙事层`
   - 情绪基调
   - 人物关系
   - 剧情节点
   - 叙事功能
2. `视觉层`
   - 景别
   - 机位
   - 构图法则
   - 光影
   - 色彩
   - 画面层次
3. `语言层`
   - 提示词参考
   - 关键词提取
   - AIGC 可见锚点
4. `复刻与运用`
   - 用这个手法的原因
   - 如何用
   - 适用场景
   - 风险与反例
5. `沉淀条目`

For a shot / SD / Seedance output, keep it executable:

- define camera position and subject position before style
- include lens, shot size, depth, camera motion, light direction, color palette, sound layers, and action timing
- preserve character asset cards instead of re-describing outfits unless the user asks for new costume design
- avoid IP-risk style labels in final prompts when the user has asked for video-generation text; translate references into visual properties
- include a short self-audit only after the usable prompt

## Mandatory SD / Seedance Shot Composition Gate

For the user's `命运覆写` video prompt work, treat every time allocation and every camera/viewpoint change as a composition decision, not just an action beat.

Whenever producing SD / Seedance / image-to-video / text-to-video / storyboard timeline output, every shot or time segment must state:

- composition type
- narrative function
- foreground / midground / background
- subject frame share and screen position
- gaze vector and motion vector
- light-to-composition relationship

The A block must convert composition into visible facts. The E timeline must include a `构图功能` note for each time segment. The self-audit must check whether every cut, POV shift, lens/shot-size change, or subject handoff has a composition reason. If a shot has no explainable composition function, redesign it before delivery.

## Quality Bar

Every result must answer:

- Is the subject's screen position unambiguous?
- Is the camera physically possible?
- Does the composition serve the dramatic beat?
- Are foreground/midground/background layers clear?
- Are light direction and color temperature specified?
- Is movement continuous across cuts?
- Does the AIGC prompt describe visible facts rather than vague praise?

Do not claim a film, director, or composition family is fully learned until at least three substantial user-fed or validated cases are recorded in `training-progress.md`.
