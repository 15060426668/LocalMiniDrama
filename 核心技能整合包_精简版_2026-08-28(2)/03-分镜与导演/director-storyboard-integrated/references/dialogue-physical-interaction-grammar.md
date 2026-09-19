# Dialogue And Physical Interaction Grammar

Runtime version: `1.0 / 2026-07-10`

Use this reference for people speaking while walking, turning, sitting, opening doors, handing objects, handling tools, arguing, reacting, colliding with space, stumbling, stopping or recovering balance.

## Contents

1. Core Priority
2. Dialogue Concurrency Scheduler
3. Dialogue Scene Templates
4. Physical Interaction Chain
5. Common Interaction Templates
6. Camera Response
7. Formal Storyboard Fields
8. SD Handoff
9. Failure Boundaries

## 1. Core Priority

The audience must read, in order:

```text
who owns the line
what physical task continues
who receives the line
what object/space changes
what new emotion or decision becomes visible
```

Every beat has one primary information owner. Other actions support or wait.

## 2. Dialogue Concurrency Scheduler

Track seven lanes:

| Lane | Required decision |
|---|---|
| speaking mouth | speaker, exact phrase window, mouth/jaw intensity, breath before/after |
| main body route | stand, walk, sit, turn, approach, withdraw; start and landing position |
| hand/prop | one supporting action, contact hand, object orientation, release point |
| listener | gaze, posture, hand, breath or route reaction; exact reaction window |
| background | one readable event or NPC action; dramatic relation to the line |
| camera | device, path, speed, which action triggers movement or cut |
| sound | dialogue priority, footsteps, object contact, room tone, interruption cue |

### Load Rule

One 2-4 second beat normally carries:

```text
one speaking mouth
+ one simple body route
+ one supporting hand/prop action
+ one listener reaction
+ one background event
```

Only one item is visually dominant at a time. Split when the speaker performs a large turn, collision, fall, complex handoff or second dialogue line while another major action is active.

### Phrase Window Rule

- Dense phrase: stable head/torso, natural mouth and jaw, small hand action.
- Phrase gap: larger gesture, turn, handoff, door action, sit/stand or camera move.
- Line ending: listener reaction, object landing sound, route change or cut.
- Interruption: interrupting sound/action enters first; the mouth stops; eyes and body redirect; the new speaker/action takes ownership.

### Walking Speech

```text
stable step rhythm -> short phrase -> partner glance during breath gap -> pace change -> next phrase or stop point
```

- Keep both characters on readable parallel or lead/follow routes.
- Let footfall rhythm reveal who controls the conversation.
- Place full head turns at a slowdown, doorway, corner or stop point.
- Background movement proves travel but keeps a lower visual priority than faces and route.

### Object Handoff During Dialogue

```text
speaker presents object while finishing phrase
-> receiver looks at object
-> speaker extends arm in phrase gap
-> receiver takes weight
-> original hand releases
-> object contact sound
-> receiver reacts or answers
```

Track object owner, hand, orientation, weight transfer and tail position.

## 3. Dialogue Scene Templates

### A. Seated Two-Person Dialogue

```text
speaker line + one table action
listener micro-reaction
object/silence landing
reply or cut
```

Use cup, paper, key, phone or utensil only when it changes power or information.

### B. Walk-And-Talk

```text
shared pace
-> speaker takes lead by half a step
-> listener answers while maintaining route
-> external sound/door/elevator creates stop point
-> bodies reorient for the decisive line
```

### C. Argument Escalation

```text
distance and safe boundary
-> one person crosses boundary while speaking
-> listener yields or blocks
-> hand/object contact occurs after phrase
-> silence/reaction shows consequence
```

Escalate one variable at a time: volume, distance, gesture size, object force, exit control or interruption.

### D. Phone / Remote Voice

```text
speaker listens while continuing simple task
-> remote line changes hand/task rhythm
-> eyes relocate to a real-space target
-> task stops or changes
-> spoken reply follows the physical realization
```

### E. Three-Person Dialogue

```text
one speaker
-> intended listener
-> silent third-person reaction
-> third person changes object/position
-> next speaker ownership becomes clear
```

Keep the third person active through listening, note-taking, pouring, packing, observing an exit or controlling a shared object.

### F. Dialogue While Working

```text
repeatable professional action establishes rhythm
-> speaker delivers information during familiar motion
-> one word changes the motion
-> listener notices the error or pause
-> work object becomes evidence
```

## 4. Physical Interaction Chain

Every interaction states:

```text
intention
-> force source and direction
-> contact point
-> material resistance / weight
-> primary body or object movement
-> secondary inertia
-> balance recovery or settling
-> residual mark/state
-> next action consequence
```

Physical interaction must change speed, route, posture, sound, object state, surface mark or decision.

