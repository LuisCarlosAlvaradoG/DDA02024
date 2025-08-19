
# ===============================================================
# 7.- ESTRUCTURAS REPETITIVAS: FOR Y RANGO
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
# Reglas pedagógicas de este archivo .py:
#   - En esta sesión se introducen y dominan los ciclos FOR y la función range().
#   - Se permite usar: entrada/salida, operaciones con números y cadenas, if/elif/else
#     (incluyendo anidados), try-except, y los patrones de contadores/acumuladores/centinelas.
#   - while puede aparecer SOLO para validaciones puntuales cuando sea necesario.
#   - ESTRICTAMENTE PROHIBIDO: listas/tuplas/diccionarios, comprensiones, funciones propias,
#     break/continue, librerías externas y manejo de archivos.
#   - Iteraremos SOBRE range() y SOBRE CADENAS exclusivamente (listas vendrán más adelante).
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: ciclo for — sintaxis y flujo
#   C) Teoría: range() — formas y casos
#   D) For sobre cadenas: por carácter y por índice
#   E) For anidados: patrones de texto y tablas
#   F) Contadores y acumuladores con for
#   G) Casos de uso guiados
#   H) Buenas prácticas, ventajas y desventajas
#   I) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Comprender la sintaxis y el flujo del ciclo for.
# - Dominar range() en sus variantes: range(stop), range(start, stop), range(start, stop, step)
#   incluyendo pasos negativos y rangos vacíos.
# - Iterar sobre CADENAS para procesar caracteres (contar, buscar, transformar).
# - Construir for ANIDADOS para producir patrones y tablas sencillas.
# - Aplicar contadores, acumuladores y validación/banderas con for.
#
# ALCANCE Y LÍMITES
# - NO usamos colecciones (listas/tuplas/dicts) ni comprensiones.
# - NO usamos break/continue; resolveremos sin estas sentencias.
# - Podemos usar if/elif/else, try-except, entrada y salida, números y cadenas.

# ---------------------------------------------------------------
# B) TEORÍA: CICLO FOR — SINTAXIS Y FLUJO
# ---------------------------------------------------------------
# Sintaxis base:
#   for variable in iterable:
#       # bloque a repetir
#
# En esta sesión nuestros iterables serán:
#   - range(...)    -> genera secuencias de enteros
#   - cadenas (str) -> generan caracteres uno por uno
#
# Flujo:
# 1) Se obtiene el primer elemento del iterable y se asigna a 'variable'.
# 2) Se ejecuta el bloque.
# 3) Se repite con el siguiente elemento, hasta agotar el iterable.
#
# Importante:
# - El número de iteraciones queda determinado por el iterable (no por una condición booleana).
# - Si el iterable está vacío, el cuerpo no se ejecuta.

# --- Código ilustrativo: for básico con range ---
print("Contar de 0 a 4:")
for i in range(5):           # 0,1,2,3,4
    print("i =", i)

print("Contar de 3 a 7:")
for x in range(3, 8):        # 3,4,5,6,7
    print("x =", x)

print("Pares de 2 a 10 (paso 2):")
for n in range(2, 11, 2):    # 2,4,6,8,10
    print("n =", n)

print("Descendiente de 5 a 1 (paso -1):")
for k in range(5, 0, -1):    # 5,4,3,2,1
    print("k =", k)

# ---------------------------------------------------------------
# C) TEORÍA: range() — FORMAS Y CASOS
# ---------------------------------------------------------------
# Formas:
# - range(stop)                -> 0, 1, ..., stop-1
# - range(start, stop)         -> start, start+1, ..., stop-1
# - range(start, stop, step)   -> start, start+step, ..., < stop
#
# Notas:
# - stop no se incluye (límite superior abierto).
# - step puede ser negativo: range(10, 0, -2) -> 10, 8, 6, 4, 2
# - Si con el step no se puede avanzar hacia el stop, el rango es VACÍO y el for no se ejecuta.
# - range() no crea listas (aún no vistas); es un objeto que genera valores bajo demanda.
#
# Comunes errores:
# - Confundir "n inclusive" con "stop exclusivo": para incluir N usa range(..., N+1).
# - Olvidar que el paso negativo exige start>stop.

# --- Código ilustrativo: variantes de range ---
print("range(0) -> no itera:")
for _ in range(0):
    print("no verás esto")

print("range(2, 2) -> vacío también:")
for _ in range(2, 2):
    print("tampoco verás esto")

print("range(10, 0, -3):")
for v in range(10, 0, -3):   # 10,7,4,1
    print(v)

