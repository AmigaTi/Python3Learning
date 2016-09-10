#!/usr/bin/python
# -*- coding: utf-8 -*-


score = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(score['Tracy'])       # 85


score['Adam'] = 67
print(score['Adam'])        # 67


# 获取键值并转换为列表
score_keys = list(score.keys())
print(score_keys)           # ['Adam', 'Tracy', 'Bob', 'Michael']

score_keys_sorted = sorted(score_keys)
print(score_keys_sorted)    # ['Adam', 'Bob', 'Michael', 'Tracy']


# 判断字典中是否存在某个键
print('Bob' in score)       # True
print('Jack' not in score)  # True


# 用一个以tuple为元素的列表来初始化字典
tel = dict([('irv', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)                  # {'jack': 4098, 'guido': 4127, 'irv': 4139}


num_pairs = {x: x**2 for x in (2, 4, 6)}
print(num_pairs)            # {2: 4, 4: 16, 6: 36}


tel = dict(irv=4139, guido=4127, jack=4098)
print(tel)                  # {'irv': 4139, 'guido': 4127, 'jack': 4098}


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


if 'hello' not in knights:
    print('the key \'hello\' is not in dict knights.')
'''
the key 'hello' is not in dict knights.
'''


next_post_info = {'next_post': -1, 'next_post_day': 'xxxx-xx-xx'}
next_post = {'next_post': 839, 'next_post_day': '2016-09-15', 'id': 1}
print('next_post_info: %s' % str(next_post_info))   # next_post_info: {'next_post': -1, 'next_post_day': 'xxxx-xx-xx'}

next_post_info = {key: next_post[key] for key in next_post_info.keys()}  # 取部分nex_post值来初始化next_post_info

print('next_post_info: %s' % str(next_post_info))   # next_post_info: {'next_post': 839, 'next_post_day': '2016-09-15'}




