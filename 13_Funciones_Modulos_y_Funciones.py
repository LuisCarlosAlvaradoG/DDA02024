
# ===============================================================
# 13.- FUNCIONES (I): MÓDULOS Y FUNCIONES. ESPECIFICACIÓN E IMPLEMENTACIÓN.
# Encabezado y parámetros.
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
#
# Reglas pedagógicas de este archivo .py:
#   - Introducimos FUNCIONES y MÓDULOS con un enfoque básico y riguroso.
#   - SOLO usamos conceptos ya vistos: entrada/salida, números y cadenas, condicionales,
#     try-except, while, for/range, contadores, acumuladores, centinelas, depurador,
#     listas, tuplas y diccionarios.
#   - Permitimos el uso de algunos módulos estándar (p.ej. 'math') solo para ilustrar
#     el concepto de módulo, manteniéndonos en operaciones simples.
#   - Evitamos temas aún no vistos: archivos, programación orientada a objetos,
#     *args/**kwargs avanzados, recursión, librerías externas.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: ¿Qué es una función? especificación vs. implementación, encabezado y cuerpo
#   C) Módulos: importación y espacios de nombres (con 'math')
#   D) Parámetros: posicionales y argumentos por palabra clave (básico)
#   E) Alcance: variables locales vs. globales (y precauciones)
#   F) Casos de uso guiados
#   G) Ventajas, desventajas y buenas prácticas
#   H) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Diferenciar ESPECIFICACIÓN (qué hace) de IMPLEMENTACIÓN (cómo lo hace).
# - Escribir encabezados 'def nombre(parámetros):' con comentarios/docstrings claros.
# - Llamar funciones con argumentos posicionales y por palabra clave.
# - Comprender el concepto de módulo y espacio de nombres básico.
# - Practicar depuración dentro de funciones con impresiones etiquetadas.

# ---------------------------------------------------------------
# B) TEORÍA: FUNCIÓN (ESPECIFICACIÓN VS IMPLEMENTACIÓN)
# ---------------------------------------------------------------
# FUNCIÓN: bloque reutilizable que recibe argumentos, realiza un procesamiento y
# opcionalmente devuelve un resultado con 'return'.
#
# ESPECIFICACIÓN (qué debe cumplir): nombre, parámetros, qué retorna, precondiciones,
# postcondiciones y descripción en español.
#
# IMPLEMENTACIÓN (cómo lo cumple): código dentro del cuerpo 'def ...:'.
#
# Estructura general:
#   def nombre(par1, par2):
#       \"\"\"Descripción breve.
#       Parámetros:
#           par1: tipo/rol esperado.
#           par2: tipo/rol esperado.
#       Retorna:
#           descripción del valor de retorno (o None si no retorna).
#       Precondiciones/Postcondiciones (si aplica).
#       \"\"\"
#       # cuerpo (usando solo lo visto)
#       # ...
#       return resultado  # o no retorna (retorno implícito None)
#
# Diferencia PRINT vs RETURN:
# - print muestra en pantalla; return entrega el valor para seguir usándolo en otro lugar.
# - Una función sin return explícito retorna None.
#
# Ejemplo simple:
def add(a, b):
    \"\"\"Suma dos números y retorna el resultado.\"\"\"
    return a + b

x = add(10, 5)        # llamada
print("add(10,5) ->", x)  # 15

# ---------------------------------------------------------------
# C) MÓDULOS: IMPORTACIÓN Y ESPACIOS DE NOMBRES
# ---------------------------------------------------------------
# Un módulo es un archivo con definiciones (funciones, constantes, etc.). Para usarlo:
#   import nombre_modulo
#   from nombre_modulo import nombre_objeto
#   import nombre_modulo as alias
#
# Demostración con el módulo estándar 'math' (operaciones numéricas básicas):
import math
print("math.pi =", math.pi)
print("math.sqrt(25) =", math.sqrt(25))
print("math.floor(3.7) =", math.floor(3.7))

