
# ===============================================================
# 3.- ESTRUCTURAS SELECTIVAS: RELACIÓN, LÓGICA, SIMPLES Y DOBLES
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
# Reglas pedagógicas de este archivo .py:
#   - SOLO se usan conceptos ya vistos: entrada/salida, operaciones con números y cadenas,
#     y AHORA condiciones SIMPLES (if) y DOBLES (if-else) con operadores de RELACIÓN y LÓGICA.
#   - ESTRICTAMENTE PROHIBIDO (en esta sesión): elif (múltiples), if anidados, while/for,
#     try/except, funciones definidas por el usuario, listas/tuplas/diccionarios.
#   - Objetivo: dominar la toma de decisiones binarias (sí/no) combinando relaciones y lógica.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: valores booleanos y verdad en Python
#   C) Teoría: operadores de RELACIÓN (==, !=, <, <=, >, >=) y encadenados
#   D) Teoría: operadores LÓGICOS (and, or, not) y precedencia
#   E) Teoría: if (simple) e if-else (doble)
#   F) Casos de uso secuenciales con condiciones (scripts guiados)
#   G) Buenas prácticas, ventajas y desventajas
#   H) Banco de ejercicios (con SOLUCIONES completas, sin elif/loops)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Comprender cómo Python evalúa expresiones a valores booleanos: True/False.
# - Usar operadores de RELACIÓN para comparar números y cadenas.
# - Usar operadores LÓGICOS para combinar condiciones.
# - Escribir decisiones SIMPLES (if) y DOBLES (if-else) sin elif ni anidar if.
# - Resolver problemas BINARIOS (dos rutas) con entradas por teclado y salidas formateadas.
#
# ALCANCE Y LIMITACIONES EN ESTA SESIÓN
# - NO se usa elif (se verá en la Sesión 4). NO if anidados.
# - NO se usan ciclos. NO se usan colecciones. NO se usa manejo de excepciones.
# - Se pueden usar operaciones numéricas y de cadenas estudiadas en la Sesión 2.

# ---------------------------------------------------------------
# B) TEORÍA: VALORES BOOLEANOS Y "VERDAD" EN PYTHON
# ---------------------------------------------------------------
# - Un valor booleano es True o False.
# - Muchas expresiones devuelven booleanos, por ejemplo 3 < 5 -> True.
# - "Verdad" en Python (truthiness):
#   * Números: 0 es False; cualquier otro número es True.
#   * Cadenas: "" (vacía) es False; cualquier cadena no vacía es True.
# - Estas reglas permiten usar directamente números o cadenas en condiciones,
#   aunque por claridad conviene comparar explícitamente.
#
# Ejemplo (solo demostración):
#   if 5:        # True porque 5 != 0
#       print("Cinco es verdadero en contexto booleano")
#   if "hola":   # True porque no es cadena vacía
#       print("Cadena no vacía es verdadera")
#
# En esta sesión preferiremos condiciones explícitas como: if x != 0, if s != "".

# --- Código ilustrativo: truthiness explícita ---
value_num = 10
value_str = "python"
print("bool(10) ->", bool(value_num))
print("bool('python') ->", bool(value_str))
print("bool(0) ->", bool(0))
print("bool('') ->", bool(""))

# ---------------------------------------------------------------
# C) TEORÍA: OPERADORES DE RELACIÓN
# ---------------------------------------------------------------
# ==  igualdad           (cuidado: para comparar, no confundir con = de asignación)
# !=  desigualdad
# <   menor que
# <=  menor o igual que
# >   mayor que
# >=  mayor o igual que
#
# COMPARACIÓN DE CADENAS
# - Es lexicográfica por código Unicode; "A" < "a" porque 'A' (65) < 'a' (97).
# - Suele ser buena idea normalizar con .lower() o .upper() antes de comparar.
#
# COMPARACIONES ENCADENADAS
# - Python permite: 1 < x < 10  (equivale a: 1 < x and x < 10)
# - Es útil para chequear intervalos sin escribir x dos veces.
#
# IGUALDAD vs IDENTIDAD
# - == compara valores; 'is' compara identidad de objeto (no usaremos 'is' aquí).

