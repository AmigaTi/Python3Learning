#!/usr/bin/python
# -*- coding: utf-8 -*-

is_debug = True


def logd(*obj):
    if is_debug:
        print(*obj)


def foo(s):
    n = int(s)
    logd('>>> n = %d' % n)
    return 10 / n

foo('1')
foo('0')

'''
>>> n = 1
>>> n = 0
Traceback (most recent call last):
  File "D:/MyDocument/MyDevelopment/PyCharmProjects/Basics/exceptions/debug-print.py", line 18, in <module>
    foo('0')
  File "D:/MyDocument/MyDevelopment/PyCharmProjects/Basics/exceptions/debug-print.py", line 15, in foo
    return 10 / n
ZeroDivisionError: division by zero
'''