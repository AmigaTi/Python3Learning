#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import time
import hashlib
import logging

from webapp.www.models import User
from webapp.www.apierror import APIValueError
from webapp.www.apierror import APIPermissionError
from webapp.www.config import configs
from webapp.www.models import next_id


logging.basicConfig(level=logging.INFO)


# 存储分页信息，用于分页显示Blog的功能
# Page.limit/Page.offset 用于SQL语句的条件设定limit=(p.offset, p.limit)
class Page(object):
    def __init__(self, item_count, page_str='1', page_size=10):
        self.item_count = item_count                            # blog总篇数
        self.page_size = page_size                              # 每页显示数，即页大小
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)    # 总页数
        self.page_index = Page.get_page_index(page_str)         # 页索引从1开始
        self.offset = self.page_size * (self.page_index - 1)    # 页偏移量 = 每页大小 * (页索引 - 1)
        self.limit = self.page_size                             # 保存页大小
        if item_count == 0 or (self.page_index > self.page_count):  # 若blog总篇数为0或页索引大于总页数则重置为第一页
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        self.has_next = self.page_index < self.page_count       # 是否有下一页，当页索引小于页总数时为True
        self.has_previous = self.page_index > 1                 # 是否有上一页，当页索引大于1时为True

    @classmethod
    def get_page_index(cls, page_str, default=1):
        try:
            page = int(page_str)
        except ValueError:
            return default
        return [default, page][page > 0]


# 检查用户
# 数据库改表，有个列是0或1表示管理员
def check_user(user, adminonly=True):
    if not adminonly and user is None:
        raise APIPermissionError('please signin first.')
    if user is None or not user.admin:
        raise APIPermissionError('just admin only')


# 检查字符串是否为空
def check_string(**kw):
    for field, string in kw.items():
        if not string or not string.strip():
            raise APIValueError(field, '%s cannot be empty.' % field)


_RE_EMAIL = re.compile(r'^[a-z0-9.\-_]+@[a-z0-9\-_]+(\.[a-z0-9\-_]+){1,4}$')  # Redundant character escape
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


# 检查邮箱和密码的格式是否合法
def check_email_password(email, password):
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('Invalid email.')
    if not password or not _RE_SHA1.match(password):
        raise APIValueError('Invalid password.')


# 将文本装换成html
def text2html(text):
    lines = map(
        lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
        filter(lambda s: s.strip() != '', text.split('\n'))
    )
    return ''.join(lines)


def make_passwd_sha1(uid, password):
    pwd_str = '%s:%s' % (uid, password)
    return hashlib.sha1(pwd_str.encode('utf-8')).hexdigest()


def make_user_sha1(user, expires):
    user_str = '%s-%s-%s-%s' % (user.id, user.passwd, expires, configs.cookie.key)
    return hashlib.sha1(user_str.encode('utf-8')).hexdigest()


# Generate cookie str by user.
def user2cookie(user, max_age):
    # max_age - cookie生命周期
    # expires - cookie失效日期，即在创建后的max_age时间后过期
    expires = str(int(time.time() + max_age))
    sha1 = make_user_sha1(user, expires)
    cookie_list = [user.id, expires, sha1]              # create cookie list
    return '-'.join(cookie_list)                       # id-expires-sha1


# Parse cookie and load user if cookie is valid.
async def cookie2user(cookie_str):
    if not cookie_str:
        return None
    try:
        cookie_list = cookie_str.split('-')             # get cookie list
        if len(cookie_list) != 3:
            return None
        uid, expires, sha1 = cookie_list
        if int(expires) < time.time():      # 检查cookie的失效期是否小于当前日期，若是则表名该cookie以失效
            return None
        user = await User.find(uid)         # 根据uid在数据库中来查找用户
        if user is None:
            return None
        if sha1 != make_user_sha1(user, expires):       # 重新计算sha1值，并与浏览器中的cookie携带的SHA1比较
            logging.info('invalid sha1 from client cookie')
            return None
        user.passwd = '******'              # 使用星号*来屏蔽类明文密码
        return user                         # cookie身份验证正确，返回user
    except Exception as e:
        logging.exception(e)
        return None


# --------------------------------------------------------------------------------------------
def get_input(infos=None):
    info_list = ['name', 'email', 'password'] if infos is None else list(infos)     # infos -> tuple
    result = []
    for info in info_list:
        while True:
            input_info = input("admin's %s: " % info).strip()
            if not input_info:
                print('invalid %s.' % info)
                continue
            if info == 'email' and not _RE_EMAIL.match(input_info):
                print('invalid email.')
                continue
            result.append(input_info)
            break
    return tuple(result)


async def check_admin_user():
    logging.info('check the default admin user...')
    users = await User.findall('admin=?', [True])  # 检查登录用户是否存在，使用邮箱来查找
    return False if len(users) == 0 else True


async def init_admin_user():
    flag = await check_admin_user()
    if flag is True:
        return
    logging.info('create admin user...')
    print('\n------------------------------------')
    name, email, password = get_input()
    print('------------------------------------\n')
    await create_admin_user(name, email, password)


# create a admin user
async def create_admin_user(name, email, password):
    password_str = '%s:%s' % (email, password)      # email: password
    sha1 = hashlib.sha1()
    sha1.update(password_str.encode('utf-8'))
    password = sha1.hexdigest()

    uid = next_id()
    passwd_sha1 = make_passwd_sha1(uid, password)
    email_md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
    image_str = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % email_md5
    user = User(id=uid, name=name.strip(), email=email, passwd=passwd_sha1, image=image_str, admin=True)
    await user.save()
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

