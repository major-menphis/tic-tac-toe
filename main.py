import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from random import randint
from pygame import mixer


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic-Tac-Toe')
        self.setWindowIcon(QIcon('./files/window_icon.png'))
        self.resize(300, 300)
        self.setMaximumSize(300, 400)
        self.setMinimumSize(300, 400)
        self.players = [
            {
                'name': 'Jogador',
                'mark': 'X'
            },
            {
                'name': 'Computador',
                'mark': 'O'
            }
        ]
        random_player = self.players[randint(0, 1)]
        self.start_player = random_player
        self.round_count = 0
        self.player_round = self.start_player
        self.player_next_round = self.update_next_player()
        self.interface()
        # iniciar o mixer do pygame
        mixer.init()
        self.play_main_song('./files/main_song.mp3')
        self.show()

    def interface(self):
        # cria layout do jogo e layout da informação
        layout = QGridLayout()
        layout_box = QVBoxLayout()
        # cria os botões do jogo
        self.btn_0 = QPushButton('', self)
        self.btn_0.setGeometry(0, 0, 100, 100)
        self.btn_1 = QPushButton('', self)
        self.btn_1.setGeometry(100, 0, 100, 100)
        self.btn_2 = QPushButton('', self)
        self.btn_2.setGeometry(200, 0, 100, 100)
        self.btn_3 = QPushButton('', self)
        self.btn_3.setGeometry(0, 100, 100, 100)
        self.btn_4 = QPushButton('', self)
        self.btn_4.setGeometry(100, 100, 100, 100)
        self.btn_5 = QPushButton('', self)
        self.btn_5.setGeometry(200, 100, 100, 100)
        self.btn_6 = QPushButton('', self)
        self.btn_6.setGeometry(0, 200, 100, 100)
        self.btn_7 = QPushButton('', self)
        self.btn_7.setGeometry(100, 200, 100, 100)
        self.btn_8 = QPushButton('', self)
        self.btn_8.setGeometry(200, 200, 100, 100)
        self.new_game_button = QPushButton('New Game', self)
        self.new_game_button.setGeometry(200, 300, 100, 50)
        # referencia a matriz de botões
        self.buttons_matrix = [
            [self.btn_0, self.btn_1, self.btn_2],
            [self.btn_3, self.btn_4, self.btn_5],
            [self.btn_6, self.btn_7, self.btn_8]
        ]
        # configura o tamanho das marcas nos botões
        for row in self.buttons_matrix:
            for btn in row:
                btn.setStyleSheet('''font-size: 16px;
                ''')
        # cria o label de informações (descrição)
        self.label_info = QLabel('Round Player:', self)
        self.label_info.setGeometry(0, 300, 200, 50)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_info.setStyleSheet('''font-size: 16px;
        padding: 5px;
        ''')
        # cria o label de informações (valores exibidos para usuário)
        self.label = QLabel(self.player_round['name'], self)
        self.label.setGeometry(0, 350, 200, 50)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet('''font-size: 14px;
        padding: 5px;
        ''')
        # adiciona os labels ao layout
        layout_box.addWidget(self.label_info)
        layout_box.addWidget(self.label)
        layout.addChildLayout(layout_box)
        # conecta as funções de cada botão
        self.btn_0.clicked.connect(lambda: self.click(self.btn_0))
        self.btn_1.clicked.connect(lambda: self.click(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.click(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.click(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.click(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.click(self.btn_5))
        self.btn_6.clicked.connect(lambda: self.click(self.btn_6))
        self.btn_7.clicked.connect(lambda: self.click(self.btn_7))
        self.btn_8.clicked.connect(lambda: self.click(self.btn_8))
        self.new_game_button.clicked.connect(self.new_game)
        # adiciona cada botão ao layout
        layout.addWidget(self.btn_0, 0, 0)
        layout.addWidget(self.btn_1, 0, 1)
        layout.addWidget(self.btn_2, 0, 2)
        layout.addWidget(self.btn_3, 1, 0)
        layout.addWidget(self.btn_4, 1, 1)
        layout.addWidget(self.btn_5, 1, 2)
        layout.addWidget(self.btn_6, 2, 0)
        layout.addWidget(self.btn_7, 2, 1)
        layout.addWidget(self.btn_8, 2, 2)

    # função ativada quando marca uma escolha
    def click(self, btn):
        mark_player = self.player_round['mark']
        btn.setText(mark_player)
        btn.setDisabled(True)
        self.check_winner()
        self.update_next_player()
        self.update_label()
        self.round()
        self.play_effect('./files/click.wav')

    # atualiza o player e conta a rodada
    def round(self):
        self.player_round = self.player_next_round
        self.round_count += 1
        return self.round_count

    # identifica o proximo player baseado no atual
    def update_next_player(self):
        copy_players = self.players.copy()
        index = self.players.index(self.player_round)
        copy_players.pop(index)
        self.player_next_round = copy_players[0]
        return copy_players[0]

    # verifica se existe um vencedor
    def check_winner(self):
        for row in range(3):
            if self.buttons_matrix[row][0].text() == self.buttons_matrix[row][1].text() == self.buttons_matrix[row][2].text() != '':
                self.disable_all_btn()
                self.label_info.setText('Winner')
                self.change_win_color_mark(
                    self.buttons_matrix[row][0],
                    self.buttons_matrix[row][1],
                    self.buttons_matrix[row][2]
                    )
                return True

        for col in range(3):
            if self.buttons_matrix[0][col].text() == self.buttons_matrix[1][col].text() == self.buttons_matrix[2][col].text() != '':
                self.disable_all_btn()
                self.label_info.setText('Winner')
                self.change_win_color_mark(
                    self.buttons_matrix[0][col],
                    self.buttons_matrix[1][col],
                    self.buttons_matrix[2][col]
                    )
                return True

        if self.buttons_matrix[0][0].text() == self.buttons_matrix[1][1].text() == self.buttons_matrix[2][2].text() != '':
            self.disable_all_btn()
            self.label_info.setText('Winner')
            self.change_win_color_mark(
                    self.buttons_matrix[0][0],
                    self.buttons_matrix[1][1],
                    self.buttons_matrix[2][2]
                    )
            return True

        elif self.buttons_matrix[0][2].text() == self.buttons_matrix[1][1].text() == self.buttons_matrix[2][0].text() != '':
            self.disable_all_btn()
            self.label_info.setText('Winner')
            self.change_win_color_mark(
                    self.buttons_matrix[0][2],
                    self.buttons_matrix[1][1],
                    self.buttons_matrix[2][0]
                    )
            return True
        else:
            if self.verify_buttons_filled():
                self.label_info.setText('A tie')
                return False

    # atualiza e mostra na tela a cor da linha do vencedor
    def change_win_color_mark(self, button_1, button_2, button_3):
        button_1.setStyleSheet('''
        font-size: 16px;
        color: red;
        ''')
        button_2.setStyleSheet('''
        font-size: 16px;
        color: red;
        ''')
        button_3.setStyleSheet('''
        font-size: 16px;
        color: red;
        ''')

    # verifica se todos os botões estão preenchidos
    def verify_buttons_filled(self):
        blank_button = 0
        for row in self.buttons_matrix:
            for btn in row:
                if btn.text() == '':
                    blank_button += 1
        if blank_button == 0:
            return True
        else:
            return False

    # desabilita os botes de escolha do jogo
    def disable_all_btn(self):
        for row in self.buttons_matrix:
            for btn in row:
                btn.setDisabled(True)

    # atualiza o label de rodada e vencedor
    def update_label(self):
        if self.label_info.text() != 'Winner' and self.label_info.text() != 'A tie':
            self.label.setText(self.player_next_round['name'])
        elif self.label_info.text() != 'A tie':
            self.label.setText(self.player_round['name'])
        else:
            self.label.setText('Try next time')

    # redefine as informações para o usuário
    def reset_label(self):
        self.label_info.setText('Round player:')
        self.label.setText(self.player_round['name'])

    # redefine os atributos do jogo
    def reset_class_atributes(self):
        random_player = self.players[randint(0, 1)]
        self.start_player = random_player
        self.round_count = 0
        self.player_round = self.start_player
        self.player_next_round = self.update_next_player()

    # inicia novo jogo
    def new_game(self):
        self.reset_buttons()
        self.reset_class_atributes()
        self.reset_label()

    # reset sas marcas dos botões
    def reset_buttons(self):
        for row in self.buttons_matrix:
            for btn in row:
                if btn.text() != '':
                    btn.setText('')
                    btn.setStyleSheet('''
                    font-size: 16px;
                    color: grey
                    ''')
                btn.setDisabled(False)

    # toca a musica principal em loop
    def play_main_song(self, file):
        mixer.music.load(file)
        mixer.music.play(-1)

    # toca os efeitos
    def play_effect(self, file):
        mixer.Sound(file).play()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    sys.exit(qt.exec())
