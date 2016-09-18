#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from webapp.www.orm import Model
from webapp.www.fields import BooleanField
from webapp.www.fields import StringField
from webapp.www.fields import FloatField
from webapp.www.fields import TextField
from webapp.www import ghelper


# 在编写ORM时，给一个Field增加一个default参数可以让ORM自己填入缺省值，非常方便。
# 并且，缺省值可以作为函数对象传入，在调用save()时自动计算。


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=ghelper.get_unique_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()                      # admin if True
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=ghelper.get_created_time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=ghelper.get_unique_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=ghelper.get_created_time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=ghelper.get_unique_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=ghelper.get_created_time)

