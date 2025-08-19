
# ===============================================================
# 17.- ARCHIVOS: NUMPY — ARREGLOS, VECTORIZACIÓN, BROADCASTING, I/O
# Curso: Algoritmos y Programación (Python) — Sesión (~3 horas)
# Teoría/comentarios: ESPAÑOL  |  Código: INGLÉS
# Restricción: SOLO NumPy (sin pandas/matplotlib).
# ===============================================================

"""
Estructura del archivo:
A) Objetivos
B) Arreglos: creación, dtype, shape
C) Indexación y slicing (1D, 2D, 3D), vistas vs. copias
D) Vectorización, ufuncs, broadcasting
E) Agregaciones y estadísticas
F) Boolean masks, where, unique, set operations
G) Reshape, concatenación y apilado
H) I/O con NumPy: loadtxt, genfromtxt, savetxt (CSV/TSV)
I) Casos de uso guiados
J) Ventajas, desventajas y buenas prácticas
K) Banco de ejercicios (SOLUCIONES incluidas)
"""

import numpy as np

# ---------------------------------------------------------------
# A) OBJETIVOS
# ---------------------------------------------------------------
# - Comprender el ndarray como estructura central de datos numéricos.
# - Practicar vectorización para evitar bucles explícitos de Python.
# - Dominar broadcasting e indexación avanzada.
# - Leer y escribir datos tabulares usando solo NumPy.
# - Resolver ejercicios de práctica con soluciones integradas.

# ---------------------------------------------------------------
# B) ARREGLOS: CREACIÓN, DTYPE, SHAPE
# ---------------------------------------------------------------
a = np.array([1, 2, 3], dtype=np.int64)
b = np.array([[1.0, 2.0], [3.0, 4.0]])
print("a:", a, "| dtype:", a.dtype, "| shape:", a.shape)
print("b:\n", b, "| dtype:", b.dtype, "| shape:", b.shape)

zeros = np.zeros((2, 3))
ones  = np.ones((2, 3))
ar    = np.arange(0, 10, 2)           # [0,2,4,6,8]
lin   = np.linspace(0.0, 1.0, 5)      # 5 puntos entre 0 y 1
full7 = np.full((2,2), 7)
eye3  = np.eye(3, dtype=int)
print(zeros, ones, ar, lin, full7, eye3, sep="\n")

# ---------------------------------------------------------------
# C) INDEXACIÓN Y SLICING; VISTAS VS. COPIAS
# ---------------------------------------------------------------
v = np.arange(10)  # [0..9]
print("v[3] ->", v[3])
print("v[2:7] ->", v[2:7])
print("v[:5] ->", v[:5], " | v[5:] ->", v[5:])

M = np.arange(12).reshape(3,4)
print("M:\n", M)
print("M[1,2] ->", M[1,2])
print("M[0:2,1:3]:\n", M[0:2,1:3])

# Vistas comparten memoria:
s = v[2:7]; s[:] = -1
print("after modifying slice, v:", v)  # también cambia v

# Copia explícita:
v_copy = v.copy(); v_copy[0]=999
print("v_copy:", v_copy, "| v:", v)

# 3D básico (didáctico):
T = np.arange(24).reshape(2,3,4)  # (profundidad, filas, cols)
print("T shape:", T.shape, "| T[1,:,2] ->", T[1,:,2])

# ---------------------------------------------------------------
# D) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------
x = np.array([1,2,3,4.])
y = np.array([10,20,30,40.])
print("x+y:", x+y, " | x*y:", x*y, " | x**2:", x**2)

# Broadcasting (3,1) + (3,) => (3,3)
col = np.array([[1],[2],[3]])
row = np.array([10,20,30])
print("col + row:\n", col + row)

angles = np.linspace(0, np.pi, 5)
print("sin:", np.sin(angles))
print("exp:", np.exp([0,1,2]))

