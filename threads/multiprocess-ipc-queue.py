#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os
import time
import random


# issue20160824
# ImportError: cannot import name '_args_from_interpreter_flags'
# rename filename


# 进程间通信
# 操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，
# 提供了Queue、Pipes等多种方式来交换数据。


# 以Queue为例，在父进程中创建两个子进程，
# 一个往Queue里写数据，一个从Queue里读数据
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 若multiprocessing在Windows下调用失败，则先考虑pickle问题。


# 写数据进程执行的代码(生产者)
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码(消费者)
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    que = Queue()
    pw = Process(target=write, args=(que,))
    pr = Process(target=read, args=(que,))
    # 启动子进程pw，写入数据
    pw.start()
    # 启动子进程pr，读取数据
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里为死循环，无法等待其结束，只能强行终止
    pr.terminate()

'''
Process to read: 34588
Process to write: 34580
Put A to queue...
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''
