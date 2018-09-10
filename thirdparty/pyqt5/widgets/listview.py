#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QMessageBox, QListView
from PyQt5.QtCore import QStringListModel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        listview = QListView(self)      # 创建列表视图
        slm = QStringListModel()        # 创建字符串列表模型，用于填充数据
        self.qList = ['Java', 'C', 'Python', 'C++', 'Shell', 'Perl']
        slm.setStringList(self.qList)   # 设置模型的数据
        listview.setModel(slm)          # 设置视图的模型

        # 单击列表项触发自定义的槽函数
        listview.clicked.connect(self.clicked)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ListView')
        self.show()

    def clicked(self, qModelIndex):
        QMessageBox.information(self, 'ListView', 'Selected: ' + self.qList[qModelIndex.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
