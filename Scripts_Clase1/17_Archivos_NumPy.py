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
ar = np.arange(0, 10, 2) #Inicio, Fin (excluyente), Paso
# list(range(0, 10, 2))
print(ar)
lin = np.linspace(0, 1, 5)
print(lin)
full = np.full((2, 3), 7)
print(full)
eye = np.eye(4)
print(eye)

# Comparaciones de listas vs arrays
lista = [5, 7, 6, 3, 2]
suma = 0
for valor in lista:
    suma += valor
print(suma)
suma_numpy = np.sum(np.array(lista))
print(suma_numpy)

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
M[1][1]

suma = 0
for i in range(len(M)):
    for j in range(len(M[0])):
        if j == 0:
            suma += M[i][j]
print(suma)

suma_numpy_matriz = np.sum(np.array(M)[:,0]) # filas, columnas
print(suma_numpy_matriz)
# ---------------------------------------------------------------
# B) INDEXACIÓN Y SLICING; VISTAS VS. COPIAS
# ---------------------------------------------------------------
v = np.arange(10)
print(v)
print(v[3])
print(v[2:6])
print(v[:5])
print(v[5:])

M = np.arange(1, 13).reshape(3, 4)
print(M)
# M[1][1]
print(M[1,1]) # Diferencia con listas, cambiamos el doble corchete por uno solo separado por comas
print(M[0:2 , 0:2]) #filas, columnas
print(M[:,0])

# Vistas comparten memoria:
v = np.arange(10)
print(v)
s = v[2:7]
print(s)

s[:] = -1
print(s)
print(v)

# Copia explícita:
v = np.arange(10)
print(v)
s = v.copy()
print(s)

s[:] = -1
print(s)
print(v)

# 3D básico (didáctico):
T = np.arange(1,25).reshape(2, 3, 4)
print(T)

# ---------------------------------------------------------------
# C) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]
print(lista1 + lista2)

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
print(x + y)
print(x**2)

# Broadcasting (3,1) + (3,) => (3,3)
col = np.array([[1], [2], [3]])
row = np.array([10, 20, 30])
col.shape, row.shape

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

A.var()
A.var(axis = 0)
A.var(axis = 1)

A.std()
A.std(axis = 0)
A.std(axis = 1)

# ---------------------------------------------------------------
# E) MASKS, WHERE, UNIQUE, SET OPS
# ---------------------------------------------------------------
import numpy as np
B = np.array([3, 8, 1, 5, 8, 2, 8])
# ¿qué valores son 8?
mask = (B == 8)
print(f"La cantidad de números en el array que son iguales a 8 es: {np.sum(mask)}")
mask2 = (B >= 5)
print(B[mask2])

np.where(B > 3, 1, 0) # Condición, Valor cuando es True, Valor cuando es False

np.unique(B) # Devuelve valores únicos

# Teoría de conjuntos
C = np.array([1, 2, 3, 4, 5])
D = np.array([4, 5, 6, 7])
np.intersect1d(C, D)
np.union1d(C, D)
np.setdiff1d(C, D)

# ---------------------------------------------------------------
# F) RESHAPE, CONCAT, APILADO
# ---------------------------------------------------------------
X = np.arange(6).reshape(2, 3)
Y = np.arange(6, 12).reshape(2, 3)

np.vstack([X, Y])

np.hstack([X, Y])

np.concatenate([X, Y], axis = 1)


# ---------------------------------------------------------------
# G) I/O CON NUMPY: loadtxt, genfromtxt, savetxt
# ---------------------------------------------------------------
def create_num_csv(path):
    ids = np.arange(1, 11).reshape(-1, 1) # .reshape(10, 1) en este caso
    x = np.linspace(0, 9, 10).reshape(-1, 1)
    y = x*2.5 + 3
    data = np.hstack([ids, x, y])
    np.savetxt(path, data, delimiter=",", fmt="%.6f")

# Uso sugerido en clase:
create_num_csv("np_basic.csv")
data = np.loadtxt("np_basic.csv", delimiter=",")
print(data)
# =============================================================================
# H) ALEATORIOS (Generator, semilla, permutaciones, muestreos)
# =============================================================================
rng = np.random.default_rng(42)
rng.integers(0, 11, size = 5)

# --- Reproducibilidad básica (semilla fija) ---

# --- Enteros aleatorios ---
# low inclusivo, high exclusivo

# --- Permutaciones / Mezclas ---

# --- Muestreo con/ sin reemplazo ---
poblacion = np.array(["Alina", "Uriel", "Santi", "Sam", "Beto"])
muestra = rng.choice(poblacion, size=3, replace=False)
print(muestra)
muestra_replace = rng.choice(poblacion, size=1, replace=True)
print(muestra_replace)
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
rng = np.random.default_rng(42)
mu, sigma = 21, 2.5
normal = rng.normal(loc = mu, scale= sigma, size = 12000)
print(normal)

import matplotlib.pyplot as plt
plt.hist(normal, bins=30)
plt.show()

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