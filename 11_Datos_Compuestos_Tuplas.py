
# ===============================================================
# 11.- DATOS COMPUESTOS: TUPLAS — INMUTABILIDAD, EMPAQUETADO Y RECORRIDOS
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
#
# Reglas pedagógicas de este archivo .py:
#   - En esta sesión introducimos TUPLAS (colección ordenada e INMUTABLE).
#   - SOLO usamos conceptos ya vistos: entrada/salida, operaciones con números y cadenas,
#     condicionales (simples/dobles/múltiples/anidadas), try-except, while, for y range,
#     contadores, acumuladores, centinelas, depuración con prints y LISTAS (de sesiones 9 y 10).
#   - ESTRICTAMENTE PROHIBIDO: diccionarios (siguiente sesión), funciones definidas por el usuario,
#     librerías externas, archivos, parámetros 'key' en sort (requiere funciones), break/continue.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: ¿Qué es una tupla? creación, inmutabilidad, tipos de elementos
#   C) Índices y slices; concatenación (+) y repetición (*)
#   D) Recorridos con for/while; pertenencia 'in'
#   E) Métodos y operaciones disponibles: len, index, count, conversión list<->tuple
#   F) Empaquetado y desempaquetado (multiple assignment, swap, *star unpacking)
#   G) Tuplas anidadas y tuplas con listas (peligro de mutabilidad interna)
#   H) Casos de uso guiados
#   I) Ventajas, desventajas y buenas prácticas
#   J) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Entender que una TUPLA es una secuencia ORDENADA e INMUTABLE.
# - Crear tuplas correctamente, incluyendo tupla de 1 elemento y tupla vacía.
# - Acceder por índice, usar slices, concatenar y repetir.
# - Recorrer con for/range y while; verificar pertenencia con 'in'.
# - Usar len(), .index(), .count(), y convertir entre lista y tupla.
# - Aplicar empaquetado/desempaquetado para asignaciones múltiples y swap de variables.
# - Reconocer implicaciones de inmutabilidad cuando la tupla contiene listas u otras tuplas.

# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UNA TUPLA?
# ---------------------------------------------------------------
# Definición:
# - TUPLA: colección ordenada, INDEXABLE e INMUTABLE (no se puede modificar un elemento).
# - Se escribe con paréntesis () y elementos separados por coma.
#
# Ejemplos:
t = (10, 20, 30)
print("t:", t)
u = ("uno", "dos", "tres")
print("u:", u)
mix = (1, "A", 2.5)  # posible, pero se recomienda homogeneidad cuando sea práctico
print("mix:", mix)
empty = ()           # tupla vacía
print("empty:", empty)
#
# Tupla de 1 elemento (¡requiere coma!):
one = (5,)           # si escribes (5) es solo el entero 5
print("one:", one, "type(one):", type(one))
not_tuple = (5)
print("not_tuple:", not_tuple, "type(not_tuple):", type(not_tuple))
#
# Inmutabilidad:
# - No puedes reasignar t[0] = 99 (TypeError). Demostración comentada:
# t[0] = 99  # Descomenta para ver TypeError

# ---------------------------------------------------------------
# C) ÍNDICES Y SLICES; CONCATENACIÓN (+) Y REPETICIÓN (*)
# ---------------------------------------------------------------
a = (5, 6, 7, 8, 9)
print("a[0] =", a[0], "a[-1] =", a[-1])
print("a[1:4] ->", a[1:4])   # subtupla desde 1 hasta 3
print("a[:3]  ->", a[:3])
print("a[3:]  ->", a[3:])
print("a[:]   ->", a[:])     # copia superficial (nuevo objeto tupla)
#
# Operadores:
x = (1, 2)
y = (3, 4, 5)
print("x + y ->", x + y)     # concatenación -> (1,2,3,4,5)
print("y * 2 ->", y * 2)     # repetición -> (3,4,5,3,4,5)

