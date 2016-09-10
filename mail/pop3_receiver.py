#!/usr/bin/python
# -*- coding: utf-8 -*-

import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr


# 收邮件步骤
# 1. 用`poplib`把邮件的原始文本下载到本地
# 2. 用`mail`解析原始文本，还原为邮箱对象


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，
# 所以解析出来的会有多个元素。


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
# Content-Type: text/plain; charset=GBK
def guess_charset(_msg):
    charset = _msg.get_charset()
    if charset is None:
        content_type = _msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 递归打印出Message对象的层次结构
# indent用于缩进显示
def print_info(msg, indent=0):
    print('start to print info...')
    if indent == 0:     # 只打印一次邮件头部信息
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:   # From / To
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)          #
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))

    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s-------------------' % ('  ' * indent))
            print_info(part, indent + 2)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)        #
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
    print('end to print info...')

# 通过POP3下载邮件


# 测试数据
email = 'linuxfor@sina.com'
password = 'linuxfor@8'
pop3_server = 'pop.sina.com'


# 输入邮件地址，口令和POP3服务器地址
# mail = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server: ')


# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 可选：打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))


# 身份认证
server.user(email)
server.pass_(password)


# stat() 返回邮件数量和占用空间
print('Messages: %s. Size: %s' % server.stat())     # Messages: 4. Size: 12983


# list()返回所有邮件的编号
resp, mails, octets = server.list()


# 可以查看返回的列表
print(mails)                    # [b'1 3493', b'2 3528', b'3 3530', b'4 2432']


# 获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp2, lines, octets2 = server.retr(index)


# lines存储了邮件的原始文本的每一行
# 可以获取整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')


# print('msg_content: \n%s' % msg_content)        # HelloMe.eml 可以在邮箱客户端中下载
# 将邮件内容解析为Message对象 (MIMEMultipart对象)
msg = Parser().parsestr(msg_content)


# print('---> msg: ', msg)
# 解析邮件各部分内容并以正确的格式打印出邮件内容信息
print_info(msg)


# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()

'''
+OK pop3 proxy server ready
*cmd* 'USER linuxfor@sina.com'
*cmd* 'PASS linuxfor@8'
*cmd* 'STAT'
*stat* [b'+OK', b'4', b'12983']
Messages: 4. Size: 12983
*cmd* 'LIST'
[b'1 3493', b'2 3528', b'3 3530', b'4 2432']
*cmd* 'RETR 4'
start to print info...
From: me <linuxfor@163.com>
To:  <linuxfor@sina.com>
Subject: HelloMe
part 0
-------------------
start to print info...
    Text: Hello world and hello me!
end to print info...
part 1
-------------------
start to print info...
    Text: <div style="line-height:1.7;color:#000000;font-size:14px;font-family:Arial"><b>Hello world and hello me!</b></div><br><br><span title="neteasefooter"><p>&nbsp;</p></span>
end to print info...
end to print info...
*cmd* 'QUIT'
'''




