#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Entry - 单行文本框
#
# 用法
#
# 　　创建:lb =Entry(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=Entry(根对象, textvariable = var)
# 　　获取文本框中的值   var.get()
# 　　设置文本框中的值   var.set(item1)


root = Tk()                 # 初始化TK()
root.title('Entry')         # 设置窗口标题
root.geometry()             # 设置窗口大小
var = StringVar()
e = Entry(root, textvariable=var)
var.set('hello me')
e.pack()

root.mainloop()             # 进入消息循环

