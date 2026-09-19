# Composition Case Library

This file stores user-fed film composition cases and reusable visual grammar. Do not claim a pattern is trained until it is recorded here and counted in `training-progress.md`.

## Case Entry Template

Use this exact structure when adding a new case:

```markdown
## Case N - Title / Source / Scene

- Date added:
- Source certainty:
- User-provided material:

### Narrative Layer

- 情绪基调:
- 人物关系:
- 剧情节点:
- 叙事功能:

### Visual Layer

- 景别:
- 机位:
- 构图法则:
- 光影:
- 色彩:
- 画面层次:
- 镜头 / 焦段 / 景深:
- 运动 / 剪辑 / 声音:

### Language Layer

- 提示词参考:
- 关键词提取:
- AIGC 可见锚点:

### Reuse

- 用这个手法的原因:
- 如何用:
- 适用场景:
- 风险与反例:

### Deposited Rule

One reusable rule in 1-3 sentences.
```

## Current Library Status

No user-fed film composition case has been formally deposited yet. The PDF manual has been ingested as a method framework, not as a trained film-style library.

## Reusable Framework Entries From The Manual

### Entry 1 - Geometry Must Serve Story Information

Composition rules are chosen after the narrative function is clear. Symmetry, negative space, leading lines, frame-within-frame, and Dutch angles are not decorative labels; each must explain what the audience should feel, know, miss, or fear.

### Entry 2 - Three-Layer Composition Diagnosis

Every frame must be split into narrative layer, visual layer, and language layer. This prevents pure theory from failing at prompt execution.

### Entry 3 - Positive / Negative / Comparison Training

The fastest way to learn a composition style is not only to collect good frames, but to compare good and weak versions of the same scene. Record what the good version does with subject placement, depth, light, and eye path that the weak version lacks.

### Entry 4 - AIGC Prompt Transfer

A film composition cannot be copied by naming the film alone. Translate it into visible prompt anchors: camera side, subject scale, body direction, lens compression or distortion, light source, depth layers, color palette, movement path, and sound environment.

## Future Case Families To Build

Use these buckets when the user starts feeding "神级构图":

- object POV and prop-framed openings
- surveillance / monitor / CCTV compositions
- public-space rupture and crowd reaction staging
- death-impact or sudden accident compositions
- empty street / worldline shift compositions
- dialogue power-triangle compositions
- over-shoulder and shoulder-neck viewpoint precision
- low-angle heroic or oppressive character entry
- negative-space isolation frames
- frame-within-frame containment shots
- moving crowd vs static subject contrast
- ring / phone / glass / reflective-object symbolic inserts

## Training Round 2026-06-25 - Classic Composition Seed Set

User-fed materials: 21 reference images and notes covering `2001: A Space Odyssey`, `The Grand Budapest Hotel`, `The Godfather`, `Blade Runner 2049`, `In the Mood for Love`, `Arrival`, and `Dune`. Source certainty follows the user's labels; some images are reference composites or repeated examples rather than individually verified film frames.

This round initially created transferable composition mechanisms, but the first pass was too coarse for the user's required training standard. Future revisions of these cases must be expanded into the mandatory `叙事层 / 视觉层 / 语言层 / 复刻与运用 / 沉淀条目` format.

## Case 1 - 2001 / Circular Module Center-Perspective Order

- Date added: 2026-06-25
- Source certainty: user-labeled classic film frame
- User-provided material: Image #1
- Scene function: sterile future-space environment with a human figure subordinated to architecture
- Emotional target: technological order, ritualized control, institutional calm

### Frame Facts

- Subject: a person centered inside a narrow doorway, holding a tray, surrounded by a circular space-module structure
- Camera position: dead-center, square to the architecture axis
- Shot size: wide interior shot
- Camera height / angle: eye-level to slightly low, neutral frontal view
- Estimated focal length / lens behavior: moderate wide lens, enough to show side wall depth without turning the frame chaotic
- Subject screen position: exact center, vertically framed by the doorway
- Foreground: side walls and dark lower arch form a tunnel mouth
- Midground: concentric circular module rings
- Background: bright doorway and centered figure
- Light sources: practical overhead panels and bright doorway backlight
- Color palette: white, black, muted gold, clinical warm-neutral
- Motion / edit / sound: works best with slow, frictionless camera or static hold; quiet mechanical ambience

### Composition Mechanism

- Dominant geometry: concentric circles around a centered human axis
- Main composition rules: absolute symmetry, center framing, frame-within-frame, circular containment
- Visual weight: architecture dominates; the person is a scale marker
- Eye path: outer ring -> inner ring -> doorway -> face/body center
- Negative space / containment: black circular arc compresses the subject into a technological aperture
- Power relation: environment/system over individual

### Why It Works

- Narrative reason: the world feels governed by machine order before the character even acts
- Emotional reason: calm becomes uncanny because the image is too controlled
- Spatial reason: circular repetition makes depth instantly readable
- AIGC reliability reason: strong geometric anchors reduce composition drift

### How To Reuse

- Best scene types: sci-fi institution, lab threshold, time-machine chamber, AI-controlled space, ritual entrance
- Required setup: central doorway, repeated circular or arched frames, small human centered inside
- Camera and lens recipe: locked-off or slow dolly, center axis, 24-35mm equivalent, deep focus
- Lighting recipe: clean practical panels, bright central threshold, dark ring edges
- Prompt anchors: `camera exactly centered on circular doorway axis`, `concentric architectural rings`, `small centered human figure`, `white black muted-gold sci-fi interior`
- Common failure: model shifts camera off-axis or makes the circle decorative instead of structural
- Anti-example: random curved corridor with centered character but no nested circular hierarchy

### Deposited Rule

