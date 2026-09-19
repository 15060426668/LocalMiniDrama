# Asset Decomposition Contract

## Evidence Ledger

Each row must contain:

- asset_id and source reference;
- source_roi or mask;
- identity_fingerprint: silhouette, proportions, component count, connection topology, material/color, wear, and current state;
- confidence O/I/U and inference reason;
- parent, support, contact, occlusion, and main axis;
- output_mode: source crop, segmentation, constrained reconstruction, or omit;
- instance_group and variant/state;
- priority P0-P3 and final-board coverage.

P0/P1 items and one representative of every repeated asset family require full traceability. If an item has no ROI, changes its silhouette or topology, or appears only as an unsupported hidden completion, omit it.

## Spatial Diagram Gate

A single perspective reference may produce no more than one local relationship diagram. A plan, elevation, or section can enter the final board only when stable axes, at least three scale/contact anchors, and the relevant boundary or connection are supported by plans, orthographic views, multiple consistent views, or a validated blockout. Unknown edges stay open or are labeled U.

## Spatial Master

Record:

- blockout_version;
- origin, axes, up, and forward;
- relative scale anchors and repeated rhythm;
- proxy camera and matching range;
- allowed local relationship scope;
- major occupancy, contact points, and occlusion order.

All asset crops, diagrams, and handoff fields must reference this same version.

## Handoff To Spatial Previs

Pass only:

- fixed landmarks and zones;
- spatial master version and coordinate convention;
- actor/prop-free camera-facing environment facts;
- asset view constraints by camera heading;
- known barriers, exits, support surfaces, and occlusion;
- O/I/U gaps requiring user confirmation.

Do not pass actors, emotional beats, dialogue, or shot timing as invented content.
