# Nombres y Apellidos: Reinel Alejandro Jaramillo Aguirre
# Tema: Registro de Temperaturas Diarias
# Tarea: Iteración de arreglos multidimensionales con bucles aninados

temperaturas = [
    [   # Santa Elena
        [30, 32, 31, 29, 28, 27, 30], # Semana 1
        [31, 33, 30, 28, 29, 27, 32]  # Semana 2
    ],
    [   # Orellana
        [25, 26, 27, 28, 26, 25, 24], # Semana 1
        [26, 27, 28, 29, 27, 26, 25]  # Semana 2
    ],
    [   # Quito
        [20, 22, 21, 19, 18, 20, 22], # Semana 1
        [21, 23, 22, 20, 19, 21, 23]  # Semana 2
    ]
]

ciudades = ["Santa Elena", "Orellana", "Quito"]

for i, ciudad in enumerate(ciudades):
    print(f"Promedios de temperatura para {ciudad}: ")
    for semana in range(len(temperaturas[i])):
        promedio = sum(temperaturas[i][semana]) / len(temperaturas[i][semana])
        print(f"  Semana {semana + 1}: {promedio: .2f}°C")
        print()