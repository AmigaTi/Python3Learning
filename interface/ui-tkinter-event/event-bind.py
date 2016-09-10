#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()

Label(root, text='Click at different\n locations in the frame below').pack()


def callback(event):
    print(dir(event))
    print('you clicked at', event.x , event.y)

frame = Frame(root, bg='khaki', width=130, height=80)
frame.bind('<Button-1>', callback)
frame.pack()

root.mainloop()

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num', 'send_event', 'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']
you clicked at 84 18
'''
