/**
 * 生成真实格式的 Excel 分镜导入模板
 */
const ExcelJS = require('exceljs');
const fs = require('fs');
const path = require('path');

async function createRealExcelTemplate() {
    const workbook = new ExcelJS.Workbook();
    
    // 工作表
    const worksheet = workbook.addWorksheet('分镜导入模板 - 真实格式');
    
    // 设置列宽
    worksheet.getColumn('A').width = 80;
    
    // 样式定义
    const titleStyle = {
        font: { name: '微软雅黑', size: 14, bold: true },
        alignment: { horizontal: 'center', vertical: 'middle' },
        fill: { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFD4E6F1' } },
        border: { top: { style: 'thin' }, bottom: { style: 'medium' }, left: { style: 'thin' }, right: { style: 'thin' } }
    };
    
    const exampleStyle = {
        font: { name: 'Consolas', size: 9, color: { argb: 'FF1E293B' } },
        alignment: { wrapText: true, vertical: 'top' },
        fill: { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF8FAFC' } },
        border: { top: { style: 'thin' }, bottom: { style: 'thin' }, left: { style: 'thin' }, right: { style: 'thin' } }
    };
    
    let row = 1;
    
    // 标题
    worksheet.getCell(`A${row}`).value = '📥 LocalMiniDrama 分镜 Excel 导入模板';
    worksheet.getRow(row).font = titleStyle.font;
    worksheet.mergeCells(`A1:A1`);
    
    row++;
    
    // 使用方法说明
    worksheet.getCell(`A${row}`).value = `⚠️ 使用说明:\n1. 将此表格内容复制到 Excel 中\n2. 每行一个完整的分镜块（从「====================【视频编号...】」开始到下一个「====」或结束）\n3. 确保场景名称与系统中已存在的场景完全匹配\n4. 人物名称用顿号「、」分隔，需与角色库中的名称完全一致\n5. 保存为.xlsx 文件后，在分镜页面点击「📥 从 Excel 导入分镜」上传`;
    worksheet.getRow(row).alignment = { vertical: 'top', wrapText: true };
    
    row++;
    worksheet.getCell(`A${row}`).value = `\n✅ 真实格式示例（请直接复制以下内容到 Excel 并作为测试数据）:`;
    worksheet.getRow(row).font = { bold: true, color: { argb: 'FF10B981' } };
    
    // 真实的分镜块数据（使用用户最初提供的完整格式）
    const REAL_BLOCK_1 = `====================【视频编号 01-01】====================
总时长：13.6s｜场景：中和宫庭院大树下｜人物：林君雪、丹珍、巧心、谷雨

【场景与连续状态】白日近黄昏，中和宫庭院大树下已有一个浅坑；林君雪蹲在坑边持小铲，脸上沾土，丹珍、巧心、谷雨围在她身边。
【光线】LG01 庭院斜阳：斜阳 5200K、强度 34%；树荫环境光 6200K、强度 18%；泥土与酒坛反光 3600K、强度 14%。
【本编号场景光影锁】先交代浅坑、酒坛和皇后亲自挖土，再以支脸嘟囔表现体力不支；三名宫女始终围在树下。

镜头 01（3.4s）树下四人全景，石径方向高机位轻俯拍，缓慢推近
画面描述（大白话）：←承上，【大树下浅坑只挖开薄薄一层，酒坛等在旁边；林君雪蹲地握着小铲，丹珍、巧心、谷雨围成半圈】。
备注：（无台词）

镜头 02（6.4s）林君雪中近景，浅坑侧方平视，静态浅焦
画面描述（大白话）：【林君雪用一只手支着脸，小铲无力垂在另一只手里；她看着迟迟挖不深的坑，带着鼻尖泥点小声嘟囔】。
备注：林君雪（台词 01）：太累了。

镜头 03（3.8s）丹珍动作近景，林君雪肩后侧拍，缓慢横移
画面描述（大白话）：【丹珍忍笑递出帕子，巧心已经蹲下查看林君雪脸上的土；谷雨扶稳坑边酒坛】。
备注：（无台词）`;

    const REAL_BLOCK_2 = `====================【视频编号 02-02】====================
总时长：13.8s｜场景：中和宫庭院大树下｜人物：丹珍、林君雪、巧心、谷雨

【场景与连续状态】丹珍将帕子递到林君雪面前，巧心蹲在她身侧，谷雨扶住酒坛；林君雪仍握着小铲不肯起身。
【光线】锁定 LG01 庭院斜阳。
【本编号场景光影锁】丹珍笑劝、巧心擦脸并接活、林君雪拒绝三步连续；不让宫女真正拿走小铲。

镜头 01（5.4s）丹珍双人近景，林君雪肩后平视，缓慢推近
画面描述（大白话）：←承上视频编号 01，【丹珍把帕子送到林君雪手边，笑着指向她脸上泥点】。
备注：丹珍（台词 02）：娘娘，都说了让奴婢们来。

镜头 02（2.6s）巧心动作近景，树根侧方低机位，静态浅焦
画面描述（大白话）：【巧心接过帕子替林君雪擦脸，另一只手伸向小铲】。
备注：巧心（台词 03）：您歇着，奴婢们挖。

镜头 03（5.8s）林君雪四人中景，酒坛方向三分之四侧拍，快速横移
画面描述（大白话）：【林君雪立即摇头，把小铲收回怀中】。
备注：林君雪（台词 04）：不行。这是本宫的诚意，必须自己挖。`;

    row++;
    worksheet.getCell(`A${row}`).value = `示例分镜块 1 (共 3 个镜头，总时长 14 秒):\n` + REAL_BLOCK_1;
    worksheet.getRow(row).style = exampleStyle;
    
    row++;
    worksheet.getCell(`A${row}`).value = `示例分镜块 2 (共 3 个镜头，总时长 14 秒):\n` + REAL_BLOCK_2;
    worksheet.getRow(row).style = exampleStyle;
    
    row++;
    worksheet.getCell(`A${row}`).value = `重要提示:\n1. 分隔符必须使用等号「====」开头\n2. 视频编号使用中文全角括号「【】」\n3. 镜头序号也使用全角括号「（X.Xs）」\n4. 时长计算方式：所有镜头秒数之和取整（13.6s → 14s, 13.8s → 14s）\n5. 支持全角/半角括号混用，解析器会自动兼容`;
    worksheet.getRow(row).alignment = { vertical: 'top', wrapText: true };
    
    row++;
    worksheet.getCell(`A${row}`).value = `字段说明:\n- 视频编号格式：【集数 - 分镜序号】如【01-01】表示第 1 集第 1 个分镜\n- 场景名：必须与系统中场景库的 location 字段完全匹配\n- 人物列表：多个角色用顿号「、」分隔，名称需与角色库的 name 字段完全匹配\n- 运镜信息：自动提取景别（特写/近景/中景/全景/远景）、机位（高机位/平视/低机位）、运动（推镜头/拉镜头/横移等）`;
    worksheet.getRow(row).alignment = { vertical: 'top', wrapText: true };
    
    // 保存文件
    const filePath = 'docs/storyboard-import-template-real.xlsx';
    await workbook.xlsx.writeFile(filePath);
    console.log(`✅ 真实格式 Excel 模板已生成：${filePath}`);
    console.log('\n💡 下一步操作:\n1. 打开生成的 Excel 文件查看示例数据\n2. 按照示例格式准备自己的分镜数据\n3. 将数据按上述格式整理好\n4. 在前端点击"📥 从 Excel 导入分镜"\n5. 选择你的数据文件进行导入');
}

createRealExcelTemplate().catch(console.error);
