#!/usr/bin/python
# -*- coding: utf-8 -*-

import zlib

# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile

s = 'witch which has which witches wrist watch'
s = s.encode('utf-8')
print(s)            # b'witch which has which witches wrist watch'
print(len(s))       # 41

t = zlib.compress(s)
print(len(t))       # 37

s = zlib.decompress(t)
print(s)            # b'witch which has which witches wrist watch'

s_crc32 = zlib.crc32(s)
print(s_crc32)      # 226805979
