# 10.- DATOS COMPUESTOS: LISTAS (II) — PATRONES AVANZADOS, ANIDADAS Y COMPRENSIONES
# ---------------------------------------------------------------
# B) LISTAS ANIDADAS (MATRICES): CREACIÓN Y RECORRIDO
# ---------------------------------------------------------------
# Matriz 3x3 fija:

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(M[1])
print(M[1][1])  # Extraer el número 5, posición 1,1  

# Recorridos:
# - Por filas
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = 0
for fila in M: #Ciclo más externo
    for val in fila: #Ciclo interno
        s += val
print(s)

# fila
# Iteracion 1 -> fila = [1, 2, 3] Ciclo interno (val in fila) Val ->  1 Val -> 2 Val-> 3  
# Iteracion 2 -> fila = [4, 5, 6] Ciclo interno (val in fila) Val ->  4 Val -> 5 Val-> 6 
# Iteracion 3 -> fila = [7, 8, 9] Ciclo interno (val in fila) Val ->  7 Val -> 8 Val-> 9 

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# - Por índices (i, j)
total = 0
for i in range(len(M)): #range(3)
    for j in range(len(M[i])): #range(3)
        total = total + M[i][j]
print(total)

# Construcción programática de matriz r x c con ceros
r = 3; c = 4
Z = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(0)
    Z.append(row)
print(Z)

# ---------------------------------------------------------------
# C) CONSTRUCCIÓN PROGRAMÁTICA: TABLAS Y PATRONES
# ---------------------------------------------------------------
# Tabla de multiplicar 1..r por 1..c (guardada en matriz T)
r = 3; c = 5
T = []
for i in range(1, r+1):
    row = []
    for j in range(1, c+1):
        row.append(i*j)
    T.append(row)
print(T)

# Patrón de tablero (caracteres)
n = 5
board = []
for i in range(n):
    row = []
    for j in range(n):
        if (i + j) % 2 == 0:
            row.append("#")
        else:
            row.append(".")
    board.append(row)
print( board)

# ---------------------------------------------------------------
# D) BÚSQUEDA, FILTRADO Y TRANSFORMACIÓN (SIN FUNCIONES)
# ---------------------------------------------------------------
# Búsqueda de un valor v en M: devuelve (i,j) de la primera aparición o (-1,-1)
v = 6
pi = -1; pj = -1
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == v and pi == -1:
            pi = i; pj = j
print(v, (pi, pj))

# Filtrar pares de una lista L en R (mantener orden)
L = [5, 2, 8, 7, 4, 9]
R = []
for x in L:
    if x % 2 == 0:
        R.append(x)
print(R)

# Transformar: sumar 1 a cada elemento de L en una NUEVA lista
L2 = []
for x in L:
    L2.append(x + 1)
print("L2:", L2)

# ---------------------------------------------------------------
# E) ORDENAMIENTOS BÁSICOS (MANUALES)
# ---------------------------------------------------------------
# Burbuja ascendente (bubble sort) sobre copia para no tocar original
A = [7, 3, 9, 1, 4]
B = A[:]  
n = len(B)
for i in range(n-1):
    for j in range(n-1-i):
        if B[j] > B[j+1]:
            tmp = B[j]
            B[j] = B[j+1]
            B[j+1] = tmp
print(B)

# Selección ascendente (selection sort)
C = A[:]
n = len(C)
for i in range(n-1):
    min_pos = i
    for j in range(i+1, n):
        if C[j] < C[min_pos]:
            min_pos = j
    # swap
    tmp = C[i]; C[i] = C[min_pos]; C[min_pos] = tmp
print(C)

# ---------------------------------------------------------------
# F) CONVERSIÓN TEXTO<->LISTA: SPLIT Y JOIN
# ---------------------------------------------------------------
# split: separa una cadena en lista por separador (por defecto, espacios)
line = "uno dos   tres"
parts = line.split()  # maneja espacios múltiples
print(parts)

csv = "a,b,c,,d"
parts2 = csv.split(",")  # separador explícito
print(parts2)

# join: une elementos de una lista de strings con un separador
joined = "-".join(["A", "B", "C"])
print(joined)

# ---------------------------------------------------------------
# G) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:
nums = [1,2,3,4,5,6]

squares = []
for x in nums:
    squares.append(x**2)
print(squares)

# cuadrados de la lista
squares_even = [x**2 for x in nums]
# Eleva al cuadrado únicamente los números pares
squares_even = [x**2 for x in nums if x % 2 == 0]
# eleva al cuadrado los pares y al cubo los impares
squares_even = [x**2 if x % 2 == 0 else x**3 for x in nums]
print(squares_even)

# longitudes de palabras con 3+ letras
words = ["sol", "luz", "programa", "if", "for"]
lengths = [w for w in words if len(w) < 4]

