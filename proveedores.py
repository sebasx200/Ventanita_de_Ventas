class Proveedores:

    def __init__(self, nombreProveedor,
                   nombreProducto,
                   cantidadComprada,
                   valor,
                   cantidadAlmacen,):

        self.nombreProveedor = nombreProveedor
        self.nombreProducto = nombreProducto
        self.cantidadComprada = cantidadComprada
        self.valor = valor
        self.cantidadAlmacen = cantidadAlmacen

    def __str__(self):
        return f"Nombre:{self.nombreProveedor}"