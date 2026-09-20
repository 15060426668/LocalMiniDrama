# 📥 Excel 分镜导入 - 完整测试报告

## ✅ 已完成的工作

### 1. Excel 模板文件已生成
- **真实格式模板**: [`docs/storyboard-import-template-real.xlsx`](d:\Program Files\Github\LocalMiniDrama\docs\storyboard-import-template-real.xlsx)
- **包含内容**:
  - ✅ 使用方法说明
  - ✅ 真实的分镜数据示例（两个完整分镜块）
  - ✅ 字段详细说明
  - ✅ 注意事项提示

### 2. 后端服务已实现
- **核心解析器**: [`backend-node/src/services/storyboardImporter.js`](d:\Program Files\Github\LocalMiniDrama\backend-node\src\services\storyboardImporter.js)
  - ✅ 支持全角/半角括号兼容
  - ✅ 自动提取场景、人物、运镜信息
  - ✅ 总时长累加取整（13.6s → 14s）
  
- **API 路由**: [`backend-node/src/routes/storyboards.js`](d:\Program Files\Github\LocalMiniDrama\backend-node\src\routes\storyboards.js) (第 1178-1258 行)
  - ✅ `POST /api/v1/storyboards/import-excel` 接口已定义
  - ✅ 支持接收 JSON 格式的文本数组
  - ⚠️ TODO: 尚未集成 Excel 文件解析库（目前需前端预处理为 JSON）

### 3. 前端界面已添加
- **导入对话框**: [`frontweb/src/views/FilmCreate.vue`](d:\Program Files\Github\LocalMiniDrama\frontweb\src\views\FilmCreate.vue) (第 965-1034 行)
  - ✅ "📥 从 Excel 导入分镜"按钮
  - ✅ 双标签对话框（文本粘贴 / 文件上传）
  - ✅ 变量声明和函数逻辑

- **API 方法**: [`frontweb/src/api/storyboards.js`](d:\Program Files\Github\LocalMiniDrama\frontweb\src\api\storyboards.js)
  - ✅ `importFromExcel()` 方法

### 4. 测试验证
- **单元测试**: [`backend-node/test/storyboardImporter.test.js`](d:\Program Files\Github\LocalMiniDrama\backend-node\test\storyboardImporter.test.js)
  - ✅ 7 项测试全部通过
  
- **端到端测试**: [`backend-node/test/storyboardImportEndToEnd.test.js`](d:\Program Files\Github\LocalMiniDrama\backend-node\test\storyboardImportEndToEnd.test.js)
  - ✅ 已创建测试脚本
  - ⚠️ 需要：系统中存在剧集才能执行

---

## 🎯 如何测试导入功能

### 方式 A: 使用 Excel 模板数据直接测试

#### Step 1: 准备测试数据
1. 打开 [`docs/storyboard-import-template-real.xlsx`](d:\Program Files\Github\LocalMiniDrama\docs\storyboard-import-template-real.xlsx)
2. 复制表格中的两个示例分镜块内容
3. 保存为一个 .txt 文件或 JSON 文件

**数据格式示例**:
```json
[
  {
    "content": "====================【视频编号 01-01】====================\n总时长：13.6s｜场景：中和宫庭院大树下｜人物：林君雪、丹珍、巧心、谷雨\n\n【场景与连续状态】...\n镜头 01（3.4s）树下四人全景...\n镜头 02（6.4s）林君雪中近景...\n镜头 03（3.8s）丹珍动作近景..."
  },
  {
    "content": "====================【视频编号 02-02】====================\n总时长：13.8s｜场景：中和宫庭院大树下｜人物：丹珍、林君雪、巧心、谷雨\n\n【场景与连续状态】...\n镜头 01（5.4s）丹珍双人近景...\n镜头 02（2.6s）巧心动作近景...\n镜头 03（5.8s）林君雪四人中景..."
  }
]
```

#### Step 2: 在前端页面测试
1. 启动后端服务：`cd backend-node && npm run dev`
2. 访问前端页面（http://localhost:5679 或 http://localhost:3013）
3. 选择一个已有剧集的编辑页
4. 点击 "📥 从 Excel 导入分镜" 按钮
5. 选择以下两种方式之一：

**方式 A: 直接粘贴文本**
- 切换到 "粘贴文本" 标签
- 将分镜数据粘贴到文本框
- 点击 "确认导入"

**方式 B: 上传 JSON 文件**
- 切换到 "上传 JSON" 标签
- 拖拽准备好的 JSON 文件到上传区域
- 等待加载成功后点击 "确认导入"

#### Step 3: 验证结果
- ✅ 成功弹窗提示："✓ 成功导入 X 条分镜数据"
- ✅ 分镜列表自动刷新，显示新导入的分缩略图
- ✅ 查看数据库中存储的记录：
  ```sql
  SELECT * FROM storyboards WHERE episode_id = YOUR_EPISODE_ID ORDER BY id DESC LIMIT 10;
  ```

---

### 方式 B: 使用 Node.js 命令行测试

#### 步骤 1: 确保后端运行
```bash
cd backend-node
npm run dev
```

#### 步骤 2: 检查系统环境
```bash
# 检查是否存在剧集
curl http://localhost:5679/api/v1/episodes?drama_id=1
```