# ---------------------------------------------------------------
# D) FOR SOBRE CADENAS: POR CARÁCTER Y POR ÍNDICE
# ---------------------------------------------------------------
# Dos enfoques principales:
# 1) Por carácter directo:
#       for ch in s:
#           # trabajar con ch
#    Útil para contar, buscar, filtrar.
#
# 2) Por índice (con range(len(s))):
#       for i in range(len(s)):
#           ch = s[i]
#    Útil cuando necesitas la posición (índice) explícita.
#
# Recordatorio: cadenas son inmutables; para "modificar" se construye una nueva.

# --- Código ilustrativo: cadenas ---
s = "Algoritmos"
count_vowels = 0
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
for ch in s:
    if ch in vowels:
        count_vowels = count_vowels + 1
print("Vocales en", s, "->", count_vowels)

# Índices
t = "Python"
for i in range(len(t)):
    print("t[", i, "] =", t[i])

# ---------------------------------------------------------------
# E) FOR ANIDADOS: PATRONES Y TABLAS
# ---------------------------------------------------------------
# For anidado = un for dentro de otro. El externo controla "filas",
# el interno controla "columnas".
#
# Patrón de rectángulo de asteriscos (r filas x c columnas):
#   for i in range(r):
#       línea = ""
#       for j in range(c):
#           línea = línea + "*"
#       print(línea)
#
# Tabla (ej. multiplicar): dos for anidados para recorrer pares (i, j).

# --- Código ilustrativo: patrones y tabla ---
# Rectángulo 3x5
rows = 3
cols = 5
for i in range(rows):
    line = ""
    for j in range(cols):
        line = line + "*"
    print(line)

# Triángulo incremental (1..5)
for i in range(1, 6):
    print("#" * i)

# Tabla de multiplicar 1..3
for i in range(1, 4):
    for j in range(1, 6):
        print(str(i) + "x" + str(j) + "=" + str(i*j))
    print("---")

# ---------------------------------------------------------------
# F) CONTADORES Y ACUMULADORES CON FOR
# ---------------------------------------------------------------
# Contador: cuenta ocurrencias que cumplen una condición.
# Acumulador: suma/concatena resultados a través del ciclo.
#
# Esquema típico:
#   count = 0
#   for ...:
#       if condición:
#           count = count + 1
#
#   acc = 0
#   for ...:
#       acc = acc + valor

# --- Código ilustrativo: suma de pares y conteo de letras ---
# Suma de pares del 1 al 10
acc = 0
for n in range(1, 11):
    if n % 2 == 0:
        acc = acc + n
print("Sum of even 1..10:", acc)

# Contar cuántas 'a' o 'A' hay en un texto
text = "Aula de Algoritmos"
count_a = 0
for ch in text:
    if ch == "a" or ch == "A":
        count_a = count_a + 1
print("Count 'a'/'A':", count_a)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Suma de N reales (N leído por teclado)
# (Descomenta para usar en clase)
# N = int(input("How many values? "))
# acc = 0.0
# for i in range(N):
#     x = float(input("Value " + str(i+1) + ": "))
#     acc = acc + x
# print("Sum:", acc)

# Caso 2) Impresión de rango con paso
# start = int(input("Start: "))
# stop = int(input("Stop (exclusive): "))
# step = int(input("Step: "))
# for v in range(start, stop, step):
#     print(v)

# Caso 3) Procesamiento de cadena: contar dígitos, letras y otros
# s = input("Text: ")
# digits = 0
# letters = 0
# others = 0
# for ch in s:
#     if "0" <= ch <= "9":
#         digits = digits + 1
#     elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
#         letters = letters + 1
#     else:
#         others = others + 1
# print("Digits:", digits, "Letters:", letters, "Others:", others)

# Caso 4) Tabla de multiplicar de un número hasta m
# n = int(input("n: "))
# m = int(input("m: "))
# for i in range(1, m+1):
#     print(n, "x", i, "=", n*i)

# ---------------------------------------------------------------
# H) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - For es ideal cuando se conoce de antemano el número de iteraciones
#   o cuando se recorre una secuencia (range o cadena).
# - Código compacto y claro comparado con while para contadores simples.
#
# Desventajas / riesgos:
# - Olvidar que range no incluye el límite superior.
# - Usar pasos incompatibles (p. ej., step positivo con start>stop) produce rangos vacíos.
#
# Buenas prácticas:
# - Nombrar claramente las variables de control (i, j) y las de estado (acc, count).
# - Comprobar casos límite: N=0, cadenas vacías, rangos vacíos.
# - Evitar dependencias externas en cada iteración (ej. no convertir repetidamente lo mismo).

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS (CON SOLUCIONES) — SOLO FOR/RANGE Y CADENAS
# ---------------------------------------------------------------
# Indicaciones:
# - NO uses listas/tuplas/diccionarios, comprensiones, break/continue, ni funciones propias.
# - Puedes combinar con if/elif/else, try-except, y entrada/salida.
# - Incluimos SOLUCIONES completas para el docente.