## 5. Common Interaction Templates

### Start / Sprint

rear foot loads -> torso leans -> rear foot pushes -> first step catches weight -> arms establish rhythm -> cloth/hair follows.

### Abrupt Stop

front foot brakes -> knee bends -> torso continues forward -> arms counterbalance -> cloth/hair overshoots -> two small recovery movements -> stable tail pose.

### Stumble / Slip

foot loses friction -> center of gravity exits support base -> arms open -> hand/shoulder finds contact -> knee absorbs drop -> opposite foot restores support -> wet/dust/contact trace remains.

### Wall Contact

incoming shoulder/hand -> surface resistance -> torso compresses/rotates -> palm or forearm takes load -> camera reacts by device logic -> body leaves wall with shortened recovery steps.

### Door Push / Pull / Squeeze

hand grips handle -> wrist turns -> latch releases -> door weight moves through shoulder -> body route follows opening arc; for squeeze, shoulders rotate narrow -> palm resists moving edge -> hips clear -> clothing follows.

### Sit / Stand

sit: feet set -> hips travel back -> hand tests surface if needed -> knees bend -> seat compresses -> torso settles.  
stand: feet pull under body -> torso leans -> hands release/support -> legs extend -> clothing and chair recover.

### Pick Up / Carry / Put Down

hand tests object -> fingers secure grip -> knees/hips load according to weight -> object rises close to body -> gait changes -> placement surface receives weight -> hand releases after stability.

### Prop Handoff

presenter owns full weight -> receiver establishes contact -> weight transfers visibly -> presenter fingers release -> receiver corrects grip -> object orientation and sound continue.

### Stairs

foot finds edge -> knee absorbs vertical change -> handrail contact modifies turn -> body height rises/falls rhythmically -> landing step changes pace.

### Vehicle Acceleration / Braking

vehicle force acts on all bodies and loose props -> seat/seatbelt provides resistance -> head/equipment follows with delay -> hands stabilize -> posture recovers into the new speed state.

## 6. Camera Response

Camera behavior follows its device:

- locked-off: body enters/leaves frame; collision is proven by full spatial relation.
- handheld: small operator reaction after impact, then rapid reframing to the recovery state.
- gimbal/steadicam: route remains smooth while subject impact creates internal contrast; camera adjusts path around the obstacle.
- dolly/track: movement stays controlled; collision may trigger a stop, push or direction change only when narratively motivated.
- body-level follow: camera height and cadence respond to footfall, wall proximity and balance recovery.

The camera keeps screen direction, contact surface and exit route readable through the interaction.

## 7. Formal Storyboard Fields

For dialogue plus action, `画面内容` records:

```text
phrase owner and line window
mouth/jaw/breath
body route and footwork
hand/prop action and ownership
listener reaction timing
background action timing
sound interruption
landing pose
```

For physical contact, `机位与运镜`, `实拍摄影证据` and `画面内容` jointly record:

```text
incoming direction
contact surface/material
contact body part
resistance and deformation
camera response
secondary cloth/hair/prop movement
recovery or rest
residual mark
tail-frame state
```

## 8. SD Handoff

The SD anchor preserves:

```text
speaking character + phrase window + simple body route + one hand action + listener window + background event
```

or:

```text
force direction + contact point + resistance + body compression + camera response + secondary inertia + recovery + residue + tail state
```

Use sequential A beats when dialogue, camera, body route, handoff, collision and background event create competing dominant actions.

## 9. Institutional Multi-Person Power Dialogue

Use when a doctor, investigator, manager, family authority, patient/employee, emotionally involved relative, and silent executor compete over what may be known or done.

Design roles by control surface rather than speaking percentage:

| Functional role | Power carrier | Blocking proof |
|---|---|---|
| Authority | document, key, diagnosis, schedule, exit permission | owns the table/door axis and decides who may inspect or leave |
| Challenger/protagonist | contradiction, testable question, route | shifts gaze between hands, objects, witnesses, and exit before speaking |
| Emotionally involved relative | memory, guilt, intimacy, social pressure | tries to close distance, touch, interrupt a handoff, or reclaim an object |
| Silent executor/witness | medication, tray, restraint, device, doorway | waits for a permission cue; delayed action reveals the real command chain |

Beat grammar:

```text
authority defines the frame
-> protagonist identifies a testable contradiction
-> relative changes emotional distance or object ownership
-> silent executor waits, acts, or refuses after reading authority
-> exit/object/information permission visibly changes
```

Every line must alter permission, ownership, alliance, testability, or the next physical action. Keep listener tasks and background routines active. Calm delivery is not automatically power; power must be proven through access, custody, information, or coordinated response.

## 10. Procedural Debrief Under Contradictory Residue

Use when a character returns from an impossible event to an institution that expects a clean report.

