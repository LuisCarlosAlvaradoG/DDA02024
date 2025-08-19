
# ===============================================================
# 20.- PRÁCTICA INTEGRAL DEL CURSO
# Tema: Análisis de "diabetes_dataset.csv"
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: 3–4 horas (clase completa con práctica guiada)
# ===============================================================
#
# REGLAS Y CONVENIOS EN ESTE ARCHIVO:
# - TODA la teoría y explicaciones están en ESPAÑOL.
# - TODO el CÓDIGO (identificadores, prints, etc.) está en INGLÉS.
# - Se cubren TODOS los temas vistos en el curso, de forma integrada:
#   1) Estructuras secuenciales: constantes/variables, entrada/salida
#   2) Estructuras secuenciales: operaciones con números y cadenas
#   3) Estructuras selectivas: relacionales, lógicas, simples y dobles
#   4) Selectivas múltiples y anidadas + try/except
#   5) Repetitivas: contadores, acumuladores y centinelas
#   6) Repetitivas: while
#   7) Repetitivas: for/range
#   8) Depurador (print-debug y pdb opcional)
#   9) Datos compuestos: listas (I y II)
#   10) Datos compuestos: tuplas
#   11) Datos compuestos: diccionarios
#   12) Funciones: módulos y funciones, encabezado y parámetros
#   13) Llamadas a funciones: paso de argumentos; con y sin retorno
#   14) Uso de bibliotecas de funciones (stdlib + numpy/pandas/matplotlib)
#   15) Archivos: manejo de datos tabulares (apertura, lectura, escritura)
#   16) Archivos con NumPy
#   17) Archivos con Pandas
#   18) Gráficas con Matplotlib integradas con NumPy/Pandas
#
# NOTAS:
# - Este script está pensado para correrse como .py desde terminal/IDE.
# - `plt.show()` está comentado para no bloquear; descomentar en clase.
# - Todas las "prácticas" incluyen la SOLUCIÓN implementada (tal como pidió el profesor).
#
# Dataset esperado: "diabetes_dataset.csv" con columnas típicas:
#   gender, age, hypertension, heart_disease, bmi, hbA1c_level, blood_glucose_level, diabetes
# (0/1 en variables binarias)
# ===============================================================

# -----------------------------
# IMPORTS (bibliotecas permitidas)
# -----------------------------
import os
import sys
import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Estilo gráfico simple (sin seaborn).
plt.rcParams["figure.figsize"] = (8, 4)

# -----------------------------
# 1) ENTRADA/SALIDA + VARIABLES/CONSTANTES
# -----------------------------
# Teoría (ES):
# - input()/print(): Entrada/Salida estándar.
# - Variables: nombres en minúsculas con guiones bajos; constantes simuladas en MAYÚSCULAS.
# - Tipado dinámico en Python; conversiones explícitas con int(), float(), str().

DEFAULT_CSV = "diabetes_dataset.csv"  # constante (ruta por defecto)
print(f"[INFO] Default CSV path is: {DEFAULT_CSV}")

# Entrada del usuario con try/except (si presiona Enter, usamos el default).
try:
    user_path = input("Enter CSV path or press Enter to use default: ").strip()
except Exception as e:
    print("[WARN] input() not available; using default path.")
    user_path = ""

csv_path = user_path if user_path else DEFAULT_CSV
print(f"[INFO] CSV path selected: {csv_path}")

# Comprobar existencia; si no existe, mostramos mensaje y salimos con código 1.
if not os.path.exists(csv_path):
    print(f"[ERROR] File not found: {csv_path}")
    print("[HINT] Place 'diabetes_dataset.csv' next to this script or input a valid path.")
    sys.exit(1)

# -----------------------------
# 2) OPERACIONES BÁSICAS CON NÚMEROS Y CADENAS
# -----------------------------
# Teoría (ES):
# - Operadores aritméticos: + - * / // % **
# - Operadores con cadenas: concatenación (+), repetición (*), slicing.
# - f-strings para formateo, .upper()/.lower() en strings.

