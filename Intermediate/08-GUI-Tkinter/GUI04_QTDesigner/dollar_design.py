from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 429)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(121, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 60, 373, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtMontoSoles = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtMontoSoles.setGeometry(QtCore.QRect(230, 109, 291, 31))
        self.txtMontoSoles.setObjectName("txtMontoSoles")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(370, 179, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.txtTipoCambio = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtTipoCambio.setGeometry(QtCore.QRect(230, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txtTipoCambio.setFont(font)
        self.txtTipoCambio.setObjectName("txtTipoCambio")
        self.btnCambiar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCambiar.setGeometry(QtCore.QRect(90, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btnCambiar.setFont(font)
        self.btnCambiar.setStyleSheet("QPushButton{\n"
"    background-color: #4CAF50; /* Verde */\n"
"    color: white; /* Texto en blanco */\n"
"    border-radius: 10px; /* Bordes redondeados opcionales  */\n"
"border: 2px solid  #4CAF50 ; /* Borde */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Cambiar el color al pasa el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41; /* Cambiar el color al hacer click */\n"
"}")
        self.btnCambiar.setObjectName("btnCambiar")
        self.txtTipoCambio_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtTipoCambio_2.setGeometry(QtCore.QRect(230, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txtTipoCambio_2.setFont(font)
        self.txtTipoCambio_2.setObjectName("txtTipoCambio_2")
        self.txtMontoObtenido = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtMontoObtenido.setGeometry(QtCore.QRect(370, 290, 151, 31))
        self.txtMontoObtenido.setObjectName("txtMontoObtenido")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CAMBIO DE DOLARES"))
        self.label.setText(_translate("MainWindow", "Módulo de Cambio de Moneda Extranjera"))
        self.label_2.setText(_translate("MainWindow", "Monto en Soles"))
        self.txtTipoCambio.setText(_translate("MainWindow", "Tipo de Cambio"))
        self.btnCambiar.setText(_translate("MainWindow", "Convertir"))
        self.txtTipoCambio_2.setText(_translate("MainWindow", "Monto Obtenido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
