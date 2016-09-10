#!/usr/bin/python
# -*- coding: utf-8 -*-

# 计算100以内所有奇数之和
counts = 0
n = 99
while n > 0:
    counts += n
    n -= 2
print(counts)       # 2500

L = ['Bart', 'Lisa', 'Adam']
N = len(L)
i = 0
while i < N:
    print("Hello %s" % L[i])
    i += 1
