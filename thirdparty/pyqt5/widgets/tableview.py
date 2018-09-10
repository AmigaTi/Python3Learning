#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QTableView, QHeaderView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['Language', 'Creator', 'Date'])
        self.qList = [['C', 'Dennis Ritchie', '1971'],
                      ['Perl', 'Larry Wall', '1987'],
                      ['Unix', 'Ken Thompson & Dennis Ritchie', '1969'],
                      ['Linux', 'Linus Torvalds', '1991']]
        for row in range(4):
            for column in range(3):
                item = QStandardItem(self.qList[row][column])
                self.model.setItem(row, column, item)

        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 显示方格完整内容
        # self.tableView.resizeRowsToContents()
        # self.tableView.resizeColumnsToContents()

        # self.model.appendRow([
        #     QStandardItem('SQLite'),
        #     QStandardItem('D. Richard Hipp'),
        #     QStandardItem('2000')
        # ])
        # self.tableView.setModel(self.model)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        self.resize(300, 300)
        self.setWindowTitle('TableView')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
