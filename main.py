from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QGridLayout, QLineEdit, QPushButton, QComboBox)
import sys
import re
import random


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PasswordGenerator')
        grid = QGridLayout()

        button = QPushButton('Generate')
        button.clicked.connect(self.generate)
        self.output_label = QLabel("")

        self.choice_label = QLabel("Choose your password strength in length")

        self.combo = QComboBox()
        self.pass_range = list(range(24))
        self.pass_range = [str(digit) for digit in self.pass_range]
        self.combo.addItems(self.pass_range)

        grid.addWidget(self.choice_label, 0, 0)
        grid.addWidget(self.combo, 0, 1)
        grid.addWidget(button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)

    def generate(self):
        SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+'
        password = []
        password_gen_range = int(self.combo.currentText())
        for _ in range(password_gen_range):
            random_number = random.randint(0, b=len(SYMBOLS)-1)
            letter = SYMBOLS[random_number]
            if letter.isalpha():
                if random.randint(1, 2) == 1:
                    letter = letter.upper()
            password.append(letter)
        password = ''.join(password)
        self.output_label.setText(f'Your new password: {password}')


app = QApplication(sys.argv)
speed_calculator = PasswordGenerator()
speed_calculator.show()
sys.exit(app.exec())
