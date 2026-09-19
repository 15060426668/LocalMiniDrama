# Counterpart Radar Shot Index

Use this file when the user asks for 对标, 拉片, 阅片量, 随便说场景就能想到电影, 场景识别, 多搜寻多拆解, 对话戏, 追逐戏, 跟拍戏, 鱼眼, 心理恐怖, 梦境, 封闭场景, or wants many film mechanisms before designing a storyboard.

Purpose: build a fast recall radar for the current scene. Retrieve by scene resemblance, then qualify by reusable storyboard mechanism rather than plot identity. Return zero to six film-reference schemes whose camera, blocking, rhythm, sound, transition, performance, object or background language can help the current design. Never pad the list.

Source confidence: treat index entries as mechanism-level recall unless the cited frame/clip/production source has been inspected for the current task. Verify the source before claiming exact seconds, lens values or archival shot order.

Reference policy: film scenes are training and design evidence. The user may select one option or combine named mechanisms from several films. The final short-form storyboard redesigns shot order, duration, camera path, blocking, focus, sound and transitions for the current story. Do not report film time ranges or rough locations by default.

## How To Use

1. Parse the user scene into one or more tags:
   - dialogue pressure.
   - urgent chase / escape.
   - following / being followed.
   - fisheye / ultra-wide distortion.
   - psychological horror atmosphere.
   - dream / reality rupture.
   - confined space.
2. If the request combines two or more tags, begins from a single frame/visual idea, or depends on background action, group blocking, sound perspective, lens continuity, color payoff, or performance-triggered editing, read `counterpart-signature-retrieval-atlas.md` and build a five-axis fingerprint.
3. Use the five axes for recall, then return only concrete visual mechanisms. For each option, name the recognizable scene situation, composition/camera route, blocking and information release, rhythm, sound/transition, reusable rule and failure boundary. Character knowledge, identity, setting, props and plot cause may differ because they will be replaced.
4. Selection first produces an approved mechanism set and unifying director grammar, then waits. Break down the current short into standard fields only after the user explicitly enters detailed storyboard:

```text
场景类型：
参考影片/场景：
构图画面：
机位与运镜：
光影/色彩：
画面基调/质感：
实拍摄影证据：
画面内容：
运动生态/层级交互：
声音设计：
转场：
可复用规则：
失败边界：
当前场景替换项：
```

5. Synthesize approved mechanisms inside current story facts and AIGC executability. If no reference is selected, use the approved original scheme instead. Once formal storyboarding begins, the approved storyboard becomes the only SD source.

Source basis used for this index includes FilmGrab frame libraries for `The Silence of the Lambs`, `Se7en`, `The Shining`, `Pi`, `Perfect Blue`, `Paprika`, `Cube`, `Buried`, `Get Out`, `Zodiac`, `Prisoners`, and `Inglourious Basterds`; ASC material on `The Shining` Steadicam work; StudioBinder's fisheye lens explainer; and public article/clip references around `The Silence of the Lambs`, `Inglourious Basterds`, `Zodiac`, and `Requiem for a Dream`.

---

## 1. Dialogue Pressure / 对话压迫

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| D01 | `The Silence of the Lambs` - Clarice meets Lecter | glass barrier, direct address, eye-line, psychological duel | straight-to-lens close-ups, face symmetry, controlled listener reaction, institutional background | power is carried by who owns the lens and who can stay still |
| D02 | `Inglourious Basterds` - farmhouse interrogation | polite table, milk, pipe, floor pressure | long polite delay, table object, reaction sweat, off-screen hidden space | ordinary hospitality becomes a trap through object and silence |
| D03 | `Inglourious Basterds` - basement tavern | group table, hand gesture, undercover pressure | crowd background, hand detail, table axis, sound drop before outbreak | identity can be exposed by a tiny body habit |
| D04 | `Se7en` - car / office moral pressure | cold system, case talk, exhausted faces | rain windows, paperwork, low-key office light, restrained blocking | dialogue pressure grows from system fatigue and object evidence |
| D05 | `Zodiac` - suspect basement / interview | polite suspect, document, basement unease | calm speech, room layout, exit awareness, small prop cues | the scariest line can be said in a normal voice in a normal room |
| D06 | `Prisoners` - interrogation / confrontation | fluorescent room, rage, suspect silence | hands, table, glass, hard light, body leaning across boundary | violence is first visible as distance collapse and object impact |
| D07 | `Get Out` - family dinner / hypnosis talk | polite racism, teacup, family gaze | seating map, cup sound, group reaction, forced smile | social pressure becomes horror through synchronized politeness |
| D08 | `The Dark Knight` - interrogation room | table, top light, power reversal | top light, table boundary, close distance, controlled smile | when one side loses control, the still person gains power |
| D09 | `The Invitation` - dinner gathering | warm room, locked exit, polite threat | door position, wine glass, group smile, phone absence | social warmth hides exit control |
| D10 | `Marriage Story` / `Revolutionary Road` - domestic rupture | home argument, small objects, old wounds | blocking distance, hand gesture, room damage, voice volume shift | emotional violence is shown through space, objects, and escalation beats |

