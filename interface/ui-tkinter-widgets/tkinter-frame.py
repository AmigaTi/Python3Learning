#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Frame - 在屏幕上创建一块矩形区域,多作为容器来布局窗体
#
# 用法
#
# 　　Frame(根对象, [属性列表])


root = Tk()                 # 初始化TK()
root.title('Frame')      # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

Label(root, text='校训', font=('Arial', 20)).pack()

frm = Frame(root)

# Left
frm_l = Frame(frm)
Label(frm_l, text='厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_l, text='博学', font=('Arial', 15)).pack(side=TOP)
frm_l.pack(side=LEFT)

# Right
frm_r = Frame(frm)
Label(frm_r, text='敬业', font=('Arial', 15)).pack(side=TOP)
Label(frm_r, text='乐群', font=('Arial', 15)).pack(side=TOP)
frm_r.pack(side=RIGHT)

frm.pack()

root.mainloop()             # 进入消息循环



















