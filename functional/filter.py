#!/usr/bin/python
# -*- coding: utf-8 -*-


# filter()接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)            # [1, 5, 9, 15]


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(l)            # ['A', 'B', 'C']


# ===================================================================
# 用filter求素数
# 先构造一个从3开始的奇数序列的生成器，并且是一个无线序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 无限序列
# 定义一个生成器，不断返回下一个素数
# 这个生成器先返回第一个素数2，然后利用filter()不断产生筛选后的新的序列
def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印100以内的素数
for r in primes():
    if r >= 100:
        break
    print(r)
# ===================================================================


# 回数是指从左向右读和从右向左读都是一样的数
# 例如12321，909
# 利用filter()滤掉非回数
def is_palindrome(n):
    tmp, m = n, 0
    while tmp:
        m = m * 10 + tmp % 10
        tmp //= 10
    return n == m


def is_palindrome2(n):
    s = str(n)
    i, j = 0, len(s) - 1
    if i == j:
        return True
    while i < j:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    if i >= j:
        return True
    else:
        return False


def is_palindrome3(n):
    return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print(list(output))
output = filter(is_palindrome2, range(1, 1000))
print(list(output))
output = filter(is_palindrome3, range(1, 1000))
print(list(output))