Dialogue design recall:

```text
speaker action -> listener reaction -> table/prop state -> background pressure -> silence or sound change -> cut point
```

---

## 2. Urgent Chase / 追逐奔逃

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| C01 | `The Shining` - Big Wheel corridors | low following, floor sound, repeated corridors | low lens height, floor material change, repeating turns | pursuit can be felt through camera height and sound rhythm |
| C02 | `The Shining` - hedge maze | snow maze, heavy breath, wrong turns | wide maze geometry, footprint, breath, axe rhythm | environment becomes the pursuer |
| C03 | `[REC]` - apartment / stair panic | reactive camera, off-screen noise, breath | handheld reaction, poor framing, sudden turns, sound hits | camera is dragged by panic rather than smoothly observing it |
| C04 | `A Quiet Place` - silent escape | tiny sounds, foot contact, breath control | sound scale, foot placement, object avoidance | a chase can be quiet but brutally tense through sound risk |
| C05 | `Children of Men` - continuous danger movement | long take, chaos around body, moving danger | foreground impacts, camera relation, background events | chase feels real when environment keeps acting around the subject |
| C06 | `Bourne Ultimatum` - foot chase | handheld body force, obstacles, urban cuts | impact cuts, stairs, doorways, hand contact | speed is created by body contact with space |
| C07 | `Train to Busan` - train corridor escape | narrow car, crowd pressure, door timing | screen direction, door choke points, bodies blocking path | chase pressure comes from blocked exits and moving crowd |
| C08 | `Oldboy` - hallway fight / corridor exhaustion | side scroll, fatigue, long corridor | lateral composition, body weight, obstacle repetition | action gains weight from exhaustion and limited direction |
| C09 | `Silent Hill` - siren / environment turn | alarm, darkness takeover, fleeing through space | sound trigger, light shift, texture change | chase can begin when space itself changes state |
| C10 | `Run Lola Run` - sprint rhythm | feet, urban rhythm, body mechanics | leg drive, rhythmic cuts, color/object repetition | running has to be edited like percussion |

Chase design recall:

```text
body force -> camera force -> foreground speed proof -> background state -> sound rhythm -> landing frame
```

---

## 3. Tracking / Following / 跟拍跟踪

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| F01 | `Following` - street tailing | black-white street, distance, reflection | target distance, crowd occlusion, window reflection | follow tension is distance management |
| F02 | `It Follows` - background slow pursuit | slow walker, wide background, viewer search | wide frame, background figure speed, character ignorance | threat can move slowly while audience scans the frame |
| F03 | `Zodiac` - investigators trailing evidence | procedural tracking, documents, office-to-street | step-by-step spatial handoff | follow a clue like a character |
| F04 | `The Conversation` - surveillance walk | plaza, sound record, long lens | long lens compression, recorded sound, public anonymity | tracking is psychological when sound is the real camera |
| F05 | `Caché` - fixed surveillance frame | static house shot, hidden watcher | unmoving frame, long duration, screen-within-screen | a still frame can become a threat by implying a watcher |
| F06 | `Rear Window` - window watching | multi-window voyeurism | window grid, foreground observer, background micro-actions | following can happen from a fixed position |
| F07 | `No Country for Old Men` - hallway / motel pursuit | quiet steps, doors, off-screen danger | door gaps, corridor sound, near-silent movement | unseen pursuit uses sound, doorways, and patience |
| F08 | `Cure` - slow walking pressure | static frame, ordinary rooms | flat distance, ordinary body movement, delayed reaction | follow shots can be hypnotic rather than kinetic |
| F09 | `Enemy` - urban doubling | yellow city, repeated routes, doubles | repeated spaces, matched blocking, ambiguous POV | following someone can become following yourself |
| F10 | `The Girl with the Dragon Tattoo` - investigation route | cold investigation, screens, files | character through systems, screen-to-space continuity | follow data into physical danger |

