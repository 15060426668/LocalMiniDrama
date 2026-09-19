# Phase Workflow Contract

Use this contract for every new black-subtractive mixed-media scene or series. Keep one user-facing phase active at a time.

## Persistent state machine

```text
idea brief
-> director improvement
-> scheme pool
-> user selection or approved combination
-> static asset prompt pack when requested
-> detailed storyboard only on explicit phase entry
-> user approval of details
-> SD/Seedance compilation only on explicit phase entry
-> generated-result repair
```

The user's explanation of the pipeline establishes the workflow; it does not authorize emitting every later phase in the same turn.

## Phase rules

### 1. Idea brief and director improvement

Lock the scene function, protagonist, era/location, weather, physical trigger, audience information order, emotional landing, platform, and inherited project style. Improve incomplete staging and causality without replacing the user's central image.

### 2. Scheme pool

Return two to four genuinely distinct schemes. Each scheme states:

- transition-before image and information owner;
- subject or prop performance that prepares the change;
- visible transition process from source to residue;
- transition-after landing image and residual motion;
- live-action plate evidence and 2D identity protection;
- sound trigger, strength, AIGC risk, and failure boundary.

Do not output a formal shot table or SD payload. Keep candidates separate until the user selects one or explicitly combines mechanisms.

### 3. Selection lock

Repeat the approved scheme checksum and resolve conflicts into one director grammar. Do not reopen rejected candidates unless the user asks.

### 4. Static asset prompt pack

This optional phase is allowed after selection when the user requests MJ stills, scene prompts, character prompts, props, look development, or keyframes. It does not advance to detailed motion design or SD video compilation.

Generate only the assets needed for stable downstream work:

1. `real_plate`: a photoreal environment without the 2D protagonist or transition effect;
2. `character_identity`: the colored rough 2D woman on a simple organized field, including the key prop she owns or operates;
3. `hero_prop`: optional and normally omitted; create a separate prop reference only when the user explicitly requests one or when mechanical shape continuity cannot be controlled otherwise;
4. `pre_transition_keyframe`: one frozen source state with visible preparation;
5. `post_transition_keyframe`: one frozen landing state with cross-medium contact proof;
6. `transition_peak_keyframe`: only after its geometry is approved or when the user explicitly requests it.

Use parameter-free MJ description prose. Keep each prompt to one frozen moment with no timeline, model parameters, artist/source names, or SD architecture. Preserve identity and culture locks across the pack. Model-facing character descriptions must spell out observable proportions, face and eye grammar, hair mass, contour pressure, broken and retraced line behavior, fill boundaries, cel-shadow behavior, local hatching, paper texture, pose, gaze, hand pressure, support and prop ownership; a source-style label or a short generic phrase never substitutes for those facts.

### 5. Detailed storyboard

Advance only when the user explicitly says `进入分镜细则` or an equally clear command. Design exact 4-15 second segment timing, formal shot rows, full subject action chains, live-plate and 2D motion ledgers, sound-picture triggers, transition geometry, landing tail, continuity, and AIGC fallback coverage. Stop before SD.

### 6. Detail approval

Treat the latest explicitly approved detailed storyboard as the only execution source. A request to revise one layer does not reopen unrelated approved facts.

### 7. SD/Seedance compilation

Advance only when the user explicitly says `进入SD输出`, requests SD/Seedance execution text, or clearly authorizes compilation of the approved storyboard. Hand off to `dream-suspense-sd`; do not invent a parallel prompt schema. Source accounts, artist names, film references, and rejected schemes remain upstream only.

### 8. Result repair

Find the first failed layer: source storyboard, identity, performance, transition geometry, live-plate integration, sound sync, continuity, or model execution. Repair that layer while preserving approved upstream locks.

## Transformation delta gate

When the user asks for a transition between eras, worlds, realities, or before/after states, write the source and destination as separate drawable facts before approving the scheme. The destination must visibly change at least three non-cosmetic axes:

- era or world rule;
- location or architectural system;
- wardrobe, role, or body-task state;
- prop function or ownership state;
- background population and social routine;
- transport, signage, lighting technology, or material culture;
- audience information or story permission.

At least three continuity anchors must also survive, such as screen position, gaze, hand route, support, dominant axis, prop silhouette, weather vector, or sound phrase. The acceptance formula is `clear destination change + clear continuity bridge`. Revealing a wider view of the same unchanged scene is a reveal, not a qualifying time/world transformation, unless the user explicitly asks for that treatment.

## Persistent project defaults

- The protagonist is a colored rough hand-drawn 2D woman unless the user explicitly changes her.
- Do not invent a male protagonist, companion, or romance beat.
- Environments and NPCs remain photoreal live action with ordinary independent behavior.
- A transition preserves preparation, at least three invariants, visible consequence, and an atmospheric landing tail.
- A requested era/world transition must pass the transformation delta gate; a same-scene widening or unmasking does not count by itself.
- Character prompts include the key held or operated prop in the same drawable composition by default; do not split out a prop sheet unless explicitly requested or technically necessary.
- When the user omits black/mask treatment, remove the entire black-treatment block rather than leaving indirect synonyms.

