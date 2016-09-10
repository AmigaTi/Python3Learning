#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


print('Process (%s) start...' % os.getpid())
print('-----------------------------------')

# Only works on Unix/Linux/Mac
# AttributeError: module 'os' has no attribute 'fork'
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，
# 就fork出子进程来处理新的http请求。