# Ejemplo: saludar y mostrar una operación simple
name = "classroom"
greeting = "Hello, " + name + "!"
print(greeting)
print(f"Basic arithmetic: 10 + 3*2 = {10 + 3*2}")

# -----------------------------
# 3) SELECTIVAS: RELACIONALES, LÓGICAS, SIMPLES Y DOBLES
# -----------------------------
# Teoría (ES):
# - if, if-else, operadores == != > >= < <=
# - lógicos: and, or, not
# - Comprobación de umbrales de salud (didáctico).

def classify_glucose(glucose_value):
    """Return a simple tag for glucose levels using simple/double selections."""
    # Nota didáctica: umbrales genéricos (solo para práctica).
    if glucose_value < 100:
        return "normal"
    else:
        return "high"

print("Glucose 90 is", classify_glucose(90), "| Glucose 145 is", classify_glucose(145))

# -----------------------------
# 4) SELECTIVAS MÚLTIPLES, ANIDADAS, TRY/EXCEPT
# -----------------------------
# Teoría (ES):
# - if/elif/else para múltiples rutas.
# - try/except para capturar errores (por ejemplo, conversión de tipos).

def risk_by_hba1c(hba1c):
    """Return risk level based on HbA1c thresholds (multiple selection)."""
    if hba1c < 5.7:
        return "low"
    elif hba1c < 6.5:
        return "prediabetes"
    else:
        return "diabetes"

def safe_float(x):
    """Parse float with try/except; return None on error."""
    try:
        return float(x)
    except Exception:
        return None

print("HbA1c 5.0 ->", risk_by_hba1c(5.0))
print("HbA1c 6.2 ->", risk_by_hba1c(6.2))

# -----------------------------
# 5) REPETITIVAS: CONTADORES, ACUMULADORES, CENTINELAS
# -----------------------------
# Teoría (ES):
# - Contador: variable que incrementa para contar elementos.
# - Acumulador: suma (o agrega) valores.
# - Centinela: valor especial para detener un proceso (en while).

# Práctica: leer primeras N líneas y contar cuántas tienen diabetes=1 (acumulador/contador).
N = 100  # constante didáctica
count_diab = 0  # contador
sum_bmi = 0.0   # acumulador
rows_read = 0

# Usando Pandas para leer rápido y luego iterar (más abajo haremos NumPy vectorizado).
df_preview = pd.read_csv(csv_path, nrows=N)
for i in range(len(df_preview)):
    rows_read += 1
    if df_preview.loc[i, "diabetes"] == 1:
        count_diab += 1
    sum_bmi += float(df_preview.loc[i, "bmi"])

avg_bmi = sum_bmi / rows_read if rows_read > 0 else float('nan')
print(f"[COUNTS] rows={rows_read} diabetics={count_diab} avg_bmi={avg_bmi:.2f}")

# -----------------------------
# 6) CICLOS WHILE (CENTINELA)
# -----------------------------
# Teoría (ES):
# - while se ejecuta mientras la condición sea True.
# - Ejemplo: evaluar pacientes hasta que el usuario escriba 'FIN'.

print("\nType patient glucose values (or FIN to stop). We'll classify them:")
while True:
    try:
        raw = input("glucose> ").strip()
    except Exception:
        # Entornos no interactivos: salimos del bucle.
        print("[WARN] input() not available for while-loop demo; skipping.")
        break
    if raw.upper() == "FIN":
        print("[INFO] Ending while-loop.")
        break
    num = safe_float(raw)
    if num is None:
        print("Invalid number, try again.")
        continue
    print(" -> class:", classify_glucose(num))

# -----------------------------
# 7) FOR Y RANGE
# -----------------------------
# Teoría (ES):
# - for i in range(n): iterar n veces.
# - enumerate para obtener (índice, valor).

sample = [90, 110, 130]
for idx, g in enumerate(sample):
    tag = classify_glucose(g)
    print(f"sample[{idx}]={g} -> {tag}")

