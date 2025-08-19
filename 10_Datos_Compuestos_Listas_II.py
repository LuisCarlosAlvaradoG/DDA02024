
# ===============================================================
# 10.- DATOS COMPUESTOS: LISTAS (II) — PATRONES AVANZADOS, ANIDADAS Y COMPRENSIONES
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
# Reglas pedagógicas de este archivo .py:
#   - Avanzamos en el manejo de listas: listas de listas (matrices simples),
#     construcción programática con bucles, búsqueda/transformación avanzadas,
#     algoritmos básicos de ordenamiento y COMPRENSIONES (nivel básico: 1 for con filtro opcional).
#   - SOLO usamos lo ya visto: for, range, while, if/elif/else, try-except,
#     contadores, acumuladores, centinelas, operaciones con números y cadenas, depurador.
#   - ESTRICTAMENTE PROHIBIDO: tuplas, diccionarios, funciones definidas por el usuario,
#     librerías externas, archivos, parámetros 'key' en sort (requiere funciones), break/continue.
#   - En comprensiones NO usamos "if-else" dentro de la expresión (tema posterior).
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Listas anidadas (matrices): creación, recorrido por filas/columnas
#   C) Construcción programática (for anidados): tablas y patrones
#   D) Búsqueda, filtrado y transformación (sin funciones)
#   E) Ordenamientos básicos (burbuja y selección) sin funciones
#   F) Conversión texto<->lista: split y join
#   G) Comprensiones de listas (básicas): [expr for ... if ...]
#   H) Casos de uso guiados
#   I) Buenas prácticas y depuración en estructuras anidadas
#   J) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Construir y manipular listas de listas (matrices simples).
# - Aplicar for anidados para recorrer filas y columnas.
# - Implementar algoritmos sencillos de búsqueda, filtrado y ordenamiento manual.
# - Convertir entre texto y listas (split/join) de forma controlada.
# - Introducir comprensiones de listas como atajo sintáctico (una sola cláusula for y filtro opcional).

# ---------------------------------------------------------------
# B) LISTAS ANIDADAS (MATRICES): CREACIÓN Y RECORRIDO
# ---------------------------------------------------------------
# Matriz 3x3 fija:
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("M:", M)
print("M[0][1] =", M[0][1])   # 2

# Recorridos:
# - Por filas
s = 0
for row in M:
    for val in row:
        s = s + val
print("Sum M:", s)

# - Por índices (i, j)
total = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        total = total + M[i][j]
print("Total by indices:", total)

# Construcción programática de matriz r x c con ceros
r = 3; c = 4
Z = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(0)
    Z.append(row)
print("Zero matrix:", Z)

# Nota sobre alias: NO hagas Z = [[0]*c]*r (produciría alias de filas).

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
print("Table:", T)

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
print("Board:", board)

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
print("First pos of", v, "->", (pi, pj))

# Filtrar pares de una lista L en R (mantener orden)
L = [5, 2, 8, 7, 4, 9]
R = []
for x in L:
    if x % 2 == 0:
        R.append(x)
print("Even filter:", R)

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
B = A[:]  # copia
n = len(B)
for i in range(n-1):
    for j in range(n-1-i):
        if B[j] > B[j+1]:
            tmp = B[j]
            B[j] = B[j+1]
            B[j+1] = tmp
print("Bubble asc:", B)

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
print("Selection asc:", C)

# ---------------------------------------------------------------
# F) CONVERSIÓN TEXTO<->LISTA: SPLIT Y JOIN
# ---------------------------------------------------------------
# split: separa una cadena en lista por separador (por defecto, espacios)
line = "uno dos   tres"
parts = line.split()  # maneja espacios múltiples
print("split default:", parts)

csv = "a,b,c,,d"
parts2 = csv.split(",")  # separador explícito
print("split(','):", parts2)

# join: une elementos de una lista de strings con un separador
joined = "-".join(["A", "B", "C"])
print("join ->", joined)

# ---------------------------------------------------------------
# G) COMPRENSIONES DE LISTAS (BÁSICAS)
# ---------------------------------------------------------------
# Regla en esta sesión: SOLO una cláusula for y un filtro opcional "if".
# Sin 'if-else' dentro de la expresión y sin anidar comprensiones.
#
# Ejemplos:
nums = [1,2,3,4,5,6]
# cuadrados de números pares
squares_even = [x*x for x in nums if x % 2 == 0]
print("squares_even:", squares_even)

# longitudes de palabras con 3+ letras
words = ["sol", "luz", "programa", "if", "for"]
lengths = [len(w) for w in words if len(w) >= 3]
print("lengths >=3:", lengths)

