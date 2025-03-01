def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

matriz = [
    [9, 4, 7],
    [3, 8, 1],
    [6, 2, 5]
]

fila_index = int(input("Coloque el índice de la fila a ordenar (0-2): "))

print("Matriz original:")
for fila in matriz:
    print(fila)

bubble_sort(matriz[fila_index])

print("\nMatriz con la fila ordenada: ")
for fila in matriz:
    print(fila)