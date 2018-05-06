#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.simpledialog as sd

root = tk.Tk()
root.title('Tkinter - SimpleDialog')
root.geometry('320x240')


# 创建一个整数输入对话框
# initialvalue  初始值
# prompt        提示信息
# title         提示框标题
def callback_integer():
    res = sd.askinteger(title='prompt', prompt='input a integer:', initialvalue=100)
    print('integer result: ', res)      # None 100


# 创建一个浮点数输入对话框
# minvalue      最小值
# maxvalue      最大值
def callback_float():
    res = sd.askfloat(title='float', prompt='input a float:', minvalue=0, maxvalue=10)
    print('float result: ', res)        # 9.6


# 创建一个字符串输入对话框
def callback_string():
    res = sd.askstring(title='string', prompt='input a string:')
    print('string result: ', res)       # hello


tk.Button(root, text='Ask Integer', command=callback_integer).pack(fill=tk.X, padx=10, pady=10)
tk.Button(root, text='Ask Float', command=callback_float).pack(fill=tk.X, padx=10, pady=10)
tk.Button(root, text='Ask String', command=callback_string).pack(fill=tk.X, padx=10, pady=10)


root.mainloop()
