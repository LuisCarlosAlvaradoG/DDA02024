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
# str -> lista
cadena = "1,2,3,4,5"
lista = cadena.split(",")
print(lista)

# join: une elementos de una lista de strings con un separador
# list -> str
lista = ['1', '2', '3', '4', '5']
cadena = ",".join(lista)
print(cadena)

# ---------------------------------------------------------------
# F) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:
lista = [1, 2, 3, 4, 5]
cuadrados = []
for i in lista:
    cuadrados.append(i**2)
print(cuadrados)

cuadrados_comp = [i**2 for i in lista]  # Operacion -> Ciclo for
print(cuadrados_comp)

numeros_str = ["1", "2", "3", "4", "5"]
numeros_int = [int(i) for i in numeros_str]
print(numeros_int)

lista = [1, 2, 3, 4, 5]
# Operacion -> Ciclo for -> Estructura if
cuadrados_pares = [i**2 for i in lista if i % 2 == 0]
print(cuadrados_pares)

lista = [1, 2, 3, 4, 5]
#Elevar al cuadrado los pares y al cubo los impares
# Operacion -> Estructura if-else -> Ciclo for
cuadrados_mixto = [i**2 if i % 2 == 0 else i**3 for i in lista]
print(cuadrados_mixto)

cuadrados_mixto = []
for i in lista:
    if i % 2==0:
        cuadrados_mixto.append(i**2)
    else:
        cuadrados_mixto.append(i**3)
# ---------------------------------------------------------------
# G) FUNCIÓN MAP USANDO LAMBDA
# ---------------------------------------------------------------

lista = [1, 2, 3, 4, 5]
# lambda -> Que variable voy a recibir y qué hacerle a la variable
# iterable -> las elementos que se convertirán en x
# map -> mapear todos los elementos de la iterable
# list -> convierte el objeto map en una lista
cuadrados = list(map(lambda x: x ** 2, lista))
print(cuadrados)

numeros_str = ["1", "2", "3", "4", "5"]
numeros_int = list(map(lambda i: int(i), numeros_str))
print(numeros_int)

entrada = int(input())
cuadrados = str([i**2 for i in range(1, entrada+1)])
print(cuadrados.replace(" ",""))

lista = ["1", "2", "3"]
",".join(lista)

n = int(input())
lista = [str(i) for i in range(1, n+1) if n%i == 0]

new_list = []
for i in range(1, n+1):
    if n%i == 0:
        new_list.append(str(i))
    
entrada = [[1,2],[3,4],[5]]
new_list = []
for sublista in entrada:
    for j in sublista:
        new_list.append(j)
print(new_list)