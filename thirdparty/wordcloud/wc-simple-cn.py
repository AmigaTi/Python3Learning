#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)
frequencies = {u'黑曼巴': 0.2, u'库日天': 0.3, u'汤神': 0.3, u'杜死神': 0.1, u'一哥': 0.1}
# font_path = "fonts/SourceHanSerif/SourceHanSerifK-Light.otf"
font_path = path.join(d, 'fonts', 'SourceHanSerif', 'SourceHanSerifK-Light.otf')

# 根据输入词频来生成词云，和英文词云不同的是要设置字体
wordcloud = WordCloud(background_color="white", font_path=font_path).fit_words(frequencies)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
