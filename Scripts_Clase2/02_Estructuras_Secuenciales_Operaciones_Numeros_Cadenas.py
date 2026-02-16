# ===============================================================
# 2.- ESTRUCTURAS SECUENCIALES: OPERACIONES, NÚMEROS Y CADENAS

# ---------------------------------------------------------------
# A) TEORÍA: NÚMEROS, LITERALES Y OPERADORES ARITMÉTICOS
# ---------------------------------------------------------------
# TIPOS NUMÉRICOS EN ESTA SESIÓN
# - int  : enteros de precisión arbitraria (no hay overflow en Python por magnitud).
# - float: números en punto flotante (doble precisión IEEE-754).
#
# LITERALES
# - Enteros: 0, 1, 42, -7
# - Separador visual con guion bajo: 1_000_000 (equivale a 1000000)
# - Flotantes: 3.14, -0.5, 2.0, .5, 5., 1e3 (1000.0), 2.5e-3 (0.0025)
#
# OPERADORES ARITMÉTICOS
# +  suma
# -  resta (también negación unaria, p. ej., -x)
# *  multiplicación
# /  división real (siempre produce float)
# // división entera (floor division)
# %  módulo (residuo)
# ** potencia (exponenciación)
#
# OBSERVACIONES
# - / siempre devuelve float (ej. 5/2 -> 2.5)
# - // "piso": 5//2 -> 2, -5//2 -> -3 (redondea hacia abajo)
# - % cumple: a == (a//b)*b + (a % b) para b != 0
# - ** tiene mayor precedencia que * y /.
# - Cuidado con la precisión en float; 0.1 + 0.2 puede ser 0.30000000000000004.

# --- Código ilustrativo: literales y operaciones ---
a = 1_000_000 
b = 250_000
c = 3.5e2  # 350.0
d = .75
e = 5.

# Aritmética básica
x = 10
y = 3
print("x + y = ", x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)   # división entera
print(x % y)    # residuo
print(x ** y)   # potencia

