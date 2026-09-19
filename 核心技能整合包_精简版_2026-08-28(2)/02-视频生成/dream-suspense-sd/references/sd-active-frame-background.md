# SD Shot Motion Ecology

Runtime version: `2.2 / 2026-07-10`

Use this file when Dream SD must translate layered motion: main characters, listeners, NPCs, props, machinery, weather, water, plants, cloth, light, camera and sound acting within the same shot.

## 1. Positive Prompt Formula

```text
initial state
+ information permission / knowledge state
+ primary motion
+ reactive character/object layer
+ ambient environmental-force family
+ camera/focus operation
+ sound-triggered visible response
+ physical/social consequence
+ landing and tail state
```

The main action keeps the highest visual priority. Background and environment remain readable, physically motivated and lower in amplitude until the story transfers attention to them.

## 2. Motion Hierarchy

For each A beat, assign:

```text
primary: one action carrying the new information
reactive: one or two responses caused by the primary action
ambient: one shared force/cycle such as wind, rain, vehicle vibration, fan airflow or screen pulse
held state: visible stillness with readable posture and attention
```

A normal 2-4 second beat carries one primary motion, one or two reactive motions, one ambient family, one camera/focus operation and one sound landing.

## 3. A-Block Field

Add:

```text
运动生态/层级交互：
信息权限/知情状态：...
主运动：...
陪体/听者：...
背景人物/NPC：...
前景与共享道具：...
背景物件/机械：...
环境力与材质响应：...
光影/摄影机运动：...
声音触发与可见反应：...
交互后果/残留：...
尾帧状态：...
```

Compact simple shots into one dense positive line. Keep dense multi-layer shots as separated tracks.

## 4. Causal Prompt Chain

```text
force/action source
-> contact or carrier
-> first visible response
-> secondary response in another layer
-> sound/light/material evidence
-> remaining trace
-> next action consequence
```

Example:

```text
woman places the key on the wooden table, key impact sends a small vibration through the water glass, man stops pouring, water crosses the cup rim and spreads along the wood grain, background child pauses halfway through folding a shirt, refrigerator hum ends, tail frame holds the key, advancing water line and unfinished shirt fold
```

## 5. Environmental Force Anchors

### Wind / Airflow

```text
window draft enters from screen right, curtain lifts leftward first, nearby plant leaves tremble with smaller amplitude, loose paper corner rises, water surface forms short ripples, leaf shadow travels across the wall, curtain and leaves settle at different speeds
```

### Rain

```text
rain strikes the window and merges into downward streaks, exterior headlights refract through the water, wet clothing grows heavier and clings to the body, shoes create puddle splashes, nearby leaves bend under droplets, drainage water carries small debris toward the frame edge
```

### Dripping Water

```text
droplet grows at the pipe edge through surface tension, stretches downward, releases under gravity, strikes the puddle, creates one crown splash and expanding rings, reflected light breaks across the rings, tail frame holds the next droplet forming
```

### Fan / Ventilation

```text
fan rotates at steady speed, hair ends and paper edges respond with repeated pulses, curtain moves with broader slower waves, smoke bends along the airflow, fan stops and every light material settles at a different delay
```

### Vehicle / Machinery

```text
vehicle vibration travels through seats and loose objects, hanging handles sway in shared rhythm, passing street lights sweep across faces and windows, braking shifts every torso forward, seatbelts and hands provide resistance, loose props slide and settle in the new speed state
```

### Door / Window

```text
hand releases the latch, door opens along its hinge arc, air pressure lifts the curtain and receipt edge, corridor light expands across the floor, nearby plant leaves move once, door continues swinging and settles with a soft hinge vibration
```

### Plants

```text
outer leaves receive the wind first, motion travels through smaller leaves into the stem, heavier leaves respond with reduced amplitude, water drops gather at leaf tips, one drop falls and bends the leaf upward, moving leaf shadow crosses the wall, stem returns gradually to rest
```

## 6. NPC And Secondary Character Anchors

Choose one readable level:

- `background person continuing a routine task with natural breathing and weight shifts`.
- `background person pausing one hand after the sound cue, gaze moving toward the source, unfinished task remaining visible`.
- `background person stepping aside and moving a cart to clear the route, cart wheels continuing to rotate`.
- `background person catching the dropped object, checking its owner, then changing route`.
- `several background people reacting unevenly: one looks up, one continues typing, one steps back after noticing the approaching figure`.

Collective synchronized motion uses a shared command, alarm, ritual, system signal or visible stimulus.

## 7. Scene Prompt Patterns

### Dialogue

```text
speaker delivers one phrase while continuing a simple hand task, listener fingers pause and eyes move toward the shared object during the phrase gap, background family member continues packing then stops after the key impact, curtain and plant leaves move in the same window draft, locked camera holds all layers, key contact sound lands the beat
```

### Multi-Person Room

```text
one speaking character owns the line, intended listener turns slightly and keeps holding the document, third person continues pouring water, fourth person notices the spill and moves a chair aside, ceiling fan maintains steady airflow through paper edges, camera keeps the table axis readable
```

### Chase

```text
runner drives forward with grounded foot contact, shoulder strikes the cleaning cart, cart rolls toward screen left, hanging bottles swing with delayed inertia, cleaner steps back and grips the handle, wet wheel tracks remain on the floor, pursuer enters the disturbed route, low follow camera lands on the rolling cart and approaching feet
```

### Hospital / Office

