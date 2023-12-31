# Form implementation generated from reading ui file 'MyApp.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(401, 316)
        Form.setAutoFillBackground(False)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 361, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #LineEdit
        self.LineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.LineEdit.setObjectName("LineEdit")
        self.horizontalLayout.addWidget(self.LineEdit)

        #Botao
        self.btn_alterar = QtWidgets.QPushButton(parent=self.widget)
        self.btn_alterar.setObjectName("btn_alterar")
        self.horizontalLayout.addWidget(self.btn_alterar)
        self.btn_alterar.clicked.connect(self.alterar_texto)

        self.verticalLayout.addLayout(self.horizontalLayout)


        #Label
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def alterar_texto(self):
        texto = self.LineEdit.text()
        self.label.setText(texto)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QtDesignerApp"))
        self.LineEdit.setPlaceholderText(_translate("Form", "Digite o seu texto aqui"))
        self.btn_alterar.setText(_translate("Form", "Alterar Texto"))
        self.label.setText(_translate("Form", "Seu texto Irá aparecer aqui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