lista = []
for w in words:
    if len(w) < 4:
        lista.append(w)

print(lengths)

# ---------------------------------------------------------------
# H) FUNCIÓN MAP USANDO LAMBDA
# ---------------------------------------------------------------
nums1 = [7,8,9,10,11,12,13]
nums2 = [1,2,3,4,5,6]

cubos = list(map(lambda x: x**3, nums))
print(cubos)

lista = []
for i, j in zip(nums1, nums2):
    print(i, j)
    lista.append((i+j))
print(lista)

sumas = list(map(lambda x, y: x+y, nums1, nums2))
print(sumas)

nums = ["1","2","3","4","5","6"]
enteros = list(map(lambda x: int(x), nums))
print(enteros)

# Ejercicio 14 - Borrar columna i
# Enunciado: Lee una matriz (lista de listas) y elimina la columna i seleccionada por el usuario
# INPUT
#[
# [1,2,3],
# [4,5,6],
# [7,8,9]
#]
# Elimina 1

# OUTPUT
#[
# [2,3],
# [5,6],
# [8,9]
#]

M = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
target = int(input())
target = target - 1
lista = []
for i in range(len(M)):
    lista2 = []
    for j in range(len(M[i])):
        if j != target:
            lista2.append(M[i][j])
    lista.append(lista2)

for i in lista:
    print(i)

# Ejercicio 15 - Cambia el target por 0
# Enunciado: Lee una matriz (lista de listas) y cambia el target del usuario por un 0
# INPUT
#[
# [5,2,3],
# [4,5,6],
# [5,8,9]
#]
# Target -> 5

# OUTPUT
#[
# [0,2,3],
# [4,0,6],
# [0,8,9]
#]
M = [
        [5,2,3],
        [4,5,6],
        [5,8,9]
]
target = int(input())
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == target:
            M[i][j] = 0

for i in M:
    print(i)


# .split() Tienes un texto, hace cortes en el caracter que tú le des y te devuelve una lista
# . join() Tienes una lista, le das el caracter de union, y te devuelve un texto

texto = "1, 2, 3, 4, 5, 6"
lista = texto.split(",")
lista = list(map(lambda x: x.strip(), lista))

texto_final = ", ".join(lista)
texto_final

lista = eval(input())
resultado = [lista[i] for i in range(len(lista)) if i % 2 == 0]
print(str(resultado).replace(", ",","))

lista = "[[1, 2, 3],[4, 5, 6],[7, 8, 9]]"
lista_externa = []
for i in range(len(lista)):
    if (lista[i-1] == "[" and lista[i] == "[") or (lista[i-1] == "," and lista[i] == "["):
        lista_interna = []
        for j in range(i,len(lista)):
            if lista[j].isdigit():
                lista_interna.append(int(lista[j]))
            if (lista[j-1] == "]" and lista[j] == ",") or (lista[j-1] == "]" and lista[j] == "]"):
                break
        lista_externa.append(lista_interna)

print(lista_externa)
        


n = int(input())
cuadrados = [i**2 for i in range(1, n+1)]
print(str(cuadrados).replace(", " , ","))

n = int(input())
cuadrados = [str(i**2) for i in range(1, n+1)]
print("[" + ",".join(cuadrados) +"]")

lista = eval(input().strip())
mayusculas = [i.upper() for i in lista]
print(str(mayusculas).replace(", ",","))

lista = input()
lista = lista[1:-1]
palabras = lista.split(",") if lista else []
palabras_final = []
for i in palabras:
    palabras_final.append(i[1:-1])

mayusculas = [i.upper() for i in palabras_final]
print(str(mayusculas).replace(", ",","))

lista = input().strip()
# [1,2,3,4,5]
lista = lista[1:-1]
numeros_str = lista.split(",") if lista else []
numeros = [int(i) for i in numeros_str]
numeros = list(map(lambda x: int(x), numeros_str))

lista = input().strip()
# ["apple","banana","orange"]
lista = lista[1:-1]
palabras_str = lista.split(",") if lista else []
palabras = [i[1:-1] for i in palabras_str]

vocales = "aeiou"
suma_palabras = 0
i = 0
while i < len(palabras):
    if palabras[i][0].lower() in vocales:
        suma_palabras += 1
    i += 1

print(suma_palabras)

#Problema 03
lista = input().strip()
# [56,78]
lista = lista[1:-1]
numeros_str = lista.split(",") if lista else []
numeros = [int(i) for i in numeros_str]

resultado = []
i = 0
while i < len(numeros):
    n = numeros[i]
    invertido = 0
    if n == 0:
        invertido = 0
    else:
        while n > 0:
            digito = n % 10
            invertido = invertido * 10 + digito
            n //= 10
    resultado.append(invertido)
    i += 1

print(str(resultado).replace(", ", ","))
