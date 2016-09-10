#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


# =================================================================
# json
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
# 由于JSON标准规定JSON编码是UTF-8，
# 所以总能正确地在Python的str与JSON的字符串之间转换。

# 把Python对象变成一个JSON
# dumps()方法返回一个str，内容就是标准的JSON
# dump()方法可以直接把JSON写入一个file-like Object
d = dict(name='Bob', age=20, score=89)
json_str = json.dumps(d)
print(json_str)            # {"age": 20, "score": 89, "name": "Bob"}

with open('json_dump.json', 'w') as f:      # 将JSON写入一个文件
    json.dump(d, f)


# 把JSON反序列化(重构)为Python对象
# loads()方法把JSON的字符串反序列化，
# load()方法从file-like Object中读取字符串并反序列化。
d = json.loads(json_str)
print(d)                   # {'name': 'Bob', 'age': 20, 'score': 89}

with open('json_dump.json', 'r') as f:      # 将JSON重构为Python对象
    d = json.load(f)
    print(d)                # {'score': 89, 'age': 20, 'name': 'Bob'}


# =================================================================
# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过很多时候，
# 我们更喜欢用class表示对象，比如定义Student类，然后序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student(%s, %d, %d)' % (self.name, self.age, self.score)

stu = Student('Jambo', 23, 92)

# Student对象不是一个可序列化为JSON的对象
# 运行代码，会毫不留情地得到一个TypeError
# TypeError: <__main__.Student object at 0x0098ED90> is not JSON serializable
# json_str = json.dumps(s)
# print(json_str)


# 前面的代码之所以无法把Student类实例序列化为JSON，
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# 只需要为Student专门写一个**转换函数**，再把函数传进去即可。
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

json_str = json.dumps(stu, default=student2dict)
print(json_str)         # {"age": 23, "score": 92, "name": "Jambo"}

# {"name": "Jambo", "age": 23, "score": 92}
print(json.dumps(stu, default=lambda obj: obj.__dict__))


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，
# 传入的object_hook函数负责把dict转换为Student实例：
def dict2student(_d):
    return Student(_d['name'], _d['age'], _d['score'])

stu = json.loads(json_str, object_hook=dict2student)
# 打印出的是反序列化的Student实例对象
print(stu)                # Student(Jambo, 23, 92)


