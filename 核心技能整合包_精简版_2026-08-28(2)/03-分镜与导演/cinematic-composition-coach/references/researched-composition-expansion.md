# Researched Composition Expansion

Created: 2026-06-25

Purpose: web-researched expansion pack for movie-level composition training. Use this file when the user asks for "影评最佳构图", "上网搜构图", "电影神级构图", or wants new case samples for GPT/SD/Seedance prompt training.

Source policy: links are kept as research anchors. Convert film references into visible composition language before using them in prompts.

## Source Index

- Citizen Kane / Gregg Toland / ceilinged sets: https://theasc.com/article/realism-for-citizen-kane/
- Barry Lyndon / John Alcott / candlelight and painterly images: https://theasc.com/article/flashback-barry-lyndon/ and https://www.criterion.com/films/29008-barry-lyndon
- Lawrence of Arabia / Ali entrance and desert scale: https://cinematyler.com/archives/814 and https://bscine.com/bsc-members/?id=416
- The Third Man / Dutch angle: https://www.propellermag.com/Jan2016/WellesThirdManJan16.html
- The Searchers / doorway ending: https://blog.filmmuseum.at/an-iconic-image/
- Parasite / class through light, height, blocking: https://www.filmmakersacademy.com/look-of-parasite/
- Stalker / tunnel slow move: https://chehubbardartist.wordpress.com/2016/08/25/film-shot-deconstruction-tunnel-shot-from-andrei-tarkovskys-stalker/
- In the Mood for Love / frame-within-frame and constricted spaces: https://offscreen.com/view/wong-kar-waias-in-the-mood-for-love-2000-postmodern-melodrama
- Children of Men / long-take tension: https://nofilmschool.com/children-of-men-long-take
- No Country for Old Men / darkness, stillness, silence: https://nofilmschool.com/3-ways-no-country-old-men-builds-tension
- There Will Be Blood / oil derrick fire: https://theasc.com/article/there-will-be-blood-cinematography-robert-elswit/
- Hero / color-segment narrative: https://offscreen.com/view/hero

## Case R1 - Citizen Kane / Low-Angle Ceiling Power And Deep-Focus Space

**叙事层**
- 情绪基调：权力、压迫、上升欲望、制度空间的沉重感。
- 人物关系：人物处在巨大室内权力空间里，观众仿佛被压在低处观看。
- 剧情节点：适合表现权力人物扩张、谈判、孤独掌权、空间吞人。
- 叙事功能：可见天花板让室内不再像舞台布景，而像一个封闭权力盒；低机位把人物和建筑一起压向观众。

**视觉层**
- 景别：中远景到全景，人物与完整室内空间同框。
- 机位：低机位仰拍，镜头接近地面或低于胸口高度。
- 构图法则：深焦构图、低机位权力构图、天花板封闭框架、前中后景多层叙事。
- 光影：高反差黑白，地面或侧向硬光塑造人物轮廓；天花板存在感增强封闭性。
- 色彩：黑白高反差，暗部厚重，亮部集中在人物脸、窗、桌面。
- 画面层次：前景桌椅/地面，中景人物，背景墙面/窗/天花板，三层都要有叙事信息。
- 镜头 / 焦段 / 景深：广角到正常广角，深焦，空间纵深清楚。
- 运动 / 剪辑 / 声音：可静止或缓慢推拉；空间混响、脚步、低声对话强化封闭室内。

**语言层**
- 提示词参考：`low angle deep focus interior, visible ceiling pressing down on the room, powerful figure framed by architecture, high contrast black and white lighting, foreground desk layer, midground character, background windows and ceiling, oppressive power composition`
- 关键词提取：`low angle`, `visible ceiling`, `deep focus`, `power interior`, `foreground-midground-background`, `high contrast black and white`
- AIGC 可见锚点：低机位、天花板入镜、前景桌椅、中景人物、背景窗墙同时清晰。

**复刻与运用**
- 用这个手法的原因：让权力不是靠台词说出来，而是靠空间压迫出来。
- 如何用：把镜头降到人物腰部以下，保留天花板和地面，人物不要只占脸，要和空间一起构成权力关系。
- 适用场景：白塔高层会议、共研会审讯室、江赝权力空间、父权/资本/机构压迫。
- 风险与反例：只仰拍脸会变成普通英雄角度；没有天花板和深焦层次就失去"空间压人"。

**沉淀条目**
- 可复用规则：低机位不是只为了显高，必须让天花板、地面、墙体一起入镜，形成权力空间的封闭盒。

## Case R2 - Barry Lyndon / Candlelight Painterly Tableau

**叙事层**
- 情绪基调：古典、衰败、虚荣、命运缓慢冷却。
- 人物关系：贵族人物被礼仪、身份、烛光和室内陈设固定成画中人。
- 剧情节点：晚宴、谈判、婚姻、贵族仪式、人物命运转折前的静态压抑。
- 叙事功能：让人物看似高贵，实际被历史与阶级陈设冻结。

