# 15.- USO DE BIBLIOTECAS DE FUNCIONES (STANDARD LIBRARY BÁSICA)
# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UN MÓDULO?
# ---------------------------------------------------------------
# - Un MÓDULO es un archivo con funciones, clases y constantes reutilizables.
# - La BIBLIOTECA ESTÁNDAR de Python incluye muchos módulos listos para usar.
# - Formas de importación (recomendaciones para cursos iniciales):
#
#   1) import nombre_modulo
#      Luego: nombre_modulo.funcion(...)
#
#   2) from nombre_modulo import nombre
#      Luego: nombre(...)
#
#   3) import nombre_modulo as alias
#      Luego: alias.funcion(...)
#
# - Evita importar con * (from modulo import *) en cursos iniciales porque contamina el espacio de nombres.
#
# - Depuración: puedes imprimir valores intermedios y usar una bandera DEBUG global para activar/desactivar trazas.

# ---------------------------------------------------------------
# C) MÓDULO math: CONSTANTES Y FUNCIONES NUMÉRICAS
# ---------------------------------------------------------------
import math

# Constantes:
print(math.pi)          # π
print(math.e)           # e

# Raíz cuadrada (dominio: x >= 0):
try:
    print(math.sqrt(25))
    # print("sqrt(-1) ->", math.sqrt(-1))  # ValueError
except ValueError:
    print("ValueError: dominio inválido")

# Potencias y valores absolutos (pow, fabs):
print(math.pow(2, 10))   
print(math.fabs(-3.5))   

# Piso y techo (enteros):
print(math.floor(3.7))   
print(math.ceil(3.1))    

# Conversión grados<->radianes y trigonometría básica:
deg = 30
rad = math.radians(deg)
print(rad)
print(math.sin(rad))
print(math.cos(rad))

# Comparación con tolerancia (flotantes): math.isclose
a = 0.1 + 0.2
b = 0.3
print("0.1+0.2 == 0.3 ?", (a == b))
print(math.isclose(a, b, rel_tol=1e-9))

# ---------------------------------------------------------------
# D) MÓDULO random: ALEATORIEDAD Y REPRODUCIBILIDAD
# ---------------------------------------------------------------
import random

# Semilla: fija la secuencia (útil para depurar o reproducir ejemplos)
random.seed(12345)

# Enteros aleatorios en [a, b] (incluye extremos):
print(random.randint(1,6))

# choice: elige un elemento de una lista no vacía
faces = ["A", "B", "C", "D"]
print(random.choice(faces))

# sample: muestra SIN reemplazo
print(random.sample(range(10), 5))

# shuffle: baraja in-place una lista
L = [1, 2, 3, 4, 5]
random.shuffle(L)
print(L)

# uniform: flotantes en [a, b]
print(random.uniform(0,1))

# ---------------------------------------------------------------
# E) MÓDULO statistics: MEDIDAS SIMPLES
# ---------------------------------------------------------------
import statistics

data = [10, 20, 20, 30, 40, 40, 40]
print(statistics.mean(data))     # promedio
print(statistics.median(data)) # mediana

# ---------------------------------------------------------------
# F) MÓDULO string: CONSTANTES Y LIMPIEZA DE TEXTO
# ---------------------------------------------------------------
import string

print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

# Limpieza de una línea: quitar puntuación y pasar a minúsculas
line = "¡Hola, mundo! Programar es GENIAL: 100% diversión."
# Construimos una nueva cadena sin puntuación:
clean = ""
for ch in line:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        clean = clean + ch
clean = clean.lower()
toks = clean.split()
print(toks)

# Contar frecuencias con diccionario:
freq = {}
for t in toks:
    if t in freq:
        freq[t] = freq[t] + 1
    else:
        freq[t] = 1
print(freq)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Normalizar y tokenizar texto usando 'string' y construir histograma con dict
import string
s = input("Texto: ")
cleaned = ""
for ch in s:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        cleaned = cleaned + ch
toks = cleaned.lower().split()
hist = {}
for w in toks:
    if w in hist: hist[w] = hist[w] + 1
    else: hist[w] = 1
print(hist)

# Caso 2) Simulación de dados con 'random' y resumen con 'statistics'
import random, statistics
random.seed(2024)  # fija la semilla para reproducción
N = int(input("Tiros de dado: "))
rolls = []
for _ in range(N):
    rolls.append(random.randint(1,6))
print("mean:", statistics.mean(rolls))
print("median:", statistics.median(rolls))
print("multimode:", statistics.multimode(rolls))

