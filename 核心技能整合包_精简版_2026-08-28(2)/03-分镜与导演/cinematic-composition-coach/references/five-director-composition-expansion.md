# Five-Director Composition Expansion

Updated: 2026-06-25

Purpose: expand the composition coach with researched, reusable composition systems for Hitchcock, David Lynch, David Fincher, Christopher Nolan, and Quentin Tarantino. Routine execution routes through `director-storyboard-integrated`.

Use this file when the user asks for:

- "top director composition"
- "five director storyboard skill"
- "large-scale web search for composition examples"
- "why does this frame feel ordinary"
- SD / Seedance prompts that need director-level composition logic

Do not copy public-facing style labels into final prompts. Translate each director reference into visible facts: camera position, object hierarchy, light direction, spatial layers, sound logic, edit timing, and body blocking.

## Research Anchors Used

- Hitchcock / Notorious key crane: Criterion, `How Hitchcock Pulled off a Shot for the Ages`, https://www.criterion.com/current/posts/6156-how-hitchcock-pulled-off-a-shot-for-the-ages
- Hitchcock / Notorious story context: Cinephilia & Beyond, https://cinephiliabeyond.org/notorious-hitchcocks-mature-intricate-espionage-masterpiece/
- Hitchcock / Psycho voyeurism and montage: BFI, `10 things you probably never knew about the shower scene in Psycho`, https://www.bfi.org.uk/interviews/psycho-shower-scene-alfred-hitchcock
- Lynch / Blue Velvet: American Cinematographer, `Blue Velvet - Small Town Horror Tale`, https://theasc.com/article/flashback-blue-velvet/
- Lynch / Blue Velvet updated ASC wrap shot: https://theasc.com/article/wrap-shot-blue-velvet/
- Fincher / Zodiac: American Cinematographer, `Zodiac: Cold Case File`, https://theasc.com/article/flashback-zodiac/
- Fincher / Zodiac workflow: ICG Magazine, `Harris Savides, ASC uses a new workflow for Zodiac`, https://www.icgmagazine.com/2007/march/march07.html
- Fincher / The Game: American Cinematographer, `AC Gallery: The Game`, https://theasc.com/article/ac-gallery-the-game/
- Nolan / Inception: American Cinematographer, `The Cinematography of Inception`, https://theasc.com/article/inception-cinematography-pfister-nolan/
- Nolan / Inception practical hallway context: British Cinematographer, https://britishcinematographer.co.uk/wally-pfister-asc-inception/
- Nolan / Oppenheimer large-format intimacy: Kodak, https://www.kodak.com/en/motion/blog-post/oppenheimer/
- Nolan / Oppenheimer sound: A Sound Effect, https://www.asoundeffect.com/oppenheimer-film-sound/
- Tarantino / The Hateful Eight: American Cinematographer, `Wide Wide West`, https://theasc.com/article/wide-wide-west-the-hateful-eight/
- Tarantino / The Hateful Eight roadshow / Ultra Panavision context: Wired, https://www.wired.com/2015/12/hateful-eight-roadshow-tech/

## Director Composition Dispatch

| Director module | Composition engine | What owns the frame | Best use in AIGC prompts | Failure to avoid |
|---|---|---|---|---|
| Hitchcock | controlled information and gaze | object, barrier, POV, reaction | lock object hierarchy, viewer knowledge, reveal order | generic dark danger |
| Lynch | ordinary space becoming wrong | sound, threshold, texture, face, empty room | define stable normality, then one measurable drift | random surreal decoration |
| Fincher | system pressure and evidence | architecture, screen, file, lightable space | use exact camera discipline, clear evidence inserts | "cool darkness" with no information function |
| Nolan | physicalized abstract rule | clock, vehicle, gravity, large-format human anchor | teach rule before complexity; use physical thresholds | scale without emotional cost |
| Tarantino | social rhythm before rupture | table, hand, drink, gesture, music, ensemble geometry | preserve room geography and dialogue pressure | starting violence or pose before pressure matures |

---

## Case FD01 - Hitchcock: Notorious Macro-To-Micro Object Descent

**Narrative Layer**

- Emotion tone: social elegance hiding private panic.
- Character relationship: one character carries the secret while the public room remains unaware.
- Plot node: a tiny object controls a large espionage danger.
- Narrative function: compress the audience's attention from the whole party to the single object that truly matters.