Tracking design recall:

```text
who knows they are being followed -> camera distance -> occlusion/reflection -> sound clue -> reveal of follower / target
```

---

## 4. Fisheye / Ultra-Wide Distortion / 鱼眼与广角扭曲

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| W01 | `Pi` - paranoid apartment / street | black-white, extreme wide, obsession | tight room, distorted face, high contrast, handheld | lens distortion externalizes paranoia |
| W02 | `Requiem for a Dream` - SnorriCam / addiction panic | face locked, background sliding | body-mounted feel, face stable, world moving | subject stays fixed while world attacks |
| W03 | `Black Swan` - rehearsal / mirror instability | body distortion, mirror, stress | wide lens near body, mirror mismatch, breath | psychological pressure distorts body space |
| W04 | `Brazil` - bureaucratic wide-angle absurdity | exaggerated rooms, faces, machines | low wide lens, production design, ceiling pressure | wide angle can turn systems into grotesque space |
| W05 | `Fear and Loathing in Las Vegas` - drug subjective | warped faces, hotel, motion | fisheye POV, color excess, body sway | altered perception can be lens grammar |
| W06 | `The Favourite` - palace fisheye | court power, distorted rooms | fisheye rooms, symmetrical absurdity | power games become spatial caricature |
| W07 | `Amélie` / stylized close wide faces | face near lens, expressive distortion | near-camera face, background pull | wide close-up amplifies subjectivity |
| W08 | `Enter the Void` - subjective spatial drift | POV, floating, neon | disembodied camera, overhead drift | camera grammar can detach from body |
| W09 | `A Clockwork Orange` - interior wide aggression | wide rooms, confrontational face | extreme wide, theatrical blocking | wide lens makes social violence feel staged and invasive |
| W10 | `12 Monkeys` / Gilliam grammar | mental institution, wide distortion | tilted wide lens, ceiling, institutional clutter | distorted lens makes institutions feel mentally unstable |

Wide distortion recall:

```text
why the world bends -> lens distance -> face/body distortion -> background stretch -> sound or movement cue
```

---

## 5. Psychological Horror / 心理恐怖压抑

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| P01 | `Mulholland Drive` - diner wall | ordinary diner, dream fear, slow approach | normal light, slow push, sound thinning | dread grows from everyday normality |
| P02 | `Blue Velvet` - grass to hidden object | suburb, grass, insect sound | surface normal, micro descent, sound scale | camera digs under the normal world |
| P03 | `Cure` - ordinary room infection | static room, repeated question | long static, dry voice, table object | stillness can feel contagious |
| P04 | `Identity` - rain motel | rain, motel rooms, identity chessboard | room numbers, keys, rain curtain, group blocking | environment organizes psychological fragments |
| P05 | `Memento` - evidence objects | memory loss, photos, notes | hand, photo, writing, temporal confusion | objects replace memory but can mislead |
| P06 | `The Others` - curtains / candle rules | light taboo, doors, old house | light as rule, curtain sound, candle flame | light is dangerous when it changes behavior |
| P07 | `Shutter Island` - institution / storm | island, ward, storm, official space | large institution, fog, controlled rooms | environment offers a rational explanation that may be false |
| P08 | `Session 9` - abandoned institution | empty hospital, tapes, dust | recorded voices, peeling walls, long corridors | sound archives make space remember |
| P09 | `Burning` - absence suspense | empty room, phone silence, missing person | empty frame, waiting, missing object | what is absent becomes the subject |
| P10 | `The Killing of a Sacred Deer` - cold order | hospital, family, flat speech | symmetrical cold frames, deadpan distance | emotional horror can come from total composure |

Psychological horror recall:

```text
normal baseline -> one wrong detail -> body micro-reaction -> object evidence -> sound shift -> lingering tail frame
```

---

