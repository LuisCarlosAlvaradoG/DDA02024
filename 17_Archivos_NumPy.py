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
# =============================================================================
# I) ALEATORIOS (Generator, semilla, permutaciones, muestreos)
# =============================================================================

# --- Reproducibilidad básica (semilla fija) ---
rng = np.random.default_rng(42)
print(rng.integers(0, 10, size=5))

# --- Enteros aleatorios ---
# low inclusivo, high exclusivo
nums = rng.integers(low=10, high=20, size=8, endpoint=False)
print(nums)

# --- Permutaciones / Mezclas ---
arr = np.arange(10)
perm = rng.permutation(arr)     # NO modifica arr
rng.shuffle(arr)                # Mezcla IN-PLACE
print("Permutation:", perm, "| Shuffled:", arr)

# --- Muestreo con/ sin reemplazo ---
poblacion = np.array(list("ABCDEFGHIJ"))
muestra_sin = rng.choice(poblacion, size=5, replace=False)
muestra_con = rng.choice(poblacion, size=5, replace=True)
print("Sin reemplazo:", muestra_sin, "| Con reemplazo:", muestra_con)

# --- Muestreo ponderado (probabilidades p deben sumar 1) ---
p = np.array([0.20, 0.10, 0.05, 0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10])
muestra_p = rng.choice(poblacion, size=6, replace=True, p=p)
print("Muestreo ponderado:", muestra_p)

# --- Barajar filas de una matriz (mantener columnas alineadas) ---
X = rng.normal(0, 1, size=(5, 3))
idx = rng.permutation(X.shape[0])
X_barajado = X[idx]
print("Índices de barajado:", idx)

# =============================================================================
# J) NUMPY — DISTRIBUCIONES (parámetros, ejemplos y usos típicos)
# =============================================================================

# -------------------------------
# UNIFORME
# -------------------------------
a, b = 2.0, 5.0
x_uniforme = rng.uniform(a, b, size=1000)
print("Uniforme ~ U[2,5]: media≈", x_uniforme.mean(), " var≈", x_uniforme.var())

# -------------------------------
# NORMAL (Gaussiana)
# -------------------------------
mu, sigma = 10.0, 2.5
x_normal = rng.normal(loc=mu, scale=sigma, size=2000)
print("Normal N(10,2.5^2): media≈", x_normal.mean(), " var≈", x_normal.var())

# Estandarizada (media 0, var 1)
z = rng.standard_normal(2000)

# -------------------------------
# LOGNORMAL (si Y~N(mu, sigma^2) entonces X=exp(Y)~LogNormal)
# -------------------------------
mu_l, sigma_l = 0.0, 0.5
x_logn = rng.lognormal(mean=mu_l, sigma=sigma_l, size=2000)
print("LogNormal: media≈", x_logn.mean(), " mediana≈", np.median(x_logn))

# -------------------------------
# EXPONENCIAL (lambda = 1/scale)
# -------------------------------
scale = 3.0              # media = 3.0
x_exp = rng.exponential(scale=scale, size=3000)
print("Exponencial(scale=3): media≈", x_exp.mean())

# -------------------------------
# GAMMA (shape=k, scale=θ) — suma de k exponenciales (si k entero)
# -------------------------------
k, theta = 2.0, 2.0
x_gamma = rng.gamma(shape=k, scale=theta, size=3000)
print("Gamma(k=2,θ=2): media teórica=kθ=4 -> empírica≈", x_gamma.mean())

# -------------------------------
# BETA (en [0,1]) — útil para proporciones
# -------------------------------
a, b = 2.0, 5.0
x_beta = rng.beta(a, b, size=5000)
print("Beta(2,5): media teórica=a/(a+b)=0.2857 -> empírica≈", x_beta.mean())

# -------------------------------
# CHI-CUADRADO (k grados de libertad)
# -------------------------------
k = 5
x_chi2 = rng.chisquare(df=k, size=4000)
print("Chi^2(df=5): media teórica=df=5 -> empírica≈", x_chi2.mean())

# -------------------------------
# t DE STUDENT (df grados de libertad)
# -------------------------------
df = 10
x_t = rng.standard_t(df=df, size=4000)
print("t-Student(df=10): media≈", x_t.mean())

# -------------------------------
# BINOMIAL (n ensayos, p éxito) — # éxitos
# -------------------------------
n, p = 20, 0.3
x_bin = rng.binomial(n=n, p=p, size=5000)
print("Binomial(n=20,p=0.3): media teórica=np=6 -> empírica≈", x_bin.mean())

# -------------------------------
# POISSON (lambda) — recuento de eventos por intervalo
# -------------------------------
lam = 4.0
x_poi = rng.poisson(lam=lam, size=5000)
print("Poisson(λ=4): media teórica=4 -> empírica≈", x_poi.mean())

