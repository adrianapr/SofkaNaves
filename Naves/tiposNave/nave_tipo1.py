from tiposNave import nave

class nave1(nave.base):
    def __init__(self,infoValues):
        super().__init__(infoValues["nombre_nave"], infoValues["Pais_creacion"], infoValues["Peso_nave"], infoValues["_id"])
        self.capacidad_transporte = infoValues["Capacidad_transporte"]
        self.capacidad_empuje = infoValues["Capacidad_empuje"]
        self.tipo_nave = "Lanzadera"