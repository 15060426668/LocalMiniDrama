# SD Video Combination Grammar

Use this file when a storyboard segment contains combined movement: character action, camera movement, space/VFX change, transition, or a landing frame in the same short video prompt. Its job is to prevent SD / Seedance from confusing `head turn` with full-body turn, `lateral truck` with orbit, or `scene change` with random morphing.

## 1. Core Split

Every complex A segment must separate five tracks before writing the final prompt:

```text
主体动作：who moves, which body part moves, which body part stays oriented, contact/weight, secondary motion.
镜头运动：camera type, path, speed, start frame, end frame, lens/device, what the camera lands on.
空间/物件变化：trigger, affected surface/object, visible process, old-to-new relation, residual trace.
落点画面：the final readable frame after the movement or VFX resolves.
连续性：what carries into the next second: body direction, object state, light state, camera relation, sound tail.
```

When dialogue is active, add a sixth track:

```text
台词/口型轨：speaking character, phrase window, mouth/jaw articulation, gesture window, listener reaction window, exact moment the body route changes.
```

Keep these tracks separate in A. SD reads mixed verbs more reliably when the subject, camera, and environment each have their own assignment.

Dialogue plus a major body route, major prop handoff, collision, or second speaker counts as a dense beat. Separate the tracks at complexity `4-5`; split the beat at `6+` or when two speaking mouths compete.

## 2. Positive Stability Anchors

The user requires positive-only prompts. Convert risks into visible anchors:

- Geometry risk -> `建筑直线保持稳定，墙线平直，透视线沿走廊深处收束`.
- Identity risk -> `同一角色外观连续，脸部特征稳定，服饰连续`.
- Floating gait risk -> `脚掌真实接触地面，脚跟到脚尖发力，重心随步伐前移`.
- Camera drift risk -> `镜头沿墙线直线横移，路径与走廊墙面平行，落点停在指定墙面`.
- Wrong turn risk -> `身体和脚步仍朝走廊深处，只有头颈短促向后瞥一眼`.
- Door continuity risk -> `原门位变成连续潮湿墙皮，保留长方形门框水印和锈色铰链痕`.

Use these as positive facts inside A. Output only positive prompt blocks by default; add other blocks only when the user explicitly asks.

## 3. Camera Movement Translation

Use standard camera terms as English anchors inside Chinese prompt lines when needed. Keep the output mainly Chinese unless the user asks for English-only.

| 中文意图 | SD anchor | Write it as |
| --- | --- | --- |
| 横移 | `lateral truck`, `truck left/right`, `slide left/right` | 镜头沿墙线做直线快速横移，rapid lateral truck / slide right，前景灯管和墙边形成视差，落点停在门位墙面 |
| 甩镜 | `whip pan`, `fast pan with motion blur` | 镜头原地快速甩向右侧，fast whip pan，运动模糊作为转场，同方向进入下一画面 |
| 背后跟拍 | `rear tracking shot`, `tracking from behind` | 背后中低机位跟拍，rear tracking shot，人物奔跑，墙线快速后退 |
| 侧面跟拍 | `side profile tracking` | 侧面平行跟拍，subject and camera moving at synchronized speed，背景灯光拖成横向光轨 |
| 主观视角 | `POV shot`, `first person view` | 第一人称主观视角，hands visible at frame edge，自然头部微晃和呼吸起伏 |
| 推近 | `dolly in`, `push in` | 稳定推近，slow dolly in，焦点落到眼睛/手/物件 |
| 拉焦 | `rack focus`, `focus shift` | 焦点从前景物件滑到人物眼睛，rack focus，前景虚化成散景 |
| 低机位贴地 | `low angle tracking close to ground` | 贴地低机位跟随脚步，脚掌和地面接触清晰，地面反光高速掠过 |

Important distinction:

- `lateral truck / slide` means camera position translates sideways.
- `pan / whip pan` means camera rotates from a fixed position.
- `orbit / arc` means camera circles around the subject.

For the user's corrected case, anchor the camera as `rapid lateral truck / slide`: the camera path stays parallel to the wall line and lands on the rear door position.

## 4. Character Action Translation

| 中文意图 | SD anchor | Required physical detail |
| --- | --- | --- |
| 扭头 | `head turn`, `turning head` | 眼睛先动，颈部转动，肩膀保持稳定，头发半拍延迟 |
| 回头瞥一眼 | `looking back over shoulder` | 身体仍朝前，只有头颈和少量上肩转动，视线短促扫过后回收 |
| 转身 | `full 180 degree turn` | 以脚为轴，重心换脚，衣摆和头发随旋转展开，转完站稳 |
| 奔跑 | `running`, `sprinting` | 蹬地发力，重心前压，脚掌落地，衣物和头发向后带出速度 |
| 前冲 | `bursting forward`, `explosive lunge forward` | 后脚蹬地，身体前倾，手臂冲刺摆动 |
| 骤停 | `abrupt halt`, `freezing in place` | 上半身因惯性前倾，手停在半空，呼吸和眼神短暂凝住 |
| 踉跄 | `stumbling`, `tripping` | 脚步错乱，手臂张开找平衡，身体晃动后重新压回重心 |
| 抓滑 | `hand slipping`, `losing grip` | 指尖沿物体表面滑过，身体瞬间下沉，手指重新抓空或抓住新物 |

