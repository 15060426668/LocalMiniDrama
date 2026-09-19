# SD Video Advanced Execution

Use this reference for micro-expression, physical behavior, time control, frame consistency, parameter notes, and generic model adaptation. Ordinary transition grammar belongs to `effects-transition-prompting.md`; continuous matter transformation belongs to `effects-material-morph-library.md`.

All delivered prompt language stays positive and executable.

## 1. Prompt Order

Build each A segment in this order:

```text
camera layer
-> subject identity and position
-> main body action
-> physical contact / force / inertia
-> environment response
-> light and texture delta
-> sound trigger
-> landing frame and continuity
```

Use English technical anchors where they improve interpretation:

- shot: `wide shot`, `medium shot`, `close-up`.
- camera: `dolly in`, `lateral truck`, `rear tracking`, `whip pan`, `rack focus`, `POV shot`.
- lens: `24mm wide angle`, `35mm lens`, `50mm lens`, `85mm portrait lens`.
- capture/texture: `ARRI Alexa look`, `Kodak Vision3 color`, `35mm film grain`, `ACES color` only when supported by the source medium.

## 2. Micro-Expression Acting

Use:

```text
core emotion
-> eyebrows / eyelids / pupils
-> mouth / nostrils / jaw
-> facial muscle tension
-> breath / throat / shoulders / fingers
-> environmental secondary motion
```

| State | Positive execution |
|---|---|
| shock | eyes widen, pupils dilate, eyebrows lift, mouth parts, facial muscles freeze for half a beat |
| restrained fear | eyes search between sound zones, eyelids hold, throat swallows, lips press together, fingertips tremble |
| controlled anger | jaw clamps, nostrils open slightly, eyes narrow, temple tightens, breath becomes heavier |
| hesitation | gaze shifts briefly aside, brow gathers, lips compress, head tilts a few degrees, hand pauses |
| resolve | jaw sets, gaze stabilizes, eyebrows lower slightly, shoulders settle, breathing becomes even |
| dissociation | gaze fixes beyond the subject, blink rate slows, mouth relaxes, fingers continue one repetitive action |

Match expression scale to shot size. Extreme close-ups can carry pupil, eyelid, skin and lip detail; wider shots prioritize posture, route, hands and breath.

### Information Permission And Dual-Channel Acting

For concealment, false intimacy, social performance or performed ignorance, write both channels as positive visible actions:

```text
public facial/voice performance
-> public body task
-> small private leak or signal
-> who can perceive it
-> remaining body/object state
```

Examples:

```text
she keeps a warm public smile and holds the embrace for the cameras, her hidden hand tightens once against his back, her dry eyes remain fixed on him at close range, the surrounding crowd continues applauding
```

```text
he continues playing the piano with a neutral forward gaze, shoulders remain steady, one wrong note and damp fingertips reveal pressure, the nearby woman watches his face while the background neighbor continues moving behind the window
```

```text
she answers politely, torso remains facing the speaker, front foot rotates toward the exit during the phrase gap, fingers secure the key inside her palm, the distant guests remain unaware
```

Keep the private signal smaller than the public action and place it in a readable frame layer. State whether only the audience, one nearby character or the whole room can perceive it.

## 3. Physical Execution

Every effect or body action states:

```text
force direction -> contact point -> weight / resistance -> primary movement -> delayed secondary movement -> settling / tail state
```

### Dialogue And Active Blocking

For speaking while walking, handling props or reacting to another character, write:

```text
spoken phrase window -> mouth/jaw articulation -> main body route -> one supporting hand/prop action -> listener reaction window -> background event -> landing pose
```

- Keep one visible speaking mouth as the dialogue owner.
- Use natural mouth and jaw articulation matched to phrase rhythm.
- Place large turns, handoffs, door actions and listener reactions in phrase gaps or directly after the spoken line.
- Keep the body route simple while the line is dense.
- Split overlapping speakers or two major simultaneous actions into sequential beats.

### Body And Ground Contact

- feet compress against the surface, center of gravity travels through the step, knees absorb impact.
- hands wrap around the object, fingertips shift under friction, wrist and shoulder carry load.
- abrupt stops show torso inertia, delayed hair/cloth movement and balance recovery.
- falls accelerate under gravity and end with impact, bounce/slide and final rest.

