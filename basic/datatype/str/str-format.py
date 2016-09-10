#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

# Old string formatting
# % 运算符

# Python has 002 quote types.
d = {'language': 'Python', 'number': 2}
print('%(language)s has %(number)03d quote types.' % d)     # Python has 002 quote types.

print('d: %s' % str(d))         # d: {'number': 2, 'language': 'Python'}s


# str.format()方法

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''

print('常量PI近似值为{0:.3f}'.format(math.pi))
'''
常量PI近似值为3.142
'''

print('{name}网址: {site}'.format(name='菜鸟教程', site='www.runoob.com'))
'''
菜鸟教程网址: www.runoob.com
'''