# ---------------------------------------------------------------
# E) AGREGACIONES Y ESTADÍSTICAS
# ---------------------------------------------------------------
A = np.arange(1,13).reshape(3,4)
print("A:\n", A)
print("sum:", A.sum(), "| axis0:", A.sum(axis=0), "| axis1:", A.sum(axis=1))
print("mean:", A.mean(), "| std:", A.std(), "| min:", A.min(), "| max:", A.max())
print("argmin:", A.argmin(), "| argmax:", A.argmax())

# ---------------------------------------------------------------
# F) MASKS, WHERE, UNIQUE, SET OPS
# ---------------------------------------------------------------
B = np.array([3,8,1,5,8,2,8])
mask = (B==8)
print("mask:", mask, "| selected:", B[mask])
print("where(B>3):", np.where(B>3,1,0))
print("unique:", np.unique(B))

C = np.array([1,2,3,4,5])
D = np.array([4,5,6,7])
print("intersect:", np.intersect1d(C,D))
print("union:", np.union1d(C,D))
print("setdiff C-D:", np.setdiff1d(C,D))

# ---------------------------------------------------------------
# G) RESHAPE, CONCAT, APILADO
# ---------------------------------------------------------------
X = np.arange(6).reshape(2,3)
Y = np.arange(6,12).reshape(2,3)
print("vstack:\n", np.vstack([X,Y]))
print("hstack:\n", np.hstack([X,Y]))
print("concatenate axis=1:\n", np.concatenate([X,Y], axis=1))

# ---------------------------------------------------------------
# H) I/O CON NUMPY: loadtxt, genfromtxt, savetxt
# ---------------------------------------------------------------
def create_num_csv(path):
    """Crea un CSV con columnas: id, x, y (y = 2.5*x + 3)."""
    ids = np.arange(1,11).reshape(-1,1)
    x = np.linspace(0.0, 9.0, 10).reshape(-1,1)
    y = x*2.5 + 3.0
    data = np.hstack([ids, x, y])
    np.savetxt(path, data, delimiter=",", fmt="%.6f")

# Uso sugerido en clase:
# create_num_csv("np_basic.csv")
# data = np.loadtxt("np_basic.csv", delimiter=",")
# print("loaded shape:", data.shape, "| head:\n", data[:5])

# ---------------------------------------------------------------
# I) CASOS GUIADOS
# ---------------------------------------------------------------
def minmax_scale(v):
    """Devuelve (v - min)/(max - min). Maneja caso max==min."""
    v = v.astype(float); mn=v.min(); mx=v.max()
    return np.zeros_like(v) if mx==mn else (v-mn)/(mx-mn)

def zscore_cols(M):
    """Estandariza columnas: (x - mu)/sigma, evitando división por cero."""
    M = M.astype(float); mu = M.mean(axis=0); sd = M.std(axis=0)
    sd = np.where(sd==0, 1.0, sd)
    return (M - mu) / sd

def pairwise_dist_2d(P):
    """Matriz de distancias euclidianas entre puntos 2D."""
    A = P[:,None,:]; B = P[None,:,:]
    return np.sqrt(((A-B)**2).sum(axis=2))

print("minmax demo:", minmax_scale(np.array([5,10,15,20])))
print("zscore demo:\n", zscore_cols(np.arange(12).reshape(3,4)))
print("pairwise demo:\n", pairwise_dist_2d(np.array([[0,0],[1,0],[1,1]])))

# ---------------------------------------------------------------
# J) VENTAJAS / DESVENTAJAS / BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas: velocidad, vectorización, broadcasting, API numérica rica.
# Desventajas: arreglos homogéneos, faltantes menos cómodos que en pandas.
# Buenas prácticas: documentar shapes; evitar copias innecesarias; preferir ufuncs.

# ---------------------------------------------------------------
# K) BANCO DE EJERCICIOS (SOLUCIONES INCLUIDAS) — 25 EJERCICIOS
# ---------------------------------------------------------------

