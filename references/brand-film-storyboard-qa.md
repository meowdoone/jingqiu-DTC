# Brand Film Storyboard QA

## Purpose

Check whether the five-panel storyboard has brand-film quality while still serving SKU conversion.

## Must Pass

```text
1. Product truth is unchanged.
2. The five panels feel like the same shoot.
3. Light direction is coherent.
4. Product material is readable.
5. Every panel has a shot function from picture_fragment_logic.
6. Product proof appears where the selected creative logic needs it.
7. The end frame strengthens buyer confidence.
8. Human presence, scene, and props support product proof.
9. There are no fake UI, fake reviews, fake badges, or fake certifications.
10. Panels can continue as video keyframes.
```

## Failure Conditions

Reject or regenerate when any of these appear:

```text
only says cinematic but has no concrete camera/light/material rules
five panels look like different projects
product proportion jumps
product color or material jumps
light direction jumps
background density jumps
product becomes secondary
scene is decorative only
props dominate product proof
selected proof moment has no proof
end frame is only aesthetic
product looks floating
shadow does not contact a real surface
AI plastic material is obvious
brand-film mood hides product truth
```

## Panel QA

```yaml
panel_qa:
  each_panel:
    pass_if:
      - product is visible
      - panel task follows picture_fragment_logic
      - camera and motion match the Reference Pack
      - light and material logic stay in the same world
    fail_if:
      - product is hidden
      - panel task is generic lifestyle
      - unsupported claim appears
      - brand-film mood overrides product proof

  proof_moment:
    pass_if:
      - material, mechanism, fit, texture, option, size, or use proof is visible
      - camera supports inspection
    fail_if:
      - only pretty shot
      - no proof asset
      - claim cannot be seen

  end_frame:
    pass_if:
      - product_position is clear
      - logo_or_label_visibility follows Product Truth Card
      - proof_memory remains
      - CTA_intent is connected to prior proof
      - camera_state settles
      - lighting_state stays continuous
    fail_if:
      - only aesthetic ending
      - product unclear
      - no buyer confidence
```

## Script QA

Script `Camera / Motion` must come from:

```text
DTC Creative Reference Pack.camera_selection
Brand Film Look Pack.shot_function_map
Brand Film Look Pack.cinematic_grammar
```

Script `Reference Logic` must explain borrowed structure without naming specific brands.

Use concrete phrases:

```text
Borrowed detail-first hook structure
Borrowed macro proof mechanic
Borrowed routine-context pacing
Borrowed hero end-frame CTA structure
```

Avoid vague phrases:

```text
inspired by a premium ad
cinematic shot
luxury brand feel
beautiful product scene
```
