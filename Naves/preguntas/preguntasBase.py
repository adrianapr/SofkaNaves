questionsLayer1 = [
    {
        'type': 'list',
        'message': 'Que quieres hacer?',
        'name': 'accion',
        'choices': [ 
            {
                'name': 'crear'
            },
            {
                'name': 'buscar'
            },
             {
                'name': 'salir'
            }
        ]
    }
]

questionsSeleccionarTipo = [
    {
        'type': 'list',
        'message': 'Selecciona un tipo de nave',
        'name': 'tipo_nave',
        'choices': [ 
            {
                'name': 'Lanzadera'
            },
            {
                'name': 'No tripulada'
            },
             {
                'name': 'Tripulada'
            },
        ],
    }
]


crearTipo1 = [
        {
        'type': 'input',
        'name': 'nombre_nave',
        'message': 'Ingresar nombre de la nave',
        },
        { 'type': 'input',
        'name': 'Pais_creacion',
        'message': 'Ingrese el pais de creacion'
        },
        { 'type': 'input',
        'name': 'Peso_nave',
        'message': 'Ingresar el peso de la nave'
        },
        { 'type': 'input',
        'name': '_id',
        'message': 'Ingresar el ID de la nave'
        },
        {'type': 'input',
        'name': 'Capacidad_transporte',
        'message': 'Ingresar capacidad de transporte'
        },
        {'type': 'input',
        'name': 'Capacidad_empuje',
        'message': 'Ingresar capacidad de empuje'
        },
]



crearTipo2 = [
        {
        'type': 'input',
        'name': 'nombre_nave',
        'message': 'Ingresar nombre de la nave',
        },
        { 'type': 'input',
        'name': 'Pais_creacion',
        'message': 'Ingrese el pais de creacion'
        },
        { 'type': 'input',
        'name': 'Peso_nave',
        'message': 'Ingresar el peso de la nave'
        },
        { 'type': 'input',
        'name': '_id',
        'message': 'Ingresar el ID de la nave'
        },
        {'type': 'input',
        'name': 'Velocidad_llegada',
        'message': 'Ingresar velocidad de llegada'
        },

]

  
crearTipo3 = [
        {
        'type': 'input',
        'name': 'nombre_nave',
        'message': 'Ingresar nombre de la nave',
        },
        { 'type': 'input',
        'name': 'Pais_creacion',
        'message': 'Ingrese el pais de creacion'
        },
        { 'type': 'input',
        'name': 'Peso_nave',
        'message': 'Ingresar el peso de la nave'
        },
        { 'type': 'input',
        'name': '_id',
        'message': 'Ingresar el ID de la nave'
        },
        {'type': 'input',
        'name': 'Capacidad_Personas',
        'message': 'Ingresar capacidad de Personas'
        },
        {'type': 'input',
        'name': 'Capacidad_Orbita',
        'message': 'Ingresar capacidad de Orbita'
        },
]

layerBuscar = [
    {
        'type': 'list',
        'message': 'Selecciona el dato a buscar',
        'name': 'naveBuscar',
        'choices': [ 
            {
                'name': 'Tipo'
            },
             {
                'name': 'ID'
            },
        ],
    }
]


crearBusquedaPorId = [
        {
        'type': 'input',
        'name': '_id',
        'message': 'Ingresar ID de la nave',
        },
]
