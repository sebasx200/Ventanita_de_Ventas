import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QApplication, QVBoxLayout, QPushButton
from PyQt5 import QtGui, QtCore, QtWidgets
from ventana_principal import Ventana_Principal

class Ventana_Inicio(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana_Inicio, self).__init__(parent)

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

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/Logo-PPI.jpeg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)




        self.grid = QtWidgets.QGridLayout()

        self.letreroBienvenida = QLabel("Bienvenidos a")
        self.letreroBienvenida.setStyleSheet("background-color: #BFEFFF; color: #000000; border:solid; border-width:1px; border-color: FF0000;"
                                    "border-radius:10px;")
        self.letreroBienvenida.setFont(QFont("Comic Sans MS", 20))



        self.botonComenzar = QPushButton()
        self.botonComenzar.setText("Comenzar")
        self.botonComenzar.setStyleSheet("background-color: #CAE1FF; color: red; margin-bottom: 10px; border:solid; border-width:1px; border-color: FF0000;")
        self.botonComenzar.setFont(QFont("Comic Sans MS", 15))
        self.botonComenzar.setFixedWidth(250)

        self.botonComenzar.clicked.connect(self.accion_BotonComenzar)


        self.grid.addWidget(self.botonComenzar, 0, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.letreroBienvenida, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.setContentsMargins(70, 0, 0, 0)


        self.fondo.setLayout(self.grid)

    def accion_BotonComenzar(self):
        print("1")
<<<<<<< HEAD
        
=======
        self.hide()
        self.ventana_principal = Ventana_Principal()
        self.ventana_principal.show()

>>>>>>> bc79b39ffade0ae3ff93eaeabe340fc52be251f9

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana_inicio = Ventana_Inicio()

    # hacer que el objeto ventana1 se vea
    ventana_inicio.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())


