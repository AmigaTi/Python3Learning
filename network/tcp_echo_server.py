#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import time


# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 绑定监听的地址和端口
s.bind(('127.0.0.1', 9898))


# 调用listen()方法开始监听端口，并指定等待连接的最大数量
s.listen(5)
print('Waiting for connecting...')


# 每个连接都必须创建新线程（或进程）来处理，
# 否则单线程在处理连接的过程中，无法接受其他客户端的连接
def do_response(in_sock, in_addr):
    print('Accept new connection from %s:%s...' % in_addr)
    in_sock.send(b'Welcome to Alpha Server!')
    while True:
        data = in_sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        in_sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    in_sock.close()
    print('Connection from %s:%s closed.' % in_addr)


# 服务器程序通过一个永久循环来接受来自客户端的连接，
# accept()会等待并返回一个客户端的连接，
# 服务器程序会永远运行下去，必须按Ctrl+C退出程序
while True:
    sock, addr = s.accept()      # 接收一个新连接
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=do_response, args=(sock, addr))
    t.start()                   # 启动子线程


'''
Waiting for connecting...
Accept new connection from 127.0.0.1:17703...
Connection from 127.0.0.1:17703 closed.
'''