## 6. Dream / Reality Rupture / 梦境现实错位

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| M01 | `Inception` - folding city | city bends, rules physicalized | impossible space, real material, stable camera | abstract dream rule becomes physical architecture |
| M02 | `Inception` - rotating hallway | gravity shift, one-take fight | real rotating set, long motion, orientation loss | spatial rule is learned through body impact |
| M03 | `Paprika` - parade / scene spill | dream parade, object morph, no hard borders | continuous transformation, object logic, sound parade | dream changes through associative motion |
| M04 | `Perfect Blue` - stage/reality cuts | idol stage, apartment, identity slip | match cuts, repeated gestures, audience confusion | performance space can bleed into private space |
| M05 | `Mulholland Drive` - dream identity shift | identity swap, object key | tone shift, actor/blocking change, object anchor | dream reveal can be quiet, object-led |
| M06 | `Jacob's Ladder` - hospital / subway flashes | urban reality cracks | strobe, body shake, medical intrusion | flashes should contaminate current reality with residue |
| M07 | `A Nightmare on Elm Street` - school / sleep rupture | ordinary school, dream threat | normal place becomes impossible through simple rules | dream can start from a familiar room |
| M08 | `The Cell` - psychological interiors | symbolic rooms, costume, color | production design as mind space | subconscious can be staged as architecture |
| M09 | `Dream Scenario` - social dream intrusion | public dreams, mundane surrealism | normal crowd behavior altered by dream premise | dreams can be social, awkward, deadpan |
| M10 | `Eternal Sunshine` - memory collapse | room erasure, relationship memory | disappearing set, fading object, emotional anchor | memory collapse works through object removal |
| M11 | `Inception` - synchronized dream-layer waking | nested spaces, body trigger, parallel timing | match body direction and impact across layers; preserve rhythmic wake cascade | replace trained dream awareness with false confidence, keeping the same cross-layer camera and action grammar |
| M12 | `Paprika` - dream-to-dream associative scene shift | continuous pursuit, identity/space changes, visual association | carry one moving body/object through several environments without resetting motion | replace the original detective/therapist identity with a protagonist who mistakes the latest space for reality |
| M13 | `Perfect Blue` - repeated bed/stage reality reset | repeated waking frame, gesture residue, uncertain performance | reuse nearly identical wake composition while one body/object detail changes | replace celebrity identity confusion with any dream-within-dream realization |
| M14 | `An American Werewolf in London` - double hospital awakening | first wake, apparent safety, rupture, second wake | repeat the hospital-bed awakening with escalating physical proof | replace the original attack and characters while preserving the false-awakening rhythm |
| M15 | `A Nightmare on Elm Street` - false-normal awakening | bright safe baseline, one wrong detail, environment takes control | delay the reveal until normal blocking has been re-established | replace supernatural knowledge and threat identity while preserving the safe-world reversal |

Dream rupture recall:

```text
real surface -> trigger -> first impossible detail -> material process -> new space -> residual trace -> sound bridge
```

Dream-awareness rule: whether the original character knows they are dreaming is a replaceable story variable. Keep or transplant the camera path, repeated framing, body trigger, environment change, rhythm, sound bridge and reveal order; rewrite awareness to fit the current protagonist.

---

## 7. Confined Space / 封闭场景密闭空间

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| K01 | `Cube` - cubic rooms | room grid, door hatches, test movement | geometric room, color change, hatch routes | rules are learned by moving through repeated rooms |
| K02 | `Saw` - wake in room | chained room, rule object, dirty light | body awakening, room map, object instructions | first minutes must teach body limits and rules |
| K03 | `Buried` - coffin space | blackness, phone, lighter, breath | micro light source, extreme close space, sound | confined space is built through touch and sound |
| K04 | `10 Cloverfield Lane` - bunker table | underground safety/prison | kitchen table, locked door, ordinary bunker objects | comfort props can become control props |
| K05 | `Panic Room` - house as system | security room, screens, intruders | maps, screens, doors, air ducts | architecture becomes a machine with rules |
| K06 | `The Descent` - cave crawl | narrow rock, light beam, breath | body compression, headlamp, texture | claustrophobia needs contact with walls |
| K07 | `Phone Booth` - public tiny trap | glass booth, street crowd, voice | transparent cage, unseen speaker, crowd | open public space can function as a sealed room |
| K08 | `Devil` - elevator | vertical box, strangers, light | overhead light, mirror, numbers, group blocking | elevator suspense comes from mechanical pauses and faces |
| K09 | `Locke` - car-only film | one man, phone calls, road night | dashboard light, speaker voices, windshield | single-location motion can be story movement |
| K10 | `Exam` - sealed test room | table, paper, rules, group pressure | symmetric room, rules object, group distrust | a room becomes suspense when rules limit behavior |

