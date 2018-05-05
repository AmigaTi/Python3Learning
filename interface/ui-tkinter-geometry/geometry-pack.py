#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# pack布局管理
# pack是三种布局管理中最常用的，另外两种布局place和grid需要精确指定控件具体的显示位置。
# pack布局可以指定相对位置，精确的位置会由pack系统自动完成。
# pack默认布局方式：
# 从上到下顺序排放，并水平居中
# 将Label控件的宽度设置为文字的宽度


root = Tk()


# fill - 填充方式
# fill=X    将控件宽度填充成父窗口一样宽
Label(root, text='Blue Sky', bg='blue', fg='white').pack(fill=X)

# padding - 控件边距
# padx - 水平外边距
# pady - 垂直外边距
# ipadx - 水平内边距
# ipady - 垂直内边距
Label(root, text='Green Grass', bg='green', fg='black').pack(fill=X, padx=10)
Label(root, text='Red Sun', bg='red', fg='white').pack(fill=X, pady=10)
Label(root, text='Blue Sky', bg='blue', fg='white').pack(ipadx=10)
Label(root, text='Blue Sky', bg='green', fg='black').pack(ipady=10)

# side - 顺序放置控件
Label(root, text='Red Sun', bg='red', fg='white').pack(padx=5, pady=10, side=LEFT)
Label(root, text='Green Grass', bg='green', fg='black').pack(padx=5, pady=10, side=LEFT)
Label(root, text='Blue Sky', bg='blue', fg='white').pack(padx=5, pady=10, side=LEFT)


# demo of side and fill options
frame = Frame(root)
Label(frame, text='Pack Demo of side and fill').pack()
Button(frame, text='A').pack(side=LEFT, fill=Y)
Button(frame, text='B').pack(side=TOP, fill=X)
Button(frame, text='C').pack(side=RIGHT, fill=NONE)
Button(frame, text='D').pack(side=TOP, fill=BOTH)
frame.pack()
# note the top frame does not expand nor does it fill in


# X or Y directions
# demo of expand options - best understood by expanding the root
# widget and seeing the effort on all the three buttons below.
Label(root, text='Pack Demo of expand').pack()
Button(root, text='I do not expand').pack()
Button(root, text='I do not fill x but I expand').pack(expand=1)
Button(root, text='I fill x and expand').pack(fill=X, expand=1)

root.mainloop()

