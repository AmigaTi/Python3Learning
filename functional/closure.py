#!/usr/bin/python
# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def count():
        ax = 0
        for n in args:
            ax += n
        return ax
    return count

# 当调用lazy_sum()时返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7)

# 调用函数f时，才真正计算求和的结果
print(f())          # 16
