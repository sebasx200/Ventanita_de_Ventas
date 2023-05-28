import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QFormLayout
from PyQt5 import QtGui, QtCore, Qt




class VentanaAdicionar(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.setFixedWidth(400)
        self.setFixedHeight(300)

        self.setWindowTitle("Añadir información de proveedor")

        self.lnombreProveedor = QLabel("Nombre de la empresa:")
        self.nombreProveedor = QLineEdit()
        self.lnombreProducto = QLabel("Producto:")
        self.nombreProducto = QLineEdit()
        self.lcantidadComprada = QLabel("Cantidad comprada")
        self.cantidadComprada = QLineEdit()
        self.lValor = QLabel("Valor")
        self.valor = QLineEdit()
        self.lCantidadAlmacen = QLabel("Cantidad en almacén")
        self.cantidadAlmacen = QLineEdit()
        self.botonIngresar = QPushButton("Ingresar datos")
        self.botonCancelar = QPushButton("Cancelar")
        self.valor.setFixedWidth(100)
        self.cantidadComprada.setFixedWidth(100)
        self.cantidadAlmacen.setFixedWidth(100)
        self.botonIngresar.setFixedWidth(120)
        self.botonCancelar.setFixedWidth(120)
        self.mensaje = QLabel("")


        layout = QFormLayout()
        layout.addRow(self.lnombreProveedor, self.nombreProveedor)
        layout.addRow(self.lnombreProducto, self.nombreProducto)
        layout.addRow(self.lcantidadComprada, self.cantidadComprada)
        layout.addRow(self.lValor, self.valor)
        layout.addRow(self.lCantidadAlmacen, self.cantidadAlmacen)

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
                self.file.write(bytes(self.nombreProveedor.text() + ";"
                                      + self.nombreProducto.text() + ";"
                                      + self.cantidadComprada.text() + ";"
                                      + self.valor.text() + ";"
                                      + self.cantidadAlmacen.text() + ";" + "\n"
                                      , encoding = 'UTF-8'))
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
