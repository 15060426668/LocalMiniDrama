---
name: mj-xianxia-megastructure
description: "Create, critique, expand, or standardize Midjourney prompts for xianxia megastructure aesthetics: 巨物美学, 仙侠巨构, 天宫, 云海, 悬浮宫殿, 天上白玉京, 十二楼五城, 人物与场景尺度关系, tiny hanfu figures dwarfed by colossal celestial architecture, cinematic wide shots, and imaginative Chinese fantasy worldbuilding beyond generic palace-on-clouds imagery."
---

# MJ Xianxia Megastructure

Use this skill to turn a xianxia scene idea into a Midjourney-ready megastructure image prompt with strong scale logic, cinematic composition, and fresh celestial architecture.

## Required Reference Routing

- For a full prompt, prompt template, or prompt system, read `references/prompt-grammar.md`.
- When the user asks for more imagination, new visual directions, or a style bible, also read `references/megastructure-motifs.md`.
- When the user asks to imitate uploaded references, first analyze the image structure, then use the references to rebuild the logic rather than copying surface details.

## Core Rule

Build the image around a scale relationship, not around a decorative xianxia setting. The human figure is usually a scale marker, witness, or threshold-crossing subject. Keep faces secondary unless the user explicitly asks for character design.

## Workflow

1. Extract the user's locked inputs: dynasty flavor, mood, time of day, subject count, dominant object, forbidden elements, MJ version or aspect ratio if provided.
2. Choose one scale grammar:
   - `witness`: tiny figures gaze at an unreachable megastructure.
   - `threshold`: figures stand at a gate, window, bridge end, cliff edge, or moon door.
   - `traverse`: figures cross a bridge, corridor, stair, cloud road, or roof spine.
   - `underbelly`: camera looks beneath a floating city, palace hull, inverted roof, or suspended foundation.
   - `interior-vista`: huge interior frame opens to a larger impossible exterior.
   - `near-far inversion`: a foreground tree, roof, or wall is already huge, but the background object is larger.
   - `cosmic wall`: people face architecture on planetary, orbital, or horizon-scale magnitude.
3. Build a scale chain with at least four levels: human, touchable architecture or tree, city/palace mass, atmospheric or cosmic field.
4. Define the camera before adjectives: position, height, lens feeling, vanishing point, foreground frame, negative space, and aspect ratio.
5. Invent one non-generic megastructure behavior: cloud waterfall, suspended columns, carved mountain-wall palace, circular moon gate, inverted city, translucent jade foundation, roofline crossing the horizon, starfield inside architecture, hanging bridges, luminous seams, or terrace floating above a lower world.
6. Specify atmosphere as distance logic: mist density, cloud layers, backlight, silhouettes, occlusion, atmospheric perspective.
7. Output in Chinese by default, with one complete MJ prompt paragraph. Use English technical phrases inside the prompt when they help MJ obey scale, camera, or rendering.

## Output Shape

For analysis or teaching requests, output:

```markdown
**宸ㄧ墿閫昏緫**
- 浜虹墿涓庡昂搴︼細
- 鍦烘櫙鏋勯€狅細
- 闀滃ご涓庨€忚锛?- 鎯宠薄鍔涘閲忥細
- MJ 椋庨櫓鎺у埗锛?
**MJ 鎻愮ず璇?*
...
```

For direct prompt generation, output only:

```markdown
**MJ 鎻愮ず璇?*
...
```

## Prompt Rules

- Prefer `tiny ancient Chinese figures`, `humans dwarfed by architecture`, `monumental scale`, `foreground scale reference`, `vast negative space`, and `atmospheric perspective`.
- Keep people at 2%-8% of frame height unless the user asks for a closer character shot.
- Use `--ar 21:9` or `--ar 16:9` for cinematic giant scenes unless the user locks another ratio.
- Add `--style raw` when the user wants cleaner composition and fewer decorative hallucinations.
- Add negative controls only at the end, and keep them practical: `--no text, watermark, subtitle, logo, modern clothes, close up portrait`.
- Do not overfill the image with random floating temples. Use one dominant impossible structure, then supporting forms.
- Do not describe the image as merely "beautiful, epic, fantasy". Prove scale through objects, distances, occlusion, repetition, and human placement.

## Quality Bar

Before finalizing, check that the prompt answers:

- What is the first-read giant object?
- Where are the humans, and why do they reveal scale?
- What foreground object makes the space touchable?
- What vanishing line or frame shape organizes the shot?
- What detail makes this more imaginative than a normal cloud palace?
- What must be constrained so MJ does not turn it into portrait, anime wallpaper, or generic temple scenery?
