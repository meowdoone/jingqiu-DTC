# Category Adapters

## Purpose

Use one primary adapter after Product Truth Card creation. The adapter converts product truth into visual locks, allowed buyer events, proof beats, and drift checks.

Do not use category adapters as product evidence. They only decide how to preserve and demonstrate the SKU.

## Adapter Record

```yaml
category_adapter:
  adapter_id:
  triggers:
  required_locks:
  allowed_buyer_events:
  recommended_panels:
  high_risk_defaults:
  forbid_mutations:
  qa_checks:
```

## custom_apparel

Use for custom T-shirts, hoodies, sweatshirts, hats, socks, tote bags, and other apparel where the buyer can upload or choose artwork/text.

Required locks:

- garment category: T-shirt stays T-shirt, hoodie stays hoodie, cap stays cap.
- color and fabric family.
- neckline, sleeve length, hem, fit, and visible garment silhouette.
- print position, print scale, and print boundary.
- same Design Asset across upload preview, print detail, worn state, and final group/gift frame.
- same front/back side when only one side is evidenced.

Allowed buyer events:

- upload or preview a design,
- confirm print placement,
- inspect print/detail and fabric surface,
- check fit on a faceless or cropped wearer,
- show one design across a single item, gift, team, event, or bulk order.

Recommended five-panel chain:

1. SKU anchor: exact garment type, color, neckline, sleeves, and print zone.
2. Configuration: upload/preview of the same Design Asset.
3. Proof detail: print area, fabric surface, stitching, or placement.
4. Wearer proof: faceless torso/partial crop showing scale and fit.
5. Purchase confidence: same design on final garment, gift, group, or bulk context.

High-risk defaults:

- perfect smiling models,
- outdoor fashion hero shots,
- group lifestyle scenes where the print becomes unreadable,
- switching between T-shirt, hoodie, jersey, polo, or sweatshirt,
- changing the uploaded image or text every panel,
- fake Amazon customization UI,
- fake brand logos or copyrighted artwork.

Forbid mutations:

- `change_garment_type`
- `change_color`
- `change_neckline`
- `change_sleeve_length`
- `move_print_position`
- `resize_design_asset_between_panels`
- `swap_design_asset`
- `invent_logo_or_artwork`
- `add_unsupported_front_back_print`

Validation checks:

- the garment type is stable in all panels,
- the Design Asset is identical or clearly the same placeholder,
- the print remains readable enough for a buyer to inspect,
- no model face is needed unless the user supplied a model direction,
- no fake platform UI or fake review badge appears.

## personalized_product

Use for configurable, engraved, printed, monogrammed, photo-upload, name-customized, modular, or choice-based products.

Required locks:

- selected option,
- same uploaded image/text/name/logo placeholder,
- final output state,
- customization placement and scale,
- product base shape, material, and color,
- visible preview-to-product continuity.

Allowed buyer events:

- choose option,
- upload image/text,
- preview placement,
- inspect personalized area,
- show final product in use or gift context.

Recommended five-panel chain:

1. SKU anchor and customization area.
2. User choice or upload preview.
3. close proof of personalized area.
4. realistic use, display, wearing, holding, or gifting moment.
5. final confidence frame showing the same selected option and personalization.

High-risk defaults:

- changing names, photos, logos, or artwork between panels,
- fake UI that looks like Amazon, Shopify, TikTok, or a real brand dashboard,
- adding emotional scenes that hide the product,
- making the personalization look like an official brand logo.

Forbid mutations:

- `swap_personalization`
- `change_selected_option`
- `move_custom_area`
- `invent_brand_logo`
- `invent_fake_ui`
- `change_product_base`

Validation checks:

- the same personalization appears from preview to final state,
- customization placement and scale stay stable,
- final frame is product-led, not only emotional or decorative.

## worn_or_carried

Use when product value depends on body scale, fit, carrying, or contact.

Required locks:

- product silhouette, color, scale, fit, and body placement.
- same wearer crop or same body relationship across panels when a wearer is used.

Allowed buyer events:

- fit check,
- scale check,
- carry/wear setup,
- detail inspection on body.

## hand_operated_or_installed

Use when value depends on setup, assembly, buttons, handles, parts, openings, cords, ports, or installation.

Required locks:

- part set,
- operation order,
- hand relationship,
- connection or placement logic.

Allowed buyer events:

- open/close,
- align,
- insert,
- connect,
- press,
- assemble,
- place.

## placed_displayed_or_stored

Use for decor, storage, tabletop, packaging, and display products.

Required locks:

- scale against surface,
- material,
- placement logic,
- package or included pieces only if evidenced.

Allowed buyer events:

- unbox,
- place,
- arrange,
- store,
- compare size,
- final display.
