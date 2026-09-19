# Counterpart Signature Retrieval Atlas

Runtime version: `1.3 / 2026-07-11`

Use this file when a user gives a scene, a single visual idea, a frame reference, or a compound request that does not fit one broad scene category. This atlas retrieves and ranks film-reference mechanisms by visual usefulness rather than by plot similarity.

The existing `counterpart-radar-shot-index.md` is the broad recall pool. This file is the compound-scene precision retrieval layer. It ranks mechanisms and supports user-approved cross-film synthesis before formal storyboarding.

Source confidence: these cards are mechanism-level training translations. Verify the source before making exact timecode, exact lens or archival shot-order claims.

## Contents

1. Five-Axis Scene Fingerprint
2. Training Card Rule
3. Multi-Character Alliance Blocking
4. Spatial Sound Perspective Across Cuts
5. Lens-Behavior Continuity
6. Color-Script Payoff
7. Performance-To-Edit Causality
8. Foreground-Background Dual Narrative
9. Retrieval Output Contract
10. Training Deposit

## 1. Five-Axis Scene Fingerprint

Convert the request into:

```text
A. dramatic action: approach / wait / search / test / hide / flee / argue / persuade / handoff / watch / wake / cross threshold
B. spatial topology: corridor / table / room / institution / vehicle / vertical space / open landscape / screen / mirror / crowd
C. information relation: audience ahead / character ahead / equal ignorance / unreliable perception / hidden third party / system knows more
D. narrative carrier: body / object / sound / light / weather / reflection / screen / background person / architecture
E. rhythm: fast compression / slow seep / delayed rupture / repetition with one change / continuous movement / reaction-first
```

Use the five axes for broad recall, then score storyboard transferability:

```text
composition and camera mechanism is useful = 2
blocking and spatial design is useful = 2
rhythm and information release is useful = 2
sound / transition / VFX logic is useful = 2
performance / object / background language is useful = 1
AIGC execution remains legible after adaptation = 1
mechanism cannot survive the current physical setup = -3
```

For the current scene, return zero to six candidates that contribute at least two concrete mechanism axes. Do not pad the list. A candidate may solve only one part of the design; the user may combine complementary mechanisms. Zero useful references routes to an original director scheme.

Replaceable variables never reduce a strong storyboard match:

```text
character / identity / awareness / relationship
dialogue / plot cause / story objective
setting / environment / props / costume
threat identity / dream-rule explanation / object meaning
```

Reject broad-scene matches that cannot name concrete visual design. Every returned reference must answer:

```text
recognizable film scene situation
composition and camera mechanism
blocking and information-release mechanism
rhythm / sound / transition mechanism
reusable rule
replaceable variables
strength and failure boundary
```

Reject only when the mechanism cannot be expressed as a coherent camera/staging rule or cannot survive the current physical setup. Film pacing is never transferred automatically; all timing and shot order are redesigned for the current short.

The user filters, combines or declines candidates across turns. A combination is valid only after one unifying director grammar resolves conflicts in camera philosophy, axis, rhythm, sound and transition.

## 2. Training Card Rule

The `0-15秒压缩节拍` column is an AIGC-short-form translation of the film mechanism, not an archival claim about the original scene timecode. When the user asks for formal pull-apart analysis, expand the selected card into the full standard fields.