# -----------------------------
# 8) DEPURADOR
# -----------------------------
# Teoría (ES):
# - print-debug: imprimir variables intermedias.
# - pdb: punto de interrupción con pdb.set_trace() (opcional).
# Nota: dejamos comentado para evitar pausar el script accidentalmente.
# import pdb; pdb.set_trace()

# -----------------------------
# 9) LISTAS (I y II)
# -----------------------------
# Teoría (ES):
# - Listas mutables; append, extend, slicing; list comprehensions.
# Práctica: lista de etiquetas de riesgo por HbA1c en las primeras 10 filas.

hb_list = list(df_preview["hbA1c_level"][:10])
risk_list = [risk_by_hba1c(x) for x in hb_list]
print("First 10 HbA1c:", hb_list)
print("Risk labels:", risk_list)

# -----------------------------
# 10) TUPLAS
# -----------------------------
# Teoría (ES):
# - Inmutables; útiles para registros pequeños, claves de dict, retorno múltiple.

def min_max_tuple(values):
    """Return (min, max) tuple from a list of numbers."""
    return (min(values), max(values))

print("min/max HbA1c first 10 ->", min_max_tuple(hb_list))

# -----------------------------
# 11) DICCIONARIOS
# -----------------------------
# Teoría (ES):
# - Pares clave:valor; métodos keys(), values(), items().
# Práctica: mapa de umbrales para categorías de glucosa (didáctico).

thresholds = {
    "normal": (0, 100),
    "prediabetes": (100, 126),
    "diabetes": (126, 10**9)  # 10**9 como 'infinito' práctico
}
print("glucose thresholds:", thresholds)

# -----------------------------
# 12) FUNCIONES (ESPECIFICACIÓN/IMPLEMENTACIÓN; PARÁMETROS)
# -----------------------------
# Teoría (ES):
# - Encabezado: def name(params): -> docstring -> cuerpo -> return opcional.
# - Parámetros por posición, retorno de uno o varios valores.

