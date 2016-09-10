#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import random
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw, ImageFont


# Platform: Window 7 x86
# Python 3.5.2
# ImagePreview: Windows Photo View


# 绘图
# 用随机颜色填充背景，再画上文字(数字和大小写字母)，最后对图像进行模糊，得到验证码图片
def image_draw():
    # 随机字母
    def randchar():
        return chr(random.randint(65, 90))

    # 随机数字字母
    def randalphanumeric(s=''):
        for i in range(ord('0'), ord('z') + 1):
            s += ' ' + chr(i)
        alphanumeric = re.split(r'[\s\W_]+', s.lstrip())
        return alphanumeric[random.randint(0, len(alphanumeric) - 1)]

    # 随机颜色1
    def randcolor():
        return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

    # 随机颜色2
    def randcolor2():
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    # 240 x 60
    width = 60 * 4
    height = 60
    # 创建Image对象
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)  # or C:\\Windows\Fonts\\Arial.ttf
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randcolor2())
    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), randalphanumeric(), font=font, fill=randcolor())
    # 模糊
    image = image.filter(ImageFilter.BLUR)
    image.save('./files/code.jpg', 'jpeg')

image_draw()
print('execute image_draw() -> ./files/code.jpg')
print('preview ./files/code.jpg')
os.system('start ./files/code.jpg')     # 生成后直接调用cmd来预览图片


