#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Button - 按钮
#
# 用法
#
# 　　Button(根对象, [属性列表])


root = Tk()                 # 初始化TK()
root.title('Button')         # 设置窗口标题
root.geometry()             # 设置窗口大小

t = Text(root)
t.pack()


def print_hello():
    t.insert('1.0', 'hello me\n')


btn_left = Button(root, text='press', command=print_hello)
btn_right = Button(root, text='press', command=print_hello)
btn_center = Button(root, text='press', command=print_hello)


# btn.pack(fill=X, expand=1)
btn_left.pack(side=LEFT)
btn_right.pack(side=RIGHT)
btn_center.pack()           # center

root.mainloop()             # 进入消息循环


