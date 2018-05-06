#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Toplevel - 与Frame类似，但其包含窗体属性，如title

root = Tk()                             # 初始化TK()
root.title('Tkinter - Toplevel')        # 设置窗口标题
root.geometry('400x300')                # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变


mbYes, mbYesNo, mbYesNoCancel, mbYesNoAbort = 0, 1, 2, 4


def messagebox():
    status_type = mbYesNo
    label_text = 'Yes'
    if status_type == mbYes:
        label_text = 'Yes'
    elif status_type == mbYesNo:
        label_text = 'YesNo'
    elif status_type == mbYesNoCancel:
        label_text = 'YesNoCancel'
    elif status_type == mbYesNoAbort:
        label_text = 'YesNoAbort'
    tpl = Toplevel()
    tpl.title('Toplevel')
    tpl.geometry('300x200')
    Label(tpl, text=label_text).pack()


# 由按钮来启动消息框
Button(root, text='click me', command=messagebox).pack()

root.mainloop()             # 进入消息循环


