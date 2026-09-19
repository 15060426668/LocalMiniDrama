---
name: scene-asset-decomposition
description: Decompose scene reference images, plans, elevations, sections, cutaways, or asset boards into an evidence-bound spatial master and reusable visual asset kit. Use for 场景拆分, 场景资产拆解, 空间模块化, 建筑/室内/街区/载具/自然地形资产前置, source-ROI mapping, or preparing a scene for live-action spatial previs. Do not use for technical 3D production assets, multi-camera storyboards, or inventing hidden geometry.
---

# Scene Asset Decomposition

Translate scene references into a reusable visual vocabulary without pretending that hidden geometry is known. The output prepares spatial previs and storyboard work; it does not replace either.

## Scope And Evidence

Accept one or more perspective images, top views, plans, orthographic elevations, sections, cutaways, renders, or asset boards. First classify what each reference can actually prove. If references conflict, preserve the conflict and prefer repeated spatial topology over a single decorative detail.

Use three confidence states:

- O (observed): directly visible or confirmed by consistent views.
- I (inferred): supported by perspective, repetition, contact, or construction logic.
- U (unknown): occluded, off-frame, or contradictory.

Do not turn I/U into asserted fact. A single perspective image permits at most one local relationship diagram; it does not authorize a complete plan, four elevations, or an unseen back side.

## Core Contract

Protect subject identity, period/style, material, wear, weather, season, and current state. Every final module, hero object, and material swatch must point to a source ROI or mask. Reject objects whose silhouette, component count, connection topology, or state drifts from the source.

Use one spatial master version for all outputs. Lock origin, axes, relative scale, repeated rhythm, proxy camera, allowed local relationship range, major occupancy, and contact positions. Do not freely generate several “similar” plans.

## Workflow

1. **Classify references.** Record whether each input proves perspective, boundary, adjacency, route, height, opening, assembly, material, or only appearance. Mark source version and contradictions.
2. **Build the evidence ledger.** For each candidate structure or asset record source ROI, identity fingerprint, confidence O/I/U, scale anchor, parent/support/contact relation, visible and hidden faces, output mode, instance group, and coverage priority.
3. **Choose the scene route.** Use only evidenced categories: interior/building, exterior/street, natural terrain, industrial/mechanical, or vehicle/cabin. Do not apply a fixed asset checklist to every scene.
4. **Lock spatial master.** Define X/Y/Z, up, forward, origin, relative scale, camera range, and repeated rhythm. Match major silhouettes, edge lines, occlusion order, and anchors before extracting assets.
5. **Gate 2D space diagrams.** Output a plan only when the reference has sufficient stable axes, scale/contact anchors, and connection evidence. Output at most one necessary elevation or section, and only when orthographic/multi-view/validated blockout evidence exists.
6. **Decompose by visual identity.** Extract SPACE/SITE/VOLUME, SHELL/TERRAIN/FRAME, OPENING/ACCESS, modular kit, fixed assembly, hero/prop/clutter/soft/foliage, material/trim/decal, and light/FX/background only where supported. Do not split technical screws or merge distinct identities.
7. **Prioritize coverage.** P0 is space-defining shell, terrain, frame, opening, and connection. P1 is fixed assembly, hero object, and high-recognition structure. P2/P3 are reusable props, foliage, clutter, decals, and micro-wear. Ensure all P0/P1 and one representative of each repeated family are covered.
8. **Prepare the visual board.** Default to one deterministic horizontal sticker-style board with a small source anchor, permitted spatial diagram, structure/modules, fixed assemblies, hero/prop families, and material/FX swatches. Image generation may create individual assets; deterministic composition must assemble the board.
9. **Handoff.** Pass the locked spatial master and asset identities to live-action-spatial-previs. That skill decides actors, camera, screen direction, and frame inclusion. This skill must not write a multi-camera shot list or invent a dramatic beat.
10. **Self-audit.** Check ROI coverage, topology, contact/support, occlusion, scale, scene type, O/I/U status, source identity, module boundaries, board readability, and whether any unknown area was silently filled.

## Output Contract

Deliver:

1. reference classification and evidence gaps;
2. one spatial master summary with version and axes;
3. an asset ledger with ROI, identity fingerprint, confidence, parent/contact, priority, instance group, and output mode;
4. permitted local plan/elevation/section diagrams;
5. one deterministic visual-board specification;
6. spatial-previs handoff fields and unresolved questions.

Do not output a technical mesh package, hidden construction dimensions, a multi-camera storyboard, or a new scene event.

## Confirmation And Privacy

Before image generation, show a short confirmation card containing scene type, invariants, permitted spatial diagrams, asset groups, inference boundary, and board ratio. Generate only after explicit confirmation. Keep source images and derived crops in the user's authorized local workspace.

Read [references/asset-decomposition-contract.md](references/asset-decomposition-contract.md) for ROI schema, spatial gates, priority rules, and the handoff shape.
