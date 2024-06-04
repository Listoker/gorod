import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QScrollArea, QFormLayout
from PyQt5.QtCore import pyqtSignal
import random
import pygame
from PyQt5 import QtWidgets


class Generachia(QWidget):
    color_data = pyqtSignal()

    def __init__(self, lvl):
        super(Generachia, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Создание мира')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        # добавление кнопок и текста в интерфейс

        self.o1 = QLabel('Название', self)
        self.o1.move(600, int(self.y / 220))
        self.o1.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.okno1 = QPushButton('Начать игру', self)
        self.okno1.move(660, int(self.y / 1.54))
        self.okno1.resize(570, int(self.y / 10.8))
        self.okno1.clicked.connect(self.start)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno1 = QPushButton('Редактор', self)
        self.okno1.move(500, int(self.y / 4))
        self.okno1.resize(570, int(self.y / 10.8))
        self.okno1.clicked.connect(self.redaktor)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno1 = QPushButton('Отмена', self)
        self.okno1.move(50, int(self.y / 1.54))
        self.okno1.resize(570, int(self.y / 10.8))
        self.okno1.clicked.connect(self.otmena)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def otmena(self):
        Generachia.close(self)

    def start(self):
        pass

    def redaktor(self):
        karta = []
        for i in range(300):
            stroka = []
            for i2 in range(300):
                # высота, ресурс, чтото
                stroka.append([0, 'pusto'])
            karta.append(stroka)
        print(karta)

        WIDTH, HEIGHT = 450, 450

        tile_width = tile_height = 50

        pygame.init()
        screen_size = (450, 450)
        screen = pygame.display.set_mode(screen_size)
        tile_images = {
            'wall': load_image('box.png'),
            'empty': load_image('grass.png')
        }
        player_image = load_image('mar.png')
        # основной персонаж
        # группы спрайтов
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        camera = Camera()
        level_map2 = load_level('map.txt')
        level_map_spisok = []
        level_map = []
        for i in level_map2:
            for j in i:
                level_map_spisok.append(j)
            level_map.append(level_map_spisok)
            level_map_spisok = []
        player, level_x, level_y = generate_level(load_level('map.txt'))

        clock = pygame.time.Clock()
        FPS = 50
        running = True
        start_screen()
        y = 0
        x = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        move(player, 'up')
                    if event.key == pygame.K_DOWN:
                        move(player, 'down')
                    if event.key == pygame.K_LEFT:
                        move(player, 'left')
                    if event.key == pygame.K_RIGHT:
                        move(player, 'right')
            screen.fill(pygame.Color('black'))
            # изменяем ракурс камеры
            camera.update(player)
            # обновляем положение всех спрайтов
            for sprite in all_sprites:
                camera.apply(sprite)
            tiles_group.draw(screen)
            player_group.draw(screen)
            pygame.display.flip()
            clock.tick()
        pygame.quit()


class Pomoch(QWidget):
    def __init__(self, lvl):
        super(Pomoch, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Обучение')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        self.o1 = QLabel('                                                                            Обучение\n'
                         '1 Управление: двигатся можно на клавиши wasd или стрелочки\n'
                         '2 чтобы добыть блок нужно нажимать на клавиши мыши, размещая курсор на игровом поле\n'
                         '3 чтобы взять в руки предмет, надо нажать на него в инвентаре\n'
                         '4 чтобы создать предмет, нужно нажать на него в левой верхней части экрана\n'
                         '5 чтобы постать блок, нужно нажать на него в инвентаре, а после нажать на клетку рядом с аватаром\n'
                         '6 чтобы ударить моба, нужно взять в руки мечь и нажать в направлении животного(надо находится поблизости)\n'
                         '7 чтобы выкинуть предмет, нужно нажать на правую клавишу мыши с наставленным курсором на предмет в инвентаре\n'
                         '8 чтобы пополнить индикатор холода, нужно находится рядом с костром\n'
                         '9 чтобы пополнить индикатор голода, нужно покушать\n'
                         '10 игру можно открыть на полный экран, нажав f11\n'
                         '11 если показатель хп упадет до 0, то вы погибните\n'
                         '12 если вы находитесь рядом с верстаком, то доступно больше крафтов\n'
                         '13 чтобы выйти из игры, нажмите esc\n', self)
        self.o1.move(10, 10)
        self.o1.resize(int(1200), int(400))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')


class VseMiri(QWidget):
    signal__ = pyqtSignal()

    def __init__(self, lvl):
        super(VseMiri, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Обучение')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        self.o1 = QLabel('Ваши миры', self)
        self.o1.move(100, int(self.y / 220))
        self.o1.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        doroga = '/'.join(os.getcwd().split('\\'))

        spisok_mirov = os.listdir(f'{doroga}/mir')

        mygroupbox = QtWidgets.QGroupBox('')
        forma = QFormLayout()
        labellist = []
        forma.addRow(self.o1)
        vihod = QPushButton("Выйти")
        vihod.setStyleSheet('QPushButton {background-color: #FFFFFF}')
        vihod.clicked.connect(self.zakritie)
        forma.addRow(vihod)
        for i in range(len(spisok_mirov)):
            labellist.append(QPushButton(spisok_mirov[i], self))
            labellist[i].setStyleSheet('QPushButton {background-color: #A3C1DA}')
            labellist[i].clicked.connect(self.mir)
            forma.addRow(labellist[i])

        mygroupbox.setLayout(forma)
        scroll = QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(700)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)

    def zakritie(self):
        VseMiri.close(self)

    def mir(self):
        button = QApplication.instance().sender()
        with open('nastroiki_mira/' + button.text()) as f:
            f = f.read().split('%_%')
            self.lvl[0] = f[0]
            self.lvl[1] = f[1]
            self.lvl[2] = f[2]
        self.signal__.emit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)