```text
professional intake routine begins
-> authority fixes the official sequence and controls the record
-> protagonist supplies one physical residue that does not fit
-> witness/executor checks procedure rather than emotion
-> document, object or body state contradicts the spoken account
-> the room redistributes access, custody or credibility
```

Block the scene through report ownership, evidence placement, chair/door relation, recording device, observer position and who may interrupt the intake. Preserve professional behavior: the protagonist may be shaken, but still selects a testable contradiction. The authority may doubt the story while treating the residue seriously.

Failure boundaries:

- A debrief that only recaps plot has no present-tense conflict.
- Instant belief or instant dismissal removes institutional tension.
- Evidence must change custody, route or permission before the scene ends.

### Procedural Debrief Counterpart Recall

Evidence status: B-grade mechanism recall. Extract authority, evidence and blocking relations only; do not treat dialogue, timing or shot order as verified.

| Film / scene situation | Institutional control surface | Blocking and camera relation | Contradictory residue / information | Transferable rule | Failure boundary |
|---|---|---|---|---|---|
| `Annihilation` - quarantine interrogation after return | Glass, protective clothing, recording, medical access and who may approach | Returned subject is isolated while questioners remain protected or partly unseen; camera alternates embodied residue with institutional observation | Memory gaps, altered body/evidence and a survivor state that does not fit the expected team outcome | Separate “do they believe her?” from “how must they handle her?”; procedure can act before belief | Do not copy the expedition lore or reduce the scene to plot recap |
| `Arrival` - military/linguistic review of contact evidence | Screens, recordings, translation notes, chain of command and access to the contact zone | Specialist, commander and technical staff occupy different distances from the evidence; screen content mediates authority | Meaning changes after a translation/recording is re-read, shifting permission to act | Let interpretation become a physical power change: access, playback, door or command | Avoid interface exposition; one linguistic contradiction should change the room |
| `Solaris` - reports and recordings confront lived experience | Archived testimony, station rules, monitor playback and scientific status | Present observer watches an earlier report or another witness while the environment quietly contradicts institutional categories | Recorded account and current embodied presence cannot both fit the official model | A debrief can use media from another time to pressure the current witness | Do not import planetary metaphysics; keep the conflict on evidence ownership and response |
| `Contact` - official hearing after an unverifiable event | Microphones, panel seating, public record, classified data and credibility | Witness is centered and exposed; authorities share a horizontal power block; hidden evidence remains outside her reach | Subjective duration conflicts with public evidence, while restricted data complicates dismissal | The institution may publicly deny while privately retaining contradictory evidence | Do not make the hearing a speech contest; show who controls records and what action follows |
| `The Thing` - blood test as group procedure under mistrust | Test tool, sample ownership, restraint, seating and who performs the procedure | Group is spatially locked; the tester controls sequence, distance and release while every result redistributes threat | A physical reaction overrides statements and alliances | When testimony is useless, a controlled test can become the debrief | Strip creature specifics; preserve test ownership, witness order and immediate permission change |
| `The Invisible Man` - institutional disbelief against bodily/material evidence | Medication, confinement, surveillance, diagnosis and visitor permission | Authority owns the room and exit; protagonist must use visible residue or device behavior rather than escalating speech | Marks, object movement or timing conflict with the official psychological explanation | Let material evidence force procedure to change before it forces belief | Avoid making authority foolish; give them rational constraints and a concrete point of failure |
| `Shutter Island` - investigator questions an institution that controls the environment | Files, staff access, locked wards, weather/transport and interview permission | Interviewees are framed within institutional geometry; staff read one another before answering | Missing records, coordinated phrasing and behavior reveal that the questioner lacks full permission | Debrief and interrogation can reverse when the institution owns every exit and witness | Do not import the identity resolution; focus on answer coordination and access control |
| `Ex Machina` - controlled sessions and private reporting | Session logs, glass rooms, keycards, cameras and private observation | Formal conversation occurs in one space while interpretation/reporting occurs in another; camera and glass divide public/private knowledge | The subject's behavior and the official test objective diverge | Separate event, observation and report into three ownership layers | Avoid copying AI lore; preserve who is observed, who writes the meaning and who controls the door |

## 11. Failure Boundaries

- Continuous mouth movement paired with multiple large body actions produces unreadable performance.
- Generic “walks while talking” lacks pace, lead/follow relation, footfall and stop point.
- A prop handoff without visible weight transfer breaks ownership continuity.
- A collision without recovery and residual state feels weightless.
- Camera shake without a contact event or device logic reads as arbitrary instability.
- Frozen listeners and background figures flatten dialogue scenes; give them one subordinate task tied to the line.
- Fixed speaking ratios, generic shot/reverse-shot, and constant interruption hide the institutional power structure.
