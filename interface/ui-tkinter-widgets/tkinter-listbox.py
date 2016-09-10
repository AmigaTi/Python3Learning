#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Listbox - 列表控件,可以含有一个或多个文本想,可单选也可多选
#
# 用法
#
# 　　创建:lb = ListBox(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=ListBox(根对象, listvariable = var)
# 　　得到列表中的所有值   var.get()
# 　　设置列表中的所有值   var.set((item1, item2, .....))
# 　　添加:lb.insert(item)
# 　　删除:lb.delete(item,...)
# 　　绑定事件 lb.bind('<ButtonRelease-1>', 函数)
# 　　获得所选中的选项 lbl.get(lb.curselection())
# 属性
#
# 　　selectmode可以为BROWSE MULTIPL SINGLE


root = Tk()                 # 初始化TK()
root.title('Listbox')         # 设置窗口标题
root.geometry()             # 设置窗口大小

var = StringVar()
lb = Listbox(root, listvariable=var)
# list_item = [1, 2, 3, 4]
# for item in list_item:
#     lb.insert(END, item)
# lb.delete(2, 4)

var.set(('a', 'ab', 'c', 'd'))
print(var.get())


def print_item(event):
    print(lb.get(lb.curselection()))

lb.bind('<ButtonRelease-1>', print_item)    # 鼠标左键单击释放事件绑定
lb.pack()

root.mainloop()             # 进入消息循环


