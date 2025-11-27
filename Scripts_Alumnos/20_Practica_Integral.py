"""
==========================================================
PRÁCTICA INTEGRADORA: NumPy, pandas y matplotlib
==========================================================

Dataset: diabetes_dataset.csv

Columnas:
- gender               (object: 'Male', 'Female', 'Other')
- age                  (float)
- hypertension         (int: 0 = no, 1 = sí)
- heart_disease        (int: 0 = no, 1 = sí)
- bmi                  (float)
- hbA1c_level          (float)
- blood_glucose_level  (int)
- diabetes             (int: 0 = no, 1 = sí)

Objetivo general:
-----------------
Usar NumPy, pandas y matplotlib para explorar el dataset,
calcular estadísticas básicas, crear nuevas variables y
visualizar patrones relacionados con la diabetes.

Instrucciones generales:
------------------------
- Responde cada ejercicio en el espacio marcado con "TU CÓDIGO AQUÍ".
- No modifiques el nombre de las variables que se indican en cada punto.
- Al final, guarda el archivo como: practica_diabetes_tuNombre.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Para que los gráficos se vean con mejor tipografía (opcional)
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["axes.grid"] = True

# ==========================================================
# EJERCICIO 0. Carga de datos
# ==========================================================
# a) Carga el archivo "diabetes_dataset.csv" en un DataFrame llamado df.
# b) Muestra las primeras 5 filas.
# c) Muestra información general del DataFrame (df.info()).
# d) Imprime el número de filas y columnas (shape).

# === TU CÓDIGO AQUÍ ===
df = pd.read_csv("diabetes_dataset.csv")
print(df.head()) #df.tail()
print(df.info())
print(df.shape)

# ==========================================================
# EJERCICIO 1. Exploración básica con pandas
# ==========================================================
# a) Calcula la estadística descriptiva (describe) de las columnas numéricas.
# b) Obtén la distribución de la variable 'diabetes' (value_counts y proporciones).
# c) Obtén la distribución de la variable 'gender' (value_counts).

# === TU CÓDIGO AQUÍ ===
desc = df.describe()
print(desc)
dist_diabetes = df["diabetes"].value_counts()
print(dist_diabetes)
dist_diabetes_prop = df["diabetes"].value_counts() / len(df) 
print(dist_diabetes_prop)
dist_diabetes_prop = df["diabetes"].value_counts(normalize=True)
print(dist_diabetes_prop)

dist_gender = df["gender"].value_counts()
print(dist_gender)
# ==========================================================
# EJERCICIO 2. Trabajo con NumPy y máscaras booleanas
# ==========================================================
# a) Extrae la columna 'age' como un arreglo de NumPy 'age_np'.
# b) Calcula la media, desviación estándar y mediana de la edad usando NumPy.
# c) Crea una máscara booleana 'mask_diab' para los pacientes con diabetes (diabetes == 1).
# d) Usando la máscara, calcula:
#    - La media de edad de pacientes con diabetes.
#    - La media de edad de pacientes sin diabetes.

# === TU CÓDIGO AQUÍ ===


# ==========================================================
# EJERCICIO 3. Índice de riesgo con NumPy (feature engineering)
# ==========================================================
# Supón que queremos construir un indicador sencillo de "riesgo" de diabetes
# combinando tres variables numéricas:
# - bmi
# - hbA1c_level
# - blood_glucose_level
#
# a) Normaliza cada una de estas columnas restando la media y dividiendo entre la desviación estándar.
#    (usa NumPy: (x - x.mean()) / x.std())
# b) Crea un nuevo arreglo llamado 'risk_index_np' definiendo:
#    risk_index = 0.4 * bmi_norm + 0.3 * hbA1c_norm + 0.3 * glucose_norm
# c) Agrega este índice al DataFrame como columna 'risk_index'.

# === TU CÓDIGO AQUÍ ===
bmi = df["bmi"].to_numpy()
hb = df["hbA1c_level"].to_numpy()
glu = df["blood_glucose_level"].to_numpy()
bmi_norm = (bmi - bmi.mean()) / bmi.std()
hb_norm = (hb - hb.mean()) / hb.std()
glu_norm = (glu - glu.mean()) / glu.std()
risk_index_np = 0.4 * bmi_norm + 0.3 * hb_norm + 0.3 * glu_norm
df["risk_index"] = risk_index_np

# ==========================================================
# EJERCICIO 4. Agrupaciones con pandas (groupby)
# ==========================================================
# a) Calcula la tasa de diabetes (promedio de la columna 'diabetes') por 'gender'.
# b) Calcula, por género, la media de 'age', 'bmi' y 'risk_index'.
# c) Ordena los resultados anteriores de mayor a menor tasa de diabetes.

# === TU CÓDIGO AQUÍ ===
tasa_diabetes_gender = df.groupby("gender")["diabetes"].mean().sort_values(ascending=False)
print(tasa_diabetes_gender)
stats_gender = df.groupby("gender")[["age","bmi","risk_index"]].mean().sort_values(by="age",ascending=False)
print(stats_gender)

# ==========================================================
# EJERCICIO 5. Tablas de contingencia (crosstab)
# ==========================================================
# a) Construye una tabla de contingencia entre 'hypertension' y 'diabetes'.
# b) Construye otra tabla de contingencia normalizada por filas para obtener
#    las proporciones de diabéticos dentro de cada categoría de 'hypertension'.

# === TU CÓDIGO AQUÍ ===
tab_htn = pd.crosstab(df["hypertension"], df["diabetes"])
print(tab_htn)
tab_htn_prop = pd.crosstab(df["hypertension"], df["diabetes"], normalize="columns")
print(tab_htn_prop)

# ==========================================================
# EJERCICIO 6. Visualización 1: Histogramas
# ==========================================================
# a) Grafica un histograma de la variable 'age'.
# b) Grafica un histograma de la variable 'bmi' solamente para pacientes con diabetes.
# c) Grafica un histograma de 'bmi' para pacientes sin diabetes.
#    (Puedes superponer ambas distribuciones o hacer 2 gráficos separados.)

# === TU CÓDIGO AQUÍ ===
plt.figure()
plt.hist(df["age"], bins = 20)
plt.title("Histograma de edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

plt.figure()
# plt.hist(df.loc[df["diabetes"] == 1, "bmi"], bins = 20)
plt.hist(df[df["diabetes"] == 1].loc[:,"bmi"], bins = 20)
plt.title("Histograma de bmi")
plt.xlabel("BMI")
plt.ylabel("Frecuencia")
plt.show()

plt.figure()
plt.hist(df[df["diabetes"] == 0].loc[:,"bmi"], bins = 20, label = "Pacientes sin diabetes")
plt.hist(df[df["diabetes"] == 1].loc[:,"bmi"], bins = 20, label = "Pacientes con diabetes")
plt.title("Histograma de BMI")
plt.xlabel("BMI")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()

# Subplots
fig, ax = plt.subplots(1,2, figsize=(12,5))
ax[0].hist(df[df["diabetes"] == 0].loc[:,"bmi"], bins = 20, label = "Pacientes sin diabetes")
ax[0].set_title("BMI sin diabetes")
ax[0].set_xlabel("BMI")
ax[0].set_ylabel("Frecuencia")
ax[1].hist(df[df["diabetes"] == 1].loc[:,"bmi"], bins = 20, label = "Pacientes con diabetes")
ax[1].set_title("BMI con diabetes")
ax[1].set_xlabel("BMI")
ax[1].set_ylabel("Frecuencia")
fig.suptitle("Distribución BMI")
plt.show()
# ==========================================================
# EJERCICIO 7. Visualización 2: Boxplots
# ==========================================================
# a) Crea un boxplot de 'blood_glucose_level' separado por 'diabetes'
#    (0 y 1 en el eje x).
# b) Interpreta visualmente si hay diferencia en los niveles de glucosa
#    entre pacientes con y sin diabetes.

# === TU CÓDIGO AQUÍ ===
data_no_diab = df[df["diabetes"] == 0].loc[:,"blood_glucose_level"]
data_diab = df[df["diabetes"] == 1].loc[:,"blood_glucose_level"]

plt.figure()
plt.boxplot([data_no_diab, data_diab], labels = ["No diabetes", "Diabetes"])
plt.title("Boxplot de nivel de glucosa en la sangre según su estado de diabetes")
plt.ylabel("blood_glucose_level")
plt.show()


# ==========================================================
# EJERCICIO 8. Visualización 3: Dispersión (scatter plot)
# ==========================================================
# a) Crea un scatter plot de 'age' (eje x) vs 'blood_glucose_level' (eje y).
# b) Colorea los puntos según la variable 'diabetes' (0 ó 1).
#    Pista: puedes usar un arreglo de colores con NumPy.

# === TU CÓDIGO AQUÍ ===
x = df["age"].to_numpy()
y = df["blood_glucose_level"].to_numpy()
diab = df["diabetes"].to_numpy()

colores = np.where(diab == 1, "gold", "cyan")

plt.figure()
plt.scatter(x, y, c = colores, alpha=0.5)
plt.title("Edad vs Nivel de glucosa en la sangre")
plt.xlabel("Edad")
plt.ylabel("Nivel de glucosa")
# plt.legend()
plt.show()


# ==========================================================
# EJERCICIO 9. Mini proyecto integrador
# ==========================================================
# Objetivo:
# Crear un pequeño análisis que responda la pregunta:
#   "¿Quiénes parecen tener mayor riesgo de diabetes en este dataset?"
#
# a) Elige un subconjunto del DataFrame filtrando por:
#    - edad mayor o igual a 40 años
#    - y/o presencia de hipertensión o enfermedad cardíaca
# b) Calcula para ese subconjunto:
#    - tasa de diabetes
#    - media de risk_index
# c) Compáralo contra la población general.
# d) Genera al menos una gráfica (a tu elección) para ilustrar la comparación.
#
# Puedes usar todas las herramientas anteriores (NumPy, pandas, matplotlib).

# === TU CÓDIGO AQUÍ ===
filtro = (df["age"] >= 40) | (df["hypertension"] == 1) | (df["heart_disease"] == 1)
df_sub = df[filtro]
tasa_diab_sub = df_sub["diabetes"].mean()
tasa_diab_total = df["diabetes"].mean()
print(f"Tasa de diabetes - subconjunto: {tasa_diab_sub}")
print(f"Tasa de diabetes - total: {tasa_diab_total}")

mean_risk_sub = df_sub["risk_index"].mean()
mean_risk_total = df["risk_index"].mean()
print(f"Risk index - subconjunto: {mean_risk_sub}")
print(f"Risk index - total: {mean_risk_total}")

plt.figure()
plt.bar(["Total", "Subconjunto"], [tasa_diab_total, tasa_diab_sub])
plt.title("Comparación de tasa de diabetes")
plt.ylabel("Proporción con diabetes")
plt.show()

import numpy as np
Equipos = ["Ame", "Rosario", "Cam", "Derek", "Matteo", "Sergio", "Matias", "Leo"]
np.random.choice(Equipos, size = 8, replace=False)