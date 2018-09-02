#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = '零零碎碎的生活'

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Drawing text')
        self.show()

    # 绘图是在paintEvent()方法中完成。
    # QPainter 对象放在begin()方法和end()方法之间，它执行部件上的低层次的绘画和其他绘图设备。
    # 实际的绘画我们委托给drawText()方法。
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, painter):
        painter.setPen(QColor(168, 34, 3))          # 设置画笔颜色
        painter.setFont(QFont('Decorative', 10))    # 设置画笔字体
        # 在窗口绘画文本，rect()方法为paintEvent返回需要更新的矩形。
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
