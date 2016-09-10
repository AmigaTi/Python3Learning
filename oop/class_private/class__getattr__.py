#!/usr/bin/python
# -*- coding: utf-8 -*-


# __getattr__(): 动态返回一个属性
# 只有在没有找到属性时，才调用__getattr__，
# 已有的属性，不会在__getattr__中查找。
# 当超出class能响应特定的几个属性时，应该抛出AttributeError错误

class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 24
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

stu = Student('kiwi')
print(stu.name)         # kiwi

# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
print(stu.score)        # 99

print(stu.age())        # 24

print(stu.sex)          # AttributeError: 'Student' object has no attribute 'sex'

