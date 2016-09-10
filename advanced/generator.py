#!/usr/bin/python
# -*- coding: utf-8 -*-


# 列表生成式
L = [x * x for x in range(10)]
print(L)        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 生成器generator
G = (x * x for x in range(10))
print(G)        # <generator object <genexpr> at 0x00544930>

# generator是可迭代对象，使用for循环进行输出
for n in G:
    print(n, end=' ')   # 0 1 4 9 16 25 36 49 64 81


# 定义generator的另一种方法：使用yield
# 变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(i_max):
    i, a, b = 0, 0, 1
    while n < i_max:
        yield b         # return b//需要在外部调用一次后才能解锁进行下次
        a, b = b, a + b
        i += 1
    return 'done'

# 迭代generator函数
for n in fib(6):
    print(n)
print()
'''
1
2
3
5
8
'''


# 杨辉三角: 新一行的每个数字等于其两肩的数字之和
# 将已有行进行补0错位[1,1]-->[0,1,1]和[1,1,0]然后相加即可得到新一行。
def triangles():
    lst = [1]
    while True:
        yield lst
        lst.append(0)     # 先占位，然后修改相应位置上的数值
        lst = [lst[i-1] + lst[i] for i in range(len(lst))]
g = triangles()
for n in range(10):
    print(next(g))

print('------------------------------------------')


def triangles2():
    lst = [1]
    while True:
        yield lst
        lst.append(1)
        tmp = lst[:]       # 只复制数值，不指向同一个对象
        length = len(lst)
        if length > 2:
            for i in range(1, length - 1):
                tmp[i] = lst[i-1] + lst[i]
            lst = tmp[:]
n = 0
for t in triangles2():
    print(t)
    n += 1
    if n == 10:
        break

print('------------------------------------------')


def triangles3():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
g = triangles3()
for n in range(10):
    print(next(g))

'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''
