from tiposNave import nave

class nave3(nave.base):
    def __init__(self, infoValues):
        super().__init__(infoValues["nombre_nave"], infoValues["Pais_creacion"], infoValues["Peso_nave"], infoValues["_id"])
        self.capacidad_personas = infoValues["Capacidad_Personas"]
        self.capacidad_orbita = infoValues["Capacidad_Orbita"]
        self.tipo_nave = "Tripulada"
