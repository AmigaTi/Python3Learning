#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()

Label(root, text='Username').grid(row=0, sticky=W)
Label(root, text='Password').grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)

# span [column, columnspan) = [0, 2)
Button(root, text='Login').grid(row=2, column=0, sticky=EW, columnspan=2)

root.mainloop()