**Visual Layer**

- Shot size: begins as high wide / ballroom overview, ends as extreme object close-up.
- Camera position: crane or jib starts above the social room, descends through the crowd axis, and lands at hand height.
- Composition rules: macro-to-micro compression, center-guided movement, crowd-as-camouflage, object-as-visual climax.
- Lighting: public room remains evenly social; the object needs a readable small highlight, not a glow.
- Color: social warmth can stay broad, while the key/object receives a tighter metallic or hard-edge glint.
- Spatial layers: foreground crowd movement, midground secret carrier, background party activity that does not know the danger.

**Language Layer**

- Prompt sentence: `Start from a high overhead view of a crowded elegant public room, then the camera descends through the moving crowd and narrows attention to one character's hand holding a small hidden object; the room stays socially alive while the object becomes the only sharp focal point.`
- Keywords: `high crane descent`, `crowd camouflage`, `secret object close-up`, `public room unaware`, `macro-to-micro suspense`.
- Visible AIGC anchors: say where the camera starts, where it ends, which hand holds the object, what the crowd is doing, and how focus transfers.

**Replication And Use**

- Why it works: it makes the camera behave like intelligence. The audience is told what matters without dialogue.
- How to use: put the object at the endpoint of a real camera journey; do not cut to the object too early.
- Best scenes: ring-box opening, phone message discovery, key / Nixie tube / receipt / coffee clue, public-space secret.
- Risk and anti-example: if the prompt only says "dramatic close-up of object", the macro social pressure disappears.

**Knowledge Entry**

- Reusable rule: when a small prop controls a large danger, first prove the large world, then let the camera physically reduce the world to the prop.

---

## Case FD02 - Hitchcock: Voyeur Barrier And Fragmented Attack Rhythm

**Narrative Layer**

- Emotion tone: private safety is invaded.
- Character relationship: viewer becomes watcher before becoming helpless witness.
- Plot node: a visual barrier hides the threat until the character is too late.
- Narrative function: transform a normal domestic act into audience complicity and shock.

**Visual Layer**

- Shot size: objective safe medium shots, barrier / peephole / curtain inserts, sudden close fragments, aftermath stillness.
- Camera position: first outside the character's awareness, then bound to the invasion line, then pulled into dead object / face / water detail.
- Composition rules: frame-within-frame, voyeur aperture, object barrier, montage fragmentation, aftermath hold.
- Lighting: practical bathroom / room light should feel ordinary before it turns exposed and hostile.
- Color: clean neutral reality; if black-and-white or desaturated, use contrast and texture as emotional violence.
- Spatial layers: barrier in foreground, vulnerable body in midground, threat emerging from background or edge.

**Language Layer**

- Prompt sentence: `A private ordinary action is framed through a partial visual barrier; the viewer sees the threat enter before the character does, then the attack is expressed through fast fragments of hand, object, water, curtain, face, and sound, followed by a long still aftermath shot.`
- Keywords: `visual barrier`, `audience sees first`, `voyeur frame`, `fragmented montage`, `aftermath stillness`.
- Visible AIGC anchors: specify barrier material, threat entry side, reaction delay, fragment list, and post-event object.

**Replication And Use**

- Why it works: the terror comes from knowledge timing, not from showing everything.
- How to use: let a phone screen, glass door, display case, CCTV monitor, shower curtain, window blind, or ring-box lid become the barrier.
- Best scenes: public accident before character notices it, stalker POV, message arriving unseen, off-screen vehicle threat.
- Risk and anti-example: if the threat and character discover the event together, the Hitchcock information gap collapses.

**Knowledge Entry**

- Reusable rule: suspense requires a timed imbalance between audience knowledge and character knowledge. Write the imbalance into the frame, not just the plot.

---

## Case FD03 - Lynch: Clean Surface / Rotten Underworld Split

**Narrative Layer**

- Emotion tone: pretty normality hiding contamination.
- Character relationship: the subject is not attacked by a villain first; the location itself becomes morally suspicious.
- Plot node: a friendly public or domestic surface begins to reveal a hidden layer.
- Narrative function: make the audience distrust beauty before the story explains why.

**Visual Layer**

