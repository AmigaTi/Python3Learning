#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QDirModel
from PyQt5.QtWidgets import QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        dm = QDirModel()
        treeview = QTreeView(self)
        treeview.setModel(dm)

        vbox = QVBoxLayout()
        vbox.addWidget(treeview)

        self.setLayout(vbox)

        self.resize(640, 480)
        self.setWindowTitle('TreeView')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
