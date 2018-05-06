#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# grid布局管理
# grid把控件位置作为一个二维表结构来维护，即按照行列的方式排列控件。
# 控件位置由其所在的行号和列好决定。
# 行号相同而列号不同的几个控件会被彼此上下排列；
# 列号相同而行号不同的几个控件会被彼此左右排列。
# grid布局会自动设置一个合适大小的格子，故不需要为每个格子指定大小。
# 相关属性
# row     指定行号
# column  指定列号
# rowspan     横跨几行
# columnspan  横跨几列


root = Tk()
root.title('Sign in')
# root.geometry('300x200')


def do_sign_in():
    username = entry_username.get()
    password = entry_password.get()
    if username == 'shellever' and password == '123456':
        label_tip['text'] = 'sign in success'
    else:
        label_tip['text'] = 'username or password error'
        entry_username.delete(0, len(username))
        entry_password.delete(0, len(password))


Label(root, text='Username').grid(row=0, sticky=W)
Label(root, text='Password').grid(row=1, sticky=W)

entry_username = Entry(root)
entry_username.grid(row=0, column=1, sticky=E)
entry_password = Entry(root)
entry_password['show'] = '*'
entry_password.grid(row=1, column=1, sticky=E)

# span [column, columnspan) = [0, 2)
Button(root, text='Login', command=do_sign_in).grid(row=2, column=0, sticky=EW, columnspan=2, padx=2, pady=2)

label_tip = Label(root)
label_tip.grid(row=3, column=0, columnspan=2)

root.mainloop()


