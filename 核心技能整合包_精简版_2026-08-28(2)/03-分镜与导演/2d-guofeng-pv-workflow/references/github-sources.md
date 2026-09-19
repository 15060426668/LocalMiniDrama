# GitHub Sources and Absorption Log

检索日期：2026-08-20。公开仓库只作为可追溯参考，不把第三方代码、品牌资产或外部服务凭据写进本技能。

## 已下载并吸收

### `Vincentwei1021/video-shotcraft`

- URL: https://github.com/Vincentwei1021/video-shotcraft
- 许可：仓库声明的 MIT；音频与外部素材另看各自授权。
- 本地：`F:/剧本创作四步骤/codex-skills/video-shotcraft`
- 吸收：镜头配方卡的“用途/能量/帧预算/命门”结构；真实运动机制优先于口号；运动与声音因果；逐镜头静帧、连帧、整片 QA；`riser -> impact -> sparkle` 作为一次性峰值句式。
- 不吸收：产品截图、品牌文案、Ink Press 产品模板、网页产品视觉、音频文件作为江湖默认资产。
- 适用边界：只在 `2d-guofeng-pv-workflow` 已确定镜头职责后查阅对应卡片，不让它替代正式分镜或表演技能。

## 已下载、只抽取规则

### `nextlevelbuilder/ui-ux-pro-max-skill`

- URL: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- 许可：仓库公开声明 MIT；外部模型依赖另行核对。
- 本地缓存：`.github-sources/ui-ux-pro-max-skill.zip`
- 吸收：设计/品牌/设计系统的分层思路；资产命名与一致性检查；视觉 token、版式层级和审查清单的“先定义系统、再批量输出”原则。
- 不吸收：网页 UI、Tailwind/shadcn、Gemini API、社交广告尺寸、Logo/CIP 业务流程。
- 适用边界：只转化为 `style-dna` 和 `layout-asset-board` 的字段与验收，不启用其外部 API。

## 已下载、暂不接入

### `ng-galien/maket`

- URL: https://github.com/ng-galien/maket
- 许可：MIT；仓库说明 Node.js >=22、Puppeteer/Chromium 和 MCP 配置。
- 本地缓存：`.github-sources/maket.zip`
- 价值：真实 HTML/CSS 画布、实时预览、资产库、数据驱动集合、文档状态、`maket_html check` 溢出/重叠检查、PDF 导出；这正是“重新排版、整合、分组”的外部工作台形态。
- 暂不接入原因：它是独立 MCP 应用，不是单一知识技能；安装会引入 Node/Chromium、端口、数据目录和 Codex 配置变更。当前 2D PV 先用本技能的无依赖 `render_pv_board.py`，等你确实需要交互式画布时再单独启用。
- 安全边界：不运行 `maket install codex --apply`，不写全局 `~/.codex/config.toml`，不启用 Gmail 或外部 OAuth。

## 结论

这次没有把第三方仓库整包拼进主技能。主技能只留下能解释、能验证、能迁移到原创江湖 PV 的小集合；原始 ZIP 和完整 `video-shotcraft` 目录保留用于追溯和按需查卡。
