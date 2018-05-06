#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Scale - 范围控件
# 相关方法
# Scale.set()  - 设置当前scale值
# Scale.get()  - 获取当前scale值


root = Tk()                             # 初始化TK()
root.title('Tkinter - Scale')           # 设置窗口标题
root.geometry('300x200')                # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

label = Label(root, text='downloading...', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)


# 带参数的回调函数
def resize(text):
    print("current text = ", text)      # 15
    label.config(font='Helvetica -%d bold' % scale.get())   # 通过config()方法来更改标签字体大小


scale = Scale(root,
              from_=10,             # 最小值，在from后添加下划线是为了避免与关键字from的冲突
              to=40,                # 最大值
              resolution=5,         # 步进值
              orient=HORIZONTAL,    # 水平方向
              label='size',         # 设置标签值，显示在水平Scale的左上方，用于提示
              command=resize)       # 注册回调函数
scale.set(12)                       # 10
scale.pack(fill=X, expand=1)

quit_btn = Button(root, text='quit', command=root.quit, activeforeground='white', activebackground='red')
quit_btn.pack()

root.mainloop()             # 进入消息循环


