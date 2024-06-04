import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from sozdanie import Generachia
from sozdanie import Pomoch
from sozdanie import VseMiri
import pygame
import random
import os


class StarveSurvival(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.lvl = ['1234567', 2, 2]
        self.generachia = Generachia(self.lvl)
        self.pomoch = Pomoch(self.lvl)
        self.vse_miri = VseMiri(self.lvl)
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 150, 1280, 720)
        self.setWindowTitle('Starve survival')

        self.greetine = QLabel(self)
        self.greetine.move(570, 100)
        self.greetine.resize(400, 100)
        self.greetine.setText("Starve survival")

        self.calculate_button = QPushButton('Начать новую игру', self)
        self.calculate_button.move(490, 200)
        self.calculate_button.resize(300, 70)
        self.calculate_button.clicked.connect(self.start_new)

        self.calculate_button = QPushButton('Продолжить с сохранения', self)
        self.calculate_button.move(490, 290)
        self.calculate_button.resize(300, 70)
        self.calculate_button.clicked.connect(self.start_old)

        self.calculate_button = QPushButton('Помощь', self)
        self.calculate_button.move(490, 380)
        self.calculate_button.resize(145, 70)
        self.calculate_button.clicked.connect(self.pomoch_)

        self.calculate_button = QPushButton('Выход из игры', self)
        self.calculate_button.move(645, 380)
        self.calculate_button.resize(145, 70)
        self.calculate_button.clicked.connect(self.vihod)

    def vihod(self):
        sys.exit()

    def pomoch_(self):
        self.pomoch.show()

    def start_new(self):
        self.generachia.show()

    def start_old(self):
        self.vse_miri.show()

    def start(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("data/fon_qt.png")))

    example = StarveSurvival()
    example.setPalette(palette)
    example.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