# ---------------------------------------------------------------
# D) RECORRIDOS CON FOR/WHILE; PERTENENCIA 'in'
# ---------------------------------------------------------------
t = (3, 7, 2, 9)
total = 0
for val in t:
    total = total + val
print("Sum (for-by-element):", total)

total2 = 0
for i in range(len(t)):
    total2 = total2 + t[i]
print("Sum (for-by-index):", total2)

i = 0
total3 = 0
while i < len(t):
    total3 = total3 + t[i]
    i = i + 1
print("Sum (while):", total3)

# Pertenencia:
print("7 in t?", 7 in t)
print("10 in t?", 10 in t)

# ---------------------------------------------------------------
# E) MÉTODOS Y OPERACIONES DISPONIBLES
# ---------------------------------------------------------------
# len(t) -> longitud
# t.index(x) -> índice de la primera aparición de x (ValueError si no está)
# t.count(x) -> cuántas veces aparece x
# Conversión: list(t) para obtener lista mutable; tuple(L) para crear tupla desde lista
#
w = ("a", "b", "a", "c", "a")
print("len(w) ->", len(w))
print("w.count('a') ->", w.count("a"))
print("w.index('b') ->", w.index("b"))
#
L = list(w)         # copia en lista
L[0] = "A"          # modifico la lista (no la tupla original)
print("L modificada:", L)
w2 = tuple(L)       # vuelvo a tupla
print("w2:", w2)
#
# join/split con tuplas de cadenas (permitido):
parts = ("hola", "mundo")
print("join:", " ".join(parts))
line = "uno dos tres"
tok = tuple(line.split())  # tuple de tokens
print("split->tuple:", tok)

# ---------------------------------------------------------------
# F) EMPAQUETADO Y DESEMPAQUETADO
# ---------------------------------------------------------------
# Empaquetado: se crea una tupla sin paréntesis usando comas.
p = 10, 20, 30
print("p empaquetado:", p, "type:", type(p))

# Desempaquetado múltiple:
a, b, c = p
print("a:", a, "b:", b, "c:", c)

# Swap (intercambio) de variables usando tuplas:
x = 1; y = 2
x, y = y, x
print("swap -> x:", x, "y:", y)

# Desempaquetado con * (estrella) para capturar "el resto":
t = (1, 2, 3, 4, 5, 6)
first, *middle, last = t
print("first:", first, "middle:", middle, "last:", last)
# Nota: middle es una LISTA (lo permite Python); puedes convertirla a tupla si lo necesitas:
middle_t = tuple(middle)
print("middle_t:", middle_t, "type:", type(middle_t))

# ---------------------------------------------------------------
# G) TUPLAS ANIDADAS Y TUPLAS CON LISTAS
# ---------------------------------------------------------------
# Tuplas anidadas:
T = ( (1,2), (3,4,5), (6,) )
print("T:", T, "T[1][2] ->", T[1][2])

# Tupla con lista interna (la tupla es inmutable, pero la lista sí cambia):
U = (1, [10, 20], 3)
print("U antes:", U)
U[1].append(99)    # válido: NO cambiamos la tupla, cambiamos la lista que contiene
print("U después:", U)
#
# Cuidado: U[0] = 100 -> TypeError (prohibido modificar posiciones de la tupla)

# ---------------------------------------------------------------
# H) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Registrar una fecha como tupla (año, mes, día) y compararla con otra
# (Descomenta para usar en clase)
# a1 = int(input("año1: ")); m1 = int(input("mes1: ")); d1 = int(input("día1: "))
# a2 = int(input("año2: ")); m2 = int(input("mes2: ")); d2 = int(input("día2: "))
# f1 = (a1, m1, d1)
# f2 = (a2, m2, d2)
# # comparación lexicográfica: primero año, luego mes, luego día
# if f1 < f2:
#     print("f1 es anterior")
# elif f1 > f2:
#     print("f1 es posterior")
# else:
#     print("mismas fechas")

