# DTC Creative Type Library

## Purpose

`creative_type` is the main DTC creative logic selected by `DTC Creative Director`. It should decide what the buyer wants to feel, become, remember, or purchase before deciding how the product proof appears.

Choose exactly one main `creative_type`. Do not blend multiple main types unless one is clearly secondary in the Reference Pack.

Default to DTC-first creative types. Use proof-first or demo-first types only when the user explicitly asks for Amazon listing, how-to, product explanation, functional demonstration, mechanism explanation, or size/fit proof.

## Schema

```yaml
creative_type:
  id:
  description:
  label:
  best_for:
  buyer_tension:
  required_product_evidence:
  visual_structure:
  hook_logic:
  proof_logic:
  CTA_logic:
  risk:
  when_not_to_use:
```

## Creative Types

```yaml
creative_types:
  - id: desire-scene
    description: 先制造一个买家想进入的场景，再让商品成为这个场景里的可拥有对象。
    label: Desire Scene
    best_for: Shopify PDP 视频、Meta/TikTok DTC 广告、品牌短片、视觉吸引力强或场景感强的商品
    buyer_tension: 用户还没进入理性比较，先需要被场景和拥有感吸引
    required_product_evidence: 商品外观、使用关系或包装必须可见，不能只拍氛围
    visual_structure: thumb-stopping scene -> buyer desire -> product enters as object -> natural proof -> brand memory
    hook_logic: 用强视觉场景或反常构图先抓注意力
    proof_logic: 把材质、尺寸、使用关系藏进自然动作，不做教程
    CTA_logic: 引导用户想拥有这个场景里的商品
    risk: 容易变成空氛围或商品太小
    when_not_to_use: 商品没有可见外观证据，或用户明确要求功能说明

  - id: identity-upgrade
    description: 让商品帮助买家靠近一种更理想的身份、状态或审美选择。
    label: Identity Upgrade
    best_for: 穿搭、个护、家居、数码配件、礼品、办公、运动和生活方式商品
    buyer_tension: 用户想让自己看起来更专业、更精致、更有准备或更像某种生活方式
    required_product_evidence: 商品必须能自然挂靠到人物状态、空间状态或使用身份
    visual_structure: identity cue -> tension gap -> product as upgrade signal -> lived-in proof -> confident end frame
    hook_logic: 用人物状态、空间状态或选择瞬间引出身份欲望
    proof_logic: 用真实携带、摆放、佩戴、触摸或使用动作证明商品属于这个身份
    CTA_logic: 引导用户选择这件能代表自己的商品
    risk: 容易让人物和身份感抢走商品
    when_not_to_use: 商品没有身份表达空间，或需要严格规格说明

  - id: ritual-moment
    description: 把商品放进一个可重复的日常仪式，让买家想把它加入自己的生活。
    label: Ritual Moment
    best_for: 护理、香氛、饮品、食品、家居、睡眠、厨房、办公和宠物日常商品
    buyer_tension: 用户想要一个更舒服、更有秩序、更像自己的日常时刻
    required_product_evidence: 商品参与的手部动作、放置关系或使用时机必须可见
    visual_structure: sensory hook -> ritual setup -> product touch/action -> small proof -> memory end frame
    hook_logic: 用触感、声音、光线、手部动作或环境细节开场
    proof_logic: 在仪式动作里自然显示商品细节、质感或使用关系
    CTA_logic: 引导用户把商品加入自己的 routine
    risk: 容易变成慢生活空镜
    when_not_to_use: 商品没有自然日常动作或场景

  - id: occasion-trigger
    description: 用一个强购买时机触发行动，如旅行、通勤、开学、健身、搬家、节日或换季。
    label: Occasion Trigger
    best_for: 季节性、礼品、旅行、运动、收纳、服饰、户外、办公室和家庭场景商品
    buyer_tension: 用户在某个时刻突然需要准备、升级、替换或送礼
    required_product_evidence: 商品必须能真实出现在该 occasion 的动作或空间里
    visual_structure: occasion cue -> urgent desire/tension -> product enters -> proof in action -> buy-now memory
    hook_logic: 用场景身份或时间压力让用户立刻识别“我也需要”
    proof_logic: 用收纳、携带、摆放、穿戴、送出或打开动作证明商品适合这个时机
    CTA_logic: 引导用户在这个 occasion 前完成购买
    risk: 容易过度节日化或编造场景
    when_not_to_use: 商品和 occasion 没有真实关系

  - id: gift-emotion
    description: 把商品作为礼物情绪的载体，强调被选择、被打开、被记住的瞬间。
    label: Gift Emotion
    best_for: 礼品、定制、套装、包装好看、家居、香氛、饰品、母婴和节日商品
    buyer_tension: 买家想送出一个不敷衍、有质感、能被记住的礼物
    required_product_evidence: 包装、定制、外观、套装内容或递送动作必须真实可见
    visual_structure: gift tension -> tactile packaging/product reveal -> emotional handoff -> product detail proof -> remembered end frame
    hook_logic: 用送礼压力、打开瞬间或触感细节抓注意力
    proof_logic: 用包装层次、商品细节、定制点或手部交接证明礼物价值
    CTA_logic: 引导用户把商品选作礼物
    risk: 容易编造祝福文字、假品牌卡或假收礼反应
    when_not_to_use: 商品没有礼品属性或包装证据

  - id: lifestyle-proof
    description: 在真实生活动作中完成商品证明，让 proof 像生活片段而不是说明书。
    label: Lifestyle Proof
    best_for: 需要证明但不适合硬演示的 DTC 商品
    buyer_tension: 用户想确认商品真的适合自己的生活，但不想看 Amazon listing demo
    required_product_evidence: 商品使用关系、尺寸、材质或结果必须在自然动作里可见
    visual_structure: lifestyle hook -> buyer action -> product role visible -> hidden proof -> brand-memory frame
    hook_logic: 用生活状态或内容原生动作开场
    proof_logic: 把手部、空间、比例、材质、结果藏在自然动作里
    CTA_logic: 引导用户把商品放进自己的场景
    risk: 容易 proof 太弱或变成泛生活方式
    when_not_to_use: 商品必须被逐步教学才能理解

  - id: creator-native-hook
    description: 用平台原生创作者开头抓人，但主线仍然是购买欲望，不是教程讲解。
    label: Creator Native Hook
    best_for: TikTok/Reels/Shorts 风格广告、UGC-like DTC 素材、需要更强前 2 秒停留的商品
    buyer_tension: 用户在刷内容，不会先听产品说明
    required_product_evidence: 创作者动作、手部或场景必须让商品真实可读
    visual_structure: native interruption -> identity/occasion tension -> product reveal -> proof inside action -> CTA cue
    hook_logic: 用平台原生动作、反差画面、第一人称场景或一句情绪句抓注意力
    proof_logic: 用自然使用、手部接触或场景结果支持，不做 step-by-step instruction
    CTA_logic: 引导用户停下来看商品并点击购买
    risk: 容易变成泛 UGC 教程或口播过多
    when_not_to_use: 用户要求无人物品牌片，或商品不能被创作者自然使用

  - id: premium-product-memory
    description: 用高级品牌片语言让商品留下形状、材质、光线和拥有感记忆。
    label: Premium Product Memory
    best_for: 高客单、礼品、包装强、质感强、家居、科技、配件、发布感或品牌感商品
    buyer_tension: 用户需要先相信这个商品有质感和值得拥有
    required_product_evidence: 形状、材质、包装、logo/label 或结构细节必须清楚
    visual_structure: product-as-memory hook -> tactile detail -> desirable scene -> restrained proof -> iconic end frame
    hook_logic: 用商品外观、材质反光、尺度关系或慢速 reveal 建立记忆
    proof_logic: 用微距、接触阴影、真实表面和手部动作支撑质感
    CTA_logic: 引导用户记住商品并进入购买页
    risk: 容易太像奢侈品空镜，商品用途不清
    when_not_to_use: 商品外观普通且必须靠步骤解释才懂

  - id: problem-solution
    description: 用商品使用过程把一个具体问题转成解决状态。
    label: Problem Solution
    best_for: 商品能清楚解决一个买家问题
    buyer_tension: 用户遇到一个具体麻烦，但还没确认哪个产品能解决
    required_product_evidence: 商品使用方式或结果必须可见
    visual_structure: problem visible -> product enters -> use/proof -> resolved state
    hook_logic: 让用户立刻认出问题
    proof_logic: 用商品动作证明解决过程
    CTA_logic: 引导用户查看商品细节或选择合适版本
    risk: 容易夸大效果
    when_not_to_use: 商品无法证明具体解决结果

  - id: objection-proof
    description: 用细节、尺寸、材质或操作消除购买疑虑。
    label: Objection Proof
    best_for: 买家对质量、尺寸、适配、使用难度、真实性有疑虑
    buyer_tension: 用户想买但不放心
    required_product_evidence: 材质、结构、尺寸、对比、操作过程必须可见
    visual_structure: objection shown -> product detail -> proof action -> confidence frame
    hook_logic: 直接点出疑虑
    proof_logic: 用细节或动作消除疑虑
    CTA_logic: 引导用户确认规格、材质、细节或适配
    risk: 容易编造竞品缺陷
    when_not_to_use: 没有可见 proof asset

  - id: feature-to-benefit
    description: 把一个可见功能翻译成用户能理解的好处。
    label: Feature To Benefit
    best_for: 商品有明确功能或结构，但用户需要理解它的好处
    buyer_tension: 用户看到功能但不知道为什么重要
    required_product_evidence: 功能入口、结构、使用动作必须可见
    visual_structure: feature close-up -> use moment -> benefit visible -> hero frame
    hook_logic: 用一个具体功能开场
    proof_logic: 把功能和用户利益连接起来
    CTA_logic: 引导用户查看功能细节
    risk: 画面容易只讲功能不讲利益
    when_not_to_use: 商品功能不可见

  - id: mechanism-reveal
    description: 展示结构、材质或工作机制，让用户知道价值来源。
    label: Mechanism Reveal
    best_for: 商品价值来自结构、材质、工艺、设置方式或工作机制
    buyer_tension: 用户需要知道“为什么这个东西有用”
    required_product_evidence: 机制、材质、部件、操作细节必须可见
    visual_structure: curiosity detail -> mechanism reveal -> macro proof -> use result
    hook_logic: 用真实细节制造好奇
    proof_logic: 用近景、拆解感或动作展示机制
    CTA_logic: 引导用户查看详情或规格
    risk: 容易做成虚构拆解
    when_not_to_use: 无法看到机制或部件

  - id: comparison
    description: 用真实或中性对比帮助用户做选择。
    label: Comparison
    best_for: 用户在多个方案、尺寸、颜色、旧方式之间做选择
    buyer_tension: 用户不知道选哪个
    required_product_evidence: 对比对象必须真实或中性，不编造竞品事实
    visual_structure: old/other option -> product difference -> side-by-side proof -> decision frame
    hook_logic: 展示选择冲突
    proof_logic: 用同画面对比证明差异
    CTA_logic: 引导用户选择版本、尺寸、颜色或配置
    risk: 容易产生虚假竞品比较
    when_not_to_use: 没有真实对比依据

  - id: scale-proof
    description: 用尺寸、比例、贴合或实物参照证明商品是否适配。
    label: Scale Proof
    best_for: 买家担心尺寸、容量、比例、贴合、收纳或安装适配
    buyer_tension: 用户想买但不确定大小是否适合自己的使用场景
    required_product_evidence: 尺寸、比例参照、佩戴/放置/安装关系必须可见
    visual_structure: scale concern -> neutral reference -> fit/placement proof -> confident choice
    hook_logic: 直接展示尺寸疑问或适配对象
    proof_logic: 用手、身体、桌面、设备、容器或同框参照证明比例
    CTA_logic: 引导用户确认尺寸、规格、容量或适配版本
    risk: 容易生成错误比例或虚假适配
    when_not_to_use: 没有尺寸、规格、适配对象或比例参照证据

  - id: routine-integration
    description: 展示商品如何自然进入日常流程。
    label: Routine Integration
    best_for: 商品适合进入日常流程
    buyer_tension: 用户想知道这个东西是否真的用得上
    required_product_evidence: 使用场景和动作必须自然
    visual_structure: routine start -> product enters -> action completes -> routine improved
    hook_logic: 用熟悉的日常瞬间开场
    proof_logic: 用流程动作证明商品自然融入
    CTA_logic: 引导用户把商品放进自己的日常
    risk: 容易变成泛生活方式广告
    when_not_to_use: 商品不依赖日常使用语境

  - id: customization-choice
    description: 展示用户如何选择、配置或定制商品。
    label: Customization Choice
    best_for: 定制、颜色、尺寸、套装、模块、配置类商品
    buyer_tension: 用户想确认“能不能选到适合我的”
    required_product_evidence: 选项、配置、定制入口必须可见
    visual_structure: choice problem -> options shown -> configuration action -> final selected state
    hook_logic: 展示选择问题或定制入口
    proof_logic: 用选项变化证明可配置
    CTA_logic: 引导用户选择款式、上传图案或确认配置
    risk: 容易生成证据外假图案
    when_not_to_use: 商品没有真实选项或配置

  - id: trust-proof
    description: 用可见细节和处理动作建立质量信任。
    label: Trust Proof
    best_for: 用户担心质量、真实感、材质、耐用、包装
    buyer_tension: 用户怕踩雷
    required_product_evidence: 材质、结构、包装、细节、评论或规格必须可见
    visual_structure: doubt cue -> detail proof -> handling proof -> confident end frame
    hook_logic: 直接进入可信细节
    proof_logic: 用微距、手部接触、真实阴影证明质感
    CTA_logic: 引导用户查看细节或评价
    risk: 容易虚构认证、评价或平台 UI
    when_not_to_use: 没有可信证据

  - id: sensory-proof
    description: 用微距、触摸或光线呈现材质和质感。
    label: Sensory Proof
    best_for: 材质、触感、光泽、声音、质地、食物、液体、面料
    buyer_tension: 用户需要感知质感
    required_product_evidence: 质地或材料必须可见
    visual_structure: macro sensory hook -> touch/action -> detail proof -> memory frame
    hook_logic: 用细节近景抓注意力
    proof_logic: 用手部、光线、微距、动作让质感可见
    CTA_logic: 引导用户查看材质或细节
    risk: 容易 AI 塑料感
    when_not_to_use: 商品没有明显感官属性

  - id: product-macro
    description: 用商品本身的细节、结构和包装完成吸引与证明。
    label: Product Macro
    best_for: 商品本身外观、结构、包装、工艺足够强
    buyer_tension: 用户需要仔细检查商品
    required_product_evidence: 商品细节必须清楚
    visual_structure: hero macro -> detail rotation -> proof detail -> clean product end frame
    hook_logic: 直接用商品细节开场
    proof_logic: 用微距和慢镜头证明细节
    CTA_logic: 引导查看商品页细节
    risk: 容易缺少购买场景
    when_not_to_use: 商品外观普通且需要真人使用才能理解

  - id: ugc-demo
    description: 用真人或手部演示解释商品使用方法。
    label: UGC Demo
    best_for: 商品需要真人解释或手部演示
    buyer_tension: 用户想看真实使用
    required_product_evidence: 商品必须能被真人自然使用
    visual_structure: creator/hand hook -> demo -> proof -> personal CTA
    hook_logic: 真人或手部直接进入
    proof_logic: 用真实动作证明使用方法
    CTA_logic: 引导用户尝试或查看链接
    risk: 商品证明容易变弱
    when_not_to_use: 商品不需要人解释

  - id: founder-demo
    description: 用品牌或创始人理由连接产品设计细节和信任。
    label: Founder Demo
    best_for: 商品需要品牌解释、研发原因、设计理由
    buyer_tension: 用户想知道为什么这个产品存在
    required_product_evidence: 商品和解释必须同框
    visual_structure: founder reason -> product design detail -> use proof -> trust CTA
    hook_logic: 用一句设计理由开场
    proof_logic: 用商品细节支持创始人说法
    CTA_logic: 引导用户了解品牌或产品细节
    risk: 容易变成空泛品牌故事
    when_not_to_use: 没有品牌/创始人素材
```

