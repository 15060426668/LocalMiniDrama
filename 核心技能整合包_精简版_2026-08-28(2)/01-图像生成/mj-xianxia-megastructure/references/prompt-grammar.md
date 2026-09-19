# Prompt Grammar

Use this reference for complete Midjourney prompts, prompt templates, and critiques.

## Megastructure Prompt Formula

Write the prompt in this order:

1. Medium and finish: cinematic fantasy concept art, film still, realistic lighting, ultra detailed environment.
2. Human scale marker: tiny ancient Chinese figures in hanfu, seen from behind, standing/walking/watching.
3. Threshold or platform: jade terrace, cliff balcony, moon gate, palace corridor, bridge, roof edge, stairway.
4. Dominant megastructure: colossal celestial palace, floating city, carved mountain-wall gate, inverted roof city, cosmic wall, endless colonnade.
5. Scale proof: repeated columns, tiny railings, huge roof shadows, cloud layers crossing through openings, distant secondary temples.
6. Spatial layering: foreground frame, midground figures, background giant structure, far cloud sea or starfield.
7. Light and atmosphere: sunrise, moonlit blue mist, rim light, volumetric clouds, atmospheric perspective.
8. Cultural construction: Tang/Song inspired rooflines, white jade balustrades, carved dragon reliefs, dougong brackets, lacquered beams, bronze lamps.
9. MJ controls: camera, aspect ratio, style, negative controls.

## Compact MJ Skeleton

```text
cinematic xianxia fantasy film still, tiny ancient Chinese figures in flowing hanfu [position/action], [threshold/platform], facing [dominant colossal structure], humans dwarfed by architecture, [scale proofs], [foreground frame], [midground], [background], sea of clouds, atmospheric perspective, [lighting], [materials], monumental scale, ultra detailed environment, realistic lighting --ar 21:9 --style raw --s 200 --no text, watermark, subtitle, logo, modern clothes, close up portrait
```

## Character Placement Patterns

- `edge witness`: figures stand at the lower edge or corner, looking outward.
- `central pilgrim`: figures at the bottom center on a bridge or stair, swallowed by the vanishing point.
- `balcony group`: three to five figures on a side balcony, seen from behind.
- `door silhouette`: one figure framed by a giant door, window, or moon gate.
- `under-roof traveler`: figures beneath a roof so large it becomes a sky.
- `cliff observer`: figures on a small cliff terrace with a tree trunk as near-scale reference.

Keep figures calm: gaze, walk, pause, bow, hold a lantern, carry a scroll, or let robes move in wind. Avoid combat poses unless requested; action usually shrinks the sacred scale.

## Camera Patterns

- Wide establishing shot: best default for scale.
- Low angle from terrace floor: roof, column, or gate becomes oppressive.
- High oblique view: reveals cloud city, circular platforms, and distance.
- Corridor vanishing point: columns repeat into haze.
- Framed vista: interior darkness around a luminous cloud exterior.
- Underbelly view: floating palace foundation overhead, clouds below.
- Long lens compression: distant palace feels impossibly close and huge.

## Scale Language

Use concrete phrases:

```text
the humans are only 3 percent of the frame height
architecture occupies most of the frame
foreground scale reference
vast negative space
colossal roofline crossing the horizon
endless repeated columns fading into mist
clouds passing through palace openings
tiny railings and steps visible against enormous walls
```

## Common Failure Fixes

- If MJ makes portraits: strengthen `tiny figures`, `seen from behind`, `wide establishing shot`, `architecture occupies most of the frame`.
- If MJ makes generic temples: add one impossible structural behavior and one scale chain.
- If MJ loses Chinese identity: add curved Tang/Song rooflines, white jade railings, carved dragon relief walls, dougong brackets, lacquered beams.
- If the scene feels flat: add foreground frame, midground platform, distant giant form, mist occlusion, and a clear vanishing line.
- If it becomes too busy: choose one dominant megastructure and make other forms distant silhouettes.

## Default Negative Tail

Use when the user wants MJ parameters:

```text
--no text, watermark, subtitle, logo, modern clothes, close up portrait, crowded random temples, cyberpunk city
```
