
# ===============================================================
# 9.- DATOS COMPUESTOS: LISTAS (I) — BASES Y PATRONES FUNDAMENTALES
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
# Reglas pedagógicas de este archivo .py:
#   - Introducimos LISTAS: creación, acceso, mutación, recorrido y métodos básicos.
#   - SOLO usamos conceptos ya vistos: entrada/salida, operaciones con números y cadenas,
#     condicionales (simples/dobles/múltiples/anidadas), try-except, while, for y range,
#     contadores, acumuladores, centinelas y depuración con prints.
#   - ESTRICTAMENTE PROHIBIDO: tuplas, diccionarios, funciones definidas por el usuario,
#     librerías externas, archivos, parámetros 'key' en sort (requiere funciones), break/continue.
#   - NO usamos comprensiones de listas en esta primera parte (se verán en Listas II).
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: ¿Qué es una lista? creación, mutabilidad, tipos de elementos
#   C) Índices, cortes (slices) y modificación in-place
#   D) Recorridos: for por elemento / por índice; while con índice
#   E) Métodos básicos: append, insert, extend, remove, pop, clear, index, count, reverse, sort
#   F) Construcción de listas a partir de entradas (fijo, centinela, validación)
#   G) Casos de uso guiados
#   H) Ventajas, desventajas y buenas prácticas (incluye depuración)
#   I) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Comprender la estructura y propiedades de las listas (mutables, ordenadas).
# - Crear listas y manipular sus elementos por índice.
# - Aplicar recorridos con for/while para contar, acumular, buscar y transformar.
# - Utilizar métodos básicos de listas sin adelantarnos a funciones ni colecciones avanzadas.
# - Construir listas a partir de entradas del usuario con cantidad fija o con centinela.

# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UNA LISTA?
# ---------------------------------------------------------------
# Definición:
# - Una lista es una colección ORDENADA y MUTABLE de elementos.
# - Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Ejemplos:
nums = [10, 20, 30]             # lista de enteros
words = ["uno", "dos", "tres"]  # lista de cadenas
mix = [1, "A", 2.5]             # mezcla (posible), pero en el curso RECOMENDAMOS homogeneidad
empty = []                       # lista vacía
print(nums, words, mix, empty)
#
# Propiedades:
# - Ordenada: mantiene el orden de inserción y acceso por posición (índice).
# - Mutable: se puede cambiar un elemento específico o rebanadas.
# - Tamaño dinámico: puede crecer/disminuir con métodos como append()/pop().
# - Homogeneidad recomendada: para claridad, usa listas "de lo mismo" (todos números o todas cadenas).

# ---------------------------------------------------------------
# C) ÍNDICES, CORTES (SLICES) Y MODIFICACIÓN IN-PLACE
# ---------------------------------------------------------------
# Índices:
# - El primer elemento está en índice 0. El último en len(lista) - 1.
# - Índices negativos: -1 -> último, -2 -> penúltimo, etc.
a = [5, 6, 7, 8]
print("a[0] =", a[0], "a[1] =", a[1], "a[-1] =", a[-1])

# Asignación a posiciones:
a[1] = 60       # modifica el segundo elemento
print("a modificado:", a)

# Cortes (slices):
# - a[inicio:fin] devuelve una SUBLISTA desde inicio hasta fin-1.
# - a[:k] desde el inicio hasta k-1; a[k:] desde k hasta el final; a[:] copia completa.
b = [10, 20, 30, 40, 50, 60]
print("b[1:4] ->", b[1:4])     # [20,30,40]
print("b[:3]  ->", b[:3])      # [10,20,30]
print("b[3:]  ->", b[3:])      # [40,50,60]
print("b[:]   ->", b[:])       # copia superficial (shallow copy)

# Asignación con slices (reemplazo de segmentos):
b[1:3] = [200, 300]            # reemplaza 20,30 por 200,300
print("b slice-replace:", b)

# Eliminar segmentos con slices vacíos:
b[2:4] = []                    # elimina posiciones 2 y 3
print("b slice-delete:", b)

# ---------------------------------------------------------------
# D) RECORRIDOS: FOR POR ELEMENTO / POR ÍNDICE; WHILE CON ÍNDICE
# ---------------------------------------------------------------
lst = [3, 7, 2, 9]
# For por elemento:
total = 0
for x in lst:
    total = total + x
print("Sum (for by element):", total)

# For por índice:
total2 = 0
for i in range(len(lst)):
    total2 = total2 + lst[i]
print("Sum (for by index):", total2)

