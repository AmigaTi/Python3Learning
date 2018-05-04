#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# 参考文章
# Tkinter教程之Label篇
# https://blog.csdn.net/jcodeer/article/details/1811293


# Label - 标签/文本
#
# 用法
# Label(根对象, [属性列表])
# 属性
# text　    要现实的文本
# fg        前景色
# bg　　    背景色
# font　    字体(颜色, 大小)
# width　   控件宽度
# height　  控件高度
# bitmap    指定显示的位图
# compound  指定文本(text)和图像(bitmap/image)在Label显示的相对位置关系，默认为None


root = Tk()                 # 初始化TK()
root.title('Label')         # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

# 默认只指定bitmap时，文本(text)会被覆盖，只显示图像
# 可选位图：error hourglass info questhead warning gray12 gray25 gray50 gray75
label = Label(root, text='show', bg='gray', bitmap='info', font=('Arial', 12), width=30, height=30)
label.pack(side=LEFT)       # 显示Label控件，LEFT/RIGHT/TOP/BOTTOM

# 同时显示图像和文本
# 可选的位置关系compound：
# left   - 图像居左
# right  - 图像居右
# top    - 图像居上
# bottom - 图像居下
# center - 文字覆盖在图像上
Label(root, text='Warning', compound='left', bitmap='warning').pack(side=TOP)

# 使用颜色值 #RRGGBB
# 使用颜色名称：red green blue yellow lightblue
Label(root, fg='white', bg='#FF00FF', text='hide').pack(side=RIGHT)

# 使用系统相关的颜色值 (Windows)，不建议使用，不利于平台移植
# SystemActiveBorder SystemActiveCaption SystemAppWorkspace SystemBackground
Label(root, fg='white', bg='SystemButtonShadow', text='Windows').pack(side=BOTTOM)


# 文本的多行显示
# 涉及的属性：
# wraplength - 指定多少单位后开始换行
# justify    - 指定多行的对齐方式
# anchor     - 指定文本(text)或图像(bitmap/image)在Label中的显示位置

# anchor可选值及其布局含义：
# nw      n       ne
# w     center    e
# sw      s       se
# 左对齐，文本居中
Label(root, text='a life of bits and pieces, make it better.', bg='gray25', width=40, height=3, wraplength=80, justify='left').pack()
# 居中对齐，文本居左
Label(root, text='a life of bits and pieces, make it better.', bg='gray50', width=40, height=3, wraplength=80, anchor='w').pack()
# 居中对齐，文本居右
Label(root, text='a life of bits and pieces, make it better.', bg='gray75', width=40, height=3, wraplength=80, anchor='e').pack()


root.mainloop()             # 进入消息循环