**视觉层**
- 景别：中景、全景、桌边群像。
- 机位：平视，端正，少移动，像观看油画。
- 构图法则：古典三角构图、桌面横向层次、烛台前景框架、人物静态摆位。
- 光影：烛光作为主光，暖色点光源近距离照亮脸和手，背景迅速坠入暗部；侧光比正面光更有体积。
- 色彩：琥珀、褐色、奶油白、暗红，低饱和暖色。
- 画面层次：前景蜡烛火焰，中景人物脸/手，背景深暗墙面和织物。
- 镜头 / 焦段 / 景深：正常焦段到轻微长焦，浅景深或中等景深；人物边缘柔。
- 运动 / 剪辑 / 声音：静态长镜头，火焰轻抖，餐具、衣料、轻声交谈。

**语言层**
- 提示词参考：`18th century candlelit interior tableau, faces illuminated only by warm candles, painterly old master composition, dark background falloff, foreground candle flames, aristocratic stillness, amber brown cream palette, soft low-key light`
- 关键词提取：`candlelight`, `old master painting`, `warm falloff`, `foreground candles`, `aristocratic tableau`
- AIGC 可见锚点：蜡烛必须在画面内，脸离蜡烛近，背景暗，不用现代顶灯。

**复刻与运用**
- 用这个手法的原因：让时间感、阶级感、命运感同时存在。
- 如何用：把光源放进画面，让人物被有限光包住，周围道具只保留软暗轮廓。
- 适用场景：仪式对话、婚戒店复古高光、贵族/资本晚宴、命运计划启动前的静态场。
- 风险与反例：把画面整体照亮会失去烛光逻辑；过多锐利细节会破坏油画感。

**沉淀条目**
- 可复用规则：烛光构图的重点不是"暖"，而是光源可见、照亮范围有限、人物像被时代固定在一幅画里。

## Case R3 - Lawrence Of Arabia / Desert Mirage Negative Space

**叙事层**
- 情绪基调：史诗、等待、未知来临、人在自然中的渺小。
- 人物关系：近处人物等待，远处人物像命运从地平线出现。
- 剧情节点：沙漠会面、陌生人登场、旅程进入新阶段。
- 叙事功能：用长时间距离感让登场变成神话，而不是普通人物走入画面。

**视觉层**
- 景别：极远景到远景。
- 机位：低平视，贴近地平线。
- 构图法则：极端负空间、地平线构图、远处小点主体、三角视线引导。
- 光影：强烈自然日光，热浪/海市蜃楼让远处主体变形。
- 色彩：沙黄、浅蓝、白光，高亮低阴影。
- 画面层次：前景沙地/水井边缘，中景等待者，背景地平线小黑点。
- 镜头 / 焦段 / 景深：长焦压缩距离，热浪压平空间；或宽银幕远景强调荒漠尺度。
- 运动 / 剪辑 / 声音：漫长等待、风声、马/骆驼远音，剪辑节奏慢。

**语言层**
- 提示词参考：`vast desert negative space, tiny distant rider emerging from heat haze on the horizon, low eye-level camera, extreme wide shot, sun-bleached sand and pale sky, mythic entrance, long-lens flattened mirage`
- 关键词提取：`vast negative space`, `tiny horizon figure`, `heat haze`, `mythic entrance`, `extreme wide shot`
- AIGC 可见锚点：主体必须小到接近地平线一点；画面大部分留给沙漠和天空。

**复刻与运用**
- 用这个手法的原因：把"来者是谁"变成观众身体上的等待。
- 如何用：先给空旷地平线，远处一点缓慢变大，不急着切近景。
- 适用场景：清宴从未来残景中出现、江赝势力远处压来、荒芜未来世界建立。
- 风险与反例：人物一开始太大，会失去等待；镜头频切会破坏神话感。

**沉淀条目**
- 可复用规则：史诗登场要让距离先表演，人物不是出现，而是从地平线被时间慢慢交给观众。

## Case R4 - The Third Man / Dutch Angle Moral Dislocation

**叙事层**
- 情绪基调：不安、异乡、道德失衡、城市迷宫。
- 人物关系：人物无法掌控城市，观众也无法获得稳定观看位置。
- 剧情节点：追踪、迷路、怀疑、发现真相前的精神歪斜。
- 叙事功能：让画面本身失去水平线，观众从视觉上感觉秩序已经坏掉。

**视觉层**
- 景别：街道中景、巷道全景、人物近景都可用。
- 机位：明显倾斜的荷兰角，常结合高反差夜景。
- 构图法则：斜线构图、失衡构图、暗部负空间、街巷引导线。
- 光影：黑白高反差，路灯、窗光、湿地反光制造锋利亮面。
- 色彩：黑白灰，强暗部。
- 画面层次：前景墙角/路灯，中景人物，背景倾斜建筑和街道。
- 镜头 / 焦段 / 景深：正常广角，保留建筑斜线。
- 运动 / 剪辑 / 声音：可静态歪斜或跟拍；脚步回声、空街风声、远处音乐。

**语言层**
- 提示词参考：`black and white noir street, strong dutch angle, tilted buildings, wet pavement reflections, lone suspicious figure in a narrow alley, high contrast street lamp shadows, moral disorientation`
- 关键词提取：`dutch angle`, `tilted buildings`, `noir alley`, `wet reflections`, `moral disorientation`
- AIGC 可见锚点：地平线倾斜、建筑竖线歪斜、人物仍要站稳。

