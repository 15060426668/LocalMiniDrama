# Detailed Character Description Contract

Use this contract for every still containing a human performance-bearing character. It applies to character sheets, identity art, expression sheets, relationship stills, key art, scene concepts, cinematic key frames, posters, and 2D-character/live-action composites. Character description defaults to detailed execution. Produce a short character summary only when the user explicitly requests brevity.

## Acceptance Principle

`粗线稿2D人物`, `可爱治愈画风`, `日系手绘`, or a source label is never a complete character description. The copy-ready MJ paragraph must make the character independently drawable by spelling out:

```text
identity and age-relative body construction
pose, support, weight, line of action, and gaze
face, eyelids, iris, catchlights, brows, nose, mouth, cheeks, and local marks
hair silhouette, clumps, interior separations, edge strands, and highlight family
outer / overlap / facial / hair / clothing / hatch line hierarchy
line tool, color, pressure, taper, breaks, overlaps, retracing, unclosed turns, and local boil
skin, hair, garment, and prop color blocks
fill-edge behavior and one-step cel-shadow placement
clothing cut, gravity folds, compression folds, wear, and contact
hands, fingers, wrists, feet, and prop ownership
motivated light response and environmental color contamination
paper, scan, animation-camera, or broadcast finish
```

## Mandatory Character Lock

Lock these facts before writing prose:

```text
exact count, gender, adult/age band, role, and culture/era:
height, head-to-body relation, shoulder/hip relation, limb length, hand/foot scale:
ordinary posture baseline and current frozen action:
support surface, pelvis, spine, shoulders, elbows, knees, feet, and center of gravity:
gaze target, eyelid state, brow distance, breath/jaw cue, and mouth state:
head/cranium, jaw, cheek, ear, nose, and facial asymmetry:
iris size/color, sclera share, main catchlight, supporting reflection, and lower-lid treatment:
hair outer mass, major clumps, sparse interior lines, edge strands, and highlight shape:
outer silhouette line:
overlap/contact line:
facial and eyelid line:
hair interior line:
clothing fold line:
local hatch line:
line tool and color:
pressure variation, taper, broken contour, overlap, retracing, unclosed turns, and local line boil:
skin midtone, cheek marks, hair mass color, garment blocks, prop accent, and shadow hue:
matte fill boundary, controlled offset/overshoot, and one-step cel-shadow shape:
clothing construction, force/contact folds, fabric weight, and wear state:
left/right hand ownership, finger pressure, thumb base, wrist and forearm route:
feet, shoes, seated/standing support, and action consequence:
key prop shape, contact point, angle, weight, and ownership state:
motivated key/fill/edge light on face, hair, hands, clothes, and prop:
paper grain, scan noise, animation-camera softness, and allowed roughness locations:
```

Keep the key prop in the same character description unless the user explicitly requests an isolated prop sheet.

## Age And Body Construction

State age through visible anatomy rather than labels alone:

- adult height, shoulder breadth, neck length, hand size, facial plane, posture, and garment weight for adult characters;
- age-appropriate head-to-body ratio and joint proportions;
- body build through silhouette, shoulder/hip relation, limb thickness, stance, and clothing fit;
- support and gravity through pelvis, planted foot, seated compression, hand pressure, or object weight.

Cute, healing, and warm adult characters keep adult anatomy. Cuteness comes from soft jaw shape, coherent eyes, cheek marks, relaxed support, gentle asymmetry, and warm local light.

## Face Construction

Describe each visible facial layer:

- cranium width and taper into the jaw;
- cheek fullness and left/right asymmetry;
- upper and lower eyelid strength and opening shape;
- iris share, color, focus direction, sclera share, one main catchlight, and restrained support reflection;
- brow shape and distance from the upper lid;
- nose mark type and visibility;
- mouth length, opening, corner asymmetry, and jaw/throat support;
- cheek blush or pressure marks: color, stroke direction, density, and location;
- under-eye or neck hatching only where the selected emotional lane requires it.

Face description cannot carry the emotion alone. Connect it to neck, shoulders, spine, hands, feet, and prop pressure.

