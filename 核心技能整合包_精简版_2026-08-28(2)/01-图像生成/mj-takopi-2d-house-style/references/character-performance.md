# Static Character Performance

## Contents

1. Performance thesis
2. Character lock card
3. Pose and silhouette
4. Face and gaze
5. Hands, feet, and objects
6. Expression families
7. Group acting
8. Character-sheet design
9. Static prompt vocabulary
10. Failure boundaries

## 1. Performance Thesis

A strong still does not label emotion. It freezes intention, body mechanics, gaze, contact, and residue at one decisive point.

```text
intention
-> line of action and weight
-> head/shoulder/spine relation
-> gaze and eyelid state
-> mouth and cheek marks
-> hands/feet and object ownership
-> clothing/hair delay
-> environment or group response
```

Choose one dominant action owner. Supporting reactions remain lower in amplitude.

## 2. Character Lock Card

Before writing the image description, lock:

```text
name used internally only:
age and role:
height and body silhouette:
head, jaw, cheek shape:
iris size/color, eyelid weight, catchlight pattern:
nose and mouth grammar:
hair outer silhouette, clumps, wisps, highlight:
skin midtone and cheek marks:
clothing cut, flat-color blocks, fold density:
hands/feet simplification:
distinctive prop and ownership:
ordinary posture baseline:
public expression baseline:
private leakage cue:
culture and period anchors:
```

For batch output, keep this card stable and change only pose, expression, lighting lane, or scene context.

## 3. Pose and Silhouette

### Ordinary baseline

- Let the pelvis and support leg carry standing weight.
- Let seated characters settle into hips, knees, furniture, or floor.
- Keep shoulders and hips slightly counterposed.
- Use small asymmetry in elbows, knees, fingers, and head tilt.
- Preserve clear negative space between arm and torso where the gesture matters.

### Open social energy

- chest and face lifted;
- head angled toward the relationship target;
- arms separated from torso;
- elbows and wrists form soft arcs;
- knees and feet point toward the group or shared object;
- hair and loose cloth retain a little delayed motion.

### Suppressed or guarded energy

- shoulders narrow inward;
- elbows approach ribs;
- hands press fabric, strap, knees, paper, or an object;
- feet turn inward or prepare an exit route;
- chin lowers while eyes may still track the social field;
- oversized clothing compresses around the abdomen or lap.

### Speed or impact still

- show anticipation or consequence rather than a neutral floating pose;
- place the support foot, lifted heel, bent elbow, or reaching hand clearly;
- let hair and cloth trail behind the body route;
- use stronger outer contour and sparse directional lines only near the force path;
- keep the face simpler than the body mechanics when motion is dominant.

## 4. Face and Gaze

### Gaze route

Specify exactly what the person looks at:

- another face;
- a hand or object;
- a point outside the frame;
- a reflection in glass;
- the floor or exit;
- nothing in focus.

Gaze direction, head direction, and torso direction may differ when the character hesitates, conceals, or leaves.

### Eyelid behavior

- relaxed: soft upper arc, visible iris, quiet lower lid;
- delighted: upper and lower lids open with a simple warm catchlight;
- smiling closed: long gentle arc with cheek lift;
- watchful: one lid slightly lower, iris shifted, brow minimally tightened;
- tired: upper lid heavy, lower lid faintly shaded, catchlight reduced;
- hurt but composed: lids hold nearly normal while mouth and hands lose coordination;
- startled: eye opens quickly but shoulders, fingers, and posture confirm the event.

### Mouth behavior

- quiet contentment: short lifted curve or small parted wedge;
- polite social smile: mouth lifts while gaze and hands remain restrained;
- open joy: one broad graphic opening with a simple inner warm plane;
- uncertainty: tiny asymmetrical opening, one corner delayed;
- suppression: compressed short line with jaw or throat tension;
- fatigue: small loose mouth, slightly lowered corners;
- anger: compact mouth tension supported by brows, jaw, shoulders, and grip;
- crying: mouth and jaw lose control only at peak; tears retain weight and path.

### Cheek and under-eye marks

- Use short vertical strokes for warmth, embarrassment, effort, or open joy.
- Use sparse irregular diagonal strokes and muted local tone for fatigue or pressure.
- Keep marks uneven and responsive to face volume.
- Do not use identical pink stripes on every expression.

## 5. Hands, Feet, and Objects

Hands often reveal the private emotional layer before the face.

Write:

```text
which hand
-> exact object or surface
-> contact point
-> finger spread or pressure
-> wrist and forearm route
-> what the contact reveals
```

Examples of visible intent:

- fingertips hovering above a phone without touching it;
- thumb pressing the edge of a notebook while the public smile remains;
- one hand splayed on glass, palm flattened and fingers uneven;
- both hands lightly folded over knees during safe intimacy;
- fingers closing around a bag strap while feet point away;
- near hand enlarged by perspective, index finger and thumb forming a readable shape;
- one fist held close to the body during running, the other arm opening for balance.

Feet and shoes should clarify support and choice: planted, dragged, lifted heel, inward toe, outward route, crossed ankles, knees gathered, or one foot already leaving.

## 6. Expression Families

### `OPEN-JOY`

Face: closed-eye arcs or wide warm irises, raised cheeks, graphic open mouth, short peach cheek lines.

Body: lifted chest, relaxed neck, arms open or gesturing, weight shared with friends or a prop.

Texture: clean face, minimal shadow, bright ordinary light or a limited warm graphic accent.

### `QUIET-CONTENTMENT`

