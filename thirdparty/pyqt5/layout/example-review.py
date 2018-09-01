#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        okBtn = QPushButton('Ok')
        cancelBtn = QPushButton('Cancel')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)      # 设置组件的跨行和跨列参数

        hbox = QHBoxLayout()            # 创建水平箱布局，用于放置两个按钮
        hbox.addStretch(1)              # 增加一个可伸缩空间，将按钮推挤到窗口右边
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()            # 创建垂直箱布局，用于放置其他布局
        vbox.addLayout(grid)            # 先添加网格布局
        vbox.addLayout(hbox)            # 再添加水平箱布局

        self.setLayout(vbox)            # 设置为垂直箱布局

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
