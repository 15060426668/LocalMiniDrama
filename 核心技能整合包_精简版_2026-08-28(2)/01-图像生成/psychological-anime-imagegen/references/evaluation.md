# Evaluation and Iteration

Inspect every generated still before delivery.

## Quality rubric

Score 1-5:

| Dimension | 5/5 means |
|---|---|
| Frozen story moment | One action state and one consequence are immediately readable. |
| Identity fidelity | Face, hair, clothing, body proportion, and distinctive props match their assigned references. |
| Subject count | Every required person or mascot appears exactly once with a clear role. |
| Social geometry | Distance, enclosure, exit ownership, gaze, and visual hierarchy support the relationship. |
| Character shape | Compact proportions, rounded faces, large dark irises, and hair silhouettes remain coherent. |
| Linework | Fine slightly uneven outlines and sparse interior marks read as hand-drawn. |
| Cel shading | One restrained shadow family supports form; psychological density remains localized. |
| Color script | Skin, hair, environment, source, shadow, and accent have distinct roles. |
| Environment | Road, school, classroom, home, or forest has readable geometry and ordinary objects. |
| Texture | Background paint, faint paper grain, bloom, and hatching follow the chosen lane. |
| Static-image clarity | The frame works as one still and contains no timeline-dependent instruction. |
| Payload hygiene | The prompt contains no IP names, source names, watermarks, or video-prompt structures. |

Acceptance target: every dimension at least 4.

## First-failure routing

| Visible failure | Repair layer |
|---|---|
| Wrong face or hair | Identity lock |
| Missing or duplicate child | Exact count and per-person role |
| Group looks randomly arranged | Social geometry and composition |
| Looks like generic modern anime | Shape language, line irregularity, flat hair masses, sparse facial detail |
| Looks too cute for the emotion | Eyelids, posture, hatching, object pressure, local shadow |
| Entire image is dark or muddy | Color localization and readable skin midtones |
| Looks like glossy 3D | Cel-shadow simplification, matte surfaces, line behavior |
| Background feels empty | Architecture, ordinary props, depth planes, routine social evidence |
| Mascot blends into humans | Clean high-chroma silhouette and lower detail density |
| Prompt includes a source name | IP-free payload gate and validator forbidden terms |
| Prompt reads like a video | Freeze the action and remove timing/camera-route language |

## Iteration protocol

1. Keep the user request, identity references, aspect ratio, and successful layers fixed.
2. Identify the first failed layer from the table.
3. Change one prompt layer.
4. Generate a new still.
5. Compare the same rubric dimensions.
6. Retain the change only when the target improves and no stable dimension drops below 4.

For several requested variants, generate each through a separate tool call and label the single changed layer.

## Forward-test set

1. Bright rural road with five laughing classmates and one isolated child; preserve ordinary daylight.
2. School corridor side profile with a simple pink mascot and an exhausted child.
3. Tight reaction close-up with hair across the eyes and localized pencil hatching.
4. Two children facing each other under a cyan sky, profile framing and restrained expressions.
5. Classroom crowd surrounding a central child with exact count and distinct reactions.
6. Clean character key art with simple cel shading and painterly foliage.
7. Repair a glossy 3D-looking result into matte hand-drawn cel animation.
8. Convert a five-second action description into one decisive frozen state.
9. Use several named references internally while producing a prompt with zero names.
10. Generate two variants that change only psychological intensity.

## Research update rule

Add external findings only when a reachable source provides a verifiable visual-production fact. Record URL, access date, fact, and prompt consequence. Do not add plot summaries, fan guesses, or unsupported production claims.
