#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# 写列表生成式时，把要生成的元素x * x放到前面，
# 后面跟for循环，就可以把list创建出来
# for循环后面加上if判断，就可以筛选出仅偶数的平方
l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)        # [4, 16, 36, 64, 100]


# 使用两层循环来生成全排列
l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)        # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 列出当前目录下的所有文件和目录名
l = [d for d in os.listdir('.')]
print(l)        # ['iterator.py', 'list -comprehensions.py', 'slice.py']


# 列表生成式可以使用两个变量来生成List
d = {'x': 'A', 'y': 'B', 'z': 'C'}
l = [k + '=' + v for k, v in d.items()]
print(l)        # ['x=A', 'y=B', 'z=C']


# 把列表中的所有字符串变成小写
l = ['Hello', 'World', 'And', 'Hello', 'Me']
print([s.lower() for s in l])   # ['hello', 'world', 'and', 'hello', 'me']


# 筛选出字符串子元素
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)       # ['hello', 'world', 'apple']


