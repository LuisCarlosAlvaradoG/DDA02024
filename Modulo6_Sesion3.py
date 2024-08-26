# Sesión 3: Bucles anidados

# Imprimir una matriz 3x3
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Generar una tabla de multiplicar
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()

# Sumar los elementos de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma = 0
for fila in matriz:
    for elemento in fila:
        suma += elemento
print(f"Suma de los elementos de la matriz: {suma}")

# Imprimir un patrón de estrellas
filas = int(input("Introduce el número de filas para el patrón de estrellas: "))
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end="")
    print()

# Imprimir una pirámide de números
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Ejercicio: Generar la tabla de adición de 1 a 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} + {j} = {i + j}", end="\t")
    print()

# Ejercicio: Imprimir la matriz transpuesta
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(matriz[j][i])
    transpuesta.append(fila)
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
