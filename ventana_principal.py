import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QLabel, QToolBar, QAction, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets


class Ventana_Principal(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana_Principal, self).__init__(parent)



        self.ancho = 1000
        self.alto = 700
        self.setWindowTitle("Ventanita de Ventas")
        self.setStyleSheet('background-color: #ABE8EF')
        self.resize(self.ancho, self.alto)
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondoventanaprincipal.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.grid = QtWidgets.QGridLayout()

        self.letreroBienvenida = QLabel("Con qué quiere empezar")
        self.letreroBienvenida.setStyleSheet(
            "background-color: white; color: #000000; border:solid; border-width:1px; border-color: FF0000;"
            "border-radius:10px;")
        self.letreroBienvenida.setFont(QFont("Comic Sans MS", 20))

        self.fondo.setLayout(self.grid)
        self.grid.addWidget(self.letreroBienvenida, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)








if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana_principal = Ventana_Principal()


    # hacer que el objeto ventana1 se vea
    ventana_principal.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
