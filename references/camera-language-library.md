# DTC Camera Language Library

## Purpose

`camera_plan` makes each storyboard panel video-keyframe ready. Camera is not style decoration; it must support hook, proof, use, or CTA.

## Schema

```yaml
camera_ref:
  id:
  description:
  best_for:
  shot_size:
  camera_position:
  camera_motion:
  product_role:
  video_keyframe_use:
  transition_logic:
  risk:
```

## Camera Entries

```yaml
cameras:
  - id: locked-off-demo
    description: 固定镜头保留动作全过程，适合稳定证明操作和尺寸。
    best_for: 清楚证明操作、尺寸、使用关系
    shot_size: medium close-up
    camera_position: fixed 45-degree or eye-level
    camera_motion: no camera movement, action happens inside frame
    product_role: product remains readable throughout
    video_keyframe_use: demo and proof panels
    transition_logic: cut on completed action
    risk: 画面可能平，但最稳定

  - id: top-down-tabletop
    description: 俯拍桌面关系，适合开箱、摆放、对齐和定制。
    best_for: 开箱、选择、摆放、定制、对齐
    shot_size: top-down medium
    camera_position: overhead
    camera_motion: slight tabletop tracking or fixed
    product_role: product and hands clearly visible
    video_keyframe_use: setup or proof moment
    transition_logic: hand movement leads next frame
    risk: 容易像平面图，缺少真实空间

  - id: macro-push-in
    description: 缓慢推进到细节，适合材质、接口、纹理和包装证明。
    best_for: 材质、纹理、结构、按钮、接口、包装细节
    shot_size: macro close-up
    camera_position: close product detail
    camera_motion: slow push-in
    product_role: product detail is the hero
    video_keyframe_use: strongest proof moment
    transition_logic: push into detail then cut to use
    risk: 容易 AI 过锐或材质假

  - id: handheld-follow
    description: 跟随手或商品移动，适合真实使用流程。
    best_for: UGC、真实使用、旅行、运动、户外、家居流程
    shot_size: close or medium close-up
    camera_position: follows hand/product
    camera_motion: subtle handheld follow
    product_role: product stays near center
    video_keyframe_use: use-action moment
    transition_logic: follow motion continues across cut
    risk: 抖动过强、商品模糊

  - id: slow-dolly
    description: 缓慢推拉突出商品重要性，适合最后的购买信心画面。
    best_for: 商品高级展示、hero shot、品牌感
    shot_size: medium to close-up
    camera_position: frontal or 45-degree
    camera_motion: slow dolly in or out
    product_role: product becomes more important over time
    video_keyframe_use: end-frame confidence moment
    transition_logic: camera settles into end frame
    risk: 容易空泛高级感

  - id: rack-focus
    description: 用焦点转移把注意力从场景或人物转到商品。
    best_for: 商品和场景关系、人物到商品转移
    shot_size: medium close-up
    camera_position: foreground/background relationship
    camera_motion: focus shift
    product_role: focus lands on product
    video_keyframe_use: hook or buyer-context moment
    transition_logic: focus shift reveals product
    risk: 商品可能不够清楚

  - id: tabletop-tracking
    description: 沿桌面横向移动，连接多个操作步骤。
    best_for: 桌面流程、开箱、对齐、选择、比较
    shot_size: top-down or 45-degree
    camera_position: parallel to table movement
    camera_motion: horizontal track
    product_role: product moves along the frame
    video_keyframe_use: motion-chain moment
    transition_logic: track direction carries continuity
    risk: 道具过多会乱

  - id: orbit-product-reveal
    description: 围绕商品轻微环绕，展示外观和多角度细节。
    best_for: 商品外观、结构、多角度展示
    shot_size: close-up / hero close-up
    camera_position: around product
    camera_motion: slight orbit
    product_role: product center hero
    video_keyframe_use: proof or hero panel
    transition_logic: orbit reveals side/detail
    risk: 容易变成 3D 假感

  - id: hero-reveal
    description: 用揭示或稳定收尾，让商品成为最终购买信心画面。
    best_for: 收尾画面、礼品、包装、定制选择
    shot_size: clean product hero
    camera_position: front or 45-degree
    camera_motion: settle or reveal
    product_role: product dominates final frame
    video_keyframe_use: end-frame confidence moment
    transition_logic: action resolves into hero frame
    risk: 只漂亮不增强购买信心

  - id: match-cut
    description: 用形状、动作或方向匹配连接两个画面。
    best_for: 商品动作和场景动作连接
    shot_size: varies
    camera_position: matched composition
    camera_motion: matched action direction
    product_role: product connects two moments
    video_keyframe_use: panel transitions
    transition_logic: match shape, motion, or direction
    risk: 太复杂，AI 生成容易不稳

  - id: split-screen-comparison
    description: 在同一画面内对比版本、尺寸、颜色或 before/after。
    best_for: 对比、选择、before/after、尺寸/颜色/版本
    shot_size: two-panel comparison inside frame
    camera_position: symmetrical
    camera_motion: minimal
    product_role: product difference must be visible
    video_keyframe_use: comparison proof panel
    transition_logic: split screen resolves to chosen product
    risk: 容易生成假竞品或假结果

  - id: over-the-shoulder-product-check
    description: 从用户背后展示检查商品和购买判断。
    best_for: 选择、检查细节、购物判断、车内/办公/桌面
    shot_size: over-shoulder close-up
    camera_position: behind user, product in hands or on surface
    camera_motion: subtle push or fixed
    product_role: product is what user is checking
    video_keyframe_use: buyer-context moment
    transition_logic: user gaze/hand directs next proof frame
    risk: 肩膀、手或设备容易遮挡商品
```

## Camera Plan Slots

```yaml
camera_plan:
  opening_camera:
  context_camera:
  proof_camera:
  use_camera:
  end_frame_camera:
```

Product proof moments use `macro-push-in`, `locked-off-demo`, `split-screen-comparison`, or another proof-first camera that makes the product detail inspectable.
