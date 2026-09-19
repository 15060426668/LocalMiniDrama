# SD Continuity Checksum

Use this reference for multi-shot A blocks, multiple 30-second segments, image-to-video continuation, recurring characters/props, complex transitions, or generated-result drift.

The checksum separates stable state from shot-specific change.

All A beats inherit the approved formal storyboard. Film references may inform upstream design but never enter this checksum. The next prompt inherits the previous tail state before applying its new storyboard delta.

## 1. Three-Part Compiler State

```text
BASE MANIFEST: stable facts for the scene/sequence
DELTA: what changes in this A segment
TAIL STATE: exact state inherited by the next segment
```

Do not rewrite the whole base manifest inside every segment. Repeat only fragile anchors needed for model stability.

## 2. Base Manifest

Lock once:

```text
medium / aspect ratio:
character identity and reference:
face / hair / wardrobe baseline:
body marks and carried residue:
space map and screen direction:
doors / windows / furniture / key props:
prop owners and initial states:
motivated light sources and color owners:
global texture and material family:
sound bed and recurring sound signatures:
camera/lens family:
current prompt number / duration / approved storyboard checksum:
incoming tail frame:
```

## 3. Per-Segment Checksum

Every A segment internally tracks:

| Bus | Start state | Delta | Tail state |
|---|---|---|---|
| Character identity | face, hair, body silhouette | expression/body action | ending posture and gaze |
| Wardrobe/body | clothing, wetness, dust, damage, breath | new contact/strain/mark | exact residue carried forward |
| Space/direction | camera side, exits, movement direction | route/camera change | final screen position and facing |
| Prop ownership | owner, hand, orientation, material state | pass/drop/grip/transform | new owner/location/state |
| Light/color | source position, color owner, exposure | flicker/extinguish/shift | final source and shadow state |
| Texture/material | surface and wear pattern | crack/wet/tear/dust/contact | residual trace |
| Sound | bed, source location, rhythm | entry/drop/distortion | sound tail/J-cut/L-cut |
| VFX/transition | source surface and boundary | visible process | new space/object and residual anchor |
| Camera | shot/lens/height/path | exact operation | landing frame |
| Storyboard source | current prompt number/duration and approved storyboard checksum | shot/beat order and camera grammar delta | storyboard remains active through prompt tail |
| Knowledge/permission | who sees, hears, knows, suspects or performs ignorance; public/private signal owner | new cue, inference or exposure | final knowledge state and who can perceive the private signal |
| Motion ecology | primary/reactive/ambient hierarchy, NPC tasks, force direction | triggered interactions and material responses | final moving/settled states and residual traces |
| Audience question | current uncertainty | new evidence/risk | next question |

## 4. Delta Compilation

A segment writes:

```text
尾帧与连续性：
起始继承：...
本镜差量：...
落点状态：...
易丢锚点：...
下一镜继承：...
```

Stable facts can be compact:

- same established character identity and wardrobe.
- same corridor geometry and screen direction.
- same motivated light family and color grade.
- same prop material and owner until the stated handoff.

Fragile facts remain explicit:

- hand carrying the card.
- wet footprint direction.
- door position.
- current wound/dust/water state.
- which fluorescent lamps are extinguished.
- which wall section has transformed.
- exact body orientation during a quick look-back.
- tail-frame hand/foot/object contact.

## 5. Complexity Score

Score each proposed A beat:

| System | Points |
|---|---:|
| one camera path | 1 |
| each major subject action | 1 |
| important prop interaction | 1 |
| active background event | 1 |
| environment/VFX process | 2 |
| second material/VFX family | 2 |
| time effect or speed ramp | 1 |
| dialogue/lip-sync plus major movement | 1 |
| identity or wardrobe transformation | 2 |

Interpretation:

- 0-3: compact and stable.
- 4-5: dense; separate tracks and protect the landing frame.
- 6+: split into sequential A beats.
- two camera paths or two transitions in one beat trigger a split.

The score is internal and never replaces director judgment.

## 6. Tail-To-Start Bridge

For adjacent segments:

```text
previous tail body position = next start body position
previous gaze direction = next start gaze origin
previous prop owner/state = next start prop owner/state
previous camera side/direction = next start camera relation
previous light state = next start light state
previous sound tail = next start sound bed or bridge
previous VFX residual trace = next start environmental proof
previous knowledge/permission state + ambient-force direction + NPC/object movement state = next start motion ecology
previous tail checksum is inherited before the next prompt applies its new storyboard delta
```

A new prompt may change angle or lens only when the approved storyboard specifies it, while preserving inherited spatial direction and state.

## 7. Image-To-Video Continuation

Treat the supplied frame as the base manifest:

- visible character features and clothing.
- exact pose, hand/foot contact and gaze.
- camera height, lens impression, crop and perspective.
- foreground/midground/background layout.
- prop positions and readable surfaces.
- light source direction, exposure and color ownership.
- material texture, weather and atmosphere.
- motion origin: which body, object, camera or environment movement starts first.

The first A beat begins from those visible facts and describes only the intended motion/delta.

## 8. Prop And Material Continuity

Track:

```text
object identity
-> owner/hand
-> orientation
-> contact marks
-> moisture/dust/damage
-> sound fingerprint
-> position at cut
-> next-shot state
```

Material transformation additionally tracks:

```text
changed area + unchanged area + moving boundary + inherited pattern + residual trace
```

## 9. Light And Sound Continuity

Light checksum:

- source location.
- source color.
- beam/contact direction.
- current active/extinguished state.
- shadow side.
- exposure and color-grade continuity.

Sound checksum:

- environment bed.
- recurring sound signature.
- source quadrant and distance.
- rhythm/tempo.
- subjective filtering.
- tail type: cut, echo, pre-lap, decay, silence.

Sound changes must trigger body, camera, focus, edit, light or space when dramatically important.

## 10. Generated-Result Repair

When output drifts, compare in order:

1. source storyboard row.
2. base manifest.
3. A segment delta.
4. tail state.
5. generated frame/video.

Repair the first layer where the fact disappears.

Typical repairs:

- identity drift -> strengthen reference/identity baseline and reduce simultaneous transformation load.
- spatial drift -> restate camera side, door positions, movement direction and landing frame.
- prop drift -> restate owner, hand, orientation, contact and tail position.
- light drift -> restate source position/color and shot-specific state.
- VFX randomness -> reduce to one matter family and name the moving boundary/inheritance.
- action loss -> separate body action from camera path and environmental process.
- transition discontinuity -> restate previous tail and next start as the same visible anchor.

## 11. A-Block Consolidation

For multi-shot or fragile sequences, consolidate continuity once:

```text
尾帧与连续性：起始继承...；本镜差量...；落点状态...；易丢锚点...；下一镜继承...
```

Do not repeat the same tail state in separate `镜间变化/尾帧`, `SD承接锚点` and `连续性校验` fields. Keep the complexity decision internal.

## 12. Regression Cases

1. Quick look-back: feet/torso continue forward, head/neck glance back, camera performs lateral truck, next beat begins after gaze returns.
2. Prop handoff: object owner, hand, orientation and sound survive the cut.
3. Dream collapse: changed/unchanged zones, moving boundary and residual trace survive across segments.
4. Domestic argument: room axis, door position, object state, wardrobe and emotional residue survive coverage changes.
5. Weather pursuit: wetness, footprints, cloth weight, visibility and sound occlusion accumulate.
6. Screen evidence: screen content, watcher reaction, room correspondence and device state remain consistent.
7. Waking transition: dream contact becomes reality contact through one inherited hand/object/light/sound anchor.
