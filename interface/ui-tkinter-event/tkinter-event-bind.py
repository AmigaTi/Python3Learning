#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


"""
按钮与功能的绑定方式：
1. 在按钮组件被声明时用command属性声明，command属性接收一个函数名，不用加引号
2. 使用bind()方法在组件被创建后进行绑定，该方法是Misc类的一个方法，并且可以调用多次实现多个事件的绑定
bind(事件类型, 带一个参数的回调函数)

事件类型的描述方式：
<MODIFIER-MODIFIER-TYPE-DETAIL>
MODIFIER表示修饰符，可选取值有：
Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
B3, Alt, Button4, B4, Double, Button5, B5 Triple,
Mod1, M1
TYPE表示类型，可选取值有：
Activate, Enter, Map,
ButtonPress, Button, Expose, Motion, ButtonRelease
FocusIn, MouseWheel, Circulate, FocusOut, Property,
Colormap, Gravity Reparent, Configure, KeyPress, Key,
Unmap, Deactivate, KeyRelease Visibility, Destroy,
Leave
DETAIL表示细节，对第二个参数的一些辅助说明
DETAIL is the button number for ButtonPress,
ButtonRelease and DETAIL is the Keysym for KeyPress and
KeyRelease.


常见事件：
<Button-1>                  鼠标左击事件
<Button-2>                  鼠标中击事件
<Button-3>                  鼠标右击事件
<Double-Button-1>           双击事件
<Triple-Button-1>           三击事件

<Bx-Motion>                 鼠标移动事件，x=[1,2,3]分别表示左、中、右鼠标操作
<B1-Motion>                 鼠标左键移动事件
<B2-Motion>                 鼠标中键移动事件
<B3-Motion>                 鼠标右键移动事件

<ButtonRelease-x>           鼠标释放事件，x=[1,2,3],分别表示鼠标的左、中、右键操作
<ButtonRelease-1>           鼠标左键释放事件
<ButtonRelease-2>           鼠标中键释放事件
<ButtonRelease-3>           鼠标右键释放事件

<Enter>                     鼠标释放事件
<Leave>                     鼠标离开时产生此事件

<BackSpace>                 键盘退格按键事件
<Return>                    键盘回车按键事件
<F5>                        键盘F5按键事件
<Shift_L>                   键盘左Shift按键事件
<Shift_R>                   键盘右Shift按键事件

<Key>                       所有的按键事件
<space>                     空格键事件
<less>                      小于键事件

<Shift-Up>                  组合键Shift+Up事件
<Control-Alt-a>             组合键Ctrl+Alt+A事件

"""


root = Tk()

Label(root, text='Click at different\n locations in the frame below').pack()


def callback(event):
    print(dir(event))
    print('you clicked at', event.x, event.y)


frame = Frame(root, bg='khaki', width=130, height=80)
frame.bind('<Button-1>', callback)
frame.pack()

root.mainloop()

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num', 'send_event', 'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']
you clicked at 84 18
'''
