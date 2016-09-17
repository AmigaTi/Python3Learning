#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import uuid

from webapp.www.config import configs

"""
ghelper(get function helper)
"""


# 交叉依赖导致无法整成找到ghelper的模块属性
# 获取唯一的id号
def get_unique_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)  # 15 + 32 + 3 = 50


# --------------------------------------------------------------------------------------------
# 获取定义在config.py中的关于数据库的配置信息
def get_database_conf():
    database = configs.database
    host = database.host
    port = database.port
    user = database.user
    password = database.password
    db = database.db
    return host, port, user, password, db       # tuple


# 获取定义在config.py中的关于服务器的配置信息
def get_server_conf():
    server = configs.server
    host = server.host
    port = server.port
    return host, port                           # tuple


def get_cookie_conf():
    cookie = configs.cookie
    name = cookie.name
    key = cookie.key
    return name, key


def get_cookie_name():
    return configs.cookie.name


def get_cookie_key():
    return configs.cookie.key

