#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


# 切分字符串


# 使用str.split()方法切分字符串
# 无法识别连续的空格
s = 'a b   c'
l = s.split(' ')
print(l)            # ['a', 'b', '', '', 'c']


# 使用正则表达式切分字符串
# 无论多少个空格都可以正常分割
l = re.split(r'\s+', s)
print(l)            # ['a', 'b', 'c']


s = 'a,b, c  d'
l = re.split(r'[\s,]+', s)
print(l)            # ['a', 'b', 'c', 'd']


s = 'a,b;; c  d'
l = re.split(r'[\s,;]+', s)
print(l)            # ['a', 'b', 'c', 'd']


s = 'a/b\;; c  d/f\g'
l = re.split(r'[\s,;/\\]+', s)
print(l)            # ['a', 'b', 'c', 'd', 'f', 'g']


def prepare_alphanumeric(_s=''):
    for i in range(ord('0'), ord('z') + 1):
        _s += ' ' + chr(i)
    alphanumeric = re.split(r'[\s\W_]+', _s.lstrip())
    print(len(alphanumeric))        # 62
    print(alphanumeric)

prepare_alphanumeric()


