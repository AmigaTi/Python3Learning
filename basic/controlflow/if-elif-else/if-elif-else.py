#!/usr/bin/python
# -*- coding: utf-8 -*-

height = 1.75       # m
weight = 80.5       # kg

# hStr = input('height(m): ')
# wStr = input('weight(kg): ')

# height = float(hStr)
# weight = float(wStr)

BMI = weight / (height ** 2)
print("BMI: %f" % BMI)

if BMI > 32:
    print('严重肥胖')
elif BMI > 28:
    print('肥胖')
elif BMI > 25:
    print('过重')
elif BMI > 18.5:
    print('正常')
else:
    print('过轻')

'''
# Result
height(m): 1.68
weight(kg): 58
BMI: 20.549887
正常
'''


# ===============================================================
a, b, c = 1, 2, 3
print('(a, b, c) = (%d, %d, %d)' % (a, b, c))       # 0. (a, b, c) = (1, 2, 3)

# 二选一的判断写法

# 1. 常规写法
if a > b:
    c = a
else:
    c = b
print('1. (a, b, c) = (%d, %d, %d)' % (a, b, c))    # 1. (a, b, c) = (1, 2, 2)


# 2. 表达式写法
c = a if a > b else b
print('2. (a, b, c) = (%d, %d, %d)' % (a, b, c))    # 2. (a, b, c) = (1, 2, 2)


# 3. 二维列表写法 +++
c = [b, a][a > b]
print('3. (a, b, c) = (%d, %d, %d)' % (a, b, c))    # 3. (a, b, c) = (1, 2, 2)
print(['Second', 'First'][True])                    # First
print(['Second', 'First'][False])                   # Second


# 4. and-or写法
c = (a > b and [a] or [b])[0]
print('4. (a, b, c) = (%d, %d, %d)' % (a, b, c))    # 4. (a, b, c) = (1, 2, 2)




