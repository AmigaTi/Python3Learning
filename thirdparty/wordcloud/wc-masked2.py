#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread


text = open('alice.txt', 'r').read()        # 读取一个txt文件
bg_pic = imread('alice_mask.png')           # 读入背景图片
# 生成词云
wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=1.5).generate(text)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