When the story needs "system order over the person", let architecture become the main subject and place the human as a centered scale marker inside repeated geometric frames.

## Case 2 - 2001 / Hexagonal Corridor Leading-Line Ritual

- Date added: 2026-06-25
- Source certainty: user-labeled classic film frame
- User-provided material: Image #2
- Scene function: movement through a futuristic corridor
- Emotional target: procedural progress, technological awe, controlled passage

### Frame Facts

- Subject: red-suited astronaut moving away through a white hexagonal corridor
- Camera position: centered behind the subject on the corridor axis
- Shot size: wide full-body corridor shot
- Camera height / angle: eye-level, frontal axis into vanishing point
- Estimated focal length / lens behavior: moderate wide, strong perspective convergence
- Subject screen position: near center, vertical red shape interrupting white geometry
- Foreground: nearest glowing hexagon frame
- Midground: astronaut and repeated wall panels
- Background: shrinking nested corridor frames
- Light sources: linear practical strips on hexagonal ribs
- Color palette: white/black clinical architecture with red-orange human contrast
- Motion / edit / sound: slow floating walk or glide; low mechanical hum, suit movement

### Composition Mechanism

- Dominant geometry: repeated hexagonal tunnel shrinking into one-point perspective
- Main composition rules: symmetry, leading lines, center-axis perspective, color isolation
- Visual weight: red astronaut draws the eye while corridor lines pull forward
- Eye path: luminous ribs -> astronaut -> distant vanishing point
- Negative space / containment: white tunnel encloses the figure
- Power relation: body is inside an engineered path, not free space

### Why It Works

- Narrative reason: movement itself becomes a ritual through the system
- Emotional reason: precision gives awe and unease at the same time
- Spatial reason: repeated hexagons make depth measurable
- AIGC reliability reason: clear vanishing point and repeated light ribs are easy to lock

### How To Reuse

- Best scene types: sci-fi corridor, lab passage, entering a restricted zone, time-machine access route
- Required setup: repeated polygonal frames and a high-contrast subject
- Camera and lens recipe: centered tracking shot, 24-28mm equivalent, deep focus
- Lighting recipe: practical strip lights on each repeating frame
- Prompt anchors: `one-point perspective hexagonal corridor`, `repeating luminous ribs`, `red figure centered`, `deep focus symmetrical sci-fi passage`
- Common failure: corridor becomes a generic hallway without polygon repetition
- Anti-example: off-center handheld corridor where lines no longer converge cleanly

### Deposited Rule

For "entering a system" shots, use repeated geometric corridor frames and center-axis tracking; the character's motion becomes submission to the path.

## Case 3 - Grand Budapest / Pastel Frontal Symmetry And Storybook Order

- Date added: 2026-06-25
- Source certainty: user-labeled classic examples
- User-provided material: Images #3 and #4
- Scene function: establish an artificial, nostalgic, storybook world
- Emotional target: whimsical order, nostalgia, elegant absurdity

### Frame Facts

- Subject: hotel facade or town street aligned to the image center
- Camera position: frontal, square, no diagonal search
- Shot size: establishing wide shot
- Camera height / angle: level, postcard-like
- Estimated focal length / lens behavior: normal to mild telephoto for flattened, miniature-like organization
- Subject screen position: architecture locked to center
- Foreground: snow, street kiosk, small figures, street objects
- Midground: building facade or central street axis
- Background: pink forest/sky or converging street
- Light sources: soft diffused daylight
- Color palette: pastel pink, white, pale blue, gentle warm accents
- Motion / edit / sound: works with static hold, precise lateral movement, or clean centered cut; light street ambience

### Composition Mechanism

- Dominant geometry: frontal bilateral symmetry plus repeated facade/window modules
- Main composition rules: center framing, absolute symmetry, color harmony, controlled miniature depth
- Visual weight: central building or kiosk anchors the frame; paired side elements reinforce order
- Eye path: center object -> mirrored sides -> upper facade/sky
- Negative space / containment: sky and snow simplify the frame
- Power relation: not domination, but authored storybook control

### Why It Works

- Narrative reason: before plot starts, the visual grammar tells the viewer this world is curated and artificial
- Emotional reason: pastel order makes the scene charming, nostalgic, and faintly unreal
- Spatial reason: strict frontal alignment prevents attention leakage
- AIGC reliability reason: symmetry, pastel palette, and facade repetition are strong generation anchors

### How To Reuse

- Best scene types: stylized opening, comedic institution, fairy-tale hotel, nostalgic town, ceremonial exterior
- Required setup: frontal architecture, paired side details, clean sky/ground bands
- Camera and lens recipe: locked frontal camera, normal/mild telephoto lens, high depth of field
- Lighting recipe: cloudy soft daylight, low contrast, clean shadows
- Prompt anchors: `perfect frontal symmetrical facade`, `pastel pink and white palette`, `soft diffused daylight`, `storybook miniature-like wide shot`
- Common failure: adding dramatic shadows or random asymmetry destroys the authored charm
- Anti-example: angled architectural shot with messy color accents and no paired side elements

### Deposited Rule

For whimsical/artificial worlds, make the camera obedient: frontal axis, centered subject, paired side objects, soft light, and a restricted pastel palette.

## Case 4 - Godfather / Low-Key Power Portrait And Venetian-Blind Shadow

- Date added: 2026-06-25
- Source certainty: user-labeled classic examples
- User-provided material: Images #5, #6, #21
- Scene function: encode authority, secrecy, and emotional unreadability
- Emotional target: danger beneath calm, paternal power, moral shadow

### Frame Facts

