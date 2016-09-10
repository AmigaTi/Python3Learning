#!/usr/bin/python
# -*- coding: utf-8 -*-

height = 1.75       # m
weight = 80.5       # kg

hStr = input('height(m): ')
wStr = input('weight(kg): ')

height = float(hStr)
weight = float(wStr)

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