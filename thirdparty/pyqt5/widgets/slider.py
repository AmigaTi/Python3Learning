#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('./imgs/audio_volume_muted_32px.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('./imgs/audio_volume_muted_32px.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('./imgs/audio_volume_low_32px.png'))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('./imgs/audio_volume_medium_32px.png'))
        else:
            self.label.setPixmap(QPixmap('./imgs/audio_volume_high_32px.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
