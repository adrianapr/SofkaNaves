from database import database

class base:
    def __init__(self, nombre, pais_creacion, peso, n_id):
        self.nombre = nombre
        self.pais_creacion = pais_creacion
        self.peso = peso
        self.n_id = n_id
        
    def guardarBaseDatos(self, document):
        database.collection.insert_one(document)
        