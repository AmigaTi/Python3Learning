#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate


# Python对SMTP支持有smtplib和email两个模块：
# email   - 负责构造邮件
# smtplib - 负责发送邮件


# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage


def prompt(_prompt):
    return input(_prompt).strip()


# return: Alias_name <xxxx@example.com>
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 测试数据
# from_addr = 'linuxfor@sina.com'
# password = 'linuxfor@8'
# to_addrs = 'linuxfor@163.com linuxfor@live.com'.split()
# smtp_server = 'smtp.sina.com'


from_addr = prompt('From: ')                # 用户的邮件地址
password = prompt('Password: ')             # 用户的邮件密码
to_addrs = prompt('To: ').split()           # 收件人邮件地址
smtp_server = prompt('SMTP server: ')       # 用户的SMTP服务器地址


# 纯文本邮件
# MIMEText(邮件正文，MIME类型，编码格式)
# plain - 纯文本，完整的MIME为text/plain
# msg = MIMEText('Python is an easy to learn, powerful programming language.', 'plain', 'utf-8')

# HTML邮件
# html = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a></p></body><html>'
# msg = MIMEText(html, 'html', 'utf-8')


# 带附件邮件MIMEMultipart
# alternative - 同时支持html和plain格式
msg = MIMEMultipart('alternative')


# 邮件的 HTML 文本中一般邮件服务商添加外链是无效的
# 邮件正文中显示图片，同时附件的图片将不再显示
plain = 'Hello world and hello me!'
msg.attach(MIMEText(plain, 'plain', 'utf-8'))       # 将纯文本添加到MIMEMultipart

html = '<html><body><h1>The hope always exists if you believe.</h1><p><img src="cid:0"></p></body></html>'
msg.attach(MIMEText(html, 'html', 'utf-8'))         # 将HTML添加到MIMEMultipart


# 添加附件：即关联一个MIMEBase，图片为本地读取
with open('./files/hope.jpg', 'rb') as f:
    # 设置附件中的MIME和文件名
    mime = MIMEBase('image', 'jpeg', filename='hope.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='hope.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 将附件添加到MIMEMultipart
    msg.attach(mime)


# 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
# From:     邮件发送者地址
# To:       邮件发送地址
# Subject:  主题
msg['From'] = _format_addr('linuxforshine<%s>' % from_addr)
msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr) for to_addr in to_addrs])
msg['Subject'] = Header('Getting started with Python', 'utf-8').encode()
msg['Date'] = formatdate()


# 标准的25端口连接SMTP服务器时，使用明文传输，发送邮件的整个过程可能会被窃听。
# 更安全地发送邮件，需加密SMTP会话，即先创建SSL安全连接，再使用SMTP协议发送邮件。
smtp_port = 25                                  # smtp.gmail.com:587
server = smtplib.SMTP(smtp_server, smtp_port)   # 创建SMTP实例，默认端口是25
# server.starttls()                               # 创建安全连接
server.set_debuglevel(1)                        # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)               # 用来登录SMTP服务器


# to_addrs - 发送地址，传入一个list可以一次发送给多个人
# 邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, to_addrs, msg.as_string())   # 发邮件
server.quit()                                   # 终止SMTP会话以及关闭连接


'''
Received: from smtp-2-31.mail.sina.com.cn (unknown [219.142.78.34])
	by mx29 (Coremail) with SMTP id T8CowEBJ7GG3QsRX3kAhBw--.1333S2;
	Mon, 29 Aug 2016 22:12:07 +0800 (CST)
Received: from unknown (HELO [192.168.1.100])([14.155.114.189])
	by sina.com with ESMTP
	29 Aug 2016 22:12:06 +0800 (CST)
X-Sender: linuxfor@sina.com
X-Auth-ID: linuxfor@sina.com
X-SMAIL-MID: 702350394492
Content-Type: multipart/mixed; boundary="===============0421119857=="
MIME-Version: 1.0
From: =?utf-8?q?linuxforshine?= <linuxfor@sina.com>
To: =?utf-8?q?Python_lovers?= <linuxfor@163.com>
Subject: =?utf-8?q?Getting_started_with_Python?=
X-CM-TRANSID:T8CowEBJ7GG3QsRX3kAhBw--.1333S2
Message-Id:<57C442B7.7C2CB3.14483@m12-79.163.com>
Authentication-Results: mx29; spf=pass smtp.mail=linuxfor@sina.com;
X-Coremail-Antispam: 1Uf129KBjDUn29KB7ZKAUJUUUUU529EdanIXcx71UUUUU7v73
	VFW2AGmfu7bjvjm3AaLaJ3UbIYCTnIWIevJa73UjIFyTuYvjxU3K0PDUUUU
Date: Mon, 29 Aug 2016 22:12:07 +0800 (CST)


--===============0421119857==
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

c2VuZCB3aXRoIGZpbGUuLi4=

--===============0421119857==
Content-Type: image/png; filename="hope.jpg"
MIME-Version: 1.0
Content-Disposition: attachment; filename="hope.jpg"
Content-ID: <0>
X-Attachment-Id: 0
Content-Transfer-Encoding: base64
'''



