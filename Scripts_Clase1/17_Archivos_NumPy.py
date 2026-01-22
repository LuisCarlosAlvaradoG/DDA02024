# 17.- ARCHIVOS: NUMPY — ARREGLOS, VECTORIZACIÓN, BROADCASTING, I/O

import numpy as np

# ---------------------------------------------------------------
# A) ARREGLOS: CREACIÓN, DTYPE, SHAPE
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# B) INDEXACIÓN Y SLICING; VISTAS VS. COPIAS
# ---------------------------------------------------------------

# Vistas comparten memoria:

# Copia explícita:

# 3D básico (didáctico):

# ---------------------------------------------------------------
# C) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------


# Broadcasting (3,1) + (3,) => (3,3)

# ---------------------------------------------------------------
# D) AGREGACIONES Y ESTADÍSTICAS
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# E) MASKS, WHERE, UNIQUE, SET OPS
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# F) RESHAPE, CONCAT, APILADO
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# G) I/O CON NUMPY: loadtxt, genfromtxt, savetxt
# ---------------------------------------------------------------


# Uso sugerido en clase:

# =============================================================================
# H) ALEATORIOS (Generator, semilla, permutaciones, muestreos)
# =============================================================================

# --- Reproducibilidad básica (semilla fija) ---

# --- Enteros aleatorios ---
# low inclusivo, high exclusivo

# --- Permutaciones / Mezclas ---

# --- Muestreo con/ sin reemplazo ---

# --- Muestreo ponderado (probabilidades p deben sumar 1) ---

# --- Barajar filas de una matriz (mantener columnas alineadas) ---

# =============================================================================
# I) NUMPY — DISTRIBUCIONES (parámetros, ejemplos y usos típicos)
# =============================================================================

# -------------------------------
# UNIFORME
# -------------------------------

# -------------------------------
# NORMAL (Gaussiana)
# -------------------------------

# Estandarizada (media 0, var 1)

# -------------------------------
# PROB-UTILIDADES: UÁR y elección ponderada
# -------------------------------
# Escenario: asignar aleatoriamente “expertos” a tickets con pesos por prioridad



# ---------------------------------------------------------------
# J) VENTAJAS / DESVENTAJAS / BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas: velocidad, vectorización, broadcasting, API numérica rica.
# Desventajas: arreglos homogéneos, faltantes menos cómodos que en pandas.
# Buenas prácticas: documentar shapes; evitar copias innecesarias; preferir ufuncs.