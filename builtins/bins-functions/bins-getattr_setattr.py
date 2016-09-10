#!/usr/bin/python
# -*- coding: utf-8 -*-


# getattr(object, name[, default])

# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes,
# the result is the value of that attribute. For example,
# getattr(x, 'foobar') is equivalent to x.foobar.
# If the named attribute does not exist, default is returned if provided,
# otherwise AttributeError is raised.

# 其实getattr()这个方法最主要的作用是实现反射机制。
# 也就是说可以通过字符串获取方法实例。
# 这样，你就可以把一个类可能要调用的方法放在配置文件里，在需要的时候动态加载。

# getattr()就是实现python反射的一块积木，结合其它方法如setattr(),dir() 等，
# 我们可以做出很多有趣的事情。


# getattr(object,name,default):
# 作用：返回object的名称为name的属性的属性值，如果属性name存在，则直接返回其属性值；
# 如果属性name不存在，则触发AttributeError异常或当可选参数default定义时返回default值。

# setattr(object,name,value):
# 作用：设置object的名称为name（type：string）的属性的属性值为value，
# 属性name可以是已存在属性也可以是新属性。


class Student(object):
    def __init__(self, _name):
        self.name = _name

    def intro(self):
        print('hello, my name is %s. I\'m a student.' % self.name)

    def hello():
        print('hello world and hello me!')


class Person(object):
    pass


if __name__ == '__main__':
    stu = Student('lucas')
    per = Person()
    name = getattr(stu, 'name', 'curry')    # 获取实例对象stu的name属性，若属性不存在，则返回默认值curry
    print('name: %s' % name)
    func = getattr(stu, 'intro', None)
    print('type(func): ', type(func))
    print('call func()...')
    func()
    print('---' * 12)

    attrs = dir(stu)
    print('attrs: ', attrs)
    for attr in attrs:
        if not attr.startswith('_'):
            setattr(per, attr, None)        # 给实例对象的属性赋值，若属性不存在，则先创建再赋值per.attr = None
    print(hasattr(per, 'name'))             # 判断实例对象是否存在name属性


'''
name: lucas
type(func):  <class 'method'>
call func()...
hello, my name is lucas. I'm a student.
------------------------------------
attrs:  [
    '__class__',
    '__delattr__',
    '__dict__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
     '__hash__',
    '__init__',
    '__le__',
    '__lt__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__weakref__',
    'hello',                # func
    'intro',                # func
    'name'                  # attr
]
'''