## 3. Multi-Character Alliance Blocking / 多人阵营与站位变化

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| AB01 | `12 Angry Men` - jury table alignment changes | persuade + table + audience reads alliances + bodies/chairs + repetition-change | 0-3秒全桌阵营；3-7秒一人起身脱离；7-11秒另一人移开视线；11-15秒空椅成为新阵营证据 | 长桌为轴，支持者与反对者分居两侧，空位和站立高度改变票势 | 中广角建立全桌，切中近景只在立场变化时发生 | 闷热中性光，汗和衬衫褶皱记录压力 | 桌面磨损、风扇、汗湿领口、椅脚真实摩擦 | 风扇底噪、椅脚拖动触发切镜，沉默后才给反应 | 用位置变化代替“我支持谁”的台词 | 不照搬陪审团设定；短剧中保留一个主轴和一次阵营移动 |
| AB02 | `Knives Out` - will reading / family reaction field | wait + seated group + audience ahead + document/background faces + reaction-first | 0-3秒文件占前景；3-6秒宣读者抬眼；6-10秒背景两人先交换眼神；10-15秒主角仍不动，其他人同时前倾 | 文件、宣读者、家属形成三层，关系由谁进入前景决定 | 50mm群像转85mm反应，焦点从纸面落到背景眼神 | 暖室内光包裹家族表面，阴影压住边缘人物 | 木桌反光、纸张纤维、旧宅纵深、不同服装材质 | 翻页声先行，呼吸与椅响叠加，切点落在未说出口的反应 | 群体戏先拍接收信息的人，再拍说话者 | 不把所有人剪成同尺寸头像；只保留2-3个关键反应链 |
| AB03 | `The Invitation` - dinner guests divide over exit/control | persuade + dinner room + hidden third party + door/wine/background people + slow seep | 0-3秒暖餐桌正常；3-7秒一人望向门；7-11秒主人挡住门线；11-15秒其余客人继续微笑但手停在杯边 | 餐桌横轴稳定，门在背景负空间，主人移动后截断唯一出口 | 固定中广角保持群体可读，微推只跟随门被占领 | 暖钨丝主光与门口冷暗形成许可差 | 酒杯指纹、餐布褶皱、门锁金属高光、真实室内反射 | 餐具声逐步减少，门锁轻响触发全桌短暂停顿 | 阵营变化先由谁控制出口表现 | 不用夸张敌意；礼貌动作必须持续到控制已经成立 |
| AB04 | `Get Out` - garden gathering social encirclement | watch + crowd + audience ahead + background gaze/body + slow seep | 0-3秒主角被人群留在中景；3-6秒前景宾客擦镜而过；6-10秒背景三人同步看他；10-15秒主角笑容收紧并后退半步 | 主角在群体中心却没有逃生空隙，背景视线形成无形包围 | 中焦压缩人群距离，轻微横移让新的凝视者不断进入边缘 | 日光表面正常，肤色和草地偏自然，异常来自同步行为 | 真实树影移动、衣料受风、杯中液体、人物遮挡层次 | 环境谈笑不断，局部问话靠近，笑声短暂同频后切主角反应 | 用NPC视线和前景经过制造社会包围 | 不把群演冻结成摆拍；每层只执行一个小动作 |
| AB05 | `A Separation` - family/legal dispute across doorway | argue + threshold room + equal ignorance + document/door + delayed rupture | 0-4秒两方隔门框说话；4-7秒文件被推到轴线上；7-11秒第三人从背景插入；11-15秒一方退进门内，权力重新分区 | 门框把家庭和制度分成两块，文件落在边界中央 | 手持中景保持生活现场感，切镜由文件移动和身体越界触发 | 自然窗光与普通顶灯混合，低饱和生活质感 | 墙面使用痕迹、文件折角、鞋与门槛接触、轻微曝光差 | 多人说话有遮盖，纸声和门碰声成为清晰剪点 | 多人争执通过阈限和文件所有权保持可读 | 不追求漂亮对称；必须保留真实抢话和空间方向 |
| AB06 | `Parasite` - family hiding as owners return | hide + layered room + audience ahead + furniture/background bodies + fast compression | 0-3秒多人散在客厅；3-6秒门外声到来；6-10秒身体依次降到家具后；10-15秒前景保持正常，背景仍有一只手未藏好 | 前景主人生活区、中景家具遮挡、背景藏身路径同时成立 | 广角固定空间图，快速小切只追踪最后暴露的身体部位 | 室内暖光保持体面，家具下暗部保留细节 | 木地板、桌布下坠、膝盖撞地、杯中液体轻晃 | 门外钥匙声先行，衣料擦地与压低呼吸分层 | 群体动作按空间顺序连锁，不靠混乱快剪 | 不复制豪宅情节；藏身路径必须在前镜提前建立 |
| AB07 | `Tinker Tailor Soldier Spy` - conference-room suspicion | watch + institutional table + system knows more + files/gaze + controlled stillness | 0-3秒长桌和文件建立级别；3-7秒一人发言，另一人不记笔记；7-11秒第三人抬眼；11-15秒主位人物合上文件结束话权 | 人物高低和桌面文件厚度构成等级，沉默者处在可观察全场的位置 | 长焦中景压平距离，克制正反打，切点跟随笔停和抬眼 | 烟灰、棕绿低饱和，柔暗实用光，黑位有层次 | 纸张旧化、烟雾层、玻璃反光、羊毛服装吸光 | 钢笔、纸页、远处电话，音乐让位给制度噪声 | 不说“谁可疑”，让不参与正常流程的人变成异常 | 不把冷峻等同纯蓝；控制来自规整动作和安静剪辑 |
| AB08 | `The Hateful Eight` - cabin conversation and shifting watch lines | wait + single room + hidden third party + doorway/coffee/eyelines + delayed rupture | 0-3秒全屋关系图；3-7秒一人走向道具；7-10秒两组视线交叉；10-15秒门边人物调整站位封住路线 | 门、壁炉、桌和道具形成四个权力点，站位变化改变谁能看见谁 | 70mm式宽幅群像保留人物间距离，近景只给关键手势 | 暖火光和窗外冷光分属不同阵营 | 木屋缝隙、厚衣料、蒸汽、杯具接触与空气层 | 风声压底，木板和杯具声可定位，话音停顿暴露观察关系 | 单空间群像用可见路线和视线交叉表达临时联盟 | 仅借群体调度；主动避开后续暴力内容与炫耀性台词 |
| AB09 | `Anatomy of a Fall` - testimony changes family alignment | explain + institutional room + unreliable account + recording/document/reaction + reaction-first | 0-3秒证据声先出现；3-6秒说话者被框在中景；6-10秒家属反应先于法庭；10-15秒一次视线回避改变可信度 | 说话者、家属、制度人物分处不同深度，证据媒介占画面边缘 | 中长焦观察，反应镜头比发言镜头更近，避免煽情推镜 | 冷中性日光，木质法庭提供克制暖色 | 真实纸面、录音设备、服装细纹、面部微汗 | 录音与现场声音质感区分，切点由呼吸和视线中断触发 | 用证词接收者的身体变化表现阵营移动 | 不用台词复述画面；证据声与反应必须有因果顺序 |
| AB10 | `Decision to Leave` - police interview with colleagues/screens | question + office/screen + character ahead + phone/reflection/background colleague + slow seep | 0-3秒屏幕与人物同框；3-7秒主问者靠近，背景同事继续工作；7-11秒被问者只看屏幕反光；11-15秒背景同事停手，私密关系被第三人察觉 | 屏幕反射把两人压在同一平面，背景同事成为关系见证 | 中焦隔玻璃/屏幕取景，轻移焦点在主谈话与背景观察间切换 | 冷办公室光，屏幕蓝只属于证据层，肤色保持中性 | 屏幕反光、桌面磨损、咖啡杯水痕、真实办公层次 | 键盘底噪持续，停键声触发焦点转向和剪镜 | 多人场景可用背景工作中断揭露私人关系 | 不堆镜面炫技；每次反射必须携带新的关系信息 |

