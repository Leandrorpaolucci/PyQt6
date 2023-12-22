from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.radio = ""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # libera o ajuste da janela
        #Form.resize(654, 568)
        #---------------------------------
        #Não libera o ajuste da janela
        Form.setFixedSize(654, 568)  # Substitua esses valores pela largura e altura desejadas
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 519, 42))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(26)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(25, 194, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 282, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(65, 157, 255)")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(parent=Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 140, 89, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 455, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(65, 157, 255)")
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 170, 88, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=Form)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 200, 69, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.checkBox = QtWidgets.QCheckBox(parent=Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 320, 82, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 350, 64, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 380, 73, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 410, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_final = QtWidgets.QLabel(parent=Form)
        self.label_final.setGeometry(QtCore.QRect(110, 450, 411, 20))
        self.label_aviso = QtWidgets.QLabel(parent=Form)
        self.label_aviso.setGeometry(QtCore.QRect(30, 240, 400, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_aviso.setFont(font)
        self.label_aviso.setStyleSheet("color: red")
        self.label_aviso.setObjectName("label_aviso")
        self.label_aviso.setText("")
        self.label_final.setText("")
        self.label_final.setObjectName("label_final")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 450, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_final = QtWidgets.QLabel(parent=Form)
        self.label_final.setGeometry(QtCore.QRect(110, 450, 411, 20))

        self.label_aviso = QtWidgets.QLabel(parent=Form)
        self.label_aviso.setGeometry(QtCore.QRect(30, 240, 400, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_aviso.setFont(font)
        self.label_aviso.setStyleSheet("color: red")
        self.label_aviso.setObjectName("label_aviso")
        self.label_aviso.setText("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.radioButton.toggled.connect(self.radio_select)
        self.radioButton_2.toggled.connect(self.radio_select)
        self.radioButton_3.toggled.connect(self.radio_select)
        self.checkBox.setChecked(True)
        self.pushButton.clicked.connect(self.btn_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LRP-Pizza\'s"))
        self.label.setText(_translate("Form", "Pizzaria LRP (Leandro R. Paolucci)"))
        self.label_2.setText(_translate("Form", "Escolha o sabor desejado da pizza"))
        self.radioButton.setText(_translate("Form", "Mussarela"))
        self.label_3.setText(_translate("Form", "Caso tenha preferência, selecione os adicionais abaixo:"))
        self.radioButton_2.setText(_translate("Form", "Calabresa"))
        self.radioButton_3.setText(_translate("Form", "Frango"))
        self.checkBox.setText(_translate("Form", "Azeitona"))
        self.checkBox_2.setText(_translate("Form", "Bacon"))
        self.checkBox_3.setText(_translate("Form", "Palmito"))
        self.checkBox_4.setText(_translate("Form", "Milho"))
        self.pushButton.setText(_translate("Form", "Enviar"))

    def radio_select(self):
        self.radio = ""

        if self.radioButton.isChecked():
            self.radio = self.radioButton.text()
        elif self.radioButton_2.isChecked():
            self.radio = self.radioButton_2.text()
        elif self.radioButton_3.isChecked():
            self.radio = self.radioButton_3.text()
        else:
            self.radio = "Você não selecionou uma pizza!"
            self.label_aviso.setText(self.radio)

    def btn_clicked(self):
        check1 = ""
        check2 = ""
        check3 = ""
        check4 = ""
        if self.checkBox.isChecked():
            check1 = self.checkBox.text()

        if self.checkBox_2.isChecked():
            check2 = self.checkBox_2.text()

        if self.checkBox_3.isChecked():
            check3 = self.checkBox_3.text()

        if self.checkBox_4.isChecked():
            check4 = self.checkBox_4.text()

        self.label_final.setText(f"A PIZZA SELECIONADA FOI: ' {self.radio} ' E OS ADICIONAIS: ' {check1} {check2} {check3} {check4} '")


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