# Caso 2) Convertir lista de calificaciones a tupla inmutable y calcular promedio con for
# L = [80, 95, 70, 100]
# T = tuple(L)
# s = 0
# for x in T:
#     s = s + x
# print("Promedio:", s / len(T))

# Caso 3) Parsear una línea "x,y,z" en tupla (x,y,z) de enteros
# line = input("x,y,z: ")
# toks = line.split(",")
# if len(toks) == 3:
#     try:
#         t = (int(toks[0]), int(toks[1]), int(toks[2]))
#         print("Tupla:", t)
#     except ValueError:
#         print("Valores no enteros")
# else:
#     print("Formato inválido")

# ---------------------------------------------------------------
# I) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Inmutabilidad: protege datos que no deben cambiar (seguridad y claridad).
# - Empaquetado/desempaquetado: facilita asignaciones múltiples y swaps.
# - Menor sobrecarga que la lista cuando solo se requiere lectura.
#
# Desventajas / riesgos:
# - No se pueden insertar/eliminar/modificar elementos (no hay append/remove/...).
# - Si la tupla contiene una lista interna, esa lista SÍ puede cambiar (mutabilidad interna).
#
# Buenas prácticas:
# - Usa tuplas para "registros" de tamaño fijo (ej.: (día, mes, año), (x, y)).
# - Si necesitas modificar con frecuencia, prefiere listas y al final convierte a tupla.
# - Al depurar, imprime los valores antes/después de desempaquetar para validar posiciones.

# ---------------------------------------------------------------
# J) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Crear tupla desde entradas
# Enunciado: 
# Read N and then N integers, store them in a tuple and print it.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
T = tuple(L)
print(T)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Acceso por índice seguro
# Enunciado: 
# Read tuple (via list inputs) and then an index i; print T[i] or 'IndexError'.
N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(input("item: "))
T = tuple(vals)
i = int(input("i: "))
if 0 <= i < len(T):
    print(T[i])
else:
    print("IndexError")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Slice de tupla
# Enunciado: 
# Read tuple and two indices a,b (a<=b), print T[a:b] (Python slice excludes b).
N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(input("item: "))
T = tuple(vals)
a = int(input("a: "))
b = int(input("b: "))
if 0 <= a <= b <= len(T):
    print(T[a:b])
else:
    print("Invalid slice")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Contar ocurrencias
# Enunciado: 
# Count how many times 'target' appears in T (use .count).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
target = input("target: ")
print(T.count(target))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Índice de primera aparición
# Enunciado: 
# Print first index of target or -1 if not found (avoid exception with a check).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
target = input("target: ")
pos = -1
for i in range(len(T)):
    if pos == -1 and T[i] == target:
        pos = i
print(pos)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - ¿Elemento pertenece?
# Enunciado: 
# Read T and an item x; print 'YES' if x in T else 'NO'.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
x = input("x: ")
found = False
for item in T:
    if item == x:
        found = True
print("YES" if found else "NO")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Sumar enteros en tupla
# Enunciado: 
# Read N ints into T and print the sum (no built-in sum).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
T = tuple(L)
acc = 0
for v in T:
    acc = acc + v
print(acc)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Mínimo y máximo manuales
# Enunciado: 
# Read floats into T; print min and max using loops.
N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(float(input("x: ")))
T = tuple(vals)
if len(T) == 0:
    print("No data")
else:
    mn = T[0]; mx = T[0]
    for x in T:
        if x < mn: mn = x
        if x > mx: mx = x
    print("Min:", mn, "Max:", mx)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Concatenación de tuplas
# Enunciado: 
# Read two tuples (via inputs) and print T1 + T2.
N1 = int(input("N1: "))
A = []
for _ in range(N1):
    A.append(input("A: "))
N2 = int(input("N2: "))
B = []
for _ in range(N2):
    B.append(input("B: "))