# ---------------------------------------------------------------
# Ejercicio 01 - Contar 0..N-1
# Enunciado: Lee N e imprime 0,1,...,N-1 usando range(N).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
for i in range(N):
    print(i)


# ---------------------------------------------------------------
# Ejercicio 02 - 1..N inclusive
# Enunciado: Lee N e imprime 1..N (si N>=1, de lo contrario no imprime nada).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
for i in range(1, N+1):
    print(i)


# ---------------------------------------------------------------
# Ejercicio 03 - N..1 descendente
# Enunciado: Lee N e imprime N, N-1, ..., 1 con paso -1.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
for i in range(N, 0, -1):
    print(i)


# ---------------------------------------------------------------
# Ejercicio 04 - Suma de 1..N
# Enunciado: Lee N y calcula la suma 1+2+...+N con for.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0
for i in range(1, N+1):
    acc = acc + i
print(acc)


# ---------------------------------------------------------------
# Ejercicio 05 - Producto de 1..N
# Enunciado: Lee N y calcula 1*2*...*N (factorial). Si N=0, el resultado debe ser 1.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
prod = 1
for i in range(1, N+1):
    prod = prod * i
print(prod)


# ---------------------------------------------------------------
# Ejercicio 06 - Suma de pares en [a,b]
# Enunciado: Lee a,b (enteros) y suma solo los pares del intervalo inclusivo.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
if a <= b:
    start = a if a % 2 == 0 else a + 1
    acc = 0
    for n in range(start, b+1, 2):
        acc = acc + n
    print(acc)
else:
    print(0)


# ---------------------------------------------------------------
# Ejercicio 07 - Potencia por sumas repetidas (n * m)
# Enunciado: Lee n y m, calcula el producto n*m sumando n, m veces (for).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
m = int(input("m: "))
acc = 0
for _ in range(m):
    acc = acc + n
print(acc)


# ---------------------------------------------------------------
# Ejercicio 08 - Potencia b^e por multiplicaciones
# Enunciado: Lee base b y exponente e>=0 y calcula b**e multiplicando en un for.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

b = float(input("b: "))
e = int(input("e (>=0): "))
p = 1.0
for _ in range(e):
    p = p * b
print(p)


# ---------------------------------------------------------------
# Ejercicio 09 - Contar vocales
# Enunciado: Lee un texto y cuenta cuántas vocales tiene.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
count = 0
for ch in s:
    if ch in vowels:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 10 - Contar dígitos
# Enunciado: Lee un texto y cuenta cuántos caracteres son dígitos ('0'..'9').
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if "0" <= ch <= "9":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 11 - Invertir cadena con for
# Enunciado: Lee una cadena y produce su inverso construyéndolo con un for descendente.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
for i in range(len(s)-1, -1, -1):
    res = res + s[i]
print(res)


# ---------------------------------------------------------------
# Ejercicio 12 - Primera posición de un carácter
# Enunciado: Lee cadena y carácter, imprime el índice de la primera aparición o -1.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
ch = input("Char: ")[:1]
pos = -1
for i in range(len(s)):
    if (pos == -1) and (s[i] == ch):
        pos = i
print(pos)


# ---------------------------------------------------------------
# Ejercicio 13 - Eliminar todas las 'a'/'A'
# Enunciado: Lee cadena y construye otra sin 'a' ni 'A'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
res = ""
for ch in s:
    if ch != "a" and ch != "A":
        res = res + ch
print(res)


# ---------------------------------------------------------------
# Ejercicio 14 - Triángulo de asteriscos
# Enunciado: Lee h e imprime un triángulo de altura h usando '#'*i.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

h = int(input("Height: "))
for i in range(1, h+1):
    print("#" * i)


# ---------------------------------------------------------------
# Ejercicio 15 - Rectángulo r x c
# Enunciado: Lee r y c e imprime un rectángulo de asteriscos r filas por c columnas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("Rows: "))
c = int(input("Cols: "))
for i in range(r):
    line = ""
    for j in range(c):
        line = line + "*"
    print(line)


