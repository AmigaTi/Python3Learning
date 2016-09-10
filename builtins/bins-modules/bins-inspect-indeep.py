#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect


# a == POSITIONAL_OR_KEYWORD        # a是用位置或参数名都可赋值的
# b == VAR_POSITIONAL               # b是可变长列表
# c == KEYWORD_ONLY                 # c只能通过参数名的方式赋值
# d == VAR_KEYWORD                  # d是可变长字典


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    print('params: ', params)
    found = False
    for name, param in params.items():
        print('%s => %s (%s)' % (name, param, param.kind))
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL
                      and param.kind != inspect.Parameter.KEYWORD_ONLY
                      and param.kind != inspect.Parameter.VAR_KEYWORD):
            print('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
            return
    print('anything all right!')
    return found


# request => request (POSITIONAL_OR_KEYWORD)
# a => a (POSITIONAL_OR_KEYWORD)
def foo(request, a): pass                   # 这种是会报错


# a => a (POSITIONAL_OR_KEYWORD)
# request => request (POSITIONAL_OR_KEYWORD)
# b => *b (VAR_POSITIONAL)
def foo2(a, request, *b): pass              # 这种不报错


# a => a (POSITIONAL_OR_KEYWORD)
# b => *b (VAR_POSITIONAL)
# request => request (KEYWORD_ONLY)
def foo3(a, *b, request): pass              # 这种也不报错


# a => a (POSITIONAL_OR_KEYWORD)
# b => *b (VAR_POSITIONAL)
# request => request (KEYWORD_ONLY)
# c => c (KEYWORD_ONLY)
def foo4(a, *b, request, c): pass           # 这种还是不报错


# a => a (POSITIONAL_OR_KEYWORD)
# b => *b (VAR_POSITIONAL)
# c => c (KEYWORD_ONLY)
# request => request (KEYWORD_ONLY)
# d => **d (VAR_KEYWORD)
def foo5(a, *b, c, request, **d): pass      # 这种还是不报错


# request => *request (VAR_POSITIONAL)
def foo6(*request): pass                    # 这种还是不报错


# request => **request (VAR_KEYWORD)
def foo7(**request): pass                   # 这种还是不报错


# def foo8(a, *b, c, **d, request): pass        # 这种系统会报错，VAR_KEYWORD只能是最后一个参数


funcs = [foo, foo2, foo3, foo4, foo5, foo6, foo7]


for func in funcs:
    print('%s%s: ' % (func.__name__, str(inspect.signature(func))), end=' ')
    has_request_arg(func)


'''
foo(request, a):  params:  OrderedDict([('request', <Parameter "request">), ('a', <Parameter "a">)])
request => request (POSITIONAL_OR_KEYWORD)
a => a (POSITIONAL_OR_KEYWORD)
request parameter must be the last named parameter in function: foo(request, a)
foo2(a, request, *b):  params:  OrderedDict([('a', <Parameter "a">), ('request', <Parameter "request">), ('b', <Parameter "*b">)])
a => a (POSITIONAL_OR_KEYWORD)
request => request (POSITIONAL_OR_KEYWORD)
b => *b (VAR_POSITIONAL)
anything all right!
foo3(a, *b, request):  params:  OrderedDict([('a', <Parameter "a">), ('b', <Parameter "*b">), ('request', <Parameter "request">)])
a => a (POSITIONAL_OR_KEYWORD)
b => *b (VAR_POSITIONAL)
request => request (KEYWORD_ONLY)
anything all right!
foo4(a, *b, request, c):  params:  OrderedDict([('a', <Parameter "a">), ('b', <Parameter "*b">), ('request', <Parameter "request">), ('c', <Parameter "c">)])
a => a (POSITIONAL_OR_KEYWORD)
b => *b (VAR_POSITIONAL)
request => request (KEYWORD_ONLY)
c => c (KEYWORD_ONLY)
anything all right!
foo5(a, *b, c, request, **d):  params:  OrderedDict([('a', <Parameter "a">), ('b', <Parameter "*b">), ('c', <Parameter "c">), ('request', <Parameter "request">), ('d', <Parameter "**d">)])
a => a (POSITIONAL_OR_KEYWORD)
b => *b (VAR_POSITIONAL)
c => c (KEYWORD_ONLY)
request => request (KEYWORD_ONLY)
d => **d (VAR_KEYWORD)
anything all right!
foo6(*request):  params:  OrderedDict([('request', <Parameter "*request">)])
request => *request (VAR_POSITIONAL)
anything all right!
foo7(**request):  params:  OrderedDict([('request', <Parameter "**request">)])
request => **request (VAR_KEYWORD)
anything all right!
'''























