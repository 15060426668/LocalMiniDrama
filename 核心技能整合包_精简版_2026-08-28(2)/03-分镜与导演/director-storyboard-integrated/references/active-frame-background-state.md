# Shot Motion Ecology

Runtime version: `2.2 / 2026-07-10`

Use this file when the user mentions 动静物, 背景人物, 多人场景, NPC不动, 画面太死, 环境交互, 道具联动, 风雨水滴, 植物摆动, 活画面, 场景运动逻辑, or wants each storyboard shot to behave like a video rather than a still image.

## Contents

1. Core Law
2. Motion Lanes
3. Motion Hierarchy And Budget
4. Causal Interaction Chain
5. Environmental Force Library
6. Background Person Logic
7. Scene Templates
8. Counterpart Training Pool
9. Formal Storyboard Gate
10. SD Handoff Anchor

## Reference Ownership

| Reference | Owns | Does not own |
|---|---|---|
| `active-frame-background-state.md` | what moves, why, knowledge permission, causal order and tail state | film-reference inventory or final prompt prose |
| `motion-ecology-counterpart-atlas.md` | film-mechanism retrieval ME-A to ME-J | generic rules repeated in every task |
| `character-performance-bible.md` | actor posture, public/private behavior and recurring performance fingerprint | NPC/environment physics |
| `dialogue-physical-interaction-grammar.md` | dialogue windows, handoffs, contact and collision scheduling | complete frame ecology |
| `screen-action-breakdown.md` | objective visible record of the shot | causal design invention |
| `storyboard-sd-compiler-contract.md` | field mapping and lossless handoff | model-specific positive phrasing |
| Dream `sd-active-frame-background.md` | positive executable motion prompt | redesigning approved storyboard logic |

## 1. Core Law

A storyboard shot is a time-based system:

```text
initial state
-> force / action / sound trigger
-> primary motion
-> secondary and background responses
-> material/light/sound consequence
-> settling or continued movement
-> tail-frame state
```

Composition defines where everything is. Motion ecology defines what every visible layer does during the shot and why.

Every visible person, object and environmental element receives one state:

- `primary`: carries the shot's main information.
- `reactive`: responds to the primary action, dialogue, sound or force.
- `ambient`: continues a physically motivated background cycle.
- `held still`: remains still for a visible reason such as attention, fear, discipline, sleep, weight or mechanical rest.

Stillness is active only when the reason is readable.

## 2. Motion Lanes

For every formal shot, check these lanes:

| Lane | What must be decided |
|---|---|
| Main subject | body route, gaze, hands, feet, breath, speaking/listening, start and landing pose |
| Co-subject/listener | simultaneous task, delayed reaction, distance change, object relation, gaze target |
| Background people/NPCs | routine, interruption, uneven reaction, route, social relation, exit blocking or continued ignorance |
| Foreground objects | occlusion, sway, pass-by, vibration, reflection, contact, frame-edge movement |
| Shared props | owner, hand, orientation, weight, trigger, material response, new state |
| Background objects/machinery | fan, screen, door, curtain, clock, elevator, vehicle, IV stand, cart, appliance, sign, loose paper |
| Natural forces | wind, rain, water, gravity, heat, cold, steam, smoke, dust, airflow, surface tension |
| Plants/living background | leaves, stems, water drops, shadow movement, touch/wind response; visible people or animals react according to attention and distance |
| Light and shadow | source movement, flicker, passing light, reflection travel, shadow displacement, exposure change |
| Camera/focus | path, cadence, parallax, focus transfer, response to contact, landing frame |
| Sound | environment bed, body foley, object contact, NPC sound, off-screen source, sound-triggered visible response |
| Tail state | final body direction, NPC state, prop position, environmental motion, light state and sound tail |

### Information Permission Layer

Motion state and knowledge state are separate. For suspense scenes, assign each important layer an information permission:

