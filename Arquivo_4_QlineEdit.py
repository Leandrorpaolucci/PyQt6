from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtCore import QSize
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("04-LineEdit")
        self.setMinimumHeight(80)
        self.setMinimumWidth(250)
        self.create_line_edit()


    def create_line_edit(self):
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 15))

        #solicita a digitação
        line_edit.setPlaceholderText("Digite a sua senha:  ")

        #seta o texto
        #line_edit.setText("Olá, tudo bem?")

        #Ocultar a senha
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
