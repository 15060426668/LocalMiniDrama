# General Video Prompt Generation Mode

Use this mode for text-to-video, image-to-video, reference-video-to-video, and mixed reference requirements.

## Input Use Judgment

Classify the input:

- `Text to Video`: text only.
- `Image Analysis to Prompt`: image is being analyzed into a full prompt.
- `Image Reference to Video`: image will be uploaded to the video model as visual reference.
- `Video Analysis to Prompt`: video is being analyzed into a full prompt.
- `Video Reference to Video`: video will be uploaded to the video model as motion/style reference.
- `Mixed Reference + Text Requirement`: reference material plus changes.

Judgment cues:

- Analysis: "分析", "描述画面", "提取提示词", "反推 prompt".
- Reference generation: "基于这张图生成视频", "让图中人物动起来", "保持参考图主体", "参考这个视频生成", "按照这个视频风格生成".
- Mixed: "分析并生成提示词", "参考这个并改成...".

## Handling Rules

### Text to Video

Complete subject, action, scene, camera, light, style, atmosphere, and dynamic details from the user's text.

### Image as Analysis Source

Extract subject, scene, composition, lighting, color, style, and turn them into a complete video prompt.

### Image as Generation Reference

Do not over-describe the existing image. Use reference-based language:

```text
Use the uploaded reference image as the primary visual reference. Preserve the subject identity, composition, outfit, facial features, style, and visual details. Add natural motion, camera movement, environmental motion, and the requested change. Maintain temporal consistency, stable subject identity, and coherent frames.
```

### Video as Analysis Source

Extract subject, action, shot, rhythm, lighting, color, style, and time progression.

### Video as Generation Reference

Do not fully restate the video. Use reference-based language:

```text
Use the uploaded reference video as the primary motion and style reference. Preserve the main subject, motion rhythm, camera movement, composition, lighting, and atmosphere. Apply only the requested changes. Maintain smooth motion, coherent frames, and temporal consistency.
```

## English Positive Prompt Requirements

Use 80-200 English words for generation mode. Include:

- subject
- action
- scene
- camera
- lighting
- style
- atmosphere
- dynamic details
- smooth motion
- temporal consistency
- stable subject identity
- coherent frames

## Negative Prompt

Use this base negative prompt unless the user requests positive-only prompts:

```text
low quality, blurry, flickering, jitter, unstable motion, distorted body, bad anatomy, extra limbs, deformed hands, inconsistent face, changing identity, warped objects, duplicated subject, unnatural motion, camera shake, overexposed, underexposed, noise, artifacts, text, watermark, logo
```

## Camera And Motion Block

Output:

- Camera movement:
- Subject motion:
- Environmental motion:
- Motion rhythm:

## Suggested Settings

Suggest when useful:

- aspect ratio
- duration
- fps
- motion strength
- reference strength if applicable
- guidance / creativity strength
- seed fixed or not
- consistency priority

Do not invent platform-specific parameter names unless the user names a platform.
