import nave

class nave3(nave.base):
    def __init__(self,nombre, pais_creacion, peso, n_id, capacidad_personas, capacidad_orbita):
        super().__init__(nombre, pais_creacion, peso, n_id)
        self.capacidad_personas = capacidad_personas
        self.capacidad_orbita = capacidad_orbita
        self.tipo_nave = "Nave espacial tripulada"
