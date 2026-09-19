# GPT Image Control Reference

Source: `F:\剧本创作四步骤\提示词画风\AIGC提示词手册·七渡(1).html`

## Central Principle

GPT-style image models often over-sharpen and over-fill detail. They also respond poorly to direct negative prompts. Convert "do not X" into a positive target.

Example:

- Weak: `不要过度锐化`
- Better: `柔焦边缘，柔和边缘过渡，胶片柔光，高光自然晕染，非数码锐利`

## Qidu Universal Prefix

```text
柯达Vision3 5219胶片质感，IMAX 65mm 拍摄，诺兰电影摄影风格，霍特玛掌镜，有机胶片颗粒，高光自然晕染（halation），柔和对比度，黑位略微提亮，自然光主导，仅使用实用光源，球面镜头（非变形宽银幕），浅景深，胶片化学调色，无数字锐化。
```

## Qidu Universal Suffix

```text
柔焦边缘，克制的细节表达，大色块优先，材质统一干净，避免堆砌细碎纹理，整体通透高级。参考电影摄影质感：自然胶片颗粒，像一张精心打光的电影剧照，而不是高清数码照片。
```

## Positive Keywords

Chinese:

```text
柔焦边缘，柔和边缘过渡，胶片柔光，高光自然晕染，化学冲印柔度，非数码锐利，克制细节，大色块，留白，化繁为简，主体突出，单一焦点，视觉层级分明，统一材质，平滑表面，干净渲染，哑光质感，材质语言一致，弱化微观细节
```

English:

```text
soft focus edges, gentle edge falloff, film-like softness, halation on highlights, photochemical softness, analog edge bloom, restrained detail, minimalist texture, large color blocks, negative space, graphic simplicity, clear visual hierarchy, unified material feel
```

## Universal Tail

Chinese:

```text
画面风格要求：柔焦边缘，克制的细节表达，大色块优先，材质统一干净，避免堆砌细碎纹理，整体通透高级。参考电影摄影质感：浅景深柔光、自然胶片颗粒、Kodak Portra 400 色调，像一张精心打光的电影剧照，而不是高清数码照片。
```

English:

```text
Visual style: soft cinematic rendering, gentle edge falloff, restrained detail, large clean color blocks over busy textures, unified material feel, film-like softness. Reference: shot on Kodak Portra 400 / Vision3 5219, shallow depth of field, natural film grain, refined cinematic still rather than a crisp digital photo.
```

## Contrast Reference Method

Use comparison language when it helps:

```text
画面应该像“胶片电影剧照”，而不是“手机 HDR 照片”。
应该像“杂志摄影作品”，而不是“游戏 CG 渲染图”。
应该像“诺兰《星际穿越》的 IMAX 胶片帧”，而不是“AI 默认美术图”。
```

## Image Refinement Prompt

Use this for existing images that are too sharp or noisy:

```text
完整提取并保留原图中的所有信息：构图、人物姿态与表情、服装、场景、道具位置、光源方向、整体色调与氛围、镜头景别。
在此基础上完全重绘这张图，重置画面质感：
- 去除原图过度锐化，消除边缘的硬刃感与高频噪点
- 弱化过于细碎的纹理细节（毛孔、布料织线、墙面颗粒、发丝抖动等）
- 改为柔和顺滑的渲染：干净的边缘、整洁的色块过渡、统一的材质表现、电影级柔光
- 保留必要的结构细节，但让画面更耐看、不刺眼、不毛躁
- 整体呈现：高级感、丝滑、通透、克制的细节、电影质感
不要改变人物、构图、光影方向和核心信息。
```

## Banana 2 / Natural Language Redraw

```text
请完整识别这张图里的所有信息：人物长相、姿态、表情、服装、配饰、场景、道具、光源方向、色彩基调、镜头景别与构图。
在保持这些信息 100% 不变的前提下，重新生成这张图，重置画面质感：
1. 去掉原图的过度锐化，消除边缘的硬刃感和不自然的高频细节
2. 抹平过于碎的纹理（皮肤毛孔、布料织线、发丝噪点、墙面颗粒）
3. 换成柔和顺滑的渲染：边缘干净、过渡自然、材质统一
4. 加入电影级柔光与通透感，画面要高级、丝滑、克制
5. 保留必要的结构细节，但整体观感舒服、不刺眼
人物的五官、脸型、发型、肤色必须和原图完全一致，这是同一个人，只是画面质感更柔和了。
```
