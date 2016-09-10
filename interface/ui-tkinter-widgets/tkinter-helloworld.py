#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1.导入Tkinter包的所有内容
from tkinter import *
import tkinter.messagebox as messagebox


# 2. 从Frame派生一个Application类，这是所有Widget的父容器
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。

# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

# pack()方法把Widget加入到父容器中，并实现布局。
# pack()是最简单的布局，grid()可以实现更复杂的布局。

# 在createWidgets()方法中，创建一个Label和一个Button，
# 当Button被点击时，触发self.quit()使程序退出。
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，
        # 使用tkMessageBox.showinfo()可以弹出消息对话框。
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        # self.helloLabel = Label(self, text='Hello, world!')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


# 3. 实例化Application，并启动消息循环
# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。
app = Application()                 # 实例化Application
app.master.title('Hello World')     # 设置窗口标题
app.master.geometry('200x100')      # 设置窗口大小
app.master.resizable(width=False, height=True)  # 设置窗口的长宽是否可变
app.mainloop()                      # 主消息循环