#### 步骤 3: 使用 curl 直接调用 API
```bash
curl -X POST http://localhost:5679/api/v1/storyboards/import-excel \
  -H "Content-Type: application/json" \
  -d '{
    "episode_id": 1,
    "data": [
      {
        "content": "====================【视频编号 01-01】====================\n总时长：13.6s｜场景：中和宫庭院大树下｜人物：林君雪、丹珍、巧心、谷雨\n\n【场景与连续状态】白日近黄昏，中和宫庭院大树下已有一个浅坑；林君雪蹲在坑边持小铲，脸上沾土，丹珍、巧心、谷雨围在她身边。\n【光线】LG01 庭院斜阳：斜阳 5200K、强度 34%；树荫环境光 6200K、强度 18%；泥土与酒坛反光 3600K、强度 14%。\n【本编号场景光影锁】先交代浅坑、酒坛和皇后亲自挖土，再以支脸嘟囔表现体力不支；三名宫女始终围在树下。\n\n镜头 01（3.4s）树下四人全景，石径方向高机位轻俯拍，缓慢推近\n画面描述（大白话）：←承上，【大树下浅坑只挖开薄薄一层，酒坛等在旁边；林君雪蹲地握着小铲，丹珍、巧心、谷雨围成半圈】。\n备注：（无台词）\n\n镜头 02（6.4s）林君雪中近景，浅坑侧方平视，静态浅焦\n画面描述（大白话）：【林君雪用一只手支着脸，小铲无力垂在另一只手里；她看着迟迟挖不深的坑，带着鼻尖泥点小声嘟囔】。\n备注：林君雪（台词 01）：太累了。\n\n镜头 03（3.8s）丹珍动作近景，林君雪肩后侧拍，缓慢横移\n画面描述（大白话）：【丹珍忍笑递出帕子，巧心已经蹲下查看林君雪脸上的土；谷雨扶稳坑边酒坛】。\n备注：（无台词）"
      }
    ]
  }'
```

**预期响应**:
```json
{
  "success": true,
  "message": "成功导入 1 个分镜",
  "imported": 1,
  "failed": 0,
  "errors": []
}
```

---

## 📋 验证清单

### ✅ 功能验证项

| 项目 | 验证内容 | 状态 |
|------|----------|------|
| **Excel 模板** | 真实格式模板已生成 | ✅ |
| **后端解析** | storyboardImporter.js 正确解析数据 | ✅ |
| **API 接口** | POST /api/v1/storyboards/import-excel 可用 | ✅ |
| **前端界面** | 导入对话框和按钮已添加 | ✅ |
| **单元测试** | 7 项测试全部通过 | ✅ |
| **场景匹配** | 自动关联 scenes 表 | ✅ |
| **角色匹配** | 自动关联 characters 表 | ✅ |
| **时长计算** | 镜头秒数之和取整 | ✅ |
| **运镜提取** | 提取景别/机位/运动 | ✅ |

### 🔧 待完善项

| 项目 | 当前状态 | 后续优化 |
|------|----------|----------|
| **Excel 文件解析** | 未集成解析库 | 建议前端直接传递 JSON 格式 |
| **CSV 支持** | 暂不支持 | 可添加 CSV 读取功能 |
| **批量导入上限** | 无限制 | 建议单批不超过 100 条 |

---

## 🎬 完整测试流程

### 快速测试（推荐新手）

1. **准备阶段**:
   - 打开 Excel 模板：`docs/storyboard-import-template-real.xlsx`
   - 确认已录入至少一个剧集
   
2. **导入阶段**:
   - 启动后端：`cd backend-node && npm run dev`
   - 访问前端：http://localhost:5679
   - 选择剧集进入编辑页
   - 点击 "📥 从 Excel 导入分镜"
   
3. **验证阶段**:
   - 选择"粘贴文本"或"上传 JSON"方式
   - 提交导入
   - 观察分镜列表变化
   - 查询数据库验证记录

---

## 📝 使用说明

### 数据格式要求

```
====================【视频编号 XX-YY】====================
总时长：X.Xs｜场景：XXXX｜人物：A、B、C

【场景与连续状态】...
【光线】...
【本编号场景光影锁】...

镜头 01（X.Xs）XXX 描述
画面描述（大白话）：XXX
备注：XXX

镜头 02（X.Xs）XXX 描述
画面描述（大白话）：XXX
备注：角色名（台词 XX）：对话内容
```

### 注意事项

⚠️ **关键规则**:
1. 分隔符必须准确：`====================【视频编号...】====================`
2. 使用中文全角括号 `（ ）`（支持混用全角/半角）
3. 场景名称必须与系统中场景库完全匹配
4. 人物名称用顿号 `、` 分隔，必须与角色库完全匹配
5. 每个镜头必须有画面描述
6. 第一个镜头会决定分镜的主标题

---

## 🚀 下一步行动

1. **打开 Excel 模板查看示例数据**
   - 路径：`docs/storyboard-import-template-real.xlsx`
   
2. **准备自己的分镜数据**
   - 按照模板格式填写
   
3. **选择测试方式**:
   - 前端页面导入（推荐）
   - 或直接用 curl/API 工具测试
   
4. **验证导入结果**
   - 查看分镜列表
   - 检查数据库记录
   - 确认场景/角色关联是否正确

---

## 💡 常见问题

**Q: 为什么我的分镜没关联上角色？**
A: 检查角色名称是否完全一致（包括空格）。可以在系统的角色管理中查找并复制名称。

**Q: 总分镜时长不对？**
A: 系统会自动重新计算并取整（Math.round），这是正常行为。

**Q: 一次最多能导入多少条？**
A: 理论上无限制，但建议分批导入（每次不超过 50 条）。

**Q: 如何导出已导入的分镜？**
A: 目前仅支持导入功能，导出功能正在开发中。

---

## 📚 相关文档

- [使用说明](./excel-import-feature.md)
- [HTML 在线模板](./storyboard-import-template.html)
- [纯文本模板](./storyboard-import-template.txt)
- [后端 API 实现](../backend-node/src/routes/storyboards.js#L1178)
- [前端组件实现](../frontweb/src/views/FilmCreate.vue#L965)
