#!/usr/bin/python
# -*- coding: utf-8 -*-

from types import MethodType


# Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age')     # 用tuple定义允许绑定的属性名称

stu = Student()             # 创建新的实例
stu.name = 'Michael'        # 绑定属性name
stu.age = 25                # 绑定属性age

# 由于score没有被放到__slots__中，故不能绑定score属性，
# 试图绑定score将得到AttributeError的错误。
# stu.score = 98              # 绑定属性score
# AttributeError: 'Student' object has no attribute 'score'


# ========================================================
# 动态语言 - 动态绑定属性和方法

class Cat(object):
    pass

# 动态给实例绑定一个属性
cat = Cat()
cat.name = 'Mao'
print(cat.name)     # Mao


# 动态给实例绑定一个方法
def set_age(self, age):
    self.age = age

cat.set_age = MethodType(set_age, cat)

cat.set_age(3)
print(cat.age)      # 3


# 给一个实例绑定的方法，对另一个实例是不起作用的
cat2 = Cat()
# cat2.set_age(4)     # AttributeError: 'Cat' object has no attribute 'set_age'


# 给类绑定方法，达到给所有实例都绑定方法
def set_color(self, color):
    self.color = color

Cat.set_color = MethodType(set_color, Cat)

cat.set_color('Black')
print(cat.color)        # Black

cat2.set_color('White')
print(cat2.color)       # White

