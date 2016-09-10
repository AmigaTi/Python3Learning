#!/usr/bin/python
# -*- coding: utf-8 -*-


# 依次打印列表中的元素
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('Hello %s!' % name)


# 计算1-10的整数之和
count = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    count += x
print("count = %d" % count)     # count = 55


# 计算1-100的整数之和
count = 0
for x in range(1, 101, 1):
    count += x
print("count = %d" % count)


ls = list(range(1, 11, 1))      # [1, 11), step = 1
print(ls)                       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


person_dict = {'name': 'hellome', 'sex': 'male'}
for k, v in person_dict.items():
    print('%s => %s' % (k, v))
'''
name => hellome
sex => male
'''


# ==============================================================
# Looping Techniques
# ==============================================================

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
'''
robin the brave
gallahad the pure
'''


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
'''
0 tic
1 tac
2 toe
'''


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
'''
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
'''


for i in reversed(range(1, 10, 2)):
    print(i)
'''
9
7
5
3
1
'''