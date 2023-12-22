from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtCore import QSize
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("07-RadioButton")




app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())