#!/usr/bin/env python
# -*- coding:utf-8 -*-


# id() -- 查看内存地址

int_list = [1, 2, 3, [4, 5]]
print('before modified=============')
print('int_list: ', int_list)
print('int_list memory address: ', id(int_list))