- Subject: seated or leaning male authority figure in dark suit, sometimes paired with another man
- Camera position: close to medium close, frontal or three-quarter
- Shot size: close shot / medium close shot
- Camera height / angle: eye-level or slightly low for authority
- Estimated focal length / lens behavior: normal to mild telephoto, compressed intimate office space
- Subject screen position: center or right-of-center, surrounded by heavy darkness
- Foreground: hands, cigarette, clasped arms, or another man's shoulder/body
- Midground: face, suit, rose, hands
- Background: venetian blinds, lamp, dark office walls
- Light sources: hard top/side tungsten, narrow window-blind light
- Color palette: black, brown, warm amber, white shirt, small red rose accent
- Motion / edit / sound: minimal movement, low voice, room tone, cigarette/cloth/hand foley

### Composition Mechanism

- Dominant geometry: face isolated by darkness and vertical blind pattern
- Main composition rules: low-key chiaroscuro, negative black space, partial face shadow, symbolic color anchor
- Visual weight: face and hands compete; eyes may be partly hidden
- Eye path: lit forehead/cheek -> shadowed eyes -> hand gesture -> red rose or white shirt
- Negative space / containment: darkness swallows room edges and hides intention
- Power relation: subject controls information by withholding visibility

### Why It Works

- Narrative reason: power is expressed through concealment, not volume
- Emotional reason: unreadable eyes make the viewer lean in and distrust the calm
- Spatial reason: blinds create prison-like rhythm and moral division
- AIGC reliability reason: clear light direction and limited color palette prevent generic "dark room" output

### How To Reuse

- Best scene types: underworld authority, secret negotiation, father figure, interrogative intimacy
- Required setup: dark room, hard top/side key, venetian blinds or slit light, visible hands
- Camera and lens recipe: close/medium close, 50-85mm equivalent, shallow to moderate depth
- Lighting recipe: warm hard key from above/front side, eyes recessed into brow shadow, background mostly black
- Prompt anchors: `low-key warm tungsten office`, `eyes partly hidden in shadow`, `venetian blind light stripes`, `hands visible as power gesture`, `small red color accent`
- Common failure: over-brightening the eyes removes mystery
- Anti-example: evenly lit portrait with no black negative space and no hand/facial hierarchy

### Deposited Rule

For deep power and hidden intention, do not brighten the whole face; let the eyes disappear partially while hands or small color accents carry controlled visual information.

## Case 5 - Godfather / Group Power Circle And Oil-Painting Office Layers

- Date added: 2026-06-25
- Source certainty: user-labeled classic example
- User-provided material: Image #7
- Scene function: group hierarchy and family/political power map
- Emotional target: closed-room authority, social pressure, alliance and threat

### Frame Facts

- Subject: multiple men arranged around an office, with one or more seated power centers
- Camera position: wide interior, slightly below standing eye level
- Shot size: group wide / ensemble medium-wide
- Camera height / angle: neutral, observational
- Estimated focal length / lens behavior: normal wide, keeps all bodies legible
- Subject screen position: semicircle/circle arrangement around the frame
- Foreground: seated bodies, chair edges, dog or low object as domestic contrast
- Midground: core men, hands, drinks, chairs
- Background: windows, desk, shelves, office texture
- Light sources: window light plus warm practicals
- Color palette: tobacco brown, cream, black, warm desk-light highlights
- Motion / edit / sound: still group pose, murmured conversation, glass/cloth/chair foley

### Composition Mechanism

- Dominant geometry: semicircle of bodies around social power
- Main composition rules: ensemble blocking, depth layering, visual hierarchy by height and center access
- Visual weight: seated central/left figure and bright faces compete with standing silhouettes
- Eye path: central seated figure -> surrounding advisors -> foreground body/object -> back windows
- Negative space / containment: dense room limits escape
- Power relation: hierarchy appears as physical placement and gaze direction

### Why It Works

- Narrative reason: audience instantly reads the room as a power network
- Emotional reason: social pressure comes from being surrounded
- Spatial reason: multiple planes make the scene feel lived-in and strategic
- AIGC reliability reason: "semicircle around central authority" is clearer than "many men in a room"

### How To Reuse

- Best scene types: family council, research committee, villain meeting, team moral debate
- Required setup: seated center, surrounding secondary figures, background office texture
- Camera and lens recipe: static wide, 28-35mm equivalent, deep enough focus for ensemble
- Lighting recipe: warm window/practical mix, faces selectively lit, corners fall into shadow
- Prompt anchors: `ensemble group arranged in a semicircle`, `central seated authority`, `warm low-key office`, `foreground body layer and background windows`
- Common failure: characters line up flatly like a school photo
- Anti-example: all people same distance from camera, same height, same light

### Deposited Rule

For group power scenes, arrange bodies as a social diagram: center controls, sides advise or pressure, foreground blocks escape, background defines institution.

## Case 6 - Blade Runner 2049 / Monumental Science-Fiction Scale And Atmosphere

- Date added: 2026-06-25
- Source certainty: user-labeled examples and related visual references
- User-provided material: Images #8, #16, #17, #18, #20
- Scene function: make the individual feel small inside a built technological world
- Emotional target: loneliness, awe, synthetic divinity, urban alienation

### Frame Facts

- Subject: small figures, city traveler, vehicle, or two-person confrontation embedded in vast architecture/weather
- Camera position: wide symmetrical axis for monumental rooms; low/wide city view for exterior scale; side profile for intimate confrontation
- Shot size: extreme wide to wide; medium-wide for dialogue
- Camera height / angle: low or centered, often making structures tower over people
- Estimated focal length / lens behavior: wide for scale and depth; telephoto compression can be used for dense neon street signs
- Subject screen position: tiny centered figure, foreground traveler, or side-profile pair
- Foreground: wet ground, vehicle, silhouetted body, glass cases, signage, rain
- Midground: main figure/object
- Background: massive architecture, fog, neon, luminous panels, industrial structures
- Light sources: volumetric beams, neon signage, cold backlight, rain-reflected practicals
- Color palette: cyan/blue haze, amber/gold interiors, magenta neon, black silhouettes
- Motion / edit / sound: rain, low drone, distant aircraft, electrical hum, wet footsteps

