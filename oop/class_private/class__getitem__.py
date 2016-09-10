#!/usr/bin/python
# -*- coding: utf-8 -*-


# __getitem__()
# 实现__getitem__()方法，使实例对象可以使用下标来获取元素
# 在__getitem__()方法中通过判断传入的参数类型(int或slice切片对象)
# 实现类似list的切片方法

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):        # item为int索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):      # item是切片对象
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            lst = []
            for x in range(stop):
                if x >= start:
                    lst.append(a)
                a, b = b, a + b
            return lst

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])

print(f[0:4])
print(f[:4])

'''
1
1
2
3
[1, 1, 2, 3]
[1, 1, 2, 3]
'''