
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
       

# Precedencia

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

# Doble

# Combinando lógica


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
