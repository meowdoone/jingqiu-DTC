# Ad Reference Decomposition Schema

## Purpose

Turn collected references into reusable DTC structure while keeping competitor or public-source material separate from product truth.

Every selected ad reference must support `creative_type`, `scene_ref`, `motion_ref`, `model_ref`, and `camera_ref` selection.

References without `source_url` or local source path cannot enter `selected_ad_references`.

## Schema

```yaml
ad_reference:
  source_url:
  source_type: public | authorized | user_provided | local_file | fallback
  local_asset_path:
  capture_time:
  permission_basis:
  platform:
  brand:
  category:
  product_type:
  region:
  language:
  format:
  aspect_ratio:
  duration:

  original_assets:
    video:
    screenshots:
    thumbnails:
    keyframes:
    transcript:
    subtitles:
    brand_assets:
    landing_page_frames:

  hook:
    first_3_seconds:
    opening_frame:
    opening_line:
    hook_type:
    visual_interruption:
    buyer_tension:
    reason_to_watch:

  scene:
    scene_ref_candidate:
    location:
    surface:
    lighting:
    props:
    realism_level:
    scene_transition:
    horizontal_16_9_fit:

  model:
    model_ref_candidate:
    presence_type:
    role:
    wardrobe:
    hand_or_body_visibility:
    expression:
    continuity_notes:

  motion:
    motion_ref_candidate:
    start_state:
    action:
    end_state:
    human_action:
    product_action:
    camera_motion:
    transition:
    pacing:
    reusable_clip_logic:

  camera:
    camera_ref_candidate:
    shot_size:
    camera_position:
    camera_movement:
    focus_behavior:
    transition_logic:

  proof:
    proof_mechanic:
    product_detail_shown:
    objection_answered:
    visual_evidence:
    unsupported_claim_risk:

  script:
    spoken_line_pattern:
    subtitle_pattern:
    CTA:
    pacing_structure:
    camera_motion_language:

  reusable_pattern:
    borrowed_structure:
    borrowed_scene_logic:
    borrowed_motion_logic:
    borrowed_camera_logic:
    borrowed_script_logic:
    picture_fragment_logic:
    what_not_to_copy:
```

## Required Judgement

Each `ad_reference` must state:

- what can be borrowed as structure,
- what cannot be copied,
- which creative type it supports,
- which scene/model/motion/camera candidates it suggests,
- whether it conflicts with `locked_terms`,
- whether it risks unsupported claims, fake UI, fake reviews, fake badges, or copied brand assets.

## Allowed Reuse

Use references for:

- hook structure,
- buyer tension,
- scene logic,
- model presence strategy,
- motion chain,
- camera language,
- proof mechanic,
- script pacing,
- CTA shape.

Do not use references for:

- replacing product color, type, geometry, material, logo, print, packaging, or design asset,
- importing competitor claims,
- copying a protected graphic, mascot, logo, UI, review, certification, or badge,
- weakening Product Truth Card locks.

## Output Use

Selected `ad_reference` records feed the internal `DTC Creative Reference Pack`, storyboard image prompt, and English script.

Do not expose full records in the final three-section response unless the user asks.
