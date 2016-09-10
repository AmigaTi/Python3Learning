#!/usr/bin/python
# -*- coding: utf-8 -*-


# type() - 查看一个类型或变量的类型
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
class Hello(object):
    def hello(self, name='world'):
        print('Hello %s.' % name)

h = Hello()
h.hello()               # Hello world.
print(type(Hello))      # <class 'type'>
print(type(h))          # <class '__main__.Hello'>
print('----------------------------------------------')


# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
# 然后调用type()函数创建出class。
def fn(self, name='me'):
    print('Hello %s.' % name)

# type("class的名称", "继承的父类集合tuple", "class的方法名称与函数绑定dict")
HelloMe = type('HelloMe', (object,), dict(hello=fn))

h = HelloMe()
h.hello()
print(type(HelloMe))    # <class 'type'>
print(type(h))          # <class '__main__.HelloMe'>
print('-----------------------------------------------------')


# str   用来创建字符串对象的类
# int   用来创建整数对象的类
# type  用来创建类对象的类

age = 35
print('age = 35')
print('age.__class__ = %s' % age.__class__)
print('age.__class__.__class__ = %s' % age.__class__.__class__)
'''
age = 35
age.__class__ = <class 'int'>
age.__class__.__class__ = <class 'type'>
'''

names = 'bob'
print('names = \'bob\'')
print('names.__class__ = %s' % names.__class__)
print('names.__class__.__class__ = %s' % names.__class__.__class__)
'''
names = 'bob'
names.__class__ = <class 'str'>
names.__class__.__class__ = <class 'type'>
'''


def foo():
    pass

def_foo = '''
def foo():
    pass
'''

print(def_foo)
print('foo.__class__ = %s' % foo.__class__)
print('foo.__class__.__class__ = %s' % foo.__class__.__class__)
'''
def foo():
    pass

foo.__class__ = <class 'function'>
foo.__class__.__class__ = <class 'type'>
'''


class Bar(object):
    pass

b = Bar()

class_bar = '''
class Bar(object):
    pass
b = Bar()
'''

print(class_bar)
print('b.__class__ = %s' % b.__class__)
print('b.__class__.__class__ = %s' % b.__class__.__class__)

'''
class Bar(object):
    pass
b = Bar()

b.__class__ = <class '__main__.Bar'>
b.__class__.__class__ = <class 'type'>
'''
print('-----------------------------------------------------')


# ========================================================================

# metaclass - 跟通过继承来获得父类的方法很像???

# 在面向对象编程中，实例化基本遵循创建实例对象、初始化实例对象、最后返回实例对象这么一个过程。
# Python 中的 __new__ 方法负责创建一个实例对象，__init__ 方法负责将该实例对象进行初始化。
# 当你进行 c1 = MyClass(11) 这样的操作的时候，其内部流程是首先调用 MyClass.__new__ 方法创建实例对象，
# 紧接着就调用该对象的 __init__ 方法完成初始化，然后将该实例对象引用给 c1 变量。

# __new__(): 对象构造函数
# __init__(): 对象初始化函数

# 其实 Python 构造实例的逻辑很简单，就是两个步骤，首先构造一个实例，然后初始化这个实例。
# 如果你使用 Foo() 方法进行实例构造，那这两个步骤自动完成。
# 如果你选择手动构造，那就要自己来控制构造实例与初始化实例。


# metaclass是类的模板，所以必须从type类型派生
# 先定义metaclass，就可以创建类，最后创建实例。
# 即可以把类看成是metaclass创建出来的“实例”。

# 定义一个metaclass类ListMetaclass时，
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，
# 以便清楚地表示这是一个metaclass

# __new__的用法：
# T.__new__(S, ...)     #return a new object with type S, a subtype of T

# 在 Python 中存在于类里面的构造方法 __init__() 负责将类的实例化，
# 而在 __init__() 启动之前，__new__() 决定是否要使用该 __init__() 方法，
# 因为__new__() 可以调用其他类的构造方法或者直接返回别的对象来作为本类的实例。


class ListMetaclass(type):      # metaclass是类的模板，所以必须从type类型派生
    def __new__(mcs, name, bases, attrs):
        print('call ModelMetaclass.__new__(%s, %s, %s, %s)' % (mcs.__name__, name, str(bases), str(attrs)))
        # attrs['add']相当于下面的def add(self, value)
        # class MyList(list):
        #     def add(self, value):
        #         self.append(value)
        attrs['add'] = lambda self, value: self.append(value)
        print('exit ModelMetaclass.__new__(%s, %s, %s, %s)' % (mcs.__name__, name, str(bases), str(attrs)))
        return type.__new__(mcs, name, bases, attrs)    # 通过type来生成类


# 通过关键字参数metaclass来指示使用ListMetaclass来创建类MyList
# 传入的关键字参数metaclass指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来代理创建，在此期间，可以修改类的定义，
# 如加上新的方法等，然后返回修改后的定义。
# __new__()方法的参数依次为：
# 1. mcs   - 当前准备创建的类的对象(metaclass)
# 2. name  - 类的名称(class)，即使用metaclass来创建的类
# 3. bases - 类继承的父类集合(tuple)
# 4. attrs - 类的方法集合(dict)，即将要创建的class的属性或方法

class MyList(list, metaclass=ListMetaclass):
    pass


# 测试MyList的add()方法
L = MyList()
L.add(1)
L.add(3)
print(L)        # [1, 3]

'''
call ModelMetaclass.__new__(ListMetaclass, MyList, (<class 'list'>,), {'__qualname__': 'MyList', '__module__': '__main__'})
exit ModelMetaclass.__new__(ListMetaclass, MyList, (<class 'list'>,), {'__module__': '__main__', 'add': <function ListMetaclass.__new__.<locals>.<lambda> at 0x0043F6F0>, '__qualname__': 'MyList'})
[1, 3]
'''

# 而普通的list没有add()方法
# L2 = list()
# L2.add(1)       # AttributeError: 'list' object has no attribute 'add'




