# Static Image Prompt Assembly

## Assembly order

Build the model prompt in this order:

```text
asset type and use case
-> reference-image roles
-> one frozen story moment
-> exact subject count and identity locks
-> environment and spatial map
-> foreground/midground/background composition
-> pose, gaze, expression, hands, and prop ownership
-> character shape language
-> linework and cel shading
-> motivated light and color script
-> background paint and capture texture
-> invariants and exclusions
```

Lead with the requested image, not with a style label.

## Copy-ready schema

```text
Use case: <static illustration / key frame / character study / concept image / edit>
Input images: <Image 1 role; Image 2 role; ...>
Primary request: <single frozen moment>
Subjects: <count, identity, clothing, pose, gaze, expression>
Environment: <place, time, fixed geometry, objects>
Composition: <aspect ratio, framing, foreground, midground, background, visual owner>
Drawing language: <proportions, face, hair masses, line behavior>
Shading and light: <cel-shadow system, source, direction, emotional localization>
Color script: <skin, hair, environment, source, shadow, accent>
Texture: <background paint, paper grain, bloom, localized hatching>
Constraints: <identity, count, prop ownership, readable anatomy, exact text if any>
Exclusions: <unwanted media, rendering, text, logo, watermark>
```

Use the user's language unless a target tool requires another language.

## Name removal

Before generation:

1. list every title, franchise, artist, director, studio, and named character in the user request and reference notes;
2. extract the visual evidence each name represents;
3. delete the names from the model prompt;
4. run the validator with every name passed as `--forbidden-term`.

Replace name dependence with visible language such as:

`compact child proportions, large dark irises, fine slightly uneven charcoal outlines, large flat hair silhouettes, restrained cel shading, bright ordinary daylight, localized pencil hatching under tired eyes, muted green-brown psychological shadows, faint paper grain`

## Static-versus-video gate

Rewrite video language into one frozen state:

- `walks toward camera, then turns` becomes `caught mid-step, torso forward, head turned back, rear heel raised`.
- `the group surrounds her` becomes `the group already forms a U-shaped enclosure around her`.
- `the bag is grabbed` becomes `one hand holds the bag's top loop while the victim's fingers still press the slipping strap`.
- `camera pushes in` becomes `tight close-up with compressed background and focus on the eyes`.

One image may imply motion through weight, cloth delay, gaze, and object state. It does not contain a timeline.

## Controlled variants

Change one layer at a time:

- composition: wide group frame vs close reaction;
- palette: ordinary summer vs muted school interior;
- finish: clean cel vs localized psychological hatching;
- perspective: normal relation vs wide social enclosure;
- emotional intensity: watchful vs suppressed vs exhausted.

Use one separate image-generation call per variant.

## Repair patterns

### Too generic

Add exact group count, identity roles, one prop owner, one social geometry, and one frozen action consequence.

### Too cute

Keep rounded proportions but reduce decorative highlights, deepen lower eyelids locally, compress posture, and let ordinary objects carry pressure.

### Too dark

Restore pale skin mids and ordinary daylight; localize darkening to hair shadow, wall shade, foreground occlusion, and eye hatching.

### Too glossy or 3D

Restore flat hair masses, matte skin, fine irregular outlines, one-step cel shadows, sparse highlights, and faint paper grain.

### Identity drift

Repeat the reference-image role, face shape, hair silhouette, clothing, body proportion, and distinctive prop. Reduce simultaneous style changes.

### Crowd drift

State exact count, foreground/midground/background roles, clothing colors, and one distinct action per person.
