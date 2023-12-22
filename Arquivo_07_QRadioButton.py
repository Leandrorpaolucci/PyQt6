from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtCore import QSize
import sys
from image import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("07-RadioButton")
        self.create_widgets()

    def create_widgets(self):
        radwhatsapp = QRadioButton("WhatsApp")
        radwhatsapp.setIcon(QIcon("image/whatsapp.png"))

        radinstagram = QRadioButton("Instagram")
        radinstagram.setIcon(QIcon("image/instagram.jpg"))

        radfacebook = QRadioButton("Facebook")
        radfacebook.setIcon(QIcon("image/facebook1.png"))

        radwhatsapp.toggled.connect(self.radio_button_selected)
        radinstagram.toggled.connect(self.radio_button_selected)
        radfacebook.toggled.connect(self.radio_button_selected)

        self.label = QLabel("Selecione a sua rede social mais utilizada")


        vbox = QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addWidget(radwhatsapp)
        vbox.addWidget(radfacebook)
        vbox.addWidget(radinstagram)
        self.setLayout(vbox)

    def radio_button_selected(self):
        radio_selected = self.sender()
        if radio_selected.isChecked():
            self.label.setText(f"Sua rede social favorita {radio_selected.text()}")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