## 4. Spatial Sound Perspective Across Cuts / 跨切镜空间声音透视

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| SP01 | `The Conversation` - plaza surveillance and replay | watch + open plaza/recording room + audience uncertain + sound + repetition-change | 0-3秒远景人群；3-6秒长焦抓目标；6-10秒录音噪声覆盖画面；10-15秒回放同一句时焦点落到新的手势 | 公共空间中目标很小，后续设备近景把空间压缩成声波证据 | 长焦窥视与设备微距交替，视觉距离和声音距离故意不一致 | 户外自然光转室内低照设备光，模拟颗粒与玻璃反射 | 风扰麦、衣料遮挡、磁带/设备机械动作 | 同一句录音从远、闷、清晰逐次变化，每次清晰度变化触发新画面 | 声音重复可以改写已看过的画面 | 不把录音当旁白；每次回放必须新增可验证信息 |
| SP02 | `Blow Out` - recording becomes reconstructed event | search + outdoor/编辑台 + character ahead + recorded sound/screen + procedural build | 0-3秒麦克风寻找声源；3-7秒异常声进入；7-11秒波形/胶片被对齐；11-15秒声音与画面同步后揭示新因果 | 户外空间先由麦克风方向建立，室内台面用素材顺序重建路径 | 声源POV、器材近景、工作台俯拍，焦点随线索移动 | 夜景实际光点转工作灯，冷暖来源清晰 | 录音轮、磁带、胶片边缘、按钮阻尼、手指油迹 | 声音先于画面，点击与拖动成为剪点，最终同步是段落落点 | 调查戏可先让声音成立，再让画面追上 | 不用抽象波形替代实物操作；观众必须看懂一次对齐动作 |
| SP03 | `The Zone of Interest` - domestic image with off-screen field | wait + home/garden + audience ahead + off-screen sound + sustained contrast | 0-4秒正常家庭行动；4-8秒远处机械/人群声持续；8-12秒人物不反应；12-15秒一个生活小动作与声响冷酷重叠 | 画面保持干净日常，危险完全位于画外方向 | 固定中广景，拒绝寻找声源，空间压力靠持续声场扩展 | 自然日光、整洁表面、克制颜色，现实质感不做恐怖化 | 风、花草、衣物、餐具与远处工业声共享真实空气 | 声音不随切镜消失，墙体和距离改变高频，生活声偶尔遮盖远声 | 画外声可让正常画面拥有第二层意义 | 不借历史情节和暴力声细节；只借“画面拒绝看、声音持续知道” |
| SP04 | `No Country for Old Men` - motel corridor approach | hide + motel room/corridor + character ahead + footsteps/door + slow measurement | 0-3秒室内静止；3-6秒走廊脚步从远侧进入；6-10秒门锁细响，人物压低身体；10-15秒声源停在门外，镜头落到门缝 | 门把、门缝与人物耳朵形成测距三角，走廊保持不可见 | 室内固定近中景与门锁特写，切镜由声源距离而非台词触发 | 暖旧灯、门缝冷光，低照度保留木纹和金属 | 锁芯划痕、墙体吸音、床单受力、鞋底与地毯声差 | 脚步频率、混响和高频衰减连续变化，停声比巨响更危险 | 用声学距离明确追者位置 | 不用无来源低频替代脚步逻辑；空间方向必须稳定 |
| SP05 | `A Quiet Place` - house movement under sound rule | cross threshold + house + system knows more + tiny object sound/body + fast restraint | 0-3秒脚落在安全材质；3-7秒手绕开会响物件；7-10秒背景物轻晃；10-15秒一次微响让全身同时冻结 | 安全路径与危险物件在同一画面，人物动作按声风险排序 | 近地面和手部特写，广角环境镜负责交代可响物位置 | 柔暗自然/实用光，木材、布、灰尘清楚 | 脚掌压力、砂粒、木板弹性、布料重量、呼吸凝结 | 环境底噪被压低，微小接触被放大，响声触发停身与切镜 | 声音规则必须改变步态和手部路径 | 不只写“保持安静”；每个动作要有具体声学后果 |
| SP06 | `The Vast of Night` - switchboard / broadcast voice | listen + booth/town + audience equal + remote voice/device + long verbal pull | 0-3秒电话线路底噪；3-7秒陌生声音进入；7-11秒角色从工作动作转为专注；11-15秒镜头离开人物看向空街，声音继续 | 狭小设备空间与空旷城镇通过同一声音连接 | 设备近景、人物慢推、空街长镜形成距离扩张 | 暖室内灯转冷夜街，模拟时代颗粒和低照黑位 | 旋钮、线缆、电话听筒、街灯雾层、玻璃反光 | 线路失真、呼吸、停顿塑造说话者距离；J-cut把声音带到空镜 | 看不见的人可以通过媒介占领整个城镇 | 不让角色复述电话内容；镜头应寻找声音造成的空间后果 |
| SP07 | `The Lives of Others` - attic surveillance | watch + apartment/attic + audience ahead + headphones/ceiling + controlled stillness | 0-3秒楼下人物日常；3-6秒切楼上监听者；6-10秒脚步经天花板变闷；10-15秒监听者摘下一侧耳机确认真实方向 | 上下两层通过声源垂直关系连接，监听设备成为中间空间 | 楼下中景与楼上紧近景交替，轴线以建筑垂直方向保持 | 楼下暖生活光，楼上冷暗工作光，材质区分私人/制度 | 木楼板传导、耳机压痕、线缆、纸笔、空气尘埃 | 同一声音在楼下清晰、楼上闷化、耳机内近化，质感变化提示空间层 | 跨切声音应携带墙体、距离和设备过滤 | 不把监听声做成全知旁白；保留误听和遮挡可能 |
| SP08 | `Kairo / Pulse` - empty room and mediated voice | search + empty apartment/screen + unreliable perception + room tone/device + slow seep | 0-4秒空房固定构图；4-8秒设备传出断续人声；8-12秒角色靠近但画面边缘保持空；12-15秒声音位置从设备偏向房间后方 | 大量负空间让声源位置可被重新判断，设备不居中 | 固定广角加极慢推，焦点不急于落到声源 | 灰冷自然光、低对比、电子屏局部亮，墙面旧痕清楚 | 电流噪点、空房混响、旧屏刷新、人物脚步延迟 | 声源方位缓慢漂移，角色回头是剪点，房间底噪不归零 | 媒介声可以逐步脱离媒介成为空间事件 | 不用突然贴脸；位置漂移必须有声学过渡 |
| SP09 | `Berberian Sound Studio` - foley creates unseen event | perform + studio + audience imagines more + foley objects + rhythmic montage | 0-3秒普通物件被摆上台；3-7秒第一次拟音与画外影像同步；7-11秒物件动作加快；11-15秒画面留在疲惫表演者，声音仍升级 | 前景拟音物件、中景双手、背景录音设备形成暴力替身 | 物件微距、手部中近景、设备表针切换，剪辑跟声音冲击 | 暖暗录音棚、局部硬光，蔬果/金属/磁带材质鲜明 | 真实切压、液体、金属、磁带转动和手部受力 | 声音承担画外事件，突然停机后只留呼吸和设备惯性 | 不展示事件本体也能制造强烈心理画面 | 主动避开血腥联想描述；用物件受力和表演者反应表达压力 |
| SP10 | `The Shining` - tricycle floor-material rhythm | move + corridor + audience equal + floor sound + repetition-change | 0-3秒轮胎压过硬地；3-6秒进入地毯突然变闷；6-10秒再回硬地，节奏恢复；10-15秒转角前声音先停半拍 | 低机位把地面图案和转角变成主要信息，人物上半身可省略 | 贴地稳定跟随，广角纵深，转角保持中心线 | 均匀酒店实用光，饱和地毯与硬地反光区分材质 | 轮胎震动、地毯绒毛、木地反射、车身轻颤 | 声音随材质瞬间切换，沉默半拍成为转角钩子 | 用材质声节奏剪空间，不依赖追兵出镜 | 不复制酒店花纹；选择当前场景真实存在的两种接触材质 |

