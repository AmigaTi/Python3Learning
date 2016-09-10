#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce


# map
# map函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])
print(list(r))      # [1, 4, 9, 16, 25]


# reduce
# reduce函数：把一个函数作用在一个序列[x1, x2, x3, ...]上，
# reduce把结果继续和序列的下一个元素做累计计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4, 5])
print(r)            # 15


# -------------------------------------------------------
# str2int
def str2int(s):
    def fn(x, y):
        return x * 10 + y
        # return lambda x, y: x * 10 + y

    def char2num2(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]
    return reduce(fn, map(char2num2, s))

r = str2int('12345')
print(r)
# -------------------------------------------------------


# 1.
# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']

L2 = list(map(normalize, L1))
print(L2)       # ['Adam', 'Lisa', 'Bart']


# 2.
# 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(lst):
    return reduce(lambda x, y: x * y, lst)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
# 3 * 5 * 7 * 9 =  945


# 3.
# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]

    def split2(cstr):
        lst = []
        i = 0
        for ch in cstr:
            if ch == '.':
                break
            i += 1
        lst.append(cstr[:i])
        lst.append(cstr[i+1:])
        return lst

    def construct(a, b):
        return a + b/10**len(str(b))

    return reduce(construct, [reduce(fn, map(char2num, l)) for l in split2(s)])

print('str2float(\'123.456\') = ', str2float('123.456'))
# str2float('123.456') =  123.456

'''
# for test customized split function
f = '123.456'
i = 0
for ch in f:
    if ch == '.':
        print(i)    # 3
        break
    i += 1
print(f)
print(f[:i])
print(f[i+1:])
'''