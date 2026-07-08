# 实时 DTC 广告参考采集策略

## 目标

Collect only enough reference evidence to choose a DTC creative structure for the current SKU. Product facts come from the Product Truth Card, not from competitor references.

## Input

```yaml
product_input:
  product_url:
  product_images:
  sku_brief:
  product_truth_card:
  selected_category_adapters:
```

## Live Crawl Plan

```yaml
live_crawl_plan:
  product_category:
  product_behavior:
  buyer_problem:
  proof_type:
  competitor_keywords:
  adjacent_category_keywords:
  platform_keywords:
  region_keywords:
  source_priority:
  expected_capture_type:
```

Completion criteria:

- Search terms include product category, behavior, buyer problem, and platform.
- At least two source classes are attempted when available: public, authorized, user_provided, local_file, or fallback.
- Every attempt creates a `source_record`.
- Blocked sources produce fallback records.

## Buyer Problem Seeds

Derive `buyer_problem` and `proof_type` from `buyer_situation_router` in [dtc-creative-pattern-library.md](dtc-creative-pattern-library.md).

Use the matched buyer situation to search for reference structures that prove the same kind of problem, not to copy another SKU's claims or assets.

## Source Priority

1. User-provided references.
2. User-owned or authorized account/library references.
3. Public brand pages, public landing pages, public ad-library pages, public social pages, public YouTube pages.
4. Search-result summaries and public snippets.
5. Built-in reference libraries.

## Capture Policy

Follow [source-compliance-policy.md](source-compliance-policy.md).

For public sources, prefer:

- `source_url`
- page title or visible summary
- permitted screenshot/keyframe
- hook and CTA text visible on the page
- structured `ad_reference`

For authorized or user-provided sources, save richer files only when the permission basis is recorded.

## Source Record

```yaml
source_record:
  source_url:
  source_type: public | authorized | user_provided | local_file | fallback
  platform:
  brand:
  category:
  country_or_region:
  language:
  allowed_capture:
  captured_assets:
    screenshots:
    keyframes:
    transcript:
    local_files:
  blocked:
  fallback_used:
  notes:
```

## Fallback Handling

If no live reference can be captured, set:

```yaml
reference_status: reference_sparse
fallback_reference_basis:
  - category adapter
  - built-in creative pattern library
  - built-in scene/model/motion/camera libraries
```

This is allowed only when the Product Truth Card is strong enough. A sparse reference state must not weaken locked product terms.