## 5. Lens-Behavior Continuity / 整段焦段与景深行为连续性

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| LC01 | `The Shining` - Steadicam corridor following | move + corridor + audience equal + architecture/body + continuous movement | 0-4秒广角贴后跟随；4-8秒转角保持人物在中心；8-12秒空间重复但地面变化；12-15秒人物离镜留下走廊 | 人物小于建筑，走廊透视线持续主导 | 24-28mm广角家族，稳定低位推进，整段不突然压成长焦 | 均匀实用光与高辨识材质色块，清晰深景 | 地板接缝、墙角透视、脚步接触、轻微设备惯性 | 脚步/轮声与转角同步，离镜后空间声延续 | 焦段连续让空间规则可信，再用内容变化制造异常 | 不靠每镜换焦段追求新鲜；变化来自路线、尺度和材质 |
| LC02 | `The Conversation` - long-lens plaza observation | watch + open crowd + audience uncertain + occlusion/sound + slow search | 0-3秒远距离锁定目标；3-7秒行人遮挡；7-11秒焦点穿过前景重新找到目标；11-15秒目标被反光分裂 | 人群层层压在同一平面，目标可被短暂吞没 | 135mm以上长焦家族，轻微寻找式摇移，焦点移动承担发现 | 日光偏平，玻璃和衣料反光制造真实干扰 | 空气压缩、前景虚化边缘、自然遮挡、远距抖动 | 环境声与录音声分层，遮挡时高频变化 | 长焦段落需要保持压缩逻辑，焦点丢失本身就是悬念 | 不把长焦写成纯背景虚化；必须保留遮挡和重新定位 |
| LC03 | `Zodiac` - controlled procedural investigation | search + office/archive + character ahead + documents/focus + measured progression | 0-3秒中广角建立证据桌；3-7秒50mm跟随手部排序；7-11秒85mm落到反应；11-15秒回到相近透视的新证据位置 | 桌面证据和人物反应共享轴线，空间不因切镜重置 | 35/50/85mm递进但透视关系稳定，机位高度与视线保持一致 | 冷绿办公实用光，纸张和肤色低饱和，黑位不死 | 文件厚度、荧光灯反射、手套/手指接触、桌面磨损 | 纸声、电话、铅笔成为程序节拍，切点跟随证据完成一次分类 | 焦段可递进，但必须服务“空间→操作→结论” | 不为每个物件做随机微距；特写只给改变判断的证据 |
| LC04 | `Prisoners` - rain search and compressed observation | search + suburb/vehicle + character ahead + weather/body + slow pressure | 0-4秒车内中长焦看雨外；4-8秒切外景保持压缩距离；8-12秒人物进入近景但背景威胁仍可读；12-15秒焦点落到湿物证 | 人物与远处目标被雨幕压近，车窗形成前景层 | 85-135mm为主，有限手持，焦点在玻璃水迹与远处人影间转换 | 灰冷天光、车内微暖实用光，湿表面高光克制 | 玻璃水流、衣料吸水、道路反射、呼吸雾气 | 雨声在车内变闷、出车后变宽，车门声触发空间转换 | 长焦与雨幕共同制造“看见但到不了”的压力 | 不让雨只做滤镜；内外声学和湿度状态要连续 |
| LC05 | `Black Swan` - close handheld rehearsal subjectivity | perform + rehearsal/mirror + unreliable perception + body/reflection + escalating closeness | 0-3秒35mm贴肩跟随；3-7秒镜面进入；7-11秒镜头更近但仍保持同一广角变形；11-15秒反射动作出现半拍偏差 | 肩、后颈、镜面和背景舞者形成拥挤层次 | 28-35mm近身手持家族，距离变化代替频繁换焦段 | 冷白排练光、皮肤与汗高光真实，镜面边缘略脏 | 呼吸带动肩背、镜面灰尘、衣料拉伸、脚尖受力 | 呼吸、鞋底摩擦和音乐拍点驱动靠近与切镜 | 主观压迫可以靠同一广角不断缩短拍摄距离 | 不把手持等同乱抖；人物方向和镜中轴线必须稳定 |
| LC06 | `The Killing of a Sacred Deer` - clinical wide tracking | approach + hospital + system knows more + architecture/scale + cold continuity | 0-4秒宽幅走廊远景；4-8秒低位平移保持人物小；8-12秒转入房间仍用宽角；12-15秒人物停下，空间继续压住头顶 | 高顶、长墙和地面线条让人物被制度吞没 | 24-32mm宽角家族，低机位稳定滑移，深景持续 | 中性偏冷临床光，规整反射，无情绪化打光 | 地面打蜡反光、门框重复、医疗服材质、真实顶灯间距 | 鞋声与空调声稳定，停步后混响尾巴暴露空间尺度 | 全段保持宽角可把制度压迫变成持续规则 | 不用极端荷兰角破坏冷静；异常来自比例和表演平静 |
| LC07 | `Decision to Leave` - compressed reflections and layered surveillance | watch + office/city + unreliable relation + reflection/screen + focus drift | 0-3秒中焦人物与玻璃重叠；3-7秒焦点落到反射；7-11秒轻横移让真实人物和反射错位；11-15秒切相近焦段的手机画面 | 真实层、反射层、屏幕层共享画面但各有信息归属 | 50-85mm中焦家族，受控横移和拉焦，不突然改透视 | 冷中性环境，屏幕和城市光作为局部色主 | 玻璃双影、手机油迹、窗框遮挡、焦点呼吸 | 城市底噪、设备声、近距离呼吸，焦点落点触发剪镜 | 多媒介画面要用稳定焦段维持关系而非炫技 | 每层只承担一个信息；反射数量过多时删到可读 |
| LC08 | `Burning` - long-distance ambiguity | watch + open landscape/room + audience behind + distant body/absence + slow seep | 0-4秒远景人物极小；4-8秒长焦保持距离观察动作；8-12秒前景遮挡短暂吞没；12-15秒人物离开，只剩被看过的空间 | 大量空域与小人物并置，缺席在人物离开后成立 | 85-200mm长焦家族，极少移动，等待行为自然完成 | 黄昏自然光或朴素室内光，低饱和空气层 | 热浪/雾霾、草木风动、窗帘、远距身体轮廓 | 风、远车、脚步逐渐减弱，离场后保留环境声 | 长焦持续观察能把普通动作变成无法确认的证据 | 不用快速推近替观众下结论；保持判断距离 |
| LC09 | `Se7en` - low-light investigative coverage | search + apartment/office + character ahead + object/light + controlled narrowing | 0-3秒35mm暗空间建立；3-7秒50mm跟随手电/台灯照到物件；7-11秒85mm反应；11-15秒回35mm显示物件与空间关系 | 暗区保留未知，亮区随调查路径逐步开放 | 35/50/85mm有限家族，焦段改变与信息权限同步 | 低照度高反差，实用灯、手电和窗光有明确来源 | 灰尘、潮墙、纸张油污、手电光束触碰材质 | 低频城市底噪、纸声、灯开关，亮区出现时剪镜 | 焦段序列应与“发现层级”对应 | 不把暗等同无细节；关键材质必须在来源光里出现 |
| LC10 | `Blade Runner 2049` - human-to-architecture scale progression | approach + monumental space + system knows more + architecture/light + slow reveal | 0-4秒超广景人物极小；4-8秒中广角进入建筑；8-12秒中焦给人物接收信息；12-15秒回广景显示系统尺度未改变 | 人物尺度变化建立接近感，最终回广景恢复无力 | 广角建立与中焦反应有计划地交替，机位轴线保持建筑中心 | 冷中性色为基底，单一暖/橙强调属于目标空间 | 巨型墙面细节、雾层、地面反光、人物衣料真实重量 | 空间低频、脚步长混响、系统声无情绪，切镜跟随尺度变化 | 大场景不是一直用广角；需用中焦让信息落到人，再回广角定权力 | 不照搬科幻美术；可转译为医院、档案馆、法院或地下设施 |