## Buyer Situation Router

Use this router after Product Truth Card creation and DTC Desire Angle, before selecting the main `creative_type`.

```yaml
default_rule:
  priority: DTC-first
  meaning: 先选择欲望、身份、场景、仪式、礼物、品牌记忆或平台原生钩子，再把商品 proof 嵌入自然动作。
  avoid_by_default:
    - Amazon listing demo
    - instruction manual tone
    - feature checklist
    - problem explanation
    - feature list
    - step-by-step use

buyer_situation_router:
  - situation: 默认 DTC 商品广告、Shopify PDP 视频、Meta/TikTok paid social 或品牌短片
    primary_creative_type: desire-scene
    secondary_creative_type: lifestyle-proof
    use_when: 用户没有明确要求 Amazon listing、how-to、产品说明或功能演示

  - situation: 买家想靠近某种生活状态、审美或身份
    primary_creative_type: identity-upgrade
    secondary_creative_type: desire-scene
    use_when: 商品能表达人物状态、空间状态、穿搭/办公/运动/家居身份

  - situation: 商品适合日常重复使用或情绪化 routine
    primary_creative_type: ritual-moment
    secondary_creative_type: lifestyle-proof
    use_when: 护理、饮品、食品、香氛、睡眠、厨房、办公、家居或宠物日常

  - situation: 有强购买时机
    primary_creative_type: occasion-trigger
    secondary_creative_type: desire-scene
    use_when: 旅行、通勤、健身、开学、搬家、节日、换季、婚礼或生日等 occasion 触发购买

  - situation: 商品有礼物属性、定制属性或包装记忆点
    primary_creative_type: gift-emotion
    secondary_creative_type: premium-product-memory
    use_when: 买家在选择送礼、纪念日、节日、定制或更有质感的礼物

  - situation: 商品需要 proof 但不能像说明书
    primary_creative_type: lifestyle-proof
    secondary_creative_type: desire-scene
    use_when: 商品确实需要展示材质、尺寸、使用关系或结果，但默认要藏进自然生活动作

  - situation: 平台原生短视频，需要前 2 秒强停留
    primary_creative_type: creator-native-hook
    secondary_creative_type: lifestyle-proof
    use_when: TikTok/Reels/Shorts 风格广告，用户不是来学习产品说明

  - situation: 商品外观、包装、材质或品牌感强
    primary_creative_type: premium-product-memory
    secondary_creative_type: sensory-proof
    use_when: 质感、包装、形状、材质、logo/label 或慢速 reveal 是购买记忆

  - situation: 商品有定制或选项，但输出仍是 DTC 广告
    primary_creative_type: customization-choice
    secondary_creative_type: gift-emotion
    use_when: 颜色、尺寸、套装、模块、配置、上传图案或个性化入口必须被看见

proof_first_exception_gate:
  applies_only_when_user_explicitly_asks_for:
    - Amazon listing
    - how-to
    - 产品说明
    - 功能演示
    - 使用方法
    - 机制解释
    - 尺寸适配证明
  allowed_primary_creative_types:
    - ugc-demo
    - feature-to-benefit
    - mechanism-reveal
    - scale-proof
```

