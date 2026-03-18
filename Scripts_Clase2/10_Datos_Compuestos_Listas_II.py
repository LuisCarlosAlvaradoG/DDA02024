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

# join: une elementos de una lista de strings con un separador

# ---------------------------------------------------------------
# F) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:


# ---------------------------------------------------------------
# G) FUNCIÓN MAP USANDO LAMBDA
# ---------------------------------------------------------------

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
