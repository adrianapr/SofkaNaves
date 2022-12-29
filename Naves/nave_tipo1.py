import nave

class nave1(nave.base):
    def __init__(self, nombre, pais_creacion, peso, n_id, capacidad_transporte, capacidad_empuje):
        super().__init__(nombre, pais_creacion, peso, n_id)
        self.capacidad_transporte = capacidad_transporte
        self.capacidad_empuje = capacidad_empuje
        self.tipo_nave = "Vehiculo Lanzadera"


