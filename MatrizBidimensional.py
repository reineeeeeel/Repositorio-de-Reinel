def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j

    return None

matriz = [
    [5, 8, 2],
    [1, 4, 7],
    [3, 9, 6]
]

valor_buscado = int(input("Coloque el valor a buscar: "))

resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"Valor hallado en la posición: {resultado}")
else:
    print(f"Valor no hallado en la matriz.")