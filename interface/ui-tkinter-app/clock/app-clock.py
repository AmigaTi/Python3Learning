#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import *


# 一个时钟程序
# https://blog.csdn.net/jcodeer/article/details/1826581
# 略有点点修改，详见此博客


# apply()函数在Python3中已经不支持
def apply(f, *args, **kws):
    return f(*args, **kws)


def create_alarm(master):
    """ 创建时间选择组件，包括小时、分钟、秒
    系统默认的时间设置为当前的事件"""
    import time
    now = time.localtime(time.time())
    lf_alarm = LabelFrame(text='Add you alarm')
    master.vHour = StringVar()
    master.vHour.set(now[3])
    Label(lf_alarm, text='Hour:').grid(row=0, column=0)
    # master.omHour = apply(OptionMenu, (lfAlarm, master.vHour) + tuple(range(0, 24)))
    master.omHour = OptionMenu(lf_alarm, master.vHour, *tuple(range(0, 24)))
    master.omHour.grid(row=0, column=1)

    master.vMinute = StringVar()
    master.vMinute.set(now[4])
    Label(lf_alarm, text='Minute:').grid(row=0, column=2)
    # master.omMinute = apply(OptionMenu, (lfAlarm, master.vMinute) + tuple(range(0, 60)))
    master.omMinute = OptionMenu(lf_alarm, master.vMinute, *tuple(range(0, 60)))
    master.omMinute.grid(row=0, column=3)

    master.vSecond = StringVar()
    master.vSecond.set(now[5])
    Label(lf_alarm, text='Second:').grid(row=0, column=4)
    # master.omSecond = apply(OptionMenu, (lfAlarm, master.vSecond) + tuple(range(0, 60)))
    master.omSecond = OptionMenu(lf_alarm, master.vSecond, *tuple(range(0, 60)))
    master.omSecond.grid(row=0, column=5)

    lf_alarm.grid(row=1, column=0, columnspan=6)


def add_alarm(master):
    """将当前的设置添加为一个提醒
    设置最后一个为激活态
    选中最后一个"""
    master.lbAlarm.insert(END, master.vHour.get() + ':' + master.vMinute.get() + ':' + master.vSecond.get())
    master.lbAlarm.selection_clear(0, END)
    master.lbAlarm.selection_set(END)
    master.lbAlarm.activate(END)


def delete_alarm(master):
    """删除一个提醒"""
    master.lbAlarm.delete(ACTIVE)
    if master.lbAlarm.size() > 0:
        master.lbAlarm.selection_set(ACTIVE)


def modify_alarm(master):
    """修改提醒，
    删除原来的提醒，添加一个新的提醒，索引使用原来"""
    t = master.vHour.get() + ':' + master.vMinute.get() + ':' + master.vSecond.get()
    n = master.lbAlarm.curselection()
    master.lbAlarm.delete(n)
    master.lbAlarm.insert(n, t)
    master.lbAlarm.selection_set(n)


def create_alarm_list(master):
    """创建提醒列表，目前所有可用的提醒均显示在这里"""
    master.lbAlarm = Listbox(master)
    master.lbAlarm.grid(row=3, column=0, columnspan=4, rowspan=3, stick=S + N + E + W)


def create_operation(master):
    """创建操作列表，对提醒列表中的提醒进行添加、修改或删除"""
    Button(master, text='Add alarm', command=lambda arg=master: add_alarm(arg)
           ).grid(row=3, column=4, columnspan=2, stick=S + N + E + W)
    Button(master, text='Modify alarm', command=lambda arg=master: modify_alarm(arg)
           ).grid(row=4, column=4, columnspan=2, stick=S + N + E + W)
    Button(master, text='Delete alarm', command=lambda arg=master: delete_alarm(arg)
           ).grid(row=5, column=4, columnspan=2, stick=S + N + E + W)


def show_current_time(master):
    """显示当前时间"""
    lb_current_time = Label(master, text='Current Time:')
    lb_current_time.grid(row=0, column=0, columnspan=2, stick=W)
    master.vCurrentTime = StringVar()
    master.etCurrentTime = Entry(master, textvariable=master.vCurrentTime, state='readonly')
    master.etCurrentTime.grid(row=0, column=2, columnspan=4, stick=S + N + E + W)


def update_time(master):
    """时钟回调函数，用于更新当前时间；
    判断是否满足提醒条件"""
    import time
    now = time.localtime(time.time())
    t = '%d:%d:%d' % (now[3], now[4], now[5])
    master.vCurrentTime.set(t)
    for item in master.lbAlarm.get(0, END):
        if str(item) == t:
            # 如果当前时间与提醒列表中的一致，打印
            print('you have a alarm', item)
    root.after(100, update_time, master)


root = Tk()
show_current_time(root)
create_alarm(root)
create_alarm_list(root)
create_operation(root)
root.after(100, update_time, root)      # 检测周期为100ms
root.mainloop()
