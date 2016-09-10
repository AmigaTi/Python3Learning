#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import StringIO


# StringIO
# StringIO不需要close，需要close()的stream也不建议手动close，而是用with自动close
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
# 数据读写不一定是文件，也可以在内存中读写
# 要把str写入StringIO，先创建一个StringIO，然后，像文件一样写入即可
# getvalue()方法用于获得写入后的str
f = StringIO()
count = f.write('hello')
print(count)            # 5
f.write(' ')
f.write('world!')
content = f.getvalue()
print(content)          # hello world!
print('--------------------------------------')


# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

'''
Hello!
Hi!
Goodbye!
'''

