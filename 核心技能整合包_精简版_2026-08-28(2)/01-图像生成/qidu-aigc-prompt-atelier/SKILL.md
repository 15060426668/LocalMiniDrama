---
name: qidu-aigc-prompt-atelier
description: Use when the user wants to convert, refine, or style image/video generation prompts using the Qidu AIGC prompt handbook: tame GPT-style over-sharpening, avoid negative-prompt traps, apply soft filmic rendering, or build Nolan/Interstellar-inspired live-action cinematic prompt language.
---

# Qidu AIGC Prompt Atelier

This skill converts rough visual prompts, storyboard shots, and image-edit instructions into the Qidu handbook style.

## Use This Skill For

- Turning ordinary AIGC prompts into restrained filmic prompts
- Removing GPT image-engine problems such as over-sharpening, busy texture, and plastic AI faces
- Rewriting "do not X" instructions into positive visual targets
- Applying Qidu / Interstellar-style live-action cinematic language
- Creating prompt suffixes for soft 35mm / IMAX film texture
- Reworking existing image prompts while preserving composition, subject, lighting, and scene information

## Core Rules

1. Convert negative instructions into positive targets.
2. Prefer large clean color blocks, restrained detail, soft edges, and unified materials.
3. Avoid writing forbidden concepts directly in generation prompts when they may trigger the model.
4. Use contrast references: "like X, not like Y" when helpful.
5. For people, specify natural skin, imperfect hair, wet catchlights, restrained pores, and non-posed mid-action.
6. For emotion, describe micro-expression, breathing, gaze, and body tension instead of theatrical expressions.
7. Preserve layout and factual details when refining an existing image or storyboard shot.

## Quick Style Suffix

Use this when the user just needs a fast quality upgrade:

```text
画面风格要求：柔焦边缘，克制的细节表达，大色块优先，材质统一干净，避免堆砌细碎纹理，整体通透高级。参考电影摄影质感：浅景深柔光、自然胶片颗粒、Kodak Portra 400 色调，像一张精心打光的电影剧照，而不是高清数码照片。
```

For the Qidu / Interstellar visual charter, prefer:

```text
诺兰《星际穿越》电影质感，霍特玛掌镜，IMAX 65mm 胶片拍摄，柯达 Vision3 5219，有机胶片颗粒，高光自然晕染，柔和对比度，自然光与实用光主导，球面镜头浅景深，胶片化学调色，无数字锐化，电影剧照级画面。
```

## Workflow

1. Identify the prompt type:
   - text-to-image
   - image refine / redraw
   - video shot prompt
   - live-action character prompt
   - atmosphere / style suffix
2. Preserve the user's factual scene content first.
3. Add only style language that improves the requested output.
4. Replace vague bans with concrete positive targets.
5. If the output is for a video model, keep timing, camera, spatial relationships, subject action, sound, and restrictions explicit.
6. End with a compact "avoid" note only for human review; do not overstuff the generation prompt with forbidden words.

## References

- Read `references/gpt-image-control.md` for GPT image-engine control, suffixes, image refinement, and forbidden prompt traps.
- Read `references/qidu-cinematic-charter.md` for Qidu / Interstellar visual DNA, human realism, motion, emotion, and ready-made templates.
- Source document: `F:\剧本创作四步骤\提示词画风\AIGC提示词手册·七渡(1).html`
