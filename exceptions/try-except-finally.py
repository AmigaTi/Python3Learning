#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# try机制
# 当我们认为某段代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后序代码不会继续执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块。
# 而不管有没有错误发生，如果有finally语句，则一定会被执行。

# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系参考：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


try:
    print('try...')
    r = 10 / 0
    print('result: ', r)
except ZeroDivisionError as e:
    print('except: ', e)
finally:
    print('finally...')
print('end')

'''
try...
except:  division by zero
finally...
end
'''


# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
# 出错并不可怕，可怕的是不知道哪里出错了。
# 解读错误信息是定位错误的关键。
# 从上往下可以看到整个错误的调用函数链
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()

'''
Traceback (most recent call last):
try...
  File "D:/workspace/PycharmProjects/Basics/exceptions/try-except-finally.py", line 50, in <module>
except:  division by zero
    main()
finally...
  File "D:/workspace/PycharmProjects/Basics/exceptions/try-except-finally.py", line 47, in main
end
    bar('0')
  File "D:/workspace/PycharmProjects/Basics/exceptions/try-except-finally.py", line 43, in bar
    return foo(s) * 2
  File "D:/workspace/PycharmProjects/Basics/exceptions/try-except-finally.py", line 39, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
'''