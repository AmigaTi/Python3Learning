#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python中是没用switch语句的，这应该是体现python大道至简的思想，
# python中一般多用字典来代替switch来实现。


# 用字典实现了选择功能
def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def mul(x, y):
    print(x * y)


def div(x, y):
    print(x / y)


operator = {'+': add, '-': sub, '*': mul, '/': div}


def f(x, o, y):
    operator.get(o)(x, y)


f(3, '+', 2)        # 5
f(3, '-', 2)        # 1
f(3, '*', 2)        # 6
f(3, '/', 2)        # 1.5


# =======================================================================
# Brian Beck提供了一个类 switch 来实现其他语言中switch的功能

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:    # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False            # continue to next case

# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = 'ten'
for case in Switch(v):
    if case('one'):                 # True
        print(1)
        break
    if case('two'):
        print(2)
        break
    if case('ten'):
        print(10)
        break
    if case('eleven'):
        print(11)
        break
    if case():      # default, could also just omit condition or 'if True'
        print("something else!")
        # No need to break here, it'll stop anyway


tp = type([1, 2]).__name__      # list
# tp = type([1, 2])               # <class 'list'>
print(tp)
for case in Switch(tp):
    if case('list'):
        print('list')
        break
    if case('dict'):
        print('dict')
        break
    if case('str'):
        print(str)
        break
    if case():
        print('default')







