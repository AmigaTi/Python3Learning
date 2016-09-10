#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，
# 所以，通过变量也能调用该函数
def now():
    print('2016-08-22')

f = now
f()                     # 2016-08-22

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)     # now
print(f.__name__)       # now


# ================================================================
# 定义一个能打印日志的decorator
# 接受一个函数作为参数，并返回一个函数
def log2(func):
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 借助Python的@语法，把decorator置于函数的定义处
# 把@log2放到now2()函数的定义处，相当于执行了语句
#       now2 = log2(now2)
# 由于log2()是一个decorator，返回一个函数，
# 所以，原来的now2()函数仍然存在，
# 只是现在同名的now2变量指向了新的函数，
# 于是调用now2()将执行新函数，即在log2()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，
# 因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
@log2
def now2():
    print('2016-08-23')

# 调用now2()函数，不仅会运行now2()函数本身，
# 还会在运行now2()函数前打印一行日志
now2()
# call now2():
# 2016-08-23


# ==============================================================
# 如果decorator本身需要传入参数，
# 那就需要编写一个返回decorator的高阶函数
# 自定义log的文本
def log3(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 3层嵌套的decorator用法
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#   now3 = log3('execute')(now3)
# 首先执行log3('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now3函数，返回值最终是wrapper函数。
# 但经过decorator装饰之后的函数，now3的__name__属性值
# 已经从原来的'now3'变成了'wrapper'。
# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖**函数签名**的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的
# import functools是导入functools模块
# 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可
@log3('execute')
def now3():
    print('2016-08-24')

now3()
# execute now3():
# 2016-08-24

print(now3.__name__)
# wrapper

print('--------------------------------------------------------')


# =================================================================
# 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可
# 一个完整的不带参数的decorator
def logd(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 一个完整的带参数的decorator
def logt(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logd
def hellome():
    print('Hello me!')

hellome()
print('hellome.__name__ = %s' % hellome.__name__)
'''
call hellome():
Hello me!
hellome.__name__ = hellome
'''


# helloworld = log3('Start')(helloworld)
@logt('Start')
def helloworld():
    print('Hello world!')

helloworld()
print('helloworld.__name__ = %s' % helloworld.__name__)
# print(type(helloworld))       # <class 'function'>
# s = "hello"
# print(type(s))                # <class 'str'>
'''
Start helloworld():
Hello world!
helloworld.__name__ = helloworld
'''

print('----------------------------------------------------------')


#
def log(obj):
    if isinstance(obj, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call')
                if obj:
                    print('%s %s(): ' % (obj, func.__name__))
                else:
                    print('call %s(): ' % func.__name__)
                func(*args, **kw)
                print('end call')
                return
            return wrapper
        return decorator
    else:
        @functools.wraps(obj)
        def wrapper(*args, **kw):
            print('begin call')
            print('call %s(): ' % obj.__name__)
            obj(*args, **kw)
            print('end call')
            return
        return wrapper


@log
def fnc():
    print('I\'m fnc for testing log without parameter')


@log('execute')
def fnc2():
    print('I\'m fnc2 for testing log with parameter')


fnc()
print('fnc.__name__ = %s' % fnc.__name__)
print('----------------------------------')
fnc2()
print('fnc2.__name__ = %s' % fnc2.__name__)

'''
begin call
call fnc():
I'm fnc for testing log without parameter
end call
fnc.__name__ = fnc
----------------------------------
begin call
execute fnc2():
I'm fnc2 for testing log with parameter
end call
fnc2.__name__ = fnc2
'''
