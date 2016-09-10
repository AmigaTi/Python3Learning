#!/usr/bin/python
# -*- coding: utf-8 -*-


l = [36, 5, -12, 9, -21]

ls = sorted(l)
print(ls)       # [-21, -12, 5, 9, 36]

ls = sorted(l, key=abs)
print(ls)       # [5, 9, -12, -21, 36]


l = ['bob', 'about', 'Zoo', 'Credit']
ls = sorted(l)
print(ls)       # ['Credit', 'Zoo', 'about', 'bob']

ls = sorted(l, key=str.lower)
print(ls)       # ['about', 'bob', 'Credit', 'Zoo']

ls = sorted(l, key=str.lower, reverse=True)
print(ls)       # ['Zoo', 'Credit', 'bob', 'about']


# 用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 按名字排序，不分大小写
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)
# [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]


# 按成绩从高到低排序
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)
# [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]







