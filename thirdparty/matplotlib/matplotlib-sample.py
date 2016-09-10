#!/usr/bin/python
# -*- coding: utf-8 -*-

# import matplotlib.pyplot as plt
from matplotlib import pyplot

# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)        # only "explode" the 2nd slice (i.e. 'Hogs')

pyplot.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Set aspect ratio to be equal so that pie is drawn as a circle.
pyplot.axis('equal')

pyplot.savefig('./pie.png')
pyplot.show()


# ImportError: No module named 'matplotlib.pyplot'; 'matplotlib' is not a package
# ImportError: cannot import name 'pyplot'

# py文件跟库重名

