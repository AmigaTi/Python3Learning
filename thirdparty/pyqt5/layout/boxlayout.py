#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okBtn = QPushButton('Ok')
        cancelBtn = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)              # 增加一个可伸缩空间，将按钮推挤到窗口右边
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)              # 增加一个可伸缩空间，将包含两个按钮的水平布局推挤到窗口底边
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('BoxLayout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