# ---------------------------------------------------------------
# H) CASOS DE USO GUIADOS
# ---------------------------------------------------------------
# Caso 1) Leer matriz r x c de enteros y calcular suma por filas y por columnas
# (Descomenta para usar en clase)
# r = int(input("rows: "))
# c = int(input("cols: "))
# M = []
# for i in range(r):
#     row = []
#     for j in range(c):
#         row.append(int(input("M["+str(i)+"]["+str(j)+"]: ")))
#     M.append(row)
# # sumas por fila
# row_sums = []
# for i in range(r):
#     s = 0
#     for j in range(c):
#         s = s + M[i][j]
#     row_sums.append(s)
# # sumas por columna
# col_sums = []
# for j in range(c):
#     s = 0
#     for i in range(r):
#         s = s + M[i][j]
#     col_sums.append(s)
# print("Row sums:", row_sums)
# print("Col sums:", col_sums)

# Caso 2) Normalizar y tokenizar una línea (lower + split), contar tokens
# line = input("Line: ").strip().lower()
# toks = line.split()
# print("Tokens:", toks, "Count:", len(toks))

# Caso 3) Construir una nueva lista con elementos únicos (preservar orden)
# L = input("Enter items separated by space: ").split()
# R = []
# for x in L:
#     seen = False
#     for y in R:
#         if y == x: seen = True
#     if not seen:
#         R.append(x)
# print("Unique:", R)

# ---------------------------------------------------------------
# I) BUENAS PRÁCTICAS Y DEPURACIÓN EN ESTRUCTURAS ANIDADAS
# ---------------------------------------------------------------
# - Evita alias involuntario al crear matrices: usa bucles para generar filas independientes.
# - Verifica límites: len(M), len(M[i]) antes de acceder a M[i][j].
# - En ordenamientos manuales, imprime trazas parciales (primeras/últimas iteraciones) si dudas.
# - En comprensiones, mantén expresiones simples y legibles; prefiere bucles si la lógica crece.

# ---------------------------------------------------------------
# J) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Cada ejercicio incluye la solución completa para el docente.

# ---------------------------------------------------------------
# Ejercicio 01 - Matriz identidad
# Enunciado: 
# Read n and build an identity matrix n x n (1 on diagonal, 0 elsewhere).
n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    M.append(row)
print(M)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Transpuesta de matriz
# Enunciado: 
# Read r,c and a matrix; output its transpose.
r = int(input("rows: "))
c = int(input("cols: "))
A = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("A["+str(i)+"]["+str(j)+"]: "))
    A.append(row)
T = []
for j in range(c):
    row = []
    for i in range(r):
        row.append(A[i][j])
    T.append(row)
print(T)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Suma de matrices (mismo tamaño)
# Enunciado: 
r = int(input("rows: "))
c = int(input("cols: "))
A = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("A["+str(i)+"]["+str(j)+"]: ")))
    A.append(row)
B = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("B["+str(i)+"]["+str(j)+"]: ")))
    B.append(row)
C = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print(C)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Buscar en matriz (primera y última aparición)
# Enunciado: 
r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
target = input("target: ")
first = (-1, -1)
last = (-1, -1)
for i in range(r):
    for j in range(c):
        if M[i][j] == target:
            if first == (-1, -1):
                first = (i, j)
            last = (i, j)
print("first:", first, "last:", last)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Eliminar columna j
# Enunciado: 
# Read matrix and remove column j from all rows if valid.
r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
jrm = int(input("column to remove: "))
if 0 <= jrm < c:
    R = []
    for i in range(r):
        row = []
        for j in range(c):
            if j != jrm:
                row.append(M[i][j])
        R.append(row)
    print(R)
else:
    print("Invalid column")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Flatten (aplanar) matriz
# Enunciado: 
# Read r,c and flatten matrix row-wise into a single list.
r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
R = []
for i in range(r):
    for j in range(c):
        R.append(M[i][j])
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Burbuja descendente
# Enunciado: 
# Implement bubble sort descending.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
n = len(L)
for i in range(n-1):
    for j in range(n-1-i):
        if L[j] < L[j+1]:
            tmp = L[j]; L[j] = L[j+1]; L[j+1] = tmp
print(L)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Selección descendente
# Enunciado: 
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
n = len(L)
for i in range(n-1):
    max_pos = i
    for j in range(i+1, n):
        if L[j] > L[max_pos]:
            max_pos = j
    tmp = L[i]; L[i] = L[max_pos]; L[max_pos] = tmp
