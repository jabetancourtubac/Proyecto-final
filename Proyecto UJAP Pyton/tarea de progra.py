

class Producto:
    def _init_(self, nombre, precio, cantidad_en_inventario):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_inventario = cantidad_en_inventario

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def obtener_cantidad_en_inventario(self):
        return self.cantidad_en_inventario

    def establecer_cantidad_en_inventario(self, nueva_cantidad):
        self.cantidad_en_inventario = nueva_cantidad


class Inventario:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def actualizar_cantidad(self, nombre_producto, nueva_cantidad):
        for producto in self.productos:
            if producto.obtener_nombre() == nombre_producto:
                producto.establecer_cantidad_en_inventario(nueva_cantidad)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.obtener_nombre() == nombre_producto:
                return producto
        return None

    def generar_informe(self):
        informe = []
        for producto in self.productos:
            informe.append(f"Producto: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}, Cantidad en inventario: {producto.obtener_cantidad_en_inventario()}")
        return informe


class Cliente:
    def _init_(self, nombre, direccion, correo_electronico):
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_direccion(self):
        return self.direccion

    def establecer_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def obtener_correo_electronico(self):
        return self.correo_electronico

    def establecer_correo_electronico(self, nuevo_correo_electronico):
        self.correo_electronico = nuevo_correo_electronico


class Pedido:
    def _init_(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.obtener_precio() * cantidad
        self.total = total

    def generar_resumen(self):
        resumen = f"Cliente: {self.cliente.obtener_nombre()}\n"
        resumen += "Productos en el pedido:\n"
        for producto, cantidad in self.productos:
            resumen += f"- Producto: {producto.obtener_nombre()}, Cantidad: {cantidad}, Precio Unitario: ${producto.obtener_precio()}\n"
        resumen += f"Total del pedido: ${self.total}\n"
        return resumen


class Tienda:
    def _init_(self):
        self.inventario = Inventario()
        self.clientes = []

    def gestionar_inventario(self):
        # Métodos para gestionar el inventario (agregar productos, actualizar cantidades, buscar productos, generar informes)
        pass

    def gestionar_clientes(self):
        # Métodos para gestionar los clientes (registrar nuevos clientes, buscar clientes)
        pass


# Ejemplo de uso del sistema:
if _name_ == "_main_":
    tienda = Tienda()

    # Agregar productos al inventario
    producto1 = Producto("Producto1", 10.0, 100)
    producto2 = Producto("Producto2", 15.0, 50)
    tienda.inventario.agregar_producto(producto1)
    tienda.inventario.agregar_producto(producto2)

    # Registrar un cliente
    cliente1 = Cliente("Cliente1", "Dirección1", "cliente1@example.com")
    tienda.clientes.append(cliente1)

    # Crear un pedido para el cliente
    pedido = Pedido(cliente1)
    pedido.agregar_producto(producto1, 3)
    pedido.agregar_producto(producto2, 2)
    pedido.calcular_total()

    # Generar un resumen del pedido
    resumen_pedido = pedido.generar_resumen()
    print(resumen_pedido)

    # Generar un informe del inventario
    informe_inventario = tienda.inventario.generar_informe()
    for producto_info in informe_inventario:
        print(producto_info)