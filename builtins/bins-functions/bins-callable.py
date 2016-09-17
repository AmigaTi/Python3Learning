#!/usr/bin/python
# -*- coding: utf-8 -*-


import types


# callable(object)

# Return True if the object argument appears callable, False if not.
# If this returns true, it is still possible that a call fails,
# but if it is false, calling object will never succeed.
# Note that classes are callable (calling a class returns a new instance);
# instances are callable if their class has a __call__() method.

# 检查对象object是否可调用。如果可以调用则返回True，否则返回False
# 注意：类是可调用的，而类的实例实现了__call__()方法才可调用。

def hello():
    print('hello world!')


class Student(object):
    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return 'Student(%s)' % self.name


class Student2(object):
    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return 'Student(%s)' % self.name

    def __call__(self):
        pass

print(isinstance(hello, types.FunctionType))            # True
print(type(hello), callable(hello))          # <class 'function'> True
print(hasattr(hello, '__call__'))           # True
print('------------------------------')

print(isinstance(Student, types.FunctionType))          # False
print(type(Student), callable(Student))        # <class 'type'> True
print(hasattr(Student, '__call__'))             # True
print('------------------------------')

stu = Student('lucas')
print(type(stu), callable(stu))            # <class '__main__.Student'> False //没有实现__call__方法
print(hasattr(stu, '__call__'))             # False
print('------------------------------')

stu2 = Student2('lucas')
print(type(stu2), callable(stu2))            # <class '__main__.Student2'> True
print(hasattr(stu2, '__call__'))             # True

