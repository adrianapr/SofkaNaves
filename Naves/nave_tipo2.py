import nave

class nave2(nave.base):
    def __init__(self, nombre, pais_creacion, peso, n_id, velocidad_llegada):
        super().__init__(nombre, pais_creacion, peso, n_id)
        self.velocidad_llegada = velocidad_llegada
        self.tipo_nave = "Nave no tripulada o robotica"