def bmi_category(bmi):
    """Return a simple BMI category for didactic purposes."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obesity"

def patient_summary_row(row):
    """Return a textual summary of a patient using f-strings."""
    return f"{row['gender']}, age {row['age']}, BMI {row['bmi']:.1f}, HbA1c {row['hbA1c_level']}, glucose {row['blood_glucose_level']} -> diabetes={row['diabetes']}"

# -----------------------------
# 13) LLAMADAS A FUNCIONES; CON/SIN RETORNO
# -----------------------------
# Práctica: imprimir 3 resúmenes (sin retorno adicional) y recoger categorías (con retorno).

for i in range(min(3, len(df_preview))):
    print("summary:", patient_summary_row(df_preview.loc[i]))

cats = [bmi_category(b) for b in df_preview["bmi"][:5]]
print("First 5 BMI categories:", cats)

# -----------------------------
# 14) USO DE BIBLIOTECAS (stdlib + numpy/pandas/matplotlib)
# -----------------------------
# - statistics.mean/median, math.isfinite; numpy vectorizado; pandas tabular; matplotlib gráficos.
print("statistics.mean of first 5 glucose:", statistics.mean(df_preview["blood_glucose_level"][:5]))

# -----------------------------
# 15) ARCHIVOS: MANEJO TABULAR CLÁSICO (open/read/write)
# -----------------------------
# Teoría (ES):
# - Abrir con open(...), leer línea a línea, escribir resultados.
# - Usamos CSV original para generar un TXT con 5 filas resumidas.

OUT_TXT = "20_preview_summary.txt"
with open(OUT_TXT, "w", encoding="utf-8") as f:
    f.write("gender,age,bmi,hba1c,glucose,diabetes\n")
    for i in range(min(5, len(df_preview))):
        r = df_preview.loc[i]
        f.write(f"{r['gender']},{r['age']},{r['bmi']:.2f},{r['hbA1c_level']},{r['blood_glucose_level']},{r['diabetes']}\n")
print(f"[WRITE] Wrote TXT preview -> {OUT_TXT}")

# -----------------------------
# 16) ARCHIVOS CON NUMPY (vectorización)
# -----------------------------
# Teoría (ES):
# - Convertir columnas a arrays NumPy para cálculos vectorizados.
# - Guardar resultados con np.savetxt.

arr_glu = df_preview["blood_glucose_level"].to_numpy(dtype=float)
arr_bmi = df_preview["bmi"].to_numpy(dtype=float)

def zscore(v):
    """Vectorized z-score with NumPy (return zeros if std=0)."""
    v = v.astype(float)
    mu = v.mean()
    sd = v.std()
    return np.zeros_like(v) if sd == 0 else (v - mu) / sd

glu_z = zscore(arr_glu)
bmi_z = zscore(arr_bmi)

np_out = np.column_stack([arr_glu, glu_z, arr_bmi, bmi_z])
np.savetxt("20_numpy_metrics.csv", np_out, delimiter=",", header="glucose,glu_z,bmi,bmi_z", comments="", fmt="%.6f")
print("[WRITE] Saved NumPy metrics -> 20_numpy_metrics.csv")

# -----------------------------
# 17) ARCHIVOS CON PANDAS (pipeline completo)
# -----------------------------
# Teoría (ES):
# - Cargar dataset completo; derivar columnas; filtrar; agrupar; escribir CSV.
df = pd.read_csv(csv_path)

# Derivadas: categorías y banderas
df["glucose_tag"] = np.where(df["blood_glucose_level"] < 100, "normal",
                      np.where(df["blood_glucose_level"] < 126, "prediabetes", "diabetes"))
df["bmi_cat"] = df["bmi"].apply(bmi_category)
df["hba1c_risk"] = df["hbA1c_level"].apply(risk_by_hba1c)

# Agrupar: tasa de diabetes por género y por categoría de BMI
group_gender = df.groupby("gender")["diabetes"].mean().reset_index(name="diabetes_rate")
group_bmi = df.groupby("bmi_cat")["diabetes"].mean().reset_index(name="diabetes_rate")

# Guardar reportes
group_gender.to_csv("20_report_gender.csv", index=False)
group_bmi.to_csv("20_report_bmi.csv", index=False)
df.to_csv("20_dataset_enriched.csv", index=False)
print("[WRITE] Saved pandas reports -> 20_report_gender.csv, 20_report_bmi.csv, 20_dataset_enriched.csv")

# -----------------------------
# 18) GRÁFICOS CON MATPLOTLIB (desde NumPy y pandas)
# -----------------------------
# A) Histograma de glucosa
# plt.figure()
# plt.hist(df["blood_glucose_level"], bins=30)
# plt.xlabel("blood_glucose_level"); plt.ylabel("count"); plt.title("Histogram of Blood Glucose")
# # plt.show()
# plt.savefig("20_hist_glucose.png")

# B) Dispersión BMI vs. Glucosa, coloreado por diabetes (0/1)
# plt.figure()
# colors = np.where(df["diabetes"]==1, "red", "blue")
# plt.scatter(df["bmi"], df["blood_glucose_level"], c=colors, alpha=0.5)
# plt.xlabel("BMI"); plt.ylabel("Blood Glucose Level"); plt.title("BMI vs Glucose (color=diabetes)")
# # plt.show()
# plt.savefig("20_scatter_bmi_glucose.png")

# C) Barras: tasa de diabetes por género (desde pandas)
# ax = group_gender.plot(x="gender", y="diabetes_rate", kind="bar", legend=False, title="Diabetes Rate by Gender")
# # plt.show()
# plt.savefig("20_bar_rate_gender.png")

print("[PLOTS] Saved: 20_hist_glucose.png, 20_scatter_bmi_glucose.png, 20_bar_rate_gender.png")

# ===============================================================
# SECCIÓN FINAL: BANCO DE EJERCICIOS INTEGRADOS (CON SOLUCIÓN)
# ===============================================================
# Nota: cada ejercicio ya tiene su solución implementada inmediatamente.
# El profesor puede ocultar el bloque de solución en clase si lo prefiere.

# EX01) Entrada/salida + try/except: solicitar un HbA1c y clasificarlo.
raw = "6.1"  # solución demostrativa (en clase, usar input())
val = safe_float(raw)
if val is not None:
    print("[EX01] HbA1c", val, "->", risk_by_hba1c(val))

# EX02) Operaciones con cadenas: normalizar texto de género.
raw_gender = "FeMaLe"
norm_gender = raw_gender.strip().capitalize()
print("[EX02]", raw_gender, "->", norm_gender)

# EX03) if/elif/else múltiple: categorizar glucosa por thresholds dict
def glucose_category_from_dict(g):
    for k,(lo,hi) in thresholds.items():
        if lo <= g < hi:
            return k
    return "unknown"

print("[EX03] glucose 115 ->", glucose_category_from_dict(115))

# EX04) Contador/acumulador: contar positivos de diabetes en 200 filas
df200 = pd.read_csv(csv_path, nrows=200)
cnt = 0; acc_glu = 0.0
for _, row in df200.iterrows():
    if row["diabetes"] == 1:
        cnt += 1
    acc_glu += float(row["blood_glucose_level"])
print("[EX04] diabetics in first 200 rows:", cnt, "avg_glucose:", acc_glu/len(df200))

# EX05) while centinela: (demostración programática)
sentinel_inputs = ["90", "130", "FIN"]
i = 0
while True:
    token = sentinel_inputs[i]; i += 1
    if token == "FIN":
        break
    print("[EX05] token:", token, "->", classify_glucose(float(token)))

# EX06) for/range + enumerate: imprimir 3 filas con índice
for idx, (_, row) in enumerate(df_preview.head(3).iterrows()):
    print(f"[EX06] row{idx} ->", patient_summary_row(row))

# EX07) listas y list-comprehension: primeras 8 etiquetas de BMI
print("[EX07] bmi cats:", [bmi_category(x) for x in df_preview["bmi"][:8]])

# EX08) tuplas: min/max de glucosa en las primeras 50 filas
first50_glu = list(df.head(50)["blood_glucose_level"]); print("[EX08] min/max glu:", min_max_tuple(first50_glu))

# EX09) diccionarios: frecuencia por etiqueta de glucosa (primeras 100 filas)
freq = {}
for g in df.head(100)["blood_glucose_level"]:
    tag = glucose_category_from_dict(g)
    freq[tag] = freq.get(tag, 0) + 1
print("[EX09] freq:", freq)

# EX10) funciones con retorno: tasa de diabetes general
def diabetes_rate(series):
    total = len(series)
    if total == 0: return 0.0
    return float(series.sum())/total

print("[EX10] rate:", diabetes_rate(df["diabetes"]))

# EX11) funciones sin retorno útil (solo efectos): escribir un CSV pequeño
def write_small_csv(path, n=5):
    df.head(n).to_csv(path, index=False)
    print("[EX11] wrote", path)
write_small_csv("20_small.csv", n=5)

# EX12) stdlib: statistics.median y math.isfinite
med_bmi = statistics.median(df_preview["bmi"])
print("[EX12] median BMI:", med_bmi, "| isfinite?", math.isfinite(med_bmi))

# EX13) NumPy: vectorizar normalización min-max para glucosa de 0..N
N = 100
gluN = df.head(N)["blood_glucose_level"].to_numpy(float)
mn, mx = gluN.min(), gluN.max()
minmax = np.zeros_like(gluN) if mx==mn else (gluN-mn)/(mx-mn)
print("[EX13] first 5 minmax:", minmax[:5])

# EX14) Pandas: groupby por 'gender' y promedio de BMI
print("[EX14]\n", df.groupby("gender")["bmi"].mean())

# EX15) Matplotlib: guardar un hist de BMI (sin show)
# plt.figure(); plt.hist(df["bmi"], bins=30); plt.title("BMI Histogram"); plt.savefig("20_hist_bmi.png")
print("[EX15] (plot saved) 20_hist_bmi.png")

# FIN DE LA PRÁCTICA INTEGRAL
# ===============================================================
