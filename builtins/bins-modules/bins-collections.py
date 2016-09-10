#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict
from collections import OrderedDict, Counter


# namedtuple
# namedtuple是一个函数，用来创建一个自定义的tuple对象，
# 规定了tuple元素的个数，并可用属性而不是索引来引用tuple的某个元素


# 用namedtuple可以很方便地定义一种数据类型，
# 它具备tuple的不变性，又可以根据属性来引用
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)                        # Point(x=1, y=2)
print(p.x)                      # 1
print(p.y)                      # 2
print(isinstance(p, Point))     # True
print(isinstance(p, tuple))     # True
print('-----------------------------')


# 用坐标和半径表示一个圆，也可以用namedtuple定义
# namedtuple('名称', [属性list])
# AttributeError: can't set attribute
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(3, 4, 5)
print(c)        # Circle(x=3, y=4, r=5)
print('-----------------------------')


# deque
# 使用list存储数据时，按索引访问元素很快，但插入和删除元素就很慢，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
# deque除了实现list的append()和pop()外，还支持appendleft()
# 和popleft()，这样就可以非常高效地往头部添加或删除元素。
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)                # deque(['y', 'a', 'b', 'c', 'x'])
print(q[1])             # a
print('-----------------------------')


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入

# 除了在Key不存在时返回默认值，defaultdict的其他行为
# 跟dict是完全一样的
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])       # abc
print(dd['key2'])       # N/A
print('-----------------------------')


# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，无法确定Key的顺序
# 如果要保持Key的顺序，可以用OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)        # {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)       # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))      # ['z', 'y', 'x']
print('-----------------------------')


# OrderedDict可以实现一个FIFO（先进先出）的dict，
# 当容量超出限制时，先删除最早添加的Key
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        # containsKey=1时表示key已存在，则执行修改操作
        # containsKey=0时表示key不存在，则执行添加操作
        containskey = 1 if key in self else 0       # ??
        # 当已达最大容量，当新加key不存在时，会运行这段，先删除最先添加的
        # 当key存在时，不会运行这段，会运行第2个if进行修改
        if len(self) - containskey >= self.capacity:
            # popitem移除键值对并返回，last=true时按LIFO顺序返回
            # last=false时按FIFO顺序返回
            last = self.popitem(last=False)
            print('remove: ', last)
        if containskey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdateOrderedDict(2)
luod['first'] = 'Hello'
luod['second'] = 'World'
luod['third'] = 'Me'
print(luod)
print('-----------------------------')
'''
add:  ('first', 'Hello')
add:  ('second', 'World')
remove:  ('first', 'Hello')
add:  ('third', 'Me')
LastUpdateOrderedDict([('second', 'World'), ('third', 'Me')])
'''


# Counter
# Counter是一个简单的计数器
# Counter实际上也是dict的一个子类
c = Counter()
for ch in 'programming':
    c[ch] += 1

# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'n': 1, 'p': 1, 'o': 1})
print(c)
print('-----------------------------')

