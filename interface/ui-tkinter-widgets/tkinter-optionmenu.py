#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()                                 # 初始化TK()
root.title('Tkinter - OptionMenu')          # 设置窗口标题
root.geometry('300x200')                    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

v = StringVar(root)
v.set('Python')             # 设置默认值
option_menu = OptionMenu(root, v, 'Python', 'Perl', 'Java')
#lang = ['Python', 'Perl', 'Java']
#option_menu = apply(OptionMenu, (root, v) + tuple(lang))
option_menu.pack()


def print_option(event):
    print('current option: ', v.get())


# 绑定OptionMenu的点击事件回调函数
option_menu.bind('<Button-1>', print_option)


root.mainloop()             # 进入消息循环