print(L)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Filtrado con comprensión (pares)
# Enunciado: 
# Read integers and build list of even numbers using a basic comprehension.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
E = [x for x in L if x % 2 == 0]
print(E)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Transformación con comprensión (cuadrados)
# Enunciado: 
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
S = [x*x for x in L]
print(S)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Contar positivos por filas
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
counts = []
for i in range(r):
    cnt = 0
    for j in range(c):
        if M[i][j] > 0: cnt = cnt + 1
    counts.append(cnt)
print(counts)


# ---------------------------------------------------------------
# Ejercicio 12 - Suma diagonal principal
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
s = 0.0
for i in range(n):
    s = s + M[i][i]
print(s)


# ---------------------------------------------------------------
# Ejercicio 13 - Suma diagonal secundaria
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
s = 0.0
for i in range(n):
    s = s + M[i][n-1-i]
print(s)


# ---------------------------------------------------------------
# Ejercicio 14 - Borrar fila i
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
irm = int(input("row to remove: "))
if 0 <= irm < r:
    R = []
    for i in range(r):
        if i != irm:
            R.append(M[i])
    print(R)
else:
    print("Invalid row")


# ---------------------------------------------------------------
# Ejercicio 15 - Matriz escalera (triángulo superior 1)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        if j >= i:
            row.append(1)
        else:
            row.append(0)
    M.append(row)
print(M)