- Shot size: composed wide or medium-wide surface view, followed by lower / closer detail that violates the postcard surface.
- Camera position: calm and frontal at first; then lower, slower, or more invasive as it enters the hidden layer.
- Composition rules: surface / underside contrast, vertical descent, bright order vs dark pocket, object threshold.
- Lighting: top world uses clean daylight or warm domestic light; underworld uses thick shadow, low practicals, sickly amber, or black zones that retain detail.
- Color: saturated ideal colors above; corrupted red, blue, amber, or fleshy tones below.
- Spatial layers: foreground ideal sign / fence / flower / counter; midground human routine; background or lower layer carries the abnormal clue.

**Language Layer**

- Prompt sentence: `Begin with a clean, almost postcard-like small-town or public-space composition, then move lower and closer until the same space reveals dark soil, insects, damaged fabric, hidden machinery, or a human trace that makes the ordinary location feel wrong.`
- Keywords: `clean surface`, `hidden rot`, `ordinary made wrong`, `low slow reveal`, `shadow pocket`.
- Visible AIGC anchors: name the normal layer first, then the exact corrupt detail; do not just write "surreal".

**Replication And Use**

- Why it works: dread is stronger when the frame first earns trust.
- How to use: for the user's cafe / lab / wedding-store scenes, first establish polished normal commerce, then reveal the small object or sound that should not belong.
- Best scenes: ring-store cold open, cafe table with wrong message, normal hallway that starts humming, sweet dialogue with a hidden threat.
- Risk and anti-example: starting already weird removes contrast; random symbols without a stable normal anchor read as noise.

**Knowledge Entry**

- Reusable rule: Lynch-style composition needs a stable ordinary surface and one precise violation. No violation, no dread; no surface, no contrast.

---

## Case FD04 - Lynch: Corridor / Threshold Dissolution

**Narrative Layer**

- Emotion tone: identity drift, dream pressure, memory instability.
- Character relationship: the character is being pulled by a room, hallway, box, door, or sound rather than by another person.
- Plot node: crossing a threshold changes the rules of reality.
- Narrative function: make the audience feel the threshold before explaining it.

**Visual Layer**

- Shot size: medium-wide corridor or room axis, then slow push / track into a doorway, box, mirror, lamp, or face.
- Camera position: aligned to the corridor / threshold so the vanishing point becomes a psychological suction point.
- Composition rules: one-point pull, deep dark endpoint, repeated door geometry, static-to-sudden movement break.
- Lighting: a single top / camera-side or practical source can keep the near space readable while the far end disappears.
- Color: blue-black, sick amber, or red should belong to a threshold object, not flood the whole frame without reason.
- Spatial layers: foreground wall / doorframe, midground figure, background black endpoint or glowing object.

**Language Layer**

- Prompt sentence: `A quiet corridor holds still with one readable vanishing point; the camera pushes so slowly it feels almost unconscious, the far end remains darker than the eye can resolve, and a single object or doorway begins to hum before the frame breaks into a faster subjective move.`
- Keywords: `slow threshold push`, `dark endpoint`, `room-tone dread`, `one-point corridor`, `sound before image`.
- Visible AIGC anchors: define corridor direction, threshold object, hum source, exposure falloff, and what changes after crossing.

**Replication And Use**

- Why it works: it turns architecture into mental pressure.
- How to use: assign one measurable drift: hum grows, exposure drops, saturation changes, focus breathes, door repeats, or shadow deepens.
- Best scenes: time-machine room, white tower corridor, memory overwrite, identity-swap anxiety, dream-like SMS transition.
- Risk and anti-example: a hallway with generic fog and red light is not enough; the threshold needs a rule and a trigger.

**Knowledge Entry**

- Reusable rule: a Lynch threshold shot must define normal geometry, then let one sensory variable drift until space stops feeling reliable.

---

## Case FD05 - Fincher: Zodiac Mundane Truth And Exposition Space

**Narrative Layer**

- Emotion tone: procedural obsession, truth buried in ordinary rooms.
- Character relationship: characters are trapped by facts, systems, jurisdictions, files, phone calls, and the impossibility of confirmation.
- Plot node: exposition-heavy investigation must remain visual without becoming theatrical.
- Narrative function: make the audience feel how much information exists and how little certainty it gives.

**Visual Layer**