Confined-space recall:

```text
wake / enter -> map the limits -> find rule object -> test exit -> sound outside / unseen voice -> object state changes -> new decision
```

---

## 8. Door / Threshold / 开门与门后压力

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| T01 | `The Others` - doors and curtains | old house, light taboo, door discipline | door latch, candle, curtain sound, child reaction | rules become visible through how doors and light are handled |
| T02 | `The Shining` - Room 237 approach | forbidden room, carpet, key, slow entry | hallway geometry, hand to knob, interior color shift | threshold suspense is built before the room is shown |
| T03 | `No Country for Old Men` - motel door pressure | door gap, lock cylinder, silent approach | lock detail, hallway silence, off-screen body | the door is a measuring device for unseen distance |
| T04 | `Panic Room` - security doors | house machine, door closing, screen control | monitors, bolts, metal contact | closing a door changes the whole architecture |
| T05 | `Coraline` - small door | child-scale portal, hidden room | unusual door size, hand object, color contrast | a small threshold makes curiosity feel like trespass |
| T06 | `The Orphanage` - hallway doors | child voice, old house, repeated doors | off-screen call, door sequence, empty reveal | repeated doors delay proof and amplify listening |
| T07 | `The Babadook` - bedroom door | domestic room, knocking, mother-child fear | door panel, bed distance, sound impact | the door lets fear enter without showing a figure |
| T08 | `The Sixth Sense` - cold room threshold | temperature cue, hallway, door frame | breath, color cool-down, frame-within-frame | an invisible rule is announced by the air itself |
| T09 | `The Wailing` - house threshold | ritual/folk fear, doorway, family | exterior darkness, porch light, hesitant bodies | crossing the threshold changes social rules |
| T10 | `The Invitation` - exit door control | party room, locked door, polite host | hand on handle, group gaze, warm light | a door becomes pressure when social permission controls it |

Door design recall:

```text
hand reaches -> latch detail -> sound gap -> door edge opens -> first slice of space -> body hesitation -> full reveal / no reveal
```

---

## 9. Mirror / Reflection / 镜子与倒影错位

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| R01 | `Black Swan` - rehearsal mirrors | mirror wall, double, body stress | reflection mismatch, shoulder/eye delay, handheld closeness | reflection becomes a second performer |
| R02 | `Perfect Blue` - stage/private identity | performer double, glass, screen | match action, reflection-like cuts, repeated gesture | identity breaks through repeated visual positions |
| R03 | `Persona` - face merging | two faces, stillness, psychological split | frontal face, half-shadow, graphic match | face composition can fuse two identities |
| R04 | `Enemy` - urban doubling | yellow glass, repeated city, double | reflection, windows, symmetrical routes | doubles feel inevitable when the city repeats them |
| R05 | `Us` - mirror hall / duplicate logic | reflection metaphor, family double | matched blocking, opposite movement | reflection grammar teaches duplicate rules |
| R06 | `The Machinist` - bathroom mirror | body collapse, shaving, fatigue | mirror grime, sink detail, hollow face | a mirror records physical deterioration |
| R07 | `Taxi Driver` - mirror self-talk | weapon rehearsal, mirror address | direct eye, small room, object in hand | mirror can turn inner monologue into confrontation |
| R08 | `Mulholland Drive` - identity object / face shift | dream identity, key, face unease | object anchor, face pause, soft room | reflection logic can be transferred to non-mirror objects |
| R09 | `Oculus` - cursed mirror room | room reflection, time slippage | mirror surface, object test, angle control | mirror suspense needs precise spatial rules |
| R10 | `Candyman` - mirror invocation | repeated phrase, bathroom mirror | face and mirror edge, whispered sound | reflection becomes a ritual interface |

Reflection design recall:

```text
real body action -> reflected action delay / mismatch -> subject notices -> light or sound confirms -> cut to object proof
```

---

