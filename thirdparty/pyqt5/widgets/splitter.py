#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        topLeft = QFrame(self)
        topLeft.setFrameShape(QFrame.StyledPanel)

        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)

        splitter2 = QSplitter(Qt.Vertical)      # 可以拖拽来调整大小
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Splitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
