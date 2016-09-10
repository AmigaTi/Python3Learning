#!/usr/bin/python
# -*- coding: utf-8 -*-


def my_abs(x):
    if not isinstance(x, (int, float)):     # 判断x是否为int或float类型
        raise TypeError('wrong operand type')
    if x >= 0:
        return x
    else:
        return -x

