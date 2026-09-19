# Midjourney Look-Development Template

Use this route when the user wants Midjourney prompt text rather than generated media. Return a copy-ready Chinese prompt and do not invoke an image generator.

## Output Contract

- Default to one parameter-free prompt unless the user supplies or approves MJ parameters.
- Preserve the requested subject count, gender, age band, action, location, era, and distance.
- Never add a male character when the user did not request one.
- Keep source artist, account, video, franchise, and donor-shot names outside the copy-ready prompt. Translate them into observable line, crop, material, and light behavior.
- If the user says not to describe masking or black subtraction, omit the whole black-geometry block. Do not reintroduce it as a curtain, portal, shadow, screen, void, or metaphor.
- Do not generate an image. The deliverable is prompt text only.

## Assembly Order

Write the prompt in this order:

1. **Drawable moment:** location, era, weather, subject action, and emotional state.
2. **Camera evidence:** camera position, lens feel, frame distance, vanishing structure, depth, and subject scale.
3. **Real plate lock:** real materials, natural exposure, documentary imperfections, grain/compression, atmospheric depth, and physically plausible reflections.
4. **2D character lock:** colored hand-drawn identity, contour behavior, fill palette, cel shadow, face grammar when readable, and distant-silhouette priorities when not.
5. **Black mode, only when requested:** choose either spatial matte motion or editorial dead-black reconstruction. Never blend both vaguely.
6. **Cross-medium proof:** support contact, cast shadow, occlusion, environmental crossing, reflection, color spill, and perspective.
7. **Failure exclusions:** reject only likely drift modes for this request; keep them in one compact sentence rather than a keyword dump.

## Real-Plate Lock

Use concrete evidence such as:

```text
真实纪录片摄影底片，普通天气与未经美化的生活场景，真实镜头透视和空气远近层次，旧木、湿石、草叶、墙皮与积水保留不规则细节，自然曝光，克制高光，轻微手机摄影压缩与胶片颗粒
```

Avoid polished 3D voids, glossy concept-art surfaces, clean studio lighting, neon portals, excessive bloom, and fully synthetic environments.

## Colored 2D Character Lock

Use the user's established character family:

```text
全彩2D手绘人物，深蓝灰色细轮廓，线条有轻微抖动、复描、断线与不均匀线重，低饱和灰蓝、旧米白和克制的局部色，哑光平涂，少量赛璐璐阴影，头发概括成宽阔块面，局部保留草稿排线，保持纸上手绘感而非商业动漫净线
```

For distant figures, replace face-detail budget with readable posture, hand tension, prop weight, silhouette, and the exact support point.

## Editorial Dead-Black Block

Use only when requested:

```text
连续现实被编辑性死黑删去，只保留人物脚下的一小块真实支撑面、一条符合原镜头透视的狭长道路或台阶、以及远处一块来自同一地点的摄影窗口；各碎片内部保持同一镜头的真实比例与光线，黑色不解释成物体或传送门
```

## Spatial Reveal Block

Use only for moving-image design or an explicitly frozen reveal state:

```text
黑色边界沿人物动作或建筑透视改变开口，先允许脚下接触和道具出现，再显露身体意图，最后才打开远处真实世界；开口具有明确方向、边缘速度和停止位置
```

## Hybrid Proof Block

```text
二维人物与实拍环境共享准确透视和光源方向，脚底接触阴影压紧在真实表面，环境冷暖色溢进入线条和阴影，雨丝、树影或前景实物从人物前后穿过；绘制身份始终清楚，人物不真人化、不漂浮
```

## Repair Questions

Before returning a prompt, check:

- Can the scene still read as a real photograph after removing all style adjectives?
- Is the subject's distance numerically or proportionally constrained?
- Is the 2D identity observable without naming a franchise or artist?
- Does the character have a visible support surface and weight cue?
- If black is present, is the selected operating mode unambiguous?
- Did the prompt invent any person, especially a male figure, that the user did not ask for?
- Did the user explicitly ask to omit the black treatment?

