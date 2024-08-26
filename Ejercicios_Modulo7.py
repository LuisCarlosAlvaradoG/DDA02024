# Ejercicio 1: Suma de Elementos de un Arreglo
# Problema: Escribe un programa en Python que calcule la suma de los elementos de un arreglo unidimensional ingresado por el usuario.

# Ejemplo de solución en Python
def suma_arreglo(arreglo):
    suma = 0
    for elemento in arreglo:
        suma += elemento
    return suma

arreglo = [int(x) for x in input("Ingresa los elementos del arreglo separados por espacios: ").split()]
resultado = suma_arreglo(arreglo)
print(f"La suma de los elementos del arreglo es: {resultado}")

# Ejercicio 2: Producto de Elementos de un Arreglo
# Problema: Escribe un programa en Python que calcule el producto de los elementos de un arreglo unidimensional ingresado por el usuario.

# Ejemplo de solución en Python
def producto_arreglo(arreglo):
    producto = 1
    for elemento in arreglo:
        producto *= elemento
    return producto

arreglo = [int(x) for x in input("Ingresa los elementos del arreglo separados por espacios: ").split()]
resultado = producto_arreglo(arreglo)
print(f"El producto de los elementos del arreglo es: {resultado}")

# Ejercicio 3: Transposición de una Matriz
# Problema: Escribe un programa en Python que realice la transposición de una matriz ingresada por el usuario (matriz bidimensional).

