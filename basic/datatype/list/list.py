#!/usr/bin/python
# -*- coding: utf-8 -*-


# 二维数组
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])      # Apple
print(L[1][1])      # Python
print(L[2][2])      # Lisa


attrs = [('http-equiv', 'content-type'), ('content', 'text/html; charset=UTF-8')]
__attrs = {}

# 方法一：将列表转换成字典
for attr in attrs:
    __attrs[attr[0]] = attr[1]
print(__attrs)      # {'content': 'text/html; charset=UTF-8', 'http-equiv': 'content-type'}

# 方法二：将列表转换成字典
__attrs = dict(attrs)
print(__attrs)      # {'content': 'text/html; charset=UTF-8', 'http-equiv': 'content-type'}


t = ('http-equiv', 'content-type')
attrs.append(t)
print(attrs)
# [('http-equiv', 'content-type'), ('content', 'text/html; charset=UTF-8'), ('http-equiv', 'content-type')]


to_addrs = ['linuxfor@163.com', 'linuxfor@live.com']
print('to_addrs <%s>' % str(to_addrs))          # to_addrs <['linuxfor@163.com', 'linuxfor@live.com']>
print('to_addrs <%s>' % ', '.join(to_addrs))    # to_addrs <linuxfor@163.com, linuxfor@live.com>
