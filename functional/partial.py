#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools

print(int('1111', base=2))  # 15

# functools.partial的作用：把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
print(int2('1111'))         # 15


max2 = functools.partial(max, 10)
print(max2(5, 6, 7))        # 10
# args = (10, 5, 6, 7)
# max(*args)