If the action is subtle, name the moving body part. If the whole body moves, name the footwork and center of gravity.

## 5. Space / VFX Translation

Write space changes as time-based visible processes:

```text
source surface/object -> trigger -> first visible change -> middle deformation -> new surface/space -> residual trace -> light/sound sync
```

Stable forms:

- Door vanished: `原门位已经被连续潮湿墙皮替代，墙皮纹理和两侧墙面接上，长方形门框水印、锈色铰链痕和滴水线保留在原位置`.
- Lights-out shift: `顶灯闪烁两次后短暂黑场，冷白灯重新亮起时空间布局已改变，灯带位置仍沿走廊中轴排列`.
- Reflection becomes real: `光滑潮湿地面的倒影先出现左右走廊，顶灯一闪，倒影里的十字回廊轮廓从地面反光抬升成真实墙线和门洞`.
- Endless corridor: `走廊尽头持续后退，天花灯一格一格拉长，门牌号沿透视线重复，空间深度向远处延伸`.
- Wall morph: `墙纸裂纹沿镜头运动方向加深，旧墙纸边缘卷起，材质逐渐变成剥落病院墙皮，墙角留下旧花纹残痕`.
- Doorframe transfer: `门框黑影遮满画面，镜头继续同方向前冲，黑影退开时露出新空间，保留同一个移动方向和同一条冷白光边`.

For complex transitions, prefer one dominant matter logic per shot: reflection, light blackout, occlusion, texture morph, fold, liquid, fragments, particles, smoke, digital refresh, paper tear.

## 6. Combined Prompt Order

Inside each A segment, write the detail in this order:

```text
镜头层 -> 主体层 -> 动作层 -> 物理层 -> 空间/物件变化层 -> 光影层 -> 画面基调/质感层 -> 声音/连续性层
```

The A block may still use the normal eight field labels. This order is a thinking checklist for the content under those labels.

## 7. Misread Repair Patterns

### Case A: quick glance back + camera slide

Weak wording:

```text
镜头跟随她回头看身后。
```

Stable positive wording:

```text
主体动作：她身体和脚步保持朝向走廊深处，只有头颈短促向后瞥一眼，头发因惯性甩起半拍后落下，视线立刻回收。
镜头运动：镜头沿走廊墙线做直线快速横移，rapid lateral truck / slide right，路径与墙面平行，从她侧脸位置扫向身后原门位，运动模糊集中在前景墙边和顶灯边缘，落点停稳在原门位墙面。
空间变化：原门位已经变成连续潮湿墙皮，保留长方形门框水印、锈色铰链痕、几道向下流的水迹。
连续性：她收回视线，重心前压，脚步继续向走廊深处加速。
```

### Case B: chase through changing corridor

```text
主体动作：角色向前奔跑，脚掌真实接触潮湿地面，重心前压，肩膀随喘息起伏，衣摆和头发向后拉出速度。
镜头运动：低机位背后跟拍，rear tracking shot close to ground，镜头与角色保持半身距离，地面反光和两侧墙线快速后退。
空间变化：每一次顶灯闪烁，地面倒影先出现新的门洞和侧廊，下一次亮起时倒影结构升成真实墙体，旧墙皮保留湿痕作为残影。
落点画面：镜头落在新的十字回廊入口，人物位于画面下三分之一，深处门洞一层套一层。
```

### Case C: door opens into waking transition

```text
主体动作：角色推开门后前脚踏空，手本能伸向门框，指尖擦过剥落墙皮，身体向黑暗下坠。
镜头运动：主观视角跟着身体失重下落，POV falling motion，画面边缘拉成长条暗影。
空间变化：门内黑暗形成深井般的纵深，黑暗中浮出病床铁栏的冷白反光，手掌在下坠末端抓住铁栏。
落点画面：画面稳定在破旧病房床边，手指紧抓生锈床栏，床头残烛火苗在右侧轻晃。
连续性：坠落风声收束成病房里的急促喘息和铁栏震动声。
```

## 8. A-Block Mini Template For Dense Shots

When a shot has two or more simultaneous movement systems, include this compact split under `机位与运镜` or `画面内容`:

```text
组合动作拆解：
主体动作：...
镜头运动：...
空间/物件变化：...
落点画面：...
连续性：...
```

Then continue the normal fields. This is allowed because it preserves detail and prevents SD misread.

## 9. Self-Audit Additions

Before final SD output, check:

- Every dense shot separates subject action, camera movement, space/object change, landing frame, and continuity.
- Camera verbs are exact: truck, pan, orbit, dolly, track, POV, rack focus.
- Character verbs name body parts, contact, weight, and secondary motion.
- Space changes use visible process and residual trace.
- The output remains positive-only.
- The A block inherits storyboard detail; the E block only indexes it.
