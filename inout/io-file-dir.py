#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join('.', 'testdir'))
# 创建一个目录
# os.mkdir('./testdir')
# 删掉一个目录
# os.rmdir('./testdir')


# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，
# 它们只对字符串进行操作。

# 把两个路径合成一个时，不要直接拼字符串，
# 而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# path/to
# 而Windows下会返回这样的字符串：
# path\to

# 通过os.path.split()函数，这样可以把一个路径拆分为两部分，
# 后一部分总是最后级别的目录或文件名。
print(os.path.split('path/to/with_file.txt'))
# ('path/to', 'with_file.txt')

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('path/to/with_file.txt'))
# ('path/to/file', '.txt')


# 文件操作

# 重命名文件
# os.rename('test.txt', 'test.py')

# 删除文件
# os.remove('test.py')


# 复制文件的函数居然在os模块中不存在：
# 原因是复制文件并非由操作系统提供的系统调用。
# shutil模块提供了copyfile()的函数等很多实用函数，是os模块的补充。


# 利用Python的特性来过滤文件
# 列出当前目录下的所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)            # ['testdir']


# 列出所有的.py文件
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l)            # ['io-bytesio.py', 'io-file-dir.py', 'io-file-with.py', 'io-stringio.py']


