from Inventario import *
from Pedido import *

class Tienda:

    def __init__(self):

        self.inventario = Inventario()      #crea la instancia con la clase inventario

        self.listaPedidos = []         # se inicializa una lista de pedidos 

    def agregarPedido(self):
        if len(self.inventario.getProductos()) >= 1:    #valida que hayan productos
            self.listaPedidos.append(Pedido(self.inventario))
        else:
            print("\nNo hay productos en el inventario.")

    def gestionarPedido(self):
        if len(self.listaPedidos) >= 1:
            opcion=0
            encuentra = False
            while opcion!=5:
                if not encuentra:
                    nombreCliente = input("\nIngrese el nombre del cliente que busca: ")

                for i in self.listaPedidos:
                    if nombreCliente.upper() == (i.getNombreCliente()).upper():
                        opcion = int(input("\nGestionar a un cliente\n"
                                        + "\n1- Agregar Productos"
                                        + "\n2- Ver Resumen"
                                        + "\n3- Cambiar la direccion"
                                        + "\n4- Cambiar el e-mail"
                                        + "\n5- Salir\n"
                                        + "\nIngrese el numero de la opcion que desee realizar: "))

                        if opcion < 1 or opcion > 5:
                            print("***Opción no válida***")

                        if opcion == 1:
                            if len(i.getListaProductos()) < len(self.inventario.getProductos()):
                                i.agregarProducto(self.inventario)
                            else:
                                print("\nNo hay mas productos que agregar.")

                        elif opcion == 2:
                            print(i.getResumen())
                            a=input()

                        elif opcion == 3:
                            i.setDireccion()

                        elif opcion == 4:
                            i.setEmail()

                        encuentra = True
                        break

                if encuentra == False:
                    print("***Cliente NO registrado***\n")
                    a=input()
        else:
            print("\nNo hay Pedidos registrados.")
            a=input()

    def agregarProducto(self):    #el self se usa por convencion y hace referencia al objeto de la clase 
        self.inventario.agregarProducto()

    def cambiarCantidad(self):
        if len(self.inventario.getProductos()) >= 1:
            self.inventario.cambiarCantidad()
        else:
            print("\nNo hay productos en el inventario.")

    def cambiarPrecio(self):
        if len(self.inventario.getProductos()) >= 1:
            self.inventario.cambiarPrecio()
        else:
            print("\nNo hay productos en el inventario.")

    def generarInformeEspecifico(self):
        if len(self.inventario.getProductos()) >= 1:
            self.inventario.generarInformeEspecifico()
        else:
            print("\nNo hay productos en el inventario.")

    def generarInformeGeneral(self):
        if len(self.inventario.getProductos()) >= 1:
            self.inventario.generarInformeGeneral()
        else:
            print("\nNo hay productos en el inventario.")