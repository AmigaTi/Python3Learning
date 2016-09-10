#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入socket库
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9797))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()


'''
Hello, Michael!
Hello, Tracy!
Hello, Sarah!
'''