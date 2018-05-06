#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Button - 按钮
#
# 用法
# 　　Button(根对象, [属性列表])
# 属性
# width    宽度
# height   高度
# bd       边框宽度(board width)，默认为1或2个像素
# relief   按钮风格设置 (可选值有：flat groove raised ridge solid sunken)
# state    按钮状态设置 (可选值有：normal active disabled)

root = Tk()                             # 初始化TK()
root.title('Tkinter - Button')          # 设置窗口标题
root.geometry()                         # 设置窗口大小
root.resizable(0, 0)                    # 禁止调整窗口大小，即最大化按钮会变灰

t = Text(root)
t.pack()


def print_hello():
    t.insert('1.0', 'hello me\n')


def handle_event(event):
    t.insert('2.0', 'event.time = %d\n' % event.time)
    t.insert('2.0', 'event.type = %s\n' % event.type)
    t.insert('2.0', 'event.widget = %s\n' % event.widget)
    t.insert('2.0', 'event.keysym = %s\n' % event.keysym)


# 通过command属性来指定Button的回调函数
btn_left = Button(root, text='left', command=print_hello)
btn_left.pack(side=LEFT)

# 通过设置relief=FLAT，将Button变成Label
btn_right = Button(root, text='right', relief=RIDGE)
btn_right.pack(side=RIGHT)

# 和Label一样，可以使用compound属性来同时显示文本与图像
btn_center = Button(root, text='center', compound='left', bitmap='info')
btn_center.pack()           # center

# 控件焦点问题
# 回调函数需要携带一个参数event
btn_center.bind("<Return>", handle_event)
btn_center.focus_set()


# 指定Button的宽度与高度三种方式
# 1. 创建Button对象时，指定宽度与高度
# 2. 使用属性width和height来指定宽度与高度
# 3. 使用configure方法来指定宽度与高度
b1 = Button(root, text='WidthHeight', width=10, height=2)
b1.pack(side=LEFT)

b2 = Button(root, text='WidthHeight2')
b2['width'] = 10
b2['height'] = 2
b2.pack()

# DISABLED NORMAL ACTIVE
b3 = Button(root, text='WidthHeight3', state=DISABLED)
b3.configure(width=10, height=2)
b3.pack(side=RIGHT)


# 绑定Button与变量
# 设置Button在textvariable属性
def change_text():
    if b['text'] == 'text':
        v.set('change')
    else:
        v.set('text')


v = StringVar()
# 通过textvariable属性将变量v与Button绑定，当v值变化时，Button显示的文本也随之变化
b = Button(root, textvariable=v, command=change_text)
v.set('text')
b.pack()


root.mainloop()             # 进入消息循环


"""
event.time = 1249669468
event.keysym = Return
event.widget = .!button3
event.type = KeyPress
"""
