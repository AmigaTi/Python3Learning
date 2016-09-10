#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入socket库
import socket


# 创建一个socket
# socket.AF_INET  - IPv4
# SOCK_DGRAM      - 指定使用UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定监听的地址和端口
s.bind(('127.0.0.1', 9797))
print('Bind UDP on 9797...')

# 绑定端口后不需要调用listen()方法，
# 直接接收来自任何客户端的数据

# recvfrom()方法返回数据和客户端的地址与端口，
# 服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
while True:
    data, addr = s.recvfrom(1024)       # 接收数据
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

'''
Bind UDP on 9797...
Received from 127.0.0.1:53307.
Received from 127.0.0.1:53307.
Received from 127.0.0.1:53307.
'''