# While con índice:
i = 0
total3 = 0
while i < len(lst):
    total3 = total3 + lst[i]
    i = i + 1
print("Sum (while by index):", total3)

# Búsqueda lineal: ¿existe el 7?
found = False
for x in lst:
    if x == 7:
        found = True
print("Contains 7?", found)

# ---------------------------------------------------------------
# E) MÉTODOS BÁSICOS DE LISTA (SIN KEY, SIN FUNCIONES AVANZADAS)
# ---------------------------------------------------------------
m = [1, 2, 3]
m.append(4)         # agrega al final
print("append ->", m)
m.insert(1, 99)     # inserta 99 en índice 1 (desplaza a la derecha)
print("insert ->", m)

n = [10, 20]
m.extend(n)         # extiende con elementos de n
print("extend ->", m)

m.remove(99)        # elimina la PRIMERA aparición de 99 (ValueError si no está)
print("remove ->", m)

last = m.pop()      # saca y retorna el último
print("pop() ->", last, "| m ->", m)
mid = m.pop(2)      # saca y retorna elemento en índice 2
print("pop(2) ->", mid, "| m ->", m)

print("count(2) ->", m.count(2))   # cuántas veces aparece 2
print("index(2) ->", m.index(2))   # primer índice de 2 (ValueError si no está)

m.reverse()         # invierte in-place
print("reverse ->", m)

m.sort()            # ordena ascendente in-place (SOLO números o SOLO cadenas)
print("sort asc ->", m)
m.sort(reverse=True)
print("sort desc ->", m)

# Copia superficial vs alias:
u = [5, 6, 7]
v = u              # alias: apuntan al mismo objeto
w = u[:]           # copia superficial independiente (para elementos "simples")
u[0] = 500
print("alias v:", v, "| copy w:", w)

# ---------------------------------------------------------------
# F) CONSTRUCCIÓN DE LISTAS DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija (for + range)
# (Descomenta para usar en clase)
# N = int(input("How many integers? "))
# L = []
# for i in range(N):
#     val = int(input("Value " + str(i+1) + ": "))
#     L.append(val)
# print("L =", L)

# F2) Centinela textual (while) hasta 'fin'
# (Descomenta para usar en clase)
# L = []
# raw = input("Value (or 'fin'): ")
# while raw.strip().lower() != "fin":
#     try:
#         x = float(raw)
#         L.append(x)
#     except ValueError:
#         print("Invalid:", raw)
#     raw = input("Value (or 'fin'): ")
# print("Collected:", L)

# F3) Validación por rango
# (Descomenta para usar en clase)
# N = int(input("How many [1..5]? "))
# L = []
# for _ in range(N):
#     valid = False
#     while not valid:
#         r = input("Enter int [1..5]: ")
#         try:
#             v = int(r)
#             if 1 <= v <= 5:
#                 L.append(v)
#                 valid = True
#             else:
#                 print("Out of range.")
#         except ValueError:
#             print("Not an integer.")
# print("Validated list:", L)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Suma, promedio, mínimo y máximo en una lista
# L = [10, 5, 8, 15, 3]
# acc = 0
# for x in L:
#     acc = acc + x
# mn = L[0]; mx = L[0]
# for x in L:
#     if x < mn: mn = x
#     if x > mx: mx = x
# avg = acc / len(L)
# print("Sum:", acc, "Avg:", avg, "Min:", mn, "Max:", mx)

# Caso 2) Filtrar positivos en una nueva lista (sin comprensiones)
# L = [3, -2, 0, 7, -5, 9]
# P = []
# for x in L:
#     if x > 0:
#         P.append(x)
# print("Positives:", P)

# Caso 3) Eliminar TODAS las apariciones de un valor dado (sin funciones avanzadas)
# L = [2, 3, 2, 4, 2, 5]
# val = 2
# R = []
# for x in L:
#     if x != val:
#         R.append(x)
# print("Removed all", val, "->", R)

