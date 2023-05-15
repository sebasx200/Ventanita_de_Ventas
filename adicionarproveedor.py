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

        layout = QFormLayout()
        layout.addRow(self.lnombreProveedor, self.nombreProveedor)
        layout.addRow(self.botonIngresar, self.botonCancelar)


        self.setLayout(layout)

        self.botonIngresar.clicked.connect(self.accion_BotonIngresar)
        self.botonCancelar.clicked.connect(self.accion_BotonCancelar)

        self.exec_()

    def accion_BotonIngresar(self):
        self.close()


    def accion_BotonCancelar(self):
        self.reject()

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventanaAdicionar = VentanaAdicionar()


    # hacer que el objeto ventana1 se vea
    ventanaAdicionar.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
