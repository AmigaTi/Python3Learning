#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools


# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。


# itertools提供的无限迭代器
# itertools.count(start,step)
# itertools.cycle(p)
# itertools.repeat(elem, n)


naturals = itertools.count(1)
for n in naturals:
    print(n)
    if n >= 10:
        break           # 防止无限循环


cs = itertools.cycle('ABC')
i = 0
for c in cs:
    print(c)
    i += 1
    if i >= 10:
        break           # 防止无限循环


# 如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('D', 3)
for n in ns:
    print(n)


# takewhile() = 根据条件判断来截取出一个有限的序列
naturals = itertools.count(1)   # 生成自然数
ns = itertools.takewhile(lambda x: x <= 10, naturals)
l = list(ns)
print(l)        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# =================================================================
# itertools提供的迭代器操作函数

# chain()
# 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c, end=' ')
print()     # generate a newline
'''
A B C X Y Z
'''


# groupby()
# 把迭代器中**相邻的重复元素**挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
'''
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
'''


# 忽略大小写：让元素'A'和'a'都返回相同的key
# 挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key
for key, group in itertools.groupby('AaaBBbcCAAa', lambda ch: ch.upper()):
    print(key, list(group))
'''
A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']
'''



