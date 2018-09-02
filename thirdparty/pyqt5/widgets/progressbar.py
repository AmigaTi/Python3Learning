#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QBasicTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()      # 创建定时器对象，用于激活进度条
        self.step = 0                   # 进度条步进值

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ProgressBar')
        self.show()

    def timerEvent(self, event):        # 定时器事件处理
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)     # 开启定时器，参数：定时时间和接收定时器事件对象
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
