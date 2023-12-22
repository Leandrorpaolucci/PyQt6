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
        self.check1 = QCheckBox("WhatsApp")
        self.check1.setIcon(QIcon("image/whatsapp.png"))
        self.check1.setFont(QFont("Sanserif", 15))
        self.check1.toggled.connect(self.item_selected)

        self.check2 = QCheckBox("Instagram")
        self.check2.setIcon(QIcon("image/instagram.jpg"))
        self.check2.setFont(QFont("Sanserif", 15))
        self.check2.toggled.connect(self.item_selected)

        self.check3 = QCheckBox("Facebook")
        self.check3.setIcon(QIcon("image/facebook1.png"))
        self.check3.setFont(QFont("Sanserif", 15))
        self.check3.toggled.connect(self.item_selected)

        self.label = QLabel("Selecione uma ou mais rede sociais mais utilizadas!")
        self.label.setFont(QFont("Sanserif", 15))


        vbox = QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.label)
        vbox.addWidget(self.check1)
        vbox.addWidget(self.check2)
        vbox.addWidget(self.check3)

    def item_selected(self):
        texto_whatsapp = ""
        texto_instagram = ""
        texto_facebook = ""
        if self.check1.isChecked():
            texto_whatsapp = self.check1.text()

        if self.check2.isChecked():
            texto_instagram = self.check2.text()

        if self.check3.isChecked():
            texto_facebook = self.check3.text()

        selecao = texto_whatsapp + " " + texto_instagram + " " + texto_facebook
        self.label.setText(f"Rede social selecionada : {selecao}")



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
