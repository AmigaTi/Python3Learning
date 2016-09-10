#!/usr/bin/python
# -*- coding: utf-8 -*-


# Python内置的@property装饰器负责把一个方法变成属性调用
# 只定义getter方法，不定义setter方法就是一个只读属性

# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@birth.setter，
# 负责把一个setter方法变成属性赋值

# @property           ->      把方法变成属性调用(getter)(可读)
# @method.setter      ->      把方法编程属性赋值(setter)(可写)

class Student(object):
    def __init__(self):
        self.__birth = 0

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2016-self.__birth


# ===============================================================================
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
# width/height unit: px
class Screen(object):
    def __init__(self):
        self.__height = 0
        self.__width = 0

    @staticmethod
    def __check_param(value):
        if not isinstance(value, int):
            raise TypeError('Must a int type')
        if value <= 0:
            raise ValueError('Must great than zero')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__check_param(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__check_param(value)
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)     # 786432
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

