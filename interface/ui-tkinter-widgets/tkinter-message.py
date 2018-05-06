#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Message - 用于显示文本，用法与Label基本一样
# 相关属性说明
# aspect     指定宽高比例，默认width/height=1.5


root = Tk()                             # 初始化TK()
root.title('Tkinter - Message')         # 设置窗口标题
root.geometry('300x200')                # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

# 自动换行
Message(root, text='Hello Message').pack()
# 需要指定足够大的宽度，使之不自动换行
Message(root, text='Hello World and hello me', width=160).pack()

root.mainloop()             # 进入消息循环


