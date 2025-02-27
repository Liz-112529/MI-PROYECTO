def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición del valor encontrado
    return None  # Retorna None si no se encuentra el valor

# Definir una matriz 3x3
matriz = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

# Solicitar al usuario el valor a buscar
valor_buscar = int(input("Ingrese el valor a buscar: "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscar)

# Mostrar el resultado
if resultado:
    print(f"Valor {valor_buscar} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_buscar} no encontrado en la matriz.")
