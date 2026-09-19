# Storyboard + Dream SD Regression Suite v5.4

Runtime version: `5.0 / 2026-07-12`

Use this suite after structural edits to either skill, after changing the shared compiler contract, or when generated output loses storyboard detail.

## Test Procedure

For each case:

1. derive a fresh partition from the current requested total and natural action/transition/information boundaries; use whole-second segments of 4-15 seconds whose durations sum exactly to the request, rebalance any 1-3 second remainder, and never reuse a fixed example partition.
2. for the current scene, return zero to six film-reference mechanisms whose camera/staging/rhythm/sound/transition logic can help the design, without padding and without requiring equal duration or timestamps.
3. let the user select, combine or decline mechanisms; establish one coherent director grammar, retime it for the current short, then write the executable formal storyboard.
4. compile the segment through `BASE MANIFEST -> SEGMENT DELTA -> TAIL STATE -> NEXT SEGMENT START`.
5. produce A blocks and a matching E timeline.
6. at the next segment boundary, inherit the prior tail state before applying the next approved storyboard delta.
7. locate the first failed layer: reference synthesis, source storyboard, manifest, A delta, tail bridge, E index, or model execution.

## Universal Gates

Every case must pass all gates:

- `21:9` cinematic composition unless the current project explicitly overrides it.
- each current scene may begin with a five-axis mechanism gate; zero useful film candidates is valid and candidate lists are never padded.
- returned candidates may be selected individually or combined by named mechanism; the approved formal storyboard becomes the sole execution source.
- film duration and edit rhythm never determine target-segment timing; long-sequence segmentation follows current-story boundaries while continuity buses remain intact.
- long-sequence segmentation is adaptive to the current scene; equal-length chunks and prior numeric examples are never treated as templates.
- integer-second timing; one user-facing SD prompt is at most 15 seconds and may contain several consecutive A beats.
- `one segment at a time` means one prompt per turn, not one camera beat; `0-5 / 5-10 / 10-15` remains one valid 15-second prompt.
- fixed-camera information refresh occurs within 1-4 seconds.
- each cut or long-take beat changes information, power, distance, direction, focus, scale, light permission, sound position, object state, body state, or spatial rule.
- each shot has one current attention owner; information permission is traceable; NPCs, props, machinery, weather, plants, light, camera and sound follow purposeful causal layers rather than random or synchronized motion; no character reacts before receiving a cue.
- rule scenes preserve trigger ownership, allowed action, external-force boundary, direct consequence, residual state and next choice.
- spoken beats fit measured Chinese phrase windows; mouth, route, hand action, listener reaction and camera landing do not compete for the same moment.
- formal storyboard rows preserve shot/lens, drawable composition, camera route, shot-level light/color, visual tone/texture, photographic evidence, visible action, motion ecology/layer interaction, sound, transition, narrative purpose, shot delta/tail frame, and SD handoff anchor.
- A inherits concrete nouns, action order, frame layers, screen direction, light source, texture proof, sound cues, transition process, and tail state from the source row.
- stable facts live in the shared manifest; shot-specific facts remain in the A delta.
- every tail state becomes the next start state before a new delta begins.
- A uses positive visible/audible execution language.
- E time ranges and actions match A exactly.
- complexity `0-3` remains compact, `4-5` uses separated tracks, and `6+` splits; two camera paths or two transitions split.

## Core Regression Cases

