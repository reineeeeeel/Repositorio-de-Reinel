# Nombres y Apellidos: Reinel Alejandro Jaramillo Aguirre
# Tarea: Desarrollo de Función para Calcular Temperaturas Promedio en Python
# Semana 13

def calcular_promedio_temperaturas(datos_temperaturas):
    """
    Calcula el promedio de temperatura para cada ciudad.

    Parámetros:
    - datos_temperaturas (list): Matriz 3D con temperaturas (ciudades, semanas, días).

    Imprime el promedio de temperatura para cada ciudad.
    """
    ciudades = ["Santa Elena", "Orellana", "Quito"]

    for i, ciudad in enumerate(ciudades):
        print(f"Promedios de temperatura para {ciudad}:")

        total_temperatura = 0
        total_dias = 0

        for semana in range(len(datos_temperaturas[i])):
            promedio_semanal = sum(datos_temperaturas[i][semana]) / len(datos_temperaturas[i][semana])
            print(f" Semana {semana + 1}: {promedio_semanal:.2f}°C")

            # Para sumar las temperaturas para el promedio total de las ciudades
            total_temperatura += sum(datos_temperaturas[i][semana])
            total_dias += len(datos_temperaturas[i][semana])

        # Para calcular el promedio total de las ciudades
        promedio_ciudad = total_temperatura / total_dias
        print(f" Promedio total de {ciudad}: {promedio_ciudad:.2f}°C\n")


temperaturas = [
    [  # Santa Elena
        [30, 32, 31, 29, 28, 27, 30],  # Semana 1
        [31, 33, 30, 28, 29, 27, 32],  # Semana 2
        [29, 28, 30, 31, 32, 33, 34],  # Semana 3
        [30, 32, 31, 29, 28, 27, 30]   # Semana 4
    ],
    [  # Orellana
        [25, 26, 27, 28, 26, 25, 24],  # Semana 1
        [26, 27, 28, 29, 27, 26, 25],  # Semana 2
        [28, 29, 30, 31, 32, 33, 34],  # Semana 3
        [25, 24, 23, 22, 21, 20, 19]   # Semana 4
    ],
    [  # Quito
        [20, 22, 21, 19, 18, 20, 22],  # Semana 1
        [21, 23, 22, 20, 19, 21, 23],  # Semana 2
        [19, 18, 20, 22, 21, 23, 24],  # Semana 3
        [20, 21, 22, 23, 24, 25, 26]   # Semana 4
    ]
]

calcular_promedio_temperaturas(temperaturas)