from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QTableWidget, QAction, QToolBar, QMainWindow, \
    QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtWidgets

import adicionar_proveedor
from productos import Productos


class VentanaItemProveedor(QDialog):

    def __init__(self, itemSeleccionado, parent=None):
        super().__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.elementoTabla = itemSeleccionado
        self.setWindowTitle("Proveedor " + str(self.elementoTabla))

        self.setFixedWidth(1000)
        self.setFixedHeight(600)

        self.barradeProductos = QToolBar("Barra de productos")
        self.barradeProductos.setIconSize(QSize(50, 50))


        self.añadir = QAction(QIcon("imagenes/add.png"), "Añadir producto", self)
        self.barradeProductos.addAction(self.añadir)

        self.modificar = QAction(QIcon("imagenes/editar.png"), "Modificar producto", self)
        self.barradeProductos.addAction(self.modificar)

        self.eliminar = QAction(QIcon("imagenes/eliminar.png"), "Eliminar producto", self)
        self.barradeProductos.addAction(self.eliminar)

        self.barradeProductos.actionTriggered[QAction].connect(self.accion_barradeProductos)

        self.file = open('BaseDeDatos/productos.txt', 'rb')

        self.productos = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 4 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            print(linea)
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u

            objetoProductos = Productos(lista[0],
                                            lista[1],
                                            lista[2],
                                            lista[3],
                                            )

            self.productos.append(objetoProductos)

        self.file.close()

        self.numeroProductos = len(self.productos)

        self.grid = QtWidgets.QGridLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Productos registrados de " + str(self.elementoTabla))
        self.letrero1.setFont(QFont("Arial", 15))
        self.letrero1.setStyleSheet("color: #000000; margin-bottom: 15px")


        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 155)


        self.tabla.setHorizontalHeaderLabels(['Nombre del producto',
                                              'Cantidad comprada',
                                              'Valor $',
                                              'Cantidad almacén (Unidad)'])




        self.scrollArea.setFixedWidth(620)
        self.scrollArea.setFixedHeight(400)
        self.contador = 0

        for p in self.productos:

            self.tabla.setItem(self.contador, 0, QTableWidgetItem(p.nombreProducto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(p.cantidadComprada))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(p.valor))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(p.cantidadAlmacen))


            self.contador += 1

        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)



        self.scrollArea.setWidget(self.tabla)

        self.grid.addWidget(self.barradeProductos, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.letrero1, 1, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.scrollArea, 2, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)



        self.setLayout(self.grid)




    def accion_barradeProductos(self, opcion):


        if opcion.text() == "Añadir producto":

            adicionar_proveedor.VentanaAdicionarProducto(self)
