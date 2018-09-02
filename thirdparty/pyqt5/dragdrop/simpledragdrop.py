#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)           # 启动放置事件

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)       # 启动拖动事件
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Simple drag and drop')
        self.show()


# 从单行文本编辑控件中将输入的文本选中后拖到按钮控件上后松开鼠标，按钮的标签将发生变化。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
