# Skill 整合更新说明

## 问题诊断

之前分镜生成时，所有镜头的 duration 都被设置为相同的固定值（如 5 秒），原因如下：

1. **Skill 未正确加载** - `storyboard_extraction` 映射为 `null`，导致 skill 未被注入
2. **固定时长覆盖** - 代码中使用 `targetClipDuration` 强制覆盖 AI 返回的 duration
3. **路径解析错误** - `readSkillMarkdown` 无法找到嵌套目录中的 skill 文件

## 解决方案

### 1. 修复 Skill 加载路径

**文件**: `backend-node/src/services/skillLoader.js`

**问题**: Skill 文件位于 `skills/03-分镜与导演/director-storyboard-integrated/SKILL.md`，但代码直接查找 `skills/director-storyboard-integrated/SKILL.md`

**解决**: 添加 `buildSkillPathCache()` 函数，递归扫描所有子目录构建路径缓存

```javascript
const _skillPathCache = {};

function buildSkillPathCache() {
  if (Object.keys(_skillPathCache).length > 0) return;
  
  const items = fs.readdirSync(SKILLS_DIR, { withFileTypes: true });
  for (const group of items) {
    if (!group.isDirectory()) continue;
    const groupPath = path.join(SKILLS_DIR, group.name);
    const subItems = fs.readdirSync(groupPath, { withFileTypes: true });
    for (const sub of subItems) {
      if (!sub.isDirectory()) continue;
      const skillPath = path.join(groupPath, sub.name, 'SKILL.md');
      if (fs.existsSync(skillPath)) {
        _skillPathCache[sub.name] = skillPath;
      }
    }
  }
}
```

### 2. 更新 Skill 映射

**文件**: `backend-node/config/skill.config.js` (新建)

将 scene_key 到 skill 的映射提取到配置文件：

```javascript
const SCENE_TO_SKILL_MAP = {
  storyboard_extraction: 'director-storyboard-integrated',
  storyboard_system: 'director-storyboard-integrated',
  storyboard_universal: 'director-storyboard-integrated',
  // ... 其他映射
};
```

### 3. 移除固定时长覆盖

**文件**: `backend-node/src/services/episodeStoryboardService.js`

**修改前**:
```javascript
const targetClip = opts.targetClipDuration != null ? Number(opts.targetClipDuration) : 0;
if (Number.isFinite(targetClip) && targetClip > 0) {
  durationSec = Math.max(durationSec, Math.round(targetClip)); // 强制覆盖！
}
```

**修改后**:
```javascript
// 不再使用 targetClipDuration 覆盖 AI 返回的时长，完全信任 AI 根据 skill 指导设置的 duration
durationSec = Math.min(STORYBOARD_DURATION_CONFIG.maxDuration, 
                       Math.max(STORYBOARD_DURATION_CONFIG.minDuration, 
                               Math.round(durationSec)));
```

### 4. 移除提示词中的固定时长约束

**文件**: `backend-node/src/services/episodeStoryboardService.js`

- 不再计算 `effectiveShotDuration`
- 不再从 `drama.metadata` 读取 `video_clip_duration`
- 传入 `null` 给 `getStoryboardUserPromptSuffix`

**文件**: `backend-node/src/services/promptI18n.js`

更新时长说明，让 AI 根据 skill 自主决定：

```javascript
const durationInstruction = durationHint
  ? `项目配置约${durationHint}秒/段（仅供参考，非强制）。根据 Skill 指导：每个镜头的 duration 应根据内容动态设置，通常为 2-4 秒...`
  : '根据 Skill 指导：每个镜头的 duration 应根据内容动态设置，通常为 2-4 秒，按动作完成、台词停顿、信息改变、遮挡或镜头落点划分';
```

### 5. 增强日志记录

**文件**: `backend-node/src/services/aiClient.js`

添加详细的 skill 注入日志：

```javascript
log.info('AI generateText: skill injected', { 
  scene_key, 
  skill: skillName, 
  skill_length: skillPrompt.length 
});
```

## Skill 内容

### director-storyboard-integrated

该 skill 包含完整的分镜指导，关键内容：

```
内部动作拍通常为 `2-4秒`，按动作完成、台词停顿、信息改变、遮挡或镜头落点划分。
```

Skill 会被注入到 system prompt 中，AI 在生成分镜时会遵循这些指导。

## 配置说明

### 分镜时长策略

**文件**: `backend-node/config/skill.config.js`

```javascript
const STORYBOARD_DURATION_CONFIG = {
  aiDecidedDuration: true,        // AI 自主决定时长
  minDuration: 1,                 // 最小 1 秒
  maxDuration: 120,               // 最大 120 秒
  defaultDuration: 5,             // AI 未返回时的默认值
  skillGuidance: {
    actionBeat: { min: 2, max: 4 },
    description: 'Set duration dynamically based on content...'
  },
};
```

### 自定义 Skill 映射

编辑 `backend-node/config/skill.config.js` 中的 `SCENE_TO_SKILL_MAP`：

```javascript
const SCENE_TO_SKILL_MAP = {
  // 修改映射
  storyboard_extraction: 'your-custom-skill',
  
  // 禁用 skill
  some_scene: null,
};
```

## 验证方法

### 1. 运行测试脚本

```bash
cd backend-node
node test-skill-loading.js
```

输出应显示：
```
Scene: storyboard_extraction
  Skill: director-storyboard-integrated
  Body length: 6843 chars
  Has duration guidance: YES ✓
```

### 2. 查看后端日志

生成分镜时，日志应显示：
```
AI generateText: skill injected {"scene_key":"storyboard_extraction","skill":"director-storyboard-integrated","skill_length":7366}
```

### 3. 检查分镜结果

调用分镜生成 API 后，检查返回的分镜数据：

```json
{
  "storyboards": [
    { "duration": 3, "title": "镜头1" },
    { "duration": 5, "title": "镜头2" },
    { "duration": 2, "title": "镜头3" },
    { "duration": 4, "title": "镜头4" }
  ]
}
```

每个分镜的 duration 应该不同，根据内容动态设置。

## 修改文件清单

1. ✅ `backend-node/config/skill.config.js` - 新建配置文件
2. ✅ `backend-node/src/services/skillLoader.js` - 修复路径缓存
3. ✅ `backend-node/src/services/episodeStoryboardService.js` - 移除固定时长
4. ✅ `backend-node/src/services/promptI18n.js` - 更新时长说明
5. ✅ `backend-node/src/services/aiClient.js` - 增强日志
6. ✅ `backend-node/test-skill-loading.js` - 测试脚本

## 下一步

所有 skill 相关的 scene_key 现在都会正确加载对应的 skill 内容。如果需要：

1. **添加新 skill** - 放入 `backend-node/skills/` 目录，更新映射配置
2. **修改时长策略** - 编辑 `STORYBOARD_DURATION_CONFIG`
3. **自定义提示词** - 修改 `promptI18n.js` 中的对应函数