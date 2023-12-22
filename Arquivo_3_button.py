from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtCore import QSize
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50 , 800,450)
        self.setWindowTitle("Meu primeiro Button")
        self.create_button()

    def create_button(self):
        btn = QPushButton("Clique Aqui", self)
        btn.setGeometry(50, 50, 300, 90)
        btn.setFont(QFont("Times", 25, QFont.Weight.Bold))
        btn.setStyleSheet("Background-color: black; color: yellow")
        btn.setIcon(QIcon("image/gifcamus.gif"))
        btn.setIconSize(QSize(100, 200))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())


