#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading


# Lock

# 多线程和多进程最大的不同在于：
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。
# 而多线程中，所有变量都由所有线程共享。
# 所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

# 因为Python的线程虽然是真正的线程，但解释器执行代码时，
# 有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
# 必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
# 让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
# 也只能用到1个核。

# 不过，Python虽然不能利用多线程实现多核任务，
# 但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。


# 银行存款
balance = 5000


# 通过threading.Lock()来创建一个锁lock
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


# 如果我们要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，
# 获得该锁以后才能改。由于锁只有一个，无论多少线程，
# 同一时刻最多只有一个线程持有该锁，故不会造成修改的冲突。

# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，
# 然后继续执行代码，其他线程就继续等待直到获得锁为止。
def run_thread(n):
    for i in range(100000):
        lock.acquire()          # 获取锁
        try:
            change_it(n)        #
        finally:
            lock.release()      # 释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()
print(balance)


