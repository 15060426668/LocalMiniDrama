---
name: director-storyboard-training-maintainer
description: Maintain and improve the director storyboard system from user-fed films, clips, screenshots, transcripts, shot tables, generated training notes, failed outputs, or targeted viewing. Use for 训练, 投喂, 素材吸收, 阅片补强, 来源审计, 去污染, 证据分级, 技能迭代, 精简合并, 删除重复技能, 饱和判断, regression maintenance, or deciding what storyboard material still needs study. Do not use for ordinary storyboard design or SD/Seedance prompt output.
---

# Director Storyboard Training Maintainer

Keep training governance outside the runtime storyboard skill. Improve the runtime libraries without making ordinary scene design load training charters, archive maps, saturation rules, or regression history.

## Required Reads

- Read `references/high-intensity-training-loop.md` for the general intake, deduplication, saturation, deposit, and iteration loop.
- Read `references/canzhu-targeted-training-charter.md` only for 《残烛》 material collection, gap analysis, or R-series training.
- Read `references/dual-skill-regression-suite.md` after structural changes to the storyboard/SD pair.
- Read `references/skill-loop-system-map.md` only for architecture audits, route ownership, or consolidation decisions.
- Use the runtime evidence policy at `../director-storyboard-integrated/references/counterpart-source-register.md` for A/B/C grading.

## Maintenance Workflow

1. Inventory the supplied material before interpreting it: actual files, groups, rows, fields, claimed durations, repeated parameters, missing layers, and internal contradictions.
2. Grade evidence before depositing it:
   - `A`: watched footage, contiguous screenshots, reliable production material, or verified source facts.
   - `B`: stable scene mechanism without verified shot-level facts.
   - `C`: generated tables, secondary summaries, memory, symbolic interpretation, unsupported timings, focal lengths, Kelvin, percentages, Hz/dB, dialogue, or micro-actions.
3. Run the story-world contamination firewall. Remove donor lore, named identities, plot solution, supernatural explanation, iconic objects, franchise design, and generated pseudo-precision.
4. Compare the residue against existing runtime libraries. A new location, film, camera move, or prop is not a new route when an existing mechanism already owns the dramatic job.
5. Deposit only when the material adds at least one of:
   - a reusable rule;
   - a failure boundary;
   - a transferable shot template;
   - a new retrieval trigger or combination grammar;
   - an SD-visible anchor or quality gate.
6. Route the deposit to the narrowest existing runtime library. Create a new runtime file only when no current owner can retrieve the capability without ambiguity.
7. Register the batch and evidence grade in `counterpart-source-register.md`. Repeated coverage belongs in the register, not in runtime prose.
8. Validate changed skills and run regressions in proportion to the blast radius.

## Deposit Contract

Write each accepted mechanism as a compact callable card:

```text
Mechanism name:
Dramatic job:
Trigger / precondition:
State chain:
Composition / camera / blocking:
Object / sound / transition proof:
Replacement variables:
Failure boundary:
Runtime owner:
Evidence grade and source register row:
```

Do not retain film names inside the final anonymous mechanism unless the entry remains a verified counterpart-retrieval card. Do not copy the source's duration or edit rhythm into the runtime template.

## Deduplication Rules

- Merge by dramatic function and state transition, not by location or technique name.
- Keep distinct submodes only when they change authority, information permission, physical proof, or the next action.
- Replace broad film lists with one mechanism card plus optional B-grade recall seeds.
- Record repeated examples as coverage evidence after two consecutive samples add no new rule, boundary, combination, or SD anchor.
- Retire obsolete routes only after their active triggers, unique rules, and regression responsibilities have been reassigned.
- Never delete active specialist skills merely because their domains are adjacent.

## Runtime Boundary

The runtime skill `director-storyboard-integrated` may contain only callable design mechanisms, routing, output contracts, and artifact validators needed during scene work. Keep the following here instead:

- intake and training charters;
- evidence normalization and saturation stopping;
- maintenance architecture maps;
- structural regression procedures and historical pass records;
- consolidation, deprecation, and source-coverage governance.

Ordinary requests such as “设计分镜”, “进入细致分镜”, or “进入SD输出” must not trigger this skill.

## Validation

After edits:

```powershell
python <skill-creator>/scripts/quick_validate.py <changed-skill>
powershell -ExecutionPolicy Bypass -File ../director-storyboard-integrated/scripts/run_static_regression.ps1
python ../director-storyboard-integrated/scripts/run_behavioral_regression.py <artifact-directory>
```

Run the full thirty-four-case behavioral suite only after shared-contract, routing, runtime-library, continuity, SD-compiler, or project-hard-lock changes. For a narrow reference-card edit, validate both skills and run targeted retrieval/static checks.
