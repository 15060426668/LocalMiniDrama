# Line, Cel, and Texture Systems

Texture begins with drawing behavior, then shading, background paint, and capture finish.

## Line grammar

Baseline line:

`fine charcoal or dark-brown contour, slight hand-drawn width variation, soft corners, sparse interior marks, clean silhouette readability`

Ordinary scenes:

- keep faces mostly open;
- use a few hair strands inside large hair masses;
- draw clothing folds at shoulders, elbows, waist, and bag contact points;
- use short cheek marks for embarrassment or strain.

Psychological scenes:

- add short irregular hatching under the eyes and along the nose, cheek, neck, hand, or hair shadow;
- let some hair strands overlap the eyes;
- increase line density locally while the rest of the frame remains simple;
- keep pupils, mouth, and face silhouette readable.

## Cel-shading grammar

### `CEL-ONE-STEP`

One restrained shadow family, clean shape edges, open pale skin, minimal ambient contamination.

### `CEL-SOFT-CONTAMINATION`

One main cel shadow plus soft reflected color from sky, wall, corridor, or foliage.

### `CEL-PSYCHO-LOCAL`

Baseline cel shading with denser localized shadow around eyes, hair, neck, and frame edge; sparse pencil hatching adds pressure.

Keep highlights small and graphic. Use glossy eye rendering only when a wet emotional eye is the main evidence.

## Background grammar

- Foliage: clustered painted leaf shapes with darker interior masses and brighter edge patches.
- Sky: broad cyan field with soft white clouds and slight bloom.
- Road: simple cool-grey plane with cracks, seams, curb, or slope lines establishing geography.
- School: faded teal frames, salmon or cream walls, wood or linoleum floor, repeated doors and ceiling lights.
- Classroom: desks, books, bags, windows, and wall papers provide social density without equal detail everywhere.

## Finish lanes

### `FINISH-PAPER-LIGHT`

Faint fine paper grain, stable cel-color regions, very light animation-photography noise.

### `FINISH-SOFT-BLOOM`

Pale bloom around sky, bright wall, or window edges; clean subject contours remain readable.

### `FINISH-PSYCHO-GRAIN`

Slightly stronger grain and uneven shadow texture in emotional close-ups, concentrated in dark regions.

### `FINISH-CLEAN-KEYART`

Clean promotional still with painterly background depth and crisp character silhouettes; minimal capture artifacts.

## Synthetic-output repair

When the output looks glossy or generic:

1. simplify face rendering;
2. merge hair into larger silhouette masses;
3. reduce smooth 3D gradients to one or two cel-shadow shapes;
4. add slight contour variation;
5. move texture into the background and localized hatching;
6. restore ordinary clothing folds and object contact;
7. keep skin matte and pale.

## Texture gate

Reject and revise when:

- skin looks plastic or airbrushed;
- hair contains thousands of photoreal strands;
- gradients replace cel-shadow shapes;
- every contour has identical vector width;
- heavy grain obscures clean color blocks;
- hatching covers every surface instead of carrying psychological pressure;
- background and character have identical detail density.