# --- Código ilustrativo: relación ---
a = 7
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a <= 7:", a <= 7)
print("b > 5:", b > 5)
print("'Ana' == 'ana':", "Ana" == "ana")
print("'ana'.lower() == 'ana':", "ana".lower() == "ana")
x = 5
print("1 < x < 10:", 1 < x < 10)  # encadenada

# ---------------------------------------------------------------
# D) TEORÍA: OPERADORES LÓGICOS Y PRECEDENCIA
# ---------------------------------------------------------------
# and : True si ambas condiciones son True.
# or  : True si al menos una condición es True.
# not : invierte el valor booleano (not True -> False).
#
# PRECEDENCIA (de mayor a menor):
# 1) not
# 2) and
# 3) or
# - Usar paréntesis para dejar claro el orden es una buena práctica.
#
# CORTOCIRCUITO (short-circuit):
# - En (A and B): si A es False, no evalúa B.
# - En (A or B): si A es True, no evalúa B.
# - En esta sesión, nos basta entender que esto ocurre; no haremos trucos avanzados.

# --- Código ilustrativo: lógica ---
p = (10 > 3)          # True
q = ("py" in "python") # True
r = (0 == 1)          # False

print("p and q:", p and q)      # True
print("p or r:", p or r)        # True
print("not r:", not r)          # True

# Precedencia
print("not p or q:", not p or q)      # (not p) or q
print("not (p or q):", not (p or q))  # niega la disyunción

# ---------------------------------------------------------------
# E) TEORÍA: IF (SIMPLE) e IF-ELSE (DOBLE)
# ---------------------------------------------------------------
# IF (SIMPLE)
#   if condicion:
#       # bloque si True
#
# IF-ELSE (DOBLE)
#   if condicion:
#       # bloque si True
#   else:
#       # bloque si False
#
# REGLAS DIDÁCTICAS DE ESTA SESIÓN
# - Solo se permite UNA condición con posible else (no elif, no anidados).
# - La condición puede combinar relaciones con and/or/not.
# - Se pueden usar conversiones de tipos y operaciones estudiadas en Sesión 2.
#
# EJEMPLOS (ver código a continuación).

# --- Código ilustrativo: if simples y dobles ---
# Simple
temperature = 101.0
if temperature >= 100.0:
    print("Boiling or above (>= 100°C)")

# Doble
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Combinando lógica
total = 1200.0
has_coupon = "yes"
if (total >= 1000.0) and (has_coupon.lower() == "yes"):
    print("Discount applies")
else:
    print("No discount")

# ---------------------------------------------------------------
# F) CASOS DE USO (SEC UENCIALES, sin elif/loops)
# ---------------------------------------------------------------

# Caso 1) Acceso sencillo por contraseña (igualdad de cadena, normalizando)
# (Descomenta para probar)
# pwd = input("Password: ")
# if pwd.strip() == "abc123":
#     print("Access granted")
# else:
#     print("Access denied")

# Caso 2) Umbral de envío gratis (números + formateo)
# subtotal = float(input("Subtotal: "))
# if subtotal >= 799.0:
#     print("Free shipping!")
# else:
#     shipping = 99.0
#     print("Shipping cost: ${:.2f}".format(shipping))

# Caso 3) Verificación de rango (comparación encadenada)
# x = float(input("Enter a value for x: "))
# if 0.0 <= x <= 1.0:
#     print("x in [0,1]")
# else:
#     print("x outside [0,1]")

# Caso 4) Comparación de cadenas sin sensibilidad a mayúsculas
# city = input("City: ")
# if city.strip().lower() == "guadalajara":
#     print("Hola, tapatío/a.")
# else:
#     print("Bienvenido/a.")

# ---------------------------------------------------------------
# G) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - Permite controlar el flujo según condiciones del problema.
# - Combinación con operadores lógicos resuelve decisiones binarias complejas.
#
# Desventajas / riesgos:
# - Comparaciones con floats pueden verse afectadas por precisión (usar tolerancias).
# - Comparaciones de cadenas sensibles a mayúsculas y espacios (normalizar con strip/lower).
# - Código poco legible si se abusa de condiciones largas sin paréntesis.
#
# Buenas prácticas:
# - Expresar condiciones de forma clara y directa; usar paréntesis explicativos.
# - Normalizar entradas de texto: .strip(), .lower() antes de comparar.
# - Para floats, considerar tolerancia: abs(a-b) <= 1e-9 (según magnitud).

