#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PIL import Image
from PIL import ImageFilter


# Platform: Window 7 x86
# Python 3.5.2
# ImagePreview: Windows Photo View


# 图像缩放
def image_thumbnail():
    # 1. 打开一个jpg图像文件
    image = Image.open('./files/cat.jpg')

    # 2. 获得图像尺寸
    w, h = image.size
    print('Original image size: %sx%s' % (w, h))

    # 3. 缩放到50%
    image.thumbnail((w//2, h//2))       # tuple
    print('Resize image to: %sx%s' % (w//2, h//2))

    # 把缩放后的图像用jpeg格式保存，并重命名保存文件名
    image.save('./files/thumbnail.jpg', 'jpeg')

print('execute image_thumbnail() -> ./files/thumbnail.jpg')
image_thumbnail()
print('preview ./files/thumbnail.jpg')
os.system('start ./files/thumbnail.jpg')
print('--' * 30)


# 图像模糊效果
def image_filter():
    # 打开一个jpg图像文件，当前路径中
    im = Image.open('./files/cat.jpg')

    # 应用模糊滤镜
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('./files/blur.jpg', 'jpeg')

image_filter()
print('execute image_filter() -> ./files/blur.jpg')
print('preview ./files/blur.jpg')
os.system('start ./files/blur.jpg')
print('--' * 30)


# 等比例压缩图片
def image_resize(im, dst_w=0, dst_h=0, qua=85):
    """
    只给了宽或者高，或者两个都给了，然后取比例合适的
    如果图片比给要压缩的尺寸都要小，就不压缩了
    """
    ori_w, ori_h = im.size
    width_ratio = height_ratio = None
    ratio = 1
    print('Original image size: %sx%s' % (ori_w, ori_h))
    if (ori_w and ori_w > dst_w) or (ori_h and ori_h > dst_h):
        if dst_w and ori_w > dst_w:
            width_ratio = float(dst_w) / ori_w      # 正确获取小数的方式
        if dst_h and ori_h > dst_h:
            height_ratio = float(dst_h) / ori_h

        if width_ratio and height_ratio:
            if width_ratio < height_ratio:          # 取最小值，即最大压缩率
                ratio = width_ratio
            else:
                ratio = height_ratio

        if width_ratio and not height_ratio:
            ratio = width_ratio

        if height_ratio and not width_ratio:
            ratio = height_ratio

        new_width = int(ori_w * ratio)
        new_height = int(ori_h * ratio)
    else:
        new_width = ori_w
        new_height = ori_h

    print('Resize image to: %sx%s' % (new_width, new_height))
    im.resize((new_width, new_height), Image.ANTIALIAS).save("./files/resized_cat.jpg", "JPEG", quality=qua)


print('execute image_resize() -> ./files/resized_cat.jpg')
img = Image.open('./files/cat.jpg')
image_resize(img, 100, 200)
print('preview ./files/resized_cat.jpg')
os.system('start ./files/resized_cat.jpg')
print('--' * 30)

'''
execute image_thumbnail() -> ./files/thumbnail.jpg
Original image size: 400x480
Resize image to: 200x240
preview ./files/thumbnail.jpg
------------------------------------------------------------
execute image_filter() -> ./files/blur.jpg
preview ./files/blur.jpg
------------------------------------------------------------
execute image_resize() -> ./files/resized_cat.jpg
Original image size: 400x480
Resize image to: 100x120
preview ./files/resized_cat.jpg
------------------------------------------------------------
'''