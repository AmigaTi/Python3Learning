#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# 获取操作系统类型
# posix - Linux/Unix/Mac OS X
# nt    - Windows
print(os.name)          # nt


# 获取详细的系统信息
# uname()函数在Windows上不提供
# print(os.uname())


# 获取系统环境变量
print(os.environ)
# 获取某个环境变量的值
print(os.environ.get('PATH'))
print(os.environ.get('PYTHON_HOME', 'default'))


# 执行外部命令
# os.system()函数用于运行shell命令或者cmd命令

# 打开图片
os.system('start goodread.png')

# D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\builtins\bins-modules
print(os.path.abspath('.'))

# D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\builtins\bins-modules
print(os.getcwd())


# 执行cmd环境下的java命令
# returnCode来接收命令执行结果，0表示执行成功
returnCode = os.system('java -version')
print('returnCode: ', returnCode)       # 0


# 获取命令执行的输出信息
# 1. 通过重定向命令将输出保存到临时文件中
# returnCode = os.system('java -version > java_version.txt')    # 在命令行窗口中手动执行也接收不到此输出信息
returnCode = os.system('dir | findstr txt > result.txt')
print('returnCode: ', returnCode)       # 0
# 使用cmd命令打开当前路径下的txt文本文件
os.system('start notepad result.txt')

# 2. 通过os.popen()来获取命令输出
# 返回值result是一个打开的文件对象，用于保存系统命令的输出
# 通过调用对象其read()方法来获取命令输出
result = os.popen('dir | findstr txt')
print(result)                   # <os._wrap_close object at 0x00000223CB3588D0>
print(result.read())            # 05/13/2018  17:01                48 result.txt
