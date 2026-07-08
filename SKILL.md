---
name: jingqiu-DTC
description: >
  当用户要把 Amazon、Shopify、TikTok Shop、商品图、商品截图、ASIN、SKU brief、商品短描述或用户提供的参考广告，转成 SKU 级 DTC 商品创意故事版、品牌片视觉规则、5 格 16:9 横屏故事版图片、英文 15 秒或 30 秒视频脚本时使用。必须先锁定 Product Truth Card，再输出 DTC Creative Reference Pack 和 Brand Film Look Pack，最后生成或记录故事版交付物、run.json、source_records.json 和本地验证结果。适用于 StoreClaw 商品内容工作流、Shopify PDP 视频、Amazon listing demo、paid social 创意测试和定制商品故事版。
---

# DTC 商品创意故事版 Skill

## 目标

把一个真实 SKU 的商品证据转成可执行的 DTC 商品创意故事版交付物。

这个 Skill 不是普通生图提示词、不是单纯视频脚本、不是竞品复刻工具。它只负责一次 SKU 级内容生成流程：

```text
商品证据
-> Product Truth Card
-> 合规来源记录
-> 广告参考拆解
-> DTC Creative Reference Pack
-> Brand Film Look Pack
-> 5 格 16:9 横屏故事版图片
-> 英文 15 秒或 30 秒视频脚本
-> 本地验证
```

最终用户可见输出只保留三段：

```markdown
## 1. 产品图

## 2. 故事版

## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` 必须嵌入或链接实际故事版图片。shot list、prompt、table、strategy 只能作为中间元数据，不能替代故事版图片。

## 结构原则

按 Skill 格式保持职责清楚：

| 位置 | 责任 | 中文说明 |
|---|---|---|
| `SKILL.md` | 硬路由、门控、流程、输出合同 | 只放另一个模型必须遵守的执行规则 |
| `references/` | 详细资料库和 schema | 创意类型、场景、动作、人物、镜头、品牌片模式、合规、QA 等长内容放这里 |
| `scripts/` | 确定性检查 | 本地结构验证放脚本，不在正文里重复实现逻辑 |
| `assets/` | 输出模板或图示 | 只放被交付物复用的素材 |

不要在 `SKILL.md` 里重复粘贴 reference 的完整库表、完整 schema 或研究报告。需要细节时按阶段读取对应文件。

## 执行合同

每次运行都按生产交付处理，不按建议稿处理。

必须做到：

1. 创建 Product Truth Card。
2. 再记录来源和合规状态。
3. 再拆解参考结构。
4. 再运行 DTC Creative Director。
5. 再创建 DTC Creative Reference Pack。
6. 再运行 Brand Film Look Director。
7. 再创建 Brand Film Look Pack。
8. 再让 Storyboard Design Expert 生成故事版和英文脚本。
9. 有本地文件权限时保存 `run.json`、`source_records.json`、`contact_sheet.png`、`panels/*.png`。
10. 当前环境不能生成或保存图片时，在 `run.json` 记录 `blocked_artifacts`，不能假装完成。
11. 最终回复保持三段输出，不默认暴露内部 JSON、完整 pack 或来源记录。

## 按需读取资料库

只在对应阶段读取对应 reference。

| 阶段 | 必读文件 | 中文说明 |
|---|---|---|
| 商品事实锁 | `references/category-adapters.md` | 按商品类别补充必须锁定的事实、买家事件、proof beat 和禁止漂移 |
| 来源采集 | `references/live-crawl-strategy.md`、`references/source-compliance-policy.md` | 规划合规来源，记录授权、失败和 fallback，不默认硬爬 |
| 参考拆解 | `references/ad-reference-analysis-schema.md` | 把参考广告拆成可借鉴结构，而不是复制素材 |
| 创意导演 | `references/dtc-creative-pattern-library.md`、`references/dtc-scene-library.md`、`references/dtc-motion-library.md`、`references/dtc-model-library.md`、`references/camera-language-library.md`、`references/brand-film-mode-library.md`、`references/dtc-director-reference-pack-schema.md` | 选择买家说服逻辑、场景、动作、人物、镜头、品牌片模式和创意执行包结构 |
| 品牌片视觉导演 | `references/brand-film-look-director.md`、`references/brand-film-mode-library.md`、`references/cinematic-grammar-rules.md`、`references/brand-film-storyboard-qa.md` | 把高级感、品牌片、cinematic、TVC 翻译成镜头、光线、材质、节奏和失败规则 |
| 故事版生成 | `references/storyboard-video-keyframe-rules.md`、`references/brand-film-storyboard-qa.md` | 约束 5 格 16:9 keyframe、end frame、脚本绑定和 QA |
| 本地验证 | `scripts/validate_storyboard.py` | 检查 run/source records、contact sheet、5 张 16:9 panel 和字段完整性 |

