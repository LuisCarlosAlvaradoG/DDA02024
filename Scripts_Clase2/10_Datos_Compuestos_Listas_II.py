# 10.- DATOS COMPUESTOS: LISTAS (II) — PATRONES AVANZADOS, ANIDADAS Y COMPRENSIONES
# ---------------------------------------------------------------
# A) LISTAS ANIDADAS (MATRICES): CREACIÓN Y RECORRIDO
# ---------------------------------------------------------------
# Matriz 3x3 fija:
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(M)
print(M[0])
print(M[1][1])

# Recorridos:
# - Por filas
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0
for i in M:
    for x in i:
        suma += x
print(suma)

# - Por índices (i, j)
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0
for i in range(len(M)):
    for j in range(len(M[0])):
        suma += M[i][j]
print(suma)


# ---------------------------------------------------------------
# B) CONSTRUCCIÓN PROGRAMÁTICA: TABLAS Y PATRONES
# ---------------------------------------------------------------
# Tabla de multiplicar 1..r por 1..c (guardada en matriz T)
r = 7; c = 5
T = []
for i in range(1, r+1):
    fila = []
    for j in range(1, c+1):
        fila.append(i*j)
    T.append(fila)

for x in T:
    print(x)
# Patrón de tablero (caracteres)
n = 5
tablero = []
for i in range(n):
    fila = []
    for j in range(n):
        if (i+j) % 2 == 0:
            fila.append("#")
        else:
            fila.append(".")
    tablero.append(fila)

for i in tablero:
    print(i)

# ---------------------------------------------------------------
# C) BÚSQUEDA, FILTRADO Y TRANSFORMACIÓN (SIN FUNCIONES)
# ---------------------------------------------------------------
# Búsqueda de un valor v en M: devuelve (i,j) de la primera aparición o (-1,-1)

# Filtrar pares de una lista L en R (mantener orden)


# Transformar: sumar 1 a cada elemento de L en una NUEVA lista


# ---------------------------------------------------------------
# D) ORDENAMIENTOS BÁSICOS (MANUALES)
# ---------------------------------------------------------------
# Burbuja ascendente (bubble sort) sobre copia para no tocar original

# Selección ascendente (selection sort)


# ---------------------------------------------------------------
# E) CONVERSIÓN TEXTO<->LISTA: SPLIT Y JOIN
# ---------------------------------------------------------------
# split: separa una cadena en lista por separador (por defecto, espacios)
# str -> list
palabra = "A,B,C,D"
salida = palabra.split(",")
print(salida)

# join: une elementos de una lista de strings con un separador
#list -> str
lista = ["A", "B", "C"]
salida = "-".join(lista)
print(salida)

# ---------------------------------------------------------------
# F) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:
nums = [1, 2, 3, 4, 5]
nums_squared = []
for i in nums:
    nums_squared.append(i**2)
print(nums_squared)

# Operacion - Ciclo for
nums_squared_comp = [x**2 for x in nums] 
print(nums_squared_comp)
#-----------------------------------------------------------------------
# Pares al cuadrado e impares al cubo
nums = [1, 2, 3, 4, 5]
nums_squared = []
for i in nums:
    if i % 2 == 0:
        nums_squared.append(i**2)
    else:
        nums_squared.append(i**3)
print(nums_squared)

# Operación if - if condicion - else - Operacion else - Ciclo for
nums_squared_comp = [x**2 if x % 2 == 0 else x **3 for x in nums] 
print(nums_squared_comp)
#---------------------------------------------------------------------------
# Cuando solamente tengo un if
# Operacion if - Ciclo for - If condicion
nums_squared_comp = [x**2 for x in nums if x % 2 == 0] 
# lista = []
# for x in nums:
#     if x % 2 == 0:
#         lista.append(x**2)
print(nums_squared_comp)
# ---------------------------------------------------------------
# G) FUNCIÓN MAP USANDO LAMBDA
# ---------------------------------------------------------------
nums = [1, 2, 3, 4, 5]
# lambda recibe una variable y le digo que hacer con esa variable 
# nums -> Es el objeto sobre el cuál voy a iterar
# map -> Le digo, itera sobre nums, recibiendo x, y eleva x al cuadrado
cuadrados = list(map(lambda x: x**2, nums))
print(cuadrados)
# Elevar al cuadrado solo los pares
cuadrados_pares = list(map(lambda x:x**2, filter(lambda x: x % 2 == 0, nums)))
print(cuadrados_pares)

# Obtener la transpuesta de M
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

T = []
for j in range(len(M)):
    fila = []
    for i in range(len(M[0])):
       fila.append(M[i][j])
    T.append(fila)

for x in T:
    print(x)


nums_str = ["1", "2", "3", "4", "5"]
lista = []
for i in nums_str:
    lista.append(int(i))
print(lista)

nums_str = ["1", "2", "3", "4", "5"]
lista = [int(i) for i in nums_str]
print(lista)

nums_str = ["1", "2", "3", "4", "5"]
lista = list(map(lambda x: int(x), nums_str))
print(lista)

# Ejercicio 05 - Eliminar columna j
# Enunciado: 
# Pedirle al usuario un número n, y crear una matriz cuadrada -> n x n
# Pedirle al usuario un "j" y eliminar la columna j de la matriz original.
n = int(input())
M = []
k = 1
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(k)
        k += 1
    M.append(fila)
print(M)

j = int(input()) - 1

M_new = []
for i in range(len(M)):
    fila_new = []
    for x in range(len(M[i])):
        if x != j:
            fila_new.append(M[i][x])
    M_new.append(fila_new)

for h in M_new:
    print(h)


# 






