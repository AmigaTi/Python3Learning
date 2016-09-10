#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from urllib import request


# 通过百度天气API，获取天气信息
def weather_work(city_name):
    city_name = str(city_name.encode('utf-8')).replace('''''\\x''', '%')[2:].upper()
    city_name = city_name[:len(city_name) - 1]
    with request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location=' + city_name + '&output=json&ak=nzOZroYb0jPL9G4541HVUxmS') as f:
        data = f.read()
        data_json = json.loads(data.decode('utf-8'))
        if data_json['error'] != 0:
            print('检查城市输入是否有误')
            return
        print(data_json['results'][0]['currentCity'] + "'s weather:")
        print(data_json['date'] + "的数据" + '\n')
        for t in data_json['results'][0]['weather_data']:
            print(t['date'] + '\n' + t['temperature'] + '\n' + t['weather'] + '\n' + t['wind'] + '\n')


while True:
    city = input('输入城市名称（q结束）：')
    if city == 'q':
        break
    weather_work(city)
