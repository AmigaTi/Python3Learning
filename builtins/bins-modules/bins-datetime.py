#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import time
from datetime import datetime, timedelta, timezone


# 获取当前日期和时间
# 注意到datetime是模块，datetime模块还包含一个datetime类，
# 通过from datetime import datetime导入的才是datetime这个类
# 如果仅导入import datetime，则必须引用全名datetime.datetime
now = datetime.now()
print(now)                          # 2016-08-25 01:10:22.345052
print(type(now))                    # <class 'datetime.datetime'>
print('------------------------------------------')


# 获取指定日期和时间
# 用指定日期时间创建datetime
dt = datetime(2016, 8, 25, 1, 16)
print(dt)                           # 2016-08-25 01:16:00
print('------------------------------------------')


# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），
# 当前时间就是相对于epoch time的秒数，称为timestamp。
# 可以认为：
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间为：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# timestamp的值与时区毫无关系
# 计算机存储的当前时间是以timestamp表示的，
# 因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）
dt = datetime(2016, 8, 25, 1, 16)
ts = dt.timestamp()                 # 把datetime转换为timestamp
print(ts)                           # 1472058960.0
print('------------------------------------------')


# timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
# timestamp是一个浮点数，没有时区的概念，而datetime是有时区的
# 格林威治标准时间与北京时间差了8小时
ts = 1472058960.0
dt = datetime.fromtimestamp(ts)     # 本地时间，即北京东八区时区时间
print(dt)                           # 2016-08-25 01:16:00
dt = datetime.utcfromtimestamp(ts)  # UTC标准时区的时间
print(dt)                           # 2016-08-24 17:16:00
print('------------------------------------------')


# str转换为datetime
# 注意转换后的datetime是没有时区信息的    +++准确地说时区默认为本地
date_str = '2016-8-25 01:16:16'
format_str = '%Y-%m-%d %H:%M:%S'
dt = datetime.strptime(date_str, format_str)
print('str -> datetime')
print(dt)                           # 2016-08-25 01:16:16

t = time.gmtime(time.time())

print(s)                            # China Standard Time
# -------------------------------------------------
date_str = 'Wed, 27 May 2015 11:00 am CST'[:-4]     # 去掉CST时区信息
format_str = r'%a, %d %b %Y %I:%M %p'               # %Z无法正确解析
dt = datetime.strptime(date_str, format_str)
print(dt)                           # 2015-05-27 11:00:00
print(dt.day)                       # 27
print(dt.tzname())                  # None
print('------------------------------------------')


# datetime转换为str
now = datetime.now()
format_str = '%a, %b %d %H:%M'
dt = now.strftime(format_str)
print(dt)                           # Thu, Aug 25 01:35
print('------------------------------------------')


# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，
# 得到新的datetime。加减可以直接用+和-运算符，
# 不过需要导入timedelta这个类
now = datetime.now()
print(now)                          # 2016-08-25 01:38:30.323599
now = now + timedelta(hours=10)
print(now)                          # 2016-08-25 11:38:30.323599
now = now - timedelta(days=1)
print(now)                          # 2016-08-24 11:38:30.323599
now = now + timedelta(days=2, hours=12)
print(now)                          # 2016-08-26 23:38:30.323599
print('------------------------------------------')


# 本地时间转换为UTC时间
# 本地时间是系统设定时区的时间
# 北京时间是UTC+8:00时区的时间
# UTC时间是UTC+0:00时区的时间
tz_utc_8 = timezone(timedelta(hours=8))     # 创建时区UTC+8:00
now = datetime.now()
print(now)                          # 2016-09-05 16:14:18.856846
print(now.timestamp())              # 1473063258.856846
dt = now.replace(tzinfo=tz_utc_8)           # 强制设置为UTC+8:00
print(dt)                           # 2016-09-05 16:14:18.856846+08:00
print(dt.timestamp())               # 1473063258.856846
print('------------------------------------------')


# 时区转换
# 以先通过utcnow()拿到当前的UTC时间，
# 再转换为任意时区的时间

# 时区转换的关键在于，拿到一个datetime时，
# 要获知其正确的时区，然后强制设置时区，作为基准时间。

# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

# 注：不是必须从UTC+0:00时区转换到其他时区，
# 任何带时区的datetime都可以正确转换，例如peking_dt到tokyo_dt的转换。

# 拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)                       # 2016-08-24 17:50:44.691602+00:00

# astimezone()将转换时区为北京时间
peking_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(peking_dt)                    # 2016-08-25 01:50:44.691602+08:00

# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)                     # 2016-08-25 02:50:44.691602+09:00

# astimezone()将peking_dt转换时区为东京时间
tokyo_dt2 = peking_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)                    # 2016-08-25 02:50:44.691602+09:00
print('======================================')


# ======================================================
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，
# 所以无法区分这个datetime到底是哪个时区，
# 除非强行给datetime设置一个时区

# 假设获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，
# 编写一个函数将其转换为timestamp
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')     # 默认时区属性为None或者说为本地
    m = re.match(r'^UTC([-|+]\d{1,2}):\d{2}$', tz_str)     # 创建匹配对象，并设置提取的分组
    tz_utc_x = timezone(timedelta(hours=int(m.group(1))))   # 创建UTC X:00时区
    dt = dt.replace(tzinfo=tz_utc_x)                        # 将dt强制设置为UTC X:00时区
    return dt.timestamp()                                  # 把datetime转换为timestamp


# 测试
print('Get the testing result: ')
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
'''
Get the testing result:
Pass
'''


