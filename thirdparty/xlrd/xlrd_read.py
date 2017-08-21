#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd


workbook = xlrd.open_workbook(u'field_dictionary.xls')
sheet_names = workbook.sheet_names()

for sheet_name in sheet_names:
    sheet2 = workbook.sheet_by_name(sheet_name)
    print("sheet name: %s" % sheet_name)
    rows = sheet2.row_values(3)     # 获取第四行内容
    cols = sheet2.col_values(1)     # 获取第二列内容
    print("rows: %s" % rows)
    print("cols: %s" % cols)

print('=' * 10)

table = workbook.sheets()[0]        # 打开第一张表
nrows = table.nrows                 # 获取表的行数
for i in range(nrows):
    if i == 0:                      # 跳过第一行，表头
        continue
    print(table.row_values(i))      # 打印一行

'''
# result:
sheet name: Fields
rows: ['HTTP', '超文本传输协议']
cols: ['Description', '动态主机配置协议', '域名系统', '超文本传输协议', '万维网']
==========
['DHCP', '动态主机配置协议']
['DNS', '域名系统']
['HTTP', '超文本传输协议']
['WWW', '万维网']
'''