# ---------------------------------------------------------------
# Ejercicio 16 - Serie aritmética
# Enunciado: Lee a, d, N e imprime los N términos: a, a+d, a+2d, ...
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
d = float(input("d: "))
N = int(input("N: "))
term = a
for _ in range(N):
    print(term)
    term = term + d


# ---------------------------------------------------------------
# Ejercicio 17 - Serie geométrica
# Enunciado: Lee a, r, N e imprime a, a*r, a*r^2, ...
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
r = float(input("r: "))
N = int(input("N: "))
term = a
for _ in range(N):
    print(term)
    term = term * r


# ---------------------------------------------------------------
# Ejercicio 18 - Suma de cuadrados
# Enunciado: Lee N y calcula 1^2 + 2^2 + ... + N^2.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0
for i in range(1, N+1):
    acc = acc + (i*i)
print(acc)


# ---------------------------------------------------------------
# Ejercicio 19 - Suma de impares
# Enunciado: Lee N y suma los primeros N impares: 1+3+5+...
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0
current = 1
for _ in range(N):
    acc = acc + current
    current = current + 2
print(acc)


# ---------------------------------------------------------------
# Ejercicio 20 - Conteo de mayúsculas
# Enunciado: Lee texto y cuenta letras entre 'A' y 'Z'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if "A" <= ch <= "Z":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 21 - Remover espacios repetidos
# Enunciado: Lee texto y genera otro sin duplicar espacios (nunca dos seguidos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
prev_space = False
for ch in s:
    if ch == " ":
        if not prev_space:
            res = res + " "
            prev_space = True
    else:
        res = res + ch
        prev_space = False
print(res)


# ---------------------------------------------------------------
# Ejercicio 22 - Tabla de multiplicar de n hasta m
# Enunciado: Lee n y m e imprime n x 1..m.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
m = int(input("m: "))
for i in range(1, m+1):
    print(n, "x", i, "=", n*i)


# ---------------------------------------------------------------
# Ejercicio 23 - Tabla 1..a por 1..b (bloques)
# Enunciado: Lee a y b e imprime una tabla con for anidados; separa cada fila con '---'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
for i in range(1, a+1):
    for j in range(1, b+1):
        print(str(i) + "x" + str(j) + "=" + str(i*j))
    print("---")


# ---------------------------------------------------------------
# Ejercicio 24 - Contar 'python' (no solapado)
# Enunciado: Lee texto y cuenta cuántas veces aparece 'python' sin solaparse.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ").lower()
target = "python"
L = len(target)
count = 0
i_jump = 0  # 0 = no salto pendiente
for i in range(len(s)):
    if i_jump > 0:
        i_jump = i_jump - 1
    else:
        if s[i:i+L] == target:
            count = count + 1
            i_jump = L - 1  # saltar los siguientes L-1 índices
print(count)


# ---------------------------------------------------------------
# Ejercicio 25 - Bordes de rectángulo hueco
# Enunciado: Lee r y c e imprime un rectángulo con bordes '*' y espacio dentro.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r = int(input("Rows: "))
c = int(input("Cols: "))
for i in range(r):
    line = ""
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            line = line + "*"
        else:
            line = line + " "
    print(line)


# ---------------------------------------------------------------
# Ejercicio 26 - Conteo de coincidencias posicionales
# Enunciado: Lee dos cadenas y cuenta cuántos índices i tienen el mismo carácter (hasta el mínimo largo).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("A: ")
b = input("B: ")
limit = len(a) if len(a) < len(b) else len(b)
count = 0
for i in range(limit):
    if a[i] == b[i]:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 27 - Cifrado César +1 (solo letras)
# Enunciado: Lee texto y sustituye cada letra por la siguiente en el alfabeto (z->a, Z->A).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
for ch in s:
    if "a" <= ch <= "z":
        if ch == "z":
            res = res + "a"
        else:
            res = res + chr(ord(ch) + 1)
    elif "A" <= ch <= "Z":
        if ch == "Z":
            res = res + "A"
        else:
            res = res + chr(ord(ch) + 1)
    else:
        res = res + ch
print(res)


# ---------------------------------------------------------------
# Ejercicio 28 - Cuenta regresiva formateada
# Enunciado: Lee n e imprime 'n... (n-1)... ... 1... ¡Listo!' en una sola línea.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
line = ""
for i in range(n, 0, -1):
    line = line + str(i) + "... "
line = line + "¡Listo!"
print(line)


