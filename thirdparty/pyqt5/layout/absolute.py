#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('A life', self)
        label1.move(15, 10)                 # 移动到 (x, y) 位置

        label2 = QLabel('of bits and pieces, ', self)
        label2.move(35, 40)

        label3 = QLabel('make it better', self)
        label3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('AbsoluteLayout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
