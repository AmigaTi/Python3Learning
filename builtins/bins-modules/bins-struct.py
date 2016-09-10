#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct

# struct.pack(fmt, v1, v2, ...)
# struct.unpack(fmt, buffer)

# format
# <         little-endian
# >         big-endian
# c         char            (1 byte)
# I         unsigned int    (4 bytes)
# H         unsigned short  (2 bytes)
# h         short           (2 bytes)
# L         unsigned long   (4 bytes)
# l         long            (4 bytes)

# struct的pack函数把任意数据类型变成bytes
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
b = struct.pack('>I', 10240099)
print(b)            # b'\x00\x9c@c'


# unpack把bytes变成相应的数据类型
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
t = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(t)            # (4042322160, 32896)


b = struct.pack('hhl', 1, 2, 3)
t = struct.unpack('hhl', b)
size = struct.calcsize('hhl')
print(b)
print(t)
print(size)

'''
b'\x01\x00\x02\x00\x03\x00\x00\x00'
(1, 2, 3)
8
'''