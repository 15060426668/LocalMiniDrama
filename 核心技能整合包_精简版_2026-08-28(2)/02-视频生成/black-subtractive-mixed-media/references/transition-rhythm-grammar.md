# Transition Rhythm Grammar for 2D Character / Live-Action Plates

## Project lock

Apply these defaults unless the user overrides them:

- The protagonist is a woman. Do not invent a male protagonist, male companion, boy, or romance beat.
- She is a colored rough hand-drawn 2D layer: unstable dark blue-gray contour, varied line pressure, small broken overlaps, matte low-saturation color blocks, restrained cel shadows, sparse local hatching, and slight drawing boil.
- The environment and NPCs are photoreal live action. Preserve lens behavior, exposure roll-off, real material texture, depth of field, motion blur, weather, and ordinary independent NPC tasks.
- The woman must remain visibly drawn. Do not convert her to photoreal skin, clean generic anime, monochrome manga, white line art, a paper cutout, or a glowing sticker.
- If the user says not to describe the mask, omit the entire black-treatment block. Do not leave indirect black-matte language behind.

## Select a transition family by dramatic cause

| Family | Use when | Required invariant | Black-subtractive adaptation |
|---|---|---|---|
| Full-cover physical wipe | A hand, sleeve, hair, suitcase, umbrella, cloth, wall edge, or passing body can plausibly occupy the lens | Cover direction and exit edge | Let the physical cover become the black mass; preserve a narrow contact or gaze aperture before the destination opens. |
| Action-phase match | The woman's step, turn, lift, throw, crouch, sit, or prop swing is the emotional verb | Support, center of gravity, action phase, and vector | Close black around the peak action, but reveal the same limb/prop on the opposite side completing the route. |
| Prop-state bridge | A phone, bottle, flower, suitcase, letter, door handle, umbrella, or cup carries meaning between worlds | Grip, prop angle, screen coordinate, and state change | Isolate the prop in a small aperture; allow the real destination to grow from its reflection, opening, spill, or contact. |
| Shape/axis match | Architecture, horizon, weapon/arm line, doorway, path, or body silhouette can map between shots | Dominant line and vanishing direction | Make the matte edge inherit the matched axis; never animate an arbitrary circle when the scene supplies a stronger shape. |
| Water/light/fabric wash | The mood should feel tactile, dreamlike, lonely, or remembered | Material flow direction, edge speed, and residue | Replace uniform wipe motion with irregular liquid, cloth, or exposure-shaped apertures; keep droplets, folds, or edge light after the reveal. |
| Phone preview to full scene | The destination can be promised before it is entered | Framing, horizon, exposure, and camera direction | The phone window is the first aperture; black removes the surrounding plate while the preview expands into the same full-scale real location. |
| Doorway/passing threshold | The action is departure, arrival, avoidance, or crossing a boundary | Travel direction, threshold plane, and timing | Treat the door/body edge as the moving matte boundary and reveal the new world in depth, not as a flat replacement. |
| Long atmospheric landing | The payoff is loneliness, freedom, memory, or scale rather than shock | Residual action and environmental motion | Stop transforming the matte after the reveal; let only small black residues or edge shadows settle while the world breathes. |

## Rhythm templates

Percentages are relative to final runtime and should follow musical phrases, not mechanical stopwatch equality.

### Template A: ordinary-to-cinematic release, 6-9 s

```text
0-18%   ordinary plate evidence and independent background life
18-30%  protagonist notices or prepares the single trigger
30-36%  cover/blur/black compression, main cut on a strong onset
36-50%  transformed world resolves; the action finishes
50-100% long landing with breath, weather, cloth/hair, and subtle camera drift
```

Use when the visual contrast itself is the hook. Do not spend the tail on a second unrelated transition.

### Template B: action-phase transformation, 6-8 s

```text
0-22%   establish stance, support, prop, and destination action geometry
22-42%  preparation and acceleration
42-48%  peak blur or full cover on the onset
48-65%  same action continues in the transformed plate
65-100% contact, reaction, recovery, and stable landing
```

The source and destination performances are one action, not two similar poses. Match support foot/seat, center of gravity, screen position, limb route, gaze, and prop angle before adding spectacle.

### Template C: tactile memory portal, 8-12 s

```text
0-25%   quiet real task, loneliness, and tactile object introduction
25-42%  hesitation, breath, gaze, and material preparation
42-55%  liquid/fabric/light/object state spreads through frame
55-66%  aperture discloses the distant real location in fragments
66-100% long scenic tail; only residual material and environmental motion remain
```

Use a delayed or softened onset when anticipation is part of the emotion. Avoid a hard flash if the material has already supplied a readable transition surface.

### Template D: slow pull-open black subtraction, 9-15 s

```text
0-15%   near-black field retains one live photographic cue
15-32%  a narrow aperture opens along gaze, hand, suitcase, doorway, or ground contact
32-48%  the 2D woman enters or is discovered without losing drawn identity
48-62%  a second depth plane and one real NPC path become readable
62-78%  aperture reaches maximum useful scale on the strongest phrase
78-100% hold; small edge settling, rain/wind/particles, breath, and camera drift only
```

