#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, tid, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = tid
        self.thread_name = name
        self.counter = counter

    def run(self):
        print('start thread: %s' % self.name)
        print_time(self.name, self.counter, 5)
        print('exit thread: %s' % self.name)


def print_time(tname, delay, counter):
    while counter:
        if exitFlag:
            tname.exit()
        time.sleep(delay)
        print('%s: %s' % (tname, time.ctime(time.time())))
        counter -= 1


# 创建新线程
t1 = MyThread(1, 'Thread-1', 1)
t2 = MyThread(2, 'Thread-2', 2)


# 开启新线程
t1.start()
t2.start()
t1.join()
t2.join()
print('exit main thread...')

'''
start thread: Thread-1
start thread: Thread-2
Thread-1: Sat Sep  3 17:51:42 2016
Thread-1: Sat Sep  3 17:51:43 2016
Thread-2: Sat Sep  3 17:51:43 2016
Thread-1: Sat Sep  3 17:51:44 2016
Thread-1: Sat Sep  3 17:51:45 2016
Thread-2: Sat Sep  3 17:51:45 2016
Thread-1: Sat Sep  3 17:51:46 2016
exit thread: Thread-1
Thread-2: Sat Sep  3 17:51:47 2016
Thread-2: Sat Sep  3 17:51:49 2016
Thread-2: Sat Sep  3 17:51:51 2016
exit thread: Thread-2
exit main thread...
'''