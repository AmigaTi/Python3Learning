#!/usr/bin/python
# -*- coding: utf-8 -*-

# ===========================================
# Description: 下载汉化组的海贼王在线漫画
# Author: linuxfor/shellever
# Email: linuxfor@163.com/shellever@163.com
# ===========================================

from html.parser import HTMLParser
from urllib import request
import json
import re
import os

# 1. 在线漫画列表
# http://hanhuazu.cc/cartoon
# 1.1 在线漫画列表索引 => 通过查找关键词"海贼王"来确定其id
# http://hhzapi.ishuhui.com/cartoon/book_list/category/1/ver/48280389.json
# 2. 海贼王 => 通过指定id来查找海贼王的更新列表得到最新的一话number
# https://hanhuazu.cc/cartoon/book?id=1
# 3. 海贼王更新说明 => 得到最新一话的number，即第number话
# https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
# 4. 海贼王会话索引列表 => 通过得到的number来索引得到最新的一话的id
# 5. https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
# 6. 海贼王会话图片索引列表 => 通过最新一话的id来得到该最新一话的图片列表url
# https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
# 7. 海贼王会话图片内容 => 通过图片列表url来得到最终的最新一话的全部图片内容
# https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/12.png


class OnePieceHTMLParser(HTMLParser):

    def __init__(self):
        super(OnePieceHTMLParser, self).__init__()
        self.__cartoon_url = 'https://hanhuazu.cc/cartoon'
        self.__pic_url = 'https://pic02.ishuhui.com'
        self.__json_url = 'https://hhzapi.ishuhui.com/cartoon'
        self.__book_id = 1          # One_Piece_Book_Id_default = 1 or other specified value
        self.__posts_list = []      # 数据缓存
        self.__imgs_dict = {}       # 图片地址URL缓存，可使用多线程下载
        self.__next_post_info = {'next_post': -1, 'next_post_day': 'xxxx-xx-xx'}
        self.__post_dict_newest = {'id': -1, 'title': 'xxx', 'number': -1}
        self.__ver = {'c_post': '12345678', 'c_conf': '87654321'}
        self.__base_index = {'en_us': 'onepiece', 'zh_cn': '海贼王', 'zh_hk': '海賊王'}
        self.__is_debug = True      # 是否开启全部的调试信息打印

    def error(self, message):
        pass

    def get_ver(self):
        return self.__ver

    def logd(self, info):
        if self.__is_debug is True:
            print(info)

    @staticmethod                                       # 静态方法，因为没有用到self参数
    def do_request(url, raw=False):                   # 发送请求，返回字节流或字符流(默认)
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as response:
            print('Status: ', response.status, response.reason)
            if raw is True:
                return response.read()                  # 图片等字节流，不能加utf-8解码
            return response.read().decode('utf-8')      # json等字符流，需要加utf-8解码

    def get_json(self, url):
        json_str = self.do_request(url)                  # 发送请求，返回json字符串
        return json.loads(json_str)                     # 将json字符串转换成Python中的dict

    def get_html_data(self):                  # book_url
        url = self.__cartoon_url
        print('Request: %s' % url)              # http://hanhuazu.cc/cartoon
        return self.do_request(url)            # 发送请求

    def make_dir(self):
        dir_name = '%d - %s' % (self.__post_dict_newest['number'], self.__post_dict_newest['title'])
        directory = os.path.join('.', dir_name)
        if not os.path.exists(directory):       # 不存在才创建，避免出错
            os.mkdir(directory)
        return directory

    def get_cartoon_id(self):         # book_list_url
        url = '%s/book_list/category/1/ver/%s.json' % (self.__json_url, self.__ver['c_post'])
        print('Request: %s' % url)      # http://hhzapi.ishuhui.com/cartoon/book_list/category/1/ver/48280389.json
        cartoon = self.get_json(url)            #
        books_list = cartoon['data']
        for book in books_list:
            if book['name'] == self.__base_index['zh_hk']:
                self.__book_id = book['id']
                self.logd('book_id: %d' % self.__book_id)
                break                   # 找到就直接退出

    def get_update_json(self):        # update_json_url
        url = '%s/update_list/ver/%s.json' % (self.__json_url, self.__ver['c_post'])
        print('Request: %s' % url)      # https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
        update = self.get_json(url)
        next_posts_list = update['data']
        for next_post in next_posts_list:
            if next_post['id'] == self.__book_id:
                self.__next_post_info = {key: next_post[key] for key in self.__next_post_info.keys()}
                self.logd('next_post_info: %s' % str(self.__next_post_info))

    def get_book_json(self):          # book_json_url
        url = '%s/book/id/%d/ver/%s.json' % (self.__json_url, self.__book_id, self.__ver['c_post'])
        print('Request: %s' % url)      # https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
        book = self.get_json(url)
        self.__posts_list = book['data']['cartoon']['1']['posts']  # array
        for post in self.__posts_list:
            if post['number'] == self.__next_post_info['next_post'] - 1:      # get the newest post
                self.__post_dict_newest = post                                # dict -> dict
                self.logd('post_dict_newest: %s' % str(self.__post_dict_newest))

    def get_post_json(self):          # post_json_url
        url = '%s/post/id/%d/ver/%s.json' % (self.__json_url, self.__post_dict_newest['id'], self.__ver['c_post'])
        print('Request: %s' % url)      # https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
        post = self.get_json(url)
        content_img = post['data']['content_img']
        self.__imgs_dict = json.loads(content_img)
        for k, v in self.__imgs_dict.items():
            png_url = re.match(r'^/upload/(.+)', v).group(1)    # /upload/cartoon/book-1/1/838-5551/12.png
            self.__imgs_dict[k] = '%s/%s' % (self.__pic_url, png_url)
            self.logd('%-9s => %s' % (k, self.__imgs_dict[k]))      # 格式化打印显示

    def get_images(self):                       # 可以缓存图片url，来减少http/GET请求次数，可以启动多线程
        directory = self.make_dir()               # 创建最新一话的目录
        print('Start to request picture...')
        for k, v in self.__imgs_dict.items():
            print('Request: %s' % v)
            img = self.do_request(v, True)
            file = os.path.join(directory, k)
            with open(file, 'wb') as f:          # mode = 'wb'
                f.write(img)                      # 将图片保存到本地

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)                       # list -> dict
        if tag == 'meta' and 'name' in attrs:    # 判断标签是否为meta，并且attrs字典中是否存在name键值
            if attrs['name'] == 'ver':
                content = json.loads(attrs['content'])
                self.__ver = {key: content[key] for key in self.__ver.keys()}   # 用部分的content来初始化__ver字典
                self.logd('ver: %s' % str(self.__ver))

    def do_parse(self):
        self.feed(self.get_html_data())
        self.logd('==' * 42)
        self.get_cartoon_id()
        self.logd('==' * 42)
        self.get_update_json()
        self.logd('==' * 42)
        self.get_book_json()
        self.logd('==' * 42)
        self.get_post_json()
        self.logd('==' * 42)
        return self                     # 为了支持链式编程


