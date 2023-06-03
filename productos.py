class Productos:

    def __init__(self,nombreProducto,
                   cantidadComprada,
                   valor,
                   cantidadAlmacen,):

        self.nombreProducto = nombreProducto
        self.cantidadComprada = cantidadComprada
        self.valor = valor
        self.cantidadAlmacen = cantidadAlmacen

    def __str__(self):
        return f"Nombre producto:{self.nombreProducto}"