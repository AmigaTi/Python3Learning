#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# re.search 扫描整个字符串并返回第一个成功的匹配
# re.search(pattern, string, flags=0)

line = 'Cats are smarter than dogs'

search_obj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if search_obj:
    print('search_obj.group(): ', search_obj.group())
    print('search_obj.group(1): ', search_obj.group(1))
    print('search_obj.group(1): ', search_obj.group(2))
else:
    print('Nothing found!')

'''
search_obj.group():  Cats are smarter than dogs
search_obj.group(1):  Cats
search_obj.group(1):  smarter
'''


# ==============================================================================
# re.match与re.search的区别

# re.match只匹配字符串的开始，若字符串开始不符合正则表达式则匹配失败，返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

line = 'Cats are smarter than dogs'


match_obj = re.match(r'dogs', line, re.M | re.I)
if match_obj:
    print('match --> match_obj.group(): ', match_obj.group())
else:
    print('No match!')


match_obj = re.search(r'dogs', line, re.M | re.I)
if match_obj:
    print('match --> match_obj.group(): ', match_obj.group())
else:
    print('No match!')

'''
No match!
match --> match_obj.group():  dogs
'''