| # | Test scene | Storyboard must prove | SD compiler must preserve | Failure signature |
|---:|---|---|---|---|
| 1 | 快速扭头回望 + rapid lateral truck | 人继续向前，肩胯保持前进，头颈短促回望；摄影机做快速横移后落回前进方向 | 身体动作与摄影机动作分轨；起幅、横移路径、回望时长、视线回收、落幅明确 | 把横移写成环绕；人物整身转向；回望后停住 |
| 2 | 狭长走廊追逐 | 前后距离、跑动方向、脚底受力、呼吸失衡、追兵声源方位、背景速度证据逐镜变化 | 地面接触、衣料惯性、墙灯掠过频率、声源逼近和每镜风险增量 | 只写快速奔跑、手持跟拍、紧张音乐；空间距离不可读 |
| 3 | 梦境坍塌 / 连续空间变形 | 变化区域、未变化区域、触发物、移动边界、材质过程、新空间和残留痕迹可见 | 单一主导物质逻辑；旧画面到新画面的全过程；尾帧残留进入下一段 | 只写空间坍塌、梦境转场或白光；多种材质同时争夺画面 |
| 4 | 家庭琐事升级为离婚争吵 | 房间轴线、门与桌的位置、物件所有权、说者与听者并行动作、权力站位、角度间光影差异；台词按实际语速可完成 | 台词/口型、主动作、听者反应、背景动作和道具状态分轨；重音、停顿、行动升级和情绪残留跨切继承 | 交替说话头像；15秒塞满台词；房间冻结；每个机位光影完全相同；道具跳手 |
| 5 | 规则物件交接 | 物件身份、材质、原持有人、手、朝向、交接动作、声音指纹和新持有人；谁能触发规则及外力边界明确 | 交接前后同一物件；手指接触顺序、方向、表面痕迹、规则反馈、直接后果和尾帧位置连续 | 物件消失、变形、换手无过程；为镜头临时改变规则；声音与接触不同步 |
| 6 | 监控/手机屏幕证据 | 屏幕内容可读，观看者反应先后明确，现实空间有对应物，设备状态可回收 | 屏内信息、屏外环境、焦点路径、观看者微反应、设备亮度/角度和后续道具状态 | UI太小；靠台词解释；屏幕内容与现实空间无对应 |
| 7 | 图生视频源帧续写 | 源图角色、姿势、手脚接触、构图层、空间位置、光源、材质和第一运动源被逐项锁定 | 第一秒从源帧状态启动，只写增量动作；摄影机起幅与源图透视一致 | 首帧已换构图、换脸、换光；人物和摄影机同时无锚点大幅运动 |
| 8 | 梦中惊醒转场 | 梦境触点与现实身体反应通过同一手、物、光、声音或构图形状连接；惊醒有肌肉和呼吸过程 | 接触锚点跨空间继承；梦境尾帧、现实首帧、抽搐/吸气/视线定位顺序明确 | 纯白闪光或无依据硬切；醒来后身体状态归零 |
| 9 | 雨夜 / 水环境追逐 | 湿度累积、脚印、水花、布料重量、头发贴附、能见度和声音遮蔽持续变化 | 水的重力、表面张力、冲击方向；衣料和步态随含水量改变；尾帧湿痕继承 | 雨只作贴图；衣服始终干轻；水花方向与脚步受力不一致 |
| 10 | 物件所有权 + 社会/制度证据 | 工牌、病历、门禁、餐具、制服磨损或公共设施通过使用痕迹说明身份、权力和前史 | 所有权、使用方式、材质磨损、空间归属、背景人员反应和后续回收点 | 道具只作装饰；信息由对白重复说明；社会空间没有使用痕迹 |

## Counterpart Retrieval Smoke Tests

The storyboard skill must fingerprint each request and return only genuinely useful film-reference mechanisms. Zero candidates is valid. Each returned candidate names a recognizable film scene and concrete visual mechanisms. The user may select one or combine several; after synthesis, one approved formal storyboard becomes the only execution source:

| Query | Required precision pool | Pass condition |
|---|---|---|
| 三个人在厨房争执，其中一人悄悄改变立场 | `counterpart-signature-retrieval-atlas.md` AB01-AB10 | blocking/position exposes the alliance shift; candidates are not three ordinary dialogue scenes |
| 隔着墙听到追兵靠近，连续切换房间机位 | SP01-SP10 | sound distance, obstruction and room response survive every cut |
| 同一场调查戏镜头忽远忽近但必须保持统一摄影逻辑 | LC01-LC10 | focal family, perspective, focus route and information progression remain coherent |
| 一个强调色前面是安全，后面反过来成为危险 | CP01-CP10 | color has source, owner, first meaning, repeated state and payoff meaning |
| 女主只看了一眼门，镜头就快速移向出口 | PE01-PE10 | gaze/body micro-action clearly causes the camera move or cut |
| 前景夫妻争吵，背景孩子无声收拾行李 | FB01-FB10 | foreground dialogue and background consequence remain simultaneously readable and causally linked |

## Execution-Risk Smoke Tests

