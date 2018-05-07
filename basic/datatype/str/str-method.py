#!/usr/bin/python
# -*- coding: utf-8 -*-


module_name = 'routes.py'
n = module_name.rfind('.')
print(n)                    # 6

# 首字母大写
print('shellever'.capitalize())     # Shellever

# 统计字符串里某个字符出现的次数
# count(self, sub, start=None, end=None)
# sub   - 搜索的子字符串
# start - 字符串开始搜索的位置，默认为第一个字符索引
# end   - 字符串中结束搜索的位置，默认为字符串的最后一个索引
print('shellever'.count('e'))       # 3

# 使用指定字符来填充字符串左右两侧，使字符串居中，默认填充字符为空格
# center(self, width, fillchar=None)
print('shellever'.center(36, '-'))  # -------------shellever--------------

# 判断字符串是否以指定子串开头
print('package://com.android.settings'.startswith('package://'))    # True

# 分割字符串
# split(self, sep=None, maxsplit=-1)
# sep - 分割符，默认为空格
# maxsplit - 最大分割次数，默认为-1，即整个字符串进行分割
print('1,2,3'.split(','))               # ['1', '2', '3']
print('1,2,3'.split(',', maxsplit=1))   # ['1', '2,3']
print('1,2,,3,'.split(','))             # ['1', '2', '', '3', '']