- Shot size: restrained medium-wide rooms, clear inserts, static / precise dialogue coverage.
- Camera position: objective, patient, often at human working height; avoids emotional showboating.
- Composition rules: space-lit environment, evidence planes, desks and files as information architecture, negative confirmation.
- Lighting: light the room so characters can inhabit it; simple motivated instruments, darkness preserving detail rather than crushing it.
- Color: muted office greens, browns, paper whites, gray-blue nights; no glamorous serial-killer contrast if the scene needs truthfulness.
- Spatial layers: foreground file / phone / desk edge, midground investigators, background shelves, windows, maps, or institutional clutter.

**Language Layer**

- Prompt sentence: `A restrained investigation room lit as a believable working space, with files, phone, map, and desk edges forming evidence planes; the camera stays precise and patient while characters process information that remains incomplete.`
- Keywords: `truthful mundane room`, `evidence planes`, `simple motivated lighting`, `objective camera`, `information without certainty`.
- Visible AIGC anchors: name evidence objects and where they sit; specify darkness has readable detail.

**Replication And Use**

- Why it works: the room becomes the trap. The composition says: all facts are present, but none are enough.
- How to use: treat whiteboards, phone UI, inbox, D-mail limit, microwave connection, and Nixie value as evidence planes.
- Best scenes: lab rule explanation, message investigation, timeline proof, police-like deduction, character comparing evidence.
- Risk and anti-example: stylized blue darkness or random fast cutting will make evidence unreadable and destroy procedural pressure.

**Knowledge Entry**

- Reusable rule: for evidence scenes, light and compose the space as a working system before pushing in on faces.

---

## Case FD06 - Fincher: Lens / Furniture / System Precision

**Narrative Layer**

- Emotion tone: controlled intimacy under institutional manipulation.
- Character relationship: the room and furniture force people into a specific power distance.
- Plot node: a seemingly normal meeting is actually a system tightening around someone.
- Narrative function: prove control through physical design choices, not just dialogue.

**Visual Layer**

- Shot size: medium two-shot, table geometry, controlled close-ups, clean inserts.
- Camera position: fixed or precise dolly; the camera feels planned, not reactive.
- Composition rules: table compression, institutional symmetry, object center, fixed lens logic.
- Lighting: soft toplight or controlled modern practical light; no random glamour spill.
- Color: controlled corporate / legal / institutional palette; muted contrast with one object or face highlight.
- Spatial layers: table as foreground plane, characters close in midground, institutional background framing them.

**Language Layer**

- Prompt sentence: `A controlled meeting scene where the table size, lens compression, and camera height force the two people close together; the room looks polished but slightly predatory, with clean practical toplight and one central document or device acting as the system's trap.`
- Keywords: `precise lens logic`, `compressed table geometry`, `institutional trap`, `fixed camera discipline`, `central evidence object`.
- Visible AIGC anchors: define table width, seating distance, lens range, central object, and whether the camera moves or stays locked.

**Replication And Use**

- Why it works: the scene feels designed against the character before any twist is spoken.
- How to use: change furniture distance, camera height, and focal length to change power; do not rely on actor shouting.
- Best scenes: lab meeting, cafe table argument, contract / marriage / timeline agreement, phone handover, message confirmation.
- Risk and anti-example: if the room is generic and the table is just decoration, the Fincher control system is absent.

**Knowledge Entry**

- Reusable rule: in Fincher grammar, lens choice and set design are not neutral. They are part of the trap.

---

## Case FD07 - Nolan: Inception Physicalized Impossible Rule

**Narrative Layer**

- Emotion tone: impossible concept made bodily.
- Character relationship: characters are not explaining the rule; their bodies prove the rule.
- Plot node: gravity, dream, time, or architecture behaves differently, and the audience must understand it fast.
- Narrative function: turn abstraction into a physical problem the viewer can track.

**Visual Layer**

- Shot size: action-readable wide / medium-wide inside a clear architectural axis.
- Camera position: aligned to the set mechanics so the audience can see the rule changing.
- Composition rules: repeated corridor geometry, body contact points, gravity contradiction, physical continuity.
- Lighting: practical fixtures built into the moving set; light must rotate or remain consistent with the physical mechanism.
- Color: each layer / rule should have its own stable palette or texture identifier.
- Spatial layers: foreground actor contact / handhold, midground combat or movement, background rotating architecture.

