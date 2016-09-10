#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.__name = name

print(Student('Michael'))       # <__main__.Student object at 0x0060ABD0>


# __str__()返回用户看到的字符串，使用print()时调用此方法
# __repr__()返回开发者看到的字符串，在命令行中非使用print()时调用此方法

# __str__()方法类似与Java中的toString()方法，用于打印实例时调用

class Dog(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Dog object (name: %s)' % self.__name

    __repr__ = __str__          #

print(Dog('XinLai'))            # Dog object (name: XinLai)
dog = Dog('XiaoHei')
print(dog)                      # Dog object (name: XiaoHei)


