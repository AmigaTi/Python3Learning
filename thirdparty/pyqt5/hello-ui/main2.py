#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


Ui_MainWindow, QtBaseClass = uic.loadUiType('hello.ui')


class MainUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec_())