## 6. Color-Script Payoff / 色彩作为证据与回收

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| CP01 | `Vertigo` - green identity return | watch + room/threshold + character behind + colored practical/body + slow apparition | 0-4秒中性房间；4-8秒门口绿光进入；8-12秒人物穿过绿区；12-15秒肤色恢复但衣物保留绿边 | 门口色区是身份阈限，人物移动完成颜色归属变化 | 固定中景转缓慢靠近，颜色变化先于脸部确认 | 绿色来自门外霓虹/实用光，雾化柔光塑造记忆质感 | 光在皮肤、发丝、墙面和空气层上的不同响应 | 环境声收窄，脚步进入色区时音乐/音色变化 | 强调色首次出现要绑定身份，回收时重新定义身份 | 不把整片染绿；强调色必须有主人、来源和叙事时机 |
| CP02 | `The Sixth Sense` - red threshold object | cross threshold + domestic/institutional room + audience ahead + object/color + delayed recognition | 0-3秒低饱和正常空间；3-7秒红色物件进入边缘；7-11秒角色靠近但未触碰；11-15秒红色与规则反馈同时成立 | 红物件只占小面积，放在门、把手、衣物或祭物等阈限位置 | 中焦稳定构图，切近景由角色注意到红色触发 | 主体色压低，红色保持明确饱和和实物来源 | 漆面、织物、金属对红光/红色材质的真实反射 | 环境底噪在注意到红色时轻减，接触声成为剪点 | 少量强调色可作为“规则将启动”的证据 | 不把红色当通用恐怖滤镜；出现次数需有回收逻辑 |
| CP03 | `Black Swan` - white/black/red identity progression | perform + rehearsal/stage + unreliable self + costume/body/color + escalation | 0-3秒白色基准；3-7秒黑色从背景/服装侵入；7-11秒镜面中黑色比例增加；11-15秒一处红色身体/道具痕迹成为越界点 | 服装色、镜面背景和身体位置共同推动身份变化 | 近身广角与镜面中景保持身体连续 | 冷白排练光，黑色吞并背景，红色只在崩裂节点出现 | 羽毛/布料、汗、粉妆、镜面污迹提供实物色差 | 音乐拍点、呼吸和衣料声同步颜色占比变化 | 色彩剧本要沿角色状态递进，而非每镜随机调色 | 不复制芭蕾符号；可转译为制服、睡衣、工牌或房间陈设 |
| CP04 | `Memento` - black-white and color convergence | search + motel/evidence space + unreliable memory + medium/color structure + structural convergence | 0-4秒黑白证据动作；4-8秒彩色结果片段；8-12秒同一物件在两种媒介中出现；12-15秒两条色彩线在物件动作上接合 | 同一物件位置和手势维持两条时间线可比性 | 相近机位和焦段让色彩成为结构变量 | 黑白保留纸面/皮肤灰阶，彩色压低饱和，交汇处曝光连续 | 拍立得显影、纸张、墨迹、皮肤纹理跨媒介一致 | 声音桥和动作匹配连接两条色彩线 | 色彩差异可承担时间/认知规则，最终必须有交汇证据 | 不只写“黑白代表过去”；每条色彩线要有独立信息功能 |
| CP05 | `Ex Machina` - glass coolness and red alert state | test + glass institution + system knows more + light/system + abrupt rule shift | 0-3秒冷白透明空间；3-7秒系统声出现；7-10秒红色应急光逐区点亮；10-15秒人物与出口被红区重新分隔 | 玻璃格网先建立自由幻觉，红光状态把格网变成牢笼 | 对称中广角，状态变化时保持机位让观众比较同一空间 | 冷白/蓝灰基准，红色由应急灯实际投射，反射多层但方向统一 | 玻璃反射、金属边缘、皮肤混色、灯具点亮顺序 | 系统提示音先行，电锁和低频随红光区域推进 | 光色变化应改变空间权限和行动路线 | 不写无来源全屋变色；点亮顺序必须对应系统控制区 |
| CP06 | `Parasite` - upper warmth to lower cold/wet descent | flee + vertical city/house + audience ahead + weather/architecture/color + continuous descent | 0-3秒上层暖室内；3-7秒冲入冷雨；7-11秒下行路灯转绿灰；11-15秒低处室内只剩浑浊实用光 | 每次下楼都减少暖色面积，人物在画面中逐渐变小 | 广角下行跟随与固定台阶远景交替，方向始终向下 | 暖木色→冷蓝雨→绿灰地下，颜色由真实地点和天气产生 | 湿衣重量、水流、路面反射、混凝土、灯具色差 | 雨声扩大、脚步变重、排水声进入，转场跟随下行动作 | 色彩变化与社会/空间高度绑定才有叙事力量 | 不用渐变滤镜代替真实光源和材质变化 |
| CP07 | `The Ring` - blue-green media contamination | watch + room/screen + audience ahead + screen/moisture/color + slow spread | 0-3秒中性房间；3-7秒屏幕蓝绿光照到脸；7-11秒相同色进入墙面/水汽；11-15秒屏幕关闭后残色仍留在环境 | 屏幕先是局部色源，随后环境材质接管这种颜色 | 中景人物与屏幕同框，近景记录残色和潮湿表面 | 低饱和蓝绿、偏冷高光、湿黑位，色彩绑定媒介与水 | CRT刷新、玻璃反射、潮墙、冷皮肤、空气湿度 | 电流噪声、磁带机械声和滴水逐层融合 | 让媒介颜色从屏幕扩散为现实污染 | 不把所有夜戏统一蓝绿；只有受媒介影响的区域继承颜色 |
| CP08 | `Gone Girl` - warm domestic image versus cold public image | perform + home/media space + audience ahead + screen/object/color + contrast montage | 0-3秒暖家庭表面；3-7秒切冷新闻/调查画面；7-11秒同一人物在两种色域中表情不同；11-15秒一个家中物件进入公共画面 | 家庭画面亲近、媒体画面平整，构图差异强化表演身份 | 家庭中焦带浅景深，媒体画面更正、更平、更冷 | 暖钨丝与冷屏幕/新闻光分属私人和公共叙事 | 家居磨损、屏幕扫描、妆发差异、相片表面 | 电视声J-cut进入家庭，快门/记者声成为身份切换剪点 | 两套色彩可以表现同一关系的私人版和公共版 | 不把暖色自动等于真诚；色彩归属需要被剧情反转检验 |
| CP09 | `Blade Runner 2049` - orange Las Vegas information zone | approach + monumental ruin + system knows more + atmosphere/color/architecture + slow reveal | 0-4秒冷基准空间；4-8秒橙尘逐渐覆盖远景；8-12秒人物进入橙色体积光；12-15秒目标轮廓从同色背景中分离 | 颜色先吞没尺度，再通过轮廓和运动释放目标 | 超广景到中广景缓慢推进，焦段变化克制 | 橙色来自尘埃/日光散射，阴影保留褐黑层次，非平面滤镜 | 空气颗粒、墙面风化、衣料沾尘、光束衰减 | 低频空间声与风沙，目标动作发出第一处清晰近声 | 单一色域可定义“进入另一套信息规则的区域” | 不直接照搬橙雾科幻城；需给当前场景合理介质来源 |
| CP10 | `The Shining` - hotel warmth and red rupture | move + hotel/room + audience ahead + architecture/color + repetition then rupture | 0-4秒暖木色和饱和地毯建立秩序；4-8秒重复走廊保持色彩规则；8-12秒红色面积突然扩大；12-15秒切回暖空间但红色小物残留 | 对称秩序让颜色重复可记，红色扩张成为结构破口 | 广角中心构图保持可比较，红色节点可用更近景但不改轴 | 暖黄/木色基准，红色由门、墙、衣物或液体材质承担 | 地毯纤维、木墙反射、灯具色温、红色表面质地 | 稳定空间底噪在红色扩张时被单一声响切开 | 颜色破坏必须建立在长期稳定色彩秩序上 | 不堆满红色装饰；先让观众记住正常比例，再改变比例 |

