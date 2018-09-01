#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QDesktopWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.setWindowTitle('DesktopWidget')
        self.center()
        self.show()

    def center(self):
        fGeometry = self.frameGeometry()
        dCenter = QDesktopWidget().availableGeometry().center()
        fGeometry.moveCenter(dCenter)
        self.move(fGeometry.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
