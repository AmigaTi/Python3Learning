#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as mb

root = tk.Tk()
root.title('Tkinter - MessageBox')
root.geometry('320x240')


# 显示信息消息框
def callback_info():
    res = mb.showinfo(title='Info', message='This is a information for you.')
    print('result = ', res)     # ok


# 显示警告消息框
def callback_warning():
    res = mb.showwarning(title='Warning', message='This is a warning for you.')
    print('result = ', res)     # ok


# 显示错误消息框
def callback_error():
    res = mb.showerror(title='Error', message='This is a error for you.')
    print('result = ', res)     # ok


# 显示询问消息框，可选有：Yes No
def callback_question():
    res = mb.askquestion(title='Question', message='This is a question for you.')
    print('result = ', res)     # no/yes


# 显示确认/取消消息框，可选有：Yes No
def callback_ok_cancel():
    res = mb.askquestion(title='OkCancel', message='This is a Ok for you.')
    print('result = ', res)     # no/yes


# 显示是/否消息框，可选有：Yes No
# 使用default属性来指定默认焦点位置为No，不指定的话默认为Yes
def callback_yes_no():
    res = mb.askyesno(title='YesNo', message='This is a Yes for you.', default=mb.NO)
    print('result = ', res)     # True/False


# 显示重试/取消消息框，可选有：Yes No
def callback_retry_cancel():
    res = mb.askyesno(title='RetryCancel', message='This is a retry for you.')
    print('result = ', res)     # True/False


tk.Button(root, text='Information', command=callback_info).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='Warning', command=callback_warning).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='Error', command=callback_error).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='Question', command=callback_question).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='OkCancel', command=callback_ok_cancel).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='YesNo', command=callback_yes_no).pack(fill=tk.X, padx=10, pady=2)
tk.Button(root, text='RetryCancel', command=callback_retry_cancel).pack(fill=tk.X, padx=10, pady=2)


root.mainloop()