### Composition Mechanism

- Dominant geometry: monumental verticals, symmetrical aisles, giant slabs, luminous haze
- Main composition rules: scale contrast, negative space, symmetry, volumetric depth, color isolation
- Visual weight: huge architecture outweighs human body
- Eye path: light source/beam -> tiny subject -> receding architecture -> atmospheric depth
- Negative space / containment: fog and darkness enlarge the void around the subject
- Power relation: city/system/species-scale world over the individual

### Why It Works

- Narrative reason: the story world feels older, larger, and colder than the character
- Emotional reason: beautiful scale becomes existential pressure
- Spatial reason: fog/rain/volume light separate planes and reveal distance
- AIGC reliability reason: "tiny subject vs massive structure" gives the model a clear size relation

### How To Reuse

- Best scene types: future dictatorship, mega-lab, white-tower exterior, ruined city, synthetic god image, lonely arrival
- Required setup: one tiny subject or vehicle against a massive structure, with haze/rain/light beams
- Camera and lens recipe: extreme wide/low angle for exteriors, centered wide for interiors, side silhouette for intimate sci-fi dialogue
- Lighting recipe: cold atmosphere plus one dominant warm or magenta practical source; visible haze to show beams
- Prompt anchors: `tiny human figure against monumental architecture`, `volumetric fog and rain`, `cold cyan atmosphere with isolated warm light`, `wet reflective ground`, `massive geometric slabs`
- Common failure: adding too many medium-scale details reduces awe
- Anti-example: hero fills the frame equally with background building, losing scale contrast

### Deposited Rule

For futuristic loneliness, make the environment the giant and the person the measurement unit; haze, rain, and one isolated light source turn scale into emotion.

## Case 7 - In The Mood For Love / Emotional Frame, Reflection, And Warm Partition

- Date added: 2026-06-25
- Source certainty: user-labeled classic examples
- User-provided material: Images #9, #10, #11
- Scene function: show intimacy blocked by social space and unspoken restraint
- Emotional target: longing, secrecy, distance, pressure under beauty

### Frame Facts

- Subject: woman framed by window/door, man reflected or separated by mirror/partition, narrow hallway texture
- Camera position: outside looking through frames, or interior side angle across a partition
- Shot size: medium shot / medium-wide
- Camera height / angle: eye-level, voyeuristic but controlled
- Estimated focal length / lens behavior: normal to mild telephoto, compressing cramped rooms and hallway layers
- Subject screen position: often off-center, trapped by vertical frame bars
- Foreground: doorframe, window edge, curtain, plant, mirror edge
- Midground: woman or reflected man
- Background: lamp, patterned wall, bed, corridor, red curtain
- Light sources: warm practical lamps, dim interior spill, occasional cool contrast from outside
- Color palette: amber, red, green, floral/patterned surfaces, low-key warmth
- Motion / edit / sound: stillness, small head/hand movement, cloth rustle, distant hallway ambience

### Composition Mechanism

- Dominant geometry: vertical partitions and reflective split space
- Main composition rules: frame-within-frame, mirror composition, partial obstruction, warm color enclosure
- Visual weight: subject is beautiful but constrained; frame edges dominate behavior
- Eye path: foreground frame -> face/hand -> reflection/empty adjacent space -> lamp color anchor
- Negative space / containment: narrow rooms and doorframes become emotional cages
- Power relation: social rules/space separate people who are emotionally near

### Why It Works

- Narrative reason: love is present but cannot occupy open space
- Emotional reason: partial views make desire feel withheld
- Spatial reason: frames and reflections allow two people to share a frame while remaining apart
- AIGC reliability reason: physical partitions give concrete anchors for "emotional distance"

### How To Reuse

- Best scene types: restrained romance, awkward intimacy, secret observation, unspoken goodbye, parallel identities
- Required setup: door/window/mirror, warm practicals, foreground obstruction, patterned room texture
- Camera and lens recipe: static or slow slide, 35-70mm equivalent, shallow to moderate depth
- Lighting recipe: warm lamps, soft falloff, shadows on frame edges, low saturation in dark corners
- Prompt anchors: `woman framed by doorway`, `man visible only through mirror reflection`, `warm amber practical lamps`, `vertical partition splitting emotional space`, `patterned walls and soft shadow`
- Common failure: placing characters in open space removes restraint
- Anti-example: clean two-shot with no foreground obstruction, no frame, no reflection

### Deposited Rule

For forbidden or restrained intimacy, do not let characters simply face each other in open space; separate them with doors, mirrors, curtains, and warm practical light.

## Case 8 - Arrival / Triple Frame Isolation And Window-Silhouette Fate

- Date added: 2026-06-25
- Source certainty: user-labeled repeated examples
- User-provided material: Images #13, #14, #15
- Scene function: isolate a character before a vast unknown event
- Emotional target: loneliness, fate, quiet dread, "seeing but not touching"

### Frame Facts

- Subject: lone woman silhouetted inside a modern home, facing a huge window and outside landscape
- Camera position: interior wide shot looking toward window wall
- Shot size: wide full-room shot
- Camera height / angle: eye-level, static
- Estimated focal length / lens behavior: moderate wide, deep interior readable
- Subject screen position: near center, small against window architecture
- Foreground: dark furniture and room shapes
- Midground: silhouetted person and window/door frames
- Background: bright gray-blue exterior with trees/water/sky
- Light sources: overcast exterior daylight; interior remains underexposed
- Color palette: blue gray, black silhouette, muted green/stone
- Motion / edit / sound: stillness, soft room tone, distant exterior ambience, quiet breath