## 主流程

按顺序执行，不能跳步：

```text
1. Product Truth Lock
2. Live DTC Ad Reference Collection
3. Ad Reference Decomposition
4. DTC Creative Director
5. DTC Creative Reference Pack
6. Brand Film Look Director
7. Brand Film Look Pack
8. Storyboard Design Expert
9. Horizontal 5-Panel Storyboard Image Generation
10. English Video Demo Script
11. Delivery Validation
```

### 1. Product Truth Lock

先创建 Product Truth Card。它是商品事实锁，负责防止 SKU 在后续创意、画面和脚本里漂移。

必须记录这些核心字段：

- `source_evidence`：商品页、商品图、截图、ASIN、SKU brief 或用户资产。
- `visual_facts`：形状、颜色、材质、纹理、包装、logo、label、可见部件、尺寸比例。
- `product_behavior`：谁用、在哪里用、怎么用、需要什么动作。
- `proof_assets`：可见细节、结果、机制或对比证据。
- `allowed_claims` / `unsupported_claims`：区分可写和不可写的表达。
- `locked_terms`：必须锁定的商品关键词。
- `forbid_mutations`：禁止发生的商品漂移。
- `evidence_conflicts`：证据冲突记录。

商品证据不足时，停止最终故事版生成；可以输出 rough concept，但必须标明不是最终商品故事版。

### 2. Live DTC Ad Reference Collection

创建 `source_records.json`，记录所有来源尝试。

公开来源保存 URL、摘要、允许截图或关键帧、结构化拆解、失败原因和 fallback。

原视频、完整广告文件、品牌资产和私域素材必须是 `authorized` 或 `user_provided` 来源。

禁止：

- 默认硬爬 TikTok、Instagram、Amazon、Meta 页面。
- 复制竞品素材、logo、包装、人物、文案。
- 把抓取失败写成已采集成功。

### 3. Ad Reference Decomposition

把每条选中参考拆成 `ad_reference`。

只借鉴：

- hook 结构。
- 买家问题表达方式。
- 场景和动作关系。
- 镜头功能。
- 节奏结构。
- proof 出现方式。

不借鉴：

- 竞品具体素材。
- 竞品包装和品牌识别。
- 竞品模特或广告原文。
- 没有证据支持的对比结论。

### 4. DTC Creative Director

DTC Creative Director 决定“这个商品用什么购买逻辑被证明”。它不生成最终图片，不写最终脚本。

固定选择顺序：

```text
Step 1: 选择 creative_type
Step 2: 选择 scene_ref
Step 3: 选择 motion_chain
Step 4: 选择 model_ref
Step 5: 选择 camera_plan
Step 6: 选择 brand_film_mode
Step 7: 选择 script_pattern
Step 8: 选择 picture_fragment_logic
Step 9: 选择 end_frame
Step 10: 输出 DTC Creative Reference Pack
```

关键边界：

- `creative_type` 只能有一个主类型。
- `scene_ref` 必须能自然容纳商品。
- `motion_chain` 必须能形成 `start_state -> action -> end_state`。
- `model_ref` 不能让人物抢商品。
- `camera_plan` 必须服务 hook、proof、use 或 CTA，不能只服务风格。
- `brand_film_mode` 只能作为内部品牌片语言，最终输出不能暴露导演名或电影名。
- `picture_fragment_logic` 决定每个 panel 的任务，不允许固定第 3 格或第 5 格模板。

### 5. DTC Creative Reference Pack

创建内部创意执行包。Storyboard Design Expert 只能消费这个包，不能重新选择创意方向。

必须包含：

```text
product_truth_lock
creative_type
selected_ad_references
scene_selection
motion_selection
model_selection
camera_selection
brand_film_mode
script_pattern
picture_fragment_logic
end_frame
rejected_references
adaptation_reason
```

每个被选中的 library item 必须保留中文 `description`，说明这个选项干什么。

