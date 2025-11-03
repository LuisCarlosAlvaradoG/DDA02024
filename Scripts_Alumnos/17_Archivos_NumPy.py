# 17.- ARCHIVOS: NUMPY — ARREGLOS, VECTORIZACIÓN, BROADCASTING, I/O

import numpy as np

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
print(v[3])
print(v[2:7])
print( v[:5], v[5:])

M = np.arange(12).reshape(3,4)
print(M)
print(M[1,2])
print(M[0:2,1:3])

# Vistas comparten memoria:
s = v[2:7]; s[:] = -1
print(v)  # también cambia v

# Copia explícita:
v_copy = v.copy(); v_copy[0]=999
print(v_copy, v)

# 3D básico (didáctico):
T = np.arange(24).reshape(2,3,4)  # (profundidad, filas, cols)
print(T.shape, T[1,:,2])

# ---------------------------------------------------------------
# D) VECTORIZACIÓN, UFUNCS Y BROADCASTING
# ---------------------------------------------------------------
x = np.array([1,2,3,4.])
y = np.array([10,20,30,40.])
print(x+y, x*y,  x**2)

# Broadcasting (3,1) + (3,) => (3,3)
col = np.array([[1],[2],[3]])
row = np.array([10,20,30])
print(col + row)

angles = np.linspace(0, np.pi, 5)
print(np.sin(angles))
print(np.exp([0,1,2]))

# ---------------------------------------------------------------
# E) AGREGACIONES Y ESTADÍSTICAS
# ---------------------------------------------------------------
A = np.arange(1,13).reshape(3,4)
print(A)
print(A.sum(), A.sum(axis=0), A.sum(axis=1))
print(A.mean(), A.std(), A.min(), A.max())
print(A.argmin(), A.argmax())

# ---------------------------------------------------------------
# F) MASKS, WHERE, UNIQUE, SET OPS
# ---------------------------------------------------------------
B = np.array([3,8,1,5,8,2,8])
mask = (B==8)
print(mask, B[mask])
print(np.where(B>3,1,0))
print(np.unique(B))

C = np.array([1,2,3,4,5])
D = np.array([4,5,6,7])
print(np.intersect1d(C,D))
print(np.union1d(C,D))
print(np.setdiff1d(C,D))

# ---------------------------------------------------------------
# G) RESHAPE, CONCAT, APILADO
# ---------------------------------------------------------------
X = np.arange(6).reshape(2,3)
Y = np.arange(6,12).reshape(2,3)
print(np.vstack([X,Y]))
print(np.hstack([X,Y]))
print(np.concatenate([X,Y], axis=1))

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
create_num_csv("np_basic.csv")
data = np.loadtxt("np_basic.csv", delimiter=",")
print("loaded shape:", data.shape, "| head:\n", data[:5])

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

print(minmax_scale(np.array([5,10,15,20])))
print(zscore_cols(np.arange(12).reshape(3,4)))
print(pairwise_dist_2d(np.array([[0,0],[1,0],[1,1]])))

# ---------------------------------------------------------------
# J) VENTAJAS / DESVENTAJAS / BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas: velocidad, vectorización, broadcasting, API numérica rica.
# Desventajas: arreglos homogéneos, faltantes menos cómodos que en pandas.
# Buenas prácticas: documentar shapes; evitar copias innecesarias; preferir ufuncs.