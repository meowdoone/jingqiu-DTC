# Brand Film Look Director

## Purpose

`Brand Film Look Director` runs after `DTC Creative Reference Pack` and before `Storyboard Design Expert`.

It turns DTC creative logic into concrete brand-film visual language. It does not change Product Truth Card, `creative_type`, selected references, `scene_ref`, `motion_chain`, `model_ref`, or `camera_plan`.

## Input

```yaml
brand_film_look_input:
  product_truth_card:
  dtc_creative_reference_pack:
  selected_ad_references:
  selected_scene_ref:
  selected_motion_chain:
  selected_model_ref:
  selected_camera_plan:
  target_platform:
  desired_visual_level:
  brand_or_seller_context:
```

## Steps

```text
1. Confirm brand_film_mode
2. Build brand_world_lock
3. Build cinematic_grammar
4. Build shot_function_map
5. Build material_and_light_rules
6. Build pacing_rules
7. Select signature_shot
8. Build end_frame_rule
9. Build failure_rules
10. Output Brand Film Look Pack
```

## Pack Schema

```yaml
brand_film_look_pack:
  brand_film_mode:
    mode_id:
    visual_signature:
    key_technique:
    product_translation:
    camera_translation:
    lighting_translation:
    risk:

  brand_world_lock:
    visual_temperature:
    color_grade:
    lighting_source:
    material_language:
    camera_behavior:
    motion_pacing:
    human_presence:
    product_scale:
    background_density:
    prop_policy:

  cinematic_grammar:
    camera_body_logic:
    lens_logic:
    focal_length_feel:
    shot_distance_rules:
    camera_movement_rules:
    lighting_direction:
    shadow_rules:
    color_grade_tokens:
    texture_rules:
    cut_rhythm:

  shot_function_map:
    panels:
      - panel_number:
        function:
        brand_film_task:
        camera_behavior:
        lighting_behavior:
        product_role:

  material_and_light_rules:
    main_light_source:
    fill_light:
    contact_shadow:
    surface_reflection:
    texture_visibility:
    product_edge_highlight:
    forbidden_light_effects:

  pacing_rules:
    beat_1:
    beat_2:
    beat_3:
    beat_4:
    beat_5:
    rhythm_note:

  signature_shot:
    panel:
    shot_type:
    why_it_is_irreplaceable:
    product_truth_supported:
    camera_language:
    material_language:

  end_frame_rule:
    product_position:
    label_or_logo_visibility:
    proof_memory:
    CTA_intent:
    camera_settle:
    lighting_continuity:

  failure_rules:
    - concrete rejection condition
```

## Rules

- Do not use vague style words as final visual instructions.
- Convert cinematic, premium, luxury, blockbuster, high-end, and dramatic lighting into camera, lens, light, material, motion, rhythm, composition, and product-scale rules.
- `shot_function_map` must follow `picture_fragment_logic`; it must not force a universal panel role template.
- `signature_shot` must be product-led, proof-supporting, video-generatable, and consistent with the Brand Film Look Pack.
- `end_frame_rule` must increase buyer confidence without inventing claims.
- Failure rules must be concrete enough to reject weak generated storyboards.

## Final Output Safety

Do not expose director names, film names, or "like this director" language in user-facing output.