**复刻与运用**
- 用这个手法的原因：把心理失衡转成画面失衡。
- 如何用：只在信息错位或人物世界观崩坏时用，倾斜角度要能被观众感觉到。
- 适用场景：时间线错位、江宴发现短信异常、清宴记忆不对劲、共研会监控视角。
- 风险与反例：滥用会显廉价；普通对话硬歪会变成故弄玄虚。

**沉淀条目**
- 可复用规则：荷兰角必须服务"世界不正"，不是为了酷；最好配合狭窄空间、强阴影和信息异常。

## Case R5 - The Searchers / Doorway Threshold Myth

**叙事层**
- 情绪基调：归来、排斥、文明与荒野分界、英雄孤独。
- 人物关系：屋内属于家庭/文明，屋外属于荒野/漂泊者。
- 剧情节点：开场门打开迎来人物，结尾门关上拒绝人物。
- 叙事功能：用同一个门框完成角色命运闭环：他拯救家庭，却不能回到家庭。

**视觉层**
- 景别：门内向外的远景/全景。
- 机位：室内暗部，平视看向明亮户外。
- 构图法则：框架构图、内外空间对比、剪影/逆光、中心远景。
- 光影：室内黑成天然遮幅，户外高亮；人物站在亮部或门框边缘。
- 色彩：室内黑/褐，室外沙黄/天蓝。
- 画面层次：前景门框黑边，中景人物，背景荒野地平线。
- 镜头 / 焦段 / 景深：正常镜头，门框完整，外景清楚。
- 运动 / 剪辑 / 声音：门开/门关作为转场；外面风声，屋内安静。

**语言层**
- 提示词参考：`dark interior doorway framing a lone figure outside in bright desert landscape, threshold composition, inside world versus outside wilderness, wide shot, strong silhouette border, mythic western loneliness`
- 关键词提取：`doorway frame`, `threshold`, `dark interior`, `bright exterior`, `lone figure outside`
- AIGC 可见锚点：镜头必须在室内，门框四边形成黑框，人物在门外。

**复刻与运用**
- 用这个手法的原因：空间边界直接讲人物归属问题。
- 如何用：让门框占画面前景，不要只拍门；人物越接近门外，越孤立。
- 适用场景：婚戒所门口、白塔入口、客厅门框看到下楼人物、角色被家庭/组织排除。
- 风险与反例：站在门内拍门外但门框不完整，阈限感会弱。

**沉淀条目**
- 可复用规则：门框不是装饰，它是两个世界的边界；人物站在哪一边，就是他属于或不属于哪里。

## Case R6 - Parasite / Class Through Height, Window, And Light

**叙事层**
- 情绪基调：阶级压迫、滑稽下的窒息、生活空间不平等。
- 人物关系：穷人家被半地下空间限制，富人家享受高处、日光和开阔。
- 剧情节点：开场建立贫困空间、角色上升进入豪宅、暴雨后垂直坠落回原处。
- 叙事功能：不靠对白讲阶级，而靠窗户高度、楼梯方向、光线质量让阶级可见。

**视觉层**
- 景别：室内全景、中景、楼梯长镜头。
- 机位：低矮半地下平视；上升/下降楼梯跟拍；豪宅用横向开阔平视。
- 构图法则：垂直阶级构图、小窗框架、横向豪宅开阔构图、楼梯动线。
- 光影：半地下只有短暂、小面积自然光，常用绿荧光/钨丝低端灯；豪宅自然光充足，夜晚暖色高级间接光。
- 色彩：穷人空间偏脏绿、黄、红褐；富人空间偏自然木色、暖白、干净阴影。
- 画面层次：半地下前景杂物，中景人物，背景高处小窗；豪宅前景留白，中景人物，背景大窗庭院。
- 镜头 / 焦段 / 景深：大画幅感，能看宽环境但保持人物隔离。
- 运动 / 剪辑 / 声音：楼梯/雨水/街道高度变化构成叙事；雨声、水流声、灯管嗡鸣。

**语言层**
- 提示词参考：`semi-basement apartment with tiny high window, limited daylight patch, cluttered foreground, greenish fluorescent practical light, family below street level, class divide through vertical composition`
- 关键词提取：`semi-basement`, `tiny high window`, `limited sunlight`, `vertical class divide`, `green fluorescent light`
- AIGC 可见锚点：小窗必须在高处，人物低于窗，室内杂乱且日间仍需开灯。

**复刻与运用**
- 用这个手法的原因：阶级关系变成空间物理关系，观众一眼懂。
- 如何用：低阶层空间拍"向上看外界"；高阶层空间拍"横向拥有风景"。
- 适用场景：白塔上下层级、实验室地下/地上对比、客厅一楼与楼梯入口的权力关系。
- 风险与反例：只写贫富道具不写窗户高度、光线差异，会变成美术陈设而非构图叙事。

**沉淀条目**
- 可复用规则：阶级构图优先写高度和光源，不是先写家具贵不贵。

## Case R7 - Stalker / Tunnel Slow Push Into Uncertainty

**叙事层**
- 情绪基调：未知、潮湿、精神试探、进入禁区。
- 人物关系：角色被隧道吞进去，观众被迫一起前进。
- 剧情节点：穿越危险通道、接近不可知区域。
- 叙事功能：用缓慢推进和暗部深处的人影，让未知不是跳出来，而是慢慢逼近。

