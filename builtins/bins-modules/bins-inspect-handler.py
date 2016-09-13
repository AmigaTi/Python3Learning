#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect


# REST API
# URL                                       http://localhost:9000
#
# router                           POST     handler
# @get('/test')                             test()
# @get('/')                                 index(request)
# @get('/api/users')                        api_get_users()
# @get('/signin')                           signin()
# @post('/api/authenticate')        *       authenticate(*, email, passwd)
# @get('/signout')                          signout(request)
# @get('/register')                         register()
# @post('/api/users')               *       api_register_user(*, email, name, passwd)
# @get('/manage/blogs')                     manage_blogs(*, page='1')
# @get('/manage/blogs/create')              manage_create_blog()
# @get('/api/blogs')                        api_blogs(*, page='1')
# @get('/api/blogs/{id}')                   api_get_blog(*, id)
# @post('/api/blogs')               *       api_create_blog(request, *, name, summary, content)


# a == POSITIONAL_OR_KEYWORD        # a是用位置或参数名都可赋值的arg
# b == VAR_POSITIONAL               # b是可变长列表*args
# c == KEYWORD_ONLY                 # c只能通过参数名的方式赋值*
# d == VAR_KEYWORD                  # d是可变长字典**kw


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters   #
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY \
                and param.default == inspect.Parameter.empty:
            args.append(name)
    print('get_required_kw_args(): ', args)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    # inspect.signature(callable, *, follow_wrapped=True)
    # Return a Signature object for the given callable
    sig = inspect.signature(fn)         # inspect.Signature object
    params = sig.parameters             # inspect.Parameter object
    # print('params: ', params)
    found = False
    for name, param in params.items():
        print('%s => %s (%s)' % (name, param, param.kind))
        # print('param.default =', param.default.__name__)
        print('param.default == inspect.Parameter.empty: ', param.default == inspect.Parameter.empty)
        print('----' * 12)
        if name == 'request':
            found = True
            continue
        # 如果找到request参数的话，后面还有POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD)这两类参数就报错，否则是不会报错的！
        # if found and (param.kind not in (VAR_POSITIONAL, KEYWORD_ONLY, VAR_KEYWORD))
        # if found and (param.kind in (POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD))
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL
                      and param.kind != inspect.Parameter.KEYWORD_ONLY
                      and param.kind != inspect.Parameter.VAR_KEYWORD):
            print('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
            return
    # print('anything all right!')
    return found


def test():
    pass


# request => request (POSITIONAL_OR_KEYWORD)
def index(request):
    pass


def api_get_users():
    pass


def signin():
    pass


# POST
# email => email (KEYWORD_ONLY)
# passwd => passwd (KEYWORD_ONLY)
def authenticate(*, email, passwd):
    pass


# request => request (POSITIONAL_OR_KEYWORD)
def signout(request):
    pass


def register():
    pass


# POST
# email => email (KEYWORD_ONLY)
# name => name (KEYWORD_ONLY)
# passwd => passwd (KEYWORD_ONLY)
def api_register_user(*, email, name, passwd):
    pass


# page => page='1' (KEYWORD_ONLY)
def manage_blogs(*, page='1'):
    pass


def manage_create_blog():
    pass


# page => page='1' (KEYWORD_ONLY)
def api_blogs(*, page='1'):
    pass


# id => id (KEYWORD_ONLY)
def api_get_blog(*, id):
    pass


# POST
# request => request (POSITIONAL_OR_KEYWORD)
# name => name (KEYWORD_ONLY)
# summary => summary (KEYWORD_ONLY)
# content => content (KEYWORD_ONLY)
def api_create_blog(request, *, name, summary, content):
    pass


# testing -------------------------------------------------

funcs = [
    test,
    index,
    api_get_users,
    signin,
    authenticate,
    signout,
    register,
    api_register_user,
    manage_blogs,
    manage_create_blog,
    api_blogs,
    api_get_blog,
    api_create_blog
]


print('====' * 15)
for func in funcs:
    print('>> %s%s: ' % (func.__name__, str(inspect.signature(func))), end=' ')
    print()         # 输出一个换行
    has_request_arg(func)
    get_required_kw_args(func)
    print('====' * 15)


'''
============================================================
>> test():
get_required_kw_args():  []
============================================================
>> index(request):
request => request (POSITIONAL_OR_KEYWORD)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  []
============================================================
>> api_get_users():
get_required_kw_args():  []
============================================================
>> signin():
get_required_kw_args():  []
============================================================
>> authenticate(*, email, passwd):
email => email (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
passwd => passwd (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  ['email', 'passwd']
============================================================
>> signout(request):
request => request (POSITIONAL_OR_KEYWORD)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  []
============================================================
>> register():
get_required_kw_args():  []
============================================================
>> api_register_user(*, email, name, passwd):
email => email (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
name => name (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
passwd => passwd (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  ['email', 'name', 'passwd']
============================================================
>> manage_blogs(*, page='1'):
page => page='1' (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  False
------------------------------------------------
get_required_kw_args():  []
============================================================
>> manage_create_blog():
get_required_kw_args():  []
============================================================
>> api_blogs(*, page='1'):
page => page='1' (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  False
------------------------------------------------
get_required_kw_args():  []
============================================================
>> api_get_blog(*, id):
id => id (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  ['id']
============================================================
>> api_create_blog(request, *, name, summary, content):
request => request (POSITIONAL_OR_KEYWORD)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
name => name (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
summary => summary (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
content => content (KEYWORD_ONLY)
param.default == inspect.Parameter.empty:  True
------------------------------------------------
get_required_kw_args():  ['name', 'summary', 'content']
============================================================
'''