#!/usr/bin/python
# -*- coding: utf-8 -*-

sites = ['Baidu', 'Google', 'Runoob', 'Taobao']
for site in sites:
    if site == 'Runoob':
        print('菜鸟教程')
        break       # 在循环到"Runoob"时会跳出循环体
    print('循环数据 ' + site)
else:
    print('没有循环数据')
print('完成循环')

'''
循环数据 Baidu
循环数据 Google
菜鸟教程
完成循环
'''
