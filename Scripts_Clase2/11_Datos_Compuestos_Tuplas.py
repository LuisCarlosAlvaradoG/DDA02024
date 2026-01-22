# 11.- DATOS COMPUESTOS: TUPLAS — INMUTABILIDAD, EMPAQUETADO Y RECORRIDOS
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UNA TUPLA?
# ---------------------------------------------------------------
# Definición:
# - TUPLA: colección ordenada, INDEXABLE e INMUTABLE (no se puede modificar un elemento).
# - Se escribe con paréntesis () y elementos separados por coma.
#
# Ejemplos:

# Tupla de 1 elemento (¡requiere coma!):
#
# Inmutabilidad:
# - No puedes reasignar t[0] = 99 (TypeError).

# ---------------------------------------------------------------
# B) ÍNDICES Y SLICES; CONCATENACIÓN (+) Y REPETICIÓN (*)
# ---------------------------------------------------------------

# Operadores:

# ---------------------------------------------------------------
# C) RECORRIDOS CON FOR/WHILE; PERTENENCIA 'in'
# ---------------------------------------------------------------

# Pertenencia:

# ---------------------------------------------------------------
# D) MÉTODOS Y OPERACIONES DISPONIBLES
# ---------------------------------------------------------------
# len(t) -> longitud
# t.index(x) -> índice de la primera aparición de x (ValueError si no está)
# t.count(x) -> cuántas veces aparece x
# Conversión: list(t) para obtener lista mutable; tuple(L) para crear tupla desde lista
#

# ---------------------------------------------------------------
# D) EMPAQUETADO Y DESEMPAQUETADO
# ---------------------------------------------------------------
# Empaquetado: se crea una tupla sin paréntesis usando comas.

# Desempaquetado múltiple:

# Swap (intercambio) de variables usando tuplas:

# Desempaquetado con * (estrella) para capturar "el resto":


# Nota: middle es una LISTA (lo permite Python); puedes convertirla a tupla si lo necesitas:

# ---------------------------------------------------------------
# E) TUPLAS ANIDADAS Y TUPLAS CON LISTAS
# ---------------------------------------------------------------
# Tuplas anidadas:

# Tupla con lista interna (la tupla es inmutable, pero la lista sí cambia):
#
# Cuidado: U[0] = 100 -> TypeError (prohibido modificar posiciones de la tupla)
