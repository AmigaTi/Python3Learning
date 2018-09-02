#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Drawing points')
        self.show()

    # 绘图是在paintEvent()方法中完成。
    # QPainter 对象放在begin()方法和end()方法之间，它执行部件上的低层次的绘画和其他绘图设备。
    # 实际的绘画我们委托给drawText()方法。
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawPoints(event, painter)
        painter.end()

    def drawPoints(self, event, painter):
        painter.setPen(Qt.red)      # 设置画笔颜色为红色
        size = self.size()          # 获取当前窗口大小

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            painter.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