## Hair Construction

Build hair in this order:

```text
outer silhouette
-> major directional masses
-> overlap boundaries
-> sparse interior separation lines
-> irregular edge strands
-> broad low-contrast highlight or limited strips
-> wind, moisture, gravity, and contact residue
```

Black hair remains a coherent charcoal mass with controlled value lift. Colored hair remains broad flat planes with one restrained shadow family.

## Linework Construction

Every character prompt names the line system explicitly:

1. `tool and color`: graphite, charcoal, dry pencil, ink-pencil hybrid, warm dark-brown, charcoal grey, or dark blue-grey;
2. `hierarchy`: strongest outer silhouette, firm overlap/contact line, lighter facial line, sparse hair interior line, force-driven clothing fold, thinnest local hatch;
3. `pressure`: where lines thicken, thin, taper, fade, or restart;
4. `human defects`: broken contour, overlap, retracing, doubled correction, incomplete closure, corner irregularity, or slight fill offset;
5. `roughness map`: exact locations such as hair edge, hand, elbow, hem, eye shadow, cheek, neck, or force peak;
6. `stability map`: eyes, mouth, finger contact, prop geometry, and identity anchors remain readable;
7. `scale adaptation`: middle/distant figures use stronger silhouette and fewer facial marks; close figures allow finer eyelid, mouth, finger, and hatch detail.

Rough linework is controlled evidence of hand drawing. Spread roughness according to force, emotion, scale, and contact rather than describing the whole body with one adjective.

## Color, Fill, And Cel Shadow

State separate roles for:

- skin midtone and cheek warmth;
- hair mass and broad highlight;
- garment flat-color blocks;
- prop accent and ownership cue;
- one cel-shadow hue, hardness, and placement;
- environmental sky, foliage, wall, water, lamp, or window contamination;
- one restrained narrative accent.

Describe matte fill boundaries and controlled hand offset. Place the one-step cel shadow under hair, chin, collar, sleeve, lap, hand/prop contact, or support according to the actual light and pose.

## Clothing, Hands, And Prop

Clothing folds appear only where gravity, bending, compression, straps, hand grip, seating, wind, or material weight creates them. State garment cut and fabric weight before folds.

For every important hand write:

```text
left or right hand
-> object or surface
-> contact point
-> thumb base and finger spread
-> pressure/compression
-> wrist and forearm route
-> what the grip reveals
```

For seated characters, state hip compression, knee route, foot support, garment gathering, and prop load. For standing characters, state support leg, free leg, heel/toe state, pelvis counterbalance, and object pull.

## Output Form

For any prompt containing a character, include these rows inside the execution lock or character lock:

```markdown
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

Then write one self-contained `MJ描述` paragraph that repeats every pixel-changing character fact. The user must not need to merge the breakdown back into the prompt.

## Hard Failure Gate

Rewrite before delivery when any of these is true:

- character style is one sentence, a source label, or an adjective bundle;
- age is named but body proportions remain unspecified;
- support, weight, center of gravity, gaze, hands, feet, or prop ownership is unclear;
- face description omits jaw/cheek construction, eyelid shape, iris/catchlight, nose, mouth, or local marks;
- hair is described only by length or color without outer mass, clumps, interior lines, edge strands, and highlight family;
- linework lacks tool/color, hierarchy, pressure, taper, broken/overlap/retraced behavior, roughness locations, or stable identity anchors;
- fill lacks matte boundary behavior, color roles, and one-step cel-shadow placement;
- clothing folds do not follow gravity, bend, compression, contact, or fabric weight;
- important hands lack finger pressure, thumb base, wrist route, and object contact;
- cute adult identity loses adult shoulders, neck, hands, posture, or garment weight;
- the final MJ paragraph omits character facts that appear only in the execution lock.

Validate saved character descriptions with:

```powershell
python scripts/validate_mj_description.py <prompt.txt> --profile detailed-character
python scripts/validate_mj_description.py <prompt.txt> --profile hybrid-scene
```
