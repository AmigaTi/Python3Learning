#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Label - 标签
#
# 用法
# 　　  Label(根对象, [属性列表])
#
# 属性
#
#       text　    要现实的文本
#       bg　　    背景颜色
#       font　    字体(颜色, 大小)
#       width　   控件宽度
#       height　  控件高度


root = Tk()                 # 初始化TK()
root.title('Label')         # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变
l = Label(root, text='show', bg='gray', font=('Arial', 12), width=5, height=2)
l.pack(side=LEFT)           # LEFT/RIGHT/TOP/BOTTOM

root.mainloop()             # 进入消息循环

