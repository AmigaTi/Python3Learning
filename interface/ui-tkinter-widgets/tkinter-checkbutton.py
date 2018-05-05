#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Checkbutton - 多选按钮
# 可以表示两种状态：On和Off
# 可以设置回调函数，每当点击此按钮时会调用回调函数


root = Tk()                                 # 初始化TK()
root.title('Tkinter - Checkbutton')         # 设置窗口标题
root.geometry('300x200')                    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

Checkbutton(root, text='Python').grid(row=0, column=0, sticky=W, padx=10, pady=10)


# 设置Checkbutton的回调函数，每次点击都将回调此函数
# 设置variable属性来获取当前状态：
# On - 默认为1
# Off - 默认为0
def callback():
    print('type this button')
    print('current status: %d' % status.get())


status = IntVar()
Checkbutton(root, text='Callback', variable=status, command=callback).grid(row=1, column=0, sticky=W, padx=10, pady=10)
'''
type this button
current status: 1
type this button
current status: 0
'''


# 修改状态默认返回值
# 通过onvalue和offvalue属性来设置Checkbutton的状态值
# onvalue      设置选中状态值
# offvalue     设置未选中状态值
def callback2():
    print('type this button')
    print('current status: %s' % status2.get())


status2 = StringVar()
Checkbutton(root,
            text='Customized',
            onvalue='Python',
            offvalue='Other',
            variable=status2,
            command=callback2).grid(row=2, column=0, sticky=W, padx=10, pady=10)
'''
type this button
current status: Python
type this button
current status: Other
'''

root.mainloop()             # 进入消息循环

