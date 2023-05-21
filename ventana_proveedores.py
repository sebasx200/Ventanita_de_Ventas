import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QToolBar, QAction, QVBoxLayout, \
    QDialogButtonBox, QDialog, QApplication, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QFormLayout, QScrollArea, \
    QTableWidget, QTableWidgetItem
from PyQt5 import QtGui, QtWidgets, QtCore

import adicionarproveedor

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

            objetoProveedores = Proveedores(lista[0],
                                            lista[1],
                                            lista[2],
                                            lista[3],
                                            lista[4],
                                            )

            self.proveedores.append(objetoProveedores)

        self.file.close()

        self.numeroProveedores = len(self.proveedores)

        self.contador = 0

        self.grid = QtWidgets.QGridLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Proveedores registrados")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: #000000;")




        self.scrollArea = QScrollArea()


        self.scrollArea.setWidgetResizable(True)


        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 160)





        self.tabla.setHorizontalHeaderLabels(['Nombre Proveedor',
                                              'Nombre del producto',
                                              'Cantidad Comprada',
                                              'Valor $',
                                              'Cantidad almacén (Unidad)'])

        # Establece el conteo de objetos por fila
        self.tabla.setRowCount(self.numeroProveedores)

        self.scrollArea.setFixedWidth(780)
        self.scrollArea.setFixedHeight(400)


# Bucle que llena la tabla con los objetos de tipo proveedor

        for p in self.proveedores:

            self.tabla.setItem(self.contador, 0, QTableWidgetItem(p.nombreProveedor))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(p.nombreProducto))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(p.cantidadComprada))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(p.valor))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(p.cantidadAlmacen))

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)

        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(100)

        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.grid.addWidget(self.letrero1, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.scrollArea, 1, 0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.botonVolver, 2, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)


        self.central.setLayout(self.grid)

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
