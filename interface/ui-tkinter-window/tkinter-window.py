#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk


# 获取屏幕大小
def get_screen_size(root):
    return root.winfo_screenwidth(), root.winfo_screenheight()


# 获取窗口大小
def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


# 将窗口置于屏幕居中显示
def centralize_window(root, ww, wh):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - ww) / 2           # left
    y = (sh - wh) / 2           # top
    # width x height + x_offset + y_offset
    root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))


root = tk.Tk()                                  # 初始化TK()
root.title('Tkinter - Window')                  # 设置窗口标题
# root.geometry('600x400')                      # 设置窗口大小
# root.overrideredirect(1)                      # 去除边框
root.iconbitmap('PowerPoint_Letter_64px.ico')   # 设置标题栏的默认图标
centralize_window(root, 600, 400)               # 窗口于屏幕居中

# root.maxsize(600, 400)                 # 设置最大化窗口大小
# root.minsize(300, 240)                 # 设置最小化窗口大小
root.resizable(0, 0)                     # 禁止调整窗口大小，即最大化按钮会变灰

root.mainloop()                          # 进入消息循环