## 10. Rule Object / Evidence Object / 规则物与证据物

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| O01 | `Memento` - Polaroid / tattoo system | photo, note, body text | hand reads object, object contradicts memory | the object becomes a temporary brain |
| O02 | `Se7en` - notebooks / box withheld | evidence, hidden content, moral pressure | prop weight, reaction, off-screen content | do not show the object if reaction can carry it |
| O03 | `Zodiac` - letters / ciphers | paper evidence, system investigation | paper texture, desk light, hands sorting | clue design is tactile and procedural |
| O04 | `The Ring` - videotape | media object, curse rule | screen glow, tape insertion, image noise | a rule can be stored in degraded media |
| O05 | `The Others` - curtains / keys | house rules, light, keys | keys, locks, curtains, candle | rule objects control behavior before plot explains them |
| O06 | `Cube` - boots / numbers / hatches | test object, room code | object enters space first, reaction waits | test the rule through an expendable object |
| O07 | `Panic Room` - monitors / map | screen evidence, house layout | screen grid, hand to button, door status | object interface turns space into a system |
| O08 | `Get Out` - teacup | small sound, hypnosis, social control | spoon, cup, close hand, sound rhythm | a tiny domestic object can hijack perception |
| O09 | `Knives Out` - medicine bottle | label, dosage, moral panic | bottle close-up, hand tremor, label read | props can stage a false moral emergency |
| O10 | `The Prestige` - machine / diary | secret device, nested evidence | diary as voice bridge, machine silhouette | object mystery works when evidence lies in layers |

Object design recall:

```text
object enters frame -> ownership established -> state or rule shown -> character tests it -> contradiction appears -> object tail-frame
```

---

## 11. Sound-Led Suspense / 声音先行悬念

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| S01 | `A Quiet Place` - silent movement | tiny noise, survival rule | foot placement, breath, object contact | sound scale turns small actions into danger |
| S02 | `The Conversation` - recorded audio | surveillance, distorted phrase | microphone distance, playback, repeated phrase | sound evidence changes meaning through repetition |
| S03 | `Blow Out` - sound recording clue | tire sound, scream, edit | waveform/listening, replay, sync | sound can reveal the event image hides |
| S04 | `Berberian Sound Studio` - unseen violence | studio foley, off-screen horror | foley objects, booth, voice layer | violence can live entirely inside sound production |
| S05 | `Mulholland Drive` - diner silence | everyday space, thinning bed | room tone drops, slow approach | silence becomes visible when normal ambience is removed |
| S06 | `The Shining` - tricycle floor changes | carpet/wood rhythm | material-specific wheel sound | floor texture edits space before camera turns |
| S07 | `No Country for Old Men` - motel quiet | door, footsteps, breath | low room tone, off-screen steps | quietness makes distance measurable |
| S08 | `The Sixth Sense` - cold breath / whisper | whisper, room chill | near voice, breath sound, still body | voice direction can contradict visual space |
| S09 | `It Follows` - slow threat sound bed | background walker, synth dread | wide frame plus steady sound pressure | music tells the audience to scan the frame |
| S10 | `The Zone of Interest` - off-screen horror field | domestic image, distant violence | ordinary visuals, constant off-screen sound | sound can make a clean frame morally unbearable |

Sound design recall:

```text
normal room tone -> first wrong sound -> subject reaction -> source search -> sound changes distance -> image withholds proof
```

---

## 12. Domestic Conflict / 家庭争吵与亲密关系破裂

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| H01 | `Marriage Story` - apartment argument | divorce, close room, escalation | distance collapse, hand gesture, voice crack | argument becomes physical when blocking distance collapses |
| H02 | `Revolutionary Road` - kitchen/living room fight | suburban marriage, trapped room | table, doorway, rigid posture | domestic layout is a battlefield map |
| H03 | `Blue Valentine` - room rupture | intimacy decay, handheld closeness | soft light, messy room, body recoil | love history is carried by small failed touches |
| H04 | `Scenes from a Marriage` - close dialogue pressure | face-to-face emotional surgery | long close-ups, eye fatigue | stillness can be more violent than movement |
| H05 | `Kramer vs. Kramer` - apartment rupture | custody, door, child nearby | door threshold, suitcase, child sound | domestic conflict must account for collateral listeners |
| H06 | `A Separation` - doorway dispute | legal/family pressure | threshold, documents, multiple speakers | family conflict becomes system pressure through paperwork |
| H07 | `The Babadook` - mother-child pressure | grief, house, bedtime | bedtime routine, door sound, toy/bed prop | ordinary care actions can turn hostile under stress |
| H08 | `Hereditary` - dinner argument | grief, table, family shock | table axis, still faces, explosive line | dinner geometry traps everyone in reaction shots |
| H09 | `The Invisible Man` - kitchen/domestic threat | empty space, table, unseen force | negative space, chair/table movement | absence can enter a domestic argument as third party |
| H10 | `Gone Girl` - couple performance | public/private marriage | smile mask, object staging, media gaze | a couple can weaponize performance and domestic evidence |