T1 = tuple(A); T2 = tuple(B)
print(T1 + T2)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Repetición de tupla
# Enunciado: 
# Read a tuple and k; print T*k.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
k = int(input("k: "))
print(T * k)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Comparar fechas (tuplas)
# Enunciado: 
# Read two dates (y,m,d) and print which one is earlier/equal/later.
y1 = int(input("y1: ")); m1 = int(input("m1: ")); d1 = int(input("d1: "))
y2 = int(input("y2: ")); m2 = int(input("m2: ")); d2 = int(input("d2: "))
f1 = (y1, m1, d1)
f2 = (y2, m2, d2)
if f1 < f2:
    print("f1<f2")
elif f1 > f2:
    print("f1>f2")
else:
    print("f1==f2")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 12 - Desempaquetado básico
# Enunciado: 
# Read a tuple of three items and print them in separate lines via unpacking.
a = input("a: ")
b = input("b: ")
c = input("c: ")
T = (a, b, c)
x, y, z = T
print(x); print(y); print(z)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 13 - Swap de variables con tuplas
# Enunciado: 
# Read x and y, swap them using x,y=y,x and print.
x = input("x: ")
y = input("y: ")
x, y = y, x
print("x:", x, "y:", y)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 14 - Empaquetado sin paréntesis
# Enunciado: 
# Read two tokens and build a packed tuple without parentheses.
a = input("a: ")
b = input("b: ")
T = a, b
print(T, type(T))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 15 - Desempaquetado con *
# Enunciado: 
# Read N tokens into T; unpack first, middle, last, and print middle as tuple.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("t: "))
T = tuple(L)
if len(T) >= 2:
    first, *middle, last = T
    middle_t = tuple(middle)
    print("first:", first, "middle:", middle_t, "last:", last)
else:
    print("Need at least 2 items")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 16 - Tupla de caracteres
# Enunciado: 
# Read a string s and build tuple of its characters; print count of vowels.
s = input("s: ")
T = tuple(s)
vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"
count = 0
for ch in T:
    if ch in vowels:
        count = count + 1
print(count)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 17 - Tupla numérica de rango
# Enunciado: 
# Read a,b and build T=tuple of ints from a to b inclusive (assume a<=b).
a = int(input("a: "))
b = int(input("b: "))
temp = []
for x in range(a, b+1):
    temp.append(x)
T = tuple(temp)
print(T)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 18 - Eliminar por re-construcción
# Enunciado: 
# Read T and a value v; build a NEW tuple without any v (no .remove since tuple no tiene).
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
v = input("v: ")
tmp = []
for x in T:
    if x != v:
        tmp.append(x)
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 19 - Invertir tupla (con while)
# Enunciado: 
# Build reversed tuple R from T using while and indices.
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
T = tuple(L)
i = len(T) - 1
tmp = []
while i >= 0:
    tmp.append(T[i])
    i = i - 1
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 20 - Tupla de pares (n, n^2)
# Enunciado: 
# For n=1..N, build a list of pairs (n, n^2) and convert to tuple of tuples.
N = int(input("N: "))
pairs_list = []
for n in range(1, N+1):
    pairs_list.append( (n, n*n) )
