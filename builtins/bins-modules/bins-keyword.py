#!/usr/bin/python
# -*- coding: utf-8 -*-

import keyword

l = keyword.kwlist
print(l)        # 输出当前版本的所有关键字
print(len(l))   # 33

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield']
'''