# ---------------------------------------------------------------
# H) BANCO DE EJERCICIOS (SIN elif, SIN anidar, SIN ciclos) — SOLUCIONES INCLUIDAS
# ---------------------------------------------------------------
# Indicaciones:
# - Usa solo if (simple) o if-else (doble).
# - Puedes combinar condiciones con and/or/not y operadores de relación.
# - Se permiten operaciones numéricas y de cadenas (Sesión 2).
# - Todas las soluciones están completas para el docente.

# ---------------------------------------------------------------
# Ejercicio 01 - Par o impar
# Enunciado: Lee un entero y muestra 'Even' si es par; en otro caso 'Odd'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("Integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# ---------------------------------------------------------------
# Ejercicio 02 - Mayoría de edad
# Enunciado: Lee una edad y muestra 'Adult' si >= 18; si no, 'Minor'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

age = int(input("Age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")


# ---------------------------------------------------------------
# Ejercicio 03 - Contraseña simple
# Enunciado: Lee una contraseña y compara con 'secreto' normalizando espacios y mayúsculas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

pwd = input("Password: ")
if pwd.strip().lower() == "secreto":
    print("Access granted")
else:
    print("Access denied")


# ---------------------------------------------------------------
# Ejercicio 04 - Máximo entre dos
# Enunciado: Lee dos enteros y muestra el mayor; si no es mayor el primero, muestra el segundo (empates incluidos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
if a > b:
    print(a)
else:
    print(b)  # incluye caso de empate


# ---------------------------------------------------------------
# Ejercicio 05 - Texto largo o corto
# Enunciado: Lee un texto y muestra 'Long' si su longitud > 10; si no, 'Short'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
if len(s) > 10:
    print("Long")
else:
    print("Short")


# ---------------------------------------------------------------
# Ejercicio 06 - Aprobado
# Enunciado: Lee una calificación (0-10) y muestra 'Pass' si >= 6.0; en otro caso 'Fail'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

grade = float(input("Grade (0-10): "))
if grade >= 6.0:
    print("Pass")
else:
    print("Fail")


# ---------------------------------------------------------------
# Ejercicio 07 - Envío gratis
# Enunciado: Lee subtotal y muestra 'Free shipping' si >= 799; de lo contrario, 'Shipping: $99.00'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

subtotal = float(input("Subtotal: "))
if subtotal >= 799.0:
    print("Free shipping")
else:
    print("Shipping: $99.00")


# ---------------------------------------------------------------
# Ejercicio 08 - Dentro del intervalo
# Enunciado: Lee x y muestra 'Inside' si 0 <= x <= 1; de lo contrario 'Outside'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
if 0.0 <= x <= 1.0:
    print("Inside")
else:
    print("Outside")


# ---------------------------------------------------------------
# Ejercicio 09 - Casi iguales
# Enunciado: Lee a y b y muestra 'Close' si |a-b| <= 1e-9; en otro caso 'Far'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
if abs(a - b) <= 1e-9:
    print("Close")
else:
    print("Far")


# ---------------------------------------------------------------
# Ejercicio 10 - Contiene 'python'
# Enunciado: Lee una cadena y muestra 'Found' si contiene 'python' (ignorando mayúsculas).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
if "python" in s.lower():
    print("Found")
else:
    print("Not found")


# ---------------------------------------------------------------
# Ejercicio 11 - Vocal o no
# Enunciado: Lee un solo carácter y muestra 'Vowel' si es vocal; si no, 'Other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

ch = input("Char: ")
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
if ch[:1] in vowels:
    print("Vowel")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 12 - Dos dígitos
# Enunciado: Lee un entero y muestra 'Two-digit' si está entre 10 y 99 (incluidos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
if 10 <= n <= 99:
    print("Two-digit")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 13 - Descuento
# Enunciado: Lee total y cupón('yes'/'no'); si total>=1000 y cupón==yes -> 'Discount'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

total = float(input("Total: "))
coupon = input("Coupon (yes/no): ")
if (total >= 1000.0) and (coupon.strip().lower() == "yes"):
    print("Discount")
else:
    print("No discount")


# ---------------------------------------------------------------
# Ejercicio 14 - Bisiesto
# Enunciado: Lee un año y muestra 'Leap' si divisible por 4 y (no por 100 o sí por 400).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

y = int(input("Year: "))
if (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0)):
    print("Leap")