**Language Layer**

- Prompt sentence: `A clear corridor action frame where the room itself rotates and changes gravity; actors grip walls, floor, and ceiling as real contact points, while the camera preserves the corridor axis so the impossible rule remains readable.`
- Keywords: `physicalized impossible rule`, `rotating corridor`, `body proves physics`, `clear axis`, `practical contact points`.
- Visible AIGC anchors: state the physical rule, the set axis, body contact points, and what the camera does to preserve clarity.

**Replication And Use**

- Why it works: the audience believes the concept because bodies obey it.
- How to use: for time-machine or worldline moments, define a physical symptom: room light direction flips, sound reverses, phone UI remains stable while environment changes, dust falls upward, or reflections move backward.
- Best scenes: D-mail send, worldline jump, memory overwrite, time-machine test, parallel rule reveal.
- Risk and anti-example: abstract "time distortion energy" without physical behavior will become generic VFX.

**Knowledge Entry**

- Reusable rule: before Nolan-level complexity, teach one physical rule and let bodies, props, and camera obey it.

---

## Case FD08 - Nolan: Large-Format Intimacy And Suspended Sound

**Narrative Layer**

- Emotion tone: historic / cosmic scale pressing onto one human face.
- Character relationship: group or civilization-level stakes return to a single breath, hand, eye, or silence.
- Plot node: a massive event occurs, but emotional understanding arrives through delayed sound and human reaction.
- Narrative function: make scale meaningful rather than decorative.

**Visual Layer**

- Shot size: extreme scale shot paired with close human anchor; wide danger followed by face, hand, cockpit, visor, window, or small boat.
- Camera position: grounded inside the event when possible; not a detached postcard.
- Composition rules: scale contrast, human anchor, image-before-sound, action-defined character, cross-strand pressure.
- Lighting: large natural or practical source dominates; faces need controlled readability, not beauty lighting.
- Color: elemental palette: dust, water, flame, white light, black void, gray metal.
- Spatial layers: vast environment / event, tiny human carrier, immediate tactile object.

**Language Layer**

- Prompt sentence: `A massive event fills the environment, but the camera returns to one human face and one tactile object; the image holds in suspended silence before the delayed shockwave or mechanical sound reaches the body.`
- Keywords: `large-format intimacy`, `scale to human face`, `delayed sound`, `suspended silence`, `physical consequence`.
- Visible AIGC anchors: define the large event, the human anchor, the sound delay, and the object that receives consequence.

**Replication And Use**

- Why it works: scale becomes emotion only when it changes one person's available choices.
- How to use: in a time jump, show empty street / altered tower / impossible crowd absence, then return to Jiang Yan's breath, phone hand, or eye.
- Best scenes: worldline transition, public rupture, city-scale consequence, timeline collapse, fatal accident aftermath.
- Risk and anti-example: huge backgrounds with equal-size characters and no reaction are spectacle wallpaper.

**Knowledge Entry**

- Reusable rule: large scale must close back onto a human anchor or object proof within the same beat.

---

## Case FD09 - Tarantino: Ultra-Wide Interior Ensemble Pressure

**Narrative Layer**

- Emotion tone: talky room pressure, suspicion, violence held in reserve.
- Character relationship: every seated / standing body owns a threat lane.
- Plot node: a group is trapped together and the frame must let the audience track all alliances.
- Narrative function: use width to make dialogue dangerous rather than static.

**Visual Layer**

- Shot size: ultra-wide ensemble, then selective singles / two-shots without losing geography.
- Camera position: low-to-human height, often lateral or crane-as-dolly movement; avoids unnecessary modern floating.
- Composition rules: wide room map, table / stove / door / window threat lanes, multi-character visual weight, off-screen suspicion.
- Lighting: motivated indoor lamps, window cold, fire warmth, negative fill; every corner must have threat legibility.
- Color: warm wood / cold exterior / costume blocks as character grouping.
- Spatial layers: foreground object or shoulder, midground dialogue cluster, background door / window / armed watcher.

**Language Layer**

- Prompt sentence: `A very wide indoor ensemble frame maps the entire room: table, door, window, stove, weapons, and each character's sightline are readable at once, while the camera glides laterally like a dolly and lets dialogue pressure build before any rupture.`
- Keywords: `ultra-wide interior`, `ensemble geography`, `threat lanes`, `dialogue pressure`, `crane as dolly`.
- Visible AIGC anchors: list every character position, object lane, door/window exit, and who watches whom.