## 7. Performance-To-Edit Causality / 微动作直接触发运镜与剪点

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| PE01 | `The Silence of the Lambs` - Clarice meets Lecter | question + institutional threshold + character behind + gaze/face + reaction-first | 0-3秒走廊主观接近；3-6秒对方已直视镜头；6-10秒主角眼神短停；10-15秒切更近的人脸权力反转 | 玻璃/栏杆分隔身体，直视镜头夺取观众位置 | 稳定中近景到特写，切镜由眼神接触而非台词句号触发 | 冷中性机构光，脸部细节清楚，背景压暗 | 玻璃反光、墙面硬质、呼吸和眼球湿润度 | 脚步停下、环境声变窄、第一句前的吸气成为剪点 | 微动作先改变权力，再改变景别 | 不让所有台词都直视镜头；只给掌控视线的一方 |
| PE02 | `No Country for Old Men` - coin-toss counter scene | test + counter/table + audience ahead + coin/hand/face + delayed rupture | 0-3秒硬币进入桌面；3-7秒对方仍不理解；7-10秒手指压住硬币；10-15秒吞咽后才切近脸 | 硬币位于双方之间，后方出口可见但距离遥远 | 固定中景维持礼貌表面，物件微距和反应特写由手停/吞咽触发 | 普通日光与店内实用光，中性色，物件金属高光明确 | 硬币旋转阻尼、柜台划痕、包装塑料、喉结动作 | 硬币声清晰，空调底噪持续，吞咽声触发反应切镜 | 物件动作可以替代威胁台词并决定剪点 | 不复制硬币命运规则；换成当前故事中真正有选择权的物件 |
| PE03 | `Zodiac` - basement realization | search + basement + audience/character同步 + gaze/sound + slow realization | 0-4秒普通交谈；4-8秒一句信息改变判断；8-11秒人物目光越过对方看向楼梯；11-15秒脚尖转向出口后才切楼梯 | 对话者在前景，出口处于人物视线的背景角落 | 中焦稳定对话，极慢推在目光偏移后开始，切镜跟脚尖转向 | 暖暗地下室光，楼梯口较冷，木墙阴影保留纹理 | 楼板声、潮木、衣料、脚掌重心变化 | 楼上轻响先行，句尾不切，等目光和脚转向才切出口 | 认知变化要经过眼睛→脚→镜头，而非立刻配恐怖音乐 | 不使用突发巨响；危险感来自出口距离被重新计算 |
| PE04 | `Get Out` - teacup hypnosis | persuade + sitting room + character behind + spoon/body + rhythmic capture | 0-3秒勺子规律碰杯；3-7秒手指停止小动作；7-10秒眼睛失焦；10-15秒身体后仰，镜头同步拉开主观空间 | 杯子处于前景声源位，人物被椅背和房间线条固定 | 杯子近景、面部中近景、主观空间变化按身体失控顺序发生 | 暖室内表面正常，杯面高光与眼睛反光成为联系 | 陶瓷、金属、椅布受力、泪液、手指僵住 | 勺碰声稳定拍点，呼吸被压低，手停是进入主观镜头的剪点 | 声音→手部→眼神→身体→镜头，因果链必须完整 | 不只写“被催眠”；每层表演和摄影变化需由上一层触发 |
| PE05 | `Marriage Story` - apartment argument escalation | argue + home room + equal knowledge + hand/distance/object + delayed rupture | 0-3秒两人隔家具说话；3-7秒一人走近，另一人后退；7-11秒手势扩大并碰到墙/物；11-15秒声音破裂后镜头停在听者反应 | 家具和门划定安全距离，距离坍塌比景别变化更重要 | 中景跟随站位，近景只在身体越界和声音破裂后出现 | 自然暖室内光，各机位随真实窗/灯方向变化 | 墙面接触、衣料褶皱、手掌发红、室内生活杂物 | 抢话、呼吸、脚步、碰墙声构成升级；最痛一句后留半拍不切 | 切镜应由关系动作触发，不按每句台词机械正反打 | 不把争吵全程拍成高声；必须有压抑、升级、失控和余波 |
| PE06 | `Prisoners` - interrogation pressure | question + interrogation room + character ahead + table/hand/body + distance collapse | 0-3秒桌面边界；3-6秒提问者前倾；6-10秒手掌压桌，物件轻震；10-15秒对方仍不回应，切提问者失控呼吸 | 桌子、玻璃或椅背维持制度边界，身体越界显示失控 | 50-85mm中近景，推近只随身体越过边界，反应镜头保持更稳 | 冷荧光顶光，皮肤疲惫、桌面高光硬，背景灰绿 | 指节、桌面震动、汗、衣袖摩擦、椅脚位移 | 手掌撞桌触发切镜，随后音乐退让给呼吸和灯噪 | 拍施压者失控比拍被施压者害怕更有权力变化 | 避开暴力展示；重点保留距离、手部和制度空间破裂 |
| PE07 | `Decision to Leave` - interrogation intimacy through gaze | question + office + hidden relation + gaze/reflection/phone + slow seep | 0-3秒程序化问答；3-7秒对方目光停在小动作；7-11秒主问者无意识靠近屏幕/玻璃；11-15秒背景同事停手触发关系暴露切镜 | 两人通过屏幕/玻璃同框，实际距离与视觉距离矛盾 | 中焦静观，拉焦从工作动作到凝视，再切背景见证者 | 冷办公室光与屏幕局部色，肤色克制 | 玻璃指纹、手机反光、咖啡水痕、眼睑微动 | 键盘停声比对白更醒目，停声触发切到第三人 | 关系变化可由凝视时间和第三人察觉完成 | 不让暧昧靠柔焦和音乐说明；必须有工作流程被打断的证据 |
| PE08 | `A Separation` - doorway argument and document action | argue + threshold + equal ignorance + paper/hand/door + overlapping realism | 0-3秒门内外同时说话；3-7秒文件被递出又收回；7-11秒一只手扶门防止关闭；11-15秒手松开，门开始回弹并触发切镜 | 门框持续分割双方，文件和手在边界上争夺 | 手持中景保持多人可见，文件近景只在所有权改变时切入 | 混合自然光，普通生活色，曝光随门开合轻变 | 文件折痕、门铰链阻力、手掌压痕、鞋尖卡门 | 抢话不中断环境声，纸/门声提供清晰动作剪点 | 让物件和阈限承担争执逻辑，可避免纯台词混乱 | 不追求完全干净对白；保留可听懂的重叠和动作优先级 |
| PE09 | `Inglourious Basterds` - farmhouse polite interrogation | persuade + table/hidden floor + audience ahead + food/pipe/reaction + long delay | 0-3秒礼貌用餐动作；3-7秒问题落下但主人继续喝；7-11秒杯子放下时手微抖；11-15秒对方换大物件/姿态占领画面 | 桌面礼物与地板隐藏空间形成上下两层信息差 | 中广角维持礼貌距离，物件近景和汗/手反应由停顿触发 | 柔日光和木屋暖色表面正常，阴影保留地板未知区 | 牛奶杯、木桌、烟、皮肤汗、地板缝隙 | 饮用、放杯、点火声拉长等待，音乐延后进入 | 礼貌动作越完整，微小失控越显眼 | 不照搬台词、身份和标志性道具；替换为当前人物关系物件 |
| PE10 | `The Invitation` - suspicion shifts after a phone/door clue | watch + dinner home + hidden third party + phone/door/listener + reaction-first | 0-3秒聚会正常进行；3-6秒手机/门口信息出现；6-10秒主角停止跟随谈话；10-15秒目光确认出口后，镜头才移到门边人 | 主谈话留在中景，线索从边缘进入，其他人继续社交 | 固定群像中先让表演偏离，再用受控摇移揭示原因 | 暖聚会灯光保持，门口冷暗作为可疑区但不过度强调 | 手机屏幕、酒杯水迹、门锁、衣物细节、背景人动作 | 谈笑底噪不断，手机振动/门响触发主角微反应和镜头转向 | 先拍“谁停止正常行为”，再拍使其停止的线索 | 不让所有人同时安静看线索；信息差需要背景继续正常 |

