#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
递归像是溯源一样，从现象追溯回至本质。
上层建筑都有其最坚固的下层基础构造。
"""


"""
走台阶算法


问题描述：
N个台阶，一次可以走一步或者两步，求走这n个台阶有多少种方法


问题分析：
本质上是斐波那契数列。
使用反向思维考虑问题，即要走到n级台阶的方式有：
1. 从n-1级台阶一次走一步的方式走到n级台阶上
2. 从n-2级台阶一次走两步的方式走到n级台阶上
以上面方式走，走到n级台阶的方式有f(n)种，并且有以下关系：
f(n) = f(n-1) + f(n-2)
当n = 1时，可得 f(1) = 1
当n = 2时，可得 f(2) = 2

参考文章：
n级阶梯，每次走一步或两步，问最多有多少种走法
https://zhidao.baidu.com/question/680394145672323012.html
"""


# 解决方法
# 1. 递归方法
def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 2. 非递归方法
def fibonacci2(n):
    if n <= 2:
        return n
    fib1 = 1
    fib2 = 2
    fibn = 0
    for i in range(3, n+1, 1):
        fibn = fib1 + fib2
        fib1 = fib2
        fib2 = fibn

    return fibn


"""
约瑟夫环问题


问题描述：
假设编号依次是 0，1，2，...，n-1 的n个人围成一个环，从编号是0的人开始依次报数，
从1报到m且报m的人从环里退出，后面的人重新从1开始报数，直到剩下一个人为止，
问环里最后剩下的那个人的编号是多少？


问题分析：
设 n 个人报数的解为 f(n, m) (以0开始编号，若编号总是从1开始，则解为 f(n, m)+1 )。
第一个人（编号一定是 m-1）出列之后，剩下的 n-1 个人组成一个新的约瑟夫环（以编号为 k = m % n 的人开始）：
k, k+1, k+2, ..., n-2, n-1, 0, 1, 2, ..., k-2
并且从 k 开始报 0

把编号做一下转换：
k   --> 0
k+1 --> 1
k+2 --> 2
...
...
k-2 --> n-2
变换后就成为了 n-1 个人报数的子问题。

假设 n-1 个人报数的子问题其解为 f(n-1, m)，则从上面的转换可以知道：f(n, m) = (f(n-1, m) + m) % n

从而有以下的递推公式：
f(1, m) = 0
f(n, m) = (f(n-1, m) + m) % n 或者 f(i, m) = (f(i-1, m) + m) % i (i > 1; i = n, n-1, ..., 2)
注：f(n, m)表示第n个人报数m退出最后胜利的编号


参考文章：
约瑟夫环之二(用递归的思想解决Josephus问题)
https://blog.csdn.net/wusuopubupt/article/details/18214999
"""


def josephus(n, m):
    if n == 1:
        return 0
    else:
        return (josephus(n-1, m) + m) % n


def josephus2(n, m):
    result = 0
    for i in range(2, n+1):
        result = (result+m) % i
    return result


if __name__ == "__main__":
    # 走台阶算法 - 斐波那契数列
    print(fibonacci(10))        # 89
    print(fibonacci2(10))       # 89

    # 约瑟夫环问题
    # 退出顺序依次是：4 3 5 1 2
    print(josephus(6, 5))       # 0
    # 退出顺序依次是：2 5 0 4 1 7 3
    print(josephus2(8, 3))      # 6
