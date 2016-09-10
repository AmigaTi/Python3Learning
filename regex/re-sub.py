#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


# re.sub用于替换字符串中的匹配项
# re.sub(pattern, replace, string, count=0)
# 可选参数 count 是模式匹配后替换的最大次数；
# count 必须是非负整数。
# 缺省值是 0 表示替换所有的匹配


phone = '2004-959-559 # 这是一个电话号码'

# 删除注释
num = re.sub(r'#.*$', '', phone)
print('电话号码：', num)     # 电话号码： 2004-959-559


# 移除非数字内容
num = re.sub(r'\D', '', phone)
print('电话号码：', num)     # 电话号码： 2004959559
