from tiposNave import nave

class nave2(nave.base):
    def __init__(self, infoValues):
        super().__init__(infoValues["nombre_nave"], infoValues["Pais_creacion"], infoValues["Peso_nave"], infoValues["_id"])
        self.velocidad_llegada = infoValues["Velocidad_llegada"]
        self.tipo_nave = "No tripulada"
