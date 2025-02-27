def bubble_sort_fila(matriz, fila):
    """Ordena una fila específica de la matriz usando Bubble Sort."""
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Definir una matriz 3x3
matriz = [
    [34, 12, 5],
    [99, 56, 23],
    [78, 45, 10]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_ordenar = int(input("Ingrese el número de fila a ordenar (0-2): "))

# Verificar si la fila es válida y ordenar
if 0 <= fila_ordenar < len(matriz):
    bubble_sort_fila(matriz, fila_ordenar)
    print("Matriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila no válido.")