**视觉层**
- 景别：隧道远景/中远景。
- 机位：低平视，沿隧道轴线缓慢向前。
- 构图法则：中心透视、黑暗负空间、重复拱/管道、远处人影锚点。
- 光影：暗色为主，局部金色/灰白光斑落在水、根须、墙面上。
- 色彩：暗绿、泥褐、冷灰，低饱和。
- 画面层次：前景湿地/管壁，中景悬挂物和光斑，背景人物几乎融入黑暗。
- 镜头 / 焦段 / 景深：广角慢推，深处保持模糊可辨。
- 运动 / 剪辑 / 声音：长镜头慢推；水滴、脚步、呼吸、石子声。

**语言层**
- 提示词参考：`slow forward camera move through a dark wet tunnel, faint golden light rings, hanging roots catching light, distant human figure fading into blackness, low saturation green brown palette, unsettling negative space`
- 关键词提取：`slow push`, `dark wet tunnel`, `distant figure`, `faint golden light`, `negative space`
- AIGC 可见锚点：远处必须有人影或目标，隧道要有重复结构和湿反光。

**复刻与运用**
- 用这个手法的原因：让观众用时间感受恐惧，而不是靠怪物。
- 如何用：少切镜，让镜头缓慢接近黑暗深处；声效比动作更重要。
- 适用场景：白塔地下通道、时间机器坠落后的残骸入口、记忆/未来片段进入。
- 风险与反例：速度太快会变成探险；灯太亮会失去未知。

**沉淀条目**
- 可复用规则：未知空间的恐惧来自"慢慢靠近看不清的深处"，不是来自快速展示危险。

## Case R8 - Children Of Men / Long-Take Crisis Inside A Moving Box

**叙事层**
- 情绪基调：突发、混乱、无处可逃、现实感压迫。
- 人物关系：一车人从同一目标突然变成互相失控的求生者。
- 剧情节点：路上伏击，关系和任务发生不可逆转折。
- 叙事功能：用连续镜头不让观众抽离，危机像现实一样没有剪辑喘息。

**视觉层**
- 景别：车内近景/中近景，偶尔看出窗外威胁。
- 机位：车内旋转/横移，紧贴人物脸和车窗。
- 构图法则：封闭空间群像、快速视点转移、前后座层次、窗外威胁框架。
- 光影：自然车窗光，外部环境光快速变化。
- 色彩：冷灰、脏绿、道路尘土色，现实低饱和。
- 画面层次：前景椅背/车窗，中景人物脸和手，背景车外路障/攻击者。
- 镜头 / 焦段 / 景深：较广角，近距离拍多人但不夸张变形。
- 运动 / 剪辑 / 声音：长镜头，车身运动、尖叫、枪声、玻璃、刹车、呼吸同时发生。

**语言层**
- 提示词参考：`continuous handheld-like camera inside a moving car, cramped group panic, camera rotating between faces and windshield threat, natural window light, no cut tension, road ambush outside, realistic chaotic sound layers`
- 关键词提取：`continuous take`, `inside moving car`, `cramped group`, `rotating camera`, `window threat`
- AIGC 可见锚点：镜头在车内，人物离镜头近，窗外威胁要可见但不是主画面全景。

**复刻与运用**
- 用这个手法的原因：让危机成为同一空间里的连锁反应。
- 如何用：不要切开解释，每个角色反应和外部威胁在一个镜头内轮流成为焦点。
- 适用场景：车祸前后、逃离共研会、客厅突发时间线变化后的群体混乱。
- 风险与反例：切得太碎会失去真实压迫；只拍外面袭击会丢掉人物关系崩坏。

**沉淀条目**
- 可复用规则：封闭空间危机要让镜头被困在人物中间，威胁通过窗、声音和身体反应侵入。

## Case R9 - No Country For Old Men / Bare-Bones Darkness And Sound Suspense

**叙事层**
- 情绪基调：寂静、等待、死亡逼近、无对白压迫。
- 人物关系：猎人与被猎者互相寻找，但不直接交流。
- 剧情节点：旅馆/街道夜间追杀，角色等待门外威胁靠近。
- 叙事功能：用极少光和极少台词，让观众靠声音、门、窗和阴影判断危险位置。

**视觉层**
- 景别：室内中景、门口近景、走廊/街道远景。
- 机位：静止观察，切换人物、门、窗、阴影。
- 构图法则：暗部负空间、门框威胁、静止等待构图、声音画外空间。
- 光影：街灯/室内小灯提供最低限度可见信息，暗部包围人物。
- 色彩：冷暗夜色、钠灯黄、黑色阴影。
- 画面层次：前景床/门框，中景人物，背景窗外路灯或走廊黑暗。
- 镜头 / 焦段 / 景深：正常焦段，静止，保留门窗位置。
- 运动 / 剪辑 / 声音：节奏放慢；远处蜂鸣、脚步、枪声、呼吸成为主要信息。

**语言层**
- 提示词参考：`dark motel room suspense, man waiting near bed, door and window visible, bare streetlamp light barely revealing key details, huge black negative space, silent cat-and-mouse tension, still camera`
- 关键词提取：`bare lighting`, `dark motel room`, `door suspense`, `sound-driven tension`, `still camera`
- AIGC 可见锚点：门、窗、人物必须同框或连续明确；不要大面积霓虹美化。