# -------------------------------
# GEOMÉTRICA (p) — # ensayos hasta 1er éxito (soporte 1,2,3,...)
# -------------------------------
p = 0.2
x_geo = rng.geometric(p=p, size=5000)
print("Geométrica(p=0.2): media teórica=1/p=5 -> empírica≈", x_geo.mean())

# -------------------------------
# MULTINOMIAL (n, p) — vector de recuentos en k categorías
# -------------------------------
p = np.array([0.5, 0.3, 0.2])
x_multi = rng.multinomial(n=20, pvals=p, size=3)  # 3 repeticiones
print("Multinomial (3 corridas, suman 20 c/u):\n", x_multi, "\nSuma filas:", x_multi.sum(axis=1))

# -------------------------------
# PROB-UTILIDADES: UÁR y elección ponderada
# -------------------------------
# Escenario: asignar aleatoriamente “expertos” a tickets con pesos por prioridad
tickets = np.arange(8)
expertos = np.array(["Ana", "Luis", "Maya"])
pesos = np.array([0.6, 0.3, 0.1])  # Ana más probable

asignado = []
for _ in tickets:
    asignado.append(rng.choice(expertos, p=pesos))
asignado = np.array(asignado)
print("Asignación ponderada:", asignado)

# ---------------------------------------------------------------
# K) CASOS GUIADOS
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

# 1) SUPERMERCADO — REDONDEO Y TOTAL CON PROMO 3x2
# Contexto: En caja, el cliente pasa precios uno a uno. Cada 3er producto (el más barato del trío) es gratis (promo 3x2).
# Además, redondea el total a 2 decimales.
import numpy as np
precios = np.array([25.9, 10.0, 12.5, 40.0, 12.5, 12.5, 100.0, 30.0, 25.0])
total = 0.0
i = 0
while i < len(precios):
    grupo = precios[i:i+3]
    if len(grupo) == 3:
        total += grupo.sum() - np.min(grupo)  # 3x2: se descuenta el menor
    else:
        total += grupo.sum()
    i += 3
total = np.round(total, 2)
print("Total a pagar:", total)

# 2) FÁBRICA — CONTROL DE CALIDAD POR LOTES
# Contexto: Sensores registran diámetros. Aprobado si |x - target| <= tol. Reporta % de rechazo por lote.
import numpy as np
rng = np.random.default_rng(7)
target, tol = 10.0, 0.3
lotes = [rng.normal(target, 0.25, 50), rng.normal(target, 0.5, 60), rng.normal(target, 0.2, 40)]
for idx, lote in enumerate(lotes, start=1):
    fuera = np.where(np.abs(lote - target) > tol, 1, 0)
    rechazo = 100 * fuera.mean()
    print(f"Lote {idx}: rechazo = {rechazo:.1f}%")

# 3) CLÍNICA — TRIAGE POR TEMPERATURA
# Contexto: Toma de temperatura de pacientes. Clasifica: <37 normal, 37–38 observación, >38 fiebre. Cuenta por categoría.
import numpy as np
temps = np.array([36.8, 37.1, 39.0, 38.2, 36.5, 37.9, 38.0, 36.9, 39.5])
cats = np.where(temps > 38, 2, np.where(temps >= 37, 1, 0))  # 0 normal,1 observ,2 fiebre
# Conteo manual con ciclo
conteo = np.zeros(3, dtype=int)
for c in cats:
    conteo[c] += 1
print("Normal/Observación/Fiebre:", conteo.tolist())

# 4) INVENTARIO — REORDEN PUNTO MÍNIMO
# Contexto: Niveles diarios de stock. Si cae por debajo de s_min, genera orden de reposición Q fija.
import numpy as np
niveles = np.array([120, 100, 85, 60, 58, 130, 110, 90, 45, 40, 95])
s_min, Q = 70, 80
ordenes = []
stock = niveles[0]
for d in range(1, len(niveles)):
    stock = niveles[d]
    if stock < s_min:
        stock += Q
        ordenes.append((d, Q))
print("Órdenes (día, cantidad):", ordenes)

# 5) GIMNASIO — CÁLCULO DE KCAL POR SESIÓN
# Contexto: Serie de ejercicios con MET estimado y minutos realizados. Calcular kcal = MET * peso(kg) * minutos/60.
import numpy as np
peso = 90
METs = np.array([8.0, 6.0, 3.5])      # correr, pesas, estiramiento
mins = np.array([20, 40, 15])
kcal = (METs * peso * mins/60).sum()
print("Kcal totales:", round(kcal, 1))

