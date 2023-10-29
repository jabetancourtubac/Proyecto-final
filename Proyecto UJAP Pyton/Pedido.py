from Cliente import *
from Inventario import *

class Pedido:

    def __init__(self, inventario):
        nombre = input("\nIngrese el nombre del cliente a registrar: ")
        self.cliente = Cliente(nombre,
                               input(f"\nIngrese la direccion de {nombre}: "),
                               input(f"\nIngrese el correo electronico de {nombre}: "))
        respuesta = "S"
        self.listaProductos = []
        self.costoTotal = 0
        self.resumen = f"\nNombre: {self.cliente.getNombre()}" + f"\nDireccion: {self.cliente.getDireccion()}" + f"\nCorreo Electronico: {self.cliente.getEmail()}\n"

        while respuesta == "S" and len(self.listaProductos) < len(inventario.getProductos()):
            encuentra = False

            while encuentra == False:
                if not encuentra:
                    nombreProducto = input("\nIngrese el nombre Producto: ")

                for i in inventario.getProductos():
                    if (i.getNombre()).upper() == nombreProducto.upper():
                        encuentra = True
                        self.listaProductos.append(i)
                        cantidadProducto = int(input(f"\nCuantos {nombreProducto.capitalize()} desea agregar?: "))
                        while cantidadProducto > i.getCantidad():
                            cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                        self.costoTotal += (i.getPrecio() * cantidadProducto)
                        self.resumen += f"\n* {nombreProducto.capitalize()}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"
                        i.setCantidad(i.getCantidad()-cantidadProducto) # descarga de inventario la cantidad comprada
                        break
                
            respuesta = (input("\nDesea agregar otro producto? (S/N): ")).upper()

            while respuesta != "S" and respuesta != "N":
                respuesta = (input("\nSolo ingrese (S/N): ")).upper()

    def agregarProducto(self, inventario):
        respuesta = "S"
        while respuesta == "S" and len(self.listaProductos) < len(inventario.getProductos()):
            encuentra = False

            while encuentra == False:
                if not encuentra:
                    nombreProducto = input("\nIngrese el nombre Producto: ")

                for i in inventario.getProductos():
                    if (i.getNombre()).upper() == nombreProducto.upper():
                        encuentra = True
                        self.listaProductos.append(i)
                        cantidadProducto = int(input(f"\nCuantos {nombreProducto} desea agregar?: "))
                        while cantidadProducto > i.getCantidad():
                            cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                        self.costoTotal += (i.getPrecio() * cantidadProducto)
                        self.resumen += f"\n* {nombreProducto}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"
                        break

            respuesta = (input("\nDesea agregar otro producto? (S/N): ")).upper()

            while respuesta != "S" and respuesta != "N":

                respuesta = (input("\nSolo ingrese (S/N): ")).upper()

    def setDireccion(self):
        self.cliente.setDireccion(input("\nIngrese la nueva direccion de entrega: "))

    def setEmail(self):
        self.cliente.setEmail(input("Ingrese el nuevo correo electronico: "))

    def getNombreCliente(self):
        return self.cliente.getNombre()
    
    def getResumen(self):
        self.resumen = f"\nNombre: {self.cliente.getNombre()}" + f"\nDireccion: {self.cliente.getDireccion()}" + f"\nCorreo Electronico: {self.cliente.getEmail()}\n"
        
        return self.resumen + f"\n\nTotal = {self.costoTotal}"
    
    def getListaProductos(self):
        return self.listaProductos