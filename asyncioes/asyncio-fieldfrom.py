#!/usr/bin/python
# -*- coding: utf-8 -*-


# yield from会把内嵌的generator输出作为当前generator输出的一部分
# For simple iterators
# yield from iterable <=> from item in iterable: yield item
# https://docs.python.org/3/whatsnew/3.3.html#pep-380

def gen_list(x):
    yield from range(x, 0, -1)
    yield from range(x)

print(list(gen_list(5)))        # [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]


