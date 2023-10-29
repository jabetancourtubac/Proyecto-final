class Producto:

    def __init__(self, nombre, precio, cantidad):   # el __init__ crea el objeto instanciandolo en la variable que lo invoca
        self.nombre = nombre                        
        self.precio = precio
        self.cantidad = cantidad

    def setPrecio(self, precio):    # Actualiza precio
        self.precio = precio

    def setCantidad(self, cantidad):    #Actualiza cantidad
        self.cantidad = cantidad

    def getNombre(self):    # Obtiene Nombre
        return self.nombre
    
    def getPrecio(self):    # Obtiene precio
        return self.precio
    
    def getCantidad(self):  # Obtiene Cantidad
        return self.cantidad