# Caso 4) Unir dos listas por concatenación y por extend
# A = [1,2,3]
# B = [4,5]
# C = A + B       # crea NUEVA lista
# print("A+B ->", C)
# A_copy = A[:]   # copia antes de modificar
# A_copy.extend(B) # modifica A_copy in-place
# print("extend ->", A_copy)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Estructura flexible y muy utilizada.
# - Permite mutación y crecimiento dinámico.
# - Facilidad para recorrer y transformar con for/while.
#
# Desventajas / riesgos:
# - IndexError si usas índices fuera de rango.
# - ValueError con remove()/index() si el elemento no existe.
# - ALIAS sin querer: dos variables referenciando la misma lista pueden causar efectos indirectos.
#
# Buenas prácticas:
# - Verifica len(lista) antes de acceder por índice.
# - Maneja excepciones de remove/index con try-except o verifica pertenencia con 'in'.
# - Para copiar usa lista[:] o list(lista) (copia superficial).
# - Usa banderas DEBUG y prints en iteraciones clave si algo no cuadra.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Crear lista y sumar
# Enunciado: 
# Read N and then N integers; print the sum.
N = int(input("N: "))
L = []
for i in range(N):
    v = int(input("Value: "))
    L.append(v)
acc = 0
for x in L:
    acc = acc + x
print(acc)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Promedio de una lista
# Enunciado: 
# Read N and then N floats; print the average with 2 decimals or 'N/A' if N==0.
N = int(input("N: "))
L = []
for i in range(N):
    x = float(input("x: "))
    L.append(x)
if len(L) == 0:
    print("N/A")
else:
    s = 0.0
    for x in L:
        s = s + x
    print("{:.2f}".format(s/len(L)))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Mínimo y máximo
# Enunciado: 
# Read values until 'fin'; report min and max if any.
L = []
raw = input("Val (or 'fin'): ")
while raw.strip().lower() != "fin":
    try:
        L.append(float(raw))
    except ValueError:
        print("Invalid:", raw)
    raw = input("Val (or 'fin'): ")
if len(L) == 0:
    print("No data")
else:
    mn = L[0]; mx = L[0]
    for x in L:
        if x < mn: mn = x
        if x > mx: mx = x
    print("Min:", mn, "Max:", mx)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Contar ocurrencias
# Enunciado: 
# Read a list and a target; count how many times it appears.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
target = input("target: ")
count = 0
for x in L:
    if x == target:
        count = count + 1
print(count)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Búsqueda lineal (índice de primera aparición)
# Enunciado: 
# Print the first index of target or -1 if not found (don't use list.index).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
target = input("target: ")
pos = -1
for i in range(len(L)):
    if pos == -1 and L[i] == target:
        pos = i
print(pos)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Eliminar todas las apariciones (con nueva lista)
# Enunciado: 
# Remove all occurrences of 'val' from L without using remove in a loop (build new list).
L = []
N = int(input("N: "))
for _ in range(N):
    L.append(int(input("x: ")))
val = int(input("val to remove: "))
R = []
for x in L:
    if x != val:
        R.append(x)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Invertir lista (sin reverse)
# Enunciado: 
# Build a reversed copy R of L without using reverse() or slicing [::-1].
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
R = []
i = len(L) - 1
while i >= 0:
    R.append(L[i])
    i = i - 1
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Concatenación vs extend
# Enunciado: 
# Show the difference between A+B and A.extend(B).
A = [1,2,3]
B = [4,5]
C = A + B
print("A:", A, "B:", B, "C=A+B:", C)
A_copy = A[:]
A_copy.extend(B)
print("A_copy after extend:", A_copy)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Eliminar por índice (pop) seguro
# Enunciado: 
# Read a list and an index; if index valid, pop and print item, else print 'IndexError'.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
idx = int(input("index to pop: "))
if 0 <= idx < len(L):
    item = L.pop(idx)
    print("popped:", item, "| now:", L)
else:
    print("IndexError")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Insertar en posición
# Enunciado: 
# Read list of ints; read pos and val; if pos in [0..len], insert and show list.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
pos = int(input("pos: "))
val = int(input("val: "))
if 0 <= pos <= len(L):
    L.insert(pos, val)
    print(L)
else:
    print("Invalid position")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Copiar sin alias (slice)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

L = []
N = int(input("N: "))
for _ in range(N):
    L.append(input("item: "))
A = L            # alias
B = L[:]         # copy
if len(L) > 0:
    L[0] = "X"
print("A (alias):", A)
print("B (copy):", B)


