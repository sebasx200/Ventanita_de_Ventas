from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from proveedores import Proveedores


class Adicionar_Proveedor(QDialog):

    def __init__(self, parent=None):
        super(Adicionar_Proveedor, self).__init__(parent)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.ancho = 400
        self.alto = 300

        self.setWindowTitle("Añadir proveedor")

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.resize(self.ancho, self.alto)

        self.formulario = QFormLayout()

        self.letrero1 = QLabel("Añadir proveedor al registro")
        self.letrero1.setFont(QFont("Arial", 10))
        self.letrero1.setStyleSheet("color: #000000; margin-bottom: 10px")

        self.mensaje = QLabel("")
        self.mensaje.setFont(QFont("Arial", 13))
        self.mensaje.setStyleSheet("color: red; margin-top: 15px")

        self.lnomProv = QLabel("Nombre del proveedor *")
        self.lnomProv.setStyleSheet("color: #000000; margin-bottom: 10px")
        self.nomProv = QLineEdit()

        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(100)
        self.botonIngresar.setStyleSheet("background-color : #FFFFFF;"
                                         "color : #000000;"
                                         "padding: 10 px; margin-top: 8px"
                                         )
        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        self.botonCancelar = QPushButton("Cancelar")
        self.botonCancelar.setFixedWidth(100)
        self.botonCancelar.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px; margin-top: 8px"
                                       )
        self.botonCancelar.clicked.connect(self.accion_botonCancelar)



        self.formulario.addRow(self.letrero1)

        self.formulario.addRow(self.lnomProv, self.nomProv)
        self.formulario.addRow(self.botonIngresar, self.botonCancelar)
        self.formulario.addWidget(self.mensaje)

        self.setLayout(self.formulario)


    def accion_botonIngresar(self):

        self.file = open('BaseDeDatos/proveedores.txt', 'rb')

        proveedores = []

        while self.file:

            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 4 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            print(lista)
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u

            objetoProveedores = Proveedores(lista[0],
                                                 )
            proveedores.append(objetoProveedores)

        self.file.close()

        existeRegistro = False
        datosCorrectos = True
        prov = ''

        for p in proveedores:

            prov = p.nombreProveedor

            if self.nomProv.text().lower().strip() == prov.lower().strip():

                existeRegistro = True

                return QMessageBox.warning(self, 'Advertencia', 'Registro duplicado, no se puede registrar')
                break


        if self.nomProv.text() == '':

            datosCorrectos = False

            self.mensaje.setText("Por favor llenar todos los campos")

        if datosCorrectos and not existeRegistro:

            self.file = open('BaseDeDatos/proveedores.txt', 'ab')

            self.file.write(bytes(self.nomProv.text() + ";" + "\n"
                                  , encoding='UTF-8'))
            self.file.seek(0, 2)
            self.file.close()

            return QMessageBox.question(
                self,
                'Confirmación',
                'El nuevo proveedor se ha ingresado correctamente.',
                QMessageBox.StandardButton.Ok
            )


    def accion_botonCancelar(self):
        self.reject()