## Selection Rules

- Select by `dtc_desire_angle`, buyer tension, and available Product Truth Card evidence, not by style words alone.
- If intent is ambiguous, choose one of the DTC-first types: `desire-scene`, `identity-upgrade`, `ritual-moment`, `occasion-trigger`, `gift-emotion`, `lifestyle-proof`, `creator-native-hook`, or `premium-product-memory`.
- Do not select `ugc-demo`, `feature-to-benefit`, `mechanism-reveal`, or `scale-proof` as the primary type unless the user explicitly asks for Amazon listing, how-to, product explanation, functional demonstration, mechanism explanation, or size/fit proof.
- `customization-choice` requires real options, configuration, or customization evidence.
- `founder-demo` requires brand/founder context; do not invent it.
- `comparison` requires a fair neutral comparison or user-provided basis.
- `scale-proof` requires real size, fit, capacity, placement, or compatibility evidence.
- `sensory-proof` and `product-macro` need strong visual detail.
- Function proof must appear inside emotion, identity, occasion, ritual, gift, lifestyle, creator-native, or brand-memory structure.
- If the product is already highly constrained by Product Truth Card, choose the lowest-risk DTC-first creative type that still gives a reason to watch and buy.
- Never make the default script an Amazon listing demo, instruction manual tone, feature checklist, problem explanation, feature list, or step-by-step use.

## Supporting Menus

Hook tactics:

- visual interruption
- identity cue
- occasion cue
- sensory interruption
- object desire reveal
- native creator interruption
- gift opening moment
- brand memory reveal
- curiosity gap
- micro proof inside action
- detail macro
- choice reveal
- ritual interruption

Desire levers:

- want to own the scene
- want to look prepared
- want to upgrade identity
- want to give a better gift
- want to make the routine feel better
- want to be ready for an occasion
- want to remember the product shape/material
- want to click before the explanation

Proof mechanics:

- material macro
- hand pressure / touch
- natural use action
- scale / fit check
- compatibility check
- configuration reveal
- package contents
- visible result
- side-by-side comparison
- expert handling
- routine completion
- proof hidden in lifestyle action

CTA patterns:

- shop the moment
- make it yours
- choose the one that fits
- gift it now
- add it to the routine
- be ready for the occasion
- remember this product
- choose your option
- upload your design
- shop the set
- confirm your fit
- build your kit