# ---------------------------------------------------------------
# Ejercicio 29 - Promedio de N reales
# Enunciado: Lee N y luego N reales; imprime el promedio con 2 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0.0
for i in range(N):
    x = float(input("Value " + str(i+1) + ": "))
    acc = acc + x
if N == 0:
    print("N/A")
else:
    print("{:.2f}".format(acc / N))


# ---------------------------------------------------------------
# Ejercicio 30 - Contar palabras (formato simple)
# Enunciado: Lee una línea (palabras separadas por un solo espacio) y cuenta palabras sin usar split.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Line (single spaces): ").strip()
if s == "":
    print(0)
else:
    count = 1
    for ch in s:
        if ch == " ":
            count = count + 1
    print(count)


# ---------------------------------------------------------------
# Ejercicio 31 - Pirámide centrada
# Enunciado: Lee h e imprime una pirámide centrada de altura h con '*'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

h = int(input("Height: "))
# anchura total = 2*h - 1
for i in range(1, h+1):
    stars = 2*i - 1
    spaces = h - i
    line = ""
    for _ in range(spaces):
        line = line + " "
    for _ in range(stars):
        line = line + "*"
    print(line)


# ---------------------------------------------------------------
# Ejercicio 32 - Alternar mayúscula/minúscula
# Enunciado: Lee texto y alterna el caso: índice par -> mayúscula, impar -> minúscula.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
for i in range(len(s)):
    ch = s[i]
    if i % 2 == 0:
        res = res + ch.upper()
    else:
        res = res + ch.lower()
print(res)


# ---------------------------------------------------------------
# Ejercicio 33 - Conteo de 'ab' en cadena
# Enunciado: Lee texto y cuenta cuántas veces aparece la subcadena 'ab' (no solapado).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
i_jump = 0
for i in range(len(s)):
    if i_jump > 0:
        i_jump = i_jump - 1
    else:
        if s[i:i+2] == "ab":
            count = count + 1
            i_jump = 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 34 - Máximo dígito de un entero
# Enunciado: Lee un entero (texto), recorre sus caracteres y muestra el dígito más grande.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("Integer: ").strip()
start = 1 if raw[:1] == "-" else 0
max_digit = "0"
for i in range(start, len(raw)):
    ch = raw[i]
    if "0" <= ch <= "9":
        if ch > max_digit:
            max_digit = ch
print(max_digit)


# ---------------------------------------------------------------
# Ejercicio 35 - Bordes diagonales (X)
# Enunciado: Lee n e imprime una X de tamaño n con 'X' sobre fondo de espacios.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
for i in range(n):
    line = ""
    for j in range(n):
        if j == i or j == (n-1-i):
            line = line + "X"
        else:
            line = line + " "
    print(line)


# ---------------------------------------------------------------
# Ejercicio 36 - Intercalar dos textos (hasta min len)
# Enunciado: Lee A y B y construye C alternando caracteres A0,B0,A1,B1,... hasta el mínimo largo.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

A = input("A: ")
B = input("B: ")
limit = len(A) if len(A) < len(B) else len(B)
C = ""
for i in range(limit):
    C = C + A[i] + B[i]
print(C)


# ---------------------------------------------------------------
# Ejercicio 37 - Contar letras distintas a espacios
# Enunciado: Lee texto y cuenta caracteres distintos de ' ' (espacio).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if ch != " ":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 38 - Suma de serie 1 + 1/2 + ... + 1/N
# Enunciado: Lee N>=1 y calcula la suma armónica parcial con for.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0.0
for i in range(1, N+1):
    acc = acc + (1.0 / i)
print("{:.6f}".format(acc))


# ---------------------------------------------------------------
# Ejercicio 39 - Suma hasta superar T con entradas fijas
# Enunciado: Lee T y luego N y a continuación N valores; suma hasta que la suma supere T o se acaben los valores.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

T = float(input("Threshold: "))
N = int(input("N: "))
acc = 0.0
count = 0
stop = False
for _ in range(N):
    if not stop:
        x = float(input("Value: "))
        acc = acc + x
        count = count + 1
        if acc > T:
            stop = True
print("Sum:", acc, "| Count:", count)


# ---------------------------------------------------------------
# Ejercicio 40 - Validar N y luego imprimir 1..N
# Enunciado: Lee N validándolo con try-except (repite con while hasta ser entero) y luego imprime 1..N con for.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

valid = False
while not valid:
    raw = input("Enter integer N: ")
    try:
        N = int(raw)
        valid = True
    except ValueError:
        print("Not an integer.")
for i in range(1, N+1):
    print(i)

