---
name: live-action-spatial-previs
description: Build and audit top-down spatial previsualization for live-action scenes before a storyboard or shot list. Use when actor blocking, camera placement, screen direction, eyelines, frame inclusion, axis continuity, over-the-shoulder geometry, or a visual sandtable handoff must be made explicit and checked.
---

# Live-Action Spatial Previs

Use this skill as the spatial contract between script, director, cinematographer and storyboard. It solves where people and props are, where the camera is, what face or body surface the camera sees, what lands on screen left/right/deep, and who is inside or outside the frame. It does not rewrite story facts, dialogue, character identity or emotional beats.

## When To Route Here

Route here when a scene has any of the following:

- two or more actors whose relative positions must survive coverage;
- a walk, entrance, exit, handoff, prop interaction or blocking change;
- a scene where a person must be on- or off-screen by geometry rather than prose;
- an over-the-shoulder, POV, reverse angle, multi-camera or axis decision;
- a continuity failure, generated-video spatial error, or a request for a director-desk/sandtable handoff.

For a simple single-subject shot with no spatial dependency, return to the main storyboard skill.

## Contract

Protect these fields as immutable inputs: scene identity, time, actor identity, dialogue ownership, action order, action result, explicit entrances/exits, story purpose and emotional beat. If a requested shot cannot exist under the protected facts, return `storyboard_conflict` with the smallest geometric explanation; do not silently change the story.

Maintain one `spatial_version` per physical setup. Use `continuous` only when the same space and time continue across shots. Use `scene_reset`, `time_jump`, `flashback`, `dream` or `parallel` when the story explicitly changes the spatial state.

## Workflow

1. **Create the baseline.** Set a top-down world coordinate system: north is up, east is right in the map, and every actor, fixed prop and camera has a position and facing. Record exits, barriers and the A/B axis.
2. **Lock movement.** Record every position change as `during_shot` or `between_shots`, with a start state, end state and readable path. An undeclared coordinate change is a continuity error.
3. **Solve each camera.** For every shot, answer all five questions before writing the shot: where each relevant actor is and faces; where and how high the camera is aimed; which side of the subject is visible; what is screen-left, screen-right and deep; who is in or out of frame.
4. **Check geometry.** Derive screen left/right from camera heading, not intuition. Check field of view, line of sight, occlusion, actor-facing angle, eyeline, axis side and foreground shoulders. Do not label an actor `partial` merely because the shot is a close-up; `partial` means an incidental edge fragment.
5. **Render the sandtable.** Run `scripts/sandtable.py` on the handoff JSON. Treat the generated HTML as a review aid, not as new story evidence.
6. **Report risks.** Flag near-axis cuts, impossible face visibility, accidental third-person inclusion, repeated coverage that may collapse into one shot, short shots with no visual/audio refresh, and paths that pass through collidable props. Suggestions are advisory; the user decides whether to revise.
7. **Hand off.** After confirmation, pass the locked spatial data to the storyboard skill. Every formal shot and later SD prompt must preserve the confirmed camera heading, screen direction, visible actors, asset view and tail state.

## Minimal Handoff Shape

```json
{
  "title": "scene name",
  "scene": {"bounds": {"w": 24, "d": 36}, "landmarks": [], "zones": []},
  "baseline": {
    "scene_id": "SC01", "spatial_version": "v1", "continuity_mode": "continuous",
    "axis": {"a": "A", "b": "B", "locked_side": -1},
    "actors": [{"id": "A", "name": "Actor A", "x": 0, "y": 0, "facing": "N", "present": true}],
    "props": []
  },
  "shots": [{
    "id": "S01", "time": "00:00-00:03",
    "camera": {"x": 0, "y": -6, "facing": "N", "fov": 40, "height": "eye-level", "label": "medium two-shot"},
    "chars": [{"name": "Actor A", "x": 0, "y": 0, "facing": "N", "main": true}],
    "expected_actor_presence": {"A": "visible"},
    "note": "shot purpose and landing state"
  }],
  "risks": []
}
```

The renderer accepts the `scene` and `shots` fields. Keep `baseline`, protected facts and movement events alongside the render input so the handoff remains auditable.

## Geometry Rules

- Camera heading determines screen orientation. Recompute left/right after every camera move.
- Put a camera in the subject's front hemisphere when expression, eyeline or lip movement matters. A back-facing camera can only ask the back to carry the shot.
- To keep an actor out of frame, place the camera where the actor is geometrically outside the field of view or use a justified long-lens crop; prose such as “not seen” is not a solution.
- If a third actor lies between camera and target, that actor is necessarily present unless the camera moves or the field of view changes.
- Preserve the axis until an intentional crossing is motivated by a visible move, neutral shot or story beat. Record the crossing explicitly.
- Distinguish camera-facing asset selection from subject identity: a multi-view environment is chosen by camera heading, not by which actor is being filmed.

## Output

Deliver, in order:

1. a compact baseline table;
2. one row per shot with camera position/heading/height, visible surface, derived screen left/right/deep, in-frame/out-of-frame actors, and movement timing;
3. the HTML sandtable path and a risk/advisory list;
4. only after confirmation, the handoff payload for the formal storyboard.

Do not output a prompt, a finished shot list, or a new dramatic beat during the spatial pass.

## Resources

- Read [references/sandtable-contract.md](references/sandtable-contract.md) for coordinate conventions, camera geometry, risk checks and JSON fields.
- Run `python scripts/sandtable.py input.json -o output.html` to render the reviewable HTML sandtable. The script uses only the Python standard library.