The reveal must feel like the screen is slowly granting spatial information. Do not simply raise global exposure from black.

## Beat construction

For each beat, write these fields before model compilation:

1. `baseline`: the ordinary task in the live plate and the NPCs' independent tasks.
2. `trigger`: one hand, body, prop, threshold, water, cloth, light, or sound event.
3. `preparation`: gaze, breath, support shift, hand route, and acceleration.
4. `concealment`: what physically occupies the lens or what black shape removes context.
5. `invariants`: at least three preserved facts across the change.
6. `release`: the first destination fragment and the exact strong onset or phrase boundary.
7. `continuation`: contact, reaction, recovery, cloth/hair inertia, particles, and real environmental response.
8. `tail`: the stable emotional image and the remaining small motions.

One beat owns one dominant transformation. Split the sequence when two independent triggers, camera paths, or world replacements compete.

## Black-subtractive adaptation

The black layer does not replace transition blocking. It edits information around an already coherent action.

```text
visible preparation
-> physically motivated cover or black compression
-> one surviving aperture keeps contact, prop, or gaze readable
-> strong onset releases the first destination depth cue
-> aperture follows the preserved action vector or scene axis
-> the same 2D action completes inside the live-action destination
-> black settles while residual body and environment motion continue
```

Rules:

- Give the matte a source, depth plane, contour, motion direction, speed change, maximum coverage, and landing state.
- During broad coverage, retain one information cue. Total emptiness is permitted only for the few frames physically required by a full lens cover.
- Use the plate's shapes: doorway, eave, window, path, stair wedge, suitcase edge, umbrella canopy, cloth fold, water sheet, or passing body.
- The matte edge may carry narrow spill or reflected light only when an actual light source or reflective surface supports it.
- The aperture must reveal perspective in order: contact/foreground, protagonist action, then wider world. Do not disclose every plane at once.
- After the main release, reduce effect activity. The tail belongs to performance, environment, and scale.

## 2D/live-action binding

Before the transition, during the cover, and after the release, preserve the same identity and spatial occupancy:

- Match camera height, horizon, lens feel, subject scale, and foot/seat plane.
- Let a real foreground object or NPC cross in front of the drawn woman when spatially plausible.
- Add contact compression, cast shadow, surface deformation, reflection or color spill where physically present, and particles crossing both depth sides.
- Apply live light direction and color temperature to the woman's matte fills and cel-shadow family without adding photoreal skin texture.
- Keep drawing boil and selective frame cadence in the contour and secondary motion, while the live camera retains natural motion blur.
- NPCs do not all notice her. Give each one a task, distance, line of sight, and staggered access to the event.

## Sound-picture binding

- Place the principal release within about 0.00-0.34 s of a strong onset by default. Earlier visual preparation is acceptable; an unexplained late cut is not.
- Bind onset to a visible cause: cover completion, foot contact, prop impact, door crossing, water crest, fabric snap, light breach, or first destination disclosure.
- Use pre-lap ambience to promise the destination only when it supports the story. Keep it subtle enough that the reveal still changes the perceived world.
- Preserve a tail of rain, wind, cloth, water, room tone, distant traffic, insects, or footsteps after the accent. Silence or noise should have a spatial source.

## Failure boundaries

- **Preset wipe**: the edge has no physical source or scene axis. Rebuild from a prop, body, threshold, or material already present.
- **Two poses, not one action**: support, weight, limb phase, or prop angle changes across the cut. Rehearse the source as the first half of the destination action.
- **Cut lands off-beat**: the visual release is more than roughly 0.34 s from the intended onset without an anticipation reason. Move the cut or choose a different onset.
- **Destination is a postcard**: motion stops after the reveal. Add action completion, reaction, recovery, weather, cloth/hair inertia, and slight camera drift.
- **2D sticker**: the woman floats above the plate. Restore scale, contact, shadow, occlusion, light spill, parallax, and depth particles.
- **Style collapse**: the woman becomes clean anime, monochrome line art, a white cutout, or a real actor. Reassert colored rough contour, matte fills, restrained cel shadows, and drawing boil.
- **Mask overproduction**: black continues performing after the emotional image has landed. Settle the matte and give the tail to the scene.
- **Male role invention**: a boy/man/romantic partner appears without request. Remove him and rebuild the action around the woman, her object, the environment, and independent real NPCs.
- **Crowd worship**: every NPC turns toward the protagonist. Restore independent tasks and staggered perception.
- **Source-name prompting**: creator or artist names appear in a model payload. Replace them with observable geometry, motion, material, light, and cadence.

## Acceptance gate

Before handing a storyboard to SD/Seedance, confirm:

- one dramatic cause selects one transition family;
- the source action visibly prepares the cover and the destination visibly completes it;
- at least three invariants survive the edit;
- the principal release is bound to an identified sound onset or phrase boundary;
- the landing occupies enough runtime to read action, scale, weather, and emotion;
- the woman remains colored rough 2D and no male lead has been invented;
- the plate and NPCs retain live-action photographic evidence and independent behavior;
- black has a physical source, changing boundary, depth position, and settling state when black treatment is requested;
- no source creator, donor caption, account name, or artist identity appears in model-facing text.

