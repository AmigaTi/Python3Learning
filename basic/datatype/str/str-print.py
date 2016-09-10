#!/usr/bin/python           # Linux/OS X系统中Python为可执行程序，Windows中忽略
# -*- coding: utf-8 -*-     # Python解释器以utf-8编码格式读取源代码文件


print('hello world and hello me!')

print('it doesn\'t matter.')

print('First line.\nSecond line.')

print(r'First line.\nSecond line.')     # First line.\nSecond line.

# 需要加反斜杠，不然后输出\n换行
print("""\
Usage: thingy [OPTIONS]
    -h              Display this usage message
    -H hostname     Hostname to connect to\
""")

print(10 * '=')         # ==========

print('Py' 'thon')      # Python

print('Py' + 'thon')    # Python

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)         # Put several strings within parentheses to have them joined together.


# s[:i] + s[i:] = s
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

word = 'Python'
print(word[0])      # P
print(word[5])      # n
print(word[-1])     # n
print(word[0:2])    # Py
print(word[:2])     # Py
print(word[2:])     # thon
print(word[-2:])    # on
print(word[:])      # Python

print(word[:2] + word[2:])  # Python

print(len(word))    # 6


if 'h' in word:
    print('\'h\' is in word \'Python\'')
else:
    print('\'h\' is not in word \'Python\'')
# 'h' is in word 'Python'


if 'q' not in word:
    print('\'q\' is not in word \'Python\'')
else:
    print('\'q\' is in word \'Python\'')
# 'q' is not in word 'Python'


