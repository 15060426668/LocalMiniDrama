# Sound Design Grammar

Use this reference when the task mentions sound design, 音效, 声场, 声画关系, 画外声, 静音, 声音转场, dream sound, hallucination sound, dialogue sound, or when a storyboard sound column feels thin.

## Table Of Contents

1. Core sound law
2. Sound design workflow
3. Seven-stem sound field
4. Five director sound grammars
5. Suspense sound vocabulary
6. Transferable templates
7. Failure boundaries

## 1. Core Sound Law

Suspense sound is not "add scary noise". It controls the viewer's imagination, safety, body response, and sense of time.

For numerical execution, combined levels, delivery profiles, spatial processing and post handoff, also read `sound-mix-metering.md`. Never write a bare dB value without a metering unit.

For film-mechanism matching of listening, off-screen worlds, subjective hearing, sound-image mismatch and sync reconstruction, read `sound-spatial-sync-counterpart-atlas.md`. This grammar remains the canonical rule source; the atlas does not duplicate the rules below.

Rules:

- unseen sound is stronger than seen sound. A source outside the frame lets the audience imagine danger.
- sound change is stronger than sound itself. A stable room tone that drops, swells, distorts, or disappears creates the hook.
- information gap is the engine. Let the audience hear danger before the character understands it.
- silence is not empty. It is an active removal of information and can be the loudest beat.
- fewer sounds are stronger. One precise sound with clear purpose beats a pile of generic effects.
- sound must belong to a source, a mind, a structure, or a transition. Do not add sound only for atmosphere.

## 2. Sound Design Workflow

Use this four-step workflow for every suspense sound plan.

### Step 1: Define The Sound Task

Choose one main task:

- known danger anxiety: the audience hears danger before the character.
- uncanny wrongness: a familiar everyday sound becomes subtly strange.
- cold procedural pressure: realistic room/city/system sounds slowly press down.
- time pressure: ticking, pulse, riser, or layered rhythm makes time physical.
- delayed rupture: relaxed daily sound prepares a sudden violent change.
- subjective collapse: hearing narrows, distorts, mutes, or floods as the character breaks.

### Step 2: Build Stems

Audit all seven stem families, then activate only those serving the beat:

```text
ENV -> BODY -> OBJ -> VOX -> FX -> INT -> MUS
```

Do not force every stem to play. A short beat usually carries 2-5 active stems and one primary sound source.

### Step 3: Design Changes

Every sound plan needs change points:

- what appears earlier than the image.
- what grows closer or farther.
- what drops out.
- what becomes subjective.
- what becomes the transition bridge.
- what remains after the visual action ends.

### Step 4: Meter And Route

For formal storyboards, assign:

```text
primary source + active bus IDs + position/distance
-> per-stem RMS dBFS / peak dBFS / relative dB
-> frequency, occlusion, RT60 and dry/wet
-> ducking/masking
-> shot LUFS-S + delivery LUFS-I/dBTP
-> visible reaction + sound bridge
```

Use logarithmic energy summation from `sound-mix-metering.md`; never add dB values linearly.

## 3. Seven-Stem Sound Field

Use these seven routed families when writing formal storyboard sound columns. Off-screen, visible, subjective and structural are source-status tags, not substitutes for a bus.

### 1. ENV: Environment And Room Tone

Purpose: establish space and baseline unease.

Examples:

- low-frequency drone, industrial hum, room tone.
- white/pink noise in empty rooms.
- air conditioner, refrigerator current, fluorescent buzz.
- rain on glass, rain on metal, city white noise.
- wind through a crack, hallway echo, old building creak.
- water pipe rumble, hollow drip, distant traffic.

Writing rule:

```text
room tone source + spatial distance + texture + emotional pressure
```

Example:

```text
The room carries a thin refrigerator hum from the far right, mixed with a dry fluorescent buzz overhead; both stay low, almost below attention, making the normal apartment feel electrically stale.
```

### 2. BODY: Subject And Body Foley

Purpose: make the body and performance physically close.

Examples:

- breath, swallowed saliva, heartbeat, fabric rustle.
- bare feet, shoes, knees, palms and body contact.
- cloth drag, coat inertia, bedding friction and breath through teeth.
- body impact, recovery step and residual tremor.

Writing rule:

```text
specific body/wardrobe sound + closeness + rhythm + what physical state it exposes
```

### 3. OBJ: Object And Mechanical Sound

Purpose: give props, clues, rules and machines material causality.

