#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request


# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
# Flask自带的Server在端口5000上监听
# 首页地址 http://localhost:5000/
# 登录表单 http://localhost:5000/signin


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home Page using Flask microframework</h1>'


@app.route('/signin', methods=['GET'])      # 显示登录表单时执行
def signin_form():
    return '''<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
                </form>'''


@app.route('/signin', methods=['POST'])     # 提交表单信息时执行
def signin():
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'admin@53':
        return '<h3>Hello, admin!</h3>' \
               '<h2><a href="http://localhost:5000/">go home</a></h2>'
    return '<h3>Wrong username or password.</h3>'


if __name__ == '__main__':
    app.run()

'''
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [31/Aug/2016 16:49:33] "GET /signin HTTP/1.1" 200 -
127.0.0.1 - - [31/Aug/2016 16:49:42] "POST /signin HTTP/1.1" 200 -
'''























