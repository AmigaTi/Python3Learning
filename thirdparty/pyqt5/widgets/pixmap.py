#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('./imgs/Animation_88.265780730897px.png')

        label = QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Pixmap')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