# Ejemplo de solución en Python
def transponer_matriz(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    matriz_transpuesta = [[0 for _ in range(num_filas)] for _ in range(num_columnas)]
    
    for i in range(num_filas):
        for j in range(num_columnas):
            matriz_transpuesta[j][i] = matriz[i][j]
    
    return matriz_transpuesta

# Ejemplo de uso
matriz = []
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

print("Ingresa los elementos de la matriz (separados por espacios):")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_transpuesta = transponer_matriz(matriz)
print("Matriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)

# Ejercicio 4: Promedio de una Matriz
# Problema: Escribe un programa en Python que calcule el promedio de todos los elementos de una matriz ingresada por el usuario.

# Ejemplo de solución en Python
def promedio_matriz(matriz):
    total_elementos = 0
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
            total_elementos += 1
    promedio = suma / total_elementos
    return promedio

# Ejemplo de uso
matriz = []
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

print("Ingresa los elementos de la matriz (separados por espacios):")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)

print("Matriz ingresada:")
for fila in matriz:
    print(fila)

resultado = promedio_matriz(matriz)
print(f"El promedio de los elementos de la matriz es: {resultado}")

# Ejercicio 5: Ordenamiento de un Arreglo
# Problema: Escribe un programa en Python que ordene de manera ascendente un arreglo unidimensional ingresado por el usuario.

# Ejemplo de solución en Python
def ordenar_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo = [int(x) for x in input("Ingresa los elementos del arreglo separados por espacios: ").split()]
arreglo_ordenado = ordenar_arreglo(arreglo)
print(f"Arreglo ordenado de manera ascendente: {arreglo_ordenado}")

# Ejercicio 6: Búsqueda en una Matriz
# Problema: Escribe un programa en Python que busque un elemento específico en una matriz ingresada por el usuario y muestre su posición si lo encuentra.

# Ejemplo de solución en Python
def buscar_en_matriz(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elemento:
                return f"El elemento {elemento} está en la posición ({i}, {j})"
    return f"El elemento {elemento} no está en la matriz"

# Ejemplo de uso
matriz = []
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

print("Ingresa los elementos de la matriz (separados por espacios):")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)

elemento_buscar = int(input("Ingresa el elemento que deseas buscar en la matriz: "))
resultado = buscar_en_matriz(matriz, elemento_buscar)
print(resultado)

# Ejercicio 7: Matriz Identidad
# Problema: Escribe un programa en Python que genere y muestre una matriz identidad de tamaño NxN, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
def matriz_identidad(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        matriz[i][i] = 1
    return matriz

N = int(input("Ingresa el tamaño de la matriz identidad (NxN): "))
matriz_ident = matriz_identidad(N)

print(f"Matriz identidad de tamaño {N}x{N}:")
for fila in matriz_ident:
    print(fila)

# Ejercicio 8: Suma de Elementos por Columna en una Matriz
# Problema: Escribe un programa en Python que calcule la suma de los elementos de cada columna de una matriz ingresada por el usuario y muestre los resultados.

# Ejemplo de solución en Python
def suma_columnas_matriz(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    sumas_columnas = [0] * num_columnas
    
    for i in range(num_filas):
        for j in range(num_columnas):
            sumas_columnas[j] += matriz[i][j]
    
    return sumas_columnas

# Ejemplo de uso
matriz = []
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

print("Ingresa los elementos de la matriz (separados por espacios):")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)

print("Matriz ingresada:")
for fila in matriz:
    print(fila)

resultados = suma_columnas_matriz(matriz)
for i, suma in enumerate(resultados):
    print(f"Suma de la columna {i + 1}: {suma}")

# Ejercicio 9: Matriz Diagonal
# Problema: Escribe un programa en Python que genere y muestre una matriz diagonal de tamaño NxN, donde N y los elementos de la diagonal son ingresados por el usuario.

# Ejemplo de solución en Python
def matriz_diagonal(N, elemento_diagonal):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        matriz[i][i] = elemento_diagonal
    return matriz

N = int(input("Ingresa el tamaño de la matriz diagonal (NxN): "))
elemento_diagonal = int(input("Ingresa el elemento de la diagonal: "))
matriz_diag = matriz_diagonal(N, elemento_diagonal)

print(f"Matriz diagonal de tamaño {N}x{N} con elemento {elemento_diagonal} en la diagonal:")
for fila in matriz_diag:
    print(fila)

# Ejercicio 10: Rotación de una Matriz
# Problema: Escribe un programa en Python que rote una matriz cuadrada 90 grados en sentido antihorario.

# Ejemplo de solución en Python
def rotar_matriz_90(matriz):
    N = len(matriz)
    matriz_rotada = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            matriz_rotada[N - 1 - j][i] = matriz[i][j]
    
    return matriz_rotada

# Ejercicio 11: Matriz Espiral
# Problema: Escribe un programa en Python que genere y muestre una matriz NxN que contenga los números del 1 al N^2 dispuestos en forma de espiral.

# Ejemplo de solución en Python
def matriz_espiral(N):
    matriz = [[0]*N for _ in range(N)]
    valor = 1
    inicio_fila = 0
    fin_fila = N - 1
    inicio_col = 0
    fin_col = N - 1
    
    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        for i in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][i] = valor
            valor += 1
        inicio_fila += 1
        
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_col] = valor
            valor += 1
        fin_col -= 1
        
        if inicio_fila <= fin_fila:
            for i in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][i] = valor
                valor += 1
            fin_fila -= 1
        
        if inicio_col <= fin_col:
            for i in range(fin_fila, inicio_fila - 1, -1):
                matriz[i][inicio_col] = valor
                valor += 1
            inicio_col += 1
    
    return matriz

# Ejemplo de uso
N = int(input("Ingresa el tamaño de la matriz espiral (NxN): "))
matriz_esp = matriz_espiral(N)

print(f"Matriz espiral de tamaño {N}x{N}:")
for fila in matriz_esp:
    print(fila)

# Ejercicio 12: Matriz Pascal
# Problema: Escribe un programa en Python que genere y muestre las primeras N filas del triángulo de Pascal.

# Ejemplo de solución en Python
def triangulo_pascal(N):
    triangulo = [[1]*i for i in range(1, N+1)]
    
    for i in range(2, N):
        for j in range(1, i):
            triangulo[i][j] = triangulo[i-1][j-1] + triangulo[i-1][j]
    
    return triangulo

# Ejemplo de uso
N = int(input("Ingresa el número de filas para el triángulo de Pascal: "))
triangulo = triangulo_pascal(N)

print(f"Triángulo de Pascal con {N} filas:")
for fila in triangulo:
    print(fila)

# Ejercicio 13: Matriz de Ceros y Unos
# Problema: Escribe un programa en Python que genere y muestre una matriz NxN donde los elementos sean 0 o 1 de manera alternada.