x = 5
y = 3
z = 4
x + y // z ** x
# Identidad: a == (a//b)*b + (a % b)
num = 29
x = 5
print(num == x)
print(num > x)
print(num != x)
print(num == (num // x) * x + (num % x))
# Precisión en float (simple demostración)
x = 0.1
y = 0.2
z = 0.3
print(z == x + y)
print(x + y)

import math
print(math.isclose(z, x+y))
# ---------------------------------------------------------------
# B) TEORÍA: PRECEDENCIA Y ASOCIATIVIDAD
# ---------------------------------------------------------------
# (De mayor a menor prioridad en lo que usamos aquí)
# 1) **        (derecha a izquierda)
# 2) *, /, //, %
# 3) +, -
# - Los paréntesis alteran el orden y SIEMPRE son la mejor forma de dejar claro
#   qué se desea calcular primero.
# - Asociatividad:
#   - ** es derecha a izquierda: 2**3**2 = 2**(3**2) = 2**9 = 512
#   - *, /, //, %, +, - son izquierda a derecha.

# --- Código ilustrativo: precedencia y paréntesis ---
print(2 ** 3 ** 2)   # 512
print((2 ** 3) ** 2) # 64

print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20

# ---------------------------------------------------------------
# C) TEORÍA: CONVERSIÓN DE TIPOS Y FUNCIONES NUMÉRICAS BÁSICAS
# ---------------------------------------------------------------
# CONVERSIÓN 
# - int("10")    -> 10
# - float("3.5") -> 3.5
# - str(42)      -> "42"
# - int(3.9)     -> 3     (trunca)
# - float(5)     -> 5.0
#
# FUNCIONES INTEGRADAS ÚTILES
# - abs(x)         : valor absoluto
# - round(x)       : redondeo al entero más cercano; .5 redondea al par más cercano (Banker's rounding)
# - round(x, n)    : redondeo con n decimales
# - pow(a, b)      : potencia (equivalente a a ** b)
# - min(x, y, ...) : mínimo
# - max(x, y, ...) : máximo

# --- Código ilustrativo: casting y funciones numéricas ---
n = 20
type(n)
type(str(n))

int("15")
float("2.75")
x = 123
x * 3
str(x) * 3

abs(-7)
round(2.5)
round(3.5)

n = 3
red = round(3.141592, n)

min(-6, 2, 3, 8, -1, 0)
max(-6, 2, 3, 8, -1, 0)

# ---------------------------------------------------------------
# D) TEORÍA: CADENAS (STRINGS), OPERADORES Y MÉTODOS
# ---------------------------------------------------------------
# CADENAS (str)
# - Secuencias de caracteres inmutables.
# - Se pueden delimitar con comillas simples '...' o dobles "..." indistintamente.
# - Soportan escape de caracteres: \\n (salto de línea), \\t (tab), \\\\ (backslash), \\' y \\".
# - Se pueden escribir cadenas multilínea con triples comillas: ''' ... ''' o \"\"\" ... \"\"\"
#
# OPERACIONES BÁSICAS
# - Concatenación: "Hola" + " " + "Mundo"
# - Repetición: "ha" * 3  -> "hahaha"
# - Longitud: len("texto")
# - Acceso por índice:  s[0], s[1], ..., s[len(s)-1]
# - Índices negativos: s[-1] (último), s[-2], etc.
# - Rebanado (slicing): s[inicio:fin:paso]
#   * inicio incluido, fin excluido; cualquiera puede omitirse.
#   * Ejemplos: s[:3], s[3:], s[1:5], s[::-1] (inverso)
#
# MÉTODOS FRECUENTES 
# - s.upper(), s.lower(), s.title()
# - s.strip(), s.lstrip(), s.rstrip()
# - s.replace(old, new)
# - s.find(sub)      -> índice o -1 si no existe
# - s.startswith(pre), s.endswith(suf)
# - s.split(sep)     -> lista de partes (aún no profundizamos en listas)
# - 'sep'.join(iterable_de_cadenas)  -> une con separador
#
# FORMATO DE CADENAS
# - "Alumno: {} | Cal: {:.2f}".format(name, score)
# - f"Alumno: {name} | Cal: {score:.2f}"
# - Alineación/ancho: {:>10}, {:<10}, {:^10}, relleno con ceros: {:06d}
# - Separador de miles: format(1000000, ',')  -> '1,000,000'
#
# INMUTABILIDAD
# - s[0] = 'H'  -> ERROR (no se puede asignar por índice).
# - Para "modificar", se construye una nueva cadena.


# --- Código ilustrativo: cadenas ---
s = "Python"
len(s)

p = "reconocer"
p[4] # Extraer la letra n
p[::-1]
p == p[::-1]

p = "algoritmos"
p[::-1]
# Acceso y slicing
n = "1234"
suma = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
suma

suma = int(n[0] + n[1] + n[2] + n[3])
suma
# sintaxis slicing [inicio : fin : paso]

# Métodos de limpieza y transformación

# Búsqueda y comprobaciones

# split y join (solo demostración de resultado)

# Formato


# ---------------------------------------------------------------
# E) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Operadores aritméticos y de cadenas permiten construir soluciones sin control de flujo.
# - Formateo de cadenas mejora la presentación de resultados.
# - Separadores en literales facilitan la lectura (1_000_000).
#
# Desventajas / riesgos:
# - Precisión en float: pequeñas diferencias por representación binaria.
# - round() usa redondeo al par en .5, lo cual puede sorprender a principiantes.
# - Inmutabilidad de cadenas: "modificar" requiere crear una nueva cadena.
#
# Buenas prácticas:
# - Usar paréntesis para dejar clara la intención en expresiones complejas.
# - Mantener nombres descriptivos y consistentes.
# - Al formatear dinero, mostrar 2 decimales y alinear columnas.
