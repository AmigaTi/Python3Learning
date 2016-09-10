#!/usr/bin/python
# -*- coding: utf-8 -*-

# __call__(): 可以直接对实例进行调用
# 即将类的实例对象当作函数来使用，相当于重载了括号运算符()。
# 而通常一个对象实例有自身的属性和方法，
# 当调用实例对象方法时，使用instance.method()来调用。


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

stu = Student('Apple')
stu()           # 重载括号运算符，直接将实例对象当作函数调用
# My name is Apple.


# ================================================================
# 判断一个变量是对象还是函数，需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象(实现__call__()方法的类实例)，
# 通过callable()函数，就可以判断一个对象是否是“可调用”对象

stu2 = Student('Kiwi')
print(callable(stu2))           # True
print(callable(max))            # True
print(callable('hellome'))      # False
