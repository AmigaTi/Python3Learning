#!/usr/bin/python
# -*- coding: utf-8 -*-

# task_master.py
# server，往任务队列中放任务后， 从结果队列中获取结果

import random
# import time
import queue
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support   # 不用加也可以正常启动服务器


# 当在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对
# 原始的task_queue进行操作，那样就绕过了QueueManager的封装，
# 必须通过manager.get_task_queue()获得的Queue接口添加。


# 发送任务的队列
task_queue = queue.Queue()

# 接收结果的队列
result_queue = queue.Queue()


# ??modified
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue
# ??


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


# 注册到网络
# ??modified
def start_server():
    # ??modified
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    # ??register内不要使用lambda，否则win7运行出错
    # ??callable=lambda: task_queue => callable=return_task_queue
    # ??callable=lambda: result_queue => callable=return_result_queue
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # ??

    # 绑定端口5000，设置验证码'abc'
    # win7 需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果
    print('Try get results...')
    # 服务器已经准备好接收数据，故开始启动task_worker.py
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:     # Queue.Empty => queue.Empty
            print('result queue is empty.')

    # 关闭
    manager.shutdown()
    print('master exit.')
# ??

if __name__ == '__main__':
    # freeze_support()      # 注释掉也可以正常运行
    start_server()

r'''
D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\thread-process>python task_master.py
Put task 5250...
Put task 4585...
Put task 140...
Put task 7655...
Put task 114...
Put task 6289...
Put task 7291...
Put task 3540...
Put task 3311...
Put task 4513...
Try get results...
Result: 5250 * 5250 = 27562500
Result: 4585 * 4585 = 21022225
Result: 140 * 140 = 19600
Result: 7655 * 7655 = 58599025
Result: 114 * 114 = 12996
Result: 6289 * 6289 = 39551521
Result: 7291 * 7291 = 53158681
Result: 3540 * 3540 = 12531600
Result: 3311 * 3311 = 10962721
Result: 4513 * 4513 = 20367169
master exit.

D:\MyDocument\MyDevelopment\PyCharmProjects\Basics\thread-process>
'''