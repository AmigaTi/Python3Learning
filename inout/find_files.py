#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


# 编写一个程序，能在当前目录以及当前目录的所有子目录下
# 查找文件名包含指定字符串的文件，并打印出相对路径。
def find_files(k, d='.'):
    all_files = [os.path.join(d, f) for f in os.listdir(d)]
    for f in all_files:
        if os.path.isfile(f) and k in os.path.split(f)[1]:
            print(f)
        elif os.path.isdir(f):
            find_files(k, f)


def do_find():
    key = input('The keyword to find: ')
    # dir = input('The directory to search in: ')
    find_files(key)

do_find()
r'''
The keyword to find: file
.\file-dir.py
.\file-with.py
.\file.txt
.\file2.txt
.\testdir\file-me.py
.\testdir\hello\file-me.py
'''