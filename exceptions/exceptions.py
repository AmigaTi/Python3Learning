#!/usr/bin/python
# -*- coding: utf-8 -*-


def input_num():
    while True:
        try:
            n = int(input('Please enter a number: '))
            break
        except ValueError:
            print('Oops! That was no valid number. Try again...')

# input_num()


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

divide(2, 1)
print('=' * 20)
divide(2, 0)

'''
result is 2.0
executing finally clause
====================
division by zero!
executing finally clause
'''