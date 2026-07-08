# Storyboard Video Keyframe Rules

## Total Image Rule

The storyboard deliverable is one contact-sheet image containing five landscape product keyframes.

The image must be:

- landscape,
- five-panel,
- 16:9 contact sheet,
- video-keyframe ready.

The final response embeds or links the contact sheet produced by the run.

## Panel Schema

```yaml
storyboard_panel:
  panel_number:
  content_task:
  creative_type:
  scene_ref:
  model_ref:
  motion_ref:
  camera_ref:
  brand_film_mode:
  ref_descriptions:
    creative_type:
    scene_ref:
    model_ref:
    motion_ref:
    camera_ref:
  product_truth_lock:
  visual_fragment_logic:
  continuity_from_previous:
  video_generation_note:
```

## Panel Planning Rule

The five panels do not use a universal fixed role template.

Each panel gets its `content_task`, `visual_fragment_logic`, camera, and motion from `picture_fragment_logic` in the `DTC Creative Reference Pack`.

The sequence must:

- keep the product visible and truthful,
- preserve the same shoot world,
- keep motion continuity across panels,
- include visible product evidence where the selected creative logic requires it,
- avoid generic lifestyle frames that do not prove the SKU.

## Rhythm Suggestion

Use this as a default pacing pattern when `picture_fragment_logic` does not provide a stronger SKU-specific sequence.

```yaml
rhythm_suggestion:
  beats:
    - quiet hook
    - brand world / buyer context
    - product proof moment
    - motion or use completion
    - restrained hero frame
```

This is pacing guidance, not a fixed role contract. If product truth, `creative_type`, or available proof needs a different order, write the reason in `picture_fragment_logic`.

## End Frame Contract

The closing purchase-confidence task must inherit `end_frame` from the `DTC Creative Reference Pack`; do not bind this rule to a fixed panel number.

```yaml
end_frame:
  product_position:
  logo_or_label_visibility:
  proof_memory:
  CTA_intent:
  camera_state:
  lighting_state:
```

Use `end_frame` to keep the closing image restrained, product-readable, and connected to the proof already shown.

## Video-Ready Keyframe Criteria

Every panel must:

- show the product clearly,
- preserve Product Truth Card locks,
- inherit `creative_type`, `scene_ref`, `model_ref`, `motion_ref`, and `camera_ref`,
- inherit `brand_film_mode` as internal brand-film language without director names,
- keep Chinese `ref_descriptions` so every selected option explains what it does,
- contain a visible action state that can continue into video generation,
- include real physical contact or plausible contact shadows,
- carry continuity from the previous panel,
- avoid fake UI, fake reviews, fake claims, fake badges, and unsupported result shots.

## Script Binding

The English script row for each panel must bind to the same camera and motion:

```text
panel camera_ref + motion_ref -> script Camera / Motion
panel borrowed logic -> script Reference Logic
panel visual proof -> subtitle and voiceover
```

Do not use voiceover to compensate for missing proof in the image.
