#!/usr/bin/python
# -*- coding: utf-8 -*-

# 创建一个0-99的数列
L = list(range(100))

# 截取前10个数
print(L[:10])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 反向截取后10个数
print(L[-10:])      # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# 截取前[10, 20)的数
print(L[10:20])     # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 前10个数，每两个取一个
print(L[:10:2])     # [0, 2, 4, 6, 8]

# 所有数，每10个取一个
print(L[::10])      # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 复制
print(L[::10][:])   # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# tuple
print((1, 2, 3, 4, 5)[:3])  # (1, 2, 3)


# 简单输入信息补全
name = ['Adam', 'Alex', 'Amy', 'Bob',
        'Boom', 'Candy', 'Chris', 'David',
        'Jason', 'Justin', 'Bill']

i_name = input('please input name: ').title()
length = len(i_name)

w_name = []
for n in name:
    if n[:length] == i_name:
        w_name.append(n)
if len(w_name) != 0:
    print("Do you want to find %s?" % w_name)
else:
    print("%s not find!" % i_name)


