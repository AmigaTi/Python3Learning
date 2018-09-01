#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qBtn = QPushButton('Quit', self)
        qBtn.clicked.connect(QCoreApplication.instance().quit)
        qBtn.resize(qBtn.sizeHint())
        qBtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PushButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setWindowTitle('MessageBox')
    # win.show()
    sys.exit(app.exec_())
