#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess


# subprocess模块可以启动一个子进程，然后控制其输入和输出

# 通过call()方法来执行系统命令，并返回命令执行结果，0表示成功
# 类似方法有：os.system()
# AttributeError: module 'subprocess' has no attribute 'call'
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code: ', r)
print('===' * 20)


# 通过check_output()方法来执行系统命令，并返回执行的输出信息，而非状态码
# 类似方法有：os.popen()
result = subprocess.check_output('python -V')
print('result:\n', result)                          # b'Python 3.6.4\r\n'
print('result:\n', result.decode('utf-8'))          # Python 3.6.4
print('===' * 20)


# 如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：

# set q=mx
# python.org
# exit
