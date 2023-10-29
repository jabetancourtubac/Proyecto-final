from Tienda import *

opcionGestion=0
tiendaOnline = Tienda()     # Se crea la instancia Tienda
while opcionGestion!=3:     #se mantiene en el menu mientras la respuesta sea N

    opcionGestion = int(input("\nMenú Principal:\n"
                              "\n1- Inventario"
                              "\n2- Clientes"
                              "\n3- Cerrar\n"
                              "\nIngrese el numero de la opcion que desee: "))

    if opcionGestion < 1 or opcionGestion > 3:    #valida que se escojan dentro de los rasgos de menu 
        print ("***Opción no válida***")
        
    if opcionGestion == 1:        #Inventario y su menu 
        opcionInventario=0
        while opcionInventario != 6:
            opcionInventario = int(input("\nMenú Inventario\n"
                                        "\n1- Agregar un producto"
                                        "\n2- Cambiar la cantidad de un producto"
                                        "\n3- Cambiar el precio de un prodcuto"
                                        "\n4- Ver el informe especifico de un producto"
                                        "\n5- Ver el informe general del inventario"
                                        "\n6- Salir\n"
                                        "\nIngrese el numero de la opcion que desee: "))
        
            if opcionInventario < 1 or opcionInventario > 6:     #Valida que este dentro de las opciones
                print("***Opción no válida***")

            #seleccion de opciones
            if opcionInventario == 1:    
                tiendaOnline.agregarProducto()
            elif opcionInventario == 2:
                tiendaOnline.cambiarCantidad()
            elif opcionInventario == 3:
                tiendaOnline.cambiarPrecio()
            elif opcionInventario == 4:
                tiendaOnline.generarInformeEspecifico()
            elif opcionInventario == 5:
                tiendaOnline.generarInformeGeneral()

    elif opcionGestion == 2:
        opcionCliente=0
        while opcionCliente!=3:
            opcionCliente = int(input("\nMenú Clientes:\n"
                                    "\n1- Agregar a un cliente"
                                    "\n2- Gestionar a un cliente"
                                    "\n3- Salir\n"
                                    "\nIngrese el numero de la opcion que desee: "))
            
            if opcionCliente < 1 or opcionCliente > 3:
                print("***Opción Inválida***")
                
            if opcionCliente == 1:
                tiendaOnline.agregarPedido()
            elif opcionCliente==2:
                tiendaOnline.gestionarPedido()
            
print("**** GRACIAS POR USAR NUESTRO SISTEMA DE e-COMMERCE ****")