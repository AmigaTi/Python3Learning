#!/usr/bin/python
# -*- coding: utf-8 -*-
import types


# type()
# 返回对应的Class类型
print(type(123))
print(type('hello'))
print(type(None))
print(type(abs))


# 判断一个对象是否为函数：使用types模块中定义的常量
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print('--------------------------------------------------')


# isinstance()
# 要判断class的类型，可以使用isinstance()函数
# 能用type()判断的基本类型也可以用isinstance()判断
# 判断一个变量是否是某些类型中的一种
print(isinstance('hello', str))
print(isinstance(123, int))
print(isinstance(b'me', bytes))
print('----------------------------------------')
print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print('----------------------------------------')
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print('----------------------------------------')


class Person(object):
    pass


class Female(Person):
    pass


print(isinstance(Female(), Person))
print(isinstance(Female(), Female))


# dir()
# 获得一个对象的所有属性和方法
# print('[')
# for name in dir('hellome'):
#     print(name)
# print(']')
print(dir('hellome'))


# hasattr()
# setattr()
# getattr()
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

# 测试对象的属性
print(hasattr(obj, 'x'))       # 测试对象obj是否有属性'x'
print(hasattr(obj, 'y'))       # 测试对象obj是否有属性'y'
setattr(obj, 'y', 19)   # 设置对象obj属性'y'
print(hasattr(obj, 'y'))       # 再次测试对象obj是否有属性'y'
print(getattr(obj, 'y'))       # 获取对象obj属性'y'

# 如果试图获取不存在的属性，会抛出AttributeError的错误
# 可以传入一个default参数，如果属性不存在，就返回默认值
# print(getattr(obj, 'z'))    # AttributeError: 'MyObject' object has no attribute 'z'
print(getattr(obj, 'z', 404))


