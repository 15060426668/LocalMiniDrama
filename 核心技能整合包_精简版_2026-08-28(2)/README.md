# 核心技能整合包（精简版）

整理日期：2026-08-28

这是当前工作区 `codex-skills` 的可复用技能归档，按使用场景重新分组。每个技能目录保留原有 `SKILL.md`、参考资料、脚本、测试夹具和必要的示例资产。

## 快速入口

| 分组 | 用途 | 技能 |
|---|---|---|
| 01-图像生成 | GPT/DALL-E、Midjourney、统一画风、国风巨构、心理动画静帧、提示词修整 | `gpt-image-prompt-field-manual`、`mj-cinematic-image-prompt`、`mj-takopi-2d-house-style`、`mj-xianxia-megastructure`、`psychological-anime-imagegen`、`qidu-aigc-prompt-atelier` |
| 02-视频生成 | 通用视频提示词、图生视频/文生视频、SD/Seedance、成片视频制作 | `video-prompt-workbench`、`dream-suspense-sd`、`video-shotcraft`、`black-subtractive-mixed-media` |
| 03-分镜与导演 | 分镜方案与细则、动画表演、国风 PV、构图训练、真人场面调度、分镜训练维护 | `director-storyboard-integrated`、`animation-suspense-performance`、`2d-guofeng-pv-workflow`、`cinematic-composition-coach`、`live-action-spatial-previs`、`director-storyboard-training-maintainer` |
| 04-剧本与对白 | 故事框架、正式剧本、悬疑写作、剧本圆桌诊断、台词诊断 | `story-framework`、`script-writing`、`mystery-writer`、`script-roundtable`、`dialogue-doctor` |
| 05-分析、训练与资产 | 影片拉片、场景拆分、空间资产前置 | `video-story-analysis`、`scene-asset-decomposition` |

项目内调用索引位于包根目录：`本地技能调用索引.md`。

## 推荐主流程

```text
story-framework
-> script-writing
-> script-roundtable
-> dialogue-doctor
-> director-storyboard-integrated
   + animation-suspense-performance
-> dream-suspense-sd
-> 生成结果 QA 与回修
```

已有成片时：`video-story-analysis -> director-storyboard-integrated`。

场景图/平面图前置时：`scene-asset-decomposition -> live-action-spatial-previs -> director-storyboard-integrated`。

## 归档说明

- `codex-skills` 中的 23 个现行技能全部纳入，包含参考资料和配套脚本。
- 本精简版不含 3D 导演台源码、旧版 6 份 Skill 模板和历史分镜训练协议；这些内容已从当前主流程中剥离，原工作区源文件不受影响。
- `black-subtractive-mixed-media` 的原始样片、逐秒抽帧和视频案例数据已移除，只保留技能说明、参考规则和脚本。
- `video-shotcraft` 的镜头卡、模板、demo、组件和音频资产保留，因为它们是该视频制作技能的可执行依赖。
- 排除了 `node_modules`、`.vite`、`dist`、Python `__pycache__`、临时文件和工作区缓存。

## 使用方式

解压后进入对应技能目录，阅读 `SKILL.md`。技能之间的调用边界、标准流程和声音工具链见 `本地技能调用索引.md`。
