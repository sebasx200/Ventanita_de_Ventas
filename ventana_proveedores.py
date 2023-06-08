import itertools
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap, QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QToolBar, QAction, QVBoxLayout, \
    QDialogButtonBox, QDialog, QApplication, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QFormLayout, QScrollArea, \
    QTableWidget, QTableWidgetItem, QMessageBox, QCheckBox, QTextBrowser
from PyQt5 import QtGui, QtWidgets, QtCore

import ventana_productos
import proveedores
from productos import Productos
from ventana_productos import Ventana_Productos
from proveedores import Proveedores
from PyQt5.QtCore import pyqtSignal



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

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondopantalla.jpeg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setCentralWidget(self.fondo)


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

            # obtenemos del string una lista con 4 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            print(lista)
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u

            self.objetoProveedores = Proveedores(lista[0],
                                            )
            self.proveedores.append(self.objetoProveedores)

        self.file.close()


        self.fileP = open('BaseDeDatos/productos.txt', 'rb')

        self.productos = []

        linea = self.fileP.readline().decode('UTF-8').strip()

        while linea:

            if linea == '':

                self.productos.append([])

            else:
                lista = linea.split(";")

                self.objetoProductos = Productos(lista[0],
                                            lista[1],
                                            lista[2],
                                            lista[3],
                                            )

                self.productos.append(self.objetoProductos)
            linea = self.fileP.readline().decode('UTF-8').strip()

        self.fileP.close()

        self.dProveedores = {}

        for nProveedor, datosProveedor in zip(self.proveedores, self.productos):
            if datosProveedor:
                self.dProveedores[nProveedor.nombreProveedor] = [datosProveedor.nombreProducto], [datosProveedor.cantidadComprada], [datosProveedor.valor], [datosProveedor.cantidadAlmacen]

        nombre_proveedor = 'Coca cola'
        nombre_producto = 'Nuevo Producto'
        cantidad_comprada = 10
        valor = 100

        # Verificar si la clave existe en el diccionario
        if nombre_proveedor in self.dProveedores:
            # La clave existe, agregar los datos del nuevo producto a la lista de valores
            self.dProveedores[nombre_proveedor][0].append(nombre_producto)
            self.dProveedores[nombre_proveedor][1].append(cantidad_comprada)
            self.dProveedores[nombre_proveedor][2].append(valor)
        else:
            # La clave no existe, mostrar un mensaje de error o realizar alguna acción de manejo de errores
            print('La clave no existe en el diccionario')

        # Verificar si el cambio se reflejó en el diccionario
        print(self.dProveedores)

        self.grid = QtWidgets.QGridLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Proveedores registrados")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: #000000; margin-bottom: 15px")

        self.letrero2 = QLabel()

        self.letrero2.setText("Para ver los productos de cada proveedor, haga doble clic en el proveedor para ver más detalles")
        self.letrero2.setFont(QFont("Arial", 13))
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 15px")

        self.botonVerProductos = QPushButton("Ver productos")
        self.botonVerProductos.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )
        self.botonVerProductos.setFixedWidth(100)
        self.botonVerProductos.clicked.connect(self.accion_botonVerProductos)


        self.botonAdd = QPushButton("Aceptar")
        self.botonAdd.setStyleSheet("background-color : #FFFFFF;"
                                             "color : #000000;"
                                             "padding: 10 px;"
                                             )
        self.botonAdd.setFixedWidth(100)
        self.botonAdd.clicked.connect(self.accion_botonAdd)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.clicked.connect(self.accion_botonVolver)


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


        self.scrollArea.setFixedWidth(780)
        self.scrollArea.setFixedHeight(400)


        self.accion_llenarTabla()




        self.tabla.itemDoubleClicked.connect(self.accion_itemClic)


        self.scrollArea.setWidget(self.tabla)

        #self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)




        self.grid.addWidget(self.letrero1, 0, 0, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.grid.addWidget(self.letrero2, 1, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        self.grid.addWidget(self.scrollArea, 2, 0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.botonVolver, 3, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        self.grid.addWidget(self.botonVerProductos, 3, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.grid.addWidget(self.botonAdd, 4, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)




        self.fondo.setLayout(self.grid)
        print(self.dProveedores)

    def accion_llenarTabla(self):

        conteoFilas = self.tabla.rowCount()

        for p in self.proveedores:

            self.tabla.insertRow(conteoFilas)

            itemProveedor = QTableWidgetItem(p.nombreProveedor)
            self.tabla.setItem(conteoFilas, 0, itemProveedor)

            datosDiccionario = self.dProveedores.setdefault(p.nombreProveedor, [])

            maxAltura = 0  # Variable para almacenar la altura máxima de la fila

            for i, valores in enumerate(datosDiccionario):
                # Combinar los valores en una sola cadena, separados por salto de línea
                valores_concatenados = "\n".join(str(valor) for valor in valores)

                item = QTableWidgetItem(valores_concatenados)
                self.tabla.setItem(conteoFilas, i + 1, item)

                # Calcular la altura necesaria en función de la cantidad de elementos en la lista
                altura = len(valores) * self.tabla.rowHeight(conteoFilas)
                maxAltura = max(maxAltura, altura)

            self.tabla.setRowHeight(conteoFilas, maxAltura)

            conteoFilas += 1

    def accion_itemClic(self, itemclic):

        elementoSelecciondo = itemclic.tableWidget().item(itemclic.row(), 0).text()
        self.ventanaProductos = Ventana_Productos(self, self.dProveedores, elementoSelecciondo)
        self.ventanaProductos.show()



    def accion_barradeProveedores(self, opcion):


        if opcion.text() == "Añadir proveedor":

            ultimaFila = self.tabla.rowCount()

            self.tabla.insertRow(ultimaFila)

            self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
            self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
            self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
            self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))
            self.tabla.setItem(ultimaFila, 4, QTableWidgetItem(''))

        if opcion.text() == "Eliminar proveedor":

            filaActual = self.tabla.currentRow()


            if filaActual <0:

                mensajeAdvertencia = QMessageBox.warning(self, 'Advertencia', 'Debe seleccionar un proveedor para eliminarlo')
                return mensajeAdvertencia

            mensajeConfirmacion = QMessageBox.question(self, 'Confirmación', '¿Está seguro/a de eliminar este proveedor?',
                                                       QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)

            if mensajeConfirmacion == QMessageBox.StandardButton.Ok:

                if (
                        self.tabla.item(filaActual, 0).text() != '' and
                        self.tabla.item(filaActual, 1).text() != '' and
                        self.tabla.item(filaActual, 2).text() != '' and
                        self.tabla.item(filaActual, 3).text() != '' and
                        self.tabla.item(filaActual, 4).text() != ''
                ):

                    for p in self.proveedores:
                        if (
                                p.nombreProveedor == self.tabla.item(filaActual, 0).text()
                        ):
                            self.proveedores.remove(p)

                            break

                    self.file = open('BaseDeDatos/proveedores.txt', 'wb')

                    for p in self.proveedores:
                        self.file.write(bytes(p.nombreProveedor + ";\n"
                                              , encoding='UTF-8'))
                    self.file.close()

                    self.tabla.removeRow(filaActual)

                    return QMessageBox.question(
                        self,
                        'Confirmation',
                        'El registro ha sido eliminado exitosamente.',
                        QMessageBox.StandardButton.Ok
                    )
                else:

                    self.tabla.removeRow(filaActual)



        if opcion.text() == "Modificar proveedor":

            filaActual = self.tabla.currentRow()

            if filaActual < 0:
                return QMessageBox.warning(self, 'Advertencia', 'Para editar, debe seleccionar un registro')

            boton = QMessageBox.question(
                self,
                'Confirmación',
                '¿Está seguro de que quiere editar este registro?',
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No
            )
            if boton == QMessageBox.StandardButton.Ok:
                nombreProveedorActualizado = self.tabla.item(filaActual, 0).text()

                with open('BaseDeDatos/proveedores.txt', 'r', encoding='UTF-8') as archivo:
                    lineas = archivo.readlines()

                with open('BaseDeDatos/proveedores.txt', 'w', encoding='UTF-8') as archivo:
                    for i, linea in enumerate(lineas):
                        if i == filaActual:
                            archivo.write(nombreProveedorActualizado + ";\n")
                        else:
                            archivo.write(linea)

                QMessageBox.question(
                    self,
                    'Confirmación',
                    'Los datos del registro se han editado exitosamente.',
                    QMessageBox.StandardButton.Ok
                )

    def accion_botonAdd(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, 'Advertencia', 'Para ingresar, debe seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'Confirmación',
            '¿Está seguro de que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Ok:
            if (
                    self.tabla.item(filaActual, 0).text() != ''
            ):
                datosVacios = False

                existeRegistro = False

                existeProveedor = False

                for p in self.proveedores:
                    if (
                            p.nombreProveedor == self.tabla.item(filaActual, 0).text()

                    ):
                        existeProveedor = True

                        return QMessageBox.warning(self, 'Advertencia', 'Registro duplicado, no se puede registrar')

                        break

                    if not existeProveedor:

                        self.file = open('BaseDeDatos/proveedores.txt', 'ab')

                        self.file.write(bytes(self.tabla.item(filaActual, 0).text() + ";""\n"
                                              , encoding='UTF-8'))
                        self.file.seek(0, 2)
                        self.file.close()

                    return QMessageBox.question(
                        self,
                        'Confirmación',
                        'Los datos del registro se han ingresado exitosamente.',
                        QMessageBox.StandardButton.Ok
                    )

            if datosVacios:
                return QMessageBox.warning(self, 'Advertencia', 'Debe ingresar todos los datos en el registro')

    def accion_botonVolver(self):

        self.hide()
        self.ventanaAnterior.show()

    def accion_botonVerProductos(self):

        item=None
        self.hide()
        self.ventanaProductos = Ventana_Productos(self, self.dProveedores, item)
        self.ventanaProductos.show()




if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana_proveedores = Ventana_Proveedores(anterior=None)



    # hacer que el objeto ventana1 se vea
    ventana_proveedores.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())
