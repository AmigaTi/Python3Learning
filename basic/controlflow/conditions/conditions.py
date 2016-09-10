#!/usr/bin/python
# -*- coding: utf-8 -*-

from HelloMe import hello
from HelloMe.me import Me

apple, boy, cat = '', 'boy', 'cat'
non_null = apple or boy or cat
print(non_null)     # boy

hello = hello.Hello()
hello.hello()       # say hello...

me = Me()
me.me()             # is real me...
