#!/usr/bin/python
# -*- coding: utf-8 -*-

import prettytable


# 创建表格
table = prettytable.PrettyTable()
# 添加表格头部
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# 按行添加数据
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
print(table)

# 按列添加数据
table.add_column("index", [1, 2, 3, 4])
print(table)


# 获取指定列或行
s = table.get_string(fields=["City name", "Population"], start=1, end=4)
print(s)


# 自定义表格输出样式

# 设定所有列左对齐
# table.align = 'l'
# 设定指定列为左对齐，其余列默认使用右对齐
table.align['Annual Rainfall'] = 'l'

# 设定数字输出格式
table.float_format = "2.2"

# 设定边框连接符为'*'，默认为'+'
# table.junction_char = '*'

# 设定排序方式
table.sortby = 'City name'

# 设定左侧不填充空白字符
# table.left_padding_width = 0

# 设定不显示边框
# table.border = 0

# 设置边框分隔符
table.set_style(prettytable.DEFAULT)

print(table)

# PrettyTable也支持输入HTML代码
s = table.get_html_string()
print(s)

# 使用copy方法复制对象
table2 = table.copy()
# 设定指定列为左对齐，其余列默认使用右对齐
table2.align['Annual Rainfall'] = 'r'

print(table2)


'''
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
+-----------+------+------------+-----------------+
'''
