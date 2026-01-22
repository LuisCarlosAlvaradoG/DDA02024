# 7.- ESTRUCTURAS REPETITIVAS: FOR Y RANGO
# ---------------------------------------------------------------
# A) TEORÍA: CICLO FOR — SINTAXIS Y FLUJO
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


# ---------------------------------------------------------------
# B) TEORÍA: range() — FORMAS Y CASOS
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


# ---------------------------------------------------------------
# C) FOR SOBRE CADENAS: POR CARÁCTER Y POR ÍNDICE
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


# Índices

# ---------------------------------------------------------------
# D) FOR ANIDADOS: PATRONES Y TABLAS
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


# Triángulo incremental (1..5)

# Tabla de multiplicar 1..3

# ---------------------------------------------------------------
# D) CONTADORES Y ACUMULADORES CON FOR
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


# Contar cuántas 'a' o 'A' hay en un texto



# ---------------------------------------------------------------
# E) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
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
