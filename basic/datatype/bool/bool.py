#!/usr/bin/python
# -*- coding: utf-8 -*-


# 在Python 中，and 和 or 执行布尔逻辑演算，但是它们并不返回布尔值；
# 而是，返回它们实际进行比较的值之一。


# and
print('a' and 'b')              # b
print('a' and 'b' and 'c')      # c
print('---' * 12)


# or
print('a' or 'b')               # a
print('' or 'b')                # b
print(0 or 'b')                 # b
print([] or 'b')                # b
print({} or 'b')                # b
print('---' * 12)


# and-or similar to bool ? a: b in C/C++/Java
a = 'first'
b = 'second'
print(1 and a or b)             # first
print((1 and a) or b)           # first
print(0 and a or b)             # second
print((0 and a) or b)           # second
print('---' * 12)


# 条件选择语句
# bool and a or b           # bool为True选择a，False选择b，不管a或b本身是真还是假
# <=> bool? a: b
# [a]: 是一个非空列表，绝不会为假，即使a为数字0或者空字符串''或者其他假值，以为它有一个元素

# 当in_bool为真时，返回in_a，否则返回in_b
def choose(in_bool, in_a, in_b):
    return (in_bool and [in_a] or [in_b])[0]

print(choose(1, 'first', 'second'))  # second



