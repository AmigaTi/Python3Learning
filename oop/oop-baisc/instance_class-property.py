#!/usr/bin/python
# -*- coding: utf-8 -*-


# 实例属性：通过实例变量或self变量绑定的属性
# 类属性：在类定义时定义的
# 相同名称的实例属性将屏蔽掉类属性

class Student(object):
    name = 'Student'            # 类属性

    def __init__(self, name):
        self.name = name        # 实例属性

stu = Student('Bob')
stu.score = 90                  # 实例属性
print('Student.name: %s' % Student.name)        # Student.name: Student
print('stu.name: %s' % stu.name)                # stu.name: Bob

