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
            ,
             {
                'name': 'continuar'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

questionsSeleccionarTipo = [
    {
        'type': 'list',
        'message': 'Selecciona un tipo de nave',
        'name': 'tipo',
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
         {
        'type': 'input',
        'name': 'nombre_lanzadera',
        'message': 'nombre_lanzadera',
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
        'name': 'n_id',
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
        {
        'type': 'input',
        'name': 'nombre_no__tripulada',
        'message': 'nombre_no__tripulada',
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
        'name': 'n_id',
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
         {
        'type': 'input',
        'name': 'nombre_tripulada',
        'message': 'nombre_tripulada',
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
        'name': 'n_id',
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