# Ejemplo de solución en Python
def matriz_ceros_unos(N):
    matriz = [[(i+j)%2 for j in range(N)] for i in range(N)]
    return matriz

# Ejemplo de uso
N = int(input("Ingresa el tamaño de la matriz de ceros y unos (NxN): "))
matriz = matriz_ceros_unos(N)

print(f"Matriz de ceros y unos de tamaño {N}x{N}:")
for fila in matriz:
    print(fila)

# Ejercicio 14: Eliminación de Elementos Repetidos en una Lista
# Problema: Escribe un programa en Python que elimine los elementos repetidos de una lista y muestre la lista resultante.

# Ejemplo de solución en Python
def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

# Ejemplo de uso
lista = input("Ingresa los elementos de la lista separados por espacios: ").split()
lista_sin_repetidos = eliminar_repetidos(lista)

print("Lista original:")
print(lista)

print("Lista sin elementos repetidos:")
print(lista_sin_repetidos)

# Ejercicio 15: Contador de Palabras en un Texto
# Problema: Escribe un programa en Python que cuente el número de veces que aparece cada palabra en un texto ingresado por el usuario.

# Ejemplo de solución en Python
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    return contador

# Ejemplo de uso
texto = input("Ingresa un texto para contar las palabras: ")
resultado = contar_palabras(texto)

print("Conteo de palabras:")
for palabra, conteo in resultado.items():
    print(f"'{palabra}': {conteo}")

# Ejercicio 16: Combinación de Listas
# Problema: Escribe un programa en Python que combine dos listas ordenadas de enteros en una sola lista ordenada.

# Ejemplo de solución en Python
def combinar_listas(lista1, lista2):
    lista_combinada = sorted(lista1 + lista2)
    return lista_combinada

# Ejemplo de uso
lista1 = [int(x) for x in input("Ingresa los elementos de la primera lista ordenada separados por espacios: ").split()]
lista2 = [int(x) for x in input("Ingresa los elementos de la segunda lista ordenada separados por espacios: ").split()]

lista_combinada = combinar_listas(lista1, lista2)
print("Lista combinada ordenada:")
print(lista_combinada)

# Ejercicio 17: Matriz de Rotación 90 Grados
# Problema: Escribe un programa en Python que rote una matriz NxN 90 grados en sentido horario.

# Ejemplo de solución en Python
def rotar_matriz_90_horario(matriz):
    N = len(matriz)
    matriz_rotada = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            matriz_rotada[j][N-1-i] = matriz[i][j]
    
    return matriz_rotada

# Ejemplo de uso
N = int(input("Ingresa el tamaño de la matriz a rotar (NxN): "))
matriz = [[int(input(f"Ingrese el elemento para la posición [{i}][{j}]: ")) for j in range(N)] for i in range(N)]

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_rotada = rotar_matriz_90_horario(matriz)
print("Matriz rotada 90 grados en sentido horario:")
for fila in matriz_rotada:
    print(fila)

# Ejercicio 18: Matriz de Identidad Especial
# Problema: Escribe un programa en Python que genere y muestre una matriz de identidad especial de tamaño NxN, donde cada fila comience con un número diferente.

# Ejemplo de solución en Python
def matriz_identidad_especial(N):
    matriz = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            matriz[i][j] = (i + j) % N + 1
    
    return matriz

# Ejemplo de uso
N = int(input("Ingresa el tamaño de la matriz de identidad especial (NxN): "))
matriz = matriz_identidad_especial(N)

print(f"Matriz de identidad especial de tamaño {N}x{N}:")
for fila in matriz:
    print(fila)

# Ejercicio 19: Lista de Números Primos
# Problema: Escribe un programa en Python que genere una lista con los primeros N números primos.

# Ejemplo de solución en Python
def numeros_primos(N):
    primos = []
    num = 2
    
    while len(primos) < N:
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
        num += 1
    
    return primos

# Ejemplo de uso
N = int(input("Ingresa un número entero positivo para generar números primos: "))
lista_primos = numeros_primos(N)

print(f"Los primeros {N} números primos son:")
print(lista_primos)

