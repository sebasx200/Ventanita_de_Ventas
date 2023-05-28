from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QTableWidget, QAction, QToolBar, QMainWindow
from PyQt5 import QtCore, QtWidgets


class VentanaItemProveedor(QDialog):

    def __init__(self, item, parent=None):
        super().__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.elementoTabla = item

        self.setWindowTitle("Proveedor " + self.elementoTabla)

        self.setFixedWidth(1000)
        self.setFixedHeight(600)

        self.barradeProductos = QToolBar("Barra de productos")
        self.barradeProductos.setIconSize(QSize(50, 50))


        self.añadir = QAction(QIcon("imagenes/add.png"), "Añadir proveedor", self)
        self.barradeProductos.addAction(self.añadir)

        self.modificar = QAction(QIcon("imagenes/editar.png"), "Modificar proveedor", self)
        self.barradeProductos.addAction(self.modificar)

        self.eliminar = QAction(QIcon("imagenes/eliminar.png"), "Eliminar proveedor", self)
        self.barradeProductos.addAction(self.eliminar)

        self.barradeProductos.actionTriggered[QAction].connect(self.accion_barradeProductos)

        self.grid = QtWidgets.QGridLayout()




        self.letrero1 = QLabel()

        self.letrero1.setText("Productos registrados de " + self.elementoTabla)
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




        self.scrollArea.setFixedWidth(610)
        self.scrollArea.setFixedHeight(400)
        self.scrollArea.setWidget(self.tabla)

        self.grid.addWidget(self.barradeProductos, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.letrero1, 1, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.scrollArea, 2, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)



        self.setLayout(self.grid)

        self.exec_()


    def accion_barradeProductos(self, opcion):
        pass

