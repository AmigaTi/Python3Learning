#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import random


# 参考文章
# [Tkinter 教程12] 布局管理 (Pack Place Grid)
# https://blog.csdn.net/liuxu0703/article/details/54428405


# place布局管理
# place可以显式地指定控件的绝对位置或相对于其他控件的位置
# 所有tkinter的标准控件都可以调用place()方法


root = tk.Tk()
root.title('geometry - place')
# width x height + x_offset + y_offset
root.geometry("300x400+30+30")

# Absolute positioning
tk.Button(root, text='Absolute Placement').place(x=20, y=10)

# Relative positioning
tk.Button(root, text='Relative').place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor=tk.NE)


# place布局示例
# 为Label控件设置随机的背景色，然后计算各个Label的背景色的亮度(灰度值)，
# 如果其亮度小于120，则将其前景色(文字颜色，fg属性)设置为白色，否则为黑色。
# 这样做是为了避免背景色和前景色过于接近而导致文字不易阅读。
languages = ['Python', 'Perl', 'C/C++', 'Java', 'Tcl/Tk']
for i in range(len(languages)):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_color = '#' + "".join(ct_hex)
    label = tk.Label(root,
                     text=languages[i],
                     fg='white' if brightness < 120 else 'black',
                     bg=bg_color)
    label.place(x=20, y=120+i*30, width=120, height=25)

root.mainloop()

