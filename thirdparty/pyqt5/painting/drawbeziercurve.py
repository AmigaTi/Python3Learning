#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Drawing Bezier curve')
        self.show()

    # 绘图是在paintEvent()方法中完成。
    # painter 对象放在begin()方法和end()方法之间，它执行部件上的低层次的绘画和其他绘图设备。
    # 实际的绘画我们委托给drawText()方法。
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(painter)
        painter.end()

    # 绘制贝塞尔曲线
    def drawBezierCurve(self, painter):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        painter.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
