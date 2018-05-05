#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Radiobutton - 单选按钮


root = Tk()                 # 初始化TK()
root.title('Label')         # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变


Radiobutton(root, text='Python').grid(row=0, column=0, sticky=W, padx=10, pady=10)


# 回调函数，按钮组内的元素被选中时，回调此函数
def callback():
    print('current selected: %d' % v.get())


# 通过绑定变量来创建一个Radiobutton组
# 绑定不同的变量属于不同的组，组内的按钮互不影响
v = IntVar()
v.set(1)        # 默认第二个被选中
for i in range(3):
    Radiobutton(root, variable=v, text='Python' + str(i),
                value=i, command=callback).grid(row=1+i, column=0, sticky=W, padx=10, pady=2)

'''
current selected: 2
current selected: 1
current selected: 0
'''

root.mainloop()             # 进入消息循环


