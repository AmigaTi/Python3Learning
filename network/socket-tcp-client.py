#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入socket库
import socket


# 创建一个socket
# socket.AF_INET  - IPv4
# socket.AF_INET6 - IPv6
# SOCK_STREAM     - 指定使用TCP协议
# SOCK_DGRAM      - 指定使用UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 建立与服务端的连接
host = 'www.sina.com.cn'
port = 80
s.connect((host, port))     # address pair


# 发送HTTP头部请求数据
# \r\n          头部配置行分隔符(head)
# \r\n\r\n      头部和内容配置行分隔符(head & body)
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


# 接收数据
buffer = []                 # 使用列表数据类型来接收每隔1024字节数据
while True:
    d = s.recv(1024)        # 每次最多接收1k字节
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)     # 将列表内的所有数据拼接成完整的字节串


# 关闭Socket连接
s.close()


# 分离接收到的数据：HTTP头和网页内容
header, html = data.split(b'\r\n\r\n', 1)

# 打印接收到的HTTP头部内容
print(header.decode('utf-8'))


# 把接收的网页内容写入文件
with open('sina.html', 'wb') as f:
    f.write(html)


'''
HTTP/1.1 200 OK
Server: nginx
Date: Sun, 28 Aug 2016 16:32:21 GMT
Content-Type: text/html
Last-Modified: Sun, 28 Aug 2016 16:31:40 GMT
Vary: Accept-Encoding
Expires: Sun, 28 Aug 2016 16:33:21 GMT
Cache-Control: max-age=60
X-Powered-By: shci_v1.03
Age: 57
Content-Length: 589078
X-Cache: HIT from ctc.gz.1cf2.43.spool.sina.com.cn
Connection: close
'''