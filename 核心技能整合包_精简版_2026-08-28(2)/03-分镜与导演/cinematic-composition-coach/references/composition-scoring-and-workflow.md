# Composition Scoring And Workflow

Use this file when producing output, not just training notes.

## Intake Checklist

Before designing or analyzing a shot, lock:

- story beat
- emotional target
- scene location and physical layout
- character positions and screen directions
- object positions
- camera starting point and ending point
- shot size and lens estimate
- foreground / midground / background
- light source direction and color temperature
- environment sound and motion if the space is alive
- cut-in and cut-out logic

If any item is unknown, infer conservatively and state the inference only outside the final prompt.

## Seven-Step Design Workflow

1. Narrative need: define what the shot must make the audience understand or feel.
2. Shot parameters: choose shot size, camera height, angle, focal length, aperture/depth, aspect ratio if needed.
3. Composition rules: pick 1-3 rules and state why.
4. Lighting: define source, direction, quality, contrast, falloff, practical lights.
5. Color: define palette, saturation, temperature contrast, symbolic anchors.
6. Motion: define actor movement, camera movement, background motion, object motion, and sound changes simultaneously.
7. Self-audit: score, find weak point, revise before final.

## Six-Dimension Scorecard

Score 0-10 each:

| Dimension | Weight | What To Check |
|---|---:|---|
| Visual narrative | 25% | Emotion, story information, relationship, power are clear. |
| Composition rules | 20% | Dominant geometry is readable and not accidental. |
| Shot language | 20% | Shot size, camera angle, lens, and depth fit the scene. |
| Light atmosphere | 15% | Light direction and quality create the right mood and remain plausible. |
| Spatial layers | 10% | Foreground, midground, background are distinct. |
| Style consistency | 10% | The shot belongs to the same world and visual grammar. |

Weighted score:

`total = narrative*0.25 + composition*0.20 + shot_language*0.20 + light*0.15 + layers*0.10 + style*0.10`

## Output: Film Case Analysis

```markdown
**案例名**

**叙事层**
- 情绪基调：
- 人物关系：
- 剧情节点：
- 叙事功能：

**视觉层**
- 景别：
- 机位：
- 构图法则：
- 光影：
- 色彩：
- 画面层次：

**语言层**
- 提示词参考：
- 关键词提取：
- AIGC 可见锚点：

**复刻与运用**
- 用这个手法的原因：
- 如何用：
- 适用场景：
- 风险与反例：

**沉淀条目**
- 可复用规则：
```

This template is mandatory for film-composition training output. A broad motif summary may appear only after the detailed case samples. If a previous answer only lists motifs without the three-layer breakdown, treat it as under-analyzed and revise.

## Output: SD / Seedance Shot Prompt

Keep the final prompt focused. Do not stuff theory names into the prompt if visible description is clearer.

Use:

```markdown
**STYLE LOCK**
...

**SPACE / POSITION LOCK**
...

**A Prompt**
Continuous shot paragraphs with exact camera, blocking, light, sound, and movement.

**E Timeline**
Time-coded action, dialogue, camera, light, sound, and background motion.

**Self-Audit**
...
```

Rules:

- write subject position before beauty language
- describe visible facts rather than "godlike composition"
- for known character assets, write "使用已确认人物资产卡外观与服饰" instead of re-describing clothes
- do not write unwanted items as negative wording inside the A prompt
- if a public location exists, include layered public ambience and bystander reactions
- movement logic is simultaneous: speech does not freeze background, props, camera, light, or other actors
- when shot duration is too long, split into multiple generated clips rather than compressing speech unnaturally

## Output: Training Update

When the user asks to train from a new case:

1. Add a case entry to `composition-case-library.md`.
2. Add a progress entry to `training-progress.md`.
3. Preserve the three-layer analysis fields: narrative layer, visual layer, language layer.
4. Extract 1-3 reusable rules.
5. Mark whether it is:
   - observed fact
   - inferred technique
   - user preference
   - AIGC prompt rule

## Self-Audit Questions

Before final answer:

- Can the image generator know where the camera is?
- Can it know who is in the foreground and who is behind?
- Does the camera see only what it physically can see?
- Are body directions and eye lines coherent?
- Is light direction consistent with the scene?
- Does the prompt preserve continuity from the previous shot only when the user wants continuity?
- Is the shot visually alive while someone speaks?
- Are sound layers tied to visible actions or plausible off-screen sources?
- Did I separate analysis from final prompt so the model does not receive confusing meta language?
