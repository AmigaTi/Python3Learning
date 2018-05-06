#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.dialog as tdialog

root = tk.Tk()
root.title('Tkinter - Dialog')
root.geometry('320x240')


# 创建一个自定义对话框
def callback_customized_dialog():
    dialog = tdialog.Dialog(None,
                            title='Customized Dialog',
                            text='This is a customized dialog',
                            bitmap=tdialog.DIALOG_ICON,
                            default=0,
                            strings=('Yes', 'No', 'Cancel'))
    print(dialog.num)


tk.Button(root, text='Customized Dialog', command=callback_customized_dialog).pack(fill=tk.X, padx=10, pady=10)
tk.Button(root, text='Quit', command=root.quit).pack(fill=tk.X, padx=10, pady=10)


root.mainloop()
