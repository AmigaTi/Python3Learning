#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request           # Accessing Request Data
from flask import render_template   # Rendering Templates


# 表单数据与数据库数据对比验证，数据库中的密码是经过md5加密的
# web/web-wsgi-flask-jinja2.py
# database/db-sqlalchemy-app.py
# builtins/bins-hash/bins-hashlib-md52salt.py


# Flask通过render_template()函数来实现模板的渲染。
# 渲染的HTML模板文件放在同级目录的templates子目录下
# web-wsgi-flask-jinja2.py
# templates
#       |
#       + signin-ok.html
#       + home.html
#       + form.html
#       + page_not_found.html


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin@53':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Wrong username or password')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()

'''
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [31/Aug/2016 18:00:57] "GET /signin HTTP/1.1" 200 -
127.0.0.1 - - [31/Aug/2016 18:01:03] "POST /signin HTTP/1.1" 200 -
'''