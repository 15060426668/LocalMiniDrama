---
name: video-story-analysis
description: Analyze existing, legally accessible film or video with traceable shot, sound, text, continuity, and production evidence. Use for 逐镜拉片, 逐帧审计, 成片复盘, 视频拆解, 导演/摄影/剪辑/声音/表演分析, reverse storyboarding, cross-film training, or aligning a finished video with scripts, storyboards, prompts, and edit versions. Do not use for inventing a new storyboard or generating a new video.
---

# Video Story Analysis

Convert an existing video and its lawful derivatives into evidence that can be reused by the storyboard skill. Separate what is visible or audible from what is inferred, and never claim more precision than the input supports.

## Route And Depth

Choose four independent dimensions before analysis:

- Evidence: overview (sampled), shot (cut-reviewed), or forensic (native-frame audit of a short interval).
- Report: L0 plan/gaps, L1 overview, L2 shot report, or L3 forensic appendix.
- Learning: add training only when the user asks for exercises, transfer, or assessment.
- Production: add production only when scripts, storyboards, prompts, edit versions, or node data are supplied for alignment.

Default to overview + L1. Use shot + L2 only for explicit 逐镜/拉片 requests. Use forensic + L3 only for a bounded short interval.

## Evidence Contract

Tag claims and keep the tags in the ledger:

- OBS: directly visible or audible fact.
- SRC: supplied production/source record.
- INF: functional interpretation supported by evidence.
- ALT: a competing interpretation that remains plausible.
- RULE: a transferable rule with stated conditions and failure mode.

Use screen-evidence levels: E0 memory/description, E1 still image, E2 unordered or non-continuous frames, E3 continuous timed audio-video, E4 frame-verified source video. Keep method evidence separate: MTH0 impression, MTH1 public record, MTH2 interview/article, MTH3 project artifacts with cross-check, MTH4 authorized production record review. E4 does not prove MTH4.

Never mark an automatic cut as confirmed until adjacent continuous frames are reviewed. Do not infer exact lens, aperture, camera model, author intent, sound mix, or full-scene conclusions without the corresponding evidence. A full-work claim needs evidence from at least two scenes.

## Workflow

1. Scope and legality. Confirm source, version, duration, requested interval, privacy boundary, and whether the user wants analysis, training, or production alignment. Do not bypass access controls.
2. Media preflight. Record duration, resolution, display ratio, frame rate/timebase, VFR suspicion, video/audio/subtitle streams, decode status, and missing evidence. If media cannot be decoded reliably, stop at L0.
3. Candidate evidence. Generate sampled overview frames or cut candidates. Treat automated boundaries as candidate; review before assigning shot IDs. For forensic work, use native PTS frames for the specified short interval.
4. Shot ledger. For each reviewed shot record time range, frame evidence, shot size/angle, camera movement only when supported by continuous frames, composition, screen direction, blocking, visible action chain, performance, light/material, sound, text, transition, and tail state.
5. Scene and sequence model. Group reviewed shots into scenes and sequences. Track entrances/exits, object ownership, eyelines, axis, spatial state, action phase, light/color, sound bridges, and unresolved continuity.
6. Semantic analysis. Analyze vertically within scenes first: objective, resistance, strategy change, value change, staging, coverage, edit, sound, and audience information. Then synthesize cross-scene rules. Attach every INF/RULE to shot or scene IDs.
7. Training or production alignment. Training adds before/after exercises, scoring anchors, and one original transfer. Production alignment maps supplied source IDs and versions; it never turns a storyboard or prompt into proof of what the finished video contains.
8. Quality gate and archive. Report unreviewed cuts, missing intervals, ASR uncertainty, low-confidence claims, and method gaps. Preserve a versioned ledger; do not silently overwrite prior conclusions.

## Input Degradation

| Available evidence | Allowed conclusion |
|---|---|
| Only title, synopsis, memory, or script | Story/intent analysis and a missing-evidence plan; no shot or sound claims. |
| Still or unordered frames | Composition, visible relation, and state differences; no complete motion, cut boundary, or sound. |
| Timed continuous video | Reviewed shot, movement, blocking, performance, edit, and listened sound claims within scope. |
| Subtitle/ASR without listened audio | Text timing and wording only; sound design remains unknown. |
| Storyboard/prompt without finished video | Intended plan analysis; do not call it a result. |
| Long video | Partition by scene or roughly 10-20 minute volumes; keep resumable state and merge only after volume review. |

## Output Contract

Deliver only the requested depth:

1. scope, evidence level, method, and exclusions;
2. main findings with OBS/SRC/INF/ALT/RULE support;
3. shot/scene/sound/text evidence tables or references;
4. continuity and uncertainty ledger;
5. training exercises or production alignment only when requested;
6. migration rules for the storyboard skill, never a new dramatic beat.

Do not paste complete subtitles, long prompts, or raw frame dumps into the report. Use stable IDs and timestamps.


## Downstream Adapters

Treat reverse storyboarding as a production profile of this skill, not a second evidence system. When the user requests a workbook, hand the reviewed ledger to the spreadsheet skill and preserve shot IDs, timestamps, review states, and image anchors. When the user requests Seedance or another video prompt, hand only approved evidence-backed shot facts to dream-suspense-sd; do not compile unresolved inference into a prompt.
## Stop Conditions

Stop or downgrade when decode/timebase fails, cuts are unreviewed, a “逐帧” claim lacks native frames, sound is inferred without listening, ASR is unverified, the requested scope exceeds the analyzed footage, or strict references/coverage fail. State the smallest next evidence action instead of filling gaps with plausible language.

Read [references/evidence-contract.md](references/evidence-contract.md) for ledger fields, review states, and training/production mapping rules.
