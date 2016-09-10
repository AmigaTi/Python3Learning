#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import re


# 创建一个套接字socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 建立与服务端的连接
sock.connect(('127.0.0.1', 9898))


# 接收服务器发来的欢迎消息
welcome = sock.recv(1204).decode('utf-8')
print(welcome)


# for data in [b'Michael', b'Tracy', b'Sarah']:
#     s.send(data)        # 发送数据
#     print(s.recv(1024).decode('utf-8'))
while True:
    name = input('Enter your name (or exit): ').strip()
    m = re.match(r'^([a-zA-Z][a-zA-Z0-9]{5,12})', name)     # c919/hellome
    if m is None:
        print('Please enter the right name again!')
        continue
    sock.send(name.encode('utf-8'))  # str -> bytes
    if name == 'exit':
        print('Client exited directly')
        break
    recv = sock.recv(1024).decode('utf-8')  # bytes -> str
    print(recv)


sock.close()


'''
Welcome to Alpha Server!
Enter your name (or exit): linuxfor
Hello, linuxfor!
Enter your name (or exit): c919
Hello, c919!
Enter your name (or exit): exit
Client exited directly
'''