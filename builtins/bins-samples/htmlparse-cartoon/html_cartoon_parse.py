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
        self.__cartoon_url = 'http://hanhuazu.cc/cartoon'
        self.__book_url = 'https://hanhuazu.cc/cartoon/book'
        self.__pic_url = 'https://pic02.ishuhui.com'
        self.__cartoon_json_url = 'http://hhzapi.ishuhui.com/cartoon'
        self.__update_json_url = 'https://hhzapi.ishuhui.com/cartoon/update_list'
        self.__book_json_url = 'https://hhzapi.ishuhui.com/cartoon/book/id'
        self.__post_json_url = 'https://hhzapi.ishuhui.com/cartoon/post/id'
        self.__next_post = 0
        self.__next_post_day = ''
        self.__book_id = 1      # One_Piece_Book_Id_default = 1 or other specified value
        self.__post_number = 0
        self.__post_id = 0
        self.__post_title = ''
        self.__post_dict = {'id': -1, 'title': 'xxx', 'number': -1}
        self.__posts_list = []  # 数据缓存
        self.__imgs_dict = {}   # 数据缓存
        self.__html_data = ''
        self.__tag = ''
        self.__attrs = {}
        self.__c_post = ''
        self.__c_conf = ''
        self.__base_index = {'en_us': 'onepiece', 'zh_cn': '海贼王', 'zh_hk': '海賊王', 'zh_tw': '海賊王'}

    def error(self, message):
        pass

    # 可以实现间隔更新数据，以减少查询次数，但数据会不时的更改，所以间隔时间需要考虑
    # 否则请求的json数据地址将会出错
    def get_html_data(self):
        # url = '%s?id=%d' % (self.__book_url, self.__book_id)
        url = self.__cartoon_url
        print('book_url: %s' % url)             # https://hanhuazu.cc/cartoon/book?id=1
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as f:
            self.__html_data = f.read().decode('utf-8')
            return self.__html_data

    # download and store to file
    # Note: MUST specify the encoding
    # @staticmethod
    def write_json_to_file(self, json_str, json_file_name):
        with open(json_file_name, 'w', encoding='utf-8') as f:      # 必须指定编码为utf-8
            f.write(json_str)

    def make_dir(self):
        dir_name = '%d - %s' % (self.__post_number, self.__post_title)
        directory = os.path.join('.', dir_name)
        if not os.path.exists(directory):       # 不存在才创建，避免出错
            os.mkdir(directory)
        return directory

    # http://hhzapi.ishuhui.com/cartoon/book_list/category/1/ver/48280389.json
    def get_cartoon_id(self):
        url = '%s/book_list/category/1/ver/%s.json' % (self.__cartoon_json_url, self.__c_post)
        print('book_list_url: %s' % url)
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as response:
            print('Status: ', response.status, response.reason)
            cartoon_json = response.read().decode('utf-8')
            print('cartoon_json: \n', cartoon_json)
            cartoon = json.loads(cartoon_json)
            print('cartoon: \n', cartoon)
            # self.write_json_to_file(cartoon_json, 'book_list.json')   # store to file
            books_list = cartoon['data']
            for book in books_list:
                if book['name'] == self.__base_index['zh_hk']:
                    self.__book_id = book['id']
                    print('book_id: %d' % self.__book_id)
                    break

    # https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
    def get_update_json(self):
        url = '%s/ver/%s.json' % (self.__update_json_url, self.__c_post)
        print('update_json_url: %s' % url)      # https://hhzapi.ishuhui.com/cartoon/update_list/ver/48280389.json
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as response:
            print('Status: ', response.status, response.reason)
            update_json = response.read().decode('utf-8')
            print('book_json: \n', update_json)
            update = json.loads(update_json)
            print('book: \n', update)
            next_posts_list = update['data']
            for next_post in next_posts_list:
                if next_post['id'] == self.__book_id:
                    print('next_post: %d' % next_post['next_post'])
                    print('next_post_day: %s' % next_post['next_post_day'])
                    self.__next_post = next_post['next_post']
                    self.__next_post_day = next_post['next_post_day']

    # https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
    def get_book_json(self):
        url = '%s/%d/ver/%s.json' % (self.__book_json_url, self.__book_id, self.__c_post)
        print('book_json_url: %s' % url)    # https://hhzapi.ishuhui.com/cartoon/book/id/1/ver/48280389.json
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as response:
            print('Status: ', response.status, response.reason)
            book_json = response.read().decode('utf-8')
            print('book_json: \n', book_json)
            book = json.loads(book_json)
            print('book: \n', book)
            posts_list = book['data']['cartoon']['1']['posts']  # array
            self.__posts_list = posts_list
            for post in posts_list:
                if post['number'] == self.__next_post - 1:      # get the newest post
                    print('number: %d' % post['number'])
                    print('id: %d' % post['id'])
                    print('title: %s' % post['title'])
                    self.__post_number = post['number']
                    self.__post_id = post['id']
                    self.__post_title = post['title']

    # https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
    def get_post_json(self):
        url = '%s/%d/ver/%s.json' % (self.__post_json_url, self.__post_id, self.__c_post)
        print('post_json_url: %s' % url)    # https://hhzapi.ishuhui.com/cartoon/post/id/5551/ver/48280389.json
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
        with request.urlopen(req) as response:
            print('Status: ', response.status, response.reason)
            post_json = response.read().decode('utf-8')
            print('post_json: \n', post_json)
            post = json.loads(post_json)
            print('post: \n', post)
            content_img = post['data']['content_img']
            imgs_dict = json.loads(content_img)
            self.__imgs_dict = imgs_dict
            print('img_dicts: \n', imgs_dict)
            print('type(img_dicts): ', type(imgs_dict))     # type(img_dicts):  <class 'dict'>
            for k, v in imgs_dict.items():
                print('%s => %s' % (k, v))

    # https://pic02.ishuhui.com/cartoon/book-1/1/838-5551/12.png
    #                   /upload/cartoon/book-1/1/838-5551/12.png
    def get_images(self):                       # 可以缓存图片url，来减少http/GET请求次数
        directory = self.make_dir()               # 创建最新一话的目录
        for k, v in self.__imgs_dict.items():
            png_url = re.match(r'^/upload/(.+)', v).group(1)
            url = '%s/%s' % (self.__pic_url, png_url)
            print('png_url: %s' % url)
            req = request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0')
            with request.urlopen(req) as response:
                print('Status: ', response.status, response.reason)
                img = response.read()
                file = os.path.join(directory, k)
                with open(file, 'wb') as f:        # mode = 'wb'
                    f.write(img)

    def get_c_post(self):
        return self.__c_post

    def get_c_conf(self):
        return self.__c_conf

    def check_attr(self):
        if self.__attrs is not None:
            if 'name' in self.__attrs:      # key
                if self.__attrs['name'] == 'ver':
                    content = json.loads(self.__attrs['content'])
                    self.__c_post = content['c_post']
                    self.__c_conf = content['c_conf']
                    return True
        return False

    def handle_starttag(self, tag, attrs):
        self.__tag = tag
        self.__attrs = dict(attrs)          # list -> dict
        print('<%s %s>' % (tag, str(self.__attrs)))
        if self.__tag == 'meta' and self.check_attr():
            print('c_post: %s' % self.__c_post)
            print('c_conf: %s' % self.__c_conf)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_data(self, data):
        print(data)

    def do_parser(self):
        self.feed(self.get_html_data())
        print('c_post: %s' % self.get_c_post())
        print('c_conf: %s' % self.get_c_conf())
        print('=============================================================')
        self.get_cartoon_id()
        print('=============================================================')
        self.get_update_json()
        print('=============================================================')
        self.get_book_json()
        print('=============================================================')
        self.get_post_json()
        print('=============================================================')


if __name__ == '__main__':
    parser = OnePieceHTMLParser()       # 创建解析器实例对象
    parser.do_parser()                  # 执行解析操作
    parser.get_images()                 # 下载解析后的图片到本地