T = tuple(pairs_list)
print(T)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 21 - Concatenar muchas tuplas
# Enunciado: 
# Read K tuples and concatenate them all (left to right) into one tuple R.
K = int(input("K: "))
R = ()
for _ in range(K):
    n = int(input("n: "))
    temp = []
    for __ in range(n):
        temp.append(input("item: "))
    R = R + tuple(temp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 22 - Contar mayores que un umbral
# Enunciado: 
# Read floats into T and count how many > T0.
N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(float(input("x: ")))
T = tuple(vals)
T0 = float(input("T0: "))
count = 0
for x in T:
    if x > T0:
        count = count + 1
print(count)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 23 - Buscar subtupla en tupla
# Enunciado: 
# Read T and S (S shorter), count how many times S appears in T consecutively (no solapado).
NT = int(input("NT: "))
A = []
for _ in range(NT):
    A.append(input("T: "))
NS = int(input("NS: "))
B = []
for _ in range(NS):
    B.append(input("S: "))
T = tuple(A); S = tuple(B)
count = 0
i = 0
while i <= len(T) - len(S):
    eq = True
    j = 0
    while j < len(S) and eq:
        if T[i+j] != S[j]:
            eq = False
        j = j + 1
    if eq:
        count = count + 1
        i = i + len(S)   # no solapado
    else:
        i = i + 1
print(count)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 24 - Intercalar dos tuplas (hasta min)
# Enunciado: 
# Interleave T and U element-by-element up to min length; result as tuple.
N1 = int(input("N1: "))
A = []
for _ in range(N1):
    A.append(input("A: "))
N2 = int(input("N2: "))
B = []
for _ in range(N2):
    B.append(input("B: "))
T = tuple(A); U = tuple(B)
limit = len(T) if len(T) < len(U) else len(U)
tmp = []
for i in range(limit):
    tmp.append(T[i]); tmp.append(U[i])
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 25 - Tupla espejo (palíndroma)
# Enunciado: 
# Check if T reads same forward/backward.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("item: "))
T = tuple(A)
left = 0; right = len(T)-1; ok = True
while (left < right) and ok:
    if T[left] != T[right]:
        ok = False
    left = left + 1
    right = right - 1
print("Palindrome" if ok else "Not palindrome")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 26 - Unir tokens con separador
# Enunciado: 
# Read tuple of words and a separator; print separator.join(T).
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("word: "))
T = tuple(A)
sep = input("sep: ")
print(sep.join(T))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 27 - Orden natural de tuplas (lista de tuplas)
# Enunciado: 
# Read list of tuples (a,b) with strings; sort the LIST (not the tuple) and print.
N = int(input("N: "))
L = []
for _ in range(N):
    a = input("a: "); b = input("b: ")
    L.append( (a, b) )
# sort asc por orden natural de tuplas
L.sort()
print(L)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 28 - Tupla de longitudes
# Enunciado: 
# Given a tuple of words, produce a tuple of their lengths.
N = int(input("N: "))
words = []
for _ in range(N):
    words.append(input("w: "))
T = tuple(words)
tmp = []
for w in T:
    tmp.append(len(w))
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 29 - Separar en pares e impares (como listas)
# Enunciado: 
# From tuple of ints T, build two LISTS: E (evens) and O (odds); print as tuples.
N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(int(input("x: ")))
T = tuple(vals)
E = []; O = []
for x in T:
    if x % 2 == 0:
        E.append(x)
    else:
        O.append(x)
print(tuple(E), tuple(O))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 30 - Tupla sin duplicados (preservando orden)
# Enunciado: 
# From T, build R without duplicates, preserving first appearances.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("item: "))
T = tuple(A)
tmp = []
for x in T:
    seen = False
    for y in tmp:
        if y == x: seen = True
    if not seen:
        tmp.append(x)
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 31 - Cortar desde primera aparición de v
# Enunciado: 
# From T, remove everything from the first 'v' (inclusive) to the end; print new tuple.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("item: "))
T = tuple(A)
v = input("v: ")
pos = -1
for i in range(len(T)):
    if pos == -1 and T[i] == v:
        pos = i
if pos == -1:
    print(T)