Examples:

- key and lock movement, latch, cup, drawer, paper, phone vibration.
- elevator motor, monitor, fan, vehicle, medical device, screen relay.
- object impact, scrape, roll, flex, fracture or settling resonance.

Writing rule:

```text
material/object + contact or mechanism + weight + rhythm + decay
```

### 4. VOX: Dialogue And Voice

Purpose: carry language, authority, information permission and social distance.

Include:

- visible dialogue and lip-sync owner.
- off-screen speech, whisper, phone, radio, public address and NPC voices.
- who hears, ignores, misreads or is excluded.
- phrase window, emphasis, breath, interruption and J/L-cut.

An off-screen unknown sound is routed by its physical family: a footstep is BODY, a lock is OBJ, a whisper is VOX. Its `off-screen` status and delayed visual proof create suspense.

### 5. FX: Designed And VFX Sound

Purpose: make animation, energy, digital failure and impossible material change feel causal and scaled.

Writing rule:

```text
visible trigger -> first audible change -> material/geometric development -> landing impact/residue
```

Match the sound to the changing matter: liquid, fragments, particles, smoke, digital, biological, cloth/paper or fold/mirror. The FX stem owns attention only while the visible change boundary is moving.

### 6. INT: Subjective/Internal

Purpose: enter the character's body or unstable perception.

Examples:

- tinnitus, muffled underwater hearing, ear pressure.
- heartbeat covering other sounds.
- breath becoming too loud.
- distorted familiar voice, reversed speech, slowed voice.
- granularized memory fragments, sound montage.
- blood rush, panic pulse, dream-layer low frequency.

Writing rule:

```text
external sound thins -> internal sound rises -> audience enters the character's sensory state
```

Impacts are routed to BODY, OBJ, FX or INT according to source. Silence is a deliberate automation event that states which buses are removed, which residual room tone remains, and when sound returns.

### 7. MUS: Music / Tonal Layer / Structural Silence

Purpose: guide structure, mark threshold/release, or create a controlled withdrawal of the sound field when source layers are not enough.

Examples:

- unresolved chord, dissonant interval, repeated ticking motif.
- Shepard tone, atonal texture, contrast song or sparse pulse.
- brake-cut or partial bus withdrawal before a reveal.
- residual room tone after dialogue, FX or music drops.

Writing rule:

```text
tonal/structural function + exact entry/exit + which buses withdraw + residual room tone + release point
```

Use sparingly. Frequent stingers cheapen suspense. Music should not explain emotion that the scene can express through space, breath, objects, and room tone.

## 4. Five Director Sound Grammars

Use one primary grammar. Borrow at most one secondary device if it solves a specific beat.

### Hitchcock: Information Gap Sound

Core equation:

```text
audience hears danger before character = anxiety
```

Use for psychological suspense, object anxiety, door/window/room threat, voyeur listening, delayed reveal.

Tools:

- repeated everyday danger cue: ticking, phone ring, bird call, door sound.
- off-screen threat sound with no source cut.
- silence before reveal or attack.
- POV listening: the audience hears what the character hears, then knows slightly more.
- reaction after sound: hold on the face instead of cutting to source.

Sound column should include:

```text
danger cue source + who hears it + who ignores it + how long before visual proof + silence/reaction beat
```

Failure:

- cue too loud or obvious.
- showing the source immediately.
- danger and sound arrive at the same time, erasing suspense.
- using silence constantly until it loses power.

### Lynch: Familiar Sound Made Wrong

Core equation:

```text
ordinary sound + subtle wrongness = uncanny reality leak
```

Use for dream, hallucination, identity drift, ordinary room turning wrong, reality collapse.

Tools:

- very low industrial drone or electrical hum.
- familiar sounds slowed, pitched, reversed, stretched, or distorted just enough to feel wrong.
- sound-image mismatch: sunny room with underground machinery, smiling face with wrong voice.
- sourceless whisper, wall friction, impossible train or wind.
- sound continues after visible source stops, or disappears while the action continues.

Sound column should include:

```text
normal source -> subtle deformation -> source uncertainty -> emotional wrongness
```

Failure:

- making the effect too obvious.
- piling random strange noises.
- explaining the sound source too early.
- losing the normal baseline before the wrongness arrives.

### Fincher: Cold Environmental Pressure

Core equation:

```text
realistic sound source + controlled discomfort = system pressure
```

