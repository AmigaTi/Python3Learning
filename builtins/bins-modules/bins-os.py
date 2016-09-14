#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# 操作系统类型
# posix - Linux/Unix/Mac OS X
# nt    - Windows
print(os.name)          # nt


# 获取详细的系统信息
# uname()函数在Windows上不提供
# print(os.uname())


# 系统环境变量
print(os.environ)
# 获取某个环境变量的值
print(os.environ.get('PATH'))
print(os.environ.get('PYTHON_HOME', 'default'))

# 执行外部命令
# os.system()函数用于运行shell命令或者cmd命令
#
# 使用cmd命令打开当前路径下的txt文本文件
os.system('start notepad firstme.txt')

# 打开图片
os.system('start goodread.png')

# D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\builtins\bins-modules
print(os.path.abspath('.'))

# D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\builtins\bins-modules
print(os.getcwd())