| Permission | Meaning | Visible execution |
|---|---|---|
| audience ahead | the audience sees/hears a layer the subject cannot access | foreground occlusion, hidden background route, POV device, isolated sound channel |
| subject ahead | the subject knows something the audience or NPCs do not | withheld hand action, guarded eyeline, controlled prop ownership |
| shared knowledge | audience and subject receive the same trigger together | synchronized gaze route, focus transfer and body decision |
| delayed knowledge | a person learns through another person's reaction, sound or material consequence | hand stops after a glance, head turns after a second cue, route changes late |
| performed ignorance | a person knows but must behave as if unaware | continued task with controlled breath, fixed gaze, suppressed hand reaction |
| public/private split | public behavior supports one story while a small private signal reveals another | public smile or embrace plus hidden grip, eye contact, whisper, foot position or object pressure |

Record this inside `运动生态/层级交互`; do not create a new decorative field.

## 3. Motion Hierarchy And Budget

For a normal 2-4 second beat:

```text
one primary motion
+ one or two reactive motions
+ one ambient motion family
+ one camera/focus operation
+ one sound trigger or sound tail
```

Examples:

- speaker places a key (`primary`); listener fingers stop (`reactive`); curtain and plant leaves move in the same window draft (`ambient`); locked camera; key contact sound ends the beat.
- runner turns a corner (`primary`); shoulder hits hanging plastic and papers lift (`reactive`); corridor lights continue flickering (`ambient`); low follow camera; footsteps carry into the cut.

More visible movement is not automatically better. The main subject keeps the greatest visual weight. Background motion becomes dominant only when the story beat is audience discovery.

Long takes may contain more events, but they occur sequentially. Each new event takes ownership after the previous event lands.

### Reaction Topology

Do not default to simultaneous reaction. Choose one topology:

- direct: trigger -> nearest/most alert person reacts -> others remain on task.
- cascade: one person reacts -> second person reads that reaction -> third person notices the changed room.
- split knowledge: one person knows, one suspects, one remains unaware.
- performed stillness: the informed person suppresses the expected reaction.
- false reading: an NPC notices the consequence but assigns the wrong cause.
- system interruption: neutral machinery, traffic, weather or a passerby changes the result without understanding the main conflict.

Use qualitative timing such as `immediate`, `one beat later`, `after seeing the listener`, or `remains unaware`. Formal storyboard timing stays on integer seconds.

### Short-Form Baseline And Activation

For AIGC short-form:

```text
1-3 seconds readable baseline
-> one small deviation
-> one recognition reaction
-> consequence or tail hook
```

If a stronger stillness baseline is needed, establish it through repetition in earlier shots. Do not hold a static frame merely to imitate feature-film duration.

### Advanced Motion Controls

- threshold control: doors, tables, light borders, curtains and frame edges separate knowledge or power zones; crossing must change access.
- progressive material change: repeated contact accumulates cracks, vibration, wetness, displacement or fatigue rather than resetting.
- camera complicity: focus, occlusion or POV may align the audience with a watcher, a deceived character or a system, but the permission must remain readable.
- body/status coupling: standing, sitting, kneeling, crouching or crawling can express status descent; camera height follows only when that descent is the scene's main axis.
- plausible intrusion: traffic, a passerby, an elevator, weather, a phone or machinery may interrupt the conflict only when already supported by the location.
- dual-channel performance: public action and private signal coexist, but the private signal stays small enough to remain hidden from in-scene observers.

## 4. Causal Interaction Chain

Use:

```text
source force/action
-> first contact or carrier
-> first visible response
-> secondary response in another layer
-> sound/light/material evidence
-> remaining trace
-> next action consequence
```

### Dialogue Example

```text
woman says the final phrase
-> key touches table
-> man stops pouring water
-> water overflows and reaches the key
-> background child pauses packing for one beat
-> refrigerator hum drops out
-> tail frame holds key, water and the child's unfinished action
```

