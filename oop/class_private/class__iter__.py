#!/usr/bin/python
# -*- coding: utf-8 -*-


# __iter__()
# __next__()
# 实现一个__iter__()方法，来返回一个迭代对象，
# 然后for循环会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1   # 初始化两个计数器

    def __iter__(self):
        return self                 # 返回实例对象本身

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 20:           # 退出循环
            raise StopIteration()
        return self.__a             # 返回下一个值

for n in Fib():
    print(n)

'''

1
1
2
3
5
8
13
'''
