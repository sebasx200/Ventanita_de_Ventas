from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtWidgets, QtCore


class Ventana_Estadisticas(QMainWindow):

    def __init__(self, anterior):
        super(Ventana_Estadisticas, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Ventanita De Ventas: Estadísticas")

        self.setWindowIcon(QtGui.QIcon("imagenes/Logo-PPI.jpeg"))
        self.ancho = 1200
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondopantalla.jpeg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setCentralWidget(self.fondo)

        self.grid = QtWidgets.QGridLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Estadísticas")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: #000000; margin-bottom: 15px")

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.grid.addWidget(self.letrero1, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.botonVolver, 1, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)

        self.fondo.setLayout(self.grid)

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()