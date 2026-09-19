---
name: dialogue-doctor
description: "Use when the user wants Step 4 dialogue diagnosis or line-level dialogue rewriting. This skill audits dialogue through a seven-dimension framework, gives reasoned rewrites, and stays strictly inside dialogue scope without changing story structure."
---

# Dialogue Doctor

This skill is Step 4 of the six-step playwriting chain.

## Use This Skill For

- Full dialogue diagnosis
- Speaker voiceprint analysis
- Subtext marking
- Rhythm-only diagnosis
- Gold-line generation for a chosen role and scene
- Focused dialogue rewriting with reasons

## Core Behavior

1. Start with self-check.
2. Auto-detect script-like input when possible.
3. Default to full diagnosis unless the user asks for a narrower mode.
4. Run the dialogue through the seven-dimension framework.
5. Every rewrite must include the reason for the change.

## Seven Dimensions

- voiceprint
- subtext
- conflict drive
- genre voice
- information efficiency
- rhythm and musicality
- memorable-line potential

## Output Contract

- No unsupported rewrite suggestions.
- If a line changes, explain why it changed and which dimensions improved.
- Be blunt when the dialogue is flat or all characters sound the same.

## Boundaries

- Do not rewrite the whole script.
- Do not change story structure.
- Push structure problems back to Step 3 or Step 2.

## Storyboard Handoff

For approved lines, emit a dialogue lock containing: exact text, speaker, language, speaker objective, surface meaning/subtext, new information, speech act, voiceprint cue, delivery mode, estimated clean speaking duration, minimum pause and lip-sync window, listener delta, intended interruption or silence, pre-emphasis/tail action, and any indispensable physical action. Mark unapproved alternatives separately. When the approved words cannot fit the available window, report the overload and return the line for user-approved revision; Step 5 may schedule timing and reactions but may not silently rewrite locked text.

## References

- Read `references/outline.md` for the phase flow, output templates, special modes, and edge handling.
- When locking dialogue for a timed video segment, also read `../director-storyboard-integrated/references/dialogue-timing-scheduler.md` for speaking-rate, pause, overlap and reaction-window checks.
- Source document: `F:\剧本创作四步骤\台词 Skill 第四步台词定稿.docx`
