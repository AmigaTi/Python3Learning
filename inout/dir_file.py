#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# 利用os模块编写一个能实现dir -l输出的程序
def dir2(path='.'):
    all_files = [x for x in os.listdir(path) if os.path.isfile(x) or os.path.isdir(x)]
    print('the amounts of items in the current directory: ', len(all_files))
    i = 1
    for f in all_files:
        print(f, end=' ')
        if i % 6 == 0:
            print()
        i += 1
    print()     # newline

dir2()
'''
the amounts of items in the current directory:  9
io-bytesio.py io-file-dir.py io-file-with.py with_file.txt with_file2.txt with_gbk.txt
with_monkey.jpg io-stringio.py testdir
'''