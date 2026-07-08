# Brand Film Mode Library

## Purpose

`brand_film_mode` turns internal cinematic direction into DTC brand-film language for SKU storyboards.

Do not expose director names, film names, or "like this director" language in final user-facing output. The final output uses brand-film language only.

## Schema

```yaml
brand_film_mode:
  mode_id:
  visual_signature:
  key_technique:
  product_translation:
  camera_translation:
  lighting_translation:
  risk:
```

## Brand Film Modes

```yaml
brand_film_modes:
  - mode_id: monumental-minimal
    visual_signature: 极简、沉浸、巨大尺度、宽幅空间、低噪声画面
    key_technique: 用负空间、稳定构图、慢速推进和尺度对比让商品有分量
    product_translation: 适合高单价、外观强、科技感、家居、包装质感强的商品；商品必须是空间中的核心证据
    camera_translation: locked-off wide-to-close, slow dolly, restrained macro insert
    lighting_translation: soft directional light, muted contrast, haze depth, controlled highlights
    risk: 容易太空、太概念，商品证明变弱

  - mode_id: precision-noir
    visual_signature: 去饱和、深阴影、锐利边缘、精确对齐、冷静秩序
    key_technique: 用低调光、暗部层次、结构近景和精准机位强化可信细节
    product_translation: 适合工具、数码、配件、材质、接口、结构、质量证明型商品；商品像证据一样被检查
    camera_translation: fixed close-up, rack focus, macro push-in, controlled product turn
    lighting_translation: low-key side light, hard edge highlight, desaturated gray/teal balance
    risk: 容易过暗、过冷，导致颜色和材质失真

  - mode_id: poetic-warmth
    visual_signature: 暖色、柔焦、慢动作、局部遮挡、近距离生活片段
    key_technique: 用实践光、浅景深、轻微手持和色彩记忆建立情绪
    product_translation: 适合礼品、家居、香氛、护理、穿搭、生活方式商品；商品必须和手、环境或使用动作产生真实关系
    camera_translation: subtle handheld follow, slow push, soft rack focus, close insert
    lighting_translation: warm practical light, soft shadow, gentle bloom, colored reflection
    risk: 容易变成纯氛围，商品边界和 proof 不够清楚

  - mode_id: symmetrical-pastel
    visual_signature: 对称、粉彩、正面构图、平面化空间、装饰性秩序
    key_technique: 用正交视角、整齐摆放、颜色分区和重复秩序降低选择成本
    product_translation: 适合包装、礼品、套装、颜色选项、定制、组合型商品；商品和选项按秩序排列
    camera_translation: top-down tabletop, frontal locked-off, centered hero reveal
    lighting_translation: even soft daylight, pastel fill, low contrast, clean shadows
    risk: 容易过度装饰或像平面海报，缺少真实使用证明

  - mode_id: natural-documentary
    visual_signature: 自然光、日常空间、克制动作、真实节奏、无炫技
    key_technique: 用真实环境和自然动作让商品证明可信
    product_translation: 适合家居、母婴、清洁、厨房、户外、日用、真实场景型商品；环境必须服务商品
    camera_translation: handheld follow, over-the-shoulder, locked-off proof, natural insert
    lighting_translation: available daylight, practical shadows, soft contrast
    risk: 容易不够高级或画面杂乱

  - mode_id: industrial-atmosphere
    visual_signature: 暗色、机械、湿润反射、工业细节、冷色层次
    key_technique: 用表面反射、结构线、机械纹理和低调光强化产品力量
    product_translation: 适合电子、设备、工具、车载、硬件、性能型商品；商品要和结构线、接口、表面纹理形成关系
    camera_translation: close industrial insert, rack focus, slow lateral move
    lighting_translation: cool side light, controlled reflection, low-key contrast
    risk: 容易让背景材质压过商品

  - mode_id: epic-scale
    visual_signature: 宽幅、强尺度、低角度、色彩分段、英雄式收束
    key_technique: 用宽幅构图、低角度和颜色段落制造商品发布感
    product_translation: 适合发布感强、礼品、户外、运动、品牌 campaign 型商品；商品必须是尺度关系里的锚点
    camera_translation: low angle hero, ultra-wide setup, slow reveal, final scale frame
    lighting_translation: golden hour, strong directional light, clear silhouette
    risk: 容易过度宏大，SKU 细节弱

  - mode_id: tactile-handmade
    visual_signature: 有机形状、手作纹理、温和运动、自然材料、触感优先
    key_technique: 用手部、材质、纸张、纤维、边缘和温和动作建立亲近感
    product_translation: 适合手作、纸品、纺织、礼品、儿童、家居、自然材质商品；材质和手部接触是画面核心
    camera_translation: hand-led motion, texture close-up, gentle push, organic framing
    lighting_translation: soft natural light, warm fill, visible texture shadows
    risk: 容易变得童趣或不够商业
```

## Selection Rules

- Select one `brand_film_mode` only after `creative_type`, `scene_ref`, `motion_chain`, `model_ref`, and `camera_plan` are chosen.
- Use `brand_film_mode` to shape composition, color, lighting, camera restraint, pacing, and end-frame mood.
- Do not let `brand_film_mode` override Product Truth Card locks, product color, material, scale, or proof requirements.
- Final user-facing output uses brand-film language only.