# Caso 3) Geometría simple con 'math': hipotenusa y ángulos
import math
a = float(input("cateto a: "))
b = float(input("cateto b: "))
hyp = math.sqrt(a*a + b*b)
ang = math.degrees(math.atan2(b, a))  # ángulo en grados
print("hipotenusa:", hyp, "ángulo:", ang)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización de soluciones probadas (funciones listas para usar).
# - Claridad: 'import math' comunica intención; menos código propio a mantener.
# - Consistencia y precisión: p.ej., 'statistics.mean' y 'math.isclose' evitan errores comunes.
#
# Desventajas / riesgos:
# - Mal uso de importaciones (espacios de nombres contaminados) puede causar choques de nombres.
# - Depender de funciones sin entender precondiciones (dominio de sqrt, modo único en statistics.mode).
#
# Buenas prácticas:
# - Prefiere 'import modulo' y usa el prefijo 'modulo.funcion' para legibilidad.
# - Documenta supuestos (rango de datos, dominios) y captura excepciones (ValueError, StatisticsError).
# - Para reproducibilidad con 'random', fija 'random.seed(...)' durante ejemplos y pruebas.
# - Activa una bandera DEBUG para imprimir valores intermedios si hace falta.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Raíz segura con try-except (math.sqrt)
# Enunciado: 
import math
x = float(input("x: "))
try:
    print(math.sqrt(x))
except ValueError:
    print("dominio inválido")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Grados a radianes y seno/coseno
# Enunciado: 
import math
deg = float(input("deg: "))
rad = math.radians(deg)
print(rad, math.sin(rad), math.cos(rad))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Redondeo hacia abajo y arriba (floor/ceil)
# Enunciado: 
import math
x = float(input("x: "))
print(math.floor(x), math.ceil(x))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Comparar floats con isclose
# Enunciado: 
import math
a = float(input("a: "))
b = float(input("b: "))
print(math.isclose(a, b, rel_tol=1e-9))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Aleatorio: barajar y tomar muestra
# Enunciado: 
import random
random.seed(2025)
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
random.shuffle(L)
k = int(input("k: "))
print("shuffled:", L)
print("sample:", random.sample(L, k if k<=len(L) else len(L)))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Dados: N tiros y frecuencia por cara
# Enunciado: 
import random
random.seed(7)
N = int(input("N: "))
freq = {1:0,2:0,3:0,4:0,5:0,6:0}
for _ in range(N):
    r = random.randint(1,6)
    freq[r] = freq[r] + 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Media, mediana y moda (statistics)
# Enunciado: 
import statistics
vals = []
N = int(input("N: "))
for _ in range(N):
    vals.append(float(input("x: ")))
print("mean:", statistics.mean(vals))
print("median:", statistics.median(vals))
try:
    print("mode:", statistics.mode(vals))
except statistics.StatisticsError:
    print("mode: not unique")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - multimode siempre (statistics.multimode)
# Enunciado: 
import statistics
tokens = input("tokens: ").split()
print(statistics.multimode(tokens))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Quitar puntuación y contar tokens (string)
# Enunciado: 
import string
s = input("text: ")
clean = ""
for ch in s:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        clean = clean + ch
toks = clean.lower().split()
freq = {}
for t in toks:
    if t in freq: freq[t] = freq[t] + 1
    else: freq[t] = 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Contraseña: verificar que tenga dígitos y letras (string)
# Enunciado: 
import string
pwd = input("password: ")
has_digit = False
has_alpha = False
for ch in pwd:
    if ch in string.digits: has_digit = True
    if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        has_alpha = True
print("OK" if (has_digit and has_alpha) else "WEAK")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Hipotenusa (math.sqrt) y ángulo (atan2)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
a = float(input("a: ")); b = float(input("b: "))
h = math.sqrt(a*a + b*b)
ang = math.degrees(math.atan2(b, a))
print(h, ang)


# ---------------------------------------------------------------
# Ejercicio 12 - Potencias y raíz n-ésima con pow
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
x = float(input("x: "))
n = int(input("n: "))
# x**(1/n) usando pow; si x<0 y n par -> dominio real inválido
if x < 0 and (n % 2 == 0):
    print("dominio inválido")
else:
    print("pow(x,n):", math.pow(x, n))
    print("root n:", math.pow(x, 1.0/n))


# ---------------------------------------------------------------
# Ejercicio 13 - Simular moneda N veces (random)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(1)
N = int(input("N: "))
h = 0; t = 0
for _ in range(N):
    if random.randint(0,1) == 0:
        h = h + 1
    else:
        t = t + 1
print("H:", h, "T:", t)


# ---------------------------------------------------------------
# Ejercicio 14 - Seleccionar al azar k elementos distintos
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(42)
L = input("items: ").split()
k = int(input("k: "))
if k <= len(L):
    print(random.sample(L, k))
else:
    print(L)  # si k > len(L), devolvemos todos


