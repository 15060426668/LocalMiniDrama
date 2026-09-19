# Skill 整合说明

## 整合概述

已将 `核心技能整合包_精简版_2026-08-28(2)` 整合到 LocalMiniDrama 项目中，实现 AI 提示词自动调用对应 skill 的功能。

## 文件结构

```
backend-node/
├── skills/                          # Skill 技能包目录
│   ├── 01-图像生成/
│   │   ├── gpt-image-prompt-field-manual/
│   │   ├── mj-cinematic-image-prompt/
│   │   ├── mj-takopi-2d-house-style/
│   │   ├── mj-xianxia-megastructure/
│   │   ├── psychological-anime-imagegen/
│   │   └── qidu-aigc-prompt-atelier/
│   ├── 02-视频生成/
│   │   ├── video-prompt-workbench/
│   │   ├── dream-suspense-sd/
│   │   ├── video-shotcraft/
│   │   └── black-subtractive-mixed-media/
│   ├── 03-分镜与导演/
│   ├── 04-剧本与对白/
│   └── 05-分析、训练与资产/
└── src/
    ├── services/
    │   ├── skillLoader.js           # Skill 加载器（新增）
    │   └── aiClient.js              # 已修改：支持 Skill 注入
    └── routes/
        ├── skills.js                # Skill API 路由（新增）
        └── index.js                 # 已修改：注册 skills 路由

frontweb/
└── src/
    └── api/
        └── skills.js                # 前端 Skill API（新增）
```

## 工作原理

### 1. Skill 加载器 (`skillLoader.js`)

- 从 `backend-node/skills/` 目录读取所有 skill 的 `SKILL.md` 文件
- 解析 frontmatter 元数据（name, description）
- 提供 skill 到 scene_key 的映射关系

### 2. AI Client 修改 (`aiClient.js`)

在 `generateText()` 函数中添加了 Skill 注入逻辑：

```javascript
// 若 scene_key 对应可用 skill，将其 instructions 合并到 system prompt
if (scene_key) {
  const skillName = skillLoader.getSkillForScene(scene_key);
  if (skillName) {
    const skillPrompt = skillLoader.buildSkillSystemPrompt(skillName);
    if (skillPrompt) {
      effectiveSystemPrompt = skillPrompt + '\n\n--- Original System Instructions ---\n' + effectiveSystemPrompt;
    }
  }
}
```

### 3. Scene Key 到 Skill 的映射

| Scene Key | 对应 Skill | 用途 |
|-----------|-----------|------|
| `role_extraction` | `gpt-image-prompt-field-manual` | 角色提取时的外貌描述优化 |
| `character_extraction` | `gpt-image-prompt-field-manual` | 角色提取 |
| `identity_anchors` | `gpt-image-prompt-field-manual` | 角色身份锚点提炼 |
| `prop_extraction` | `gpt-image-prompt-field-manual` | 道具提取 |
| `scene_extraction` | `gpt-image-prompt-field-manual` | 场景提取 |
| `first_frame_prompt` | `mj-cinematic-image-prompt` | 首帧图像提示词生成 |
| `key_frame_prompt` | `mj-cinematic-image-prompt` | 关键帧图像提示词生成 |
| `last_frame_prompt` | `mj-cinematic-image-prompt` | 尾帧图像提示词生成 |
| `panel_prompt` | `mj-cinematic-image-prompt` | 四宫格提示词生成 |
| `action_prompt` | `mj-cinematic-image-prompt` | 动作序列提示词生成 |
| `image_polish` | `qidu-aigc-prompt-atelier` | 图像提示词润色 |
| `role_image_polish` | `qidu-aigc-prompt-atelier` | 角色图像润色 |
| `prop_image_polish` | `qidu-aigc-prompt-atelier` | 道具图像润色 |
| `video_prompt_sd` | `dream-suspense-sd` | 视频生成提示词（SD/Seedance） |

### 4. API 端点

后端新增三个 API：

- `GET /api/skills` - 列出所有可用 skill
- `GET /api/skills/:name` - 获取 skill 元信息
- `GET /api/skills/:name/content` - 获取 skill 完整内容

## 使用方式

### 自动模式（默认）

项目运行时，AI 调用会自动注入对应 skill 的 instructions。无需任何配置。

### 查看可用 Skills

启动项目后访问：`http://127.0.0.1:3013/api/skills`

### 禁用 Skill 注入

如需禁用某个 scene_key 的 skill 注入，编辑 `backend-node/src/services/skillLoader.js` 中的 `getSkillForScene()` 函数，将对应 skill 设为 `null`。

## 向后兼容性

- ✅ 所有原有功能保持不变
- ✅ Skill 注入是**追加**到原有 system prompt 之前，不会覆盖原有逻辑
- ✅ 若 skill 不存在或映射为 null，则使用原有 system prompt
- ✅ 前端无需修改即可享受 skill 增强

## 最新更新

### 分镜时长动态设置（2026-09-19）

**问题**：之前分镜生成时，所有镜头都被强制设置为固定的秒数（如项目配置的 15 秒/段）。

**解决**：现在根据 skill 指导，AI 会根据内容动态设置每个分镜的时长：
- 内部动作拍通常为 **2-4 秒**
- 按动作完成、台词停顿、信息改变、遮挡或镜头落点划分
- 快速动作/对白用较短时长，复杂运动/情绪节拍用较长时长
- 项目配置的秒数仅作为参考上限，不再强制

**修改文件**：
- [episodeStoryboardService.js](file:///d:/Program%20Files/Github/LocalMiniDrama/backend-node/src/services/episodeStoryboardService.js#L1125-L1224) - 更新提示词约束
- [promptI18n.js](file:///d:/Program%20Files/Github/LocalMiniDrama/backend-node/src/services/promptI18n.js#L445-L477) - 更新时长说明

## 扩展 Skills

如需添加新 skill：

1. 在 `backend-node/skills/` 下创建新目录
2. 添加 `SKILL.md` 文件（必须包含 frontmatter）
3. 在 `skillLoader.js` 的 `getSkillForScene()` 中添加映射

## 启动项目

```bash
# Windows
cd "d:\Program Files\Github\LocalMiniDrama"
run_dev.bat

# 或手动启动
cd backend-node && npm run dev
cd frontweb && npm run dev
```

访问：
- 后端：http://127.0.0.1:3013
- 前端：http://127.0.0.1:5173