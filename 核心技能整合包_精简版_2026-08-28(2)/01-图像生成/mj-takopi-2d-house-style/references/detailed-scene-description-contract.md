# Detailed Scene Description Contract

Use this contract for every scene concept, environment frame, cinematic key frame, poster with a spatial setting, photoreal plate, or 2D-character/live-action composite. A scene request defaults to detailed execution. Produce a short answer only when the user explicitly requests a concise prompt.

## Acceptance Principle

A scene description must be drawable as one still and photographically explainable. It must answer all of these questions:

```text
what is the frozen moment
where is the camera
what is the shot size
what frame geometry organizes the image
what occupies foreground, midground, and distance
where the subject sits in the frame and at what scale
which focal length creates that spatial relation
which aperture and focus plane control depth
where every important light comes from
which material and atmospheric facts prove the environment
how the subject supports weight and handles the prop
how the 2D drawing is constructed
how the 2D subject belongs to the real plate when the image is hybrid
```

One sentence, a generic mood paragraph, or a list of style adjectives does not satisfy a scene request.

## Mandatory Scene Lock

Lock these facts before writing the copy-ready paragraph:

```text
asset and frozen moment:
aspect and frame orientation:
country / region / era / time / weather:
camera side, height, distance, angle, and horizon:
shot size and subject scale:
focal length and lens character:
aperture, depth of field, and exact focus target:
shutter / ISO / capture behavior when rain, motion, low light, or grain matters:
foreground framing and occlusion:
midground subject zone and clean silhouette field:
background scale, atmosphere, and destination of the eye:
primary visual read / secondary read / negative space:
key light source, direction, hardness, color, and exposure ownership:
fill or environmental bounce:
backlight / edge light when present:
negative fill and shadow framing:
practical lights and reflective relays:
palette roles and value hierarchy:
real materials, weather response, imperfections, and capture evidence:
subject count, identity, age, pose, support, gaze, hands, prop, and frozen consequence:
shape, face, hair, line hierarchy, fill, cel shadow, local hatching, and paper/capture texture:
cross-medium contact, occlusion, shadow, reflection, parallax, atmosphere, and color spill when hybrid:
```

Numeric photography choices are descriptive image facts, not Midjourney flags. Preserve user-supplied values. When values are absent, select them from the intended subject scale and depth design rather than adding random specifications.

## Depth Architecture

Write all three planes as concrete object maps:

- `foreground`: name the closest framing objects, their scale, focus state, edge position, and whether they occlude only the border or a deliberate subject fragment.
- `midground`: place the main subject, support surface, owned prop, interaction space, and the clean value field that keeps the silhouette readable.
- `background`: establish geography, architecture, people, weather, scale cues, atmospheric perspective, and the final eye destination.

For mask-friendly subjects, keep the full subject and owned prop inside one readable midground depth band. Concentrate incidental foreground occlusion near frame edges and place a simple contrasting value field behind the subject. Describe this positively as the existing composition.

## Camera And Optics

Scene descriptions state:

- frame orientation or aspect in prose;
- shot size;
- camera height, side, angle, and approximate distance when spatial immersion matters;
- one focal length or narrow focal range;
- aperture and resulting depth behavior;
- exact focus target;
- shutter, ISO, motion blur, compression, grain, halation, bloom, flare, or lens moisture only when they visibly change the still.

The focal length must agree with the composition. Use wider lenses for environmental inclusion and foreground scale, normal lenses for natural spatial presence, and longer lenses for layered compression or subject isolation. Aperture must agree with the required number of readable depth planes.

## Light Architecture

Do not replace light design with `cinematic lighting` or a color adjective. State the visible structure:

1. `key`: source, direction, size/hardness, color family, and which planes it exposes;
2. `fill/bounce`: sky, water, wall, foliage, floor, or interior relay and its lower intensity;
3. `back/edge`: source and the exact contour, rain, hair, prop, or architecture it separates;
4. `negative fill`: eave, tree, wall, pillar, umbrella, interior darkness, or camera-side blocker that shapes contrast;
5. `practical`: lamp, window, sign, candle, screen, vehicle, or reflected source with a physically limited pool;
6. `reflection chain`: how wet stone, water, glass, lacquer, metal, cloth, skin, and paint respond differently;
7. `exposure hierarchy`: deepest readable dark, protected skin/subject midtone, controlled highlight, and atmospheric falloff;
8. `palette ownership`: environment base, subject colors, shadow bias, motivated warm/cool relation, and one restrained accent.

