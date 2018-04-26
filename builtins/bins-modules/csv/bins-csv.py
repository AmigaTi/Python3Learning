#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

'''
AMEX Companies - NASDAQ.com
https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX
'''

# 从csv文件中读取数据
with open('companylist.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# 写入数据到csv文件中
languages = [
    ['Language', 'Creator', 'CreatedTime'],
    ['Python', 'Guido van Rossum', 'NA'],
    ['Unix', 'Ken Thompson & Dennis Ritchie', '1969'],
    ['Linux', 'Linux Torvalds', '1991'],
    ['C', 'Dennis Ritchie', '1971']
]

# 若不指定newline=''，则每写入一行将有一空行被写入
with open('languages.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerows(languages)
    for row in languages:
        writer.writerow(row)
print('===' * 20)


# 使用DictReader和DictWriter来以字典方式获取数据
# 表的第一行作为key，可以访问每一行中的数据

with open('languages.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Language'] == 'Python':
            print('Author of Python: ', row['Creator'])     # Author of Python:  Guido van Rossum


headers = ['name', 'age']
data = [
    {'name': 'Bob', 'age': 23},
    {'name': 'Tom', 'age': 30},
    {'name': 'Jerry', 'age': 18}
]

with open('persons.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    # writer.writerows(data)
    for row in data:
        writer.writerow(row)

'''
['Symbol', 'Name', 'LastSale', 'MarketCap', 'ADR TSO', 'IPOyear', 'Sector', 'Industry', 'Summary Quote', '']
['XXII', '22nd Century Group, Inc', '2.13', '264409865.31', 'n/a', 'n/a', 'Consumer Non-Durables', 'Farming/Seeds/Milling', 'https://www.nasdaq.com/symbol/xxii', '']
['FAX', 'Aberdeen Asia-Pacific Income Fund Inc', '4.58', '1154759173.92', 'n/a', '1986', 'n/a', 'n/a', 'https://www.nasdaq.com/symbol/fax', '']
'''