### Wind Example

```text
window draft enters from screen right
-> curtain lifts leftward
-> nearby plant leaves tremble with smaller amplitude
-> loose receipt corner lifts
-> water surface forms short ripples
-> moving leaf shadow crosses the wall
-> curtain settles while one drop remains on a leaf tip
```

### Chase Example

```text
runner's shoulder hits cleaning cart
-> cart wheels rotate and drift
-> hanging bottles swing
-> cleaner steps back and grips handle
-> water trail records wheel movement
-> pursuer later follows the disturbed cart and wet track
```

## 5. Environmental Force Library

| Force/state | Visible carriers | Physical behavior | Useful story effect |
|---|---|---|---|
| wind / airflow | hair, clothing, curtains, paper, leaves, hanging signs, flame, smoke | light elements respond first; heavier elements lag; movement shares one direction with different amplitude | proves an open window, approaching weather, ventilation change or unseen passage |
| rain | glass, skin, clothing, roofs, puddles, drains, plants | droplets merge, streak, splash, increase cloth weight, form runoff and ripples | alters visibility, route, evidence, sound and fatigue |
| dripping water | pipe, ceiling stain, leaf tip, faucet, wet cloth | droplet grows through surface tension, falls under gravity, splashes and leaves expanding rings | countdown, silence accent, spreading damage, tail-frame rhythm |
| gravity / slope | bodies, rolling objects, hanging props, liquid | acceleration follows incline; loose objects roll; posture compensates | reveals floor tilt, vehicle motion, dream-rule change or instability |
| heat | steam, skin, glass, metal, air | steam rises, condensation forms on cooler surfaces, air shimmers, skin reflects moisture | pressure, enclosed heat, cooking routine, machinery load |
| cold | breath, glass, metal, fabric, water | breath condenses, glass fogs, skin tightens, metal contact becomes cautious | bodily vulnerability, threshold warning, exterior exposure |
| fan / ventilation | hair ends, paper, curtain, smoke, plant leaves | repeated pulse or steady directional movement; nearby objects respond more strongly | mechanical rhythm, institutional routine, subtle state change when it stops |
| vehicles / machinery | bodies, straps, loose props, reflections, hanging handles | acceleration, vibration, braking inertia, repeated mechanical cycles | makes space move even when characters sit still |
| doors/windows | air pressure, hinge, light strip, curtain, nearby paper | opening changes airflow, light, sound and shadow; door continues swinging or settles | threshold consequence and spatial continuity |
| screen/light source | face, wall, glass, metal, eye highlights | pulse, scan, passing band or color shift follows source content | mediated information, system state, off-screen event |
| plants | leaves, stems, flowers, soil, water drops, shadows | wind/touch response travels from exposed leaves to stem; drops gather and fall; leaves settle at different speeds | proves airflow, time, neglect, touch or environmental change |

Environmental interaction uses one dominant force family per short beat. Rain may cause wet clothing, puddle ripples and plant movement because all three share the same force.

## 6. Background Person Logic

Background people remain part of the scene even while another character owns the line.

Assign one behavior level:

| Level | Behavior | Use |
|---:|---|---|
| 0 | readable silhouette/posture, breathing or weight shift | low-priority crowd depth |
| 1 | routine continues: walking, cleaning, typing, eating, packing, guarding, serving | living space and social realism |
| 2 | subtle reaction: glance, hand stop, delayed step, breath, route adjustment, unfinished action | main event affects nearby people |
| 3 | causal participation: moves aside, blocks route, catches object, opens door, passes information, follows a trace | NPC changes the action |
| 4 | background becomes the new information owner | audience discovers clue/threat through background |

NPC reaction is uneven:

- one person notices first.
- another continues the routine.
- someone misreads the event.
- someone protects their own task or space.
- someone reacts only after a sound or object reaches them.

Synchronized reactions require an explicit system, ritual, command or shared stimulus.

