#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import copy

# 深拷贝和浅拷贝
# 深copy新建一个对象重新分配内存地址，复制对象内容。
# 浅copy不重新分配内存地址，内容指向之前的内存地址。
# 浅copy如果对象中有引用其他的对象，如果对这个子对象进行修改，子对象的内容就会发生更改。

# python的浅拷贝，其仅仅是拷贝了 一个整体的对象(应该说一个对象最外面的那一层)，而对于对象里面包含的元素不会进行拷贝。


int_list = [1, 2, 3, [4, 5]]
print('before modified=============')
print('int_list: ', int_list)
print('int_list memory address: ', id(int_list))

# 浅拷贝
shallow_copy = copy.copy(int_list)

# 深拷贝
deep_copy = copy.deepcopy(int_list)

# 对list里面的list对象进行修改
int_list[3].append(6)

print('after modified==============')
print('int_list: ', int_list)
print('int_list memory address: ', id(int_list))
print('int_list[3] memory address: ', id(int_list[3]))
print('----------------------------')
print('shallow_copy: ', shallow_copy)
print('shallow_copy memory address: ', id(shallow_copy))
print('shallow_copy[3] memory address: ', id(shallow_copy[3]))
print('----------------------------')
print('deep_copy: ', deep_copy)
print('deep_copy memory address: ', id(deep_copy))
print('deep_copy[3] memory address: ', id(deep_copy[3]))

'''
before modified=============
int_list:  [1, 2, 3, [4, 5]]
int_list memory address:  1454344018952
after modified==============
int_list:  [1, 2, 3, [4, 5, 6]]
int_list memory address:  1454344018952
int_list[3] memory address:  1454344018824
----------------------------
shallow_copy:  [1, 2, 3, [4, 5, 6]]
shallow_copy memory address:  1454344024392
shallow_copy[3] memory address:  1454344018824
----------------------------
deep_copy:  [1, 2, 3, [4, 5]]
deep_copy memory address:  1454344027016
deep_copy[3] memory address:  1454344025672
'''