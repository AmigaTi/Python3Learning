#!/usr/bin/python
# -*- coding: utf-8 -*-


# ===============================================
# 读文件
# ===============================================

f = None
try:
    f = open('./with_file.txt', 'r')        # 以只读模式打开文件
    s = f.read()                            # 读取文件的全部内容
    print(s)                                # 打印文件内容
finally:
    if f:                                   # 如果f不为None
        f.close()                           # 关闭文件
print('----------------------------')
'''
Hello world
Hello me
'''


# ===============================================
# with...as         自动调用close()方法
# ===============================================
# read()            小文件，一次性读取
# read(size)        不能确定文件大小，每次最多读取size个字节的内容
# readline()        每次读取一行内容，可用于配置文件读取
# readlines()       一次读取所有内容并按行返回list

with open('./with_file.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())                 # 去掉末尾的\n
print('----------------------------')
'''
Hello world
Hello me
'''


# 二进制文件，打开模式为rb

with open('./with_monkey.jpg', 'rb') as f:
    print(f.read())
print('----------------------------')


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# 遇到编码错误，则通过errors参数设置为ignore直接忽略掉

with open('./with_gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
print('----------------------------')
'''
你好，世界
你好，我
'''


# ===============================================
# 写文件
# ===============================================

with open('./with_file2.txt', 'w') as f:
    f.write('You look so beautiful.')

# 测试是否内容写入成功
with open('./with_file2.txt', 'r') as f:
    print(f.read())
'''
You look so beautiful.
'''
