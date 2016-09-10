#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import Iterable


d = {'a': 1, 'b': 2, 'c': 3}

# 迭代字典的键key
for key in d:
    print(key, end=' ')         # a b c
print()

# 迭代字典的键值value
for val in d.values():
    print(val, end=' ')         # 1 2 3
print()

# 迭代字典的子元素item
for k, v in d.items():
    print("%s: %d" % (k, v), end=',')   # b: 2,a: 1,c: 3,
print()

# 迭代字符串的字符
for ch in 'shellever':
    print(ch, end=' ')          # s h e l l e v e r
print()


# 判断对象是否为可迭代对象
# 通过collections模块的Iterable类型
print(isinstance('abc', Iterable))      # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(123, Iterable))        # False


# Python内置的enumerate函数可以把一个list
# 变成(索引-元素)对，然后就可以在for循环
# 中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 0 A
# 1 B
# 2 C


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# 1 1
# 2 4
# 3 9


for x in [(1, 1), (2, 4), (3, 9)]:
    print(x)
# (1, 1)
# (2, 4)
# (3, 9)

