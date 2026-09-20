import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter

# 创建工作簿和工作表
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "分镜导入模板"

# 定义样式
title_font = Font(name='微软雅黑', size=16, bold=True)
header_font = Font(name='微软雅黑', size=11, bold=True)
normal_font = Font(name='微软雅黑', size=10)
border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)
fill_blue = PatternFill(start_color='D4E6F1', end_color='D4E6F1', fill_type='solid')
fill_green = PatternFill(start_color='D5F5E3', end_color='D5F5E3', fill_type='solid')

# 添加说明部分
ws['A1'] = '📥 LocalMiniDrama 分镜 Excel 导入模板使用说明'
ws.merge_cells('A1:G1')
ws.cell(row=1).font = title_font
ws.cell(row=1).alignment = Alignment(horizontal='center')

instructions = [
    '使用方法：将以下内容复制到 Excel 中，每行一个完整的分镜块',
    '',
    '格式规范：',
    '====【视频编号】====总时长（秒）、场景名、人物 1、人物 2...',
    '镜头 XX(X.Xs) 画面描述',
    '台词："角色对白内容"',
    '运镜：景别 + 机位 + 运动（可选）',
    '备注：特殊要求（可选）',
    '',
    '注意事项：',
    '1. 每行填写一个完整的分镜块（从====开始到下一个===或结束）',
    '2. 视频编号格式：【集数 - 分镜序号】，如【01-01】表示第 1 集第 1 个分镜',
    '3. 镜头序号不要跳号，可以中断补上',
    '4. 场景和人物名称必须与系统中已存在的素材名称完全一致',
    '5. 支持中文括号 ( ) 或英文括号 ()',
    '6. 每个镜头必须有画面描述',
    '',
    '示例数据：',
    '====【01-01】====30、书房、张三',
    '镜头 01(3.5s) 坐在书桌前翻阅文件',
    '台词："这份报告终于完成了..."',
    '运镜：特写，固定镜头',
    '备注：体现疲惫感',
    '====',
    '镜头 02(6.4s) 站起来走到窗边眺望远方',
    '台词："接下来的挑战..."',
    '运镜：中景，缓慢推镜头',
    '备注：窗外夜景',
    '====',
    '镜头 03(3.8s) 回头看向书桌上的照片',
    '台词："一定会努力 overcome 的"',
    '运镜：全景，摇镜头到照片',
    '====',
    '====【02-02】====45、公园、李四、王五',
    '镜头 01(5.4s) 两人在长椅上交谈，秋日午后阳光洒在脸上',
    '台词："听说项目通过了？"',
    '运镜：近景，轻微晃动模拟手持',
    '====',
    '镜头 02(2.6s) 点头微笑',
    '台词："是啊，不容易啊"',
    '运镜：特写，自然光',
    '====',
    '镜头 03(5.8s) 看向远处的孩子玩耍',
    '台词："看到新一代成长真好"',
    '运镜：远景，缓慢拉远',
]

for i, line in enumerate(instructions, start=3):
    ws.cell(row=i, column=1).value = line
    ws.cell(row=i, column=1).font = normal_font
    ws.cell(row=i, column=1).alignment = Alignment(wrap_text=True)

# 设置列宽
ws.column_dimensions['A'].width = 100

# 保存工作簿
file_path = r'd:\Program Files\Github\LocalMiniDrama\docs\storyboard-import-template.xlsx'
wb.save(file_path)
print(f'Excel 模板已保存到：{file_path}')