**复刻与运用**
- 用这个手法的原因：让观众害怕看不见的空间，而不是看见的反派。
- 如何用：减少对白，建立门窗位置，用声音提示危险移动。
- 适用场景：夜晚白塔潜入、江赝监视、短信发送后环境异变前的停顿。
- 风险与反例：把反派直接拍清楚会削弱悬念；光太漂亮会偏离自然恐惧。

**沉淀条目**
- 可复用规则：悬疑夜景不是越黑越好，而是只照亮门、窗、人物这些判断危险所需的信息。

## Case R10 - There Will Be Blood / Oil Derrick Fire As Hellish Capital

**叙事层**
- 情绪基调：贪婪、失控、工业地狱、财富与灾难同源。
- 人物关系：人物面对自己创造的工业怪物，利益与危险同时爆发。
- 剧情节点：油井喷发燃烧，资本欲望以灾难形式显现。
- 叙事功能：火焰不是背景灾难，而是人物欲望的可见化。

**视觉层**
- 景别：远景/全景到中远景。
- 机位：低平视或侧面远观，让油井火柱占据主视觉。
- 构图法则：巨大火柱垂直构图、人物剪影尺度对比、工业结构框架。
- 光影：火焰作为主光，橙色强光照亮烟雾和人物轮廓，周围黑夜吞没细节。
- 色彩：黑、橙、烟灰、油污褐。
- 画面层次：前景泥地/人物，中景井架结构，背景火柱和烟。
- 镜头 / 焦段 / 景深：宽幅远景，多机位可捕捉危险动作；主构图应保留火柱完整高度。
- 运动 / 剪辑 / 声音：火焰轰鸣、木架爆裂、奔跑、工业低频。

**语言层**
- 提示词参考：`night oil derrick explosion, towering orange fire geyser engulfing wooden industrial structure, small silhouetted workers in foreground, black smoke, hellish capitalism imagery, wide shot, fire as the only key light`
- 关键词提取：`oil derrick fire`, `fire as key light`, `small silhouettes`, `industrial structure`, `black smoke`
- AIGC 可见锚点：火柱要垂直巨大，人物小，井架结构必须清楚。

**复刻与运用**
- 用这个手法的原因：把欲望、灾难、财富统一成一个光源。
- 如何用：让危险光源成为主光，而不是另外打漂亮灯；人物被火照亮/吞没。
- 适用场景：未来战争爆炸、白塔实验失控、江赝科技独裁导致灾难的视觉隐喻。
- 风险与反例：只拍爆炸特效会变成动作场面；必须保留人和工业结构的尺度关系。

**沉淀条目**
- 可复用规则：灾难构图要让灾难成为主光源，人物只是被欲望/火焰照出的剪影。

## Case R11 - Hero / Single-Color Narrative Version

**叙事层**
- 情绪基调：每段颜色代表一种叙述版本和心理立场。
- 人物关系：同一事件在不同人物叙述中被不同色彩重新解释。
- 剧情节点：回忆、谎言、推演、真相层层替换。
- 叙事功能：色彩直接承担叙事可靠性和情绪态度，而不是单纯美术风格。

**视觉层**
- 景别：全景武打、近景对峙、室内/外景均可。
- 机位：端正、仪式化，强调色块纯度和人物位置。
- 构图法则：单色统治、色彩隔离、对称/仪式构图、人物小尺度与布景色块。
- 光影：根据颜色保持统一光质；红段热烈，蓝段冷静，白段清冷，绿段回忆/启蒙。
- 色彩：红、蓝、白、绿、黑等分段，不混色。
- 画面层次：前景服装/布料，中景人物，背景同色建筑/自然景。
- 镜头 / 焦段 / 景深：根据动作可广角或长焦，但色块要干净。
- 运动 / 剪辑 / 声音：同段色彩内保持一致动作韵律和音乐情绪。

**语言层**
- 提示词参考：`single-color narrative sequence, all costumes and environment dominated by deep red, ritual symmetrical composition, two warriors facing each other, color represents emotional version of memory, clean large color blocks`
- 关键词提取：`single color narrative`, `large color blocks`, `memory version`, `ritual composition`, `color-coded truth`
- AIGC 可见锚点：一段只允许一个主色统治，服装、背景、道具共同服务主色。

**复刻与运用**
- 用这个手法的原因：把复杂叙述版本变成观众一眼能识别的颜色规则。
- 如何用：给每个时间线/记忆版本锁不同主色，场景、服装、光影一起统一。
- 适用场景：命运覆写不同世界线、未来预演、谎言/真实对照、记忆覆盖前后。
- 风险与反例：只加滤镜不改服装/场景/光源，会变成廉价调色。

**沉淀条目**
- 可复用规则：色彩叙事不是调色，是把某一段的服装、空间、光源、道具都交给同一种心理颜色。

## Case R12 - In The Mood For Love / Constricted Stairway Passing

**叙事层**
- 情绪基调：暧昧、克制、擦肩错过、欲望被礼法压缩。
- 人物关系：两个人靠得很近，但社会空间不允许他们真正停留。
- 剧情节点：楼梯/走廊反复相遇，关系在重复中升温。
- 叙事功能：狭窄楼梯让相遇成为身体上的必经，但也让亲密无法展开。

