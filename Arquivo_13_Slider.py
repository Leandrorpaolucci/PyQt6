from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(("13_Slider"))
        self.create_widgets()

    def create_widgets(self):
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition((QSlider.TickPosition.TicksBelow))
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.slider_value)

        self.label = QLabel("0")

        layhouthorizontal = QHBoxLayout()
        layhouthorizontal.addWidget(self.slider)
        layhouthorizontal.addWidget(self.label)
        self.setLayout(layhouthorizontal)

    def slider_value(self):
        self.label.setText(str(self.slider.value()))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())