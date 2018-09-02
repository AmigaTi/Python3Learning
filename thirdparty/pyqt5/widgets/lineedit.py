#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        lineEdit = QLineEdit(self)

        lineEdit.move(60, 100)
        self.label.move(60, 40)

        # 如果单行文本编辑框框内文本被改变，调用onChanged()方法
        lineEdit.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('LineEdit')
        self.show()

    def onChanged(self, text):
        self.label.setText(text)        # 设置标签的显示文本
        self.label.adjustSize()         # 调整标签相对于显示的文本的长度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
