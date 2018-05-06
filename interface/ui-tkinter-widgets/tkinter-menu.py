#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import StringVar


PROGRAM_NAME = 'Footprint Editor'


root = Tk()                         # 初始化Tk()
root.title(PROGRAM_NAME)            # 设置窗口标题
# root.iconbitmap(r'C:\Python35\DLLs\pyc.ico')      # 设置图标
root.geometry('300x200')            # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变


# Adding Menubar in the widget
menu_bar = Menu(root)


# tearoff=1 => 此菜单可以独立拉出来，产生悬浮菜单
file_menu = Menu(menu_bar, tearoff=1)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

themes_menu = Menu(tearoff=0)


# Callback function
def _msgbox():
    messagebox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2016.')


def print_themes():
    print('themes: ', v.get())


# Adding menu items
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', underline=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', underline=0)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', underline=0)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S', compound='left')
file_menu.add_separator()       # 添加分隔符，对相关的菜单项进行分组，只是UI上的展示效果
file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', command=root.quit)

edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left')
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left')
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left')
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left')
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left')
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left')

about_menu.add_command(label='About', command=_msgbox)
about_menu.add_command(label='Help', accelerator='Ctrl+H')

view_menu.add_checkbutton(label='Show Line Number')
view_menu.add_cascade(label='Themes', menu=themes_menu)

# theme组内只有一个处于选中状态
v = StringVar()
themes_menu.add_radiobutton(label='Default', variable=v, command=print_themes)
themes_menu.add_radiobutton(label='Dark Light', variable=v, command=print_themes)
v.set('Default')        # 设置默认选中项

# all file menu-items will be added here next
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View', menu=view_menu)
menu_bar.add_cascade(label='About', menu=about_menu)

root.config(menu=menu_bar)      # 设置主菜单


# 设置鼠标右键弹出菜单
def popup(event):
    menu_bar.post(event.x_root, event.y_root)


root.bind('<Button-3>', popup)  # 绑定鼠标的右键事件，按鼠标右键时弹出右键菜单


root.mainloop()             # 进入消息循环


