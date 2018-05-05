#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Entry - 单行文本框
#
# 用法
# 　　创建:lb = Entry(根对象, [属性列表])
# 　　绑定变量 var = StringVar()    lb = Entry(根对象, textvariable = var)
# 　　获取文本框中的值   var.get()
# 　　设置文本框中的值   var.set()


root = Tk()                           # 初始化TK()
root.title('Tkinter - Entry')         # 设置窗口标题
root.geometry('300x240')

# 在Entry中设定初始值，需要使用textvariable属性与变量进行绑定
var = StringVar()
entry = Entry(root, textvariable=var)
var.set('hello world and hello me')
entry.grid(row=0, column=0, padx=10, pady=10)

# 设置Entry为只读，即不允许用户改变
entry['state'] = 'readonly'


# 设置Entry为密码输入框
# 将Entry作为一个密码输入框来使用，即不显示用户输入的内容值，用特定符号代替。
# 使用用属性show来指定
password_var = StringVar()
password_entry = Entry(root, textvariable=password_var)
password_var.set('type password here')
password_entry.grid(row=1, column=0, padx=10, pady=10)
password_entry['show'] = '*'


# 验证输入内容是否有效
# 1. 回调函数，带参数
def test(content, reason, name):
    # 失去焦点时，回调此函数，并传入由validatecommand属性所指定的参数
    print(content, reason, name)
    if content == 'shellever':
        print('Hello %s' % content)
        return True
    else:
        print('Hello other')
        return False


v = StringVar()
test_cmd = root.register(test)      # 需要将函数进行包装
# %P  表示当输入框的值允许改变，该值有效，该值为当前文本框内容
# %v  表示当前validate的值，此处为小写字母
# %W  表示该组件的名称
test_entry = Entry(root,
                   textvariable=v,
                   validate='focusout',
                   validatecommand=(test_cmd, '%P', '%v', '%W'))

test_entry.grid(row=2, column=0, padx=10, pady=10)
'''
shellever focusout .!entry3
Hello shellever
linuxfor focusout .!entry3
Hello other
'''


# 2. 回调函数，不带参数
def test2():
    if content.get() != 'shellever':
        result.set('It\'s not shellever')
        return False
    else:
        result.set('hello shellever')
        return True


content = StringVar()
input_entry = Entry(root,
                    textvariable=content,
                    validate='focusout',
                    validatecommand=test2)
input_entry.grid(row=3, column=0, padx=10, pady=10)

Label(root, text='result:').grid(row=4, column=0, sticky=W, padx=10, pady=10)

result = StringVar()
Label(root, textvariable=result).grid(row=4, column=1, padx=10, pady=10)


root.mainloop()             # 进入消息循环

