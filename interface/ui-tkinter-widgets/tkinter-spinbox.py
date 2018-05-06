#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Spinbox


root = Tk()                             # 初始化TK()
root.title('Tkinter - Spinbox')         # 设置窗口标题
root.geometry('300x200')                # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变


Spinbox(root,
        from_=0,        # 最大值
        to=100,         # 最小值
        increment=5     # 步进值
        ).grid(row=0, column=0, padx=5, pady=5)


# 使用values属性来指定步进值序列
# 使用command属性来指定回调函数
def get_spin_value():
    print("current value of spin: ", sp.get())


sp = Spinbox(root,
             values=(0, 2, 3, 5, 7, 11, 13, 17),     # 更次更新使用values指定的值
             command=get_spin_value)                 # 回调函数
sp.grid(row=0, column=1, padx=5, pady=5)


root.mainloop()             # 进入消息循环


