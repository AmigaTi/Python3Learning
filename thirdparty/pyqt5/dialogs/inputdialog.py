#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QInputDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showInputDialog)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('InputDialog')
        self.show()

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'InputDialog', 'Enter your name;')
        if ok:
            self.lineEdit.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
