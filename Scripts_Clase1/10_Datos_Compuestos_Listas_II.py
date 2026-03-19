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
print(M[1][0])
print(len(M))
print(len(M[0]))
# Recorridos:
# - Por filas
suma = 0
for i in M:
    for j in i:
        suma += j
print(suma)

suma = 0
for fila in M:
    for num in fila:
        suma += num
print(suma)
# - Por índices (i, j)
suma = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        suma += M[i][j]
print(suma)
# Construcción programática de matriz r x c con ceros


# ---------------------------------------------------------------
# B) CONSTRUCCIÓN PROGRAMÁTICA: TABLAS Y PATRONES
# ---------------------------------------------------------------
# Tabla de multiplicar 1..r por 1..c (guardada en matriz T)

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

