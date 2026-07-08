# DTC Scene Library

## Purpose

`scene_ref` decides where the product can be proven. The scene is not decoration.

## Schema

```yaml
scene_ref:
  id:
  description:
  best_for:
  product_fit:
  location:
  surface:
  lighting:
  props_allowed:
  props_forbidden:
  human_presence:
  camera_space:
  proof_supported:
  production_risk:
  horizontal_16_9_notes:
```

## Scene Entries

```yaml
scenes:
  - id: studio-tabletop
    description: 在中性桌面上证明包装、材质、尺寸和细节。
    best_for: 泛 SKU、包装、配件、定制商品、细节证明
    product_fit: 商品可以放在桌面被检查
    location: 中性室内桌面
    surface: matte table / neutral tabletop
    lighting: soft daylight or soft studio daylight
    props_allowed: 包装、说明卡、手部、少量中性道具
    props_forbidden: 遮挡商品的装饰物、假 UI、假评论卡
    human_presence: hand-only or no-human
    camera_space: top-down, 45-degree, macro
    proof_supported: 材质、尺寸、包装、结构、选项
    production_risk: 容易太像棚拍
    horizontal_16_9_notes: 桌面需要横向留白，商品不能被裁切

  - id: bathroom-counter
    description: 把个护、美妆或洗护商品放进洗手台日常场景。
    best_for: 护理、美妆、个护、香氛、洗护
    product_fit: 商品自然出现在洗手台或镜柜边
    location: bathroom counter
    surface: stone counter / ceramic counter
    lighting: soft morning light
    props_allowed: 毛巾、镜子边缘、水滴、基础洗漱道具
    props_forbidden: 过多护肤品、假皮肤效果
    human_presence: hand-only / partial body
    camera_space: counter-level, mirror-adjacent, macro
    proof_supported: 质地、用法、日常流程、包装
    production_risk: 容易杂乱
    horizontal_16_9_notes: 保持台面横向干净，商品在视觉中心

  - id: kitchen-prep
    description: 用厨房准备、倒入、打开或清洁动作证明商品。
    best_for: 食品、饮品、厨房工具、容器、清洁用品
    product_fit: 商品参与准备、倒入、打开、清洁或盛放动作
    location: kitchen counter
    surface: wood / stone / stainless counter
    lighting: daylight kitchen
    props_allowed: 食材、杯子、碗、布、手部
    props_forbidden: 过度装饰食物、无法证明的效果
    human_presence: hand-only / home user
    camera_space: top-down, side close-up, tracking
    proof_supported: 容量、倒入、质地、清洁、使用流程
    production_risk: 道具容易遮挡商品
    horizontal_16_9_notes: 道具只服务商品动作

  - id: desk-setup
    description: 在办公桌面展示数码、文具、收纳或效率关系。
    best_for: 办公、数码、配件、文具、收纳、小工具
    product_fit: 商品进入工作桌面或设备旁
    location: desk setup
    surface: desk mat / wood desk
    lighting: window light / practical desk lamp
    props_allowed: laptop edge, notebook, cable, pen
    props_forbidden: 复杂设备墙、抢眼 RGB、假 app UI
    human_presence: hand-only / office worker
    camera_space: over-the-desk, tabletop tracking, rack focus
    proof_supported: 适配、尺寸、整理、连接、效率
    production_risk: 容易变成泛办公氛围
    horizontal_16_9_notes: 商品必须在桌面主轴上

  - id: travel-packing
    description: 在行李打包场景证明便携、尺寸和收纳。
    best_for: 收纳、服饰、配件、旅行用品、便携产品
    product_fit: 商品被放入包、箱、袋或旅行场景
    location: bed / suitcase / packing table
    surface: fabric / suitcase interior
    lighting: hotel or home daylight
    props_allowed: 行李箱、衣物边缘、护照边缘、收纳袋
    props_forbidden: 过度旅行大片、无关景点
    human_presence: hand-only / traveler
    camera_space: top-down packing, close-up insert
    proof_supported: 尺寸、便携、收纳、组合
    production_risk: 商品容易被衣物淹没
    horizontal_16_9_notes: 行李箱横向打开，商品在中心动作线上

  - id: bedside-routine
    description: 在床头日常流程里证明放置、触感、开关或护理。
    best_for: 睡眠、香氛、灯具、小家居、护理、阅读相关商品
    product_fit: 商品参与夜间或晨间流程
    location: bedside table
    surface: wood / fabric / nightstand
    lighting: soft warm practical light
    props_allowed: 书、杯子、床品边缘、灯光
    props_forbidden: 过度情绪化人物、杂乱床品
    human_presence: hand-only / home user
    camera_space: locked-off, slow push-in, rack focus
    proof_supported: 日常融入、触感、开关、放置
    production_risk: 容易太氛围不证明商品
    horizontal_16_9_notes: 保持床头横向层次，商品不靠边

  - id: gym-locker
    description: 在运动前后场景证明便携、穿戴和场景身份。
    best_for: 运动用品、饮品、毛巾、包、护具、穿戴产品
    product_fit: 商品在运动前后被拿取、穿戴、收纳
    location: gym locker / bench
    surface: bench / locker shelf
    lighting: clean overhead gym light
    props_allowed: 水瓶、毛巾、运动鞋边缘
    props_forbidden: 过多人体运动夸张动作
    human_presence: athlete / hand-only
    camera_space: handheld follow, low angle, product close-up
    proof_supported: 便携、穿戴、耐用、场景身份
    production_risk: 商品容易被动作遮挡
    horizontal_16_9_notes: 商品始终在手部动作中心

  - id: car-interior
    description: 在车内空间证明适配、固定、尺寸和便携。
    best_for: 车载用品、便携设备、收纳、香氛、数码配件
    product_fit: 商品自然出现在中控、座椅、杯架或后备箱
    location: car interior
    surface: dashboard / seat / console
    lighting: natural daylight through window
    props_allowed: 车内真实结构
    props_forbidden: 假导航 UI、危险驾驶动作
    human_presence: hand-only / driver partial
    camera_space: over-the-shoulder, close insert, locked-off
    proof_supported: 适配、尺寸、固定、便携
    production_risk: 空间窄，商品容易暗
    horizontal_16_9_notes: 横屏需保留车内空间线索

  - id: gifting-table
    description: 在礼品包装桌面证明定制、包装和送礼选择。
    best_for: 礼品、定制、包装好看的商品
    product_fit: 商品被打开、摆放、递出或个性化展示
    location: tabletop / gift wrapping surface
    surface: paper / table / fabric
    lighting: soft daylight
    props_allowed: 包装纸、丝带、卡片、手部
    props_forbidden: 假品牌卡、假祝福文字
    human_presence: hand-only / couple / shopper
    camera_space: top-down, macro, hero reveal
    proof_supported: 包装、定制、礼物感、选择
    production_risk: 容易变成节日装饰
    horizontal_16_9_notes: 商品和包装层次横向展开

  - id: unboxing-table
    description: 在开箱桌面证明部件、包装和完整性。
    best_for: 套装、包装、配件、多部件商品
    product_fit: 商品从包装中取出并展示部件
    location: clean table
    surface: matte table
    lighting: soft daylight
    props_allowed: 包装盒、内衬、说明书、手部
    props_forbidden: 不存在的配件
    human_presence: hand-only
    camera_space: top-down, 45-degree, tabletop tracking
    proof_supported: 包装、部件、开箱、完整性
    production_risk: 容易编造配件
    horizontal_16_9_notes: 部件横向排布，不遮挡主商品

  - id: outdoor-use
    description: 在户外动作中证明便携、使用关系和场景适配。
    best_for: 户外、运动、宠物、便携、穿戴产品
    product_fit: 商品必须自然参与户外动作
    location: park / trail / street / outdoor table
    surface: ground / bench / hand-held
    lighting: natural daylight
    props_allowed: 极少量场景线索
    props_forbidden: 夸张旅行大片、难以证明的性能
    human_presence: user / athlete / hand-only
    camera_space: handheld follow, medium close-up, product insert
    proof_supported: 使用关系、便携、场景身份
    production_risk: 背景容易压过商品
    horizontal_16_9_notes: 背景虚化，商品靠近镜头

  - id: no-human-product-macro
    description: 用无人物微距场景证明商品材质、结构和工艺。
    best_for: 商品本身细节足够强，不需要人物
    product_fit: 商品可通过材质、结构、包装自己证明
    location: neutral macro setup
    surface: matte / reflective controlled surface
    lighting: soft studio daylight
    props_allowed: 无或极少
    props_forbidden: 人物、复杂道具、假 UI
    human_presence: no-human
    camera_space: macro, slow push-in, orbit
    proof_supported: 材质、结构、工艺、包装
    production_risk: 容易缺少使用语境
    horizontal_16_9_notes: 需要用 5 格镜头变化保持节奏
```

## Scene Lock

After selecting a scene, five panels must preserve:

- same space,
- same surface family,
- same light direction,
- same prop system,
- same product scale logic.