### Composition Mechanism

- Dominant geometry: nested rectangular frames around a small silhouette
- Main composition rules: triple frame, center framing, silhouette, size contrast
- Visual weight: window is brighter/larger than the person
- Eye path: bright exterior -> dark silhouette -> nested door/window borders -> empty room
- Negative space / containment: large glass wall becomes a soft barrier
- Power relation: fate/world/event outside dominates interior human control

### Why It Works

- Narrative reason: the character is visually placed before an event too large to grasp
- Emotional reason: backlit silhouette removes facial detail and turns the person into a vulnerable outline
- Spatial reason: interior darkness vs exterior brightness creates a threshold
- AIGC reliability reason: "small silhouette against large window" is a clean, controllable setup

### How To Reuse

- Best scene types: receiving impossible news, alien/time event, future vision, quiet revelation, memory isolation
- Required setup: large window/door grid, dark interior, bright cold exterior
- Camera and lens recipe: static wide, 28-35mm equivalent, deep focus
- Lighting recipe: natural overcast backlight, interior exposure low, no strong face fill
- Prompt anchors: `lone silhouette centered before huge glass window`, `dark interior foreground`, `cold blue-gray overcast exterior`, `nested rectangular frames`, `quiet isolated wide shot`
- Common failure: lighting the face too clearly breaks the isolation
- Anti-example: close-up reaction shot that explains emotion instead of letting space carry it

### Deposited Rule

For fate and unknowability, make the outside world bright and unreachable, the interior dark and still, and the person a small centered silhouette caught between frames.

## Case 9 - Dune / Apocalyptic Scale Silhouette

- Date added: 2026-06-25
- Source certainty: user-labeled classic example
- User-provided material: Image #19
- Scene function: show human smallness before environmental and historical catastrophe
- Emotional target: epic dread, survival, mythic distance

### Frame Facts

- Subject: two silhouetted figures on a ridge, smoke columns and distant fires behind them
- Camera position: low distant wide, watching figures as silhouettes
- Shot size: extreme wide / long shot
- Camera height / angle: low horizon-level, slightly looking across landscape
- Estimated focal length / lens behavior: moderate long/wide landscape compression, minimal facial detail
- Subject screen position: near center/right, small against smoke and sky
- Foreground: dark ridge line
- Midground: standing figures
- Background: smoke plumes, fires, flying object, mountains/sky
- Light sources: low exterior backlight and fire glow
- Color palette: dusk gray, smoke black, ember orange
- Motion / edit / sound: wind, distant explosions, low rumble, ash/sand movement

### Composition Mechanism

- Dominant geometry: horizontal ridge plus vertical smoke columns
- Main composition rules: silhouette, scale contrast, negative sky, environmental dominance
- Visual weight: smoke columns outweigh human forms
- Eye path: silhouettes -> fire line -> smoke columns -> sky object
- Negative space / containment: sky and smoke swallow detail
- Power relation: history/environment/war over people

### Why It Works

- Narrative reason: disaster is shown through aftermath scale, not exposition
- Emotional reason: people become witnesses, not masters
- Spatial reason: horizon line grounds the bodies while vertical smoke gives epic height
- AIGC reliability reason: simple silhouettes against smoke are controllable and legible

### How To Reuse

- Best scene types: future war memory, ruined world vision, apocalyptic prophecy, aftermath reveal
- Required setup: small figures on ridge, multiple vertical smoke columns, distant fire line
- Camera and lens recipe: locked extreme wide, low horizon, deep focus
- Lighting recipe: backlight/dusk silhouette, fire glow at ground plane
- Prompt anchors: `two tiny silhouetted figures on dark ridge`, `multiple towering smoke columns`, `distant fires across horizon`, `wide apocalyptic landscape`, `gray dusk sky with ember glow`
- Common failure: making figures too large or facially detailed removes epic distance
- Anti-example: medium shot of people reacting with explosions behind them

### Deposited Rule

For epic catastrophe, keep humans small and unreadable; let smoke, horizon, and distant fire carry the scale of history.

## Case 10 - Blade Runner 2049 / Side-Backlight Two-Person Tension

- Date added: 2026-06-25
- Source certainty: user-labeled classic example
- User-provided material: Image #20
- Scene function: intimate confrontation inside industrial/cybernetic weather
- Emotional target: fragile contact, distrust, melancholy tension

### Frame Facts

- Subject: two wet figures facing each other in profile, hands meeting near center
- Camera position: side-on, medium-wide, bodies in silhouette
- Shot size: medium-wide two-shot
- Camera height / angle: eye-level
- Estimated focal length / lens behavior: normal lens, moderate compression, background industrial forms readable
- Subject screen position: woman left, man right, hands center
- Foreground: dark bodies and hands
- Midground: faces in profile, wet clothing/hair
- Background: stairs, industrial silhouettes, cyan fog, small practical light
- Light sources: strong cyan backlight/top backlight, low practical glow
- Color palette: teal/cyan, black, wet highlights
- Motion / edit / sound: rain, breath, hand contact, distant machinery, low drone

### Composition Mechanism

- Dominant geometry: two opposing vertical silhouettes connected by central hands
- Main composition rules: profile opposition, side backlight, central hand anchor, negative space between faces
- Visual weight: hands become emotional hinge
- Eye path: woman's face -> joined hands -> man's face -> background light
- Negative space / containment: gap between heads carries emotional distance
- Power relation: neither dominates fully; contact is tense and temporary

### Why It Works

- Narrative reason: the relationship is shown through hand contact, not explanatory dialogue
- Emotional reason: silhouettes hide expression while body distance reveals tension
- Spatial reason: industrial background frames intimacy as fragile within a cold world
- AIGC reliability reason: left/right profile and center-hand contact are specific enough to generate