**视觉层**
- 景别：中景、中近景。
- 机位：楼梯侧面或转角偷窥式机位。
- 构图法则：框中框、垂直门廊/楼梯框架、身体遮挡、狭窄负空间。
- 光影：单盏顶灯或墙灯，暖色小范围照亮，周围暗。
- 色彩：暗红、黄、褐、绿色点缀，复古高密度。
- 画面层次：前景墙角/楼梯扶手，中景人物擦肩，背景暗楼梯/走廊。
- 镜头 / 焦段 / 景深：中长焦压缩狭窄空间，浅景深让偷窥感更强。
- 运动 / 剪辑 / 声音：慢速上下楼，衣料摩擦，脚步，音乐循环。

**语言层**
- 提示词参考：`narrow 1960s apartment stairway, man and woman passing each other closely without touching, warm overhead lamp, frame within frame, compressed vertical space, restrained romantic tension, dark red brown palette`
- 关键词提取：`narrow stairway`, `passing without touching`, `warm overhead lamp`, `frame within frame`, `restrained tension`
- AIGC 可见锚点：楼梯必须窄，人物只是擦肩，不要拥抱；前景墙/扶手遮挡。

**复刻与运用**
- 用这个手法的原因：让空间替人物表达克制。
- 如何用：把人物动线设计成必须靠近，但镜头和遮挡不允许他们完全同框舒展。
- 适用场景：小蝶清宴微妙亲密、江宴苏灵鸳旧关系闪回、婚戒所走廊擦肩。
- 风险与反例：空间太宽会失去压缩；人物直接拥抱会破坏克制。

**沉淀条目**
- 可复用规则：暧昧不是靠靠近，而是靠"被空间迫近却不能停留"。

## Cross-Case Technique Summary

1. 权力空间：低机位 + 天花板 + 深焦，适合机构压迫。
2. 古典命运：可见烛光 + 暗背景 + 静态摆位，适合仪式/贵族/命运感。
3. 史诗登场：极远景 + 负空间 + 地平线等待，适合神话化人物出现。
4. 精神失衡：荷兰角 + 夜景强反差 + 倾斜建筑，适合真相错位。
5. 阈限命运：门框内外明暗对比，适合归属/排斥/进入另一个世界。
6. 阶级叙事：高度 + 窗户 + 光线质量，适合社会关系可视化。
7. 未知空间：慢推 + 隧道 + 远处黑暗人影，适合心理恐惧。
8. 封闭危机：长镜头困在人物中间，威胁从窗和声音侵入。
9. 极简悬疑：只照亮判断危险所需的信息，其他交给黑暗和声音。
10. 灾难欲望：让灾难成为主光源，人物成为被照出的剪影。
11. 色彩叙事：一段一个主色系统，不能只靠滤镜。
12. 情感克制：狭窄空间让人靠近，社会规则让人不能停留。

## Corrective Training - Scale, Light Control, Hero Entrance, And Danger Staging

Created: 2026-06-25

Reason: the user rejected a ship-pier farewell draft as ordinary and under-composed. The failure diagnosis and new rules below must be applied before generating future farewell, hero entrance, or accident images.

Additional research anchors:

- The Godfather / Gordon Willis exposure, dim interiors, chocolate filters, and precise printing: https://theasc.com/article/the-godfather-on-location-gordon-willis-cinematography/
- Godfather lighting summary and Willis practical/top-light discussion: https://www.indiewire.com/features/general/godfather-50th-anniversary-cinematography-1234712372/
- Avengers assemble / portal scene development and hero-shot pacing: https://en.wikipedia.org/wiki/Avengers_assemble_scene and https://www.slashfilm.com/1771437/marvel-avengers-endgame-portal-scene-original-version/
- Endgame epic battle cinematography challenge: https://nofilmschool.com/avengers-endgame-cinematography-interview
- Children of Men car long take: https://nofilmschool.com/children-of-men-long-take
- Mad Max: Fury Road center framing / action clarity: https://nofilmschool.com/how-to-watch-mad-max-fury-road

### Failure Diagnosis - Ordinary Ship Farewell

**What failed**
- Character scale was too equal; both people held similar visual weight, so the distance did not hurt.
- The ship did not dominate the relationship; it became scenery instead of the machine physically taking one person away.
- The water gap was visible but not dramatic enough; it did not become a negative-space wound.
- Both characters were lit and readable in a similar way, flattening emotional hierarchy.
- Body acting was too generic: standing, looking, restrained hand gesture. It lacked a specific irreversible action such as hand leaving rail, rope falling, gangway lifted, ship turning away, or one person being blocked by hull geometry.

**Correction rule**
- Farewell images need unequal visual weight. Choose whose pain owns the frame. Make one person large/near/partly shadowed and the other tiny/far/isolated, or make the departing vessel massive enough to swallow the departing person.
- Physical separation must have proof: raised gangway, slack rope, closing door, hull blocking sightline, wake cutting through reflection, crowd/security line, or water widening.
- Light must control information like a low-key power scene: reveal hands, profile, glasses edge, or shoulder line; hide eyes or face when withholding emotion is stronger than showing it.

