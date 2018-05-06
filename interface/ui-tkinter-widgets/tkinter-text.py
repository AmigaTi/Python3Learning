#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Text - 可编辑文本框
#
# 用法
# 　　t = Text(根对象)
# 　　添加内容   t.insert(mark, 内容)
# 　　删除内容   t.delete(mark1, mark2)
# 　　其中，mark可以是行号或者特殊标识，例如
#       INSERT     光标的插入点
#       CURRENT    鼠标的当前位置所对应的字符位置
#       END        这个Textbuffer的最后一个字符
#       SEL_FIRST  选中文本域的第一个字符，如果没有选中区域则会引发异常
#       SEL_LAST   选中文本域的最后一个字符，如果没有选中区域则会引发异常


root = Tk()                         # 初始化TK()
root.title('Tkinter - Text')        # 设置窗口标题
# root.geometry('300x200')            # 设置窗口大小

t = Text(root)
t.insert(1.0, 'hello\n')            # 向第一行第一列插入文本
t.insert('2.end', 'hello me\n')     # 向第二行末尾插入文本
t.insert(END, 'hello world\n')      # 向默认插入文本
t.grid(row=0, column=0, rowspan=2, columnspan=2)


# 使用表达式来增强mark
'''
+ count chars      前移count字符
- count chars      后移count字符
+ count lines      前移count行
- count lines      后移count行
linestart          移动到行的开始
linesend           移动到行的结束
wordstart          移动到字的开始
wordend            移动到字的结束
'''


# 创建自定义mark
def forward_chars():
    t.mark_set('test_mark', 1.2)


# 使用自定义mark来插入文本
def insert_text():
    t.insert('test_mark', 'mark')


Button(root, text='forward 5 chars', command=forward_chars).grid(row=2, column=0)
Button(root, text='test mark', command=insert_text).grid(row=2, column=1)

root.mainloop()             # 进入消息循环

