import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer, Qt


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic-Tac-Toe')
        self.resize(300, 300)
        self.setMaximumSize(300, 400)
        self.setMinimumSize(300, 400)
        self.player = 'player'
        self.interface()
        self.show()

    def interface(self):
        layout = QGridLayout()
        layout_box = QVBoxLayout()

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

        self.buttons_matrix = [
            [self.btn_0, self.btn_1, self.btn_2],
            [self.btn_3, self.btn_4, self.btn_5],
            [self.btn_6, self.btn_7, self.btn_8]
        ]

        self.label_info = QLabel('Round Player:', self)
        self.label_info.setGeometry(0, 300, 300, 50)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_info.setStyleSheet('''font-size: 15px;
        padding: 5px;
        ''')

        self.label = QLabel(self.player, self)
        self.label.setGeometry(0, 350, 300, 50)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet('''font-size: 14px;
        padding: 5px;
        ''')

        layout_box.addWidget(self.label)
        layout_box.addWidget(self.label_info)

        layout.addChildLayout(layout_box)

        self.btn_0.clicked.connect(lambda: self.click(self.btn_0))
        self.btn_1.clicked.connect(lambda: self.click(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.click(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.click(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.click(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.click(self.btn_5))
        self.btn_6.clicked.connect(lambda: self.click(self.btn_6))
        self.btn_7.clicked.connect(lambda: self.click(self.btn_7))
        self.btn_8.clicked.connect(lambda: self.click(self.btn_8))

        layout.addWidget(self.btn_0, 0, 0)
        layout.addWidget(self.btn_1, 0, 1)
        layout.addWidget(self.btn_2, 0, 2)
        layout.addWidget(self.btn_3, 1, 0)
        layout.addWidget(self.btn_4, 1, 1)
        layout.addWidget(self.btn_5, 1, 2)
        layout.addWidget(self.btn_6, 2, 0)
        layout.addWidget(self.btn_7, 2, 1)
        layout.addWidget(self.btn_8, 2, 2)
        layout.addWidget(self.label)

        #self.timer = QTimer()
        #self.timer.timeout.connect(self.update)
        #self.timer.start(900)

    def click(self, btn):
        mark_text = self.player_mark()
        btn.setText(mark_text)
        btn.setDisabled(True)
        self.check_winner()
        self.update()

    def player_mark(self):
        if self.player == 'player':
            self.player = 'computer'
            return 'X'
        elif self.player == 'computer':
            self.player = 'player'
            return 'O'

    def check_winner(self):
        for row in range(3):
            if self.buttons_matrix[row][0].text() == self.buttons_matrix[row][1].text() == self.buttons_matrix[row][2].text() != '':
                print('winner')
                self.disable_all_btn()
                self.label_info.setText('Winner')

    def disable_all_btn(self):
        for row in self.buttons_matrix:
            for btn in row:
                btn.setDisabled(True)

    def update(self):
        if self.label_info != 'Winner':
            self.label.setText(self.player)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    sys.exit(qt.exec())