# ---------------------------------------------------------------
# Ejercicio 12 - Filtrar no-ceros
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
R = []
for x in L:
    if x != 0:
        R.append(x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 13 - Intercalar dos listas (hasta el mínimo)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Interleave A0,B0,A1,B1,... up to min length
NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(input("A: "))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(input("B: "))
limit = len(A) if len(A) < len(B) else len(B)
C = []
for i in range(limit):
    C.append(A[i]); C.append(B[i])
print(C)


# ---------------------------------------------------------------
# Ejercicio 14 - Contar pares en la lista
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
count = 0
for x in L:
    if x % 2 == 0:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 15 - Rotación a la derecha en 1 (sin métodos)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Rotate right by 1: [a,b,c,d] -> [d,a,b,c]
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
if len(L) > 0:
    last = L[len(L)-1]
    R = [last]
    i = 0
    while i < len(L)-1:
        R.append(L[i])
        i = i + 1
    print(R)
else:
    print([])


# ---------------------------------------------------------------
# Ejercicio 16 - Eliminar duplicados preservando orden (sin sets)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
R = []
for x in L:
    # check membership manually
    seen = False
    for y in R:
        if y == x:
            seen = True
    if not seen:
        R.append(x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 17 - Unir listas alternando bloques de tamaño k
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Merge A and B in blocks of size k: A0..A(k-1), B0..B(k-1), A(k)..A(2k-1), ...
k = int(input("k: "))
NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(input("A: "))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(input("B: "))
i = 0
C = []
turnA = True
while i < len(A) or i < len(B):
    if turnA:
        j = i
        c = 0
        while j < len(A) and c < k:
            C.append(A[j]); j += 1; c += 1
    else:
        j = i
        c = 0
        while j < len(B) and c < k:
            C.append(B[j]); j += 1; c += 1
    turnA = not turnA
    if not turnA:
        # just switched from A to B; do nothing
        pass
    i = i + k
print(C)


# ---------------------------------------------------------------
# Ejercicio 18 - Invertir in-place sin reverse
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
left = 0
right = len(L) - 1
while left < right:
    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    left = left + 1
    right = right - 1
print(L)


# ---------------------------------------------------------------
# Ejercicio 19 - Concatenación de varias listas
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Read K lists, then concatenate them all left-to-right.
K = int(input("K: "))
ALL = []
for _ in range(K):
    n = int(input("n: "))
    T = []
    for __ in range(n):
        T.append(input("item: "))
    ALL = ALL + T
print(ALL)


# ---------------------------------------------------------------
# Ejercicio 20 - Seleccionar elementos en posiciones pares
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Build R with elements from even indices of L (0,2,4,...)
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
R = []
for i in range(0, len(L), 2):
    R.append(L[i])
print(R)


# ---------------------------------------------------------------
# Ejercicio 21 - Sumar elemento a elemento (hasta min longitud)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(float(input("A: ")))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(float(input("B: ")))
limit = len(A) if len(A) < len(B) else len(B)
C = []
for i in range(limit):
    C.append(A[i] + B[i])
print(C)


# ---------------------------------------------------------------
# Ejercicio 22 - Mover ceros al final preservando orden
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
R = []
zeros = 0
for x in L:
    if x == 0:
        zeros = zeros + 1
    else:
        R.append(x)
for _ in range(zeros):
    R.append(0)
print(R)


# ---------------------------------------------------------------
# Ejercicio 23 - Encontrar segundo mínimo (si existe)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
if len(L) < 2:
    print("N/A")
else:
    mn = L[0]
    for x in L:
        if x < mn: mn = x
    # find minimal greater than mn
    have = False
    smn = 0.0
    for x in L:
        if x > mn:
            if not have:
                smn = x; have = True
            else:
                if x < smn:
                    smn = x
    if have:
        print(smn)
    else:
        print("N/A")


# ---------------------------------------------------------------
# Ejercicio 24 - Eliminar primera y última aparición de un valor
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
val = input("val: ")
# find first
first = -1
for i in range(len(L)):
    if L[i] == val and first == -1:
        first = i
# find last
last = -1
for i in range(len(L)-1, -1, -1):
    if L[i] == val and last == -1:
        last = i
R = []
for i in range(len(L)):
    if i != first and i != last:
        R.append(L[i])
print(R)


# ---------------------------------------------------------------
# Ejercicio 25 - Contar cambios de signo consecutivos
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
count = 0
i = 1
while i < len(L):
    if (L[i-1] < 0 and L[i] > 0) or (L[i-1] > 0 and L[i] < 0):
        count = count + 1
    i = i + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 26 - Separar pares e impares (dos listas)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
E = []; O = []
for x in L:
    if x % 2 == 0:
        E.append(x)
    else:
        O.append(x)
print("E:", E)
print("O:", O)


# ---------------------------------------------------------------
# Ejercicio 27 - Eliminar elementos por rango de índices
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Remove items between i and j inclusive if valid; otherwise print original.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
i = int(input("i: "))
j = int(input("j: "))
if 0 <= i <= j < len(L):
    R = L[:i] + L[j+1:]
    print(R)
else:
    print(L)


# ---------------------------------------------------------------
# Ejercicio 28 - Duplicar cada elemento (números)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
R = []
for x in L:
    R.append(2*x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 29 - Aplanar lista de dos niveles simple (sin nested loops complejos)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Given K sublists entered one by one, concatenate into a single list (two-level only).
K = int(input("K: "))
R = []
for _ in range(K):
    n = int(input("n: "))
    T = []
    for __ in range(n):
        T.append(input("item: "))
    # concatenate
    for y in T:
        R.append(y)
print(R)


# ---------------------------------------------------------------
# Ejercicio 30 - Reemplazar todas las ocurrencias
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Replace every 'old' with 'new' in L.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
old = input("old: ")
new = input("new: ")
for i in range(len(L)):
    if L[i] == old:
        L[i] = new
print(L)


# ---------------------------------------------------------------
# Ejercicio 31 - Contar sublistas vacías
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Count empty sublists inside L (two-level list).
K = int(input("K sublists: "))
L = []
for _ in range(K):
    # read sublist length
    n = int(input("n: "))
    T = []
    for __ in range(n):
        T.append(input("item: "))
    L.append(T)
count = 0
for sub in L:
    if len(sub) == 0:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 32 - Partir en dos por umbral
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Split numbers into <=T and >T
T = float(input("T: "))
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
A = []; B = []
for x in L:
    if x <= T:
        A.append(x)
    else:
        B.append(x)
print("<=T:", A)
print(">T:", B)


# ---------------------------------------------------------------
# Ejercicio 33 - Repetir cada carácter en lista de strings
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# For each string s, build a new string where each char is doubled: 'hi'->'hhii'.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("s: "))
R = []
for s in L:
    t = ""
    for ch in s:
        t = t + ch + ch
    R.append(t)
print(R)


# ---------------------------------------------------------------
# Ejercicio 34 - Ordenar ascendente y descendente (sin key)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Read ints, print ascending and then descending copies (without modifying original).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
A = L[:]  # copy
A.sort()
D = A[:]  # copy of sorted asc
D.sort(reverse=True)
print("Asc:", A)
print("Desc:", D)


# ---------------------------------------------------------------
# Ejercicio 35 - Eliminar desde la primera aparición hasta el final
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Remove all elements from first 'val' (inclusive) to the end.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
val = input("val: ")
pos = -1
for i in range(len(L)):
    if pos == -1 and L[i] == val:
        pos = i
if pos == -1:
    print(L)
else:
    print(L[:pos])


# ---------------------------------------------------------------
# Ejercicio 36 - Empaquetar pares consecutivos en sublistas (dos niveles)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Given L of length N, produce [[L0,L1],[L2,L3],...] (last singleton if odd length).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
R = []
i = 0
while i < len(L):
    if i+1 < len(L):
        R.append([L[i], L[i+1]])
    else:
        R.append([L[i]])
    i = i + 2
print(R)


# ---------------------------------------------------------------
# Ejercicio 37 - Contar runs (bloques) de iguales consecutivos
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Number of groups where consecutive identical values appear.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
if len(L) == 0:
    print(0)
else:
    runs = 1
    i = 1
    while i < len(L):
        if L[i] != L[i-1]:
            runs = runs + 1
        i = i + 1
    print(runs)


# ---------------------------------------------------------------
# Ejercicio 38 - Remover todos excepto la primera aparición
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Keep first occurrence of each value and remove later ones (preserve order).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
R = []
for x in L:
    seen = False
    for y in R:
        if y == x:
            seen = True
    if not seen:
        R.append(x)
print(R)


# ---------------------------------------------------------------
# Ejercicio 39 - Sublista espejo (palíndromo de lista)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Check if L reads the same forward and backward.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
left = 0; right = len(L) - 1
ok = True
while (left < right) and ok:
    if L[left] != L[right]:
        ok = False
    left = left + 1
    right = right - 1
print("Palindrome" if ok else "Not palindrome")


# ---------------------------------------------------------------
# Ejercicio 40 - Emparejar elementos por índice (A y B)
# Enunciado: Ejercicio práctico sobre listas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

# Read A and B, build list of pairs [Ai,Bi] up to min length (two-level list).
NA = int(input("NA: "))
A = []
for _ in range(NA):
    A.append(input("A: "))
NB = int(input("NB: "))
B = []
for _ in range(NB):
    B.append(input("B: "))
limit = len(A) if len(A) < len(B) else len(B)
R = []
for i in range(limit):
    R.append([A[i], B[i]])
print(R)

