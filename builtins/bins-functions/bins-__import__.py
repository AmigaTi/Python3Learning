#!/usr/bin/python
# -*- coding: utf-8 -*-


# __import__(name, globals=None, locals=None, fromlist=(), level=0)

# import sys <=> sys = __import__('sys')
# import spam <=> spam = __import__('spam', globals(), locals(), [], 0)
# import spam.ham <=> spam = __import__('spam.ham', globals(), locals(), [], 0)

# from spam.ham import eggs, sausage as saus
# <=>
# _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
# eggs = _temp.eggs
# saus = _temp.sausage

