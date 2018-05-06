#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
root.title('Tkinter - FileDialog')
root.geometry('320x240')


# 创建打开文件对话框，获取文件的完整路径
def callback_openfilename():
    filename = fd.askopenfilename()
    print('[open]filename = ', filename)      # $filename


# 指定要保存的文件名称及路径
def callback_savefilename():
    filename = fd.asksaveasfilename()
    print('[save]filename = ', filename)


# 选择一个目录，返回此目录的完整路径
def callback_directory():
    directory = fd.askdirectory()
    print('directory = ', directory)


tk.Button(root, text='File Open', command=callback_openfilename).pack(fill=tk.X, padx=10, pady=10)
tk.Button(root, text='File Save', command=callback_savefilename).pack(fill=tk.X, padx=10, pady=10)
tk.Button(root, text='Directory Select', command=callback_directory).pack(fill=tk.X, padx=10, pady=10)


root.mainloop()
