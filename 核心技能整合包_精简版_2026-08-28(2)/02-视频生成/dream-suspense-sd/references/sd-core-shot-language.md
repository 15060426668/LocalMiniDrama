# SD Core Shot Language

Use this reference when converting storyboard rows that depend on gaze chains, blocking, thresholds, foreground occlusion, cut-point rhythm, or reaction-first suspense into Dream SD / Seedance A and E blocks.

## Positive Translation Order

For each A segment, translate core shot language in this order:

1. Camera layer: shot size, lens, angle, movement path, start frame, landing frame.
2. Spatial relation: subject position, boundary, axis, distance, foreground/midground/background.
3. Gaze chain: eye direction, target, receiver, blink/avoidance/body pause.
4. Occlusion layer: physical foreground filter, visible fragment, revealed area.
5. Reaction detail: body freeze, hand, throat, eyes, foot, breath, object tremor.
6. Cut anchor: incomplete action, sound bridge, landing state.

## Gaze Chain Prompt Anchors

Use visible eye vectors:

- `her eyes drop to the ticket corner in his pocket, pause, then lift to his face`
- `he keeps his eyes fixed on her while his fingers stop moving on the table`
- `she glances toward the door slit, blinks once, then lowers her eyes`
- `the group follows the father's gaze toward the child at the doorway`

Add one micro-body proof:

- eyelid hold, pupils widening, jaw setting, throat swallow, fingertip pause, breath catch, shoulder tightening.

## Blocking / Axis / Threshold Prompt Anchors

Write exact spatial facts:

- `one foot inside the warm bedroom light, one foot in the cold corridor`
- `his hand grips the doorknob, his shoulder blocks half the doorway`
- `the table forms a hard horizontal barrier between them`
- `she leans across the table line while he pulls his chair backward`
- `the elevator corner traps her body while two figures stand near the door`

Maintain screen direction:

- `camera stays on the same side of the table axis`
- `movement continues from screen left to screen right`
- `the door remains on the rear right wall across the whole segment`

## Foreground Occlusion Prompt Anchors

Use a physical occluder and a readable fragment:

- `black doorframe edge covers the left half of the frame, only one sleeve and one eye visible through the slit`
- `foreground shoulder silhouette blocks part of her face while the mirror behind her shows a different hand movement`
- `rainy glass covers the foreground with streaking reflections, his outline stays broken behind the water`
- `curtain fabric sways across the lens, revealing only shoes and a hand near the floor`

Keep layers separated:

- foreground occluder, midground subject, background clue, light source, reflection surface.

## Cut-Point Prompt Anchors

Make the incomplete action visible:

- `at the final beat her fingers touch the metal handle and stop`
- `the cup leaves his hand and hangs at the edge of the frame`
- `the smile remains on her face while her eyes lose focus`
- `the door opens only a narrow strip of light`
- `his foot lifts from the floor, held before stepping across the threshold`

Sound bridge anchors:

- `the handle click begins before the next frame`
- `room tone drops as the object starts to fall`
- `a hallway voice arrives one beat before the image changes`

## Reaction-First Prompt Anchors

Translate emotion through body sequence:

- `she freezes, fingers tighten around the blanket, throat swallows once, eyes widen toward the unseen doorway`
- `he keeps standing still, keys slip from his hand onto the floor, shoulders lower slowly`
- `her hand stops scrolling, phone screen dims, she stays seated facing the bathroom door`
- `his outstretched hand remains suspended in the air, mouth slightly open, breath silent`

Use trigger-to-reaction chain:

`off-screen sound / object evidence / light change -> body stop -> body fragment detail -> face or delayed blankness -> tail frame`.

## A Block Mini-Checklist

Every relevant segment should preserve:

- gaze path and target.
- exact position and threshold/axis.
- foreground occlusion layer and visible fragment.
- reaction body detail.
- incomplete action or sound bridge at the cut.
- landing frame that continues into E.

