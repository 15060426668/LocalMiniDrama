#!/usr/bin/env python3
"""Validate formal 2D animation-performance and SD handoff artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path


FIELD_PATTERNS = {
    "表演任务": r"表演任务|acting\s+task",
    "知情/误读权限": r"知情\s*/\s*误读权限|信息权限|knowledge\s*/?\s*misread",
    "四项强度": (
        r"四项强度|事件强度\s*/\s*内在情绪\s*/\s*公开表情\s*/\s*可见反应幅度"
    ),
    "正常基准": r"正常基准|表演基准|normal\s+baseline",
    "触发": r"触发|trigger",
    "关键姿势链": r"关键姿势链|关键姿势|key\s*pose",
    "时间与间距": r"时间与间距|时间\s*/\s*间距|timing\s*(?:and|/|&)\s*spacing",
    "脸部与口型": r"脸部与口型|面部与口型|脸部\s*/\s*口型|face\s*(?:and|/|&)\s*lip",
    "身体/重心/手脚": r"身体\s*/\s*重心\s*/\s*手脚|身体与重心|body\s*/\s*center\s+of\s+gravity",
    "次级运动": r"次级运动(?:与材质)?|secondary\s+(?:motion|action)",
    "动画镜头突变": r"动画镜头突变|镜头突变|animation\s+shot\s+mutation",
    "环境/物件/NPC表演": (
        r"环境\s*/\s*物件\s*/\s*NPC表演|环境、物件与NPC表演|环境与NPC表演|environment\s*/\s*object\s*/\s*NPC"
    ),
    "声音触发": r"声音触发|声画触发|sound\s+trigger",
    "恢复与尾帧": r"恢复与尾帧|恢复\s*/\s*尾帧|recovery\s*(?:and|/|&)\s*tail",
    "SD承接锚点": r"SD承接锚点|SD锚点|handoff\s+anchor",
}

EXPRESSIVE_FIELD_PATTERNS = {
    "动画表达引擎": r"动画表达引擎|主表达引擎|animation\s+expression\s+engine",
    "情绪特效链": r"情绪特效链|情绪效果链|emotion(?:al)?\s+effect\s+chain",
    "效果接力链": r"效果接力链|特效接力链|effect\s+relay\s+chain",
    "环境响应链": r"环境响应链|环境特效链|environment\s+response\s+chain",
    "环境换手": r"环境换手|环境接管|environment\s+handoff",
    "视觉状态刷新": r"视觉状态刷新|视觉刷新链|visual\s+state\s+refresh",
    "动画专属镜头": r"动画专属镜头|动画专属帧|animation[-\s]+only\s+(?:shot|frame)",
    "动画转场与归模": r"动画转场与归模|转场与归模|animation\s+transition\s+and\s+return",
}

EXPRESSIVE_DOCUMENT_PATTERNS = {
    "动画方案筛选": r"动画方案筛选|三引擎方案筛选|animation\s+candidate\s+screen",
    "表达机制选型": r"表达机制选型|五域发散|expression\s+mechanism\s+selection",
    "段级主表达引擎": r"段级主表达引擎|段落主表达引擎|segment\s+expression\s+engine",
    "动画表达评分": r"动画表达评分|动画语言评分|animation\s+expression\s+score",
}

SCENE_DOCUMENT_PATTERNS = {
    "导演事实锁": r"导演事实锁|现实事实锁|director\s+fact\s+lock",
    "动画视觉命题": r"动画视觉命题|动画命题|animation\s+visual\s+proposition",
    "世界可变性扫描": r"世界可变性扫描|十二轴扫描|world\s+mutability\s+scan",
    "激活世界轴": r"激活世界轴|激活轴|active\s+world\s+axes",
    "场景架构候选": r"场景架构候选|动画场景候选|scene\s+architecture\s+candidates",
    "动画场景规划": r"动画场景规划|主世界法则|animation\s+scene\s+plan",
    "视觉状态图": r"视觉状态图|动画状态图|visual\s+state\s+graph",
    "动画镜头策略": r"动画镜头策略|投影策略|animation\s+shot\s+strategy",
}

MIXED_REALITY_DOCUMENT_PATTERNS = {
    "混合现实路由": r"混合现实路由|2D入现实路由|mixed[-\s]+reality\s+route",
    "真人底片锁": r"真人底片锁|实拍底片锁|live[-\s]+action\s+plate\s+lock",
    "2D角色层锁": r"2D角色层锁|二维角色层锁|drawn[-\s]+character\s+lock",
    "跨媒介融合证据": r"跨媒介融合证据|空间归属证据|cross[-\s]+medium\s+integration",
    "手绘区别保留": r"手绘区别保留|手绘差异保留|hand[-\s]+drawn\s+distinction",
    "双层尾态": r"双层尾态|双媒介尾态|dual[-\s]+layer\s+tail",
}

ALL_FIELD_PATTERNS = {
    **FIELD_PATTERNS,
    **EXPRESSIVE_FIELD_PATTERNS,
    **SCENE_DOCUMENT_PATTERNS,
    **MIXED_REALITY_DOCUMENT_PATTERNS,
}

INTENSITY_LABELS = ["事件强度", "内在情绪", "公开表情", "可见反应幅度"]

BEAT_HEADING = re.compile(
    r"(?mi)^(?:#{1,6}\s*)?(?:"
    r"第\s*\d+(?:\s*[-—~至到]\s*\d+)?\s*(?:秒|镜|节拍)"
    r"|镜头\s*[A-Za-z0-9一二三四五六七八九十]+"
    r"|Beat\s*\d+"
    r")[^\n]*$"
)

POSITIVE_ONLY_FORBIDDEN = [
    r"不要",
    r"禁止",
    r"避免",
    r"不能",
    r"负向提示词",
    r"negative\s+prompt",
    r"\bwithout\b",
    r"\bno\s+",
]

SOURCE_MARKERS = [
    r"《[^》]{1,100}》",
    r"(?:参考|模仿|复刻|致敬)\s*(?:作品|动画|电影|影片|导演|作者|工作室|IP)",
    r"(?:作品|电影|影片|导演|作者|工作室|IP)(?:名称|名字|风格)?\s*[：:]",
]

ANIMATION_EFFECT_MARKERS = re.compile(
    r"压缩|拉伸|伸长|收缩|变形|离模|归模|回弹|过冲|残影|smear|"
    r"粗线|断线|墨块|平面化|压平|二维层|纸片|拼贴|漫画格|绘画系统|媒介|"
    r"图形|蛇形|鱼眼|透视|尺度|几何|帧密度|影子|回忆|重建|"
    r"色块|白场|黑场|侵入|污染|碎裂|裂开|折叠|液化|漂移",
    re.I,
)

ENVIRONMENT_RESPONSE_MARKERS = re.compile(
    r"环境|背景|门框|课桌|餐桌|地板|墙纸|墙线|墙面|窗|杯|光|影|风|雨|云|人群|NPC|物件|"
    r"挤压|扩张|收缩|倾斜|漂移|震动|吞没|遮挡|流过|继续|接管|响应",
    re.I,
)

RETURN_MARKERS = re.compile(
    r"归模|回落|恢复|收回|缩回|落地|残留|余波|锚点|尾帧|后果|接管",
    re.I,
)

RELAY_MARKERS = re.compile(
    r"继承|接力|交给|接住|沿同一|同形|同向|同色|同声|末端|起点|"
    r"落成|变成|转为|取得画面|夺回画面|接管画面",
    re.I,
)

ANCHOR_MARKERS = re.compile(
    r"支点|脚下|鞋底|脚步|台阶|手掌|接触|桌边|门框|扶手|栏杆|纸张|纸边|"
    r"声源|视线|物件|持有|锚点|落地|残留",
    re.I,
)

ENVIRONMENT_HANDOFF_MARKERS = re.compile(
    r"接管|取得(?:画面|中心|余波)|换手|夺回|继续|留下|吞没|遮满|判决",
    re.I,
)

ABSTRACT_EXPRESSION_MARKERS = re.compile(
    r"邪恶|阴冷|恐怖|压迫感|诡异|崩溃|疯狂|动画感|炫技|像(?:毒蛇|美杜莎)",
    re.I,
)

CONTACT_ACTION_MARKERS = re.compile(
    r"拿取|拿起|抓住|握住|接住|递出|递给|拥抱|抱住|抱紧|推门|推开|推倒|"
    r"拉住|拉开|扶住|扶起|坐下|落地|着地|撞上|撞到|击中|打中|砍中|踢中|"
    r"格挡|踩住|踩到|摔倒|拔刀|拔剑",
    re.I,
)

CONTACT_EVENT_MARKERS = re.compile(
    r"接触|触碰|碰到|贴住|握住|抓住|接住|抱住|抱紧|抱实|压住|压实|踩住|"
    r"击中|打中|砍中|踢中|撞上|撞到|落地|着地|坐到|坐进|坐上|扶住|交叉",
    re.I,
)

FORCE_CONFIRMATION_MARKERS = re.compile(
    r"重量|承重|阻力|反作用|摩擦|压缩|形变|下沉|缓冲|陷入|回弹|受力|挤压|冲击|弯曲|绷紧",
    re.I,
)

POST_CONTACT_STATE_MARKERS = re.compile(
    r"落定|站稳|接稳|持有|松开|收回|放下|滑动|滑下|滚动|滚出|停下|恢复|"
    r"尾帧|新状态|重新支撑|重建支点|共同重心|继续下沉",
    re.I,
)

COMPOUND_CAMERA_MARKERS = re.compile(
    r"环绕|绕(?:过|行|至)|越顶|"
    r"贴地.{0,24}(?:俯视|拉升|升空|高空)|"
    r"(?:俯冲|拉升).{0,24}(?:俯视|仰视|高空|贴地)|"
    r"穿过.{0,18}(?:遮挡|前景|门框|人群|车辆)|"
    r"POV|第一人称|连续景别",
    re.I,
)

CAMERA_DIRECTION_ANCHOR_MARKERS = re.compile(
    r"身体朝向|主体朝向|屏幕方向|世界方向|运动方向|"
    r"面向|朝向|消失点|地平线|视平线|目标方向|道路轴|车道轴|走廊轴",
    re.I,
)

CAMERA_START_MARKERS = re.compile(
    r"开始机位|起始机位|初始机位|镜头从|摄影机从|机位从",
    re.I,
)

CAMERA_ROUTE_MARKERS = re.compile(
    r"沿|经过|越过|穿过|绕过|外球面|轨道|弧线路径|空间路径|运行路径|环绕路径",
    re.I,
)

CAMERA_LANDING_MARKERS = re.compile(
    r"摄影机落点|镜头落点|最终机位|最终景别|最后停在|结束于|收在|"
    r"落在.{0,24}(?:俯视|仰视|全景|近景|中景|特写|机位|构图)|"
    r"落点锁定|最终锁定",
    re.I,
)

PROCESS_ENTRY_MARKERS = re.compile(
    r"从.{0,24}(?:边缘|瞳孔|眼|手|指尖|物件|墙|影|裂缝|表面|声源|扶手|门框|桌面).{0,12}"
    r"(?:长出|冒出|渗出|裂开|游出|出现|开始|掀起|取得)|"
    r"(?:关键词|重音|触碰|接触|敲击|脚步|门声|铃声|视线).{0,16}(?:触发|使|让|化成)|"
    r"第一道(?:裂纹|影线|图形|高光)|入口",
    re.I,
)

PROCESS_DEVELOPMENT_MARKERS = re.compile(
    r"沿|逐段|逐层|逐块|依次|穿过|爬|游走|缠|卷曲|扩张|吞没|挤窄|"
    r"折叠|重组|复制|平面化|颗粒化|遮满|夺取画面|取得画面|接住|落成|变成|转为",
    re.I,
)

RESIDUE_MARKERS = re.compile(
    r"残留|余波|留下|落成|后果|尾帧|污迹|字迹|空位|错位|尾音|声音尾巴|暗痕|折痕|裂纹状",
    re.I,
)

MECHANISM_FAMILY_PATTERNS = {
    "全身与支点": re.compile(
        r"(?:肩|脊柱|骨盆|髋|重心|支撑脚|脚下支点|手掌|全身|躯干|身体高度).{0,14}"
        r"(?:压缩|伸展|后撤|承重|失衡|越过|下降|转向|收窄|前倾|后仰|抬高|压低|弹开|回弹|折叠|寻找|错拍)|"
        r"(?:压缩|伸展|后撤|承重|失衡|越过|下降|转向|收窄|前倾|后仰|抬高|压低|弹开|回弹|折叠|寻找|错拍).{0,14}"
        r"(?:肩|脊柱|骨盆|髋|重心|支撑脚|脚下支点|手掌|全身|躯干|身体高度)", re.I
    ),
    "意象外化": re.compile(
        r"蛇形|蛇影|蛇发|鳞状|石化|触手|藤蔓|针线|捕食影|实体化|具象化|影线|缠绕", re.I
    ),
    "异常空间": re.compile(
        r"(?:空间|墙体|台阶|走廊|楼梯|透视|消失点|出口).{0,18}"
        r"(?:挤压|挤窄|延长|复制|折叠|弯曲|取消|拉长|压缩|封住|重构)|"
        r"深井|无限延长|审讯场|不同画层|尺度法庭", re.I
    ),
    "回忆与时间": re.compile(
        r"回忆|过去|旧场景|旧房间|重建.{0,16}(?:家庭|餐桌|房间|争吵)|裂片背面|最近一次|闪回|时间压缩", re.I
    ),
    "物件与材质": re.compile(
        r"(?:铅笔|包带|门把|桌面|纸张|书页|铃铛|碗|筷子|饭勺|物件|材质|裂片).{0,18}"
        r"(?:变形|落成|接住|牵引|折叠|裂开|卷曲|平面化|重组|接管|取得)", re.I
    ),
    "混合媒介": re.compile(
        r"粗笔|涂鸦|像素|纸片|拼贴|沙画|墨水|漫画格|儿童画|蜡笔|Q版|平面化|绘画系统|混合媒介|图形层", re.I
    ),
    "群体几何": re.compile(
        r"群体|NPC|同学|人群|社交|闭环|拓扑|前景身体|课桌网格|"
        r"(?:目光|朝向|物件通道).{0,16}(?:连成|改指|转向|封锁|迁移)", re.I
    ),
    "声音可视化": re.compile(
        r"(?:声音|声源|重音|回声|敲击声|门声|铃声|脚步声).{0,18}"
        r"(?:化成|变成|重建|生成|取得|夺回|扩张|实体化|可视化)|拟声字", re.I
    ),
    "喜剧与转场": re.compile(
        r"喜剧|搞笑|错拍|字面化|擦屏|动作偷渡|定格批注|尾刀|类型片|误会|Q版", re.I
    ),
    "环境行动": re.compile(
        r"(?:环境|背景|墙面|墙体|栏杆|扶手影|门框|课桌|晨光|空椅).{0,20}"
        r"(?:挤压|诱导|拒绝|吞没|重建|裂开|卷曲|封住|夺回|判决|取得画面|延长|复制|展开|压缩|折叠)", re.I
    ),
}

WORLD_AXIS_PATTERNS = {
    "时间": re.compile(r"时间", re.I),
    "空间": re.compile(r"空间", re.I),
    "物理": re.compile(r"物理", re.I),
    "人物形象": re.compile(r"人物形象|角色形象", re.I),
    "绘画媒介": re.compile(r"绘画媒介|绘画系统|媒介", re.I),
    "投影镜头": re.compile(r"投影\s*/?\s*镜头|投影镜头|镜头投影", re.I),
    "环境材质": re.compile(r"环境材质|环境\s*/?\s*材质", re.I),
    "物件符号": re.compile(r"物件符号|物件\s*/?\s*符号", re.I),
    "群体拓扑": re.compile(r"群体拓扑|群体\s*/?\s*拓扑", re.I),
    "声音文字": re.compile(r"声音\s*/?\s*文字|声音文字", re.I),
    "光色": re.compile(r"光色|光\s*/?\s*色", re.I),
    "转场剪辑": re.compile(r"转场\s*/?\s*剪辑|转场剪辑", re.I),
}

WORLD_REWRITE_FAMILY_PATTERNS = {
    "时间改写": re.compile(
        r"(?:时间|帧密度|动作|声拍).{0,18}(?:停住|冻结|重复|循环|错拍|压缩|倒序|提前|异步|拉长)", re.I
    ),
    "空间改写": re.compile(
        r"(?:空间|房间|走廊|楼梯|台阶|地面|墙体|透视|消失点|画框).{0,20}"
        r"(?:压缩|延长|复制|折叠|翻面|弯曲|拉长|分层|嵌套|吞没|关闭|裂开)", re.I
    ),
    "物理改写": re.compile(
        r"(?:重力|惯性|体积|材质|影子|身体|人物).{0,18}"
        r"(?:改向|失效|纸化|液化|颗粒化|结晶|磁化|压扁|吹胀|折叠|滞留|先行)", re.I
    ),
    "人物形象改写": re.compile(
        r"(?:轮廓|比例|头身|发型|耳朵|衣褶|服装图案|影子|分身|人物细节|角色形象).{0,18}"
        r"(?:伸长|压缩|放大|缩小|分裂|删减|归还|变成|取得|离模|折叠)", re.I
    ),
    "绘画媒介改写": re.compile(
        r"(?:绘画|线条|粗笔|蜡笔|纸片|拼贴|像素|漫画格|沙画|墨水|儿童画|媒介).{0,18}"
        r"(?:替换|接管|压平|展开|折回|侵入|重组|擦除|改变|切换)", re.I
    ),
    "投影改写": re.compile(
        r"(?:投影|透视|视点|消失点|前后景|图层|画框).{0,18}"
        r"(?:压平|退出|折断|翻面|分裂|错位|变形|移动|夺权|切换)", re.I
    ),
    "环境行动": re.compile(
        r"(?:环境|背景|墙面|课桌|栏杆|门框|窗|空位).{0,18}"
        r"(?:挤压|诱导|拒绝|吞没|复制|剥落|呼吸|遗忘|关闭|见证|接管)", re.I
    ),
    "物件世界化": re.compile(
        r"(?:杯|笔|门|包带|照片|食物|屏幕|物件|裂纹|字迹).{0,18}"
        r"(?:改写|变成|生成|牵引|切割|封住|扩张|折叠|成为世界|接管空间)", re.I
    ),
    "群体拓扑改写": re.compile(
        r"(?:群体|同学|人群|NPC|课桌通道|目光线|社交圈).{0,18}"
        r"(?:闭合|排除|迁移|复制|关闭|吞掉|改指|统一删减|变成剪影)", re.I
    ),
    "声音文字改写": re.compile(
        r"(?:声音|重音|回声|拟声字|字幕|台词|文字|字形).{0,18}"
        r"(?:生成|实体化|推开|压扁|遮挡|切割|重建|擦除|取得画面|变成)", re.I
    ),
    "光色改写": re.compile(
        r"(?:颜色|色彩|阴影|暖光|冷光|光色)(?:所有权)?(?:由|从|逐渐|开始|直接|完全|局部|沿)?.{0,6}"
        r"(?:取得(?:画面|所有权)|夺回|传染|吞没|只保留|退出|扩张|收回|反证)", re.I
    ),
    "转场因果": re.compile(
        r"(?:转场|遮满|动作|形状|材质|声音|画格|纸边).{0,18}"
        r"(?:接住|继承|造成下一|偷渡|匹配|击穿|掀开|扩大|落到新空间)", re.I
    ),
}

CONVENTIONAL_COVERAGE_MARKERS = re.compile(
    r"正反打|过肩|双人中景|人物中景|中景对话|近景反应|反应特写|脸部特写|"
    r"道具特写|空镜|切到说话者|切到听者|谁说话.{0,8}(?:给谁镜头|切谁)",
    re.I,
)


@dataclass
class Finding:
    level: str
    beat: str
    code: str
    message: str


def split_beats(text: str) -> list[tuple[str, str]]:
    matches = list(BEAT_HEADING.finditer(text))
    if not matches:
        return [("全文", text)]

    beats: list[tuple[str, str]] = []
    prefix = text[: matches[0].start()].strip()
    if prefix and any(re.search(p, prefix, re.I) for p in FIELD_PATTERNS.values()):
        beats.append(("前置节拍", prefix))

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title = re.sub(r"^#{1,6}\s*", "", match.group(0)).strip()
        beats.append((title, text[match.start() : end]))
    return beats


def field_value(block: str, pattern: str) -> str | None:
    label = re.compile(
        rf"(?mi)^\s*(?:[-*]\s*)?(?:\*\*)?(?:{pattern})(?:\*\*)?\s*[：:]\s*(.*)$"
    )
    match = label.search(block)
    if not match:
        return None
    inline = match.group(1).strip()
    if inline:
        return inline

    remainder = block[match.end() :]
    for line in remainder.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(
            re.match(
                rf"^(?:[-*]\s*)?(?:\*\*)?(?:{candidate})(?:\*\*)?\s*[：:]",
                stripped,
                re.I,
            )
            for candidate in ALL_FIELD_PATTERNS.values()
        ):
            return ""
        return stripped
    return ""


def validate_intensities(block: str, beat: str, findings: list[Finding]) -> None:
    explicit = []
    for label in INTENSITY_LABELS:
        match = re.search(rf"{label}\s*[：:=]?\s*(10|[0-9])(?:\s*/\s*10)?", block)
        if match:
            explicit.append((label, int(match.group(1))))

    if len(explicit) == 4:
        return

    combined = re.search(
        r"(?:四项强度|事件强度\s*/\s*内在情绪\s*/\s*公开表情\s*/\s*可见反应幅度)"
        r"\s*[：:]\s*((?:10|[0-9])(?:\s*/\s*(?:10|[0-9])){3})",
        block,
        re.I,
    )
    if combined:
        return

    findings.append(
        Finding(
            "WARNING",
            beat,
            "INTENSITY_VALUES",
            "四项强度字段存在，但未读到完整的0-10数值；建议分别锁定事件、内在、公开表情和可见反应。",
        )
    )


def validate_pose_chain(value: str, beat: str, findings: list[Finding]) -> None:
    parts = [p.strip() for p in re.split(r"->|→|⇒|=>|—>|\s+到\s+", value) if p.strip()]
    if len(parts) < 4:
        findings.append(
            Finding(
                "WARNING",
                beat,
                "POSE_CHAIN_SHORT",
                "关键姿势链少于4态；重要动作通常需要起始、预备、峰值和恢复/落定。",
            )
        )


def validate_motion_completeness(
    values: dict[str, str],
    block: str,
    beat: str,
    findings: list[Finding],
    profile: str,
) -> None:
    """Check cross-field acting causality, not only field presence."""
    present = sum(
        bool(values.get(name))
        for name in (
            "表演任务",
            "触发",
            "关键姿势链",
            "脸部与口型",
            "身体/重心/手脚",
            "恢复与尾帧",
        )
    )
    if present < 4:
        return

    pose = values.get("关键姿势链", "")
    parts = [p.strip() for p in re.split(r"->|→|⇒|=>|—>|\s+到\s+", pose) if p.strip()]
    abstract_action = re.compile(
        r"(?:冲过去|跑过去|打斗|躲开|跳下|伸手|转身|攻击|逃跑|移动过去|快速完成|发生变化|变形)"
    )
    if len(parts) < 4:
        if abstract_action.search(pose):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "ABSTRACT_ACTION_SUMMARY",
                    "主体动作仍是单一摘要动词；必须展开触发、预备、支点/发力、峰值、接触或结果、恢复。",
                )
            )
        elif profile in ("expressive", "scene", "mixed-reality") or len(parts) > 0:
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "MOTION_CHAIN_INCOMPLETE",
                    "关键姿势链少于4个可辨状态；普通节拍至少写基准、触发、可见反应和恢复/落定。",
                )
            )

    body = values.get("身体/重心/手脚", "")
    if body and not re.search(
        r"重心|支点|承重|肩|脊柱|腰|髋|骨盆|膝|脚|腿|手|腕|肘|前倾|后仰|失衡",
        body,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "BODY_MECHANICS_THIN",
                "身体字段没有支点、重心、关节或手脚发力证据。",
            )
        )

    face = values.get("脸部与口型", "")
    if face and not re.search(
        r"眼|瞳孔|视线|目光|眉|嘴|口型|下颌|呼吸|吸气|吞咽|眨|睫毛",
        face,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "FACE_GAZE_THIN",
                "脸部字段没有眼、视线、口型、呼吸或眨眼的可见载体。",
            )
        )

    secondary = values.get("次级运动", "")
    if secondary and not re.search(
        r"延迟|慢半拍|滞后|惯性|过冲|回弹|继续|落下|飘|震|碎|材质|布料|衣|发|道具",
        secondary,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "SECONDARY_MOTION_THIN",
                "次级运动没有来源、延迟、惯性、材质或停止顺序。",
            )
        )

    ecology = values.get("环境/物件/NPC表演", "")
    if ecology and not re.search(
        r"先|随后|然后|延迟|慢半拍|继续|保持|接管|响应|换手|误读|任务|反应|波|距离",
        ecology,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "ECOLOGY_CAUSAL_ORDER_THIN",
                "环境/物件/NPC字段没有时间顺序、反应延迟、任务保持或接管证据。",
            )
        )

    sound = values.get("声音触发", "")
    if sound and not re.search(
        r"声源|脚步|呼吸|风声|雨声|吸力声|笔声|舞步音|静音|重音|敲|碰|先|后|延迟|触发|反应|驱动|接管|尾音|声桥",
        sound,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "SOUND_PICTURE_CAUSALITY_THIN",
                "声音字段没有声源、时序或可见声画反应。",
            )
        )

    recovery = values.get("恢复与尾帧", "")
    if recovery and not re.search(
        r"恢复|落定|落点|收势|回到|尾帧|末端|落下|残留|余波|继承|下一|继续|留下|保持|仍",
        recovery,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "TAIL_INHERITANCE_THIN",
                "恢复字段没有可见落定、残留或下一拍继承状态。",
            )
        )

    motion_text = " ".join(
        values.get(name, "")
        for name in (
            "关键姿势链",
            "脸部与口型",
            "身体/重心/手脚",
            "次级运动",
            "环境/物件/NPC表演",
            "声音触发",
            "恢复与尾帧",
        )
    )
    contact_text = " ".join(
        values.get(name, "")
        for name in (
            "表演任务",
            "关键姿势链",
            "身体/重心/手脚",
            "次级运动",
            "环境/物件/NPC表演",
            "恢复与尾帧",
        )
    )
    if CONTACT_ACTION_MARKERS.search(contact_text):
        if not CONTACT_EVENT_MARKERS.search(contact_text):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "CONTACT_EVENT_MISSING",
                    "接触型动作从接近直接跳到结果；必须写可见的触碰、握住、落地、撞击或共同接触节点。",
                )
            )
        if not FORCE_CONFIRMATION_MARKERS.search(contact_text):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "CONTACT_FORCE_PROOF_MISSING",
                    "接触型动作缺少重量、阻力、压缩、摩擦、缓冲或反作用证明。",
                )
            )
        if not POST_CONTACT_STATE_MARKERS.search(contact_text):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "POST_CONTACT_STATE_MISSING",
                    "接触后没有新的支点、持有关系、落定、松开、滑滚或恢复状态。",
                )
            )
    if not re.search(
        r"先|随后|然后|接着|再|才|晚|延迟|慢半拍|同时|随着|带动|之后|前后|一拍",
        motion_text,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "MOTION_TIME_ORDER_THIN",
                "主体、表情、环境和声音没有共享的先后/错时因果线。",
            )
        )

    if re.search(r"所有人(?:同时|同步)|全员(?:同时|同步)|大家同时", block, re.I) and not re.search(
        r"延迟|分层|各自|不同|有人|部分|反应波",
        block,
        re.I,
    ):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "SYNCHRONIZED_CROWD_DEGENERATION",
                "群体被写成同步反应；需要按知情路径、距离和个体任务分层。",
            )
        )


def validate_compound_camera_path(
    values: dict[str, str], beat: str, findings: list[Finding]
) -> None:
    """Require spatial proof only when a compound camera move is explicitly requested."""
    camera_text = values.get("动画镜头突变", "")
    if not camera_text or not COMPOUND_CAMERA_MARKERS.search(camera_text):
        return

    missing = []
    if not CAMERA_DIRECTION_ANCHOR_MARKERS.search(camera_text):
        missing.append("主体/屏幕/世界方向锚")
    if not CAMERA_START_MARKERS.search(camera_text):
        missing.append("摄影机开始机位")
    if not CAMERA_ROUTE_MARKERS.search(camera_text):
        missing.append("可追踪空间路径")
    if missing:
        findings.append(
            Finding(
                "ERROR",
                beat,
                "COMPOUND_CAMERA_PATH_THIN",
                "复合运镜缺少" + "、".join(missing) + "；必须把摄影机路径与主体运动分开描述。",
            )
        )

    if not CAMERA_LANDING_MARKERS.search(camera_text):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "CAMERA_LANDING_MISSING",
                "复合运镜没有最终机位、景别或画面所有者落点，无法把尾态交给下一拍。",
            )
        )


def detected_mechanism_families(text: str) -> list[str]:
    return [
        name
        for name, pattern in MECHANISM_FAMILY_PATTERNS.items()
        if pattern.search(text)
    ]


def field_content_text(block: str) -> str:
    values = []
    for pattern in ALL_FIELD_PATTERNS.values():
        value = field_value(block, pattern)
        if value:
            values.append(value)
    return "\n".join(values)


def validate_expressive_handoff(
    block: str, beat: str, findings: list[Finding]
) -> None:
    content = field_content_text(block)
    checks = (
        (
            PROCESS_ENTRY_MARKERS,
            "MISSING_MODEL_PROCESS_ENTRY",
            "表达型承接未写清动画越界从哪个身体、物件、声音或空间入口出现。",
        ),
        (
            PROCESS_DEVELOPMENT_MARKERS,
            "MISSING_MODEL_PROCESS_DEVELOPMENT",
            "表达型承接未写清动画机制沿什么路径、表面、方向或节奏发展。",
        ),
        (
            RETURN_MARKERS,
            "MISSING_MODEL_PROCESS_RETURN",
            "表达型承接未写归还触发、回收路径或现实夺回画面的过程。",
        ),
        (
            RESIDUE_MARKERS,
            "MISSING_MODEL_PROCESS_RESIDUE",
            "表达型承接未写效果结束后的身体、物件、空间、声音或意义残留。",
        ),
    )
    for pattern, code, message in checks:
        if not pattern.search(content):
            findings.append(Finding("ERROR", beat, code, message))

    families = detected_mechanism_families(content)
    if len(families) < 2:
        findings.append(
            Finding(
                "ERROR",
                beat,
                "HANDOFF_MECHANISM_DIVERSITY_THIN",
                "表达型承接只读到"
                + ("、".join(families) if families else "零类")
                + "非脸部动画机制；至少需要两类承载并通过同一因果链接力。",
            )
        )


def validate_expressive_fields(
    block: str, beat: str, findings: list[Finding]
) -> None:
    values: dict[str, str] = {}
    for name, pattern in EXPRESSIVE_FIELD_PATTERNS.items():
        value = field_value(block, pattern)
        if value is None:
            findings.append(Finding("ERROR", beat, "MISSING_EXPRESSIVE_FIELD", f"缺少高密度动画字段：{name}"))
        elif not value.strip():
            findings.append(Finding("ERROR", beat, "EMPTY_EXPRESSIVE_FIELD", f"高密度动画字段为空：{name}"))
        else:
            values[name] = value.strip()

    engine = values.get("动画表达引擎", "")
    if engine and len(re.sub(r"\s+", "", engine)) < 12:
        findings.append(
            Finding(
                "ERROR",
                beat,
                "EXPRESSION_ENGINE_THIN",
                "动画表达引擎过短；应贯通触发、主动画变量、人物、环境/物件、转场和残留。",
            )
        )

    effects = values.get("情绪特效链", "")
    if effects and not ANIMATION_EFFECT_MARKERS.search(effects):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "NO_ANIMATION_EFFECT_OPERATOR",
                "情绪特效链未读到形体、线条、透视、尺度、帧密度、图形或材质动画算子。",
            )
        )

    relay = values.get("效果接力链", "")
    if relay:
        relay_states = [
            part.strip()
            for part in re.split(r"->|→|⇒|=>|—>", relay)
            if part.strip()
        ]
        if len(relay_states) < 4:
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "EFFECT_RELAY_SHORT",
                    "效果接力链少于4态；应写出来源、继承、换手/变形、现实落地和残留。",
                )
            )
        if not RELAY_MARKERS.search(relay):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "NO_INHERITED_BATON",
                    "效果接力链未说明后一效果继承前一效果的形状、方向、色光、节奏、材质、证据或画面权限。",
                )
            )
        if not ANCHOR_MARKERS.search(relay):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "NO_RELAY_REALITY_ANCHOR",
                    "效果接力链缺少支点、接触、声源、视线、物件或落地残留等现实锚点。",
                )
            )

    environment = values.get("环境响应链", "")
    if environment and not ENVIRONMENT_RESPONSE_MARKERS.search(environment):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "NO_ENVIRONMENT_RELAY",
                "环境响应链未读到环境、物件、NPC、光影或空间几何的接力动作。",
            )
        )

    environment_handoff = values.get("环境换手", "")
    if environment_handoff:
        if not ENVIRONMENT_RESPONSE_MARKERS.search(environment_handoff):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "NO_HANDOFF_CARRIER",
                    "环境换手未写环境、物件、NPC、光影或空间几何中的接管载体。",
                )
            )
        if not ENVIRONMENT_HANDOFF_MARKERS.search(environment_handoff):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "NO_ENVIRONMENT_OWNERSHIP_CHANGE",
                    "环境换手未说明何时取得画面、中心、判决或余波所有权。",
                )
            )

    refresh = values.get("视觉状态刷新", "")
    if refresh:
        states = [part.strip() for part in re.split(r"->|→|⇒|=>|—>", refresh) if part.strip()]
        if len(states) < 4:
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "VISUAL_REFRESH_SHORT",
                    "视觉状态刷新少于4态；高密度动画段需写出4-7个意义不同的连续画面状态。",
                )
            )

    animation_only = values.get("动画专属镜头", "")
    if animation_only:
        if not ANIMATION_EFFECT_MARKERS.search(animation_only):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "NO_ANIMATION_ONLY_OPERATION",
                    "动画专属镜头未读到形体、绘画系统、帧密度、图形侵入或空间变形算子。",
                )
            )
        if not ANCHOR_MARKERS.search(animation_only):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "ANIMATION_ONLY_NO_ANCHOR",
                    "动画专属镜头缺少身体支点、接触、视线、声源、物件或落地锚点。",
                )
            )

    transition = values.get("动画转场与归模", "")
    if transition and not RETURN_MARKERS.search(transition):
        findings.append(
            Finding(
                "ERROR",
                beat,
                "NO_RETURN_OR_RESIDUE",
                "动画转场与归模未写回落锚点、现实落地或残留后果。",
            )
        )
    if transition and re.search(r"完全恢复|恢复原样|回到原样|清除(?:全部)?效果", transition):
        if not re.search(r"残留|余波|后果|污迹|字迹|空位|错位|尾音|声音尾巴|物件状态", transition):
            findings.append(
                Finding(
                    "ERROR",
                    beat,
                    "RESET_WITHOUT_RESIDUE",
                    "动画效果结束后完全复原且没有现实残留；应把形体、物件、空间、声音或意义后果留在落地帧。",
                )
            )

    content = field_content_text(block)
    families = detected_mechanism_families(content)
    if len(families) < 2:
        findings.append(
            Finding(
                "ERROR",
                beat,
                "FACE_ONLY_OR_MECHANISM_THIN",
                "高密度动画只读到"
                + ("、".join(families) if families else "零类")
                + "非脸部机制；必须让全身/支点、意象、空间、回忆、物件、媒介、群体、声音、喜剧或环境中的至少两类共同承载。",
            )
        )
    if ABSTRACT_EXPRESSION_MARKERS.search(content) and len(families) < 2:
        findings.append(
            Finding(
                "ERROR",
                beat,
                "ABSTRACT_EXPRESSION_UNCOMPILED",
                "抽象情绪词尚未编译成可见入口、发展路径、身体/空间参与、归还与残留。",
            )
        )


def validate_expressive_document(text: str, findings: list[Finding]) -> None:
    values: dict[str, str] = {}
    for name, pattern in EXPRESSIVE_DOCUMENT_PATTERNS.items():
        value = field_value(text, pattern)
        if value is None:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "MISSING_EXPRESSIVE_DOCUMENT_FIELD",
                    f"缺少段级高密度动画字段：{name}",
                )
            )
        elif not value.strip():
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "EMPTY_EXPRESSIVE_DOCUMENT_FIELD",
                    f"段级高密度动画字段为空：{name}",
                )
            )
        else:
            values[name] = value.strip()

    candidates = values.get("动画方案筛选", "")
    if candidates:
        missing = [
            label
            for label in ("身体驱动", "物件驱动", "环境驱动")
            if label not in candidates
        ]
        if missing:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "CANDIDATE_FAMILIES_MISSING",
                    "动画方案筛选缺少候选族：" + "、".join(missing),
                )
            )
        score_tokens = re.findall(r"(?:[0-9]|[12][0-9]|30)\s*/\s*30", candidates)
        if len(score_tokens) < 3:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "CANDIDATE_SCORES_MISSING",
                    "动画方案筛选需给身体、物件、环境三套候选各一个六轴总分（x/30）。",
                )
            )
        if not re.search(r"入选|选择|淘汰|主引擎", candidates):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "CANDIDATE_DECISION_MISSING",
                    "动画方案筛选未写入选/淘汰决定。",
                )
            )

    mechanism_selection = values.get("表达机制选型", "")
    if mechanism_selection:
        domains = re.findall(
            r"形体域|意象域|空间域|时间域|媒介域|身体形体|意象外化|异常空间|回忆时间|混合媒介|喜剧转场",
            mechanism_selection,
        )
        if len(set(domains)) < 3:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "MECHANISM_IDEATION_DOMAINS_THIN",
                    "表达机制选型少于三个发散域；应在形体、意象、空间、时间/回忆、媒介/声音/喜剧中先比较再选择。",
                )
            )
        if not re.search(r"主机制|入选|选择|采用", mechanism_selection):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "MECHANISM_SELECTION_DECISION_MISSING",
                    "表达机制选型未写主机制入选决定。",
                )
            )

    engine = values.get("段级主表达引擎", "")
    if engine and len(re.sub(r"\s+", "", engine)) < 16:
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "SEGMENT_ENGINE_THIN",
                "段级主表达引擎过短；应贯通触发、主变量、接力、换手、归模和残留。",
            )
        )

    score = values.get("动画表达评分", "")
    if score:
        for axis in ("动画专属性", "因果接力", "观看权限", "表演完整度", "视觉留存", "情绪精度"):
            axis_value = re.search(rf"{axis}\s*[：:=]?\s*([0-5])\s*/\s*5", score)
            if not axis_value:
                findings.append(
                    Finding(
                        "ERROR",
                        "全文",
                        "EXPRESSION_SCORE_AXIS_MISSING",
                        f"动画表达评分缺少0-5数值维度：{axis}",
                    )
                )
            elif int(axis_value.group(1)) == 0:
                findings.append(
                    Finding(
                        "ERROR",
                        "全文",
                        "EXPRESSION_SCORE_AXIS_ZERO",
                        f"动画表达评分存在零分维度：{axis}；必须重做。",
                    )
                )
        total = re.search(r"总分\s*[：:=]?\s*([0-9]|[12][0-9]|30)\s*/\s*30", score)
        if not total:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "EXPRESSION_SCORE_TOTAL_MISSING",
                    "动画表达评分缺少总分（x/30）。",
                )
            )
        elif int(total.group(1)) < 24:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "EXPRESSION_SCORE_TOO_LOW",
                    "动画表达评分低于24/30，需重做表达引擎或接力链。",
                )
            )


def detected_world_axes(text: str) -> list[str]:
    return [
        name
        for name, pattern in WORLD_AXIS_PATTERNS.items()
        if pattern.search(text)
    ]


def validate_mixed_reality_document(text: str, findings: list[Finding]) -> None:
    values: dict[str, str] = {}
    for name, pattern in MIXED_REALITY_DOCUMENT_PATTERNS.items():
        value = field_value(text, pattern)
        if value is None:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "MISSING_MIXED_REALITY_FIELD",
                    f"缺少2D入现实字段：{name}",
                )
            )
        elif not value.strip():
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "EMPTY_MIXED_REALITY_FIELD",
                    f"2D入现实字段为空：{name}",
                )
            )
        else:
            values[name] = value.strip()

    route = values.get("混合现实路由", "")
    if route and not (
        re.search(r"2D|二维|手绘|drawn", route, re.I)
        and re.search(r"真人|实拍|底片|live[-\s]+action|plate", route, re.I)
    ):
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "MIXED_REALITY_ROUTE_UNCLEAR",
                "混合现实路由必须明确2D主体表演与真人/实拍底片并存。",
            )
        )

    plate = values.get("真人底片锁", "")
    if plate:
        plate_groups = (
            r"视平线|透视|消失点|horizon|perspective",
            r"摄影机|机位|镜头运动|camera",
            r"深度|前景|中景|后景|遮挡|depth|occlusion",
            r"光源|光线|色温|阴影|light",
            r"颗粒|景深|运动模糊|压缩噪声|grain|blur",
            r"真人NPC|真人同学|真人学生|路人|人群|路线|real[-\s]+NPC",
        )
        covered = sum(bool(re.search(pattern, plate, re.I)) for pattern in plate_groups)
        if covered < 5:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "LIVE_ACTION_PLATE_LOCK_THIN",
                    "真人底片锁需覆盖透视、摄影机、深度、光、摄影质感和真人NPC路线中的至少五类。",
                )
            )

    drawn = values.get("2D角色层锁", "")
    if drawn:
        drawn_groups = (
            r"身份|身高|尺度|比例|轮廓|identity|scale",
            r"粗线|铅笔|干笔|断线|断续|重画|线条|rough\s+line",
            r"平涂|填色|阴影块|纸面|flat\s+fill",
            r"分拍|曝光|帧感|线沸腾|失帧|cadence|line\s+boil",
            r"离模|归模|锚点|off[-\s]+model|return",
        )
        covered = sum(bool(re.search(pattern, drawn, re.I)) for pattern in drawn_groups)
        if covered < 4:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "DRAWN_CHARACTER_LOCK_THIN",
                    "2D角色层锁需覆盖身份尺度、粗线、填色、帧感和离模归模中的至少四类。",
                )
            )

    integration = values.get("跨媒介融合证据", "")
    if integration:
        checks = (
            (
                r"支点|脚底|座面|手掌|接触|承重|support|contact",
                "MISSING_SHARED_SUPPORT_PROOF",
                "跨媒介融合缺少共同地面/座面、支点或接触证明。",
            ),
            (
                r"前后遮挡|遮挡交换|从.{0,8}(?:前方|后方)|穿出|occlusion",
                "MISSING_DEPTH_OCCLUSION_PROOF",
                "跨媒介融合缺少真人/实物与2D角色的前后遮挡交换。",
            ),
            (
                r"投影|影子|反射|倒影|视差|景深|运动模糊|shadow|reflection|parallax",
                "MISSING_OPTICAL_INTEGRATION_PROOF",
                "跨媒介融合缺少投影、反射、视差、景深或运动模糊证据。",
            ),
            (
                r"形变|褶皱|位移|弯曲|湿痕|反光|材质|声响|material",
                "MISSING_REAL_MATERIAL_CONSEQUENCE",
                "跨媒介接触后没有真实道具或材质后果。",
            ),
        )
        for pattern, code, message in checks:
            if not re.search(pattern, integration, re.I):
                findings.append(Finding("ERROR", "全文", code, message))

    if re.search(r"遮挡|挡住|遮住|occlusion", text, re.I) and re.search(
        r"挥手|指向|松手|接物|递出|递回|收回|指尖|手掌|handoff|wave|point", text, re.I
    ):
        if not re.search(
            r"可见(?:起势|结果|侧)|重新出现|从遮挡后.{0,12}(?:出现|穿出|收回)|交还观看权限|恢复观看权限|visible[-\s]+side|reappear",
            text,
            re.I,
        ):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "OCCLUDED_GESTURE_VISIBILITY_MISSING",
                    "遮挡中的关键手势缺少可见起势/结果或遮挡后的观看权限交还。",
                )
            )

    distinction = values.get("手绘区别保留", "")
    if distinction:
        if not re.search(r"粗线|断续|断线|重画|压力|线沸腾|铅笔|干笔|line", distinction, re.I):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "HANDDRAWN_LINE_DISTINCTION_MISSING",
                    "手绘区别未写线条压力、断续、重画痕或线沸腾。",
                )
            )
        if not re.search(r"分拍|曝光|帧感|失帧|姿势跳跃|cadence|frame", distinction, re.I):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "HANDDRAWN_CADENCE_DISTINCTION_MISSING",
                    "手绘区别未写选择性分拍、曝光节奏或可读的失帧姿势跳跃。",
                )
            )

    tail = values.get("双层尾态", "")
    if tail and not (
        re.search(r"底片|摄影机|真人|plate", tail, re.I)
        and re.search(r"2D|二维|手绘|线条", tail, re.I)
        and re.search(r"下一|继承|继续|入口|尾帧", tail, re.I)
    ):
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "DUAL_LAYER_TAIL_INCOMPLETE",
                "双层尾态必须同时锁定真人底片、2D角色和下一拍继承。",
            )
        )


def detected_world_rewrite_families(text: str) -> list[str]:
    return [
        name
        for name, pattern in WORLD_REWRITE_FAMILY_PATTERNS.items()
        if pattern.search(text)
    ]


def validate_scene_document(text: str, findings: list[Finding]) -> None:
    values: dict[str, str] = {}
    for name, pattern in SCENE_DOCUMENT_PATTERNS.items():
        value = field_value(text, pattern)
        if value is None:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "MISSING_SCENE_DOCUMENT_FIELD",
                    f"缺少动画场景规划字段：{name}",
                )
            )
        elif not value.strip():
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "EMPTY_SCENE_DOCUMENT_FIELD",
                    f"动画场景规划字段为空：{name}",
                )
            )
        else:
            values[name] = value.strip()

    fact_lock = values.get("导演事实锁", "")
    if fact_lock:
        required_fact_groups = (
            r"剧情|因果|任务",
            r"信息|知情|误读|知道|确认",
            r"空间|站位|轴线",
            r"时长|秒",
            r"尾态|尾帧|结尾",
        )
        missing_count = sum(
            1 for pattern in required_fact_groups if not re.search(pattern, fact_lock)
        )
        if missing_count:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "DIRECTOR_FACT_LOCK_THIN",
                    "导演事实锁未完整覆盖剧情/信息、现实空间站位、时长和必须尾态。",
                )
            )

    proposition = values.get("动画视觉命题", "")
    if proposition:
        if len(re.sub(r"\s+", "", proposition)) < 16 or not re.search(
            r"每|逐|开始|变成|改写|改变|折起|折叠|压缩|压扁|挤压|拉长|拉开|撤走|关闭|吞没|生成|复制|夺走|失去|留下",
            proposition,
        ):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "VISUAL_PROPOSITION_NOT_ACTIONABLE",
                    "动画视觉命题必须是世界如何随戏剧变化的可画动词句，而非风格或情绪标签。",
                )
            )

    mutability_scan = values.get("世界可变性扫描", "")
    if mutability_scan:
        axes = detected_world_axes(mutability_scan)
        if len(axes) < len(WORLD_AXIS_PATTERNS):
            missing = [name for name in WORLD_AXIS_PATTERNS if name not in axes]
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "WORLD_AXIS_SCAN_INCOMPLETE",
                    "世界可变性扫描未覆盖全部十二轴，缺少：" + "、".join(missing),
                )
            )

    active_axes = values.get("激活世界轴", "")
    if active_axes:
        active_part = re.split(r"未激活|其余|保持现实", active_axes, maxsplit=1)[0]
        axes = detected_world_axes(active_part)
        if len(axes) < 2:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "ACTIVE_WORLD_AXES_TOO_FEW",
                    "激活世界轴少于两根；动画场景至少需要两类非摄影变量形成因果接力。",
                )
            )
        elif len(axes) > 5:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "ACTIVE_WORLD_AXES_OVERLOADED",
                    "激活世界轴超过五根；应选择2-4根主轴，复杂段最多五根，其余保持现实基准。",
                )
            )

    architectures = values.get("场景架构候选", "")
    if architectures:
        families = set(
            re.findall(
                r"形体|身份|空间|物理|时间|记忆|环境|群体|物件|图形|媒介|喜剧",
                architectures,
            )
        )
        if len(families) < 3:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "SCENE_ARCHITECTURE_DIVERSITY_THIN",
                    "场景架构候选少于三种真正不同的世界组织方式。",
                )
            )
        if not re.search(r"入选|选择|采用|淘汰|主架构", architectures):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "SCENE_ARCHITECTURE_DECISION_MISSING",
                    "场景架构候选未写入选与淘汰决定。",
                )
            )

    scene_plan = values.get("动画场景规划", "")
    if scene_plan:
        missing = [
            label
            for label in ("主世界法则", "反法则", "接力棒", "现实锚点", "归还", "残留")
            if label not in scene_plan
        ]
        if missing:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "SCENE_WORLD_LAW_FIELDS_MISSING",
                    "动画场景规划缺少：" + "、".join(missing),
                )
            )

    state_graph = values.get("视觉状态图", "")
    if state_graph:
        state_ids = {
            int(value)
            for value in re.findall(r"(?<![A-Za-z0-9])S([0-9]+)(?![0-9])", state_graph, re.I)
        }
        state_count = len(state_ids)
        if state_count < 4 or state_count > 7:
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "SCENE_STATE_COUNT_INVALID",
                    f"视觉状态图读到{state_count}态；场景规划需要4-7个意义不同的状态。",
                )
            )
        if not re.search(r"->|→|⇒|=>|—>", state_graph):
            findings.append(
                Finding(
                    "ERROR",
                    "全文",
                    "SCENE_STATE_GRAPH_NOT_LINKED",
                    "视觉状态图未写状态之间的因果或接力顺序。",
                )
            )

    shot_strategy = values.get("动画镜头策略", "")
    if shot_strategy and not re.search(
        r"观看|画面所有者|投影|透视|图层|画框|基准|对照|判决|落地",
        shot_strategy,
    ):
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "ANIMATION_SHOT_STRATEGY_GENERIC",
                "动画镜头策略未说明观看权限、投影/图层变化或常规镜头只承担的基准/落地任务。",
            )
        )

    rewrite_families = detected_world_rewrite_families(text)
    if len(rewrite_families) < 2:
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "NO_ANIMATION_WORLD_REWRITE",
                "场景未读到至少两类可执行世界改写；时间、空间、物理、人物形象、媒介、投影、环境、群体、声音文字或转场仍被当成固定背景。",
            )
        )

    coverage_hits = CONVENTIONAL_COVERAGE_MARKERS.findall(text)
    if len(coverage_hits) >= 3 and len(rewrite_families) < 2:
        findings.append(
            Finding(
                "ERROR",
                "全文",
                "LIVE_ACTION_COVERAGE_DEGENERATION",
                "场景主要依赖中景/过肩/正反打/反应或道具特写，删掉摄影机术语后没有独立动画世界法则。",
            )
        )


def validate_block(block: str, beat: str, mode: str, profile: str) -> list[Finding]:
    findings: list[Finding] = []
    values: dict[str, str] = {}

    for name, pattern in FIELD_PATTERNS.items():
        value = field_value(block, pattern)
        if value is None:
            findings.append(Finding("ERROR", beat, "MISSING_FIELD", f"缺少字段：{name}"))
        elif not value.strip():
            findings.append(Finding("ERROR", beat, "EMPTY_FIELD", f"字段为空：{name}"))
        else:
            values[name] = value.strip()

    if "四项强度" in values:
        validate_intensities(block, beat, findings)
    if "关键姿势链" in values:
        validate_pose_chain(values["关键姿势链"], beat, findings)
    validate_motion_completeness(values, block, beat, findings, profile)
    validate_compound_camera_path(values, beat, findings)

    baseline = values.get("正常基准", "")
    if baseline and len(re.sub(r"\s+", "", baseline)) < 8:
        findings.append(
            Finding(
                "WARNING",
                beat,
                "BASELINE_THIN",
                "正常基准过短；应包含姿势、支点、任务循环或正常节拍中的至少两项。",
            )
        )

    mutation = values.get("动画镜头突变", "")
    if mutation and len(re.sub(r"\s+", "", mutation)) < 16:
        findings.append(
            Finding(
                "WARNING",
                beat,
                "SHOT_MUTATION_THIN",
                "动画镜头突变过短；关键阈值应写画面所有者、触发、越界变量、身体后果、现实锚点和落地帧。",
            )
        )

    ecology = values.get("环境/物件/NPC表演", "")
    if ecology and len(re.sub(r"\s+", "", ecology)) < 16:
        findings.append(
            Finding(
                "WARNING",
                beat,
                "ECOLOGY_THIN",
                "环境/物件/NPC表演过短；应说明哪一层响应、误读、继续日常或接管余波。",
            )
        )

    if mode == "handoff":
        for pattern in POSITIVE_ONLY_FORBIDDEN:
            if re.search(pattern, block, re.I):
                findings.append(
                    Finding(
                        "ERROR",
                        beat,
                        "NEGATIVE_MODEL_LANGUAGE",
                        f"承接内容出现负面式模型指令：{pattern}",
                    )
                )
        for pattern in SOURCE_MARKERS:
            if re.search(pattern, block, re.I):
                findings.append(
                    Finding(
                        "ERROR",
                        beat,
                        "SOURCE_OR_IP_MARKER",
                        "承接内容出现作品/IP/作者来源标记；请改写为可执行画面属性。",
                    )
                )

    if profile in ("expressive", "scene"):
        validate_expressive_fields(block, beat, findings)
        if mode == "handoff":
            validate_expressive_handoff(block, beat, findings)

    return findings


def validate_document(text: str, mode: str, profile: str) -> tuple[list[Finding], int]:
    beats = split_beats(text)
    findings: list[Finding] = []
    if profile in ("expressive", "scene"):
        validate_expressive_document(text, findings)
    if profile == "scene":
        validate_scene_document(text, findings)
    if profile == "mixed-reality":
        validate_mixed_reality_document(text, findings)
    for beat, block in beats:
        findings.extend(validate_block(block, beat, mode, profile))
    return findings, len(beats)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate formal 2D animation-performance artifacts."
    )
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--mode", choices=["formal", "handoff"], default="formal")
    parser.add_argument(
        "--profile",
        choices=["standard", "expressive", "scene", "mixed-reality"],
        default="standard",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    if not args.artifact.is_file():
        print(f"ERROR: artifact not found: {args.artifact}", file=sys.stderr)
        return 2

    text = args.artifact.read_text(encoding="utf-8-sig")
    findings, beat_count = validate_document(text, args.mode, args.profile)
    errors = [item for item in findings if item.level == "ERROR"]
    warnings = [item for item in findings if item.level == "WARNING"]

    if args.json_output:
        payload = {
            "artifact": str(args.artifact),
            "mode": args.mode,
            "profile": args.profile,
            "beats": beat_count,
            "errors": len(errors),
            "warnings": len(warnings),
            "findings": [asdict(item) for item in findings],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item.level} [{item.beat}] {item.code}: {item.message}")
        status = "PASS" if not errors else "FAIL"
        print(
            f"{status}: {args.artifact} | mode={args.mode} | beats={beat_count} "
            f"| profile={args.profile} | errors={len(errors)} | warnings={len(warnings)}"
        )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
