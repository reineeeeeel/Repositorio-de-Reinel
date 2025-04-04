# Nombres y Apellidos: Reinel Alejandro Jaramillo Aguirre

with open("mynotes.txt", "w") as file:
    file.write("1. Comprar frutas y verduras para la semana.\n")
    file.write("2. No olvidar apagar las luces antes de salir.\n")
    file.write("3. Beber al menos dos litros de agua al día.\n")

with open("mynotes.txt", "r") as file:
    for line in file:
        print(line.strip())