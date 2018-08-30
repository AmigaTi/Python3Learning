#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# foo('0')

'''
Traceback (most recent call last):
  File "D:/workspace/PycharmProjects/Basics/exceptions/raise-error-exception.py", line 21, in <module>
    foo('0')
  File "D:/workspace/PycharmProjects/Basics/exceptions/raise-error-exception.py", line 17, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
'''


# raise语句如果不带参数，就会把当前错误原样抛出。
# 当前函数不知道应该怎么处理该错误时，需要继续往上抛，让顶层调用者去处理。
def foo2(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

'''
ValueError!
Traceback (most recent call last):
  File "D:/workspace/PycharmProjects/Basics/exceptions/raise-error-exception.py", line 52, in <module>
    bar()
  File "D:/workspace/PycharmProjects/Basics/exceptions/raise-error-exception.py", line 46, in bar
    foo('0')
  File "D:/workspace/PycharmProjects/Basics/exceptions/raise-error-exception.py", line 20, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
'''