if __name__ == '__main__':
    # parser = OnePieceHTMLParser()       # 创建解析器实例对象
    # parser.do_parse()                   # 执行解析操作
    # parser.get_images()                 # 下载解析后的图片到本地
    OnePieceHTMLParser().do_parse().get_images()        # 链式编程


# is_debug = False
'''
Request: https://hanhuazu.cc/cartoon
Status:  200 OK
Request: https://hhzapi.ishuhui.com/cartoon/book_list/category/1/ver/48280389.json
Status:  200 OK
Request: https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
Status:  200 OK
Request: https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
Status:  200 OK
Request: https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
Status:  200 OK
Start to request picture...
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/12.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/13.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/08-09.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/03.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/10-11.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/06.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/14.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/01.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/07.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/02.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp1.jpg
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/16-17.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/00.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/15.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/05.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp2.jpg
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/04.png
Status:  200 OK
'''


# # is_debug = True
'''
Request: https://hanhuazu.cc/cartoon
Status:  200 OK
ver: {'c_conf': '54280413', 'c_post': '48280389'}
======================================================================
Request: https://hhzapi.ishuhui.com/cartoon/book_list/category/1/ver/48280389.json
Status:  200 OK
book_id: 1
======================================================================
Request: https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
Status:  200 OK
next_post_info: {'next_post': 839, 'next_post_day': '2016-09-15'}
======================================================================
Request: https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
Status:  200 OK
post_dict_newest: {'id': 5551, 'number': 838, 'title': '喬老大'}
======================================================================
Request: https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
Status:  200 OK
00.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/00.png
10-11.png => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/10-11.png
02.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/02.png
sp1.jpg   => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp1.jpg
15.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/15.png
04.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/04.png
16-17.png => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/16-17.png
01.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/01.png
06.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/06.png
08-09.png => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/08-09.png
14.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/14.png
13.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/13.png
12.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/12.png
05.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/05.png
07.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/07.png
sp2.jpg   => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp2.jpg
03.png    => https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/03.png
======================================================================
Start to request picture...
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/00.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/10-11.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/02.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp1.jpg
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/15.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/04.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/16-17.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/01.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/06.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/08-09.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/14.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/13.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/12.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/05.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/07.png
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/sp2.jpg
Status:  200 OK
Request: https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/03.png
Status:  200 OK
'''