else:
    print("Not leap")


# ---------------------------------------------------------------
# Ejercicio 15 - XOR simple
# Enunciado: Lee dos banderas ('yes'/'no') y muestra 'True' si exactamente una es 'yes'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("Flag A (yes/no): ").strip().lower() == "yes"
b = input("Flag B (yes/no): ").strip().lower() == "yes"
# XOR sin operadores especiales: (a and not b) or (not a and b)
if (a and (not b)) or ((not a) and b):
    print("True")
else:
    print("False")


# ---------------------------------------------------------------
# Ejercicio 16 - Recargo por tarjeta
# Enunciado: Lee método ('cash' o 'card') y precio; si 'card' agrega 3% y muestra total.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

method = input("Method (cash/card): ").strip().lower()
price = float(input("Price: "))
if method == "card":
    total = price * 1.03
    print("Total: {:.2f}".format(total))
else:
    print("Total: {:.2f}".format(price))


# ---------------------------------------------------------------
# Ejercicio 17 - Palíndromo
# Enunciado: Lee una palabra y muestra 'Palindrome' si s == s[::-1].
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Word: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# ---------------------------------------------------------------
# Ejercicio 18 - Signo
# Enunciado: Lee un real y muestra 'Positive' si >0; si no, 'Non-positive'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
if x > 0:
    print("Positive")
else:
    print("Non-positive")


# ---------------------------------------------------------------
# Ejercicio 19 - Capitalización inicial
# Enunciado: Lee una palabra y muestra 'OK' si su primera letra es mayúscula.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
if w[:1] == w[:1].upper() and w != "":
    print("OK")
else:
    print("Not OK")


# ---------------------------------------------------------------
# Ejercicio 20 - Correo permitido
# Enunciado: Lee un correo y muestra 'Allowed' si termina con '@uni.mx'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

mail = input("Email: ")
if mail.strip().endswith("@uni.mx"):
    print("Allowed")
else:
    print("Not allowed")


# ---------------------------------------------------------------
# Ejercicio 21 - Calefacción
# Enunciado: Lee temperatura y muestra 'ON' si < 18.0, si no 'OFF'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t = float(input("Temperature (C): "))
if t < 18.0:
    print("ON")
else:
    print("OFF")


# ---------------------------------------------------------------
# Ejercicio 22 - Cercanía
# Enunciado: Lee dos reales y umbral; muestra 'Close' si |a-b|<=umbral; si no 'Far'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
thr = float(input("threshold: "))
if abs(a - b) <= thr:
    print("Close")
else:
    print("Far")


# ---------------------------------------------------------------
# Ejercicio 23 - Solo letras (simple)
# Enunciado: Lee un carácter y muestra 'Alpha' si 'a'<=ch<='z' o 'A'<=ch<='Z'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

ch = input("Char: ")
c = ch[:1]
if ("a" <= c <= "z") or ("A" <= c <= "Z"):
    print("Alpha")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 24 - Arroba en texto
# Enunciado: Lee una cadena y muestra 'Has @' si contiene '@'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
if "@" in s:
    print("Has @")
else:
    print("No @")


# ---------------------------------------------------------------
# Ejercicio 25 - Minúsculas completas
# Enunciado: Lee una palabra y muestra 'lower' si s == s.lower(); si no, 'other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
if w == w.lower():
    print("lower")
else:
    print("other")


# ---------------------------------------------------------------
# Ejercicio 26 - Múltiplos
# Enunciado: Lee un entero y muestra 'FizzBuzz' si divisible por 3 y por 5; si no, 'Other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 27 - Largo mínimo
# Enunciado: Lee contraseña y muestra 'OK' si len>=8; si no, 'Too short'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

