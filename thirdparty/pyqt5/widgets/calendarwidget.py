#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import QDate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.move(20, 20)
        calendar.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = calendar.selectedDate()
        self.label.setText(date.toString())
        self.label.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('CalendarWidget')
        self.show()

    def showDate(self, date):
        self.label.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