# ---------------------------------------------------------------
# Ejercicio 15 - Media truncada: eliminar extremos y promediar
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import statistics
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
if len(L) <= 2:
    print("N insuficiente")
else:
    # quitar min y max (una vez cada uno)
    # encontrar posiciones
    mn = L[0]; mx = L[0]; pmin = 0; pmax = 0
    for i in range(len(L)):
        if L[i] < mn: mn = L[i]; pmin = i
        if L[i] > mx: mx = L[i]; pmax = i
    R = []
    for i in range(len(L)):
        if i != pmin and i != pmax:
            R.append(L[i])
    print("mean:", statistics.mean(R))


# ---------------------------------------------------------------
# Ejercicio 16 - Moda robusta con multimode
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import statistics
L = input("items: ").split()
M = statistics.multimode(L)
print("modas:", M)


# ---------------------------------------------------------------
# Ejercicio 17 - Construir string de dígitos válidos (string.digits)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("text: ")
only_digits = ""
for ch in s:
    if ch in string.digits:
        only_digits = only_digits + ch
print(only_digits)


# ---------------------------------------------------------------
# Ejercicio 18 - Eliminar puntuación (string.punctuation)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("text: ")
clean = ""
for ch in s:
    if ch not in string.punctuation:
        clean = clean + ch
print(clean)


# ---------------------------------------------------------------
# Ejercicio 19 - Barajar varias veces y mostrar primeras m cartas
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(99)
deck = input("deck items: ").split()
m = int(input("m: "))
T = int(input("times: "))
for _ in range(T):
    random.shuffle(deck)
print(deck[:m])


# ---------------------------------------------------------------
# Ejercicio 20 - Generar vector aleatorio de enteros [a,b]
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(321)
n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))
V = []
for _ in range(n):
    V.append(random.randint(a,b))
print(V)


# ---------------------------------------------------------------
# Ejercicio 21 - Ángulo entre dos vectores 2D (math)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
ax = float(input("ax: ")); ay = float(input("ay: "))
bx = float(input("bx: ")); by = float(input("by: "))
dot = ax*bx + ay*by
na = math.sqrt(ax*ax + ay*ay)
nb = math.sqrt(bx*bx + by*by)
if na == 0 or nb == 0:
    print("indefinido")
else:
    cosang = dot / (na*nb)
    # limitar cosang a [-1,1] por errores numéricos
    if cosang < -1: cosang = -1
    if cosang > 1: cosang = 1
    ang = math.degrees(math.acos(cosang))
    print(ang)


# ---------------------------------------------------------------
# Ejercicio 22 - Promedio y desviación absoluta media (manual + statistics.mean)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import statistics
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(float(input("x: ")))
if len(L) == 0:
    print("N/A")
else:
    m = statistics.mean(L)
    s = 0.0
    for x in L:
        s = s + abs(x - m)
    mad = s / len(L)
    print("mean:", m, "MAD:", mad)


# ---------------------------------------------------------------
# Ejercicio 23 - Contar letras ascii (string.ascii_letters)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("text: ")
letters = 0
for ch in s:
    if ch in string.ascii_letters:
        letters = letters + 1
print(letters)


# ---------------------------------------------------------------
# Ejercicio 24 - Filtro: solo tokens alfabéticos (string.ascii_letters)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
toks = input("tokens: ").split()
R = []
for t in toks:
    ok = True
    for ch in t:
        if ch not in string.ascii_letters:
            ok = False
    if ok:
        R.append(t)
print(R)


# ---------------------------------------------------------------
# Ejercicio 25 - Simular selección sin reemplazo (random.sample)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(11)
items = input("items: ").split()
k = int(input("k: "))
k = k if k <= len(items) else len(items)
print(random.sample(items, k))


# ---------------------------------------------------------------
# Ejercicio 26 - Construir histograma de notas (statistics.mean para promedio)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import statistics
N = int(input("N: "))
grades = []
for _ in range(N):
    grades.append(float(input("grade: ")))
H = {}
for g in grades:
    b = int(g) // 10 * 10
    label = str(b) + "-" + str(b+9)
    if label in H: H[label] = H[label] + 1
    else: H[label] = 1
print("hist:", H, "mean:", statistics.mean(grades) if len(grades)>0 else "N/A")


# ---------------------------------------------------------------
# Ejercicio 27 - Texto: normalizar con string y contar top-1 (manual)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("text: ")
clean = ""
for ch in s:
    if ch not in string.punctuation and ch != "¡" and ch != "¿":
        clean = clean + ch
tokens = clean.lower().split()
freq = {}
for t in tokens:
    if t in freq: freq[t] = freq[t] + 1
    else: freq[t] = 1
