# DTC Model / Human Presence Library

## Purpose

`model_ref` decides whether a human, hand, body crop, founder, expert, or no-human strategy enters the storyboard.

## Schema

```yaml
model_ref:
  id:
  description:
  best_for:
  presence_type:
  role:
  visibility:
  wardrobe:
  hands:
  face:
  body_language:
  continuity_lock:
  when_to_use:
  when_not_to_use:
  risk:
```

## Model Entries

```yaml
models:
  - id: no-human-product-macro
    description: 只让商品和光线出场，突出细节、结构、材质或包装。
    best_for: 细节、结构、材质、包装本身足够强
    presence_type: no-human
    role: none
    visibility: product only
    wardrobe: none
    hands: none
    face: none
    body_language: none
    continuity_lock: product, light, background continuous
    when_to_use: 商品自己能解释价值
    when_not_to_use: 必须真人使用才看得懂
    risk: 缺少使用语境

  - id: hand-only
    description: 用手部动作完成演示，避免身份信息干扰。
    best_for: SKU 演示、开箱、使用、触摸、尺寸证明
    presence_type: partial-human
    role: user hands
    visibility: hands only
    wardrobe: neutral sleeves if visible
    hands: clean natural hands, consistent tone/nails
    face: not visible
    body_language: precise, product-first
    continuity_lock: same hand type, skin tone, action direction
    when_to_use: 需要动作证明但不需要身份
    when_not_to_use: 需要身份、情绪或口播信任
    risk: 手遮挡商品

  - id: ugc-creator
    description: 用日常创作者身份解释商品真实使用。
    best_for: 真实使用、解释、信任建立
    presence_type: human
    role: creator / everyday user
    visibility: face optional, upper body or hands
    wardrobe: simple casual, non-branded
    hands: natural demo gestures
    face: friendly but not over-modeled
    body_language: direct, practical
    continuity_lock: same person, outfit, scene
    when_to_use: 观众需要看到真实使用者
    when_not_to_use: 商品细节比人物更重要
    risk: 商品细节容易变弱

  - id: founder
    description: 用创始人或制作者身份说明设计原因和品牌信任。
    best_for: 品牌原因、设计逻辑、研发理由
    presence_type: human
    role: founder / maker
    visibility: upper body + product
    wardrobe: simple credible wardrobe
    hands: holding/pointing to product
    face: calm credible
    body_language: explains product, not performing
    continuity_lock: product always in frame
    when_to_use: 有真实品牌或创始人语境
    when_not_to_use: 没有创始人素材
    risk: 空泛品牌片

  - id: shopper
    description: 用买家检查或选择动作表现购买判断。
    best_for: 选择、对比、试用、购买判断
    presence_type: human / partial-human
    role: buyer deciding
    visibility: hands, torso, over-shoulder
    wardrobe: everyday neutral
    hands: compares, picks, checks
    face: usually not needed
    body_language: evaluating
    continuity_lock: action or gaze around product choice
    when_to_use: 存在选项、适配、颜色、尺寸疑虑
    when_not_to_use: 没有购买选择场景
    risk: 泛购物氛围

  - id: expert
    description: 用专业使用者动作展示技术、护理或工具类商品。
    best_for: 技术、护理、工具、功能商品
    presence_type: human
    role: expert user
    visibility: hands / upper body
    wardrobe: category-appropriate, no fake credential
    hands: careful demonstration
    face: optional
    body_language: precise and calm
    continuity_lock: no fake certification, product visible
    when_to_use: 有证据支持专业动作
    when_not_to_use: 没有专家语境
    risk: 假专家感

  - id: couple
    description: 用双人互动展示礼品、家庭或共享场景。
    best_for: 礼品、家庭、共享场景
    presence_type: human group
    role: two users
    visibility: hands / partial bodies
    wardrobe: coordinated neutral
    hands: passing, unboxing, using together
    face: optional
    body_language: restrained, product-focused
    continuity_lock: same two people across panels
    when_to_use: 礼物或共享使用有意义
    when_not_to_use: 单人场景足够证明
    risk: 情绪表达容易压过商品证明

  - id: parent
    description: 用照护者动作展示家庭或儿童相关商品。
    best_for: 家庭、儿童相关、照护类商品
    presence_type: human
    role: parent / caregiver
    visibility: hands / partial body
    wardrobe: home casual
    hands: careful handling
    face: optional
    body_language: protective, practical
    continuity_lock: no unsupported safety/effect claims
    when_to_use: 证据支持家庭或照护使用
    when_not_to_use: 商品和家庭语境无关
    risk: 编造安全声明

  - id: athlete
    description: 用运动者身体关系展示穿戴、户外或健身商品。
    best_for: 运动、户外、穿戴、健身商品
    presence_type: human
    role: active user
    visibility: partial body / hands / gear use
    wardrobe: sport neutral
    hands: grip, wear, pack, adjust
    face: not needed
    body_language: active but controlled
    continuity_lock: product visible, not buried by movement
    when_to_use: 商品有真实运动或户外使用语境
    when_not_to_use: 商品不支持运动场景
    risk: 夸大性能

  - id: office-worker
    description: 用办公人群动作展示桌面、数码或效率工具。
    best_for: 办公、桌面、数码、效率工具
    presence_type: human / partial-human
    role: office user
    visibility: hands, torso, over-desk
    wardrobe: neutral workwear
    hands: type, plug, organize, place
    face: not needed
    body_language: focused
    continuity_lock: desk, hands, device relationship stable
    when_to_use: 商品进入工作流程
    when_not_to_use: 商品和办公无关
    risk: 泛办公氛围

  - id: home-user
    description: 用家庭用户动作展示家居、清洁、收纳或日常使用。
    best_for: 家居、日常使用、收纳、清洁、家庭商品
    presence_type: human / partial-human
    role: everyday home user
    visibility: hands / partial body
    wardrobe: casual neutral
    hands: use, place, clean, open
    face: optional
    body_language: natural
    continuity_lock: same home scene and light
    when_to_use: 商品依赖家庭日常流程
    when_not_to_use: 专业或户外场景更合适
    risk: 生活方式化但缺少证明
```

## Selection Rules

- Prefer `no-human-product-macro` or `hand-only` when product proof does not require identity.
- Use faces only when identity or trust is needed and evidence supports it.
- For custom apparel, prefer faceless torso or cropped wearer unless the user provides model direction.
- Model strategy must not hide the product or weaken product proof.