```text
foreground character continues the professional task, background worker types steadily, elevator numbers change floor by floor, IV stand wheels turn after sleeve contact, frosted-glass silhouette pauses at the alarm tone, fluorescent light and monitor pulse remain continuous, tail frame holds the rolling stand beside the opened elevator
```

### Weather Exterior

```text
character crosses the frame against strong wind, coat and hair trail with different weight, roadside plants bend in the same direction, rainwater runs along the curb, loose sign vibrates, pedestrian grips an umbrella and changes route, vehicle spray briefly masks the background, wet footprints remain after the character exits
```

### Quiet Suspense Room

```text
subject performs one small foreground task, fan airflow moves curtain and plant leaves, water droplet grows at the pipe edge, background person holds a still listening posture, fan stops after the off-screen sound, curtain and leaves settle, droplet falls into the new silence, camera holds the resulting ripple
```

## 8. Consistency Anchors

```text
main subject identity and route remain stable, NPC positions and task states carry across cuts, shared force direction stays consistent, object ownership and material traces persist, machinery cycles continue through edits, light source direction remains stable, environmental motion settles naturally, tail state becomes the next start state
```

For complex motion ecology, compile through `BASE MANIFEST -> SEGMENT DELTA -> TAIL STATE -> NEXT SEGMENT START`.

## 9. Beat Phase Scheduler

Do not start every layer at the same instant. Schedule a normal 2-4 second beat through four phases:

```text
phase 1: establish the active routine or environmental cycle
phase 2: primary action or sound trigger
phase 3: one or two delayed reactions in other layers
phase 4: physical consequence, settling motion and tail state
```

Example:

```text
the waiter continues wiping the next table, the woman pushes the key across the wood, the key touches the water glass, the listener's pouring hand stops after the contact sound, the waiter glances over one beat later, spilled water advances along the grain, focus lands on the wet key while the curtain continues settling
```

Dialogue mouth movement, body route, hand interaction, listener reaction, NPC reaction and camera landing receive separate windows when they cannot remain legible together.

## 10. Shared Force And Delay Grammar

All carriers affected by one force share direction and timing logic:

```text
force source and direction
-> lightest / closest carrier responds first
-> heavier / farther carrier responds with lower amplitude and delay
-> contact creates material-specific motion and sound
-> layers settle at different speeds
```

Apply this to:

- wind -> loose hair -> paper edge -> curtain -> plant stem.
- braking -> loose prop -> torso -> hanging handle -> liquid surface.
- foot impact -> floor vibration -> glass ripple -> hanging object -> dust fall.
- door opening -> pressure wave -> light strip -> curtain -> paper -> room sound change.
- rain -> glass streak -> clothing weight -> puddle splash -> drainage flow -> plant drop fall.

NPC reactions also use delay and distance. A nearby listener may stop a hand first; a distant worker may react only after the sound reaches the background.

## 11. Motion-Ecology Complexity Gate

Count the following inside one A beat:

| Element | Points |
|---|---:|
| primary subject action | 1 |
| dialogue/lip-sync concurrent with body movement | 1 |
| each important reactive person or NPC layer | 1 |
| performed ignorance or public/private dual-channel signal | 1 |
| prop or machinery force-transfer chain | 1 |
| one environmental-force family | 1 |
| second independent environmental-force family | 2 |
| moving light or focus transfer | 1 |
| camera path | 1 |
| transition or material transformation | 2 |

- `0-4`: compile as one dense positive line.
- `5-6`: separate subject, background/environment and camera/sound tracks.
- `7+`: split into sequential A beats.
- Two primary actions, two camera paths or two unrelated force families always trigger a split.

## 12. Positive-Only Motion Audit

Before output:

- preserve every motion layer present in the approved storyboard.
- omit layers absent from the source instead of inventing filler people, weather, plants, machinery or props.
- describe visible action and audible consequence directly; replace abstract words such as `dynamic`, `cinematic movement`, `busy background` or `tense atmosphere` with physical verbs and carriers.
- keep one primary attention owner at any instant.
- preserve who can perceive each cue; a character reacts only after seeing, hearing, touching or inferring it through another visible reaction.
- keep public behavior dominant and private signals smaller, localized and readable only to the intended audience/character layer.
- give collective synchronized movement a shared command, alarm, ritual or visible stimulus.
- keep NPC routines purposeful and reactions uneven.
- keep force direction, object ownership, material traces, machinery cycles and tail state consistent across cuts.
- write only positive executable prompt content in the user-visible five-field A output; keep E indexes internal or in a separate production attachment.

## 13. Information-Permission Compiler

When suspense depends on who knows or perceives what, compile one of these positive structures:

### Audience Ahead

```text
hidden background action remains visible to the camera, foreground subject continues without seeing it, occlusion and focus keep both knowledge layers readable, subject reacts only when a later sound or contact reaches them
```

### Delayed Knowledge Cascade

```text
first person receives the cue and stops one hand, second person reads that changed posture one beat later, third person continues the routine until the shared object or sound reaches them
```

### Performed Ignorance

```text
informed character continues the expected task with stable gaze and posture, breath tightens, fingertip pressure changes, one small error appears, nearby observer keeps testing while the wider background remains unaware
```

### Public/Private Split

```text
public gesture and voice maintain the social story, small private hand/gaze/foot/whisper signal reveals the hidden intention at close range, surrounding NPCs continue the public interpretation
```

### Camera Misdirection

```text
camera and responders hold focus on the dominant visible event, a fair secondary clue remains present at lower priority, later rack focus or reaction transfers ownership to that clue
```

Keep the in-scene knowledge map stable across cuts. A character cannot react to a layer they have not seen, heard, touched or inferred through another visible reaction.
