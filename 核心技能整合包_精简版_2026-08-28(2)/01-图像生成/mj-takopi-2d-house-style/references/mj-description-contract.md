# Parameter-Free MJ Description Contract

## Contents

1. Final output rule
2. Input classification
3. Assembly order
4. House-style description blocks
5. Asset-specific schemas
6. Positive control language
7. Cultural locking
8. Controlled variants
9. Repair routing
10. Final audit

## 1. Final Output Rule

Return one continuous Chinese descriptive paragraph by default. The paragraph contains only drawable image facts and art-direction language.

The final paragraph contains:

- no Midjourney flags or settings;
- no aspect-ratio, version, stylize, chaos, quality, seed, style-reference, image-weight, or negative parameters;
- no `::` weighting syntax;
- no source title, artist, studio, director, franchise, or named-style phrase;
- no negative prompt list;
- no seconds, camera movement, transition, tail frame, A block, or video timeline;
- no invented exact typography unless the user supplies the text and explicitly requires it.

Static viewpoint, framing, depth, and perspective descriptions are allowed because they describe one image.

## 2. Input Classification

Assign every reference one role before writing:

- `identity`: face, hair, body, clothing, or prop must stay stable;
- `style evidence`: line, shape, cel, color, texture, and expression rendering only;
- `composition`: framing, perspective, overlap, depth, or subject placement only;
- `palette`: color roles and light relation only;
- `environment`: architecture, landscape, furniture, props, and material density;
- `edit target`: preserve the supplied image except for the requested change;
- `culture`: location, period, clothing, furniture, signage system, and social details.

State conflicts internally and apply:

```text
current user locks
-> edit target / identity
-> approved composition and moment
-> house-style baseline
-> culture and environment evidence
-> lane-specific variation
```

## 3. Assembly Order

Build the paragraph in this order:

```text
asset type and frozen moment
-> exact subject count and identity
-> cultural environment and spatial layout
-> framing and visual hierarchy
-> pose, weight, gaze, expression, hands, and prop ownership
-> character proportions, face, eyes, mouth, hair, and clothing
-> linework hierarchy
-> cel shading and motivated light
-> palette roles
-> background paint and material details
-> paper/capture finish
-> continuity locks expressed as visible current facts
```

Do not begin with a named style. Lead with the image being made, then make the drawing system explicit.

## 4. House-Style Description Blocks

Use these as modular language, not as mandatory verbatim boilerplate.

### Baseline drawing block

```text
手绘二维赛璐璐动画插画，人物采用柔软年轻的轮廓、略大的头部、窄肩与纤细四肢，脸型上宽下短、下颌圆钝，五官留白充足，眼睛以大面积完整虹膜和克制湿润高光作为识别中心，鼻子只用极短笔触，嘴形简洁而富有节奏，头发先形成大块清晰剪影，再用少量不规则发束和边缘碎发补充方向，深棕灰细线具有轻微手绘粗细变化，人物表面保持哑光平涂，以一组克制的赛璐璐阴影塑造头发、下颌、衣袖和接触关系，脸颊与眼下只保留局部短线排线，角色色块干净，背景绘制与材质信息更丰富，画面覆盖极轻的纸张颗粒和传统动画摄影质感
```

### Ordinary daylight block

```text
自然天空或窗户形成宽阔柔和主光，皮肤中间调明亮清楚，阴影偏冷灰绿或蓝灰，树叶、墙面和地面提供低强度反射色，世界保持普通而明亮，人物情绪只通过局部发影、眼睑、手部和姿态发生变化
```

### Warm emotional block

```text
浅金、桃橙与暖奶油色光从侧面或后方进入，沿头发、脸颊、耳朵、颈部和衣领形成简洁暖色边缘，暗部保留中性灰褐分离，眼睛或嘴形成为唯一高强度表情中心，温暖光线仍服从真实接触、服装重量和空间材质
```

### Psychological-local block

```text
人物仍处在可读的普通环境中，压力集中在偏低的上眼睑、失焦视线、紧窄肩线、贴近身体的手臂、压住衣料或背带的手指，以及眼下和颈侧少量灰橄榄色排线，皮肤中间调保持苍白哑光，环境光色不随情绪整体变黑
```

### Painterly environment block

```text
环境以较人物更高的材质密度绘制，前景、中景、背景具有清楚遮挡和尺度变化，木材、纸张、布料、塑料、玻璃、金属、墙面磨损、地面缝隙与生活杂物按功能组成疏密不同的物件岛，远处轮廓和色块更柔，主体周围保留一块简洁明亮的空间作为视觉落点
```

### Simple mascot block