Face: soft gaze, small smile, low brow tension, restrained catchlight.

Body: settled hips, hands resting on knees/paper/bedding, shoulders uneven but relaxed.

Texture: gentle cel shadow, faint grain, environment remains present.

### `WONDER`

Face: widened iris, lifted brows, small open mouth or quiet smile, one warm secondary reflection.

Body: neck lengthens, torso leans forward, hands hover or open, hair/cloth gains a small upward rhythm.

Texture: localized sparkle or heart/star graphics only if the character owns the interpretation.

### `WATCHFUL`

Face: gaze shifts before head, one eyelid changes, mouth stays small.

Body: torso continues its prior task, one hand pauses, feet keep their previous route.

Texture: ordinary cel baseline with one localized shadow or object reflection.

### `SOCIAL-MASK`

Face: polite smile or neutral mouth retained, eyes slightly off focus.

Body: public posture continues while fingers press fabric, knees close, shoulders narrow, or feet turn away.

Texture: clean face mids, sparse under-eye or cheek hatching, ordinary background activity.

### `SUPPRESSED-HURT`

Face: heavy lids, lowered gaze, compact mouth, damp eye with limited highlight.

Body: chin low, shoulders inward, elbows close, hands gripping a strap or lap, body made smaller.

Texture: local grey-olive or grey-violet shadow around eyes/neck, short irregular hatching, daylight retained.

### `EXHAUSTED`

Face: half-open eyes, reduced catchlight, loose small mouth, hair partly across face.

Body: spine curved, head slightly off-axis, one shoulder lower, oversized shirt hanging heavily.

Texture: matte pale skin, localized eye shadow, quiet cyan/grey/brown environment, mild capture grain.

### `ANGER-HELD`

Face: brows converge modestly, iris focused, jaw and mouth compact rather than oversized.

Body: weight moves forward, shoulder line tightens, hand or prop grip becomes decisive.

Texture: stronger contact line, local warm cheek/ear tone or cool shadow, clean background geometry.

### `EMOTIONAL-PEAK`

Face: one dominant change, such as large wet eyes, bold open mouth, tears, or closed-eye laugh.

Body: neck, shoulders, spine, hands, and center of gravity participate.

Texture: graphic accent, stronger light, or rougher line remains local; reality contact and clothing weight stay visible.

## 7. Group Acting

### Friendship ensemble

- stagger heights and body directions;
- give each person a different smile, eye state, hand gesture, and prop;
- use shoulder contact, shared paper, bags, or converging gaze to connect them;
- keep one quiet character lower in amplitude rather than forcing equal excitement.

### Intimate trio

- center one calm figure and place two more active figures on different sides;
- let hands on knees, a shared page, shoulder overlap, or mascot position create the relationship triangle;
- vary who looks at whom; the viewer need not receive every gaze.

### Group pressure

- define exact count and spatial roles;
- let one body or object control the route;
- keep the vulnerable person smaller, lower, occluded, or outside the gaze circuit;
- assign staggered low-amplitude reactions instead of synchronized faces;
- preserve ordinary tasks for people who have not noticed the event.

### Character plus mascot

- separate detail density and hue;
- specify whether the mascot rests on, leans toward, floats beside, or presses against the character;
- let the mascot's simple tilt and silhouette contrast with the human's eyelids, hands, and posture;
- keep the relationship readable even if the mascot has only dot eyes and a tiny mouth.

## 8. Character-Sheet Design

For a stable series design, request a clean sheet with:

- neutral full body front or three-quarter pose;
- side and back silhouette when hair/costume requires it;
- calm face, open joy, watchful, social mask, suppressed hurt, and exhausted expression;
- one hand/prop interaction;
- flat color blocks and one restrained cel-shadow sample;
- hair mass and edge-wisp consistency;
- clothing fold density at shoulders, elbows, waist, knees, and straps;
- culture-specific costume and object details;
- simple clean background or organized model-sheet field.

Do not overload one sheet with cinematic lighting, dense environment, and every emotion. Separate identity sheet, expression sheet, and scene look-dev when necessary.

## 9. Static Prompt Vocabulary

Use concrete phrases such as:

```text
soft short jaw and gently full cheeks
large coherent dark iris with one main wet catchlight
heavy upper eyelid and faint lower-lid shadow
small nose mark and compact asymmetrical mouth
short uneven peach cheek strokes
large charcoal hair silhouette with sparse irregular edge wisps
thin dark-brown hand-drawn contour with tapered pressure changes
one-step cel shadow under hair, chin, sleeve, and object contact
matte pale skin and broad flat clothing color
shoulders drawn inward while fingers press the bag strap
rear heel raised, front foot planted, hair and shirt hem trailing the run
simple coral mascot silhouette with dot eyes and tiny mouth
```

Avoid abstract labels when a visible action can replace them.

## 10. Failure Boundaries

Reject and rewrite when:

- the face alone carries the emotion while shoulders, hands, and posture remain neutral;
- every mood uses giant wet eyes and pink blush;
- the child body looks like an adult body with a large head pasted on;
- adult characters retain child hand size, shoulder width, or posture;
- hands are hidden or malformed when the prop interaction is central;
- all group members use the same face and gesture;
- running or impact poses float without support foot, force route, or cloth/hair delay;
- eyes contain excessive gemstone detail unrelated to the lane;
- sadness automatically becomes tears, darkness, and a collapsed body;
- expression vocabulary replaces exact gaze, mouth, hand, and weight instructions.
