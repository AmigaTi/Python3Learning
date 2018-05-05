#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# grid布局管理
# grid把控件位置作为一个二维表结构来维护，即按照行列的方式排列控件。
# 控件位置由其所在的行号和列好决定。
# 行号相同而列号不同的几个控件会被彼此上下排列；
# 列号相同而行号不同的几个控件会被彼此左右排列。
# grid布局会自动设置一个合适大小的格子，故不需要为每个格子指定大小。
# 相关属性
# row     指定行号
# column  指定列号


root = Tk()

Label(root, text='Username').grid(row=0, sticky=W)
Label(root, text='Password').grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)

# span [column, columnspan) = [0, 2)
Button(root, text='Login').grid(row=2, column=0, sticky=EW, columnspan=2)

root.mainloop()


