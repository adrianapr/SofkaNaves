from pprint import pprint
from PyInquirer import prompt, Separator
from preguntas.preguntasBase import questionsLayer1, questionsSeleccionarTipo
from preguntas.preguntasBase import crearTipo1, crearTipo2, crearTipo3, layerBuscar,crearBusquedaPorId
from tiposNave.nave_tipo1 import nave1
from tiposNave.nave_tipo2 import nave2
from tiposNave.nave_tipo3 import nave3
from database import database
from helpers.inventarioNaves import guardarInventario


def  nave_tipo1():
    values = prompt(crearTipo1)
    naveCreada = nave1(values)
    naveCreada.guardar()


def  nave_tipo2():
    values = prompt(crearTipo2)
    naveCreada = nave2(values)
    naveCreada.guardar()


def  nave_tipo3():
    values = prompt(crearTipo3)
    naveCreada = nave3(values)
    naveCreada.guardar()


def buscarId():
    values = prompt(crearBusquedaPorId)
    result = database.buscarporId(values)
    if result == None:
        print("No se encontró nave con el ID que ingresaste, intenta nuevamente")
    else: 
        print("**** Estos son los datos de la nave seleccionada: ****")
        print(result)


def buscarporTipo():
    values = prompt(questionsSeleccionarTipo)
    results = database.buscarPorTipo(values)
    print("**** Estos son los datos de las naves encontradas: ****")
    for r in results:
        print(r)

 
def seleccionar_tipo():
    print(">>>>> Vamos a crear tu nave, por favor dinos:")
    respuesta = prompt(questionsSeleccionarTipo)
    tipo_seleccionado = respuesta["tipo_nave"]

    if tipo_seleccionado == "Lanzadera":
        nave_tipo1()
    elif tipo_seleccionado == "No tripulada":
        nave_tipo2()
    elif tipo_seleccionado == "Tripulada":
        nave_tipo3()
    print("Felicitaciones, tu nave ha sido creada exitosamente")


def buscar_tipo():
    print(">>>>> Vamos a buscar la nave")
    naveAbuscar = prompt(layerBuscar)
    filtro_seleccionado = naveAbuscar["naveBuscar"]

    if filtro_seleccionado == "ID":
       buscarId()
    elif filtro_seleccionado == "Tipo":
        buscarporTipo()



accion_seleccionada=""


guardarInventario()

while accion_seleccionada != "salir": 
    layer1 = prompt(questionsLayer1)
    accion_seleccionada = layer1["accion"]

    if accion_seleccionada == "crear":
        seleccionar_tipo()
    elif accion_seleccionada == "buscar":
        buscar_tipo()
    
