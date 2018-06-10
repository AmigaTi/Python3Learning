#!/usr/bin/python
# -*- coding:utf-8 -*-

from openpyxl import Workbook
from openpyxl.styles import Font, colors, Alignment


# 创建一个新的工作簿，默认可读写
wb = Workbook()


# grab the active worksheet - 获取默认表格
ws = wb.active


# 属性是可读写的
# 获取默认表名
print(ws.title)     # Sheet
# 修改默认表名
ws.title = 'example'

# Data can be assigned directly to cells
ws['A1'] = 42


# 设置字体
ws['B1'] = '你好，世界'
bold_italic_24_font = Font(name='my_font', size=24, italic=True, color=colors.RED, bold=True)
ws['B1'].font = bold_italic_24_font

# Rows can also be appended - 添加一行
ws.append([1, 2, 3])    # 分别对A2 B2 C2表格单元赋值


# 通过属性row和column来指定表格单元，并使用属性value进行赋值
ws.cell(row=3, column=2, value=6)
d = ws.cell(row=4, column=2)
d.value = '=SUM(B2:B3)'


# 浮点类型赋值，以文本类型保存到表格单元中
c = ws['C3']
c.value = '2.50'
print(c.value)


# 对齐方式
# 设置A5中的数据垂直居中和水平居中
# TypeError: cell() missing 1 required positional argument: 'column'
# c = ws.cell('A5')
c = ws['A5']
c.value = '666'
align = Alignment(horizontal='center', vertical='center')
c.alignment = align


# 设置行高和列宽
# 列宽的30和行高的30差别很大
c = ws.cell(row=5, column=5)
c.value = "Hello World and Hello me"
ws.column_dimensions['E'].width = 30    # 设置列宽
ws.row_dimensions[5].height = 30        # 设置行高


# 合并单元格
ws.merge_cells('A6:E7')
ws['A6'].value = '888'       # 合并后的坐标为A6
# 拆分单元格
ws.usmerge_cells('A1:C3')     # 拆分后值回到A1位置


# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()


# 遍历表格
# UserWarning: Using a range string with iter_rows is deprecated. Use ws[range_string]
# for row in ws.iter_rows('A1:C3'):
for row in ws['A1:C3']:
    for cell in row:
        print(cell.value)


# 获取当前工作表的数据长度与宽度
# TypeError: object of type 'generator' has no len()
# print(len(ws.rows))
# print(len(ws.columns))
print(type(ws.rows))        # <class 'generator'>
print("sheet rows = %d" % len(list(ws.rows)))
print("sheet columns = %d" % len(list(ws.columns)))


# 保存文件 - 指定路径和文件名，后缀为xlsx
# 注意保存前，文件要先确保已关闭，否则会报如下错误：
# PermissionError: [Errno 13] Permission denied: 'sample.xlsx'
wb.save("sample.xlsx")

