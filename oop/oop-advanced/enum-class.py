#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum, unique


# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print('---------------------------------------')
'''
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
'''


@unique                     # @unique装饰器可以检查保证没有重复值
class Weekday(Enum):
    Sun = 0                 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day = Weekday.Mon
print(day)                  # Weekday.Mon
print(Weekday.Tue)          # Weekday.Tue
print(Weekday['Wed'])       # Weekday.Wed
print(Weekday.Thu.value)    # 4
print(day == Weekday.Fri)   # False
print(Weekday(1))           # Weekday.Mon
print('---------------------------------------')


for name, member in Weekday.__members__.items():
    print(name, '=>', member)
print('---------------------------------------')


for value in Weekday.__members__.values():
    print(value)
print('---------------------------------------')


for value in Weekday.__members__.values():
    print(value.value)

'''
issue:
ImportError: cannot import name 'Enum'
solution:
rename the enum.py filename to enum-class.py
'''