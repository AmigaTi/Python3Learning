#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Canvas - 用于绘制图形的容器

root = Tk()                             # 初始化TK()
root.title('Tkinter - Canvas')          # 设置窗口标题
root.geometry('300x200')                # 设置窗口大小
root.resizable(width=False, height=True)    # 设置窗口的长宽是否可变

canvas = Canvas(root, bg='white')       # 创建一个画布，背景色为白色

# 绘制矩形
# fill    - 填充颜色
# outline - 边框颜色
# width   - 边框宽度
# dash    - 虚线宽度
rt = canvas.create_rectangle(10, 10, 110, 110, fill='gray', outline='red', width=5, dash=10)

canvas.pack()


# 修改矩形坐标，即实现移动和缩放
canvas.coords(rt, (40, 40, 80, 80))

root.mainloop()             # 进入消息循环