### Case R13 - Godfather-Inspired Low-Key Information Control

**叙事层**
- 情绪基调：权力、隐忍、不可读、情绪被压在黑暗里。
- 人物关系：被拍者控制信息；观众只能看见被允许看见的脸部、手部、衣领、眼镜边缘或道具高光。
- 剧情节点：谈判、离别前克制、身份压迫、无法说出口的决定。
- 叙事功能：让光线成为叙事审查器；不是把画面拍黑，而是让可见信息变少且更准。

**视觉层**
- 景别：近景、中近景、室内群像或夜景离别局部均可。
- 机位：略低或平视，人物不必大幅动作；权力来自静止和看不透。
- 构图法则：低调光、局部可见、负空间、手部/眼部信息分配、门窗/栏杆/船舷遮挡。
- 光影：顶光或高侧光压出眉骨阴影，眼睛可半隐；小范围暖光只落在手、唇、眼镜边、领口或道具上；暗部保留层次。
- 色彩：黑、暖褐、金黄小面积高光，外部冷蓝或暗绿作为对比。
- 画面层次：前景遮挡物制造信息筛选，中景人物局部受光，背景暗部吸收环境。
- 镜头 / 焦段 / 景深：50-85mm，中浅景深，曝光精确，不让暗部死黑。
- 运动 / 剪辑 / 声音：少动；衣料、手指、玻璃、门锁、远处脚步比大动作更重要。

**语言层**
- 提示词参考：`low-key dramatic lighting, warm top-side key light hiding the eyes in brow shadow, only the hand on the railing and glasses edge catching a narrow amber highlight, deep dark background with preserved shadow detail, restrained unreadable farewell`
- 关键词提取：`low-key`, `eyes partly hidden`, `top-side key`, `controlled highlight`, `negative fill`, `hands as emotional proof`
- AIGC 可见锚点：必须写清哪一部分被照亮，哪一部分被藏住；不能只写“教父感”或“暗黑高级”。

**复刻与运用**
- 用这个手法的原因：克制情绪比哭喊更高级，观众会盯着可见细节读人物。
- 如何用：把主光缩小，允许脸的一部分沉入阴影，把情绪转移到手、眼镜、肩、嘴角。
- 适用场景：男主不想走但必须走、权力人物命令、隐瞒真相、失去但不能崩溃。
- 风险与反例：全画面压暗但没有信息锚点，就是欠曝；把眼睛补得太亮会失去不可读性。

**沉淀条目**
- 可复用规则：低调光的核心是“控制观众知道什么”，不是“画面变黑”。每个暗部都要有叙事理由。

### Case R14 - Hero Entrance / Delayed Reveal And Silhouette Scale

**叙事层**
- 情绪基调：希望、压迫解除、命运人物入场、观众等待被兑现。
- 人物关系：入场者不是单独摆姿势，而是被光、群体、空间或危机托举成答案。
- 剧情节点：援军到来、主角登场、反派压迫被打破、危机中出现转机。
- 叙事功能：用延迟揭示和视觉中心把“这个人来了”变成事件。

**视觉层**
- 景别：从极远景/远景建立轮廓，再到中景英雄身形。
- 机位：低机位、背光、中心轴或慢速环绕；人物先成为轮廓，再给局部身份锚点。
- 构图法则：中心视觉锚点、背光剪影、群体/门户/烟雾托举、分层入场、负空间等待。
- 光影：强背光或门户光形成轮廓边，正面先不全亮；雾尘让光路可见。
- 色彩：背景冷或灰，入场光可暖金/白/橙，强调色归属于入口光源。
- 画面层次：前景被压迫者或战场碎片，中景入场者，背景门/光/军阵/烟尘。
- 镜头 / 焦段 / 景深：24-50mm 根据规模；大场面用宽幅广角，个人入场可用50-70mm压缩仪式感。
- 运动 / 剪辑 / 声音：先声音/光进入，再轮廓，再身份动作；不要一开始就全亮全清楚。

**语言层**
- 提示词参考：`low-angle hero entrance silhouette, backlight pouring through a huge doorway, dust and haze revealing light beams, the figure stands center while background crowd forms a wide support layer, identity revealed by one clear gesture and rim-lit outline`
- 关键词提取：`delayed reveal`, `rim-light silhouette`, `low angle`, `center anchor`, `supporting crowd`, `portal/door light`
- AIGC 可见锚点：入场者要先轮廓化；身后必须有光源/门/人群/烟尘支撑，不能只有一个人站空地。

**复刻与运用**
- 用这个手法的原因：英雄感来自“被等待”和“改变局势”，不是来自摆一个帅姿势。
- 如何用：先让环境承受压力，再让光或声音打开入口，最后让人物走进视觉中心。
- 适用场景：江宴主视角获得转机、未来清宴出现、白塔援军、反派压迫空间被打破。
- 风险与反例：人物和背景同等亮度、同等大小，会变成普通站姿；没有等待和前置压力，登场没有重量。

**沉淀条目**
- 可复用规则：英雄登场必须先制造缺口，再让人物填补缺口。光、声、空间和群体反应要一起服务入场。

### Case R15 - Accident / Danger Staging Through Causal Chain And Center Clarity

