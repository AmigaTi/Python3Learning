#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit_32px.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')                # 定义此操作的一个快捷键
        exitAction.setStatusTip('Exit application')     # 当鼠标浮于菜单项之上就会显示的一个状态提示
        exitAction.triggered.connect(qApp.quit)         # 触发信号时执行QApplication的quit方法，中断应用

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar()                                # 开启状态栏显示功能

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ToolBar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