# También podemos importar un nombre específico:
from math import sqrt
print("sqrt(81) =", sqrt(81))

# O usar un alias para el módulo:
import math as m
print("m.ceil(2.1) =", m.ceil(2.1))

# Nota pedagógica: por claridad en cursos iniciales, preferimos 'import math' y luego 'math.algo'.

# ---------------------------------------------------------------
# D) PARÁMETROS: POSICIONALES Y POR PALABRA CLAVE (BÁSICO)
# ---------------------------------------------------------------
# En Python, al llamar una función, podemos pasar argumentos por posición o nombrarlos.

def rectangle_area(width, height):
    \"\"\"Retorna el área de un rectángulo width x height (ambos >= 0).\"\"\"
    if width < 0 or height < 0:
        # Especificación: asumimos no-negativos. Aquí validamos y usamos try/except o if.
        # Por simplicidad, devolvemos 0 si no cumple:
        return 0
    return width * height

# Llamadas por posición:
print("rect pos:", rectangle_area(3, 4))

# Llamadas por palabra clave (keyword arguments):
print("rect kw:", rectangle_area(height=4, width=3))

# Mezcla (posicionales primero, luego keywords):
print("rect mixed:", rectangle_area(5, height=2))

# ---------------------------------------------------------------
# E) ALCANCE: LOCALES VS. GLOBALES (Y PRECAUCIONES)
# ---------------------------------------------------------------
# Variables definidas dentro de una función son LOCALES a esa función.
# Variables definidas fuera pertenecen al ámbito GLOBAL del módulo.
# Evitar depender de globales salvo necesidad; pasar datos por parámetros es más claro.

DEBUG = False  # bandera global de depuración

def increment_all_by_one(L):
    \"\"\"Suma 1 a cada entero de la LISTA L y retorna una NUEVA lista.\"\"\"
    if DEBUG:
        print("[DBG] original L:", L)
    R = []
    for x in L:
        R.append(x + 1)
    if DEBUG:
        print("[DBG] result R:", R)
    return R

data = [1, 2, 3]
print("increment_all_by_one:", increment_all_by_one(data))
print("after call, data still:", data)  # data NO se modificó (retornamos copia)

# ---------------------------------------------------------------
# F) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Validación de entrada con función (retorna entero en [a..b] o None)
def read_int_in_range(a, b):
    \"\"\"Lee un entero usando input(); retorna el valor si está en [a..b], o None en caso contrario.\"\"\"
    raw = input("Enter int ["+str(a)+".."+str(b)+"]: ")
    try:
        n = int(raw)
        if a <= n <= b:
            return n
        else:
            print("Out of range")
            return None
    except ValueError:
        print("Not an integer")
        return None

# (Descomenta para usar en clase)
# v = read_int_in_range(10, 20)
# print("read_int_in_range ->", v)

# Caso 2) Resumen de lista: suma, promedio, min, max (retorno múltiple con tupla)
def list_summary(nums):
    \"\"\"Recibe una lista de números y retorna (suma, promedio, min, max).
    Si la lista está vacía, retorna (0, None, None, None).
    \"\"\"
    if len(nums) == 0:
        return (0, None, None, None)
    s = 0.0
    mn = nums[0]; mx = nums[0]
    for x in nums:
        s = s + x
        if x < mn: mn = x
        if x > mx: mx = x
    avg = s / len(nums)
    return (s, avg, mn, mx)

print("list_summary demo:", list_summary([3, 7, 2, 9]))

# ---------------------------------------------------------------
# G) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización, claridad, pruebas más fáciles, depuración localizada.
# - Encapsulan detalles: cambias la implementación sin tocar el resto del programa.
#
# Desventajas/riesgos en principiantes:
# - Exceso de dependencia de variables globales puede generar errores sutiles.
# - Mala especificación (sin aclarar pre/post) crea confusión en el uso.
#
# Buenas prácticas:
# - Escribe una ESPECIFICACIÓN clara (docstring) antes de implementar.
# - Prefiere retornar valores a imprimir dentro de la función, salvo funciones “procedimiento”.
# - Diseña funciones pequeñas y con responsabilidad única.
# - Agrega trazas con bandera DEBUG cuando algo no cuadre.