# 6) TRANSPORTE — DISTRIBUCIÓN DE EDADES (HISTOGRAMA)
# Contexto: Edades de pasajeros en una semana. Construye histograma por rangos [0-18,19-30,31-50,51+].
import numpy as np
edades = np.array([16, 22, 34, 55, 42, 19, 28, 67, 14, 31, 51, 49, 23, 18, 60])
bins = np.array([0, 19, 31, 51, 200])
hist, _ = np.histogram(edades, bins=bins)
print("Pasajeros por rango [0-18,19-30,31-50,51+]:", hist.tolist())

# 7) HOSPITAL — PROMEDIOS Y OUTLIERS EN TIEMPOS DE ESPERA
# Contexto: Tiempos (min). Marca como outlier si > mu + 2*sd. Reemplaza outliers con el percentil 90.
import numpy as np
espera = np.array([15, 20, 22, 100, 18, 17, 19, 120, 21, 23, 16, 15])
mu, sd = espera.mean(), espera.std()
p90 = np.percentile(espera, 90)
limite = mu + 2*sd
ajustada = np.where(espera > limite, p90, espera)
print("Media original:", round(mu,2), " | Outliers:", np.sum(espera > limite))
print("Media ajustada:", round(ajustada.mean(),2))

# 8) E-COMMERCE — TASA DE DEVOLUCIONES POR CATEGORÍA
# Contexto: 1-devuelto/0-no, con categorías. Calcula tasa por categoría con loop sobre únicas.
import numpy as np
cats = np.array(['A','B','A','A','C','B','B','C','A','C','C','B'])
dev  = np.array([  0 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 0 ])
for c in np.unique(cats):
    tasa = dev[cats==c].mean()
    print(f"Cat {c}: tasa devoluciones = {tasa:.2f}")

# 9) PANADERÍA — DETECTAR RUPTURA DE STOCK POR DEMANDA
# Contexto: Demanda diaria y producción diaria. Detecta días con ruptura (demanda acumulada > prod acumulada).
import numpy as np
demanda = np.array([20, 25, 40, 30, 50, 60, 20])
prod    = np.array([30, 30, 35, 35, 35, 35, 35])
acum_d = np.cumsum(demanda)
acum_p = np.cumsum(prod)
ruptura = np.where(acum_d > acum_p, 1, 0)
dias_ruptura = [i for i, r in enumerate(ruptura) if r==1]
print("Días con ruptura:", dias_ruptura)

# 10) TELECOM — REDONDEO DE GB FACTURABLES
# Contexto: Se cobra por bloques de 0.5 GB hacia arriba (ceil). Calcular GB facturables por usuario.
import numpy as np
consumo_gb = np.array([1.01, 0.49, 2.25, 3.0, 0.5, 4.74])
bloque = 0.5
fact = np.ceil(consumo_gb / bloque) * bloque
print("GB facturables:", fact)

# 11) ENERGÍA — SUAVIZADO DE PRODUCCIÓN SOLAR
# Contexto: Producción horaria con nubes. Aplica media móvil 3 (con np.convolve). Reporta pico suavizado.
import numpy as np
prod = np.array([0, 2, 5, 9, 12, 10, 7, 5, 3, 1, 0])
kernel = np.ones(3)/3
suave = np.convolve(prod, kernel, mode='same')
print("Pico suavizado:", np.max(suave), " | Hora índice:", int(np.argmax(suave)))

# 12) ESTADIO — ASIGNACIÓN EN BLOQUES
# Contexto: N asientos vendidos consecutivos. Reacomoda en matriz de filas=secciones para visualizar huecos.
import numpy as np
N = 30
vendidos = np.zeros(N, dtype=int)
vendidos[[0,1,2,7,8,9, 15,16, 25,26,27]] = 1
M = vendidos.reshape(6,5)  # 6 secciones x 5 asientos
huecos_por_fila = (M==0).sum(axis=1)
print("Huecos por sección:", huecos_por_fila.tolist())

# 13) LABORATORIO — NORMALIZAR Y DETECTAR COLUMNA CONSTANTE
# Contexto: Medidas en columnas. Estandariza z-score; si sd=0, deja la columna en ceros.
import numpy as np
X = np.array([[5, 2, 9],
              [6, 2, 7],
              [7, 2, 9],
              [8, 2, 7]], dtype=float)
mu, sd = X.mean(axis=0), X.std(axis=0)
sd = np.where(sd==0, 1.0, sd)
Z = (X - mu) / sd
const_cols = [j for j, s in enumerate(sd) if s==1.0 and np.all(X[:,j]==X[0,j])]
print("Z-shape:", Z.shape, "| Columnas constantes:", const_cols)