pwd = input("Password: ")
if len(pwd) >= 8:
    print("OK")
else:
    print("Too short")


# ---------------------------------------------------------------
# Ejercicio 28 - Intervalo (0,1)
# Enunciado: Lee x y muestra 'Inside' si 0<x<1; si no, 'Outside'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
if 0.0 < x < 1.0:
    print("Inside")
else:
    print("Outside")


# ---------------------------------------------------------------
# Ejercicio 29 - Dominio .com
# Enunciado: Lee una URL y muestra 'COM' si termina con '.com' (tras strip).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

url = input("URL: ")
if url.strip().lower().endswith(".com"):
    print("COM")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 30 - Rango seguro
# Enunciado: Lee temperatura y muestra 'Safe' si 18<=t<=24; si no, 'Unsafe'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t = float(input("Temperature (C): "))
if 18.0 <= t <= 24.0:
    print("Safe")
else:
    print("Unsafe")


# ---------------------------------------------------------------
# Ejercicio 31 - Misma inicial
# Enunciado: Lee dos palabras y muestra 'Same' si comparten el primer carácter.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w1 = input("Word 1: ")
w2 = input("Word 2: ")
if w1[:1] == w2[:1] and w1 != "" and w2 != "":
    print("Same")
else:
    print("Different")


# ---------------------------------------------------------------
# Ejercicio 32 - Múltiplo
# Enunciado: Lee a y b y muestra 'Yes' si a es múltiplo de b (b != 0 asumido).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
if b != 0 and a % b == 0:
    print("Yes")
else:
    print("No")


# ---------------------------------------------------------------
# Ejercicio 33 - Upper completo
# Enunciado: Lee una palabra y muestra 'UPPER' si w == w.upper(); si no, 'other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
if w == w.upper():
    print("UPPER")
else:
    print("other")


# ---------------------------------------------------------------
# Ejercicio 34 - Punto final
# Enunciado: Lee una oración y muestra 'OK' si termina con '.' (tras strip).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Sentence: ")
if s.strip().endswith("."):
    print("OK")
else:
    print("Missing dot")


# ---------------------------------------------------------------
# Ejercicio 35 - Plan válido
# Enunciado: Lee 'basic'/'pro' y muestra 'Valid' si es uno de esos; si no, 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

plan = input("Plan (basic/pro): ").strip().lower()
if (plan == "basic") or (plan == "pro"):
    print("Valid")
else:
    print("Invalid")


# ---------------------------------------------------------------
# Ejercicio 36 - Tres iguales
# Enunciado: Lee a, b, c y muestra 'All equal' si a==b y b==c (una sola condición).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("a: ")
b = input("b: ")
c = input("c: ")
if (a == b) and (b == c):
    print("All equal")
else:
    print("Not all equal")


# ---------------------------------------------------------------
# Ejercicio 37 - Extensión .py
# Enunciado: Lee un nombre de archivo y muestra 'Python file' si termina con '.py'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

fname = input("Filename: ")
if fname.lower().endswith(".py"):
    print("Python file")
else:
    print("Other file")


# ---------------------------------------------------------------
# Ejercicio 38 - Positivo y par
# Enunciado: Lee un entero y muestra 'OK' si es >0 y par; si no, 'NO'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
if (n > 0) and (n % 2 == 0):
    print("OK")
else:
    print("NO")


# ---------------------------------------------------------------
# Ejercicio 39 - Autorización simple
# Enunciado: Lee user y token; muestra 'Authorized' si user=='admin' y token=='XYZ'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

user = input("User: ")
token = input("Token: ")
if (user == "admin") and (token == "XYZ"):
    print("Authorized")
else:
    print("Denied")


# ---------------------------------------------------------------
# Ejercicio 40 - Mínimo de caracteres
# Enunciado: Lee un texto y un mínimo m; si len(text)>=m -> 'OK', si no 'Too short'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

text = input("Text: ")
m = int(input("Minimum: "))
if len(text) >= m:
    print("OK")
else:
    print("Too short")