# ---------------------------------------------------------------
# H) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Suma de dos números (return)
# Enunciado: 
def add2(a, b):
    return a + b

x = float(input("a: "))
y = float(input("b: "))
print(add2(x, y))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Es par (bool)
# Enunciado: 
def is_even(n):
    return (n % 2) == 0

n = int(input("n: "))
print(is_even(n))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Área de triángulo (base*height/2)
# Enunciado: 
def triangle_area(base, height):
    if base < 0 or height < 0:
        return 0.0
    return (base * height) / 2.0

b = float(input("base: "))
h = float(input("height: "))
print(triangle_area(b, h))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Clamp a rango [a..b]
# Enunciado: 
def clamp(x, a, b):
    if x < a:
        return a
    elif x > b:
        return b
    else:
        return x

x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))
print(clamp(x, a, b))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Contar dígitos en cadena
# Enunciado: 
def count_digits(s):
    count = 0
    for ch in s:
        if "0" <= ch <= "9":
            count = count + 1
    return count

print(count_digits(input("s: ")))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Mínimo manual (lista)
# Enunciado: 
def my_min(L):
    if len(L) == 0:
        return None
    mn = L[0]
    for x in L:
        if x < mn: mn = x
    return mn

N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(float(input("x: ")))
print(my_min(vals))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Promedio robusto (lista)
# Enunciado: 
def average(L):
    if len(L) == 0:
        return None
    s = 0.0
    for x in L:
        s = s + x
    return s / len(L)

N = int(input("N: "))
vals = []
for _ in range(N):
    vals.append(float(input("x: ")))
print(average(vals))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Normalizar texto (strip+lower)
# Enunciado: 
def norm_text(s):
    return s.strip().lower()

print(norm_text(input("text: ")))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Contar palabras (split)
# Enunciado: 
def count_words(line):
    toks = line.split()
    return len(toks)

print(count_words(input("line: ")))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Usar módulo math: hipotenusa
# Enunciado: 
import math
def hyp(a, b):
    if a < 0 or b < 0:
        return 0.0
    return math.sqrt(a*a + b*b)

a = float(input("a: "))
b = float(input("b: "))
print(hyp(a, b))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Repetir cadena n veces (return)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def repeat_text(s, n):
    if n < 0:
        return ""
    res = ""
    for _ in range(n):
        res = res + s
    return res

print(repeat_text(input("s: "), int(input("n: "))))


# ---------------------------------------------------------------
# Ejercicio 12 - Máximo y posición (tupla)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def max_and_pos(L):
    if len(L) == 0:
        return (None, -1)
    mx = L[0]; pos = 0
    for i in range(len(L)):
        if L[i] > mx:
            mx = L[i]; pos = i
    return (mx, pos)

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
print(max_and_pos(L))


# ---------------------------------------------------------------
# Ejercicio 13 - Filtrar positivos (nueva lista)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def filter_positive(L):
    R = []
    for x in L:
        if x > 0:
            R.append(x)
    return R

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
print(filter_positive(L))


# ---------------------------------------------------------------
# Ejercicio 14 - Contar ocurrencias (lista)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_occurrences(L, val):
    c = 0
    for x in L:
        if x == val:
            c = c + 1
    return c

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
v = input("val: ")
print(count_occurrences(L, v))


# ---------------------------------------------------------------
# Ejercicio 15 - Buscar primera posición (lista)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def first_index(L, val):
    for i in range(len(L)):
        if L[i] == val:
            return i
    return -1

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
v = input("val: ")
print(first_index(L, v))