Use for crime, evidence, institutions, interrogation, apartments, marriage traps, offices, hospitals, procedural suspense.

Tools:

- distorted but realistic city bed: slowed train brake, rain on glass, HVAC, fluorescent hum.
- small high-frequency irritants: metal scrape, electric hiss, paper friction.
- no music in key discovery/dialogue scenes; use micro foley and breath.
- cold electronic pulse with no melody when system pressure rises.
- spatial separation: outside world far and muffled, room sounds dry and close.

Sound column should include:

```text
real source + texture + distance + small discomfort + what detail becomes louder under pressure
```

Failure:

- generic scary sound with no real source.
- sound bed too loud or too busy.
- cold style pasted onto scenes that need intimacy.
- darkness of sound with no information hierarchy.

### Nolan: Time And Structure Sound

Core equation:

```text
abstract rule/time becomes audible = structural pressure
```

Use for countdown, nested dream, rule-based sequence, mission, loop, memory/time distortion, large-scale pressure.

Tools:

- tick/tock, watch, metronome, pulse, machine rhythm.
- Shepard tone or endless riser for unresolved pressure.
- low-frequency pulse for deeper layer or heavier rule.
- sound pre-lap from next space/time layer.
- music or sound motif slowed/stretched to signal layer change.

Sound column should include:

```text
which rule/time layer has which sound marker + how the marker changes + where release occurs
```

Failure:

- using Shepard tone as decoration.
- no release point.
- no different marker for different layers.
- sound structure is more complex than the audience can read.

### Tarantino: Contrast And Delayed Rupture

Core equation:

```text
relaxed everyday sound + sudden dry rupture = delayed violence
```

Use for dialogue pressure, dinner/bar/closed-room standoffs, etiquette hiding danger, absurd violence.

Tools:

- needle drop: light old song or pop song against threat/violence.
- hyper-clear daily foley: cup, boot, chair, chewing, fabric, gun metal.
- conversational bed that suddenly thins.
- tiny danger click inside relaxed chatter.
- violence sound is dry, sudden, and short; after it, return to daily sound or dead silence.

Sound column should include:

```text
relaxed social sound -> tiny danger sound -> pause -> dry rupture -> immediate contrast after
```

Failure:

- making the scene ominous too early.
- slow-motion or over-processed violence sound.
- daily sounds not specific enough.
- contrast song chosen without story irony or rhythm function.

## 5. Suspense Sound Vocabulary

Use vocabulary as functional choices, not decoration.

### Environment Bed

- low-frequency drone / industrial hum: subconscious unease.
- infrasound: physical anxiety, use sparingly.
- room tone: isolation, trapped realism.
- white/pink noise: masked information, empty space.
- wind howl: outside threat, lonely corridor.
- pipe rumble: hidden building interior.
- mains hum / fluorescent buzz: faulty civilization, institutional pressure.
- rain on glass/metal: cold city pressure.
- old floor/door creak: house as living witness.
- insect or bird bed made unnatural: peaceful surface with hidden rot.

### Tension Build

- riser: something is coming.
- Shepard tone: release denied.
- tick/tock: time made physical.
- heartbeat: body alignment.
- breath: intimate panic or hidden presence.
- string glissando: nervous alarm.
- metal tremor: one-touch rupture.

### Impact

- stinger / hit: short shock.
- impact: physical blow.
- brake cut: all sound stops, brain blank.
- reverse reverb: inhaled supernatural pull.
- record scratch: reality/rhythm interruption.
- scream design: nonhuman fear.
- silence hit: post-impact void.

### Space Clues

- distant whisper: watched, uncertain presence.
- footstep echo: scale, approach, pursuit.
- door creak: secret opening.
- floorboard creak: someone else is there.
- water drip: empty time and erosion.
- key turn: entry, trap, loss of control.
- glass break: boundary breach.

### Psychological Distortion

- pitch shift: familiar becomes alien.
- granularization: memory/world fragmentation.
- binaural beat: altered consciousness.
- disembodied sound: impossible source.
- tinnitus ring: shock or breakdown.
- distortion/saturation: reality overload.
- audio montage: memory flash, mental clutter.

## 6. Transferable Templates

### Off-Screen Threat Template

- environment: low room tone, realistic and thin.
- near foley: breath or hand sound becomes close.
- off-screen: one sound appears from door, wall, window, or upstairs.
- camera: stay on character or empty space; do not show source immediately.
- change: room tone drops before the next sound.
- best use: door approach, hallway, hidden room, apartment, night home.

