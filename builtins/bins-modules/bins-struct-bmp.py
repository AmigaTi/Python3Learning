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


# 编写一个bmpinfo.py，可以检查任意文件是否是位图文件，
# 如果是，打印出图片大小和颜色数

def bmp_check(file):
    with open(file, 'rb') as f:
        bs = f.read(30)
        # print(bs)
        ts = struct.unpack('<ccIIIIIIHH', bs)
        # print(ts)
        print('File: %s' % file)
        if ts[0] == b'B' and ts[1] == b'M':
            print('File Type: bmp')
            print('size: %d x %d' % (ts[6], ts[7]))
            print('colors: %d' % ts[9])
        else:
            print('File Type: unknown')
        print('---------------------')

bmp_check('goodread.bmp')
bmp_check('goodread.png')


'''
File: goodread.bmp
File Type: bmp
size: 72 x 72
colors: 1
---------------------
File: goodread.png
File Type: unknown
---------------------
'''

