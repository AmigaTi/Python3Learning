#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Menubutton - 已过时，从Tk8.0开始使用Menu代替

root = Tk()                                 # 初始化TK()
root.title('Tkinter - Menubutton')          # 设置窗口标题
root.geometry('300x200')                    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

menubutton = Menubutton(root, text='Lang')
menubutton.pack()

user_choice = IntVar()
user_choice.set(1)  # OFFICEOpen默认选中

file_menu = Menu(menubutton, tearoff=False)
file_menu.add_radiobutton(label='OFFICEOpen', variable=user_choice, value=1)
file_menu.add_radiobutton(label='WPSOpen', variable=user_choice, value=2)

# 这里不是root
menubutton.config(menu=file_menu)

'''
mbLang = Menubutton(root, text='Language')
mbLang.menu = Menu(mbLang)

# 生成菜单项
for item in ['Python', 'PHP', 'CPP', 'Java']:
    mbLang.menu.add_command(label=item)

mbLang['menu'] = mbLang.menu
mbLang.pack(side=LEFT)


# 添加Checkbutton菜单项
mbOS = Menubutton(root, text='OS')
mbOS.menu = Menu(mbOS)
for item in ['Unix', 'Linux', 'Soloris', 'Windows']:
    mbOS.menu.add_checkbutton(label=item)
mbOS['menu'] = mbOS.menu
mbOS.pack(side=LEFT)
'''

root.mainloop()             # 进入消息循环