Ordinary daylight, overcast rain, warm interiors, sunset, night, and psychological pressure each require different source logic. Preserve ordinary believable light when the desired emotion is cute, warm, healing, lonely, or restrained; emotion changes local pose, gaze, color, and contrast before it changes the weather into spectacle.

## Subject And Prop Performance

Keep the key prop inside the character description unless the user explicitly requests an isolated prop sheet. Write:

```text
support surface and weight
pelvis / spine / shoulder relation
head and gaze target
which hand owns which part of the prop
finger pressure and wrist route
feet or seated support
cloth and hair residue
one visible consequence frozen after the action
```

At midground scale, prioritize silhouette, support, hands, prop angle, face readability, and contact over tiny costume decoration.

## 2D Drawing Lock

Never substitute a source label or `rough 2D style` for drawing construction. State:

- adult or age-appropriate body proportions and silhouette;
- head, jaw, cheeks, eye opening, iris, catchlight, nose, mouth, and cheek marks;
- hair outer mass, major clumps, sparse edge strands, and highlight family;
- outer contour weight, inner line weight, pressure variation, broken lines, overlaps, retracing, unclosed turns, and local boil;
- matte fill boundaries and their controlled hand offset;
- one-step cel-shadow family tied to the motivated light;
- local hatching locations and emotional function;
- paper, scan, animation-camera, or broadcast grain finish.

Cute, healing, or warm adult characters keep adult height, shoulders, neck, hands, posture, and clothing weight. Soft faces, coherent wet irises, cheek hatching, a quiet smile, relaxed support, and warm local light carry cuteness without making the character a child.

## Photoreal Plate And Hybrid Binding

When the environment is live action and the subject is 2D, describe both layers independently and then their shared evidence:

```text
real plate: horizon, lens, exposure, depth, material irregularity, weather, capture noise, NPC routes
2D subject: identity, proportions, line, fill, cel shadow, paper/capture texture
shared proof: support contact, dynamic cast shadow, foreground/background occlusion, rain or particles on both sides, correct reflection, perspective, parallax, focus-plane relation, environmental color spill
```

The 2D character remains visibly drawn. Spatial membership comes from contact and depth evidence, not a luminous outline.

## Output Form

For scene tasks, return:

```markdown
**执行锁**
画幅与构图：...
机位与景别：...
焦段与景深：...
近景 / 中景 / 远景：...
光影结构：...
人物与道具：...
二维画风：...
实拍融合：...

**MJ描述**
one continuous parameter-free Chinese paragraph
```

The execution lock is concise but complete. The MJ paragraph repeats every pixel-changing fact needed for independent copy use. Do not make the user reconstruct the prompt from the breakdown.

## Hard Failure Gate

Rewrite before delivery when any of these is true:

- the scene answer is one sentence or a short generic paragraph without explicit detail;
- foreground, midground, or background is missing;
- subject position, scale, or silhouette field is unclear;
- shot size, camera position, focal length, aperture, depth behavior, or focus target is missing;
- lighting is only an adjective and does not identify key, fill/bounce, edge or negative fill, practicals, material response, and exposure hierarchy as relevant;
- environment realism depends only on `photorealistic` without lens, material, weather, imperfection, and capture evidence;
- character style depends on a source name or `rough line art` without face, hair, contour hierarchy, line defects, fill, cel shadow, hatching, and texture;
- hands, support, weight, gaze, or prop ownership is abstract;
- a 2D subject in a real plate lacks contact, shadow, occlusion, atmosphere, reflection/parallax, or shared light evidence;
- the final MJ paragraph omits facts that appeared only in the execution lock.

Validate saved scene descriptions with:

```powershell
python scripts/validate_mj_description.py <prompt.txt> --profile detailed-scene
python scripts/validate_mj_description.py <prompt.txt> --profile hybrid-scene
```
