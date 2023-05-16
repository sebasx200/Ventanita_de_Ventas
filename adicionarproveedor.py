import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QFormLayout
from PyQt5 import QtGui, QtCore




class VentanaAdicionar(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(400)
        self.setFixedHeight(300)

        self.setWindowTitle("Añadir información de proveedor")

        self.lnombreProveedor = QLabel("Nombre del proveedor:")
        self.nombreProveedor = QLineEdit()
        self.botonIngresar = QPushButton("Ingresar datos")
        self.botonCancelar = QPushButton("Cancelar")
        self.botonIngresar.setFixedWidth(150)
        self.botonCancelar.setFixedWidth(150)
        self.mensaje = QLabel("")


        layout = QFormLayout()
        layout.addRow(self.lnombreProveedor, self.nombreProveedor)
        layout.addRow(self.botonIngresar, self.botonCancelar)
        layout.addRow(self.mensaje)



        self.setLayout(layout)

        self.botonIngresar.clicked.connect(self.accion_BotonIngresar)
        self.botonCancelar.clicked.connect(self.accion_BotonCancelar)

        self.exec_()

    def accion_BotonIngresar(self):

        self.datosCorrectos = True

        if (self.nombreProveedor.text() == ''):

            self.datosCorrectos = False

            self.mensaje.setText("Los campos están vacíos")

        if self.datosCorrectos:

            if self.datosCorrectos:

                self.file = open('BaseDeDatos/proveedores.txt', 'ab')
                self.file.write(bytes(self.nombreProveedor.text() +"\n", encoding = 'UTF-8'))
                self.file.close()

                self.file = open('BaseDeDatos/proveedores.txt', 'rb')

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    print(linea)
                    if linea == '':
                        break
                self.file.close()


    def accion_BotonCancelar(self):
        self.reject()

