#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()         # 创建一个信号 closeApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.comm = Communicate()
        self.comm.closeApp.connect(self.close)  # 将自定义的closeApp信号连接到QMainWindow的close()槽上

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('emit')
        self.show()

    def mousePressEvent(self, event):
        self.comm.closeApp.emit()               # 发射信号 closeApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
