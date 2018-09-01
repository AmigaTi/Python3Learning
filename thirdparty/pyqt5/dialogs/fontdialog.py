#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showFontDialog)
        vbox.addWidget(btn)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('FontDialog')
        self.show()

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()        # 弹出字体对话框
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