**叙事层**
- 情绪基调：突发、不可逆、空间失控、人物被物理因果逼着反应。
- 人物关系：危险不是背景爆点，而是打断人物关系的力量。
- 剧情节点：车祸、桥裂、坠落、袭击、机械失控、公共空间事故。
- 叙事功能：让观众清楚知道危险从哪来、如何扩大、角色何时发现、谁被迫改变动作。

**视觉层**
- 景别：事故前用空间关系镜头，触发用细节或中近景，失控用广角/中心锚点。
- 机位：贴近角色视角或危险路径；车内/船上/桥面等封闭空间优先让观众被困在现场。
- 构图法则：因果链中心构图、危险从画外进入、固定视觉地标、快速但可读的中心信息。
- 光影：危险光源或反光先出现，如车灯、火光、裂缝水光、警示灯；不要只在爆发后才给危险。
- 色彩：警示色必须归属明确物体，红灯/火光/银色裂缝/手机光不能全画面乱飘。
- 画面层次：前景人物或道具反应，中景危险路径，背景公共/机械空间持续运动。
- 镜头 / 焦段 / 景深：24-35mm用于空间失控，50mm用于角色困在危险中，100mm用于事故证据特写。
- 运动 / 剪辑 / 声音：先听见或看见异常，再给角色反应，再给危险扩展；声音必须贴因果。

**语言层**
- 提示词参考：`danger enters from off-screen left as a hard reflected light before impact, central frame keeps the cracking structure and character hand in the same readable axis, foreground breath freezes, midground object shifts, background crowd reacts half a beat later, layered metallic crack and low-frequency rumble`
- 关键词提取：`causal chain`, `off-screen threat`, `center clarity`, `visual landmark`, `reaction delay`, `sound proof`
- AIGC 可见锚点：必须写危险起点、路径、角色发现时刻、视觉地标和声音来源。

**复刻与运用**
- 用这个手法的原因：事故好看不等于有效；有效事故要让观众懂因果且来不及阻止。
- 如何用：给一个固定地标，所有切镜围绕它推进；快切时把关键信息放中心，不让眼睛乱找。
- 适用场景：高架桥裂、车祸、船离岸绳索断裂、白塔坠落、时间机器故障。
- 风险与反例：只写爆炸、摇晃、尖叫会变成混乱背景；没有因果链就没有悬疑和压迫。

**沉淀条目**
- 可复用规则：危险事故的核心不是“更乱”，而是“因果更清楚”。危险必须从一个可见/可听起点逐步夺走角色选择。

### Case R16 - Extreme Farewell Distance / Unequal Scale And Irreversible Transit

**叙事层**
- 情绪基调：无法追回、时代/命运吞人、关系被交通工具切断。
- 人物关系：留下者拥有画面前景重量，离开者被船、车、门、队伍或距离吞小；或反过来，让离开者巨大前景遮住留下者，表现逃不掉的选择。
- 剧情节点：船离岸、列车出站、车门关闭、城门落下、空间通道断开。
- 叙事功能：用比例差和不可逆动作证明离别已经发生。

**视觉层**
- 景别：极宽幅远景或强前景过肩。
- 机位：留在一方的视角；不要让两人平等站成普通双人构图。
- 构图法则：极端尺度差、负空间水面/轨道/道路、物理屏障、运动矢量对抗静止矢量。
- 光影：前景人物可半剪影，远方人物只有轮廓/小高光；把亮部给“切断物”如船舷、车门、缆绳、桥口。
- 色彩：夕阳暖光连接两人，冷暗水痕/车体阴影/门影切断连接。
- 画面层次：前景一方的大体量身体或手，中景屏障/水面/绳索，背景另一方小人物和巨大交通工具。
- 镜头 / 焦段 / 景深：两种选择：24-35mm近大远小强化比例，或85-135mm压缩远方巨物吞人；必须明确主导一方。
- 运动 / 剪辑 / 声音：离开物持续运动，留下者静止；缆绳落水、汽笛、门锁、轮机声是不可逆证据。

**语言层**
- 提示词参考：`extreme farewell composition, woman huge in left foreground silhouette on the pier occupying one third of frame, departing ship dominates the right background, man tiny at the bow rail less than five percent of frame height, raised gangway and slack rope falling into dark water, golden sunset path broken by black wake`
- 关键词提取：`unequal scale`, `foreground giant`, `tiny distant lover`, `physical separation proof`, `negative water gap`, `irreversible transit`
- AIGC 可见锚点：明确比例：前景人物占画面三分之一，远方人物小于画面高度5%-8%；船/门/车要比人物更有重量。

**复刻与运用**
- 用这个手法的原因：离别痛感来自“追不上”的物理事实，不是两个人一起站得好看。
- 如何用：只选一个人物做主视觉，另一个人物变成远方目标；让交通工具、门、绳索、队伍完成分离。
- 适用场景：船头/码头、列车/站台、城堡/低路、高架桥/车流、时空门关闭。
- 风险与反例：两人比例相同、同等清晰、同等亮度，就是普通合照；没有不可逆动作，就是摆拍。

**沉淀条目**
- 可复用规则：离别构图必须不平等。至少有一个维度失衡：比例、焦点、亮度、运动、遮挡或高度。
