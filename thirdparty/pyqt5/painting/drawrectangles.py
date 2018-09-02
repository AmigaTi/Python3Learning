#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Drawing rectangles')
        self.show()

    # 绘图是在paintEvent()方法中完成。
    # QPainter 对象放在begin()方法和end()方法之间，它执行部件上的低层次的绘画和其他绘图设备。
    # 实际的绘画我们委托给drawText()方法。
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawRectangles(event, painter)
        painter.end()

    def drawRectangles(self, event, painter):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        painter.setPen(color)

        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(10, 15, 90, 60)

        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(130, 15, 90, 60)

        painter.setBrush(QColor(25, 0, 90, 200))
        painter.drawRect(250, 15, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
