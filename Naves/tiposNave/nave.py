from database import database

class base:
    def __init__(self, nombre, pais_creacion, peso, _id):
        self.nombre = nombre
        self.pais_creacion = pais_creacion
        self.peso = peso
        self._id = _id

    def guardar(self): 
        database.guardarBaseDatos(self.__dict__)