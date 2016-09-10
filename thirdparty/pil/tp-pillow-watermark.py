#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont


def text_watermark(img, text, out_file='./files/watermark_cat.jpg', angle=23, opacity=0.20):
    # watermark = Image.new('RGBA', img.size, (255, 255, 255))    # 白色的膜，去掉(255,255,255)就好
    watermark = Image.new('RGBA', img.size)                       # 没有白色的膜
    font = 'C:/Windows/Fonts/Arial.ttf'
    size = 2
    n_font = ImageFont.truetype(font, size)                 # 得到字体
    n_width, n_height = n_font.getsize(text)
    text_box = min(watermark.size[0], watermark.size[1])
    while n_width + n_height < text_box:
        size += 2
        n_font = ImageFont.truetype(font, size)
        n_width, n_height = n_font.getsize(text)            # 文字逐渐放大，但要小于图片的宽高最小值

    text_width = (watermark.size[0] - n_width) / 2
    text_height = (watermark.size[1] - n_height) / 2
    draw = ImageDraw.Draw(watermark, 'RGBA')                # 在水印层加画笔
    draw.text((text_width, text_height), text, font=n_font, fill='#21acda')
    watermark = watermark.rotate(angle, Image.BICUBIC)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    Image.composite(watermark, img, watermark).save(out_file, 'JPEG')


if __name__ == '__main__':
    im = Image.open('./files/cat.jpg')
    text_watermark(im, 'linuxfor')