Domestic conflict recall:

```text
small practical dispute -> object ownership fight -> distance collapse / withdrawal -> listener reaction -> room damage or object state -> silence after line
```

---

## 13. Institution / Hospital / 机构空间压迫

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| I01 | `Shutter Island` - ward corridors | official space, storm, unreliability | guards, doors, medical props, wet light | institution offers safety and threat at once |
| I02 | `Session 9` - abandoned hospital | asylum, tapes, dust | long corridors, peeling paint, recorded voice | institutional ruins feel like archived memory |
| I03 | `One Flew Over the Cuckoo's Nest` - ward routine | group room, nurses, rules | desks, chairs, group arrangement | room layout expresses administrative power |
| I04 | `12 Monkeys` - mental ward wide distortion | institutional clutter, wide lens | ceiling, bars, crowd, extreme wide | wide lens makes bureaucracy feel mentally unstable |
| I05 | `The Killing of a Sacred Deer` - hospital coldness | medical corridors, flat affect | symmetrical halls, clinical light | emotional dread rises when everyone stays composed |
| I06 | `Jacob's Ladder` - hospital nightmare | medical hallway, flashes | fluorescent flicker, body on gurney | medical imagery can invade reality as fragments |
| I07 | `Unsane` - psych ward | phone/camera paranoia, ward | institutional forms, locked doors | administrative paperwork can trap a character |
| I08 | `A Cure for Wellness` - sanatorium | wellness facade, water, old building | polished surfaces, medical ritual | luxury cleanliness can hide institutional violence |
| I09 | `The Jacket` - morgue drawer / asylum | restraint, drawer, memory | body confinement, medical light | institutional tools make memory physical |
| I10 | `Fractured` - hospital disappearance | missing family, procedures | waiting room, screens, corridors | institutional normality can erase personal truth |

Institution design recall:

```text
official order -> personal doubt -> rule/object proof -> corridor or desk barrier -> staff reaction -> system sound tail
```

---

## 14. Rain Night / Motel / Wet Space / 雨夜旅馆与潮湿空间

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| N01 | `Identity` - rain motel | storm, room numbers, group distrust | rain curtain, neon, wet asphalt, keys | weather organizes fragmented characters into one trap |
| N02 | `Psycho` - Bates Motel exterior | rain, sign, isolated motel | wet windshield, neon sign, office window | arrival is framed as surrender to a lit trap |
| N03 | `Se7en` - city rain | constant rain, moral decay | wet streets, low contrast, green-yellow interiors | weather can be the city's moral texture |
| N04 | `Memories of Murder` - rain crime site | field, mud, rural investigation | mud, flashlight, wet clothing | rain destroys evidence and certainty |
| N05 | `Prisoners` - rain suburbs | grey houses, wet roads, searching | car windows, rain on faces | weather turns grief into physical weight |
| N06 | `Zodiac` - rainy streets / cars | investigation drift, city | windshield distortion, sodium light | rain turns city clues into layers of glass |
| N07 | `The Ring` - wet cursed image | water motif, TV, damp rooms | condensation, screen glow, pale skin | moisture can make media horror feel material |
| N08 | `Dark Water` - leaking apartment | ceiling leak, child anxiety | stain, drip, damp wall | one water mark can become a spreading threat |
| N09 | `Insomnia` - cold wet town | fog, docks, sleeplessness | cold daylight, wet surfaces | wet cold can exhaust the mind without darkness |
| N10 | `Mother!` - house damage escalation | liquid, floor, crowd pressure | spills, stains, soaked surfaces | surface damage records psychological invasion |

Wet-space recall:

```text
wet surface proof -> distorted reflection -> sound of drip/rain -> object becomes damp -> body slips/hesitates -> trace remains
```

---

## 15. Waking / Reality Landing / 梦醒落地

