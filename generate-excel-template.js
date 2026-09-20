const ExcelJS = require('exceljs');

async function createExcelTemplate() {
    const workbook = new ExcelJS.Workbook();
    workbook.creator = 'LocalMiniDrama';
    workbook.created = new Date();

    // 定义样式
    const titleStyle = {
        font: { name: 'Microsoft YaHei', size: 16, bold: true },
        alignment: { horizontal: 'center', vertical: 'middle' },
        fill: {
            type: 'pattern',
            pattern: 'solid',
            fgColor: { argb: 'FF667EEA' }
        },
        border: {
            bottom: { style: 'medium', color: { argb: 'FFFFFFFF' } },
            top: { style: 'medium', color: { argb: 'FFFFFFFF' } },
            left: { style: 'medium', color: { argb: 'FFFFFFFF' } },
            right: { style: 'medium', color: { argb: 'FFFFFFFF' } }
        }
    };

    const headerStyle = {
        font: { name: 'Microsoft YaHei', size: 11, bold: true },
        fill: {
            type: 'pattern',
            pattern: 'solid',
            fgColor: { argb: 'FFD4E6F1' }
        },
        border: {
            bottom: { style: 'thin', color: { argb: 'FFCCCCCC' } },
            top: { style: 'thin', color: { argb: 'FFCCCCCC' } },
            left: { style: 'thin', color: { argb: 'FFCCCCCC' } },
            right: { style: 'thin', color: { argb: 'FFCCCCCC' } }
        }
    };

    const normalStyle = {
        font: { name: 'Microsoft YaHei', size: 10 },
        alignment: { vertical: 'middle', wrapText: true },
        border: {
            bottom: { style: 'thin', color: { argb: 'FFE0E0E0' } },
            top: { style: 'thin', color: { argb: 'FFE0E0E0' } },
            left: { style: 'thin', color: { argb: 'FFE0E0E0' } },
            right: { style: 'thin', color: { argb: 'FFE0E0E0' } }
        }
    };

    const successStyle = {
        font: { name: 'Microsoft YaHei', size: 10, color: { argb: 'FF10B981' } },
        fill: {
            type: 'pattern',
            pattern: 'solid',
            fgColor: { argb: 'FFF0FDF4' }
        },
        border: {
            bottom: { style: 'thin', color: { argb: 'FFC6F6E5' } },
            top: { style: 'thin', color: { argb: 'FFC6F6E5' } },
            left: { style: 'thin', color: { argb: 'FFC6F6E5' } },
            right: { style: 'thin', color: { argb: 'FFC6F6E5' } }
        }
    };

    // 创建工作表
    const worksheet = workbook.addWorksheet('分镜导入模板');

    // 添加说明部分（跨列）
    let row = 1;
    worksheet.getCell(`A${row}`).value = '📥 LocalMiniDrama 分镜 Excel 导入模板';
    worksheet.mergeCells(`A${row}:G${row}`);
    worksheet.getRow(row).font = titleStyle.font;
    worksheet.getRow(row).fill = titleStyle.fill;
    worksheet.getRow(row).border = titleStyle.border;

    // 使用方法标题
    row++;
    worksheet.getCell(`A${row}`).value = '一、使用方法';
    worksheet.getRow(row).font = headerStyle.font;
    worksheet.getRow(row).fill = headerStyle.fill;
    worksheet.getColumn('A').width = 30;
    worksheet.getColumn('B').width = 50;
    worksheet.getColumn('C').width = 50;
    worksheet.getColumn('D').width = 30;
    worksheet.getColumn('E').width = 30;
    worksheet.getColumn('F').width = 30;
    worksheet.getColumn('G').width = 40;

    // 使用步骤
    const steps = [
        '1️⃣ 打开此 Excel 文件',
        '2️⃣ 按下方格式填写分镜数据',
        '3️⃣ 每行一个完整的分镜块（从====开始到下一个===或结束）',
        '4️⃣ 保存文件',
        '5️⃣ 在分镜页面点击"📥 从 Excel 导入分镜"',
        '6️⃣ 上传此文件即可'
    ];

    for (let i = 0; i < steps.length; i++) {
        row++;
        worksheet.getCell(`A${row}`).value = steps[i];
        worksheet.getRow(row).style = normalStyle;
    }

    // 数据格式规范
    row++;
    worksheet.getCell(`A${row}`).value = '二、数据格式规范';
    worksheet.getRow(row).font = { name: 'Microsoft YaHei', size: 12, bold: true, color: { argb: 'FF4F46E0' } };
    worksheet.getRow(row).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF1F5F9' } };
    worksheet.mergeCells(`A${row}:G${row}`);

    // 示例分镜文本（放在表格中展示）
    row++;
    worksheet.getCell(`A${row}`).value = '基本格式:';
    worksheet.getRow(row).font = { bold: true };

    row++;
    worksheet.getCell(`A${row}`).value = `====【XX-YY】====总时长（秒）、场景名、人物 1、人物 2...\n镜头 XX(X.Xs) 画面描述\n台词："角色对白内容"\n运镜：景别 + 机位 + 运动（可选）\n备注：特殊要求（可选）`;
    worksheet.getRow(row).alignment = { horizontal: 'left', vertical: 'top', wrapText: true };
    worksheet.getRow(row).font = { name: 'Consolas', size: 10, color: { argb: 'FF475569' } };
    worksheet.getRow(row).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF8FAFC' } };
    worksheet.mergeCells(`A${row}:G${row}`);

    // 字段说明表格
    row++;
    worksheet.getCell(`A${row}`).value = '字段名称';
    worksheet.getCell(`B${row}`).value = '格式要求';
    worksheet.getCell(`C${row}`).value = '必填';
    worksheet.getCell(`D${row}`).value = '说明';
    worksheet.getColumn('A').width = 18;
    worksheet.getColumn('B').width = 35;
    worksheet.getColumn('C').width = 8;
    worksheet.getColumn('D').width = 60;

    const fieldData = [
        { name: '🎬 分镜标题', format: '====【XX-XX】====总时长、场景、人物...', required: '是', desc: '视频编号、总时长（秒）、关联的场景和人物（逗号分隔）' },
        { name: '🎞️ 镜头信息', format: '镜头 01(3.5s)', required: '是', desc: '支持中文或英文括号，小数点后一位' },
        { name: '📝 画面描述', format: '纯文本', required: '是', desc: '详细描述该镜头的画面内容，包含动作、环境等' },
        { name: '🎵 台词', format: '台词:"XXX"', required: '否', desc: '角色的对白或旁白' },
        { name: '📷 运镜', format: '运镜：特写，固定镜头', required: '否', desc: '景别可选：大特写/特写/近景/中景/全景/远景' },
        { name: '💭 备注', format: '备注：xxx', required: '否', desc: '特殊要求、情感表达、氛围提示等' }
    ];

    fieldData.forEach(item => {
        row++;
        worksheet.getCell(`A${row}`).value = item.name;
        worksheet.getCell(`B${row}`).value = item.format;
        worksheet.getCell(`C${row}`).value = item.required;
        worksheet.getCell(`D${row}`).value = item.desc;
        
        // 设置样式
        const cellStyle = { ...normalStyle };
        if (item.required === '是') {
            cellStyle.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFE2E8F0' } };
            worksheet.getCell(`C${row}`).font = { name: 'Microsoft YaHei', size: 10, color: { argb: 'FFFF0000' }, bold: true };
        } else {
            cellStyle.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF1F5F9' } };
        }
        worksheet.getRow(row).style = cellStyle;
    });

    // 完整示例
    row++;
    worksheet.getCell(`A${row}`).value = '三、完整示例';
    worksheet.getRow(row).font = { name: 'Microsoft YaHei', size: 12, bold: true, color: { argb: 'FF4F46E0' } };
    worksheet.getRow(row).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF1F5F9' } };
    worksheet.mergeCells(`A${row}:G${row}`);

    row++;
    worksheet.getCell(`A${row}`).value = `====【01-01】====30、书房、张三\n镜头 01(3.5s) 坐在书桌前翻阅文件\n台词："这份报告终于完成了..."\n运镜：特写，固定镜头\n备注：体现疲惫感\n\n镜头 02(6.4s) 站起来走到窗边眺望远方\n台词："接下来的挑战..."\n运镜：中景，缓慢推镜头\n备注：窗外夜景\n\n镜头 03(3.8s) 回头看向书桌上的照片\n台词："一定会努力 overcome 的"\n运镜：全景，摇镜头到照片\n\n====\n\n====【02-02】====45、公园、李四、王五\n镜头 01(5.4s) 两人在长椅上交谈，秋日午后阳光洒在脸上\n台词："听说项目通过了？"\n运镜：近景，轻微晃动模拟手持\n\n镜头 02(2.6s) 点头微笑\n台词："是啊，不容易啊"\n运镜：特写，自然光\n\n镜头 03(5.8s) 看向远处的孩子玩耍\n台词："看到新一代成长真好"\n运镜：远景，缓慢拉远`;
    worksheet.getRow(row).alignment = { horizontal: 'left', vertical: 'top', wrapText: true };
    worksheet.getRow(row).font = { name: 'Consolas', size: 10, color: { argb: 'FF1E293B' } };
    worksheet.getRow(row).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF8FAFC' } };
    worksheet.mergeCells(`A${row}:G${row}`);

    // 注意事项
    row++;
    worksheet.getCell(`A${row}`).value = '四、注意事项';
    worksheet.getRow(row).font = { name: 'Microsoft YaHei', size: 12, bold: true, color: { argb: 'FFEA580C' } };
    worksheet.getRow(row).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFDF2F8' } };
    worksheet.mergeCells(`A${row}:G${row}`);

    const tips = [
        '✅ 分隔符必须准确：====【XX-XX】====中的等号数量不能少',
        '✅ 场景和人物名称要完全匹配（包括空格、中英文字符）',
        '✅ 至少需要有一个镜头（没有镜头的分镜无法保存）',
        '✅ 每个镜头必须有画面描述（否则会导致 AI 生成失败）',
        '✅ 首次测试建议小规模（先试 5-10 条再批量导入）'
    ];

    tips.forEach((tip, index) => {
        row++;
        worksheet.getCell(`A${row}`).value = tip;
        worksheet.getRow(row).style = successStyle;
    });

    // 保存文件
    const filePath = 'docs/storyboard-import-template.xlsx';
    await workbook.xlsx.writeFile(filePath);
    console.log(`✅ Excel 模板已生成：${filePath}`);
}

createExcelTemplate().catch(console.error);