## 7. Scene Templates

### Dialogue / Domestic Conflict

```text
speaker mouth and body task
-> listener hand/gaze reaction
-> shared prop state
-> background family/NPC routine or pause
-> appliance/window/weather movement
-> object/silence tail frame
```

### Multi-Person Room

```text
one line owner
-> intended listener
-> third person keeps task
-> fourth person notices consequence
-> shared object changes owner/state
-> room machinery and sound remain continuous
```

### Chase / Escape

```text
body force
-> contact with set/prop
-> moving trace
-> NPC/object reaction
-> weather/light/mechanical response
-> threat uses or follows the trace
```

### Hospital / Office / Institution

```text
professional task
-> device/door/elevator cycle
-> worker continues routine
-> one worker pauses at abnormal sound
-> paper/IV/cart/screen changes state
-> system tone carries across cut
```

### Exterior Weather

```text
character route
-> weather acts on clothing/body
-> plants/signs/water respond
-> vehicle/pedestrian behavior changes
-> visibility and sound distance change
-> wet/dust/snow trace remains
```

### Quiet Suspense Room

```text
small subject action
-> ambient fan/curtain/plant/water motion
-> one cycle stops or changes
-> subject or NPC reacts after delay
-> held stillness becomes the new dominant state
```

## 7A. Uneven Ensemble Cover Story

Use when several relatives, staff members, neighbors or colleagues maintain one public explanation but do not possess equal knowledge or control.

```text
normal shared routine establishes each person's task
-> protagonist introduces one contradiction
-> designated speaker answers while others continue the cover story
-> one informed person reacts too early, one follows the speaker, one remains genuinely unaware
-> a silent executor waits for an authority cue
-> object, exit or information ownership exposes the command chain
```

Assign each person a separate knowledge state and repair behavior. The useful clue is not “everyone acts strange”; it is the mismatch between who should know, who reacts first, who watches whom, and who can change access. Keep the public scene functioning while private errors accumulate.

Failure boundaries:

- Synchronized staring turns social suspense into a signal that everyone is guilty.
- Identical nervous gestures erase hierarchy.
- A cover story with no practical control over doors, documents, objects or witnesses is only suspicious dialogue.

### Uneven Cover-Story Counterpart Recall

Evidence status: B-grade mechanism recall. Use social timing, knowledge distribution and control surfaces; strip donor plot and ritual rules.

