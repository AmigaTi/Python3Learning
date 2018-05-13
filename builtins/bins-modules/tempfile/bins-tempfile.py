#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tempfile


# 创建临时文件，关闭后也需要手动删除文件
# os.remove(file)
def make_file():
    file_name = 'temp.%s.txt' % os.getpid()
    temp = open(file_name, 'w+b')
    try:
        print('temp: {}'.format(temp))      # temp: <_io.BufferedRandom name='temp.7328.txt'>
        print('temp.name: {}'.format(temp.name))    # temp.name: temp.7328.txt
        temp.write(b'hello world and hello me!')
        temp.seek(0)
        print('--' * 20)
        print('content: {}'.format(temp.read()))    # content: b'hello world and hello me!'
    finally:
        temp.close()
        # os.remove(file_name)


# 使用tempfile.TemporaryFile()方法创建临时文件，关闭时自动清除文件
def make_temp_file():
    temp = tempfile.TemporaryFile()
    try:
        print('temp: {}'.format(temp))          # temp: <tempfile._TemporaryFileWrapper object at 0x000001430AEF85C0>
        print('temp.name: {}'.format(temp.name))    # temp.name: C:\Users\xxx\AppData\Local\Temp\tmpv8l_16uc
        temp.write(b'hello world and hello me!')
        temp.seek(0)
        print('--' * 20)
        print('content: {}'.format(temp.read()))    # content: b'hello world and hello me!'
    finally:
        temp.close()        # It will be destroyed as soon as it is closed.
    print('exist: {}'.format(os.path.exists(temp.name)))    # exist: False


# 使用tempfile.NamedTemporaryFile()方法创建临时文件，关闭时自动清除文件
def make_named_temp_file():
    temp = tempfile.NamedTemporaryFile()
    try:
        print('temp: {}'.format(temp))      # temp: <tempfile._TemporaryFileWrapper object at 0x0000020F518574A8>
        print('temp.name: {}'.format(temp.name))    # temp.name: C:\Users\xxx\AppData\Local\Temp\tmpvsg6oog9
        temp.write(b'hello world and hello me!')
        temp.seek(0)
        print('--' * 20)
        print('content: {}'.format(temp.read()))    # content: b'hello world and hello me!'
    finally:
        temp.close()
    print('exist: {}'.format(os.path.exists(temp.name)))    # exist: False


# 使用tempfile.NamedTemporaryFile()方法创建临时文件，关闭时自动清除文件
# 相关属性说明：
# prefix - 指定临时文件名称前缀
# suffix - 指定临时文件名称后缀
# dir    - 指定临时文件存放目录
def make_named_temp_file_with_option():
    temp = tempfile.NamedTemporaryFile(prefix='temp_', suffix='.txt')
    try:
        print('temp: {}'.format(temp))      # temp: <tempfile._TemporaryFileWrapper object at 0x00000237E205A5C0>
        print('temp.name: {}'.format(temp.name))    # temp.name: C:\Users\xxx\AppData\Local\Temp\temp_kqsjf0p4.txt
        temp.write(b'hello world and hello me!')
        temp.seek(0)
        print('--' * 20)
        print('content: {}'.format(temp.read()))    # content: b'hello world and hello me!'
    finally:
        temp.close()
    print('exist: {}'.format(os.path.exists(temp.name)))    # exist: False


if __name__ == '__main__':
    make_file()
    print('==' * 20)
    make_temp_file()
    print('==' * 20)
    make_named_temp_file()
    print('==' * 20)
    make_named_temp_file_with_option()