# 01) dtype y astype
v = np.array([1,2,3,4], dtype=np.int32); print(v.dtype); print(v.astype(np.float64))

# 02) Indexación 2D y slicing
M = np.arange(1,13).reshape(3,4); print(M[1,2], M[0:2,1:3])

# 03) Broadcasting col + row
col = np.arange(1,4).reshape(3,1); row = np.array([10,20,30]); print(col+row)

# 04) Ufunc trig
x = np.linspace(0, np.pi, 4); print(np.sin(x), np.cos(x))

# 05) Agregaciones por eje
A = np.arange(12).reshape(3,4); print(A.sum(axis=0), A.mean(axis=1))

# 06) Máscara y where
v = np.array([3,7,1,9]); print(v[v>3]); print(np.where(v%2==0,0,1))

# 07) unique e intersección
a = np.array([1,2,2,3,4,4]); b = np.array([3,4,5]); print(np.unique(a), np.intersect1d(a,b))

# 08) Reshape y concatenar
X = np.arange(6).reshape(2,3); Y = np.arange(6,12).reshape(2,3); print(np.concatenate([X,Y],axis=0))

# 09) Min-max manual
v = np.array([5.,10.,15.]); mn=v.min(); mx=v.max(); print((v-mn)/(mx-mn) if mx!=mn else np.zeros_like(v))

# 10) Z-score por columnas
M = np.arange(12).reshape(3,4).astype(float); mu=M.mean(axis=0); sd=M.std(axis=0); sd=np.where(sd==0,1,sd); print((M-mu)/sd)

# 11) Distancias 2D por broadcasting
P = np.array([[0,0],[2,0],[2,2]], float); A_=P[:,None,:]; B_=P[None,:,:]; print(np.sqrt(((A_-B_)**2).sum(axis=2)))

# 12) argsort
v = np.array([5,1,4,2,3]); idx=np.argsort(v); print(idx, v[idx])

# 13) Reemplazar negativos por 0
v = np.array([-3,0,5,-1]); print(np.where(v<0,0,v))

# 14) Sumar por bloques (reshape)
v = np.arange(12); B = v.reshape(4,3); print(B.sum(axis=1))

# 15) vstack/hstack
a = np.array([1,2,3]); b = np.array([4,5,6]); print(np.vstack([a,b])); print(np.hstack([a,b]))

# 16) Producto punto y norma
x = np.array([1,2,3.]); y = np.array([4,5,6.]); print((x*y).sum(), np.sqrt((x*x).sum()))

# 17) Guardar CSV con savetxt
X = np.arange(1,6).reshape(-1,1); Y = 2*X + 1; D = np.hstack([X,Y]); np.savetxt("np_ex17.csv", D, delimiter=",", fmt="%.0f"); print("saved np_ex17.csv")

# 18) Cargar CSV y promedio
try:
    D = np.loadtxt("np_ex17.csv", delimiter=","); print(D.mean(axis=0))
except OSError:
    print("Missing file")

# 19) Centrar columnas
M = np.arange(12).reshape(3,4).astype(float); mu = M.mean(axis=0); print(M-mu)

# 20) Seleccionar columnas con take
M = np.arange(20).reshape(5,4); print(np.take(M,[0,2],axis=1))

# 21) Filtrar filas por condición de columna
M = np.array([[1,10],[2,20],[3,15]]); print(M[M[:,1] >= 15])

# 22) nan_to_num
v = np.array([1.0,np.nan,2.5]); print(np.nan_to_num(v, nan=0.0))

# 23) eye/diag
print(np.eye(4)); print(np.diag([10,20,30]))

# 24) unique con counts
v = np.array([1,2,2,3,3,3]); print(np.unique(v, return_counts=True))

# 25) column_stack
a = np.array([1,2,3]); b = np.array([10,20,30]); print(np.column_stack([a,b]))
