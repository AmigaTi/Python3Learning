#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request, parse


# Get
# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应


# # 对豆瓣的一个URL: https://api.douban.com/v2/book/2129650进行抓取，并返回响应
def get_html():
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s ' % (k, v))
        print('Data: ', data.decode('utf-8'))

# get_html()


# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。

# 如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，
# **User-Agent**头就是用来标识浏览器的。

# 例如，模拟iPhone 6去请求豆瓣首页，
# 这样豆瓣会返回适合iPhone的移动版网页
def get_html_req():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        data = f.read().decode('utf-8')
        print('Data: ', data)
        with open('./douban_html_page.html', 'w', encoding='utf-8') as f:
            f.write(data.strip())

# get_html_req()


# Post
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
# 模拟一个微博登录，先读取登录的邮箱和口令，
# 然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
def login_req():
    print('Login to weibo.cn...')
    email = input('Email: ')
    password = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', password),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data: ', f.read().decode('utf-8'))

# login_req()


# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，
# 那么就需要利用ProxyHandler来处理
def proxy():
    proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


# 利用urllib读取XML，将XML一节的数据由硬编码改为由urllib获取
# urllib.error.HTTPError: HTTP Error 401: Unauthorized
# ???需要注册来获取授权key???
def fetch_xml(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    with request.urlopen(req) as response:
        print('Status: ', response.status, response.reason)
        the_page = response.read().decode('utf-8')
        return the_page


# 测试
print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))