### 6. Brand Film Look Director

Brand Film Look Director 把“高级感、品牌片、cinematic、TVC、大牌感”翻译成可执行视觉规则。它不能重选商品事实，也不能重选创意方向。

不能只写：

```text
cinematic
premium
luxury
high-end
dramatic lighting
```

必须拆成：

```text
光源
镜头距离
焦段感觉
机位
运镜
调色
材质
阴影
节奏
构图
商品占比
人物出镜程度
真实接触阴影
收尾镜头状态
失败规则
```

执行边界：

- 在 DTC Creative Reference Pack 之后运行。
- 在 Storyboard Design Expert 之前运行。
- 不能覆盖 Product Truth Card。
- 不能把风格放在 SKU truth 前面。
- 不能在最终用户输出暴露导演名、电影名或“像某导演”。

### 7. Brand Film Look Pack

创建内部品牌片视觉执行包。

必须包含：

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

完成标准：

- `brand_film_mode` 只能选一个主模式。
- `brand_world_lock` 保持同一商品、同一视觉世界、同一光线方向、同一材质逻辑。
- `cinematic_grammar` 把 mood 翻译成 camera、light、material、motion、color、rhythm、composition。
- `shot_function_map` 跟随 `picture_fragment_logic`，不能套固定 panel 模板。
- `signature_shot` 必须服务商品证明。
- `end_frame_rule` 必须增强购买信心，不能编造 claim。
- `failure_rules` 必须具体到能拒绝弱生成结果。

### 8. Storyboard Design Expert

Storyboard Design Expert 只执行，不重新做策略。

允许输入：

```text
Product Truth Card
DTC Creative Reference Pack
Brand Film Look Pack
```

禁止输入：

```text
临时新创意
未记录来源的竞品素材
没有证据的 claims
绕过 Product Truth Card 的风格词
固定第 3 格或第 5 格模板
```

故事版必须满足：

- 一张实际故事版图片。
- 5 个 16:9 横屏 keyframe。
- 每个 panel 都是 video-ready keyframe。
- 每个 panel 的任务来自 `picture_fragment_logic`。
- 同一商品、同一拍摄世界、同一光线方向、同一材质逻辑。
- 商品必须可读，不能被人物、背景或道具抢走。
- 有真实接触阴影，不能漂浮。
- 不出现假 UI、假评论、假 badge、假认证、假 before/after。

默认节奏可以参考：

```text
quiet hook
brand world / buyer context
product proof moment
motion or use completion
restrained hero frame
```

这是节奏建议，不是固定 panel 编号规则。

### 9. Horizontal 5-Panel Storyboard Image Generation

生成或组装一张 5 格 16:9 横屏故事版图片。

有本地文件权限时保存：

```text
contact_sheet.png
panels/panel_01.png
panels/panel_02.png
panels/panel_03.png
panels/panel_04.png
panels/panel_05.png
```

图片生成提示必须包含：

```text
1. product_truth_lock
2. creative_type
3. selected_ad_reference logic
4. scene_ref
5. model_ref
6. motion_chain
7. camera_plan
8. brand_film_mode
9. brand_film_look_pack
10. brand_world_lock
11. cinematic_grammar
12. shot_function_map
13. material_and_light_rules
14. picture_fragment_logic
15. end_frame
16. five-panel picture_fragment_logic
17. horizontal 16:9 contact sheet constraint
18. same shoot / same product / same lighting continuity
19. real physical contact shadows
20. no fake UI / no fake claims / no fake reviews
```

完成标准：`contact_sheet.png` 或嵌入图片存在；有本地文件权限时 5 张 panel 文件存在；每个 panel 都是 video-ready keyframe。

### 10. English Video Demo Script

默认生成 15 秒脚本。用户明确要求时生成 30 秒脚本。

脚本表结构：

