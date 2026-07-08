# Cinematic Grammar Rules

## Purpose

Translate "cinematic / premium / brand film" intent into concrete visual grammar.

## Weak Words

Do not use these as final visual instructions:

```text
cinematic
premium
luxury
high-end
blockbuster
movie-like
dramatic
8K
masterpiece
brand film
```

These words can describe user intent, but the storyboard prompt must translate them into specific visual rules.

## Grammar Fields

```yaml
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
```

## Camera Rules

Every camera choice must serve a function:

```text
hook_camera: create attention through product-related framing
context_camera: establish brand world or buyer context
proof_camera: make product evidence inspectable
motion_camera: carry the action chain
hero_camera: settle buyer confidence
```

Do not choose a camera only because it looks premium.

## Light Rules

Each storyboard should keep one main light logic.

Useful instructions:

```text
soft daylight from camera-left
large diffused window light
warm practical lamp in background
narrow edge highlight along product silhouette
controlled studio softbox above and left
low sun backlight with real contact shadow
```

Avoid:

```text
random dramatic lighting
fantasy glow
impossible rim light
inconsistent panel-to-panel light direction
floating product shadow
```

## Material Rules

Make the product material readable.

```text
fabric: weave, tension, fold, touch pressure
paper: edge, matte grain, slight bend
plastic: translucency, molded edge, controlled highlight
metal: clean edge highlight, real reflection
glass: refraction, controlled reflection, contact shadow
liquid: viscosity, surface tension, real pour
food: texture, moisture, realistic surface
wood: grain, matte reflection, contact mark
```

## Pacing Suggestion

Use this only when `picture_fragment_logic` does not require a stronger SKU-specific sequence:

```text
quiet hook
brand world / buyer context
product proof moment
motion or use completion
restrained hero frame
```

This is guidance, not a hard panel contract.

## Same-World Rules

The five panels must feel like the same brand-film shoot:

```text
same product instance
same light family
same color grade
same material response
same human presence strategy
same background density
same prop policy
same camera restraint level
```
