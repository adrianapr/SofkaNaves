from pprint import pprint
from PyInquirer import prompt, Separator
from preguntas.preguntasBase import questionsLayer1, questionsSeleccionarTipo
from preguntas.preguntasBase import crearTipo1, crearTipo2, crearTipo3
from tiposNave.nave_tipo1 import nave1
from tiposNave.nave_tipo2 import nave2
from tiposNave.nave_tipo3 import nave3


def  nave_tipo1():
    values = prompt(crearTipo1)
    print(values)
    resultado = nave1(values["nombre_nave"], values["Pais_creacion"], values["Peso_nave"], values["n_id"], values["Capacidad_transporte"], values["Capacidad_empuje"])



def  nave_tipo2():
    values = prompt(crearTipo2)
    print(values)
    resultado = nave2(values["nombre_nave"], values["Pais_creacion"], values["Peso_nave"], values["n_id"], values["Velocidad_llegada"])



def  nave_tipo3():
    values = prompt(crearTipo3)
    print(values)
    resultado = nave3(values["nombre_nave"], values["Pais_creacion"], values["Peso_nave"], values["n_id"], values["Capacidad_Personas"], values["Capacidad_Orbita"] )

 
def seleccionar_tipo():
    print("##### Vamos a crear tu nave, por favor dinos:")
    respuesta = prompt(questionsSeleccionarTipo)
    tipo_seleccionado = respuesta["tipo"]
    print(tipo_seleccionado)

    if tipo_seleccionado == "Lanzadera":
        nave_tipo1()
    elif tipo_seleccionado == "No tripulada":
        nave_tipo2()
    elif tipo_seleccionado == "Tripulada":
        nave_tipo3()
    print("Felicitaciones, tu nava ha sido creada exitosamete")



accion_seleccionada=""

while accion_seleccionada != "salir":
    layer1 = prompt(questionsLayer1)
    accion_seleccionada = layer1["accion"]

    if accion_seleccionada == "crear":
        seleccionar_tipo()
    elif accion_seleccionada == "buscar":
        layerBuscar =  prompt(questionsBuscar)
    












