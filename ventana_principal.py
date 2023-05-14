import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QLabel, QToolBar, QAction, QWidget, \
    QDesktopWidget
from PyQt5 import QtGui, QtCore, QtWidgets



class Ventana_Principal(QMainWindow):

    def __init__(self, anterior):
        super(Ventana_Principal, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Ventanita De Ventas")

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

        self.grid = QtWidgets.QGridLayout()

        self.letrero1 = QLabel ("Con qué quieres empezar")

        self.botonProveedores = QPushButton("Proveedores")
        self.botonProveedores.clicked.connect(self.accion_botonProveedores)

        self.botonEstadisticas = QPushButton("Estadísticas")
        self.botonEstadisticas.clicked.connect(self.accion_botonEstadisticas)

        self.botonBuscar = QPushButton("Búsquedas")
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        self.botonVolver = QPushButton("Volver al inicio")
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.grid.addWidget(self.letrero1, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.botonProveedores, 1, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.botonEstadisticas, 2, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.botonBuscar, 3, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.botonVolver, 4, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)



        self.central.setLayout(self.grid)



    def accion_botonProveedores(self):
        print("1")

    def accion_botonEstadisticas(self):
        print("2")

    def accion_botonBuscar(self):
        print("3")

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()




if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana_principal = Ventana_Principal()


    # hacer que el objeto ventana1 se vea
    ventana_principal.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
