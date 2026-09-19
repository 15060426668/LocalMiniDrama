# Evidence Contract

Use this contract to keep an existing-video analysis auditable and useful to later storyboard work.

## Minimum Ledger

Each shot row should have:

- shot_id and scene_id;
- start/end time plus frame or PTS references when available;
- review_state: candidate, reviewed, or unresolved;
- evidence tags: OBS, SRC, INF, ALT, or RULE;
- visual fields: shot size, camera side/height as observable, composition, screen direction, blocking, action phase, performance, light/material, and tail state;
- audio/text fields: dialogue or subtitle event, sound source, music/silence, and alignment confidence;
- continuity fields: entrance/exit, eyeline, axis, object ownership, location, light/color, and unresolved risk;
- source links to frames, audio segments, transcripts, scripts, or versions.

## Review State

candidate means machine-generated or unreviewed. reviewed means adjacent continuous frames or the relevant audio were inspected. unresolved means the evidence is insufficient or conflicting. Never use reviewed as a synonym for “the model thinks this is correct.”

## Claim Ladder

An observation states what the frame or waveform supports. An inference explains function and names its evidence. A rule generalizes only after at least two scene examples and must include:

- condition;
- visible/audible mechanism;
- audience effect;
- failure mode;
- transfer boundary.

If a claim depends on production intention, label its method evidence separately. A supplied storyboard is SRC for intended design, not OBS for the finished cut.

## Reverse Storyboard Handoff

When the analysis is used by the director skill, hand off only stable, evidence-backed fields:

- scene and shot IDs with time ranges;
- spatial state, screen direction, visible actors, entrances/exits, and object ownership;
- camera and edit facts at the level the footage supports;
- performance beats as visible actions and timing;
- sound/text events with alignment confidence;
- unresolved items and the smallest verification action.

Do not hand off invented lens numbers, hidden motivations, unverified author intent, or new story beats.

## Training Handoff

A useful exercise contains a source interval, a single skill target, an observable success criterion, and an original transfer task. Score the learner against evidence, not taste words such as “高级” or “电影感”.
