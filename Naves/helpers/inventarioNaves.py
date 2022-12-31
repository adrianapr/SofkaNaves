from tiposNave.nave_tipo1 import nave1
from tiposNave.nave_tipo2 import nave2
from tiposNave.nave_tipo3 import nave3
from database import database

Lanzadera = [
    {
        'nombre_nave': 'Saturno v',
        'Pais_creacion': 'EE.UU',
        'Peso_nave': '2900 toneladas',
        '_id': '1',
        'Capacidad_transporte': ' 118 toneladas',
        'Capacidad_empuje': '3500 toneladas'
    },
    {
        'nombre_nave': 'Delta V',
        'Pais_creacion': 'EE.UU',
        'Peso_nave': '7300 toneladas',
        '_id': '2',
        'Capacidad_transporte': ' 23 toneladas',
        'Capacidad_empuje': '8499 toneladas'
    },
    {
        'nombre_nave': 'Energia',
        'Pais_creacion': 'Rusia Ucrania',
        'Peso_nave': '2400 toneladas',
        '_id': '3',
        'Capacidad_transporte': '100 toneladas',
        'Capacidad_empuje': '3060 toneladas'
    }
]


No_tripuladas = [
    {   'nombre_nave': 'Pionero X',
        'Pais_creacion': 'EE.UU Rusia',
        'Peso_nave': '258 toneladas',
        '_id': '4',
        'Velocidad_llegada': '4 Millones de  años'
    },
        
    {   
        'nombre_nave': 'New Horizons',
        'Pais_creacion': 'EE.UU NASA',
        'Peso_nave': '10 toneladas',
        '_id': '5',
        'Velocidad_llegada': ' 9 millones de años'
    },
    {
        'nombre_nave': 'Cassini-Huygens',
        'Pais_creacion': 'Europa ESA',
        'Peso_nave': '200 toneladas',
        '_id': '6',
        'Velocidad_llegada': ' 1.6 millones de años'
    }
]

Tripuladas=[
        {   
            'nombre_nave': 'Skylab',
            'Pais_creacion': 'EE.UU',
            'Peso_nave': '77 toneladas',
            '_id': '7',
            'Capacidad_Personas':'3 personas',
            'Capacidad_Orbita':'435 kilometros'
            },
        {
            'nombre_nave': 'Salyut sovietico',
            'Pais_creacion': 'Europa ESA',
            'Peso_nave': '200 toneladas',
            '_id': '8',
            'Capacidad_Personas':'3 personas',
            'Capacidad_Orbita':' 248 kilometros'
        },
        {
            'nombre_nave': 'Estacion espacial internacional',
            'Pais_creacion': 'Europa ESA',
            'Peso_nave': '420 toneladas',
            '_id': '9',
            'Capacidad_Personas':'7 personas',
            'Capacidad_Orbita':' 386 kilometros'
        }
    
    ]

def guardarInventario():
    if not database.buscarporId('1'):
        nave1(Lanzadera[0]).guardar()
    if not database.buscarporId('2'):
        nave1(Lanzadera[1]).guardar()
    if not database.buscarporId('3'):
       nave1(Lanzadera[2]).guardar()
    if not database.buscarporId('4'):
        nave2(No_tripuladas[0]).guardar()
    if not database.buscarporId('5'):
        nave2(No_tripuladas[1]).guardar()
    if not database.buscarporId('6'):
        nave2(No_tripuladas[2]).guardar()
    if not database.buscarporId('7'):
        nave3(Tripuladas[0]).guardar()
    if not database.buscarporId('8'):
        nave3(Tripuladas[1]).guardar()
    if not database.buscarporId('9'):
        nave3(Tripuladas[2]).guardar()