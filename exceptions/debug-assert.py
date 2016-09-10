#!/usr/bin/python
# -*- coding: utf-8 -*-


# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'     #
    return 10 / n

foo('0')

# AssertionError: n is zero!

