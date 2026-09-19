---
name: video-prompt-workbench
description: Use when the user asks to generate, reverse-engineer, analyze, or convert text/images/videos into prompts for general AI video models: 通用视频提示词, 视频反推提示词, 视频prompt, 图生视频, 文生视频, 视频参考生成, reference image/video to video, video analysis to prompt, camera motion prompt, negative prompt, suggested video settings.
---

# Video Prompt Workbench

This skill ports the user's Canvas Workbench agents into Codex: one mode for general video prompt generation, one mode for accurate video reverse-engineering.

## Required References

Read `references/generation-mode.md` when producing a prompt from text, an image, a reference video, or mixed requirements.

Read `references/reverse-engineering-mode.md` when the user uploads a video and asks to analyze, reverse, extract, or restore its prompt.

## Mode Selection

Choose one mode before writing:

- `Text to Video`: user gives only text and asks for a video prompt.
- `Image Analysis to Prompt`: user asks to analyze/describe/extract prompt from an image.
- `Image Reference to Video`: user says to use an uploaded image as the generation reference, make it move, preserve subject, or create video from it.
- `Video Analysis to Prompt`: user asks to analyze/describe/extract/reverse prompt from a video.
- `Video Reference to Video`: user says to use an uploaded video as motion/style reference and apply requested changes.
- `Mixed Reference + Text Requirement`: user provides references plus specific edits, style, action, or camera instructions.

If the material will be passed into a video model as a reference, do not replace it with a long visual description. Treat it as the primary visual/motion anchor and only add motion, camera, environment changes, style, and user-required edits.

If the user asks for reverse-engineering, treat the uploaded video as the sole source of truth.

## Output Policy

For generation mode, output:

1. `输入类型判断`
2. `用户意图判断`
3. `中文理解`
4. `通用视频英文正向提示词`
5. `负向提示词`
6. `镜头与运动提示`
7. `推荐参数`
8. `最终可复制版本`

For reverse-engineering mode, output:

1. `视频内容概述`
2. `反推准确性判断`
3. `深度分析`
4. `反推思路`
5. `通用视频英文正向提示词`
6. `负向提示词`
7. `镜头与运动拆解`
8. `推荐生成参数`
9. `最终可复制版本`

## Compatibility With Existing Skills

Use `dream-suspense-sd` instead when the user specifically asks for Seedance-style shot-by-shot prompts, A/E blocks, audio-synced storyboard prompts, continuity-locked cinematic clips, or lossless storyboard conversion.

Use this skill when the request is about general video model prompts, reference-use judgment, or prompt reverse-engineering from uploaded videos.