best_k = None; best_v = 0
for k in freq:
    if best_k is None or freq[k] > best_v:
        best_k = k; best_v = freq[k]
print(best_k, best_v)


# ---------------------------------------------------------------
# Ejercicio 28 - Aproximar π por Monte Carlo (random)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random, math
random.seed(77)
N = int(input("samples: "))
inside = 0
i = 0
while i < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x*x + y*y <= 1.0:
        inside = inside + 1
    i = i + 1
pi_est = 4.0 * inside / N if N>0 else 0.0
print("pi_est:", pi_est, "close?:", math.isclose(pi_est, math.pi, rel_tol=1e-1))


# ---------------------------------------------------------------
# Ejercicio 29 - Escalar vector con math.fabs para magnitud
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
N = int(input("N: "))
V = []
for _ in range(N):
    V.append(float(input("x: ")))
k = float(input("k: "))
R = []
for x in V:
    R.append(k*x)
mag = 0.0
for x in R:
    mag = mag + x*x
mag = math.sqrt(mag)
print(R, mag, math.fabs(mag))


# ---------------------------------------------------------------
# Ejercicio 30 - Aleatorizar orden de preguntas (random.shuffle)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
random.seed(555)
Q = []
n = int(input("n questions: "))
for _ in range(n):
    Q.append(input("Q: "))
random.shuffle(Q)
print(Q)


# ---------------------------------------------------------------
# Ejercicio 31 - Segmentar tokens alfanuméricos (string.digits y ascii_letters)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
toks = input("tokens: ").split()
alpha = []
num = []
other = []
for t in toks:
    if all([(ch in string.ascii_letters) for ch in t]):
        alpha.append(t)
    elif all([(ch in string.digits) for ch in t]):
        num.append(t)
    else:
        other.append(t)
print("alpha:", alpha, "num:", num, "other:", other)


# ---------------------------------------------------------------
# Ejercicio 32 - Medidas de tendencia central de enteros (statistics)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import statistics
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(int(input("x: ")))
print("mean:", statistics.mean(L) if len(L)>0 else "N/A")
print("median:", statistics.median(L) if len(L)>0 else "N/A")
try:
    print("mode:", statistics.mode(L))
except statistics.StatisticsError:
    print("mode: not unique")


# ---------------------------------------------------------------
# Ejercicio 33 - Validar matrícula: 3 letras + 3 dígitos (string)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("id: ")
ok = (len(s) == 6)
i = 0
while ok and i < 3:
    if s[i] not in string.ascii_letters: ok = False
    i = i + 1
j = 3
while ok and j < 6:
    if s[j] not in string.digits: ok = False
    j = j + 1
print("VALID" if ok else "INVALID")


# ---------------------------------------------------------------
# Ejercicio 34 - Crear contraseña aleatoria con letras y dígitos (random, string)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random, string
random.seed(909)
length = int(input("length: "))
pool = string.ascii_letters + string.digits
pwd = ""
i = 0
while i < length:
    pwd = pwd + random.choice(pool)
    i = i + 1
print(pwd)


# ---------------------------------------------------------------
# Ejercicio 35 - Contar signos de puntuación en texto (string.punctuation)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
s = input("text: ")
c = 0
for ch in s:
    if ch in string.punctuation: c = c + 1
print(c)


# ---------------------------------------------------------------
# Ejercicio 36 - Normalizar números con floor y ceil (math)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
x = float(input("x: "))
print("floor:", math.floor(x), "ceil:", math.ceil(x))


# ---------------------------------------------------------------
# Ejercicio 37 - Vector unitario (math.sqrt)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
x = float(input("x: ")); y = float(input("y: "))
n = math.sqrt(x*x + y*y)
if n == 0:
    print("N/A")
else:
    print([x/n, y/n])


# ---------------------------------------------------------------
# Ejercicio 38 - Aleatorio controlado por seed (random.seed)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import random
seed = int(input("seed: "))
random.seed(seed)
print(random.randint(1,100), random.randint(1,100), random.randint(1,100))


# ---------------------------------------------------------------
# Ejercicio 39 - Detectar tokens con caracteres no permitidos (string)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import string
allowed = string.ascii_letters + string.digits + "_"
toks = input("tokens: ").split()
bad = []
for t in toks:
    ok = True
    for ch in t:
        if ch not in allowed:
            ok = False
    if not ok:
        bad.append(t)
print(bad)


# ---------------------------------------------------------------
# Ejercicio 40 - Comparar preciso vs. con tolerancia (isclose)
# Enunciado: Ejercicio de práctica con bibliotecas estándar.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import math
a = 0.1 + 0.2
b = float(input("b: "))
print("==:", a == b, "isclose:", math.isclose(a, b, rel_tol=1e-9))