# ---------------------------------------------------------------
# Ejercicio 16 - Multiplicación escalar de matriz
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
k = float(input("k: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
R = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(M[i][j] * k)
    row = row
    R.append(row)
print(R)


# ---------------------------------------------------------------
# Ejercicio 17 - Tokens únicos (preservando orden) con split
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

line = input("Line: ").strip()
tokens = line.split()
unique = []
for t in tokens:
    seen = False
    for u in unique:
        if u == t: seen = True
    if not seen:
        unique.append(t)
print(unique)


# ---------------------------------------------------------------
# Ejercicio 18 - Join con separador personalizado
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("word: "))
sep = input("sep: ")
print(sep.join(L))


# ---------------------------------------------------------------
# Ejercicio 19 - Ordenar por burbuja solo parte de la lista [l..r]
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
l = int(input("l: "))
r = int(input("r: "))
if 0 <= l <= r < len(L):
    n = r - l + 1
    # bubble on window
    i = 0
    while i < n-1:
        j = l
        while j < l + n - 1 - i:
            if L[j] > L[j+1]:
                tmp = L[j]; L[j] = L[j+1]; L[j+1] = tmp
            j = j + 1
        i = i + 1
print(L)


# ---------------------------------------------------------------
# Ejercicio 20 - Seleccionar columnas pares de matriz
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
R = []
for i in range(r):
    row = []
    for j in range(0, c, 2):
        row.append(M[i][j])
    R.append(row)
print(R)


# ---------------------------------------------------------------
# Ejercicio 21 - Contar apariciones de cada token (sin diccionarios)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Build two parallel lists: tokens and counts
line = input("Line: ")
tokens = line.split()
V = []     # unique tokens
C = []     # counts
for t in tokens:
    pos = -1
    for i in range(len(V)):
        if V[i] == t:
            pos = i
    if pos == -1:
        V.append(t); C.append(1)
    else:
        C[pos] = C[pos] + 1
print("V:", V)
print("C:", C)


# ---------------------------------------------------------------
# Ejercicio 22 - Diagonalizar desde un vector (n)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
v = []
for _ in range(n):
    v.append(input("v: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(v[i])
        else:
            row.append(0)
    M.append(row)
print(M)


# ---------------------------------------------------------------
# Ejercicio 23 - Comprensión con filtro de longitud
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("word: "))
k = int(input("min length: "))
R = [w for w in L if len(w) >= k]
print(R)


# ---------------------------------------------------------------
# Ejercicio 24 - Cuadrados pares en rango
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
R = [x*x for x in range(a, b+1) if x % 2 == 0]
print(R)


# ---------------------------------------------------------------
# Ejercicio 25 - Normalizar espacios con split/join
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
toks = s.split()
print(" ".join(toks))


# ---------------------------------------------------------------
# Ejercicio 26 - Perímetro de contorno (matriz de 0/1)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Count how many 1's are on the border of an r x c matrix.
r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
per = 0
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            if M[i][j] == 1:
                per = per + 1
print(per)


# ---------------------------------------------------------------
# Ejercicio 27 - Matriz espejo horizontal
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
R = []
for i in range(r):
    row = []
    left = 0; right = c-1
    while left <= right:
        row.append(M[i][right])
        right = right - 1
    R.append(row)
print(R)


# ---------------------------------------------------------------
# Ejercicio 28 - Rotación de lista k veces a la izquierda (manual)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
k = int(input("k: "))
k = k % len(L) if len(L) > 0 else 0
R = L[k:] + L[:k]
print(R)


# ---------------------------------------------------------------
# Ejercicio 29 - Intersección de listas (sin conjuntos)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(input("A: "))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(input("B: "))
R = []
for x in A:
    # include x if appears in B and not already included (to avoid duplicates)
    found = False
    for y in B:
        if y == x: found = True
    already = False
    for z in R:
        if z == x: already = True
    if found and not already:
        R.append(x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 30 - Diferencia A\B (sin conjuntos)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(input("A: "))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(input("B: "))
R = []
for x in A:
    inB = False
    for y in B:
        if y == x: inB = True
    if not inB:
        # also avoid duplicates in R
        seen = False
        for z in R:
            if z == x: seen = True
        if not seen:
            R.append(x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 31 - Zigzag de matriz
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
R = []
for i in range(r):
    if i % 2 == 0:
        for j in range(c):
            R.append(M[i][j])
    else:
        j = c-1
        while j >= 0:
            R.append(M[i][j])
            j = j - 1
print(R)


# ---------------------------------------------------------------
# Ejercicio 32 - Triángulo inferior (1 bajo diagonal)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        if j <= i:
            row.append(1)
        else:
            row.append(0)
    M.append(row)
print(M)


# ---------------------------------------------------------------
# Ejercicio 33 - Comprensión: letras mayúsculas de una cadena
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
U = [ch for ch in s if "A" <= ch <= "Z"]
print(U)


# ---------------------------------------------------------------
# Ejercicio 34 - Comprensión: tokens numéricos a enteros (validando)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Build list of ints only from tokens that are all digits (no signs).
toks = input("Tokens: ").split()
R = []
for t in toks:
    ok = True
    for ch in t:
        if not ("0" <= ch <= "9"):
            ok = False
    if ok:
        R.append(int(t))
print(R)


# ---------------------------------------------------------------
# Ejercicio 35 - Ordenar filas de matriz por burbuja (independiente)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
# bubble each row ascending
for i in range(r):
    n = len(M[i])
    a = 0
    while a < n-1:
        b = 0
        while b < n-1-a:
            if M[i][b] > M[i][b+1]:
                tmp = M[i][b]; M[i][b] = M[i][b+1]; M[i][b+1] = tmp
            b = b + 1
        a = a + 1
print(M)


# ---------------------------------------------------------------
# Ejercicio 36 - Recorrer bordes de matriz en orden horario
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M.append(row)
R = []
# top row
for j in range(c):
    R.append(M[0][j])
# right col
for i in range(1, r):
    R.append(M[i][c-1])
# bottom row (if more than 1 row)
if r > 1:
    j = c-2
    while j >= 0:
        R.append(M[r-1][j])
        j = j - 1
# left col (if more than 1 col)
if c > 1:
    i = r-2
    while i >= 1:
        R.append(M[i][0])
        i = i - 1
print(R)


# ---------------------------------------------------------------
# Ejercicio 37 - Filtro de matriz por umbral (binaria)
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
T = float(input("threshold: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
B = []
for i in range(r):
    row = []
    for j in range(c):
        if M[i][j] >= T:
            row.append(1)
        else:
            row.append(0)
    B.append(row)
print(B)


# ---------------------------------------------------------------
# Ejercicio 38 - Reemplazar por promedio de fila
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("rows: "))
c = int(input("cols: "))
M = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(float(input("M["+str(i)+"]["+str(j)+"]: ")))
    M.append(row)
R = []
for i in range(r):
    s = 0.0
    for j in range(c):
        s = s + M[i][j]
    avg = s / c if c != 0 else 0.0
    row = []
    for j in range(c):
        row.append(avg)
    R.append(row)
print(R)


# ---------------------------------------------------------------
# Ejercicio 39 - Comprensión: duplicar tokens que no sean 'x'
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

toks = input("Tokens: ").split()
R = [t+t for t in toks if t != "x"]
print(R)


# ---------------------------------------------------------------
# Ejercicio 40 - Diagonal secundaria con ceros fuera
# Enunciado: Ejercicio práctico de listas avanzadas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
M = []
for i in range(n):
    row = []
    for j in range(n):
        if j == n-1-i:
            row.append(1)
        else:
            row.append(0)
    M.append(row)
print(M)