```text
一个高纯度珊瑚粉色的圆润小生物采用极简轮廓、点状眼睛与微小嘴形，表面是干净平涂，情绪由身体倾斜、压扁、抬起和短小肢体方向表达，它与人物和环境形成清楚的细节密度差和色相差
```

## 5. Asset-Specific Schemas

### 5.1 Character identity sheet

Include:

1. exact age and role;
2. full-body or three-quarter neutral stance;
3. body silhouette and head/shoulder relation;
4. face, eye, mouth, hair, and skin locks;
5. costume construction and flat-color blocks;
6. one hand/prop interaction;
7. clean line and cel-shadow sample;
8. simple organized background.

Keep dramatic lighting and dense environment outside the base identity sheet.

### 5.2 Expression sheet

Include a stable head, hair, clothing collar, and light baseline. Change one expression family per face: calm, open joy, watchful, social mask, suppressed hurt, exhausted, anger held, emotional peak. Describe eyelids, iris focus, mouth, cheek marks, brows, jaw, neck, and shoulder cue for each.

### 5.3 Ensemble key art

Include exact subject count, staggered heights, distinct gestures, gaze routes, props, overlaps, and silhouette separation. Use white, cream, or a simple graphic field when the line and personalities should dominate.

### 5.4 Relationship still

Describe one frozen social fact: shared paper, hands on knees, shoulder overlap, opposing profile gaze, one person leaning in while another remains quiet, or a mascot pressing against a cheek. Keep every body connected to support and space.

### 5.5 Scene concept or key frame

Include:

1. place, country/period, time, and weather;
2. foreground, subject zone, midground, and background;
3. ordinary functional objects and material clusters;
4. exact subject count and positions;
5. one frozen action consequence;
6. line/cel relation between characters and background;
7. motivated light and palette roles;
8. paper/capture finish.

### 5.6 Overhead lived-in room

Describe a near-vertical top view, room geometry, one light bedding/floor island, a readable body pose, object clusters arranged around daily activities, believable scale and orientation, muted material palette, and selective high-chroma props guiding the eye.

### 5.7 Psychological close-up

Describe crop, gaze target, eyelid weight, iris focus, mouth residue, hair crossing the face, cheek/under-eye hatching, one hand or material cue, localized shadow, and compressed environment. Preserve open skin midtones and matte cel color.

### 5.8 Culture-specific adaptation

Describe the exact regional world through architecture, clothing, furniture, school/work objects, domestic tools, transport, landscape, and writing system. Keep the same house face, line, cel, and texture rules.

## 6. Positive Control Language

Write the desired image state rather than a prohibition.

| Drift | Positive target language |
|---|---|
| glossy 3D face | matte pale skin, sparse facial planes, graphic one-step cel shadow, thin irregular contour |
| photoreal hair | broad flat hair masses, a few directional clumps, sparse edge wisps, low-contrast graphic highlight |
| vector-clean line | fine charcoal contour with tapered pressure changes and slight corner irregularity |
| generic pointed anime face | broad upper cranium, gently full cheeks, short soft jaw, tiny nose mark, compact mouth |
| gemstone eyes everywhere | large coherent iris, one main wet catchlight, restrained supporting reflection |
| random clothing wrinkles | folds concentrated at shoulder, elbow, waist compression, knee, strap, hand grip, and fabric weight |
| empty scene | three depth planes, functional ordinary objects, material clusters, one protected subject island |
| global dark sadness | ordinary daylight retained, local hair shadow, heavy eyelid, inward posture, sparse under-eye hatching |
| mascot blends into humans | simple high-chroma flat silhouette, dot eyes, tiny mouth, radically lower detail density |
| national setting drift | exact local architecture, clothing construction, furniture, daily objects, signage system, and landscape |

Omit undesired elements by fully specifying the desired subject scope and medium. Do not append a negative list.

## 7. Cultural Locking

For every project define:

```text
country and region
historical period or contemporary year range
urban/rural/social context
school, home, street, workplace, or fantasy institution type
clothing and uniform construction
furniture and floor/wall materials
daily tools, packaging, food, bags, stationery, and transport
writing system and whether exact text is required
weather, vegetation, and landscape
```

Use these facts to localize the image. Do not change eye size or face construction as a shortcut for nationality.

## 8. Controlled Variants

When the user asks for variants, change one layer at a time:

- composition: ensemble vs environmental dominance;
- emotional lane: ordinary vs psychological-local;
- finish: clean key art vs broadcast grain;
- light: ordinary daylight vs warm emotional side light;
- background density: simple graphic field vs lived-in material scene;
- viewpoint: normal relation vs overhead environment vs child-height foreground.

