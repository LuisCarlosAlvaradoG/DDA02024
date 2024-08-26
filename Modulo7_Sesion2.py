# Sesión 2: Arreglos multidimensionales

# Crear una matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz:")
for fila in matriz:
    print(fila)

# Acceder a elementos de la matriz
print("Elemento en la primera fila, segunda columna:", matriz[0][1])

# Modificar elementos de la matriz
matriz[1][1] = 10
print("Matriz después de modificar un elemento:")
for fila in matriz:
    print(fila)

# Añadir una fila a la matriz
nueva_fila = [10, 11, 12]
matriz.append(nueva_fila)
print("Matriz después de añadir una fila:")
for fila in matriz:
    print(fila)

# Eliminar una fila de la matriz
matriz.pop(0)
print("Matriz después de eliminar la primera fila:")
for fila in matriz:
    print(fila)

# Ejercicio: Calcular la suma de todos los elementos de una matriz
suma = 0
for fila in matriz:
    for elemento in fila:
        suma += elemento
print(f"La suma de los elementos de la matriz es: {suma}")

# Ejercicio: Encontrar el elemento máximo en una matriz
max_elemento = matriz[0][0]
for fila in matriz:
    for elemento in fila:
        if elemento > max_elemento:
            max_elemento = elemento
print(f"El elemento máximo en la matriz es: {max_elemento}")

# Ejercicio: Transponer una matriz
matriz_transpuesta = []
for i in range(len(matriz[0])):
    nueva_fila = []
    for fila in matriz:
        nueva_fila.append(fila[i])
    matriz_transpuesta.append(nueva_fila)
print("Matriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)

# Ejercicio: Multiplicar dos matrices
matriz_a = [
    [1, 2],
    [3, 4]
]
matriz_b = [
    [5, 6],
    [7, 8]
]
matriz_resultado = []
for i in range(len(matriz_a)):
    nueva_fila = []
    for j in range(len(matriz_b[0])):
        suma = 0
        for k in range(len(matriz_a[0])):
            suma += matriz_a[i][k] * matriz_b[k][j]
        nueva_fila.append(suma)
    matriz_resultado.append(nueva_fila)
print("Resultado de la multiplicación de matrices:")
for fila in matriz_resultado:
    print(fila)