### How To Reuse

- Best scene types: tense alliance, reluctant confession, rescue hesitation, identity recognition, sci-fi romance
- Required setup: two people in profile, wet/cold environment, central hand contact
- Camera and lens recipe: side-on medium-wide, 35-50mm equivalent, moderate depth
- Lighting recipe: strong cyan backlight, rain/haze to reveal rim light, minimal front fill
- Prompt anchors: `side profile two-shot`, `woman on left man on right`, `hands meeting at exact center`, `cyan backlight through rain and mist`, `industrial silhouettes in background`
- Common failure: turning it into a frontal romantic embrace
- Anti-example: bright evenly lit two-shot with full facial detail and no central hand anchor

### Deposited Rule

For intimate tension in a cold world, use side profiles, central hand contact, and backlight silhouette; the gap between faces is the emotional battlefield.

## Case 11 - Noir Office Smoke Layers / Horizontal Compartment Frame

- Date added: 2026-06-25
- Source certainty: user-fed reference composite
- User-provided material: Image #12
- Scene function: encode thinking, pressure, bureaucracy, secrecy
- Emotional target: dense interior anxiety, mental fog, procedural burden

### Frame Facts

- Subject: seated man at desk, cigarette smoke above/around him
- Camera position: looking through horizontal architectural/desk/window divisions
- Shot size: medium to medium-wide office shot
- Camera height / angle: slightly high or level, observing through frame compartments
- Estimated focal length / lens behavior: normal lens, layered but compressed interior
- Subject screen position: lower compartment or center-bottom, often back or downward gaze
- Foreground: dark horizontal frame edge
- Midground: smoke and desk objects
- Background: office shelves/walls/windows
- Light sources: hard practical/top light, narrow strips, low room fill
- Color palette: black, brown, nicotine amber, smoke gray-blue
- Motion / edit / sound: drifting smoke, paper, pen, phone, low room hum

### Composition Mechanism

- Dominant geometry: horizontal compartments plus drifting smoke
- Main composition rules: frame-within-frame, atmosphere layer, object clutter as psychological pressure
- Visual weight: smoke occupies more space than the body, turning thought into visible texture
- Eye path: smoke -> head/hand -> desk objects -> dark frame
- Negative space / containment: dark borders press down on the character
- Power relation: institution/workload traps the person inside a box

### Why It Works

- Narrative reason: mental pressure becomes visible through smoke and object density
- Emotional reason: the frame feels like watching someone through a sealed office tank
- Spatial reason: horizontal divisions produce compartments of thought/action
- AIGC reliability reason: smoke and frame edges give visible anchors for "oppressive interior"

### How To Reuse

- Best scene types: late-night planning, detective/research work, corporate conspiracy, time-machine rule deduction
- Required setup: desk, smoke or haze, horizontal frame edge, low light, cluttered props
- Camera and lens recipe: static medium-wide through obstruction, 35-50mm equivalent
- Lighting recipe: top/practical light, dark edges, smoke catching a white strip of light
- Prompt anchors: `man seated at cluttered desk seen through horizontal frame`, `cigarette smoke drifting in upper layer`, `low-key warm office`, `dark borders compressing the image`
- Common failure: smoke becomes decorative fog unrelated to subject
- Anti-example: clean bright office desk with no atmospheric layer and no frame division

### Deposited Rule

For thinking under pressure, give the frame compartments and air texture: smoke/haze above, desk objects below, and the person trapped between horizontal borders.

## Training Round 2026-06-25 - Four User-Fed Composition Practice Set

User-fed materials: four reference frames for self-analysis, self-audit, correction, and knowledge-base deposit. Source certainty is based on visible frames and user material; composition facts are prioritized over film-title naming.

## Case 12 - Mirror / Doorway / Split Family Witness Frame

- Date added: 2026-06-25
- Source certainty: user-fed screenshot; visible composition facts prioritized
- User-provided material: current Image #1

### Narrative Layer

- 情绪基调: domestic unease, psychological fracture, child witnessing adult instability.
- 人物关系: adult male dominates the room in the right foreground; the child is small and distant in the doorway; the mirror exposes the adult's front while his physical body faces away.
- 剧情节点: a tense bedroom encounter where the child enters or observes the adult from a threshold.
- 叙事功能: split the adult into body and reflection, making the room feel psychologically divided; place the child in a doorway to show separation, fear, and witness status.

### Visual Layer

- 景别: wide interior / medium-wide bedroom tableau.
- 机位: static eye-level or slightly low eye-level from inside the bedroom, looking diagonally across bed, mirror, and door.
- 构图法则: mirror reflection composition, frame-within-frame, triangular blocking, threshold framing, foreground/midground/background hierarchy.
- 光影: low interior light with muted warm-pink walls and greenish shadow; the doorway is brighter, while the mirror and bed area remain heavier and more oppressive.
- 色彩: muted pink, gray-blue robe, yellow door light, dark wood, sickly green undertone.
- 画面层次: foreground right = adult body on bed; midground left = dresser mirror reflecting the same adult's face; background center = child framed by open door; architecture links all three points.
- 镜头 / 焦段 / 景深: moderate wide lens, deep enough focus to keep adult body, mirror reflection, and child readable at once.
- 运动 / 剪辑 / 声音: best as a held shot; tiny hand gesture, robe/bed cloth friction, room tone, distant hallway air.

### Language Layer

