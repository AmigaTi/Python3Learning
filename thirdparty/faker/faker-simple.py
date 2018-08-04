#!/usr/bin/python
# -*- coding:utf-8 -*-

from faker import Faker

fake = Faker()

# Basic Usage
print(fake.name())
print(fake.address())
print(fake.text())

for _ in range(10):
    print(fake.name())


# Localization
# en_US - English (United States)
# zh_CN - Chinese (China)
# zh_TW - Chinese (Taiwan)
fake = Faker(locale='zh_CN')   #
for _ in range(10):
    print(fake.name())

print('--' * 20)
print("name: " + fake.name())                                       # 姓名
print('address: ' + fake.address())                                 # 地址
print('country: ' + fake.country())                                 # 国家
print('country_code: ' + fake.country_code())                       # 国家编码
print('city_suffix: ' + fake.city_suffix())                         # 市/县
print('district: ' + fake.district())                               # 区
print('geo_coordinate: ' + fake.geo_coordinate().to_eng_string())   # 地理坐标
print('latitude: ' + fake.latitude().to_eng_string())               # 纬度
print('longitude: ' + fake.longitude().to_eng_string())             # 经度
print('numerify: ' + fake.numerify())              # 三位随机数字
print('postcode: ' + fake.postcode())              # 邮编
print('province: ' + fake.province())              # 省份

print('street_address: ' + fake.street_address())               # 街道地址
print('street_name: ' + fake.street_name())                     # 街道名称
print('street_suffix: ' + fake.street_suffix())                 # 街/路

print('random_digit: %d' % fake.random_digit())                     # 0-9随机数
print('random_digit_not_null: %s' % fake.random_digit_not_null())   # 1-9随机数
print('random_element: ' + fake.random_element())                   # 随机字母
print('random_int: %d' % fake.random_int())                         # 随机数字[min, max]，默认为0-9999
print('random_letter: ' + fake.random_letter())                     # 随机字母
print('random_number: %d' % fake.random_number())                   # 随机数字，通过digits设置生成的数字位数

print('color_name: ' + fake.color_name())           # 随机颜色名称
print('hex_color: ' + fake.hex_color())             # 随机颜色HEX表示
print('rgb_color: ' + fake.rgb_color())             # 随机颜色RGB表示
print('safe_color_name: ' + fake.safe_color_name()) # 随机安全色名
print('safe_hex_color: ' + fake.safe_hex_color())   # 随机安全Hex颜色

print('bs: ' + fake.bs())                                                   # 随机公司服务名
print('company: ' + fake.company())                                         # 随机公司名称 (长)
print('company_prefix: ' + fake.company_prefix())                           # 随机公司名称 (短)
print('company_suffix: ' + fake.company_suffix())                           # 公司性质
print('credit_card_expire: ' + fake.credit_card_expire())                   # 随机信用卡到期日
print('credit_card_full: ' + fake.credit_card_full())                       # 完整信用卡信息
print('credit_card_number: ' + fake.credit_card_number())                   # 信用卡卡号
print('credit_card_provider: ' + fake.credit_card_provider())               # 信用卡类型
print('credit_card_security_code: ' + fake.credit_card_security_code())     # 信用卡安全码

print('phone_number: ' + fake.phone_number())       # 电话号码
print('profile: ' + str(fake.profile()))            # 档案信息