else:
    print(T[:pos])

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 32 - Empaquetar consecutivos (tupla de tuplas)
# Enunciado: 
# Given T, produce tuple of pairs (T0,T1),(T2,T3),... last singleton if odd length.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("item: "))
T = tuple(A)
tmp = []
i = 0
while i < len(T):
    if i+1 < len(T):
        tmp.append( (T[i], T[i+1]) )
    else:
        tmp.append( (T[i],) )
    i = i + 2
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 33 - Comparación lexicográfica explícita
# Enunciado: 
# Read two tuples (a1,a2,a3) and (b1,b2,b3) of ints; print relation (<,>,==).
A = (int(input("a1: ")), int(input("a2: ")), int(input("a3: ")))
B = (int(input("b1: ")), int(input("b2: ")), int(input("b3: ")))
if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 34 - Tupla a lista, modificar, regresar a tupla
# Enunciado: 
# Convert T to list, replace all 'old' with 'new', and convert back to tuple.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(input("item: "))
T = tuple(A)
old = input("old: ")
new = input("new: ")
L = list(T)
for i in range(len(L)):
    if L[i] == old:
        L[i] = new
R = tuple(L)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 35 - Sumar por posiciones (dos tuplas)
# Enunciado: 
# Read two tuples of equal length of floats; produce tuple of sums position-wise.
N = int(input("N: "))
A = []
for _ in range(N):
    A.append(float(input("A: ")))
B = []
for _ in range(N):
    B.append(float(input("B: ")))
T1 = tuple(A); T2 = tuple(B)
tmp = []
for i in range(N):
    tmp.append(T1[i] + T2[i])
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 36 - Tupla de tokens numéricos válidos
# Enunciado: 
# Read tokens and keep only those that are valid integers (no signs).
toks = input("Tokens: ").split()
tmp = []
for t in toks:
    ok = True
    for ch in t:
        if not ("0" <= ch <= "9"):
            ok = False
    if ok:
        tmp.append(int(t))
R = tuple(tmp)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 37 - Cuentas paralelas (tokens y frecuencias)
# Enunciado: 
# Like a simple frequency count using two parallel tuples (no dicts).
toks = input("Tokens: ").split()
V = []  # unique tokens
C = []  # counts
for t in toks:
    pos = -1
    for i in range(len(V)):
        if V[i] == t:
            pos = i
    if pos == -1:
        V.append(t); C.append(1)
    else:
        C[pos] = C[pos] + 1
print(tuple(V))
print(tuple(C))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 38 - Tupla de tuplas: buscar valor
# Enunciado: 
# Read matrix-like tuple of tuples and search for value; print first (i,j) or (-1,-1).
r = int(input("rows: "))
c = int(input("cols: "))
M_list = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M_list.append(tuple(row))
M = tuple(M_list)
target = input("target: ")
pi = -1; pj = -1
for i in range(r):
    for j in range(c):
        if pi == -1 and M[i][j] == target:
            pi = i; pj = j
print((pi, pj))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 39 - Bordes de matriz (tupla de tuplas)
# Enunciado: 
# Print border elements of an r x c tuple-of-tuples matrix as a tuple in clockwise order.
r = int(input("rows: "))
c = int(input("cols: "))
M_list = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("M["+str(i)+"]["+str(j)+"]: "))
    M_list.append(tuple(row))
M = tuple(M_list)
tmp = []
# top row
for j in range(c):
    tmp.append(M[0][j])
# right col
for i in range(1, r):
    tmp.append(M[i][c-1])
# bottom row
if r > 1:
    j = c-2
    while j >= 0:
        tmp.append(M[r-1][j])
        j = j - 1
# left col
if c > 1:
    i = r-2
    while i >= 1:
        tmp.append(M[i][0])
        i = i - 1
print(tuple(tmp))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 40 - Validación con try-except y tuplas
# Enunciado: 
# Keep reading integers until 'fin'; store them in a tuple and print count and average.
vals = []
raw = input("x (or 'fin'): ")
while raw.strip().lower() != "fin":
    try:
        vals.append(int(raw))
    except ValueError:
        print("Invalid:", raw)
    raw = input("x (or 'fin'): ")
T = tuple(vals)
if len(T) == 0:
    print("No data")
else:
    s = 0
    for v in T:
        s = s + v
    print("Count:", len(T), "Avg:", s/len(T))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

