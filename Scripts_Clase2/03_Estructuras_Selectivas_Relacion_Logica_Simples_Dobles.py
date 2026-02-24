
# ===============================================================
# 3.- ESTRUCTURAS SELECTIVAS: RELACIÓN, LÓGICA, SIMPLES Y DOBLES

# ---------------------------------------------------------------
# A) TEORÍA: VALORES BOOLEANOS Y "VERDAD" EN PYTHON
# ---------------------------------------------------------------
# - Un valor booleano es True o False.
# - Muchas expresiones devuelven booleanos, por ejemplo 3 < 5 -> True.+
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

# --- Código ilustrativo: truthiness explícita ---
x = 5
str(x)
y = "5"
int(y)

bool(1) # True
bool(0) # False
bool(5) # True

bool("a") # True
bool(" ") # True
bool("") # False

# if condición: -> Nota: si el resultado de la condición es True, aplico la operación dentro del if
# si existe un else, el el resultado de la condición es False, aplico la operación dentro del else.
if 0:
    print("Hola")
else:   # Cualquier otro caso
    print("Adiós")
# else no lleva ninguna condición

if 0: 
    print("Hola")

# ---------------------------------------------------------------
# B) TEORÍA: OPERADORES DE RELACIÓN
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
# - == compara valores; 'is' compara identidad de objeto .

# --- Código ilustrativo: relación ---
a = 10
b = 5
print(a == b)  # False
print(a > b)   # True
print(a >= b)   # True
print(a < b)   # False
print(a <= b)   # False
print(a != b)   # True

c = 7
print(a > b > c)  # False
print(a > b < c)  # True

# ---------------------------------------------------------------
# C) TEORÍA: OPERADORES LÓGICOS Y PRECEDENCIA
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

# --- Código ilustrativo: lógica ---
p = (10 > 3)            # True
q = ("py" in "python")  # True
r = (0 == 1)            # False

print(p and q) # True and True -> True
print(p or r)  # True or False -> True
print(q and r) # True and False -> False

# Precedencia
print(not p or q) # not True or True -> False or True -> True
print(not (p or q)) # not (True or True) -> not (True) -> False

# ---------------------------------------------------------------
# D) TEORÍA: IF (SIMPLE) e IF-ELSE (DOBLE)
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

# --- Código ilustrativo: if simples y dobles ---
# Simple
x = 17
if x >= 18: # x >= 18 -> True
    print("Acceso concedido")

# Doble
x = 15
if x >= 18:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Combinando lógica
edad = 18
nacionalidad = "Española"

if (edad >= 18) or (nacionalidad.lower() == "mexicana"):
    print("Acceso concedido")
else:
    print("Acceso denegado")


# ---------------------------------------------------------------
# E) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
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
# Ejercicio 04 - Máximo entre dos
# Enunciado: Lee dos enteros y muestra el mayor; si no es mayor el primero, 
# muestra el segundo (empates incluidos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
a = int(input()) # 1
b = int(input()) # 10

if a > b:
    print(a)
else:
    print(b)

# ---------------------------------------------------------------
# Ejercicio 05 - Texto largo o corto
# Enunciado: Lee un texto y muestra 'Long' si su longitud > 10; si no, 'Short'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
m = input()

if len(m) > 10:
    print("Long")
else:
    print("Short")

# ---------------------------------------------------------------
# Ejercicio 11 - Vocal o no
# Enunciado: Lee un solo carácter y muestra 'Vocal' si es vocal; si no, 'Otro'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
# 'a' -> 'Vocal'
# 'c' -> 'Otro'
# '5' -> 'Otro'
c =  input()
vocales = "aeiouáéíóú"

if c.strip().lower() in vocales:
    print("Vocal")
else:
    print("Otro")

s = " Hola "
s.strip()