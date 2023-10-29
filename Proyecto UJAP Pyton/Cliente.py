class Cliente:

    def __init__(self, nombre, dirceccion, email):
        self.nombre = nombre
        self.direccion = dirceccion
        self.email = email

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setEmail(self, email):
        self.email = email

    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getEmail(self):
        return self.email