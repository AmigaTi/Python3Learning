#!/usr/bin/python
# -*- coding: utf-8 -*-


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

print(callable(hello))          # True

print(callable(Student))        # True

stu = Student('lucas')
print(callable(stu))            # False

stu2 = Student2('lucas')
print(callable(stu2))            # True


