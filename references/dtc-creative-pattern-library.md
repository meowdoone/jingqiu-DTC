# DTC Creative Type Library

## Purpose

`creative_type` is the main DTC creative logic selected by `DTC Creative Director`.

Choose exactly one main `creative_type`. Do not blend multiple main types unless one is clearly secondary in the Reference Pack.

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

Use this router after Product Truth Card creation and before selecting the main `creative_type`.

```yaml
buyer_situation_router:
  - situation: 商品需要解释怎么用
    primary_creative_type: ugc-demo
    secondary_creative_type: routine-integration
    use_when: 使用方法、操作顺序、上手方式或真实使用语境需要被看见

  - situation: 买家担心质量
    primary_creative_type: trust-proof
    secondary_creative_type: mechanism-reveal
    use_when: 材质、结构、包装、耐用感、工艺或可信细节是购买阻力

  - situation: 买家担心尺寸适配
    primary_creative_type: comparison
    secondary_creative_type: scale-proof
    use_when: 尺寸、容量、比例、贴合、佩戴、安装或收纳适配需要被证明

  - situation: 商品有定制或选项
    primary_creative_type: customization-choice
    secondary_creative_type: null
    use_when: 颜色、尺寸、套装、模块、配置、上传图案或个性化入口必须被看见

  - situation: 商品材质、细节强
    primary_creative_type: sensory-proof
    secondary_creative_type: product-macro
    use_when: 质地、纹理、光泽、触感、结构、包装或工艺是主要吸引点

  - situation: 商品使用步骤重要
    primary_creative_type: feature-to-benefit
    secondary_creative_type: mechanism-reveal
    use_when: 用户需要理解功能入口、步骤顺序、机制细节和最终好处
```

## Selection Rules

- Select by buyer tension and available proof, not by desired style.
- `customization-choice` requires real options, configuration, or customization evidence.
- `founder-demo` requires brand/founder context; do not invent it.
- `comparison` requires a fair neutral comparison or user-provided basis.
- `scale-proof` requires real size, fit, capacity, placement, or compatibility evidence.
- `sensory-proof` and `product-macro` need strong visual detail.
- If the product is already highly constrained by Product Truth Card, choose the lowest-risk creative type that still gives a reason to watch.

## Supporting Menus

Hook tactics:

- visual interruption
- problem recognition
- direct question
- specific claim
- curiosity gap
- before-after contrast
- micro demo
- detail macro
- choice reveal
- mistake callout
- comparison open
- routine disruption

Proof mechanics:

- material macro
- hand pressure / touch
- use sequence
- scale / fit check
- compatibility check
- configuration reveal
- package contents
- visible result
- side-by-side comparison
- expert handling
- routine completion
- social proof frame

CTA patterns:

- check the details
- choose your option
- upload your design
- shop the set
- confirm your fit
- see how it works
- get the routine
- try it today
- build your kit
- compare the options