# ---------------------------------------------------------------
# Ejercicio 16 - Eliminar todas las apariciones (copia)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def remove_all(L, val):
    R = []
    for x in L:
        if x != val:
            R.append(x)
    return R

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
v = input("val: ")
print(remove_all(L, v))


# ---------------------------------------------------------------
# Ejercicio 17 - Join manual con separador
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def join_with_sep(items, sep):
    res = ""
    for i in range(len(items)):
        if i > 0:
            res = res + sep
        res = res + items[i]
    return res

print(join_with_sep(input("line: ").split(), input("sep: ")))


# ---------------------------------------------------------------
# Ejercicio 18 - Contar vocales (cadena)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_vowels(s):
    v = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    c = 0
    for ch in s:
        if ch in v:
            c = c + 1
    return c

print(count_vowels(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 19 - Normalizar lista de strings
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def normalize_tokens(tokens):
    R = []
    for t in tokens:
        R.append(t.strip().lower())
    return R

print(normalize_tokens(input("line: ").split()))


# ---------------------------------------------------------------
# Ejercicio 20 - Frecuencias (dict)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def frequencies(tokens):
    F = {}
    for t in tokens:
        if t in F:
            F[t] = F[t] + 1
        else:
            F[t] = 1
    return F

print(frequencies(input("line: ").lower().split()))


# ---------------------------------------------------------------
# Ejercicio 21 - Sumar rango [a..b]
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def sum_range(a, b):
    s = 0
    for x in range(a, b+1):
        s = s + x
    return s

a = int(input("a: ")); b = int(input("b: "))
print(sum_range(a, b))


# ---------------------------------------------------------------
# Ejercicio 22 - Es palíndromo (texto normalizado)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def is_palindrome(s):
    t = ""
    for ch in s.lower():
        if ch != " ":
            t = t + ch
    left = 0; right = len(t)-1; ok = True
    while (left < right) and ok:
        if t[left] != t[right]:
            ok = False
        left = left + 1
        right = right - 1
    return ok

print(is_palindrome(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 23 - Mayor de tres (solo if)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def max3(a, b, c):
    m = a
    if b > m: m = b
    if c > m: m = c
    return m

a = float(input("a: ")); b = float(input("b: ")); c = float(input("c: "))
print(max3(a, b, c))


# ---------------------------------------------------------------
# Ejercicio 24 - Contar > umbral en lista
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_greater_than(L, T):
    c = 0
    for x in L:
        if x > T:
            c = c + 1
    return c

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
T = float(input("T: "))
print(count_greater_than(L, T))


# ---------------------------------------------------------------
# Ejercicio 25 - Reemplazar en lista (in-place)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def replace_inplace(L, old, new):
    for i in range(len(L)):
        if L[i] == old:
            L[i] = new

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
old = input("old: "); new = input("new: ")
replace_inplace(L, old, new)
print(L)


# ---------------------------------------------------------------
# Ejercicio 26 - Mín y máx en una pasada (tupla)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def min_max(L):
    if len(L) == 0:
        return (None, None)
    mn = L[0]; mx = L[0]
    for x in L:
        if x < mn: mn = x
        if x > mx: mx = x
    return (mn, mx)

print(min_max([float(input("x1: ")), float(input("x2: ")), float(input("x3: "))]))


# ---------------------------------------------------------------
# Ejercicio 27 - Escalar lista por k (nueva)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def scale(L, k):
    R = []
    for x in L:
        R.append(x * k)
    return R

N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
k = float(input("k: "))
print(scale(L, k))


# ---------------------------------------------------------------
# Ejercicio 28 - Intercalar dos listas (hasta min)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def interleave(A, B):
    R = []
    limit = len(A) if len(A) < len(B) else len(B)
    for i in range(limit):
        R.append(A[i]); R.append(B[i])
    return R

NA = int(input("NA: ")); NB = int(input("NB: "))
A = []; B = []
for _ in range(NA):
    A.append(input("A: "))
for _ in range(NB):
    B.append(input("B: "))
print(interleave(A, B))


# ---------------------------------------------------------------
# Ejercicio 29 - Join de números con separador
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def join_numbers(L, sep):
    res = ""
    for i in range(len(L)):
        if i > 0:
            res = res + sep
        res = res + str(L[i])
    return res

print(join_numbers([1,2,3,4], "-"))


# ---------------------------------------------------------------
# Ejercicio 30 - Contar tokens válidos (enteros)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_int_tokens(tokens):
    c = 0
    for t in tokens:
        ok = True
        for ch in t:
            if not ("0" <= ch <= "9"):
                ok = False
        if ok:
            c = c + 1
    return c

print(count_int_tokens(input("tokens: ").split()))


# ---------------------------------------------------------------
# Ejercicio 31 - Frecuencias de bigramas (tuplas)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def bigram_freq(tokens):
    F = {}
    i = 1
    while i < len(tokens):
        pair = (tokens[i-1], tokens[i])
        if pair in F:
            F[pair] = F[pair] + 1
        else:
            F[pair] = 1
        i = i + 1
    return F

print(bigram_freq(input("line: ").lower().split()))


# ---------------------------------------------------------------
# Ejercicio 32 - Cortar lista desde primera aparición
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def cut_from_first(L, val):
    pos = -1
    for i in range(len(L)):
        if pos == -1 and L[i] == val:
            pos = i
    if pos == -1:
        return L[:]
    else:
        return L[:pos]

print(cut_from_first(input("line: ").split(), input("val: ")))


# ---------------------------------------------------------------
# Ejercicio 33 - Token más largo
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def longest(tokens):
    if len(tokens) == 0:
        return ""
    best = tokens[0]
    for t in tokens:
        if len(t) > len(best):
            best = t
    return best

print(longest(input("line: ").split()))


# ---------------------------------------------------------------
# Ejercicio 34 - Normalizar espacios con función
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def normalize_spaces(s):
    toks = s.split()
    res = ""
    for i in range(len(toks)):
        if i > 0:
            res = res + " "
        res = res + toks[i]
    return res

print(normalize_spaces(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 35 - Contar cambios de signo
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def sign_changes(L):
    if len(L) <= 1:
        return 0
    c = 0
    i = 1
    while i < len(L):
        if (L[i-1] < 0 and L[i] > 0) or (L[i-1] > 0 and L[i] < 0):
            c = c + 1
        i = i + 1
    return c

print(sign_changes([float(input("x1: ")), float(input("x2: ")), float(input("x3: "))]))


# ---------------------------------------------------------------
# Ejercicio 36 - Tabla de multiplicar como lista de strings
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def mult_table(n, m):
    L = []
    for i in range(1, m+1):
        L.append(str(n) + " x " + str(i) + " = " + str(n*i))
    return L

print(mult_table(5, 5))


# ---------------------------------------------------------------
# Ejercicio 37 - Contar mayúsculas en texto
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_upper(s):
    c = 0
    for ch in s:
        if "A" <= ch <= "Z":
            c = c + 1
    return c

print(count_upper(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 38 - Matriz identidad (lista de listas)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def identity(n):
    M = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        M.append(row)
    return M

print(identity(int(input("n: "))))


# ---------------------------------------------------------------
# Ejercicio 39 - Sumar matrices (misma dimensión)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def add_matrices(A, B):
    r = len(A); c = len(A[0]) if r>0 else 0
    R = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        R.append(row)
    return R

print(add_matrices([[1,2],[3,4]], [[5,6],[7,8]]))


# ---------------------------------------------------------------
# Ejercicio 40 - Hipotenusa con verificación (math)
# Enunciado: Ejercicio práctico de funciones básicas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
def safe_hyp(a, b):
    if a < 0 or b < 0:
        return None
    return math.sqrt(a*a + b*b)

print(safe_hyp(float(input("a: ")), float(input("b: "))))