### Collision And Recovery

Write collisions as:

```text
incoming direction -> contact surface -> body part contacting -> surface resistance -> torso/limb compression -> camera reaction -> delayed cloth/hair/prop inertia -> recovery step -> residual mark -> tail state
```

Examples of readable anchors:

- shoulder brushes a narrow wall, torso compresses sideways, palm touches the wall for balance, two shorter recovery steps restore the forward route.
- wet shoe slides laterally, knee bends to absorb the drop, hand strikes the wall, body regains balance with weight shifted to the opposite foot.
- doorway closes at a steady rate, body turns sideways, palm resists the door edge, hips clear the gap, coat hem follows half a beat later.

### Cloth And Hair

- lightweight cloth responds quickly with small ripples.
- cotton forms medium-weight structured folds.
- heavy coats swing slowly with visible inertia.
- hair follows head motion with a short delay, weighted ends and natural settling.

### Water And Fluid

- gravity controls flow direction.
- surface tension shapes droplets and merging trails.
- impact creates crown splash, secondary droplets and outward ripples.
- viscosity matches the material and slows or accelerates movement.

### Fire And Smoke

- flame rises with heat, keeps a teardrop core and curling edge.
- smoke is dense near the source, forms turbulent eddies, thins while rising.
- sparks and ash travel with convection and settle according to weight.

### Breakage And Debris

- cracks propagate from the contact point before separation.
- fragments receive different velocities and rotations.
- sharp edges catch light while dust responds more slowly.
- debris falls, bounces or slides, then reaches a readable tail state.

## 4. Time Control

| Effect | Anchor | Use |
|---|---|---|
| natural speed | `real-time motion, 24fps cinematic movement` | dialogue, pursuit, ordinary action |
| slow motion | `overcranked, 120fps look` | impact peak, expression, suspended cloth/dust |
| extreme slow motion | `time almost frozen, hyper-detailed suspended motion` | one decisive shock beat |
| fast motion | `undercranked, subject readable, edge/background motion blur` | short montage, acceleration |
| speed ramp | `natural speed -> slow at peak -> return to natural speed` | one action climax |
| freeze | `motion holds for one second while the selected camera relation continues` | evidence or decision emphasis |
| reverse motion | `objects and bodies return through the same physical path` | memory, rule reversal, reconstruction |

Time changes preserve direction, contact and readable subject identity.

## 5. Model Routing

Default output stays model-neutral. Read `sd-video-web-research-2026.md` when the user names a current model or requests latest model strategy.

Compact fallback:

- AnimateDiff: explicit moving object, verb-first action and physical anchor.
- SVD: small conservative subject movement and environmental micro-motion.
- Pika: clear natural-language start/middle/end VFX.
- Kling / 可灵: detailed Chinese body physics, spatial relation and mouth action.
- Runway: camera/lens/light language placed first.

## 6. Positive Consistency Anchors

Use only the anchors relevant to the risk:

```text
temporal coherence,
stable subject identity and clothing,
continuous camera path,
stable architectural geometry and screen direction,
grounded foot and hand contact,
natural weight and inertia,
consistent motivated light direction and exposure,
continuous color grade,
readable landing frame
```

Global locks own stable identity, medium, palette and room geometry. A segments repeat only the fragile anchors needed by that shot.

## 7. Parameter Notes

Add parameters only when the user asks for model tuning:

| Parameter | Starting range |
|---|---|
| CFG Scale | 6-8 |
| Motion Scale | 0.6-0.8 |
| Context Length | 16 frames |
| Context Overlap | 4 frames |
| Sampling Steps | 20-25 |
| Sampler | DPM++ 2M Karras |

Treat these as starting points rather than universal values.

## 8. Execution Rules

1. Camera layer comes first.
2. Each short beat has one main camera path.
3. Each character has one readable main action path.
4. Contact, force, weight and delayed secondary motion prove physics.
5. Abstract emotion becomes muscles, breath, posture and object handling.
6. Fast motion keeps the subject readable and puts blur on edges/background.
7. Slow motion reveals one selected physical or emotional detail.
8. Complex prompts use only the consistency anchors that protect fragile details.
9. Ordinary transitions route to `effects-transition-prompting.md`; matter transformations route to `effects-material-morph-library.md`.
10. The landing frame and inherited tail state are explicit.