- 提示词参考: `wide bedroom interior, adult man seated on the right foreground bed with his back and profile to camera, the left dresser mirror reflects the same man's front face, small child standing in the open doorway at center background, triangular blocking, muted pink walls, dim uneasy domestic light, deep focus, mirror and doorway both visible`
- 关键词提取: `same person reflected in mirror`, `child in doorway`, `triangular blocking`, `split identity`, `deep focus bedroom`, `threshold witness`.
- AIGC 可见锚点: explicitly state that the mirror shows the same adult, not a second man; child is centered in the open doorway; adult body is large on the right foreground bed.

### Reuse

- 用这个手法的原因: it turns a normal room into a psychological map without dialogue.
- 如何用: place the emotionally unstable subject as a large foreground body, reveal their face in a mirror, and place the witness or vulnerable character at a doorway behind them.
- 适用场景: family dread, child witnessing danger, split identity, hidden emotional truth, a character being watched without direct confrontation.
- 风险与反例: if the mirror is treated as a decorative duplicate, the shot collapses; if the child is made too large or too close, the witness distance disappears.

### Self-Audit Correction

- Good: the analysis must catch the three-point geometry: real body, reflected face, doorway child.
- Missing risk: do not describe it as "mirror symmetry"; it is not symmetrical, it is a split-view psychological triangle.
- Correction: always lock mirror physics and subject identity in AIGC prompt language.

### Deposited Rule

When using mirrors in tense interiors, the mirror must reveal information the physical body hides. Add a doorway witness only when distance, fear, or moral observation matters.

## Case 13 - Window-Grid Silhouette / Aftermath Bond Against The City

- Date added: 2026-06-25
- Source certainty: user-fed screenshot; likely a well-known ending frame, but visible facts remain primary
- User-provided material: current Image #2

### Narrative Layer

- 情绪基调: rupture, fragile intimacy, post-crisis stillness, strange calm after collapse.
- 人物关系: two figures stand side by side, physically connected by hands, facing the city rather than each other.
- 剧情节点: aftermath or ending beat where private connection is framed against a damaged or unstable urban world.
- 叙事功能: make the emotional relationship small but clear, while the city outside carries the larger consequence.

### Visual Layer

- 景别: wide interior silhouette shot.
- 机位: static eye-level camera behind the pair, looking outward through a huge window wall.
- 构图法则: window-grid frame-within-frame, backlit silhouette, center pair blocking, negative exterior space, scale contrast.
- 光影: cold blue/cyan city backlight; interior foreground falls into black silhouette; practical lamp or office light accents on the side.
- 色彩: cyan-blue exterior, black silhouettes, small warm practical highlights.
- 画面层次: foreground = dark interior clutter and two bodies; midground = window grid; background = night skyline and distant urban light.
- 镜头 / 焦段 / 景深: moderate wide lens, deep background readable; faces intentionally unreadable.
- 运动 / 剪辑 / 声音: should hold still after motion; distant city rumble, glass/room air, quiet breathing, line delivery or silence can sit over the image.

### Language Layer

- 提示词参考: `wide interior shot from behind two silhouetted people holding hands in front of a floor-to-ceiling window grid, cold cyan night city skyline outside, dark office foreground, fragile stillness after urban rupture, faces hidden, strong backlight, rectangular window frames dividing the skyline`
- 关键词提取: `backlit silhouettes`, `window grid`, `two figures holding hands`, `city aftermath`, `cyan night`, `dark interior foreground`.
- AIGC 可见锚点: two people must face away from camera; hands connect near center; window grid must divide the skyline; faces should stay dark.

### Reuse

- 用这个手法的原因: it fuses private emotion and public disaster in one frame.
- 如何用: put the characters in silhouette with minimal facial detail, then let the windowed world carry scale and consequence.
- 适用场景: ending beat, worldline shift aftermath, confession after catastrophe, quiet pause after a major decision.
- 风险与反例: if the figures turn around or faces are lit, the shot becomes a normal dialogue reaction and loses aftermath scale.

### Self-Audit Correction

- Good: reading the hand contact as the emotional hinge is essential.
- Missing risk: do not call it only "romantic skyline"; the city and window grid are active story weight.
- Correction: always describe the damaged/unstable outside world and dark interior contrast.

### Deposited Rule

For "private bond after public rupture", keep the people as dark connected silhouettes and let a huge backlit windowed world explain the scale of what happened.

## Case 14 - Frontal Domestic Symmetry / Vertical Family Hierarchy Tableau

- Date added: 2026-06-25
- Source certainty: user-fed screenshot; visible composition facts prioritized
- User-provided material: current Image #3

### Narrative Layer

- 情绪基调: storybook domestic order, childhood boredom, precise comedy, contained family life.
- 人物关系: older girl occupies the raised window-seat level, absorbed in reading; younger boys lie below on the floor, separated by height and maturity.
- 剧情节点: domestic introduction or character-establishing room tableau.
- 叙事功能: show family hierarchy and personality through vertical placement: the girl has an upper private world, the boys occupy the lower shared floor world.

### Visual Layer

- 景别: frontal medium-wide / wide room tableau.
- 机位: locked-off eye-level camera square to the room's central window.
- 构图法则: near-perfect frontal symmetry, central window axis, vertical split, horizontal row blocking, controlled prop balance.
- 光影: warm practical lamps on both sides, soft daylight through center curtains, low-contrast cozy interior light.
- 色彩: warm beige/yellow walls, orange-red clothing, patterned dark curtains, cream window, red rug accents.
- 画面层次: upper layer = girl on window seat and shelves; lower layer = three boys on rug and floor objects; side layer = chair and lamps balancing asymmetry.
- 镜头 / 焦段 / 景深: normal lens or mild wide, deep focus, flat theatrical frontality.
- 运动 / 剪辑 / 声音: minimal motion; page turns, floor shifting, toy or book foley, soft room tone.

### Language Layer

