# Layout and Asset Board

## 板不是文件夹列表

文件夹按素材来源组织，版式板按制作决策组织。一个资产可以同时出现在“角色”“镜头 03”“前景遮挡”和“可复用道具”四个视图中，但只能有一个稳定 ID 和一个主文件来源。

## 资产最小字段

| 字段 | 说明 | 示例 |
|---|---|---|
| `id` | 稳定资产 ID，不随排版变化 | `char_shenyi_portrait_v02` |
| `class` | `character/costume/weapon/prop/fg/mg/bg/fx/text/sound` | `weapon` |
| `name` | 人能读的中文名 | `沉衣_短刀_拔刀姿态` |
| `source` | 原始路径、截图、参考片时间码或用户提供 | `refs/shenyi_knife.png` |
| `roi` | 从来源取出的区域；未知就写 `U` | `x=0.42,y=0.16,w=0.31,h=0.71` |
| `evidence` | `O` 观察到、`I` 输入明确提供、`U` 未知/待证 | `I` |
| `version` | 版本或校验标识 | `v02` |
| `depth` | `fg/mg/bg` 或 `flat` | `mg` |
| `shots` | 所属镜头 ID 列表 | `S02,S05` |
| `reuse` | 可复用范围和限制 | `可换色，不可镜像` |
| `status` | `need/rough/approved/hold/rejected` | `approved` |

## 三种分组视图

### 1. 按制作阶段

`brief -> styleframe -> asset extraction -> shot ledger -> performance -> sound -> render QA`

每个阶段只展示它需要的字段，避免把最终分镜、未验收资产和灵感图片混在一个长文档里。

### 2. 按画面层级

```text
FG：门框、雨帘、纸角、飞尘、遮挡手
MG：角色、兵器、桌案、旗幡、近处建筑
BG：山门、城郭、长路、地图、天空、雾
FX：墨渗、描线、冲击线、纸屑、光束
TEXT：片名、地点、门派、章回、印章
SOUND：环境底、动作音、重拍、尾音
```

这个视图用于检查 2D 合成是否有前后景、遮挡和动势，而不是把所有东西都画在一张平面上。

### 3. 按叙事功能

`identity / relationship / place / threat / action / consequence / handoff`

每个镜头至少有一个身份功能和一个动作/后果功能；只有“好看”而没有功能的资产放入 `hold`，不能进入主镜头。

## 镜头台账最小字段

| 字段 | 必填内容 |
|---|---|
| `id` | `S01`、`S02` 等稳定编号 |
| `group` | `opening/hero/relationship/conflict/ensemble/outro` |
| `time` | 起止秒或帧数 |
| `purpose` | 该镜头改变了什么信息/关系 |
| `subject` | 主体、对方、关键物件 |
| `action` | 一个主动作语法和七拍动作链摘要 |
| `camera` | 景别、方向、运动、轴线状态 |
| `layers` | 使用的资产 ID 和 FG/MG/BG 层级 |
| `sound` | 触发点、音色、尾音、是否交棒 |
| `tail` | 结尾静止状态或下一镜入口 |
| `risk` | 角色一致性、空间连续性、墨效因果等风险 |

## 排版规则

1. 先按 `group` 排镜头，再按时间排序；不要按资产名称排序后假装是时间线。
2. 组内先显示镜头 ID、目的和主体，再显示素材细节；扫描时先判断叙事，再检查资源。
3. 资产板默认显示 `status != rejected`，但保留筛选查看被拒版本，避免误删历史决策。
4. 同一角色的多个版本必须相邻，明确 `approved` 版本和差异；不要把相似 PNG 当成独立角色。
5. 未知字段保持 `U`，不能用“看起来像”填成精确坐标、镜头或材质。
6. 一张板只突出一种比较关系：按镜头、按资产类或按角色；多种关系用标签/筛选，不用嵌套卡片堆叠。

## 文件命名

推荐格式：`{class}_{subject}_{function}_{version}.{ext}`。

示例：

```text
char_shenyi_identity_v02.png
weapon_shortblade_draw_action_v01.png
bg_qinghe_gate_establish_v03.png
fx_ink_bleed_scene03_v01.png
text_chapter_01_v01.txt
```

中文工作区可以保留中文可读名，但 ID 仍保持稳定的 ASCII 片段，便于脚本、剪辑和版本追踪。

## 与现有技能的交接

- 场景图、平面图和切面：先交 `scene-asset-decomposition`，它负责证据状态和空间母版。
- 已确认的空间坐标和相机：交 `live-action-spatial-previs` 或 `director-storyboard-integrated`。
- 角色动作、衣摆、兵器轨迹：交 `animation-suspense-performance`。
- 需要网页化预览、排序和筛选：运行 `scripts/render_pv_board.py`。