**Replication And Use**

- Why it works: the audience enjoys listening because the frame never loses where danger sits.
- How to use: for cafe / lab group scenes, establish everyone in one readable geography before cutting to reactions.
- Best scenes: four-person theory argument, awkward public behavior, lab confrontation, staged power comedy before rupture.
- Risk and anti-example: close-up ping-pong destroys the room pressure; random wide shots without threat lanes are just coverage.

**Knowledge Entry**

- Reusable rule: long dialogue needs mapped geography. The viewer should know who can reach the door, object, phone, weapon, or truth first.

---

## Case FD10 - Tarantino / Richardson: Table Bounce And Polite Threat

**Narrative Layer**

- Emotion tone: charm, politeness, and humor sitting on top of lethal control.
- Character relationship: one character controls the rhythm while the other performs normality to survive.
- Plot node: a conversation hides interrogation, coercion, or delayed violence.
- Narrative function: make a table scene visually alive through light, hands, objects, pauses, and power seating.

**Visual Layer**

- Shot size: table-wide geography, medium two-shots, slow pressure close-ups, object / hand inserts.
- Camera position: stable enough to let speech rhythm mature; push or lateral move only when power shifts.
- Composition rules: head-of-table power, table-as-stage, hot table plane, hand / glass / pipe / milk / document as rupture cue.
- Lighting: hard backlight or window source bounces off table / wall / costume into faces; practical above can justify highlights.
- Color: warm table surface, strong face highlights, darker surrounding room to keep attention on social game.
- Spatial layers: foreground table objects, midground speaking faces and hands, background door / family / hidden listener.

**Language Layer**

- Prompt sentence: `A polite table conversation with a hard backlight and table bounce lifting the faces from below; hands, glass, paper, and food sit in the foreground as possible rupture triggers, while the dominant speaker controls pauses and eye contact.`
- Keywords: `table bounce key`, `polite threat`, `head-of-table power`, `hands as trigger`, `dialogue pressure`.
- Visible AIGC anchors: name table object, dominant speaker position, backlight source, bounce surface, and the exact gesture that changes tension.

**Replication And Use**

- Why it works: the scene can stay entertaining while the composition quietly turns the table into a trap.
- How to use: for Jiang Yan's exaggerated speech or Su Lingyuan's technical explanation, keep the social rhythm alive with bystander reactions, hands, objects, and shifting gaze.
- Best scenes: cafe table theory, wedding-store clerk embarrassment, phone handover, "sent message?" suspicion, public absurdity.
- Risk and anti-example: a long monologue in a neutral medium shot is dead. The table must hold objects, light, and power.

**Knowledge Entry**

- Reusable rule: Tarantino-style dialogue composition is not "people talking." It is a room-sized timing mechanism with object triggers.

---

## Cross-Director Practical Rules

1. Choose the suspense engine before choosing the director grammar.
2. Do not make both characters equal unless equality is the dramatic point.
3. An object shot must either reveal, conceal, trigger, prove, or mislead.
4. A public scene must include public behavior: staff, bystanders, ambient sound, reaction delay, interrupted routine.
5. A long speech does not freeze the frame. Camera, background, hands, props, light, and other actors continue moving.
6. Large scale without a human anchor is wallpaper.
7. Darkness without information control is underexposure.
8. Surreal imagery without an ordinary baseline is random.
9. Dialogue without power movement is transcription, not cinema.
10. If a final prompt uses known character asset cards, do not restate or invent costumes unless the user requests a costume change.

## AIGC Transfer Checklist

Before writing an SD / Seedance prompt from these director systems, lock:

- Primary director grammar and one secondary support at most.
- Screen-space positions of every character.
- Foreground, midground, background actions.
- Light source, direction, contrast function, and key visible highlight.
- Lens / shot size / camera height / motion path.
- Object ownership and object state changes.
- Sound layer: near foley, midground human response, far ambience, and subjective / off-screen cue.
- Information timing: what audience sees first, what character sees later.
- Cut reason: what new information or emotional state changes at the edit.

If any of the above is missing, the prompt is not ready.
