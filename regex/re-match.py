#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


# 分组

# 用()表示的就是要提取的分组（Group）
# group(0)表示原始字符串，
# group(1)、group(2)……表示第1、2、……个子串

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，
# 否则返回None
s = '010-12345'
pattern = r'^(\d{3})-(\d{3,8})$'
m = re.match(pattern, s)
if m is not None:
    print('match success')
    print('m.group(0) = \'%s\'' % m.group(0))   # m.group(0) = '010-12345'
    print('m.group(1) = \'%s\'' % m.group(1))   # m.group(1) = '010'
    print('m.group(2) = \'%s\'' % m.group(2))   # m.group(2) = '12345'
else:
    print('match failed')


# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
t = re.match(r'^(\d+)(0*)$', '102300').groups()
print(t)        # ('102300', '')

# 非贪婪匹配
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，
# 结果0*只能匹配空字符串了
# 加个?就可以让\d+采用非贪婪匹配
t = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(t)        # ('1023', '00')


# 编译
# 当使用正则表达式时，re模块内部会进行下面步骤：
# 1. 编译正则表达式，若正则表达式的字符串本身不合法，会报错
# 2. 用编译后的正则表达式去匹配字符串
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
t = re_telephone.match('010-12345').groups()
print(t)        # ('010', '12345')
t = re_telephone.match('010-10086').groups()
print(t)        # ('010', '10086')
print('-----------------------------------')


# =========================================================
# 1. 验证Email
# someone@gmail.com
# bill.gates@microsoft.com
# linuxfor@163.com

s1 = 'someone@gmail.com'
s2 = 'bill.gates@microsoft.com'
s3 = 'linuxfor@163.com'
pattern = r'^[0-9a-z\_\.]+@[0-9a-z]+\.[a-z]+$'
re_email = re.compile(pattern)
print('matched: \'%s\'' % re_email.match(s1).group(0))
print('matched: \'%s\'' % re_email.match(s2).group(0))
print('matched: \'%s\'' % re_email.match(s3).group(0))
'''
matched: 'someone@gmail.com'
matched: 'bill.gates@microsoft.com'
matched: 'linuxfor@163.com'
'''


# 2. 验证并提取出带名字的Email地址
# <Tom Paris> tom@voyager.org

s = '<Tom Paris> tom@voyager.org'
pattern = r'^<([a-zA-Z]+)\s+[a-zA-Z]+>\s+([0-9a-z\_\.]+@[0-9a-z]+\.[a-z]+)$'
re_email = re.compile(pattern)
m = re_email.match(s)
print('%s\'s mail: %s' % (m.group(1), m.group(2)))
'''
Tom's mail: tom@voyager.org
'''