| # | Counterpart | Scene Recall Keywords | Pull-Apart Focus | Transferable Mechanism |
|---:|---|---|---|---|
| A01 | `Inception` - kick / bathtub waking | body impact, water, breath | falling body, water hit, gasp | waking feels real when the body pays a price |
| A02 | `Mulholland Drive` - identity shift waking | bed, key, altered person | room stillness, object anchor, face pause | waking can be quiet and existential |
| A03 | `Perfect Blue` - bed/stage confusion | repeated wake, performance bleed | matched gesture, bed frame, time slip | wake-up works when the previous scene leaves residue |
| A04 | `Paprika` - dream device waking | interface, therapy room | eyes, device, sound bridge | technology can provide the wake-up anchor |
| A05 | `Jacob's Ladder` - hospital/subway jolts | body jerk, flash, medical residue | abrupt body reaction, fragment overlay | awakening can be a violent nervous-system reset |
| A06 | `Memento` - motel room disorientation | motel bed, notes, phone | object scan, body checks, black/white order | wake-up can be an information inventory |
| A07 | `Shutter Island` - institutional confusion | room, guards, storm | room evidence, facial stillness | waking should question which reality is official |
| A08 | `The Machinist` - insomnia wakefulness | thin body, room, clock | clock, body, dirty texture | waking can feel like never sleeping at all |
| A09 | `A Nightmare on Elm Street` - dream injury residue | bed, sweat, physical trace | body mark, sheets, breath | reality landing is proven by residue from the dream |
| A10 | `Brazil` - fantasy/office collision | fantasy cut, bureaucratic room | image contrast, sound cut, object carryover | wake-up can collapse grandeur into institutional routine |

Wake-up design recall:

```text
dream body state -> impact or breath trigger -> eye / hand / sheet action -> room inventory -> residue proof -> new rule object
```

---

## 16. Fast Scene-To-Counterpart Routing

| User says... | First radar pull |
|---|---|
| "两个人对峙 / 审问 / 吵架" | D01, D02, D05, D06, D10 |
| "过道逃跑 / 被追 / 慌乱开门" | C01, C02, C03, C07, K02 |
| "有人跟着她 / 背后有人 / 镜头跟随" | F01, F02, F04, F05, F07 |
| "鱼眼 / 压迫脸 / 主观崩溃" | W01, W02, W03, W06, W10 |
| "心理恐怖 / 不惊悚但压抑" | P01, P03, P04, P08, P09 |
| "梦里醒来 / 空间变形 / 幻觉坍塌" | M01, M02, M03, M04, M10 |
| "密闭房间 / 规则局 / 醒来出不去" | K01, K02, K03, K04, K10 |
| "开门 / 门后 / 门缝 / 推门转场" | T01, T02, T03, T04, T06 |
| "镜子 / 倒影 / 另一个自己" | R01, R02, R04, R08, R09 |
| "规则物 / 卡片 / 证据 / 物件特写" | O01, O02, O03, O05, O08 |
| "声音先到 / 看不见的人 / 画外声" | S01, S02, S05, S07, S08 |
| "家庭争吵 / 离婚 / 亲密关系爆发" | H01, H02, H03, H08, H10 |
| "病房 / 收容机构 / 医院 / 异常管理系统" | I01, I02, I05, I06, I10 |
| "雨夜 / 旅馆 / 潮湿封闭空间" | N01, N02, N03, N08, N09 |
| "梦醒 / 从幻觉回到房间 / 惊醒" | A01, A02, A03, A05, A06 |
| "背景也要动 / 活画面" | D07, C05, C09, P04, K05 |
| "三人以上 / 阵营变化 / 谁站哪边" | `counterpart-signature-retrieval-atlas.md` AB01-AB10 |
| "声音跨房间 / 跨切镜距离变化 / 画外声测距" | `counterpart-signature-retrieval-atlas.md` SP01-SP10 |
| "整段焦段逻辑 / 镜头为什么忽近忽远" | `counterpart-signature-retrieval-atlas.md` LC01-LC10 |
| "颜色是伏笔 / 强调色回收 / 色彩改写规则" | `counterpart-signature-retrieval-atlas.md` CP01-CP10 |
| "一个眼神或手势触发推镜/切镜" | `counterpart-signature-retrieval-atlas.md` PE01-PE10 |
| "前景说话，背景人物/物件同时讲故事" | `counterpart-signature-retrieval-atlas.md` FB01-FB10 |

## 17. Minimum Counterpart Breakdown Output

When using this radar in a final storyboard, include a compact version before the shot design:

```text
对标雷达：
1. 片段A：借镜头机制...
2. 片段B：借声音机制...
3. 片段C：借空间/物件机制...

导演取舍：
采用...
放弃...
转译规则...
```

For training deposit, use the full拉片表单 and store the result in the matching scene-family library.
