import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QToolBar, QAction, QVBoxLayout, \
    QDialogButtonBox, QDialog, QApplication, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QFormLayout, QScrollArea, \
    QTableWidget, QTableWidgetItem
from PyQt5 import QtGui, QtWidgets, QtCore

import adicionarproveedor
from adicionarproveedor import VentanaAdicionar
from proveedores import Proveedores



class Ventana_Proveedores(QMainWindow):

    def __init__(self, anterior):
        super(Ventana_Proveedores, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Ventanita De Ventas: Proveedores")

        self.setWindowIcon(QtGui.QIcon("imagenes/Logo-PPI.jpeg"))
        self.ancho = 1200
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.central = QWidget()
        self.setCentralWidget(self.central)



        self.barradeProveedores = QToolBar("Barra de proveedores")
        self.barradeProveedores.setIconSize(QSize(50, 50))
        self.addToolBar(self.barradeProveedores)

        self.añadir = QAction(QIcon("imagenes/add.png"), "Añadir proveedor", self)
        self.barradeProveedores.addAction(self.añadir)

        self.modificar = QAction(QIcon("imagenes/editar.png"), "Modificar proveedor", self)
        self.barradeProveedores.addAction(self.modificar)

        self.eliminar = QAction(QIcon("imagenes/eliminar.png"), "Eliminar proveedor", self)
        self.barradeProveedores.addAction(self.eliminar)

        self.barradeProveedores.actionTriggered[QAction].connect(self.accion_barradeProveedores)

        self.file = open('BaseDeDatos/proveedores.txt', 'rb')

        self.proveedores = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u

            objetoProveedores = Proveedores(lista[0])

            self.proveedores.append(objetoProveedores)

        self.file.close()

        self.numeroProveedores = len(self.proveedores)

        self.contador = 0

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Proveedores registrados")
        self.letrero1.setFont(QFont("Comic Sans MS", 20))
        self.letrero1.setStyleSheet("color: #000000;")

        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()


        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)


        self.tabla.setHorizontalHeaderLabels(['Nombre Proveedor'])
        self.tabla.setRowCount(self.numeroProveedores)

        for p in self.proveedores:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(objetoProveedores.nombreProveedor))
            self.contador += 1

        self.scrollArea.setWidget(self.tabla)

        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(100)

        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        self.central.setLayout(self.vertical)

    def accion_barradeProveedores(self, opcion):


        if opcion.text() == "Añadir proveedor":

            adicionarproveedor.VentanaAdicionar(self)

    def accion_botonVolver(self):

        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana_proveedores = Ventana_Proveedores(anterior=None)


    # hacer que el objeto ventana1 se vea
    ventana_proveedores.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
