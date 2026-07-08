# 来源采集与素材使用策略

## 目标

把广告参考变成可追溯的创意结构，不把外部素材当成可随意复制的资产库。

## Source Types

```yaml
source_types:
  public:
    description: publicly reachable pages or ad libraries
    default_capture:
      - source_url
      - page_title
      - public summary
      - allowed screenshot or keyframe when access and platform rules permit
      - structured ad_reference decomposition
    restricted_capture:
      - original video files
      - full ad downloads
      - private brand assets
      - gated creative-library assets

  authorized:
    description: user-owned, user-paid, logged-in, or explicitly permitted source
    allowed_capture:
      - source_url
      - screenshots
      - keyframes
      - original files when the user has rights to use them
      - transcripts or scripts when accessible
      - brand assets when user-owned or authorized

  user_provided:
    description: files, links, screenshots, scripts, competitor lists, or examples supplied by the user
    allowed_capture:
      - uploaded files
      - screenshots
      - downloaded files supplied by the user
      - scripts
      - notes
      - reference URLs

  local_file:
    description: local workspace files already available for this run
    allowed_capture:
      - local path
      - file metadata
      - derived keyframes or screenshots when relevant

  fallback:
    description: source access failed, so a lower-fidelity reference was used
    allowed_capture:
      - attempted_source_url
      - fallback_type
      - fallback_source_url
      - reason
```

## Public-Source Rule

For public sources, default to structural learning:

- Keep the URL.
- Summarize the visible page or ad.
- Capture screenshots or keyframes only when the platform surface allows access and the result is needed for decomposition.
- Convert the reference into `ad_reference`.
- Use scene, hook, pacing, product-proof mechanic, and camera logic as inspiration.

Do not store public original videos, full ad files, private brand assets, or gated assets unless the source is reclassified as `authorized` or `user_provided`.

## Authorized And User-Provided Rule

Authorized and user-provided sources may be saved more fully, but the run must record why the source is allowed:

```yaml
permission_basis:
  source_type:
  user_supplied: true | false
  user_owned_or_authorized: true | false
  notes:
```

## Source Record

Every reference, including failed attempts, must create a source record:

```yaml
source_record:
  source_url:
  source_type: public | authorized | user_provided | local_file | fallback
  allowed_capture:
  captured_assets:
  local_paths:
  capture_time:
  permission_basis:
  notes:
```

## Use Boundaries

Captured references may be used for:

- ad structure decomposition
- scene and camera selection
- model or hand-presence strategy
- motion chain selection
- hook and CTA pattern selection
- storyboard prompt structure
- English script pacing

Captured references must not be used to:

- replace the current SKU's Product Truth Card
- copy a competitor product design
- copy a brand logo, artwork, or protected character
- invent claims, certifications, UI, reviews, or badges
- imply authorization that was not recorded

## Fallback Order

When a source is blocked, inaccessible, login-gated, or unsafe to capture:

```text
platform page
-> search result summary
-> manual link supplied by user
-> user-provided reference
-> uploaded asset
-> built-in reference libraries
```

Record the fallback:

```yaml
fallback_record:
  attempted_source_url:
  fallback_type:
  fallback_source_url:
  user_provided_asset_path:
  reason:
```