### Invisible-Presence Causal Proof Template

- baseline: establish an empty but geographically readable room with stable room tone and visible materials.
- first proof: one body-scale sound occurs at a precise location: floor compression, chair load, mattress spring, breath displacement, fabric brush or wet step.
- material response: the visible object reacts with plausible force, weight and delay; sound and movement share the same contact point.
- position continuity: the unseen body cannot jump randomly. Each new sound or object response must follow a possible route through doors, floor zones, furniture gaps or air movement.
- character test: powder, water, hanging fabric, reflected light, loose paper, steam or a movable object is introduced to convert sound into partial visual evidence.
- social pressure: another person may hear only the visible disturbance or the character's reaction, creating doubt without erasing the physical evidence.
- landing: preserve a displaced object, footprint, compressed surface, wet trace, open latch or continuing breath position.
- best use: invisible pursuer, empty-room coercion, unseen domestic intruder, presence that others refuse to believe.

### Behavioral Entrainment Template

- neutral cue: begin with a plausible repeated sound belonging to the place: bell, ventilation pulse, spoken response, work rhythm, exercise count, appliance cycle or public-address phrase.
- first synchronization: one body's breathing, hand motion, gaze or posture begins matching the cue.
- group spread: synchronization moves through people at different delays; do not make everyone snap into identical action at once.
- permission shift: the cue starts deciding when people sit, speak, eat, stop, turn or cross a threshold.
- break attempt: one character interrupts, leaves the rhythm, blocks the source or introduces a personal counter-sound.
- consequence: the room, group or system reacts to the desynchronization through gaze, route closure, repeated phrase, changed volume or renewed timing.
- residue: after escape or silence, the character retains a breath cadence, phrase fragment, hand rhythm or involuntary response.
- best use: ritual pressure, institutional conditioning, workplace conformity, cult-like group behavior, hypnotic daily routine.

### Uncanny Everyday Template

- environment: familiar appliance/room tone.
- deformation: one daily sound is subtly slowed, pitched, or stretched.
- mismatch: the visible source does not fully explain the sound.
- subjective: character pauses, hearing narrows.
- change: the sound continues half a beat after the source stops.
- best use: dreams, false awakening, hallucination, perfect home becoming wrong.

### Cold Evidence Template

- environment: HVAC, rain, fluorescent buzz, city hum.
- near foley: paper, keyboard, phone, pen, breath.
- off-screen: distant institution sound, elevator, printer, traffic, machine.
- music: none or nearly none.
- change: as truth appears, background falls away and tiny evidence foley grows.
- best use: investigation, interrogation, hospital, file review, crime apartment.

### Time Pressure Template

- environment: neutral bed or machine room.
- motif: ticking, pulse, clock, monitor, repeating object sound.
- structure: motif changes speed/weight with the rule.
- transition: next scene sound enters early.
- release: the motif stops, lands, or drops at the reveal.
- best use: countdown, nested dream, rule card, mission, loop, memory fracture.

### Delayed Rupture Dialogue Template

- environment: social daily sound, room chatter, cutlery, cup, chair.
- near foley: one small object sound gets too clear.
- danger cue: a click, metal touch, silence in conversation.
- change: chatter thins or stops for 1-3 seconds.
- rupture: one dry gunshot, slap, glass break, or door slam.
- aftermath: return to song/chatter or leave dead silence.
- best use: dining table, bar, family argument, negotiation, domestic standoff.

## 7. Failure Boundaries

- Do not make the sound column only "environment sound + music". Write layers, sources, distance, and change.
- Do not fill every shot with music. Suspense needs air.
- Do not use jump scares as the default solution.
- Do not use a sound with no source, no psychological rule, and no transition function.
- Do not make all sound equally loud and equally close.
- Do not explain off-screen sound too quickly.
- Do not make danger cues too clear too early.
- Do not copy a director's signature sound without the matching suspense task.
- Do not let dialogue freeze the sound world; listener foley, room tone, background, and off-screen pressure continue or change.
- Do not ignore sound continuity in transitions; sound can bridge time, space, memory, and hallucination more cleanly than a hard cut.
- Do not prove an invisible body with unrelated random object motion. Sound position, contact force, visible response and subsequent route must belong to one continuous physical owner.
- Do not reduce behavioral conditioning to an unsupported exact frequency. The mechanism is repeated cue, bodily synchronization, social permission and residue; Hz values require a real source and production reason.
