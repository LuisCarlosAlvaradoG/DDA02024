# 17.- ARCHIVOS: NUMPY — ARREGLOS, VECTORIZACIÓN, BROADCASTING, I/O

import numpy as np

# ---------------------------------------------------------------
# A) ARREGLOS: CREACIÓN, DTYPE, SHAPE
# ---------------------------------------------------------------
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

b.shape

ceros = np.zeros((2, 3))
print(ceros)
unos = np.ones((2, 3))
print(unos)
ar = np.arange(10, 0, -2)
print(ar)
lin = np.linspace(0, 10, 5)
print(lin)
full = np.full((2,2), 7)
print(full)
eye = np.eye(4)
print(eye)

# Comparación de listas vs arrays
lista = [1, 2, 3, 4, 5]
suma = 0
for x in lista:
    suma += x
print(suma)
suma_numpy = np.sum(np.array(lista))
print(suma_numpy)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0
for x in matriz:
    suma += x[0]
print(suma)

suma_matriz = np.sum(np.array(matriz)[:,0])
print(suma_matriz)

# ---------------------------------------------------------------
# B) INDEXACIÓN Y SLICING; VISTAS VS. COPIAS
# ---------------------------------------------------------------
v = np.arange(10)
print(v[3])
print(v[2:7])
print(v[:5])
print(v[5:])

M = np.arange(12).reshape(3, 4)
print(M)
print(M[1, 2])   # filas, columnas
print(M[0:2, 1:3])
print(M[:,0])

# Vistas comparten memoria:
s = v[2:7]
s[:] = -1
print(v)

# Copia explícita:
v_copy = v.copy()
v_copy[0] = 999
print(v_copy)
print(v)

# 3D básico (didáctico):
T = np.arange(24).reshape(2, 3, 4)  # profundidad, filas, columnas
print(T)


# ---------------------------------------------------------------
# C) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
print(x + y)
print(x*y)
print(x**2)

# Cómo se tendría que hacer con listas
lista1 = [1, 2, 3, 4] 
lista2 = [10, 20, 30, 40]
resultado = []
for i, j in zip(lista1, lista2):
    resultado.append(i + j)
print(resultado)

# Broadcasting (3,1) + (3,) => (3,3)
col = np.array([[1], [2], [3]])
row = np.array([10, 20, 30])
print(col + row)

# ---------------------------------------------------------------
# D) AGREGACIONES Y ESTADÍSTICAS
# ---------------------------------------------------------------
A = np.arange(1, 13).reshape(3, 4)
print(A)

A.sum()
A.sum(axis = 0)
A.sum(axis = 1)

A.mean()
A.mean(axis = 0)
A.mean(axis = 1)

A.std()
A.std(axis = 0)
A.std(axis = 1)

A.argmin()
A.argmax()
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