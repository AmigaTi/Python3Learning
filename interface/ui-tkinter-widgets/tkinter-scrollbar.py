#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Scrollbar - 滚动条，在屏幕上创建一块矩形区域，多作为容器与其他控件(Listbox/Text)结合使用
# 用法
# 　　Frame(根对象, [属性列表]), 最长用的用法是和别的控件一起使用


root = Tk()                             # 初始化TK()
root.title('Tkinter - Scrollbar')       # 设置窗口标题
root.geometry("300x240")                # 设置窗口大小


def print_item(event):
    print('event: ', event)     # <ButtonRelease event state=Mod1|Mod3|Button1 num=1 x=15 y=63>
    print("curse selection: ", lb.get(lb.curselection()))   # 3


# 创建列表框
var = StringVar()
lb = Listbox(root, height=5, selectmode=BROWSE, listvariable=var)
lb.bind('<ButtonRelease-1>', print_item)    # 绑定回调函数
for item in range(20):
    lb.insert(END, item)


# 创建滚动条 (注意要互相注册回调函数以实现关联)
# 使用Listbox的yscroolcommand来关联Scrollbar的set函数
# 使用Scrollbar的command来关联Listbox的yview函数
scrl = Scrollbar(root, orient=VERTICAL)     # 不指定的话，默认也为垂直方向
scrl.pack(side=RIGHT, fill=Y)               # side指定Scrollbar为居右，fill指定填充整个剩余区域
lb.configure(yscrollcommand=scrl.set)       # 指定Listbox的垂直滚动回调函数为Scrollbar的set
lb.pack(side=LEFT, fill=BOTH)               # side指定Listbox为居左
scrl['command'] = lb.yview                  # 指定Scrollbar的回调函数为Listbox的yview


root.mainloop()             # 进入消息循环


