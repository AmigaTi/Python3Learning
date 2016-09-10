#!/usr/bin/python
# -*- coding: utf-8 -*-


# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
def build(x, y):
    return lambda: x * x + y * y

print(build(3, 4))          # <function build.<locals>.<lambda> at 0x0090F390>
print(build(3, 4)())        # 25


def f(x):
    return x * x

f2 = lambda x: x * x

print(f(5))                 # 25
print(f2(5))                # 25
