#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.colorchooser as cc

root = tk.Tk()
root.title('Tkinter - ColorChooser')
root.geometry('320x240')


# 创建颜色选取器对话框，返回两种表示的颜色值：(R, G, B) 和 #RRGGBB
def callback_color_chooser():
    color = cc.askcolor()
    print('color = ', color)    # color =  ((163.63671875, 124.484375, 197.76953125), '#a37cc5')


tk.Button(root, text='Ask Color', command=callback_color_chooser).pack(fill=tk.X, padx=10, pady=10)

root.mainloop()
