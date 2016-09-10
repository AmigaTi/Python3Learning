#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


# 内置的函数 dir() 可以找到模块内定义的所有名称。
# 以一个字符串列表的形式返回
print(dir(sys))


# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
print(dir())


class Person(object):
    def __init__(self, _name):
        self.name = _name

    def say_hello(self):
        print('Hello, I\'m %s' % self.name)

person = Person('lucas')
attrs = dir(person)
print(attrs)

'''
[
    '__class__',
    '__delattr__',
    '__dict__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__le__',
    '__lt__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__weakref__',
    'name',                     #
    'say_hello'                 #
]
'''
