# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (Guayaquil, Quito y Pastaza)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    {"ciudad": "Guayaquil", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 21}
        ]
    ]},
    {"ciudad": "Quito", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 4},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 5},
            {"day": "Domingo", "temp": 9}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 3},
            {"day": "Martes", "temp": 6},
            {"day": "Miércoles", "temp": 7},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 5},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 8}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 5},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 7},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 6},
            {"day": "Domingo", "temp": 8}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 4},
            {"day": "Martes", "temp": 6},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 7},
            {"day": "Viernes", "temp": 7},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 8}
        ]
    ]},
    {"ciudad": "Pastaza", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 8}
        ]
    ]}
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    print(f"Promedio de temperaturas en {ciudad["ciudad"]}: ")
    for semana_idx, semana in enumerate(ciudad["semanas" ]):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f" Semana {semana_idx + 1}: {promedio:.2f} °C")