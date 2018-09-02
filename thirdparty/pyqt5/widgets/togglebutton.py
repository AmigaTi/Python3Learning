#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtGui import QColor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        redBtn = QPushButton('Red', self)
        redBtn.setCheckable(True)
        redBtn.move(10, 10)
        redBtn.clicked[bool].connect(self.setColor)     # 把clicked信号连接到setColor方法上

        greenBtn = QPushButton('Green', self)
        greenBtn.setCheckable(True)
        greenBtn.move(10, 60)
        greenBtn.clicked[bool].connect(self.setColor)

        blueBtn = QPushButton('Blue', self)
        blueBtn.setCheckable(True)
        blueBtn.move(10, 110)
        blueBtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QFrame {background-color: %s}' % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('ToggleButton')
        self.show()

    def setColor(self, pressed):
        # 获取信号发送器，用于判断是哪个按钮发送的信号
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet('QFrame {background-color: %s}' % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