Keep identity, culture, line system, cel system, and subject count fixed unless the user explicitly changes them.

## 9. Repair Routing

### Looks generic

Strengthen short soft jaw, large coherent iris, sparse nose/mouth, broad hair silhouette, uneven cheek hatching, hand/contact action, and background-to-character detail contrast.

### Looks too cute

Keep the soft family shape while lowering eyelids, reducing decorative highlights, narrowing shoulders inward, quieting the mouth, and localizing grey-olive shadow and under-eye marks.

### Looks too dark

Restore pale skin mids, natural sky/window light, environment-local colors, and one small accent. Keep darkness local to hair, eye, neck, foreground occlusion, or material evidence.

### Looks glossy or 3D

Merge hair into larger shapes, simplify skin to matte flat color, reduce gradients to one graphic shadow family, soften specular highlights, restore charcoal contour variation, and move texture into backgrounds.

### Face identity drifts

Repeat face shape, iris size/color, eyelid weight, mouth grammar, hair outer mass, major clumps, skin tone, cheek marks, and clothing collar. Reduce simultaneous lane changes.

### Group count or relationships drift

State exact count, name internal roles, assign foreground/midground/background positions, give each person one gaze and gesture, and define one shared object or blocked route.

### Cultural setting drifts

Replace generic country labels with exact architecture, clothing, furniture, floor, bags, signs, packaging, transit, and vegetation.

## 10. Final Audit

Before output, confirm:

- one frozen moment is drawable;
- subject count and identity roles are exact;
- culture layer is concrete;
- framing has a first read, second read, and depth structure;
- body weight, gaze, hands, and prop ownership are visible;
- the face and hair follow the family grammar;
- line hierarchy is hand-drawn and economical;
- one cel-shadow family and motivated light are specified;
- skin, hair, clothing, environment, light, shadow, and accent have separate color roles;
- backgrounds are denser than character surfaces when the scene requires depth;
- paper/capture finish is light and matte;
- the source label has been translated away;
- the paragraph contains no negative list, video grammar, weighting syntax, or MJ parameters.

## Example: Character Key Art

```text
三名年轻角色的二维动画人物定调插画，干净的浅奶油色背景让人物轮廓和互动成为第一视觉中心，三人以不同身高和身体方向自然靠拢，左侧长发女孩抬臂举着小型拍摄板并闭眼大笑，中间短发女孩肩膀放松、双手轻握斜挎包带，右侧男孩微微侧身、耳机垂在颈前并留下略显尴尬的半闭眼表情，每个人的手势、视线和道具归属清楚，人物采用略大的头部、窄肩和纤细四肢，脸型上宽下短、下颌圆钝，五官简洁，大面积完整虹膜配一处主要湿润高光，鼻子只用短小笔触，笑脸通过柔软眼睑弧线、简洁嘴形和短促桃粉色脸颊排线完成，头发先形成黑色或金色的大块剪影，再用少量方向明确的边缘发束分开，深棕灰细线带轻微手绘粗细变化，服装以清楚平涂色块和肩部、肘部、腰部、背带接触处的少量褶皱塑造重量，皮肤哑光明亮，只用一组克制的赛璐璐阴影，画面加入少量与人物情绪对应的粉色和黄色图形符号，整体保留极轻纸张颗粒与干净动画插画质感
```

## Example: Lived-In Scene

```text
一幅接近垂直俯视的二维动画室内关键帧，狭小卧室的地面、榻垫与家具边缘形成完整平面地图，一张凌乱的浅灰白被褥位于画面中央成为明亮视觉岛，短发少女仰躺在其中，身体和四肢保持放松而略显疲惫的自然重量，手边贴着一个极简珊瑚粉圆形小生物，床铺周围分布书包、课本、文具、衣物、餐具、插线板、鞋、塑料包装和生活小物，它们按学习、进食、换衣和出门等功能组成疏密不同的物件簇，人物表面保持干净哑光的平涂赛璐璐色块，头发是大块柔软黑色剪影，脸部只有简洁闭眼、短小鼻口和少量疲惫线条，深棕灰细轮廓带轻微手绘变化，被褥、纸张、旧布、木材、塑料、金属和地面纹理比人物拥有更丰富的材质笔触，环境以灰褐、暗橄榄、旧红和洗淡蓝为主，青绿色短裤与粉色小物形成有限高纯度落点，侧上方日光落在被褥和人物脸上，四周逐渐进入较深但仍可读的生活阴影，整幅画带极轻纸张颗粒和传统动画摄影的柔和质感
```