- 提示词参考: `locked frontal wide shot of a warm attic bedroom, central window with curtains, older girl sitting on a raised window seat reading, three younger boys lying on the patterned rug below in a horizontal row, symmetrical lamps and shelves, storybook domestic order, warm soft practical light, precise tableau composition`
- 关键词提取: `frontal symmetry`, `raised window seat`, `children in lower row`, `vertical hierarchy`, `warm domestic tableau`, `controlled props`.
- AIGC 可见锚点: camera must be square to the room; the girl is above the boys; boys form a lower horizontal row; lamps and shelves create side balance.

### Reuse

- 用这个手法的原因: it turns family relation into readable geometry.
- 如何用: divide the room into vertical social tiers and keep the camera frontal so the hierarchy cannot be missed.
- 适用场景: character introduction, quirky family room, childhood memory, orderly but emotionally separated household.
- 风险与反例: if the camera becomes diagonal or handheld, the storybook tableau breaks; if everyone is placed at the same height, the hierarchy disappears.

### Self-Audit Correction

- Good: symmetry and color are obvious, but the key is vertical relationship, not just "pretty centered room".
- Missing risk: do not ignore props; shelves, lamps, books, and chair are balance weights that keep the frame authored.
- Correction: prompt must lock upper/lower human layers, not merely say "children in a cozy room".

### Deposited Rule

For stylized family tableaux, frontality gives order, but vertical placement gives meaning: upper level can signal privacy, maturity, fantasy, or distance; lower level can signal childhood, dependence, or group identity.

## Case 15 - Apocalyptic Smoke-Column Silhouette / Witnesses Against Disaster Scale

- Date added: 2026-06-25
- Source certainty: user-fed screenshot; visible composition facts prioritized
- User-provided material: current Image #4

### Narrative Layer

- 情绪基调: dread, awe, aftermath, historical or planetary catastrophe.
- 人物关系: two figures stand as witnesses, not controllers; their bodies are subordinate to smoke, fire, and sky objects.
- 剧情节点: disaster reveal, alien/war aftermath, or moment of realizing the event is bigger than the characters.
- 叙事功能: reduce human agency and let environmental scale deliver the story shock.

### Visual Layer

- 景别: extreme wide / panoramic long shot.
- 机位: low horizon-level camera across a dark ridge, slightly below or level with the silhouetted figures.
- 构图法则: silhouette, scale contrast, negative sky, horizontal ridge line, vertical smoke-column rhythm, tiny warm fire anchors.
- 光影: dusk or low exterior backlight; foreground ridge and figures remain nearly black; distant fires glow along the horizon.
- 色彩: blue-gray smoke and sky, black foreground silhouettes, small orange fire points.
- 画面层次: foreground = black ridge; midground = two silhouetted witnesses; background = fire line, vertical smoke columns, mountains/sky, distant craft-like shapes.
- 镜头 / 焦段 / 景深: wide panoramic framing, deep focus, no facial detail.
- 运动 / 剪辑 / 声音: slow hold or very slow push; wind, low rumble, distant explosions, smoke roar, ash movement.

### Language Layer

- 提示词参考: `extreme wide dusk landscape, two tiny silhouetted figures standing on a dark ridge in the foreground, multiple towering black smoke columns rising from distant fires across the horizon, cold blue-gray sky, small orange fire points, huge disaster scale, no facial detail, deep focus, quiet witness composition`
- 关键词提取: `tiny silhouettes`, `dark ridge`, `vertical smoke columns`, `distant fires`, `negative sky`, `witnesses not heroes`.
- AIGC 可见锚点: figures must stay small and black; smoke columns dominate the frame; fire points sit low along the horizon; sky/land ratio must feel vast.

### Reuse

- 用这个手法的原因: it makes disaster scale legible without explanatory dialogue.
- 如何用: keep the characters small, place them on a dark simple foreground strip, and give the background vertical smoke/fires that outweigh them.
- 适用场景: worldline catastrophe vision, city after temporal change, alien arrival aftermath, war memory, prophetic future.
- 风险与反例: if characters become close-up reaction subjects, catastrophe becomes backdrop rather than main event.

### Self-Audit Correction

- Good: the horizontal/vertical contrast must be captured: ridge line vs smoke columns.
- Missing risk: do not fill the frame with explosions; the power comes from distance, smoke scale, and silence.
- Correction: specify witness stillness and low distant sound, not only visual destruction.

### Deposited Rule

For catastrophe reveal shots, make humans witnesses on a dark foreground strip and let vertical smoke, tiny fire points, and negative sky carry the emotional mass.

## Round 3 Transfer Rules

1. A mirror shot must answer what the reflection reveals that the physical body hides; otherwise it is decoration.
2. Window-grid silhouettes work when the outside world carries consequence and the interior characters remain unreadable.
3. Frontal domestic symmetry needs hierarchy, not just neatness: use height, rows, props, and color to show relationships.
4. Disaster scale should often be distant and quiet; small witnesses plus vertical smoke can be stronger than large explosions.
5. For AIGC prompts, lock identity and physics in reflective shots: `same person reflected`, `faces hidden`, `figure remains tiny`, `upper/lower layer`.

## Round 1 Transfer Rules

1. Symmetry is not automatically "pretty"; in these cases it means system, ritual, authored order, or monumental pressure.
2. Low-key light works when it controls information: hide eyes, reveal hands, isolate one color anchor.
3. Frame-within-frame is strongest when it carries social or emotional imprisonment, not when it is a random doorway.
4. Scale contrast needs a tiny subject and a dominant environment; if the subject becomes too large, awe collapses.
5. Atmospheric sci-fi depends on visible media: rain, haze, smoke, volume light, reflective ground.
6. Dialogue composition can move emotion into hands, profile gaps, and body distance instead of facial exposition.
7. AIGC transfer should name visible geometry and light behavior, not rely only on film/director names.
