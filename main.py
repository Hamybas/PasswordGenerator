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

        grid.addWidget(button, 0, 0)
        grid.addWidget(self.output_label, 1, 0)

        self.setLayout(grid)

    def generate(self):
        SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+'
        password = []
        for _ in range(12):
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