| Query | Required route | Pass condition |
|---|---|---|
| 两人边走边争论，一人递回钥匙，背景电梯到达 | `dialogue-physical-interaction-grammar.md` + DL01-DL20 | speaking mouth, walk route, key weight transfer, listener reaction, elevator event, camera and sound receive separate windows or a justified split |
| 女主雨中奔跑，鞋底打滑，手掌撞墙后继续逃 | `dialogue-physical-interaction-grammar.md` + PC01-PC20 + SD physical execution | force, wet friction, wall contact, body compression, camera response, recovery steps and wet hand mark survive into A |
| 四人餐桌对话，主角说话时另外三人各有任务和不同反应 | `active-frame-background-state.md` + dialogue grammar | one line owner remains dominant; listener, serving action, phone-check and delayed glance have separate priorities and causal timing |
| 开窗后风吹动窗帘、植物、水面和纸张 | `active-frame-background-state.md` + SD motion ecology | all carriers share one wind direction, respond by weight/distance, settle at different speeds and leave one readable tail state |
| 医院走廊人物经过护士站并碰到输液架 | motion ecology + physical interaction | body contact moves the stand, wheels continue, nurse reacts unevenly, monitor/elevator cycles persist, sound and tail trace carry into the next shot |
| 餐厅争吵中钥匙碰杯、倒水溢出、服务员延迟抬眼、窗风同时作用于窗帘和植物 | ME-B + ME-C + ME-D + SD motion ecology | key remains primary; listener, waiter, water, curtain and plant respond in causal order; wind carriers share direction; wet-key tail state is inherited |
| 车辆急刹时人物、吊环、杯中水和背景乘客同时受力 | ME-A + ME-C + SD shared-force grammar | all layers share braking direction but respond by weight, restraint and delay; one camera landing and one sound impact remain dominant |
| 黑暗空间中观众看见跟随者，主体只能听见脚步 | ME-I01 + SD information-permission compiler | hidden background action remains visible to audience; subject route reacts only to audible/tactile cues; knowledge state stays consistent across cuts |
| 门铃打断多人聚会，四人依次停止手中任务 | ME-I03 + ME-J04 | reaction forms a cascade based on attention and social reading; television/weather cycles continue; doorway changes access and group blocking |
| 镜头前公开拥抱，贴身手势向伴侣传递威胁 | ME-I05 + dual-channel acting | public face/body and private hand/gaze/whisper occupy separate amplitude layers; crowd reads only the public layer; tail state preserves contact pressure |

## Registered Behavioral Run

The executable registry contains fourteen general execution cases, ten single-mechanism rule/identity cases, four cross-mechanism integration cases, five 《残烛》 actual-scene hard-lock cases, and one project-wide core-candle continuity case. The project cases cover the cold-open landing, rule-card game start, hidden response plus rule test, reverse-room containment, birthday rewind loop closure, and CZ07-CZ12 candle ownership/state continuity.

```powershell
python ../../director-storyboard-integrated/scripts/run_behavioral_regression.py <artifact-directory>
```

Each artifact is named `BR01.md` through `BR34.md`. Every artifact with A must pass positive-language, source-shot mapping, source-anchor coverage, required case terms and any declared hard-lock exclusions. If E is emitted, A/E timing must also match. Missing artifacts remain pending and are never counted as passed.

## Pass Record

First run deterministic format regression:

```powershell
powershell -ExecutionPolicy Bypass -File ../../director-storyboard-integrated/scripts/run_static_regression.ps1
```

This verifies canonical storyboard fields, integer timing, total user-facing SD prompt duration, positive-only A content, source-shot-to-A mapping, compact execution-field coverage, optional E equality and separation of model payload from production attachments. It does not replace the thirty-four registered behavioral scene tests.

Latest deterministic run:

```text
Date: 2026-07-12
Pass storyboard fixture: pass
Fail storyboard fixture rejected: pass
Pass SD fixture: pass
Fail SD fixture rejected: pass
One 15-second prompt with three internal A beats: pass
Cumulative A duration above 15 seconds rejected: pass
Validator result: pass
Validator contract unit tests: pass
Multi-film mechanism retrieval, short-form retiming and storyboard-only SD source policy: pass
Alphanumeric source-shot IDs and strict 100% anchor coverage: pass
Dialogue timing estimator: pass
Model-profile compiler: pass
Frame-sequence technical QA: pass
Planned sound-mix calculator: pass
Actual PCM WAV delivery self-test: pass
Behavioral thirty-four-case suite: BR01-BR14 preserve the v4.9 execution surface; BR15-BR24 cover single rule/identity mechanisms; BR25-BR28 validate cross-mechanism arbitration and stable coverage; BR29-BR33 validate 《残烛》 locked-scene execution and premature-information exclusion; BR34 validates the original candle as one uninterrupted A-tier anchor across scene changes
```

Record only the compact result:

```text
Case:
Storyboard gate: pass / repair
Compiler gate: pass / repair
Continuity bridge: pass / repair
Complexity decision: compact / separated tracks / split
First failed layer:
Repair applied:
```

The two-skill system reaches behavior-verified status only when all registered cases pass after the latest structural edit.
