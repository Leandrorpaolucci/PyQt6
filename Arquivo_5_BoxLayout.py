from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtCore import QSize
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("05-Box_Layout")
        self.criar_widgets_horizontal()
        self.criar_widgets_vertical()


    def criar_widgets_horizontal(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton("Entrar")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Digite o seu e-mail: ")

        line_edit2 = QLineEdit()
        line_edit2.setPlaceholderText(("Insira a senha:" ))
        line_edit2.setEchoMode(QLineEdit.EchoMode.Password)

        hbox.addWidget(line_edit)
        hbox.addWidget(line_edit2)
        hbox.addWidget(btn1)

        self.setLayout(hbox)

    def criar_widgets_vertical(self):
        vbox = QVBoxLayout()

        btn1 = QPushButton("Entrar")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Digite o seu e-mail: ")

        line_edit2 = QLineEdit()
        line_edit2.setPlaceholderText(("Insira a senha:"))
        line_edit2.setEchoMode(QLineEdit.EchoMode.Password)

        vbox.addWidget(line_edit)
        vbox.addWidget(line_edit2)
        vbox.addWidget(btn1)

        self.setLayout(vbox)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())