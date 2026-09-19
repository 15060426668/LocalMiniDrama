# Control Matrix

Choose one primary rendering lane, one composition control, one light system, and one texture finish. IDs remain internal.

## Rendering lanes

| ID | Story function | Character treatment | Environment treatment |
|---|---|---|---|
| `LANE-DAYLIGHT` | ordinary childhood life, friendship, walking home, school routine | compact proportions, open pale faces, simple expressions | clear readable setting, natural greens, cyan sky, restrained cel shadows |
| `LANE-PRESSURE` | exclusion, bullying, social control, public embarrassment | victim smaller and inward; group faces bright or playfully calm | blocked routes, foreground bodies, desks, bags, doors, or walls carry pressure |
| `LANE-PSYCHO` | exhaustion, dread, shame, grief, private realization | tight crop, heavy lower eyelids, sparse hatching, muted shadows | simplified or compressed background, selective darkening, ordinary details continue |
| `LANE-SURREAL` | mascot intrusion, emotional allegory, impossible companion | human rendering follows one other lane; mascot remains extremely simple | environment remains materially credible so the flat mascot reads as alien |

## Composition controls

| ID | Frame design | Best use |
|---|---|---|
| `COMP-PROFILE-TWO` | two faces in opposing profile, narrow gap, shared sky or wall | direct relationship tension |
| `COMP-GROUP-FRONT` | group walking toward camera, staggered heads and bags, readable road depth | ordinary group introduction |
| `COMP-ENCLOSURE` | vulnerable child centered or off-center inside a U-shape of bodies and objects | bullying and exclusion |
| `COMP-LOW-VULNERABLE` | camera slightly above or crowd eye level, victim lower in frame | shame, power imbalance |
| `COMP-PSYCHO-CLOSE` | eyes and hair dominate, compressed background, one prop reflection | emotional reaction |
| `COMP-CORRIDOR-SIDE` | side-profile subject against repeated doors, windows, or wall panels | school isolation |
| `COMP-DUTCH-SURREAL` | mild tilted horizon, simple mascot in foreground, human farther back | comedic or unsettling surreal contrast |
| `COMP-ENSEMBLE-LAYERS` | foreground, midground, and background children each carry different reactions | classroom or playground social field |

## Lens-impression controls

- `LENS-WIDE-SOCIAL`: 24-32mm impression, close camera, clear foreground enlargement, readable group geography.
- `LENS-NORMAL-RELATION`: 40-55mm impression, balanced person/environment relation.
- `LENS-CLOSE-EMOTION`: 75-100mm impression, compressed background and isolated face.
- `LENS-MILD-FISHEYE`: controlled edge stretch for subjective pressure; use only with a readable center and user approval.

These are static perspective descriptions, not time-based camera moves.

## Light systems

| ID | Source and behavior | Color role |
|---|---|---|
| `LIGHT-OVERCAST-DAY` | large soft sky source, mild top-front direction, open face mids | cyan-white sky, cool grey shadow, natural greens |
| `LIGHT-WARM-WALL` | hard or semi-hard daylight bouncing from a pale wall | warm skin edge, soft grey interior shadow |
| `LIGHT-SCHOOL-WINDOW` | lateral window light with darker corridor falloff | faded teal and salmon architecture, cool face shadow |
| `LIGHT-BACKLIT-SKY` | bright sky behind profiles, pale hair rim, restrained bloom | cyan background, neutral skin, dark hair mass |
| `LIGHT-PSYCHO-LOCAL` | ordinary source with locally deepened hair and eye shadows | brown-green or grey-violet pressure zone |

## Expression controls

- `EXPR-OPEN`: relaxed eyelids, small mouth, ordinary posture.
- `EXPR-PLAYFUL-MASK`: smiling eyes or raised mouth corner with socially controlling body position.
- `EXPR-WATCHFUL`: one eye angle change, head tilt, quiet observation.
- `EXPR-SUPPRESSED`: lowered gaze, inward shoulders, closed mouth, fingers pressing fabric or bag strap.
- `EXPR-EXHAUSTED`: heavy lower eyelids, slightly parted or compressed lips, sparse under-eye hatching.
- `EXPR-SHOCKED-CHILD`: large eyes, small open mouth, rigid shoulders; keep anatomy simple.

## Finish controls

- `FINISH-CEL-CLEAN`: clean flat fills, sparse shadow shapes, faint paper grain.
- `FINISH-CEL-SOFT`: restrained cel fill plus soft ambient contamination and mild bloom.
- `FINISH-PSYCHO-HATCH`: baseline cel rendering plus localized pencil hatching and denser shadow texture.
- `FINISH-PAINTED-BG`: simple character surfaces against textured hand-painted foliage, classrooms, roads, or corridors.

## Compatibility gate

Verify:

- one primary rendering lane;
- one dominant composition;
- one lens impression;
- one motivated light system;
- one baseline finish plus at most one local psychological finish;
- identities and group count match the references;
- the frozen moment reads from a single still image;
- the model-facing prompt contains no source names and no video structure.
