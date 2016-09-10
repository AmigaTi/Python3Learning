#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle


# 序列化pickling          把变量从内存中变成可存储或传输的过程
# 反序列化unpickling      把变量内容从序列化的对象重新读到内存的过程

# 可以把序列化后的内容写入磁盘或者通过网络传输到别的机器上。

# Python提供了pickle模块来实现序列化。


# pickle.dumps()方法把任意对象序列化成一个bytes，
# 然后，就可以把这个bytes写入文件。

d = dict(name='Bob', age=20, score=88)

bts = pickle.dumps(d)           # pickle.dumps()
print(bts)


# 把一个对象序列化并写入文件

# pickle.dump()方法直接把对象序列化后写入一个file-like Object
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
f = open('pickle_dump.pkd', 'wb')       # pkd -> PicKle Dump
pickle.dump(d, f)               # pickle.dump()
f.close()
'''
b'\x80\x03}q\x00(X\x05\x00\x00\x00scoreq\x01KXX\x03\x00\x00\x00ageq\x02K\x14X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
'''


# 当要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，

# 从文件中反序列化出一个对象

# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
# 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已
f = open('pickle_dump.pkd', 'rb')
d = pickle.load(f)              # pickle.load()
f.close()
print(d)
'''
{'score': 88, 'age': 20, 'name': 'Bob'}
'''