# 14) METEOROLOGÍA — ALERTA POR LLUVIA EXTREMA
# Contexto: Lluvias diarias (mm). Alerta si día supera el percentil 95 de toda la serie.
import numpy as np
lluvia = np.array([0, 2, 0, 15, 0, 3, 70, 1, 0, 40, 0, 5, 0, 60])
p95 = np.percentile(lluvia, 95)
alertas = np.where(lluvia > p95, 1, 0)
for d, a in enumerate(alertas):
    if a==1:
        print(f"Alerta día {d}: {lluvia[d]} mm (> p95={p95:.1f})")

# 15) BANCO — DESGLOSE DE BILLETES
# Contexto: Cajero necesita desglosar un monto en billetes [1000,500,200,100,50,20]. Usa while y NumPy.
import numpy as np
monto = 12890
den = np.array([1000, 500, 200, 100, 50, 20])
res = np.zeros_like(den)
i = 0
while i < len(den):
    if monto >= den[i]:
        res[i] = monto // den[i]
        monto = monto % den[i]
    i += 1
print("Desglose [1000,500,200,100,50,20]:", res.tolist(), "| Remanente:", monto)

# =============================================================================
# PROB 1) DOS DADOS — SUMA MÍNIMA Y DOBLES
# =============================================================================
# Contexto:
# En un juego de mesa se lanzan 2 dados justos durante 100 rondas. 
# (a) Estima la probabilidad de que la suma sea >= 10.
# (b) Estima la probabilidad de obtener “dobles” (mismo número en ambos dados).
# Reporta ambas probabilidades simuladas y los conteos.
import numpy as np
rng = np.random.default_rng(2025)

N = 100  # número de rondas
d1 = rng.integers(1, 7, size=N)
d2 = rng.integers(1, 7, size=N)
suma = d1 + d2

# Conteos con ciclo + selectivas
cnt_ge10 = 0
cnt_dobles = 0
for i in range(N):
    if suma[i] >= 10:
        cnt_ge10 += 1
    if d1[i] == d2[i]:
        cnt_dobles += 1

p_ge10 = cnt_ge10 / N
p_dobles = cnt_dobles / N

print(f"[Dados] Rondas={N} | P(suma>=10)≈{p_ge10:.3f}  | P(dobles)≈{p_dobles:.3f}")

# =============================================================================
# PROB 2) URNA SIN REEMPLAZO — AL MENOS 2 ROJAS
# =============================================================================
# Contexto:
# Una urna tiene 8 bolas rojas y 12 azules (total 20). Se extraen 5 SIN reemplazo.
# Estima la probabilidad de obtener AL MENOS 2 rojas.
# Usa simulación con distribución hipergeométrica y valida con conteo en un loop.
import numpy as np
rng = np.random.default_rng(2025)

Nsim = 50_000
N = 20         # total
K = 8          # éxitos (rojas)
n = 5          # extracciones
# Muestras hipergeométricas: número de rojas en cada experimento
x = rng.hypergeometric(ngood=K, nbad=N-K, nsample=n, size=Nsim)

cnt_al_menos_2 = 0
for k in x:
    if k >= 2:
        cnt_al_menos_2 += 1

p_est = cnt_al_menos_2 / Nsim
print(f"[Urna] N={N}, K={K}, n={n} | P(X>=2)≈{p_est:.4f}  (sim {Nsim} corridas)")

# =============================================================================
# PROB 3) CALL CENTER — PROCESO DE POISSON POR HORA
# =============================================================================
# Contexto:
# En un call center llegan llamadas como un proceso de Poisson con tasa λ=12 por hora.
# Se simulan 8 horas de operación (una jornada).
# (a) Estima la probabilidad de que en alguna hora haya 20 o más llamadas.
# (b) Estima la probabilidad de que el total diario supere 100 llamadas.
# Se hace por simulación y con conteos en ciclos.
import numpy as np
rng = np.random.default_rng(2025)

lam = 12     # tasa por hora
horas = 8
Nsim = 20_000

# Genera matriz (Nsim x horas) con llamadas por hora
llamadas = rng.poisson(lam=lam, size=(Nsim, horas))

cnt_hora_20omas = 0
cnt_total_100mas = 0
for i in range(Nsim):
    hay_pico = False
    total = 0
    # ciclo por hora
    for h in range(horas):
        total += llamadas[i, h]
        if llamadas[i, h] >= 20:
            hay_pico = True
    if hay_pico:
        cnt_hora_20omas += 1
    if total > 100:
        cnt_total_100mas += 1

p_pico = cnt_hora_20omas / Nsim
p_total = cnt_total_100mas / Nsim
print(f"[Poisson] λ={lam}/h, {horas}h | P(≥20 en alguna hora)≈{p_pico:.4f} | P(total>100)≈{p_total:.4f}")
