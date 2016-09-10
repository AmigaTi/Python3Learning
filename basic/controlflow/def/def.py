#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


# 空函数
def nop():
    pass


# 使用内置函数isinstance()来实现数据类型检查
# 只允许整数和浮点数类型的参数
def cabs(ia):
    if not isinstance(ia, (int, float)):
        raise TypeError('wrong operand type')
    if ia >= 0:
        return ia
    else:
        return -ia

print("abs(-1) = %d" % cabs(-1))


# 返回多个值
def move(ix, iy, step, angle=0):
    nx = ix + step * math.cos(angle)
    ny = iy - step * math.sin(angle)
    return nx, ny       # tuple，不需要加括号

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)             # 151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6)
print(r)                # (151.96152422706632, 70.0)


# ax^2 + bx + c = 0 (a != 0)
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

print(quadratic(2, 3, 1))       # (-0.5, -1.0)
print(quadratic(1, 3, -4))      # (1.0, -4.0)


# ========================================================================
# 默认参数
# 必选参数在左，默认参数在右
def power(ix, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= ix
    return s

print(power(5))         # 25
print(power(5, 2))      # 25


# =====================================================
def enroll(name, gender, age=16, city='Shenzhen'):
    print('--------------------')
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)

enroll('Sarah', 'Female')
enroll('Bob', 'Male', 18)       #
enroll('Adam', 'Male', city='Beijing')  # 跳过左前面的默认参数时，需指定名字
# =====================================================


# ========================================================================
# 默认参数必须指向不变对象
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l

print(add_end())
print(add_end())


# 由于参数个数不确定，使用list或tuple作为参数
def calc(nums):
    isum = 0
    for n in nums:
        isum += n * n
    return isum

print(calc([1, 2, 3]))          # 14
print(calc((1, 3, 5, 7)))       # 84


# ========================================================================
# 可变参数 - *list/*tuple
def calc2(*nums):
    counts = 0
    for n in nums:
        counts += n * n
    return counts

print(calc2())                  # 0
print(calc2(1, 2, 3))           # 14
print(calc2(1, 3, 5, 7))        # 84

# Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去
l = [1, 2, 3]                   # list
t = (1, 3, 5, 7)                # tuple
print(calc2(*l))                # 14
print(calc2(*t))                # 84


# ========================================================================
# 关键词参数 - **dict
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

# name:  Michael age:  30 other:  {}
person('Michael', 30)

# name:  Bob age:  35 other:  {'city': 'Beijing'}
person('Bob', 35, city='Beijing')

# name:  Adam age:  31 other:  {'gender': 'Male', 'job': 'Engineer'}
person('Adam', 31, gender='Male', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# name:  Jack age:  23 other:  {'job': 'Engineer', 'city': 'Beijing'}
person('Jack', 23, **extra)


# *args必须在**kws之前
def cheese_shop(kind, *args, **kws):
    print('-- Do you have any', kind, '?')
    print('-- I\'m sorry, we\'re all out of', kind)
    for arg in args:
        print(arg)
    print('-' * 40)
    keys = sorted(kws.keys())
    for kw in keys:
        print(kw, ':', kws[kw])

cheese_shop('Limburger', 'It\'s very runny, sir.',
            'It\'s really very, VERY runny, sir.',
            keeper='Michael Palin',
            client='John Cleese',
            sketh='Cleese Shop Sketch')


# ========================================================================
# 命名关键字参数 - *
# 调用方式：命名关键字参数必须传入参数名，否则调用错误
def student(name, age, *, address, fav):
    print(name, age, address, fav)

student('Jack', 22, address='Beijing', fav='sport')


# ========================================================================
# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))          # 120


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact2(5))         # 120
print(fact_iter(5, 1))  # 120


# 汉诺塔目标: 把A柱子上的k个盘子移动到C柱子
# k个盘子分解成两份 = 最底的一个盘子 + 其他上面的k-1个盘子
# 递归思想：将目标分解成三个小的子目标
# 1. 将前(k-1)个盘子从A移动到B上
# 2. 将最底下的最后一个盘子从A移动到C上
# 3. 将B上的(k-1)个盘子移动到C上
# 然后每个子目标又是一次独立的汉诺塔游戏，
# 也就可以继续分解目标直到k为1
def hanoi_tower(k, a, b, c):
    if k == 1:
        print("%s --> %s" % (a, c))     # A --> C
    else:
        hanoi_tower(k-1, a, c, b)       # 1.
        hanoi_tower(1, a, b, c)         # 2.
        hanoi_tower(k-1, b, a, c)       # 3.

n = 3
# n = int(input('Enter the number: '))
hanoi_tower(n, 'A', 'B', 'C')

# 测试结果
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
