#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QListWidget


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, 'ListWidget', 'Selected: ' + item.text())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        listWidget = ListWidget(self)
        listWidget.resize(300, 120)
        listWidget.addItem('QPushButton')
        listWidget.addItem('QMessageBox')
        listWidget.addItem('QLabel')
        listWidget.addItem('QLineEdit')

        listWidget.itemClicked.connect(listWidget.clicked)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ListWidget')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
