# DTC Motion Library

## Purpose

`motion_chain` makes the storyboard video-ready. Every selected motion must have:

```text
start_state -> action -> end_state
```

## Schema

```yaml
motion_ref:
  id:
  description:
  best_for:
  start_state:
  action:
  end_state:
  human_action:
  product_action:
  camera_support:
  video_keyframe_use:
  continuity_note:
  risk:
```

## Motion Entries

```yaml
motions:
  - id: pick-up
    description: 用拿起动作让商品进入使用位置或视觉中心。
    best_for: 可手持商品
    start_state: 商品静置在桌面或场景中
    action: 手进入画面拿起商品
    end_state: 商品进入使用位置或镜头中心
    human_action: hand enters, grips, lifts
    product_action: product moves from surface to hand
    camera_support: locked-off-demo / handheld-follow
    video_keyframe_use: 商品进入或使用准备 moment
    continuity_note: 手型和商品角度必须连续
    risk: 手遮挡商品

  - id: unbox
    description: 用开箱动作证明包装、部件和真实完整性。
    best_for: 包装、套装、多部件商品
    start_state: 包装关闭
    action: 打开包装并取出商品
    end_state: 商品和包装关系清楚
    human_action: hands open box, remove product
    product_action: product revealed from package
    camera_support: top-down-tabletop / tabletop-tracking
    video_keyframe_use: 真实感、开箱完整性或 proof setup moment
    continuity_note: 不要生成不存在的配件
    risk: 包装和商品不一致

  - id: align
    description: 用对齐动作证明尺寸、贴合、安装或定制位置。
    best_for: 安装、贴合、定制、尺寸适配
    start_state: 商品和目标对象分离
    action: 对齐商品和目标对象
    end_state: 位置或尺寸关系被确认
    human_action: hands align edges or placement
    product_action: product moves into fit position
    camera_support: top-down-tabletop / locked-off-demo
    video_keyframe_use: proof panel
    continuity_note: 对齐对象必须真实存在
    risk: 编造兼容关系

  - id: apply
    description: 用涂抹、贴合或按压证明实际使用状态。
    best_for: 护理、贴片、涂抹、身体接触商品
    start_state: 商品靠近身体或表面
    action: 涂抹、贴合或按压
    end_state: 使用状态可见
    human_action: hand applies product
    product_action: product contacts surface/body
    camera_support: macro-push-in / handheld-follow
    video_keyframe_use: proof or use-completion moment
    continuity_note: 不夸大效果
    risk: 生成虚假 before/after

  - id: pour
    description: 用倾倒动作证明液体质地、容量或容器关系。
    best_for: 液体、饮品、调料、清洁液、容器
    start_state: 容器倾斜前
    action: 倾倒
    end_state: 液体进入杯、碗、表面或目标容器
    human_action: hand tilts product
    product_action: liquid flows
    camera_support: macro-push-in / locked-off-demo
    video_keyframe_use: 质地或容量 proof
    continuity_note: 液体状态要真实
    risk: 液体过度完美或不符合物理

  - id: tap
    description: 用点击或轻触动作证明按钮、触控或开关机制。
    best_for: 电子、开关、小工具、按钮类商品
    start_state: 手指接近按钮或触控区
    action: 点击 / 轻触
    end_state: 商品状态变化或操作完成
    human_action: finger taps
    product_action: product responds visibly if evidence supports
    camera_support: macro-push-in / rack-focus
    video_keyframe_use: mechanism proof moment
    continuity_note: 不能生成假 UI
    risk: 虚构功能反馈

  - id: plug-in
    description: 用插入或连接动作证明接口、充电或适配关系。
    best_for: 电子、适配、充电、连接
    start_state: 线缆或接口分离
    action: 插入或连接
    end_state: 连接关系清楚
    human_action: hand guides connector
    product_action: connector enters port
    camera_support: macro-push-in / over-the-shoulder-product-check
    video_keyframe_use: 适配 proof
    continuity_note: 接口类型必须和商品证据一致
    risk: 编造兼容设备

  - id: wear
    description: 用穿戴动作证明身体位置、比例和使用状态。
    best_for: 服饰、配饰、穿戴、护具
    start_state: 商品未穿戴
    action: 穿上、戴上、套上
    end_state: 商品在身体上位置清楚
    human_action: body/hand wears product
    product_action: product fits body
    camera_support: handheld-follow / locked-off-demo
    video_keyframe_use: 使用证明或 benefit moment
    continuity_note: 模特身体和商品比例一致
    risk: 商品变形或比例错误

  - id: unfold
    description: 用展开动作证明折叠结构或完整形态。
    best_for: 折叠、收纳、服饰、便携商品
    start_state: 商品折叠或收纳
    action: 展开
    end_state: 商品完整形态可见
    human_action: hands unfold
    product_action: product expands
    camera_support: top-down-tabletop / tabletop-tracking
    video_keyframe_use: setup or proof panel for structure
    continuity_note: 展开前后是同一商品
    risk: 形状跳变

  - id: fold
    description: 用折叠动作证明收纳、便携或结构逻辑。
    best_for: 收纳、服饰、便携商品
    start_state: 商品展开
    action: 折叠
    end_state: 商品进入收纳状态
    human_action: hands fold
    product_action: product becomes compact
    camera_support: top-down-tabletop / handheld-follow
    video_keyframe_use: 便携 proof
    continuity_note: 折叠逻辑要真实
    risk: 商品结构不支持折叠

  - id: compare
    description: 用并置和指向动作证明尺寸、颜色、版本或旧方式差异。
    best_for: 尺寸、颜色、版本、旧方式对比
    start_state: 两个对象并置
    action: 手部指向或移动其中一个
    end_state: 差异被看见
    human_action: hand points, slides, swaps
    product_action: product contrasted with neutral object
    camera_support: split-screen-comparison / locked-off-demo
    video_keyframe_use: comparison proof panel
    continuity_note: 只能比较有证据的差异
    risk: 虚构竞品缺陷

  - id: rotate
    description: 用旋转动作证明商品多角度外观和关键细节。
    best_for: 外观、结构、包装、细节
    start_state: 商品正面或静止
    action: 旋转商品
    end_state: 侧面、背面或关键细节可见
    human_action: hand rotates or turntable motion
    product_action: product reveals multiple sides
    camera_support: orbit-product-reveal / macro-push-in
    video_keyframe_use: 商品细节 proof
    continuity_note: logo 和结构不能跳变
    risk: 生成不同商品

  - id: reveal
    description: 用移开遮挡或打开外层制造商品出现和选择确认。
    best_for: 礼品、开箱、定制、包装、选择
    start_state: 商品被部分遮挡
    action: 移开遮挡或打开外层
    end_state: 商品完整出现
    human_action: hand pulls cover/card/box
    product_action: product becomes visible
    camera_support: hero-reveal / top-down-tabletop
    video_keyframe_use: hook or hero moment
    continuity_note: 遮挡物不能变成假品牌资产
    risk: 过度戏剧化

  - id: hand-pass
    description: 用交接动作证明礼品、共享或社交使用场景。
    best_for: 礼品、社交、交接、家庭场景
    start_state: 商品在一只手中
    action: 递给另一只手
    end_state: 接收者拿到商品
    human_action: two hands pass product
    product_action: product remains visible during transfer
    camera_support: handheld-follow / locked-off-demo
    video_keyframe_use: 社交 proof 或 CTA frame
    continuity_note: 人物设定必须一致
    risk: 交接动作容易遮挡商品

  - id: texture-touch
    description: 用触摸、按压或滑过证明材质反馈和质感。
    best_for: 面料、材质、皮革、纸张、食品、护肤
    start_state: 手指靠近材质表面
    action: 触摸、按压、滑过
    end_state: 材质反馈可见
    human_action: fingers press or glide
    product_action: texture responds subtly
    camera_support: macro-push-in
    video_keyframe_use: sensory proof moment
    continuity_note: 反馈必须真实克制
    risk: AI 塑料感

  - id: close-open
    description: 用打开动作证明盖子、盒子、包、瓶或收纳结构。
    best_for: 盒子、盖子、包、瓶、夹具、收纳
    start_state: 商品关闭
    action: 打开
    end_state: 内部或功能状态可见
    human_action: hand opens lid/zip/flap
    product_action: product changes state
    camera_support: top-down-tabletop / macro-push-in
    video_keyframe_use: 机制或包装 proof
    continuity_note: 打开结构必须真实
    risk: 编造内部结构
```

## Motion Checks

Reject a motion choice when:

- the action cannot be shown in a still keyframe,
- the product does not support the action,
- the action requires unsupported claims,
- the selected camera cannot show the action,
- the selected proof moment loses product evidence.