## 8. Foreground-Background Dual Narrative / 前景主戏与背景第二叙事

| ID | Counterpart fragment | Five-axis fingerprint | 4-30秒重排入口 | 构图/调度 | 机位/镜头 | 光影/色彩/质感 | 实拍证据 | 声音/剪点 | 可借机制 | 边界 |
|---|---|---|---|---|---|---|---|---|---|---|
| FB01 | `Rear Window` - observer and multiple windows | watch + room/courtyard + audience ahead + background people/architecture + scan rhythm | 0-3秒前景观察者；3-7秒焦点/视线到第一扇窗；7-11秒第二扇窗动作与主线形成反差；11-15秒回前景反应 | 前景人物只占边缘，窗格组成多个可读小舞台 | 固定观察位，中长焦选择窗口，摇移遵循视线链 | 不同窗内实用光建立各自生活，前景较暗 | 窗框、玻璃反光、窗帘、远距人物尺度、室内层次 | 城市底噪连贯，不同窗口有局部声提示但不全知 | 一张画面可让背景人物提供证据、反差和时间流逝 | 不让十个窗口同时抢戏；一次只激活一个主背景动作 |
| FB02 | `It Follows` - slow figure in ordinary background | move/wait + street/school + audience ahead + background body + slow approach | 0-3秒主角正常行动；3-7秒远处人物沿直线进入；7-11秒前景同伴遮挡又放出；11-15秒主角仍未知，背景距离明显缩短 | 主体偏侧给背景路线留负空间，威胁保持小但方向明确 | 中广角或中焦固定观察，镜头不主动放大威胁 | 普通日光/室内光，异常不靠色调提示 | 行人步态差异、地面尺度、前景遮挡、自然光变化 | 环境声正常，稳定低频提示观众持续扫描 | 观众先发现的背景动作必须有可测距离变化 | 不让背景人物瞬移或突然加速；威胁来自坚持同一方向 |
| FB03 | `Parasite` - table/sofa hiding with normal life above | hide + living room + audience ahead + furniture/body + sustained split | 0-3秒前景主人正常谈话；3-7秒家具下背景手指缓慢收回；7-11秒液体/物件接近藏身处；11-15秒前景笑声继续，藏者屏住呼吸 | 家具边缘横切画面，上层生活与下层藏身同时可读 | 低机位中广角保持双层，不频繁切到藏者全脸 | 上层暖光，下层暗但保留皮肤/地面细节 | 地板灰尘、桌布、杯中液体、身体受压、呼吸造成布料微动 | 对话和餐具在上层，近距离呼吸/衣料在下层，声音透视分开 | 主戏可保持正常，背景小动作承担生死压力 | 不用背景夸张挥手；动作幅度必须符合被发现风险 |
| FB04 | `Children of Men` - long-take danger around the subject | flee + vehicle/street + equal ignorance + crowd/environment + continuous movement | 0-3秒主体目标明确；3-6秒前景路人/物体擦镜；6-10秒背景事件升级并影响路线；10-15秒主体被迫改变动作 | 主体不是永远居中，前中后景事件按距离依次影响他 | 广角长镜跟随，摄影机被环境迫使改位但保持方向 | 自然/实用光与脏空气，颜色克制，真实曝光变化 | 碎屑、泥水、车体、衣料、群众碰撞和镜头污染痕迹 | 多层环境声按距离进入，撞击/呼喊触发转向而非随机抖动 | 长运镜的新鲜感来自环境不断改变主体任务 | 不用无关群众动作填满画面；背景事件必须改变路线或判断 |
| FB05 | `The Lives of Others` - private scene with unseen institutional listener | talk + apartment/attic + audience ahead + listener/equipment + parallel stillness | 0-3秒前景私人谈话；3-7秒切/构图带出楼上监听手；7-11秒楼下一个词让监听者停笔；11-15秒回楼下，人物不知道已改变第三人 | 私人空间与监听空间通过建筑垂直关系和同一台词连接 | 两个稳定机位，焦段相近，剪镜由监听者动作而非发言者句号触发 | 楼下暖、楼上冷暗，色差表示生活与制度 | 天花板、线缆、纸笔、耳机、房间空气质感 | 同一句话跨两空间，墙体过滤与耳机近声并存 | 背景/异空间角色可以被主场台词改变，从而形成第二叙事 | 不把监听者写成纯功能NPC；给其一次可见价值判断动作 |
| FB06 | `Cure` - ordinary room with peripheral behavioral anomaly | wait + ordinary room + audience uncertain + background body/object + slow seep | 0-4秒前景正常问答；4-8秒背景人物重复小动作；8-12秒前景继续说话，重复动作频率改变；12-15秒主角终于看向背景 | 主谈话居中偏正常，异常留在边缘并有完整动作空间 | 固定中广角，极少推移，观众可自行扫描 | 平淡日常光，低饱和旧表面，不做明显恐怖光 | 墙面褪色、桌椅磨损、衣物、反复触碰留下的物理痕迹 | 房间底噪持续，重复物件声逐渐从背景进入注意层 | 背景异常先存在一段时间，再被角色承认 | 不用闪烁灯或音效标记异常；靠频率和行为逻辑破坏正常 |
| FB07 | `Burning` - foreground conversation with absent-object pressure | talk + room/landscape + audience behind + absence/background space + slow ambiguity | 0-3秒前景对话；3-7秒构图保留一个空位/空屋；7-11秒对方目光短暂越过主角；11-15秒风/门帘动，缺席仍无解释 | 空位、窗外或远处建筑占稳定负空间，人物不遮住它 | 中长焦静观，焦点可短暂落到空处但不揭示答案 | 黄昏/朴素自然光，空气层和低饱和材质 | 门帘、尘、草、空椅使用痕迹、远景热浪 | 对话间隙保留风和远声，缺席物不配专门恐怖音 | 背景的“没有”可以持续给对话施压 | 不用空镜直接宣布失踪；保持多种解释可能 |
| FB08 | `Caché` - fixed house image becomes evidence | watch + exterior house/screen + audience uncertain + architecture/background passerby + repetition-change | 0-4秒固定住宅全景；4-8秒普通路人经过；8-12秒画面似乎无事但一处门窗状态变化；12-15秒切观看者反应确认它是被观看影像 | 建筑占据大部分画面，人物极小，时间通过日常经过留下 | 完全固定远景，后切室内观看位置形成屏中屏 | 自然平光、录像质感与现实质感存在轻微差异 | 车流、树影、门窗、录像噪点、屏幕反射 | 街声平稳，录像回放设备声进入后改变观看属性 | 重复固定画面用一个可验证差异制造监视压力 | 不无限延长静帧；短剧版在4秒内必须出现可读变化或观看反应 |
| FB09 | `Get Out` - garden party background gazes and interruptions | talk + crowd/garden + audience ahead + NPC gaze/object + social layering | 0-3秒前景寒暄；3-6秒背景一人停止笑；6-10秒另一人绕路靠近主角；10-15秒前景问题结束时背景人已封住退路 | 前景对话清楚，背景NPC沿主角退路分布，视线交叉 | 中焦群像，轻横移保持前景讲话者同时释放背景路线 | 正常日光与自然肤色，异常来自行为同步 | 酒杯液面、树影、衣料风动、人物经过遮挡 | 谈笑底噪、杯声、背景问候交错；一次集体静默作为风险升级 | 对话戏背景人物要改变空间，不只站着听 | 不让全部NPC同一秒看主角；分批动作更真实也更压迫 |
| FB10 | `Decision to Leave` - foreground task and reflected relationship clue | search/talk + office/mountain/phone + hidden relation + reflection/background task + focus route | 0-3秒前景执行工作；3-7秒反射中出现另一人；7-11秒背景任务继续但节奏变慢；11-15秒焦点回前景，人物已经改变握物方式 | 前景物件、人物、反射/屏幕形成三层因果链 | 中焦受控构图，拉焦遵循物件→反射→手部反应 | 冷中性现实光，反射色略偏但保持来源 | 玻璃、手机、纸面、手指压力、远景空气层 | 工作声持续，反射人物动作不单独配音，手部声音变化触发回焦 | 背景关系信息应落回前景身体动作形成闭环 | 不让反射只做漂亮构图；它必须改变当前任务的执行方式 |

## 9. Retrieval Output Contract

For a new scene or visual request, output the scheme pool in this order:

```text
场景五轴指纹：A / B / C / D / E
当前故事任务/目标时长：
候选1：film scene + useful visual mechanisms + replacement variables + strength/failure boundary
候选2：film scene + useful visual mechanisms + replacement variables + strength/failure boundary
候选3-6：same format
导演排序：rank candidates and state possible combination roles without merging them prematurely
```

After the user approves one option or a combination, state the unifying director grammar and build a newly timed current-segment storyboard. Do not report film locations or exact time ranges by default.

## 10. Training Deposit

This atlas promotes six previously thin layers into active retrieval:

- multi-character alliance blocking.
- spatial sound perspective across cuts.
- lens-behavior continuity.
- color-script payoff.
- performance-to-edit causality.
- foreground-background dual narrative.

Each layer contains ten mechanism-different film fragments and an AIGC-compatible 15-second compression skeleton.