```markdown
| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

要求：

- `Camera / Motion` 必须匹配 `camera_selection` 和 `motion_selection`。
- `屏幕字幕` 和 `旁白 / 口播` 的内容使用自然英文。
- `Reference Logic` 说明借鉴了什么结构，但不写具体品牌名。
- 不写 unsupported claims。
- 不写无法从商品证据推导的功效、认证、评价或平台 UI。

### 11. Delivery Validation

有本地文件时运行：

```bash
python3 scripts/validate_storyboard.py /path/to/output_dir
```

验证通过后再报告完成。验证失败时记录失败原因，不要把失败结果说成完成。

## 本地产物

每次本地执行保存：

```text
run.json
source_records.json
contact_sheet.png
panels/*.png
```

`run.json` 至少包含：

```text
product_truth_card
category_adapter
dtc_director_input
dtc_creative_reference_pack
brand_film_look_pack
output_paths
blocked_artifacts
source_url
locked_terms
forbid_mutations
creative_type
scene_ref
motion_chain
model_ref
camera_plan
brand_film_mode
end_frame
panel_count
panel_aspect_ratio
contact_sheet
```

`source_records.json` 记录所有来源尝试、成功来源、失败来源和 fallback。

## validator 范围

`scripts/validate_storyboard.py` 检查工程结构：

- `run.json` 存在且是 JSON object。
- `source_records.json` 存在且是 JSON object。
- `source_url` 和 `locked_terms` 存在。
- `creative_type`、`scene_ref`、`motion_chain`、`model_ref`、`camera_plan` 存在。
- `brand_film_mode` 存在且字段完整。
- `brand_film_look_pack` 存在且字段完整。
- `end_frame` 存在且字段完整。
- contact sheet 存在且可读取。
- 5 张 panel 图片存在且都是 16:9。
- `brand_film_mode` 和 `brand_film_look_pack` 不暴露导演名或电影名。

validator 不能证明视觉真相。以下内容需要人工复核或多模态视觉 QA：

- 图片里是否真的是同一商品。
- logo 或 label 是否视觉一致。
- 材质是否真实。
- 人物是否抢商品。
- 商品 proof 是否真的成立。
- 画面是否有 AI 塑料感。
- 接触阴影是否物理正确。

## 硬规则

1. 没有 Product Truth Card，不生成最终商品故事版。
2. 没有 DTC Creative Reference Pack，不生成故事版图片。
3. 没有 Brand Film Look Pack，不生成故事版图片。
4. Storyboard Design Expert 不能重新选择 `creative_type`。
5. 只能选择一个主 `creative_type`。
6. 不能选择商品无法自然出现的场景。
7. 不能选择无法形成 `start_state -> action -> end_state` 的动作。
8. 不能选择会隐藏商品或削弱商品证明的人物策略。
9. 镜头必须服务 hook、proof、use 或 CTA，不能只服务风格。
10. 不能固定第 3 格或第 5 格承担某个功能。
11. 每个 panel 的任务来自 `picture_fragment_logic`。
12. 每个 panel 都必须是 video-ready keyframe。
13. 英文脚本的 `Camera / Motion` 必须匹配 `camera_selection` 和 `motion_selection`。
14. 最终用户输出不能暴露导演名、电影名或“像某导演”。
15. 不能把 prompt 当成交付物。
16. 不能默认硬爬平台或复制竞品素材。
17. 不能声称 validator 已经自动证明视觉商品一致性。

## 禁止保留的旧规则

不要写进 Skill：

```text
固定 panel_3
固定 panel_5
第 3 格必须是最强商品证明
第 5 格必须是 hero
contact sheet 必须横向单行
FYPro / image-to-video 前置故事版承诺
自动抓取全网竞品广告
自动复刻竞品视频
没有商品证据时生成最终商品故事版
完全自动判断视觉商品一致性
visual-truth-review.md
references/visual-truth-review.md
```

## 能力边界

这个 Skill 可以稳定承担：

- 商品事实锁定。
- 合规来源记录。
- 参考结构拆解。
- 创意方向选择。
- 场景、动作、人物、镜头选择。
- 品牌片视觉规则生成。
- 5 格故事版结构规划。
- 英文视频脚本。
- 本地交付结构验证。

这个 Skill 不能替代：

- 商品证据本身。
- 平台授权数据源。
- 图像生成模型质量控制。
- 人工或多模态视觉 QA。
- 批量 SKU 调度系统。
- 自动视频成片系统。

## 最终输出格式

最终回复使用这个形状：

```markdown
## 1. 产品图

![产品图](...)

## 2. 故事版

创意大片方向：...

同一拍摄世界锁：...

![5 格 16:9 横屏故事版](...)

## 3. 15 秒或者 30 秒视频脚本文字

| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

除非用户明确要求，不要在最终回复里展开完整 Product Truth Card、完整 DTC Creative Reference Pack、完整 Brand Film Look Pack、source records、run.json 或验证日志。
