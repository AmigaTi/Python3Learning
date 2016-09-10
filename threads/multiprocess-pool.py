#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os
import time
import random


# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

# 代码解读：

# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process。

# 注意输出的结果，task 0，1，2，3是立刻执行的，
# 而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小为4，
# 因此最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
# 由于Pool的默认大小是CPU的核数，若拥有8核CPU，至少9个子进程才能看到等待效果。

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool(4)         # 创建进程池，用于批量启动子进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))        #
    print('Waiting for all subprocess done...')
    p.close()           # 不再添加新的进程
    p.join()            # 等待所有子进程执行完毕
    print('All subprocess done.')


'''
Parent process 8008.
Waiting for all subprocess done...
Run task 0 (3704)...
Run task 1 (8064)...
Run task 2 (3124)...
Run task 3 (7704)...
Task 2 runs 0.87 seconds.
Run task 4 (3124)...
Task 4 runs 0.81 seconds.
Task 3 runs 1.90 seconds.
Task 0 runs 2.03 seconds.
Task 1 runs 2.01 seconds.
All subprocess done.
'''

