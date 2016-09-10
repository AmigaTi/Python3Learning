#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import threading


# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持

# asyncio的编程模型就是一个消息循环。
# 从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

@asyncio.coroutine      # 把一个generator标记为coroutine类型
def hello(num):
    print('Hello world! (%d, %s)' % (num, threading.current_thread()))
    # 异步调用asyncio.sleep(1)
    # asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，
    # 而是去执行EventLoop中其他可以执行的coroutine，因此可以实现并发执行。
    yield from asyncio.sleep(1)     # asyncio.sleep()也是一个coroutine
    print('Hello again! (%d, %s)' % (num, threading.current_thread()))


loop = asyncio.get_event_loop()                 # 获取EventLoop

tasks = [hello(1), hello(2), hello(3)]          # 用Task封装两个coroutine
loop.run_until_complete(asyncio.wait(tasks))    # 执行coroutine # or hello()

loop.close()                                    # 关闭EventLoop


# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

'''
Hello world! (2, <_MainThread(MainThread, started 43436)>)
Hello world! (1, <_MainThread(MainThread, started 43436)>)
Hello world! (3, <_MainThread(MainThread, started 43436)>)
Hello again! (2, <_MainThread(MainThread, started 43436)>)
Hello again! (1, <_MainThread(MainThread, started 43436)>)
Hello again! (3, <_MainThread(MainThread, started 43436)>)
'''