#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import inspect


# inspect — Inspect live objects
# The inspect module provides several useful functions to help get information
# about live objects such as modules, classes, methods, functions, tracebacks,
# frame objects, and code objects. For example, it can help you examine the
# contents of a class, retrieve the source code of a method, extract and format
# the argument list for a function, or get all the information you need to
# display a detailed traceback.


def welcome():
    print('welcome here!')


def say_hello(name):
    print('hello, %s' % name)


def get_max(a, b):
    if a >= b:
        return a
    return b


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Student(%s, %d)' % (self.name, self.age)


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.POSITIONAL_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        print(param.kind)
        if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            args.append(name)
    return tuple(args)


if __name__ == '__main__':
    print(inspect.getsource(welcome))
    print('--' * 32)
    print(inspect.signature(say_hello).parameters)
    print('--' * 32)
    print(inspect.signature(get_max).parameters)
    print('--' * 32)
    print(inspect.isclass(Student))         # True
    print(inspect.signature(Student))       # (name, age)
    print(get_named_kw_args(get_max))       # ('a', 'b')


'''
def welcome():
    print('welcome here!')

----------------------------------------------------------------
OrderedDict([('name', <Parameter "name">)])
----------------------------------------------------------------
OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b">)])
----------------------------------------------------------------
True
(name, age)
()
'''
