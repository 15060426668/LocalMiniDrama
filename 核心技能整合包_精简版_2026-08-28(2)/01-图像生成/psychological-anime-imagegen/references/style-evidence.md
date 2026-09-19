# Style Evidence Atlas

Use this file to translate the bundled reference images into visible prompt language. Asset IDs are internal evidence labels. Model-facing prompts contain only the extracted traits.

## Evidence map

| Asset | Primary evidence | Secondary evidence | Weight |
|---|---|---|---:|
| `style-evidence-01.png` | simplified side-profile faces, large dark hair masses, thin contour line, flat cel color, cyan sky | low-angle intimacy, two-person gaze tension | high |
| `style-evidence-02.png` | soft daylight, restrained shadow shapes, slightly rough hair strands, large tired eyes | asymmetric emotional posture, gentle bloom | high |
| `style-evidence-03.png` | muted school corridor, teal/pink architectural separation, quiet side-profile fatigue | simple rounded mascot against human figure | high |
| `style-evidence-04.png` | compact child proportions, ordinary group energy, simple expressive faces, saturated natural greens | wide-angle social geometry, school bags and casual clothing | high |
| `style-evidence-05.png` | tilted playful composition, forest green depth, clean rounded mascot silhouette | sparkle accents and comedic-surreal contrast | medium |
| `style-evidence-06.png` | central-victim crowd geometry, strong near-far distortion, many reaction faces | magenta grade and graphic exaggeration | low; use geometry only |
| `style-evidence-07.png` | ensemble separation, lush outdoor palette, black/white/pink shape contrast | promotional grouping and pipe-scale composition | medium |

## Stable fingerprint

### Character shape

- Child and young-teen bodies use compact proportions, narrow shoulders, slim limbs, slightly oversized heads, and ordinary clothing.
- Faces use soft jawlines, small noses, short mouths, large dark irises, and simple ears.
- Hair reads as a few large silhouette masses with sparse interior strands. Black hair is often treated as a near-solid shape.
- Expressions stay legible with small changes to eyelid angle, mouth corner, cheek marks, shoulder height, and head tilt.

### Linework

- Use fine dark-brown or charcoal outlines rather than pure vector-black everywhere.
- Preserve slight hand-drawn width changes and small contour irregularities.
- Keep interior detail sparse in ordinary scenes.
- Add short pencil-like hatching beneath eyes, along cheeks, necks, or hair shadows only when psychological pressure increases.

### Shading

- Use restrained cel shading with one main shadow family and occasional soft edge contamination from the environment.
- Ordinary daylight faces remain mostly open and pale.
- Emotional close-ups deepen eye sockets, lower eyelids, neck shadow, and hair-over-face shadow while keeping features readable.
- Strong backlight creates a soft pale rim and slight bloom, not photorealistic volumetric rendering.

### Color

- Ordinary outdoors: cyan or turquoise sky, dense leaf greens, cool grey roads, pale skin, simple clothing accents.
- Schools and homes: muted salmon, faded teal, dull cream, medium wood brown, cool grey-green shadow.
- Psychological pressure: brown-grey, olive-green, grey-violet, muted blue, and localized dark maroon contamination.
- Rounded mascot forms: one clean high-chroma pink or coral shape with minimal facial marks, separated from the human palette.

### Composition

- Use wide lenses or close camera distance for group scenes so foreground bodies feel larger and social distance becomes physical.
- Keep a vulnerable child lower, smaller, off-center, or enclosed by shoulders, desks, doors, pipes, or corridor lines.
- Use profile two-shots for direct relationship tension.
- Use quiet close-ups with compressed or simplified backgrounds for private emotional collapse.
- Use occasional tilt or mild edge distortion for subjective discomfort; keep ordinary architecture readable.

### Texture

- Preserve clean cel-color regions with faint paper grain or animation-photography noise.
- Let background painting carry more texture than faces.
- Use soft bloom around bright windows or sky edges.
- Keep chromatic aberration, heavy grain, painterly brushwork, glossy CGI, and plastic skin outside the baseline.

## Lane translation

### Ordinary daylight

`compact child proportions, soft rounded faces, large dark irises, fine slightly uneven charcoal linework, sparse interior lines, restrained one-step cel shading, cyan daylight, dense natural greens, ordinary school clothing, faint paper grain`

### Relational pressure

`wide social framing, foreground shoulders and school bags forming an enclosure, uneven group spacing, one smaller isolated child, playful expressions carrying social control, ordinary daylight continuing around the conflict`

### Psychological close-up

`tight face framing, hair partly covering the eyes, dark lower eyelids, sparse pencil hatching under the eyes and along the cheek, muted brown-green shadow, pale open skin midtones, compressed background, soft animation-photography grain`

### Surreal contrast

`simple rounded high-chroma mascot silhouette, two dot eyes and a tiny mouth, clean flat fill, minimal line detail, materially richer human environment, clear scale contrast`

## Outlier control

- Treat `style-evidence-06.png` as a composition experiment rather than a color authority because its magenta grade, fisheye distortion, watermark, and graphic sharpening differ from the main cluster.
- Treat promotional or composite images as palette and ensemble evidence, not exact scene-light evidence.
- When one image conflicts with the majority, preserve the majority fingerprint unless the user explicitly selects the outlier.

## Research status

On 2026-07-13, network access from the local execution environment failed at DNS/HTTP resolution. No external production claims were incorporated. The current atlas is derived from the seven user-supplied images only. Future updates may add verified source URLs and production facts, but model-facing prompts still remain name-free.
