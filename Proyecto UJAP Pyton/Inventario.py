from Producto import *

class Inventario:

    def __init__(self):
        
        self.productos = [] # crea una lista de productos donde se ingresan todos los productos que se vayan creando 

    def agregarProducto(self):
        nombre = input("\nIngrese el nombre del producto a agregar: ")
        self.productos.append(Producto(nombre,
                                       float(input(f"\nIngrese el precio de {nombre}: ")),
                                       int(input(f"\nIngrese la cantidad de {nombre}: "))))
        
    def cambiarPrecio(self):
        encuentra = False
        while encuentra == False:   # Sino encuentra el nombre
            nombre = input("\nIngrese el nombre del producto: ")    # Producto a cambiar el precio
            for i in self.productos:    # Recorre la lista para buscar el producto indicado
                if (i.getNombre()).upper() == nombre.upper():   # Realiza comparacion en mayúscula
                    precio = float(input(f"\nIngrese el nuevo precio de {nombre}: "))
                    i.setPrecio(precio)
                    encuentra = True
                    break
            if not encuentra:
                print("Producto no existe... Reintente")

    def cambiarCantidad(self):
        encuentra = False
        while encuentra == False:   # Sino encuentra el nombre
            nombre = input("\nIngrese el nombre del producto: ")
            for i in self.productos:    
                if (i.getNombre()).upper() == nombre.upper():   
                    cantidad = int(input(f"\nIngrese la nueva cantidad de {nombre}: "))
                    i.setCantidad(cantidad)
                    encuentra = True
                    break
            if not encuentra:
                print("Producto no existe... Reintente")

    def generarInformeEspecifico(self):
        encuentra = False
        while encuentra == False:   # Sino encuentra el nombre
            nombre = input("\nIngrese el nombre del producto: ")
            for i in self.productos:
                if (i.getNombre()).upper() == nombre.upper():
                    print(f"\nProducto: {i.getNombre()}"
                        f"\nPrecio: {i.getPrecio()}"
                        f"\nCantidad: {i.getCantidad()}")
                    encuentra = True
                    break
            if not encuentra:
                print("Producto no existe... Reintente")
            a=input()

    def generarInformeGeneral(self):
        print("\nInforme General del Inventario: ")
        numero = 1  #contador de itens 
        for i in self.productos:
            print(f"\n{numero})  Nombre: {i.getNombre()}"
                  f"\n    Precio: {i.getPrecio()}"
                  f"\n    Cantidad: {i.getCantidad()}")
            numero += 1
        numero=input()
    
    def getProductos(self):
        return self.productos