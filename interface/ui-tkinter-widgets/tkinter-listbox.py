#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Listbox - 列表控件，可以含有一个或多个文本项，可单选也可多选
#
# 用法
# 　　创建:lb = ListBox(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=ListBox(根对象, listvariable=var)
# 　　得到列表中的所有值   var.get()
# 　　设置列表中的所有值   var.set((item1, item2, .....))
# 　　添加:lb.insert(item)
# 　　删除:lb.delete(item,...)
# 　　绑定事件 lb.bind('<ButtonRelease-1>', 函数)
# 　　获得所选中的选项 lbl.get(lb.curselection())
# 属性
# 　　selectmode可以为BROWSE MULTIPL SINGLE EXTENDED
#               BROWSE - 可以使用鼠标移动选中位置，默认配置
#               SINGLE - 不支持鼠标移动选中位置
#               EXTENDED - 支持使用Shift或Control来进行元素选择


root = Tk()                             # 初始化TK()
root.title('Tkinter - Listbox')         # 设置窗口标题
root.geometry("300x240")                # 设置窗口大小


lb = Listbox(root)
# 项列表框中添加元素
# 插入位置可选有：ACTIVE END
# ACTIVE - 使用当前选中的索引作为插入位置
# END - 向列表框的最后进行插入
for item in ['Python', 'Java', 'C/C++', 'Perl', 'JavaScript']:
    lb.insert(END, item)
lb.grid(row=0, column=0, padx=2, pady=2)
# 删除列表框中的元素项
# 第一个参数为开始的索引值
# 第二个参数为结束的索引值，若不指定则只删除第一个索引项
lb.delete(1, 2)
# lb.delete(0, END)    # 删除全部内容
# 设置默认选中项
lb.select_set(0, END)   # 默认全部选中
# 清除默认选中项
lb.selection_clear(2, END)
# 获取当前列表框中的元素项个数
print('listbox size: %d' % lb.size())   # 3
# 返回指定索引的元素项值
print('lb.get(2) = ', lb.get(2))        # JavaScript
print('lb.get(1, 2) = ', lb.get(1, 2))  # ('Perl', 'JavaScript')
# 返回当前选中的元素项的索引
print('lb.curselection() = ', lb.curselection())    # (0, 1)
# 判断一个元素项是否被选中
print('lb.selection_includes(0) = ', lb.selection_includes(0))  # True


# 创建一个可以多选的列表框
# 依次点击item，均显示为选中状态
# 每次点击item，将改变当前状态，类似Checkbutton
lb = Listbox(root, selectmode=MULTIPLE)
for item in ['Curry', 'Durant', 'Tompson']:
    lb.insert(END, item)
lb.grid(row=1, column=0, padx=2, pady=2)


# 绑定变量
var = StringVar()
lb = Listbox(root, listvariable=var)
# list_item = [1, 2, 3, 4]
# for item in list_item:
#     lb.insert(END, item)
# lb.delete(2, 4)

# 改变变量的值，使用元组来设置与列表框元素
var.set(('a', 'ab', 'c', 'd'))
print(var.get())


def print_item(event):
    print(lb.get(lb.curselection()))


# 使用bind来指定回调函数
lb.bind('<ButtonRelease-1>', print_item)    # 鼠标左键单击释放事件绑定
lb.grid(row=0, column=1, padx=2, pady=2)


root.mainloop()             # 进入消息循环

