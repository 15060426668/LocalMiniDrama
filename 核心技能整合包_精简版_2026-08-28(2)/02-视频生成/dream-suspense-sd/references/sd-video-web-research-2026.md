# SD Video Web Research 2026

Use this file after browsing current AI-video prompt guidance or when the user asks for self-iteration from online prompt material. This module distills current public guidance into positive-only SD / Seedance prompt execution.

## Research Anchors

- Runway Academy Prompting Guide: Gen-4.5 image-to-video guidance centers prompts on motion, camera work, and temporal progression.
- Runway Gen-4.5 Help: the model supports detailed camera choreography, intricate scene composition, precise event timing, and subtle atmospheric changes.
- Luma Dream Machine Camera Motion Guide: camera control names include Pan, Orbit, Crane, Move, Push In, and Pull Out, useful as explicit camera anchors.
- Luma Best Practices: visual reference, camera motion, extend/keyframes, and looping help stabilize image-to-video continuity.
- Kling VIDEO 3.0 User Guide: Multi-Shot understands scene coverage, shot changes, camera angles, shot-reverse-shot dialogue, cross-cut dialogue, and voice-over.
- Kling Image-to-Video Guide: the key formula is Subject + Movement for motion control in a still image.
- Kling Prompt Guide: cinematic prompts benefit from camera language, lighting, native audio dialogue, and multi-shot scripting.
- ByteDance Seedance official page: Seedance supports text-to-video and image-to-video, smooth motion, physical realism, native multi-shot storytelling, prompt following, and rich camera movement control.
- BytePlus Dreamina Seedance prompt guide: camera movement prompts can use standard camera movement terms directly.

## Round 1: Source-Backed Prompt Compiler

Current model guides converge on one practical structure:

```text
subject -> visible action -> setting -> camera language -> lighting -> atmosphere -> timing -> continuity anchors
```

For Dream SD A blocks, compile this into:

```text
camera layer -> subject/action layer -> scene motion layer -> light/color layer -> texture layer -> sound layer -> continuity layer
```

Use three motion lanes:

- Subject motion: character/object behavior, gesture, expression, contact, weight, breathing, gaze.
- Scene motion: dust, rain, smoke, curtain, reflection, shadow, props, environment response.
- Camera motion: locked, handheld, dolly, pan, truck, orbit, crane, push in, pull out, rack focus.

Image-to-video prompts focus on motion and transformation because the image already carries visual identity and composition. Text-to-video prompts carry both visual construction and movement.

## Round 2: Model-Specific Positive Strategy

### Runway Gen-4 / Gen-4.5

Use for detailed camera choreography, precise timing, subtle atmospheric changes, and cinematic scene construction.

Prompt style:

```text
medium close-up, 35mm lens, slow dolly in, the subject turns her head slightly, dust moves in the window light, cool fluorescent practical light, precise 2-second timing, stable exposure and same color grade
```

Strengths to exploit:

- complex sequenced instructions.
- detailed camera choreography.
- precise timing of events.
- subtle atmospheric changes.
- strong text-to-video and image-to-video control.

### Kling / 可灵

Use for physically readable subject action, multi-shot scripting, dialogue mouth-sync, and Chinese prompt readability.

Prompt style:

```text
中近景，35mm lens，低角度慢推，人物向镜头走来，脚掌真实接触地面，衣摆跟随步伐延迟摆动，冷白顶灯从右上方打出硬边阴影，口型同步短句台词，真实物理，电影感
```

Structure:

```text
subject + visible action + scene + camera language + lighting + atmosphere + optional dialogue timing
```

### Seedance / Dreamina

Use for storyboard-to-video, multi-shot narrative continuity, cinematic aesthetics, smooth action, text-to-video, image-to-video, and direct camera terminology.

Prompt style:

```text
widescreen cinematic shot, 21:9, low angle rear tracking shot, the character runs through a narrow reflective corridor, grounded foot contact, cloth and hair following with delayed inertia, fluorescent lights passing rhythmically overhead, camera keeps a stable rear distance, cold practical lighting, wet wall texture, temporal coherence and stable subject identity
```

