#!/usr/bin/python
# -*- coding: utf-8 -*-

# 定义一个含可变列表list的元组tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)        # ('a', 'b', ['X', 'Y'])

# 定义一个只有一个元素的tuple，需要加额外的逗号来消除歧义
t = (1,)
print(t)        # (1,)

# 定义一个空的tuple
t = ()
print(t)        # ()


# 将列表转换为元组
l = ['Google', 'Taobao', 'Runnob', 'Baidu']
t = tuple(l)
print(l)        # ['Google', 'Taobao', 'Runnob', 'Baidu']
print(t)        # ('Google', 'Taobao', 'Runnob', 'Baidu')
