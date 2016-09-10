#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading


# 任何进程默认就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程，
# threading模块有个current_thread()函数，永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，
# 名字仅仅在打印时用来显示，完全没有其他意义，
# 为指定名字，Python自动给线程命名为Thread-1，Thread-2...


# 启动一个线程就是把一个函数传入并创建Thread实例，
# 然后调用start()开始执行

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(1, 6):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()       # 启动线程活动
t.join()        # 等待子线程中止
print('thread %s ended.' % threading.current_thread().name)

'''
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
'''