Structure:

```text
camera/lens/framing + subject/action + scene/space + camera movement + lighting/color + texture/material + sound cue + timing + continuity anchors
```

### Luma Dream Machine / Ray

Use for camera-motion concepts, image-to-video extension, keyframe continuity, looping, character reference, and visual reference.

Useful camera anchors:

- `Pan Left / Pan Right`
- `Orbit Left / Orbit Right`
- `Crane Up / Crane Down`
- `Move Left / Right / Up / Down`
- `Push In / Pull Out`

Prompt style:

```text
the image comes alive with a slow push in, window curtain moving slightly, character breathing subtly, camera moves closer while preserving the same face and costume, ending frame holds on her eyes
```

### SVD / Stable Video Diffusion

Use for conservative image-to-video motion. Keep motion compact and clear.

Prompt style:

```text
subtle natural movement, eyes blinking once, hair moving lightly in air, candle flame flickering, stable subject identity, smooth frame-to-frame motion
```

Best use:

- short clips.
- still image animation.
- micro motion.
- environment movement.
- restrained camera.

### AnimateDiff / ComfyUI AnimateDiff

Use for local workflows, prompt scheduling, sliding context, controlled motion amount, and prompt travel.

Prompt style:

```text
low angle rear tracking shot, subject running, feet contacting ground, coat following with delayed inertia, corridor lights passing rhythmically, prompt travel keeps the same subject and corridor geometry across scheduled beats
```

Execution anchors:

- context window continuity.
- prompt scheduling for scene changes.
- motion amount controlled by scale/effect.
- consistent seed and overlap for temporal smoothness.

## Round 3: Quality Reinforcement

### One-Shot Rule

Each short A segment carries one main action and one auxiliary movement:

- main action: character runs, door opens, head turns, candle flickers, corridor stretches.
- auxiliary movement: camera pushes, light flickers, smoke drifts, cloth sways, focus shifts.

### Camera First

The first meaningful phrase in every A segment should be camera/lens/framing:

```text
low angle close-up, 24mm wide angle, handheld rear tracking...
medium close-up, 50mm lens, locked camera...
wide shot, 35mm lens, slow crane up...
```

### Physical Proof

Every visible action gets a physical proof:

- walking/running: foot contact, weight shift, heel-to-toe or push-off.
- head turn: eyes lead, neck rotates, hair follows with delay.
- cloth/hair: material weight, inertia, delayed motion, settling.
- water/fire/smoke: gravity, surface tension, heat rising, buoyancy, turbulence.
- impact: contact point, force direction, momentum transfer, settling.

### Expression Proof

Every emotional close-up gets muscle proof:

```text
eyes widening, pupils dilating, brows lifting, mouth parting, throat swallowing, fingertips tightening, shoulders holding breath
```

### Time Proof

Time effects name speed and visible micro-detail:

- natural speed: readable body mechanics.
- slow motion: hair, cloth, dust, droplets, blinking, breath.
- speed ramp: normal speed -> slowed peak -> accelerated exit.
- reverse motion: object returns to earlier position through visible backward movement.

### Positive Consistency Tail

Use a compact positive tail for complex shots:

```text
temporal coherence, stable subject identity, same face and clothing in every frame, stable geometry, straight architectural lines, natural physics, grounded foot contact, consistent lighting, stable exposure, same color grade, ease-in ease-out movement, continuous camera path
```

Chinese version:

```text
帧间运动连续，人物身份稳定，同一张脸与同一套服饰贯穿全段，建筑线条稳定，透视线平直，脚掌真实接触地面，光源方向稳定，曝光稳定，调色连续，镜头运动有缓入缓出。
```

## Online-Iteration Checklist

Before final SD output:

- camera layer appears first.
- subject motion, scene motion, and camera motion are separated.
- one main action is clear.
- physical proof is present.
- micro-expression muscle detail is present when emotion matters.
- transition has a continuity anchor.
- target-model phrasing is applied when named.
- positive consistency anchors appear in complex shots.
- final output remains positive-only.
