#!/usr/bin/python
# -*- coding: utf-8 -*-


for i in range(5):          # [0, 5)
    print(i)
'''
0
1
2
3
4
'''


for i in range(5, 9):       # [5, 9)
    print(i)
'''
5
6
7
8
'''


for i in range(0, 10, 3):   # [0, 10), step = 3
    print(i)
'''
0
3
6
9
'''


# 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao']
for i in range(len(a)):
    print(i, a[i])
'''
0 Google
1 Baidu
2 Runoob
3 Taobao
'''


# 创建一个列表
l = list(range(5))
print(l)        # [0, 1, 2, 3, 4]
