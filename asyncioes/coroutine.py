#!/usr/bin/python
# -*- coding: utf-8 -*-


# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，
# 通过锁机制控制队列和等待，但一不小心就可能死锁。

# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，
# 待消费者执行完毕后，切换回生产者继续生产，效率极高。


# consumer函数是一个generator
# yield -> return
def consumer():
    r = ''
    while True:
        print('before yield---------> r = ', r)
        n = yield r     # 接收调用者发出的参数赋值给n，并将r数值返回给调用者
        print('after yield---------< r = ', r)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


# chm search: send (generator.method)
# generator.send(value)
# Resumes the execution and “sends” a value into
# the generator function. The value argument becomes the result of the
# current yield expression. The send() method returns the next value
# yielded by the generator, or raises StopIteration if the generator
# exits without yielding another value. When send() is called to start
# the generator, it must be called with None as the argument, because
# there is no yield expression that could receive the value.
def produce(c):
    # 因为第一次调用yield表达式，还没有接受参数赋值的变量，所以只能传递None作为send的参数
    print('c.send(None)...')
    c.send(None)        # 调用c.send(None)启动生成器generator 为了初始化r = '200 OK'，相当于初始化操作
    for n in range(1, 6):       # [1, 6)
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   # 将参数n传递给yield
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


# 把一个consumer传入produce后：
# 1. 首先调用c.send(None)启动生成器
# 2. 然后，一旦生产了东西，通过c.send(n)切换到consumer执行
# 3. consumer通过yield拿到消息，处理，又通过yield把结果传回
# 4. produce拿到consumer处理的结果，继续生产下一条消息
# 5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，
# 所以称为协程，而非线程的抢占式多任务。

cons = consumer()
produce(cons)


'''
c.send(None)...
before yield---------> r =
[PRODUCER] Producing 1...
after yield---------< r =
[CONSUMER] Consuming 1...
before yield---------> r =  200 OK
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 2...
after yield---------< r =  200 OK
[CONSUMER] Consuming 2...
before yield---------> r =  200 OK
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 3...
after yield---------< r =  200 OK
[CONSUMER] Consuming 3...
before yield---------> r =  200 OK
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
after yield---------< r =  200 OK
[CONSUMER] Consuming 4...
before yield---------> r =  200 OK
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
after yield---------< r =  200 OK
[CONSUMER] Consuming 5...
before yield---------> r =  200 OK
[PRODUCER] Consumer return: 200 OK
'''















