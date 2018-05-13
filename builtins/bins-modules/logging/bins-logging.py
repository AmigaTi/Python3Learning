#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

'''
参考文章：
http://www.cnblogs.com/yyds/p/6901864.html

logging模块的日志级别
|日志等级|描述|
|---|---|
|DEBUG|最详细的日志信息，典型应用场景是问题诊断|
|INFO|信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作|
|WARNING|当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的|
|ERROR|由于一个更严重的问题导致某些功能不能正常运行时记录的信息|
|CRITICAL|当发生严重错误，导致应用程序不能继续运行时记录的信息|

logging模块定义的格式字符串字段
'''

# 配置日志器
# logging.basicConfig()函数是一个一次性的配置工具，只在第一次调用时起作用
# filename - 日志输出文件，配置后将不再控制台上输出
# level    - 日志级别
# format   - 日志格式
# datefmt  - 日期/时间格式
LOG_FILE = 'my.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")


# 输出结果中每行日志记录的各个字段含义分别是：
# 日志级别:日志器名称:日志内容
'''
WARNING:root:This is a warning log.
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log.
'''