| Film / scene situation | Public routine | Uneven reaction topology | Control surface / background proof | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `Get Out` - family welcome and social gathering | Hospitality, introductions, drinks, photographs and polite conversation continue | One person overperforms warmth, one watches the protagonist, another slips through an over-specific response, guests react with different delays | Door routes, phone/camera, serving tasks and who may be alone with the protagonist | Make normal hospitality the cover story and let private errors arrive through different people | Do not make every guest visibly threatening or copy the original racial/medical plot mechanism |
| `The Invitation` - dinner party maintains normality around missing information | Toasts, food service, reunion conversation and host duties remain active | Host redirects, one guest follows, one dissents, one remains socially unaware, protagonist notices before the room does | Front door, phone, wine, absent guest and who controls departures | A social event stays credible when most people keep performing ordinary tasks | Avoid having the room fall silent at the first clue; let doubt spread through a cascade |
| `Rosemary's Baby` - neighbors and professionals reinforce one explanation | Care visits, medical advice, gifts, food and concern form a benign routine | Neighbor intrudes eagerly, professional authority stays calm, partner repairs inconsistencies, protagonist receives information last | Medicine, appointment, keys, food, body access and private phone calls | Different social roles can maintain one story by controlling different needs | Strip occult lore; do not make every helper share the same acting style |
| `The Wicker Man` - community answers as if the outsider asks the wrong question | Work, school, shops, music and local ceremony continue around the investigation | Some residents answer literally, some tease, some defer to authority, children repeat learned behavior | Map, registry, transport, lodging and public gathering control access | A community cover story is strongest when daily life does not pause for the investigator | Avoid broad eccentricity as a substitute for information hierarchy |
| `Midsommar` - collective care and ritual normalize escalating control | Meals, greetings, shared work and ceremony provide orderly group rhythm | Elders initiate, peers mirror, newcomers hesitate, one outsider resists, another seeks belonging | Seating, food, sleeping space, translation and ritual timing distribute permission | Collective synchronization should have a visible source and unequal personal motives | Do not use synchronized reactions without a command/ritual cue; strip specific ceremonial lore |
| `Shutter Island` - staff and patients maintain incompatible versions of normal | Institutional routines, interviews, rounds and security continue | Staff check superiors before answering, one witness leaks fear, another follows the script, a patient may signal privately | Files, ward keys, medication, transport and weather-bound exits | Let the cover story leak through who looks at whom before speaking | Do not rely on the original identity solution; preserve only coordinated access and reaction timing |
| `The Stepford Wives` - polished domestic routine hides uniform control | Household care, parties, shopping and partner presentation appear frictionless | Public smiles remain stable while tiny timing, vocabulary or object-use repetitions expose imitation | Home ownership, appliances, clothing, clubs and partner access | Excessive perfection can be evidence when one human irregularity is missing | Avoid making every person identical in one shot; reveal the pattern through repeated behavior across encounters |
| `Speak No Evil` - politeness keeps the victim inside an unsafe social contract | Meals, parenting, guest etiquette and apologies remain plausible | Host crosses boundaries calmly, partner repairs discomfort, guest suppresses objection, child reacts without authority | Car, bedroom, food, personal belongings and departure timing | Social pressure works when the protagonist participates in maintaining the cover story | Do not confuse passivity with stupidity; show the cost and social cue behind each compromised choice |

## 8. Counterpart Retrieval

Read `motion-ecology-counterpart-atlas.md` only when the scene needs film matching or the movement logic remains generic after applying this grammar.

Route by the layer carrying new information:

| Need | Atlas pool |
|---|---|
| subject route, balance, collision or recovery | ME-A |
| listener, NPC, crowd or ensemble behavior | ME-B |
| prop ownership, machinery or foreground force transfer | ME-C |
| wind, rain, water, plants, cloth or material delay | ME-D |
| moving light, focus, camera or spatial perception | ME-E |
| off-screen sound, distance or sound-triggered reaction | ME-F |
| residual trace, aftermath or tail state | ME-G |
| multi-layer integrated staging | ME-H |
| information permission, knowledge delay or performed ignorance | ME-I |
| threshold, misdirection, progressive activation or plausible intrusion | ME-J |

Retrieve one primary mechanism and at most one supporting mechanism. Do not stack film references when one causal chain already solves the shot.

## 9. Formal Storyboard Gate

Add this field to every formal shot:

```text
运动生态/层级交互：
信息权限/知情状态：
公开行为/私下信号：
主运动：
陪体/听者：
背景人物/NPC：
前景与共享道具：
背景物件/机械：
环境力与材质响应：
光影/摄影机运动：
声音触发与可见反应：
交互后果/残留：
尾帧状态：
```

Compress quiet/simple shots to one line, but never omit the state logic.

Before finalizing, ask:

- What continues moving before the main action?
- Who can see, hear or infer each important layer, and who remains unaware or performs ignorance?
- What does the main action physically or socially affect?
- Who notices, who continues, and who reacts late?
- Which object or environmental element carries the force onward?
- What remains moving or changed after the subject stops?
- Does the background support the subject or steal attention?

## 10. SD Handoff Anchor

Preserve:

```text
primary motion + reactive layer + ambient force family + NPC state + object/material consequence + camera/focus operation + sound-triggered response + tail state
```

For dense shots, split the movement into sequential A beats. Keep stable scene geometry and environmental-force direction across the split.
