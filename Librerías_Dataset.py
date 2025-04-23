import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leer el dataset
df = pd.read_csv("diabetes_dataset.csv")  # Asegúrate de tener el archivo con estas columnas

# Vista general
print("Primeras filas:\n", df.head())
print("\nInformación general:")
print(df.info())

# ===============================
# 🎯 ESTRUCTURAS SELECTIVAS
# ===============================
# Clasificar pacientes según su HbA1c en una nueva columna
def clasificar_hba1c(valor):
    if valor < 5.7:
        return "Normal"
    elif 5.7 <= valor < 6.5:
        return "Prediabetes"
    else:
        return "Diabetes"

df["HbA1c_clasificacion"] = df["hbA1c_level"].apply(clasificar_hba1c)

# Clasificar IMC manualmente
df["bmi_categoria"] = df["bmi"].apply(
    lambda x: "Bajo peso" if x < 18.5 else
              "Normal" if x < 25 else
              "Sobrepeso" if x < 30 else
              "Obesidad"
)

# ===============================
# 🔁 ESTRUCTURAS REPETITIVAS
# ===============================
# Calcular número total de diabéticos y no diabéticos con bucle for
conteo = {"diabéticos": 0, "no_diabéticos": 0}
for valor in df["diabetes"]:
    if valor == 1:
        conteo["diabéticos"] += 1
    else:
        conteo["no_diabéticos"] += 1

print("\nConteo manual con for:")
print(conteo)

# Bucle while para imprimir los primeros 5 registros manualmente
print("\nPrimeros 5 registros usando while:")
i = 0
while i < 5:
    print(df.iloc[i][["gender", "age", "bmi", "diabetes"]])
    i += 1

# ===============================
# 🧮 USO DE LISTAS Y LISTAS DE LISTAS
# ===============================
# Crear una lista de listas con [edad, glucosa] solo de pacientes diabéticos
lista_pacientes = []
for i in range(len(df)):
    if df.loc[i, "diabetes"] == 1:
        lista_pacientes.append([df.loc[i, "age"], df.loc[i, "blood_glucose_level"]])

print("\nEjemplo de lista de listas [edad, glucosa]:")
print(lista_pacientes[:3])  # Mostrar solo los 3 primeros

# ===============================
# 📊 VISUALIZACIÓN CON MATPLOTLIB
# ===============================

# Histograma de IMC por grupo
plt.figure(figsize=(10, 5))
plt.hist(df[df["diabetes"] == 1]["bmi"], bins=15, alpha=0.7, label="Diabéticos", color="darkred")
plt.hist(df[df["diabetes"] == 0]["bmi"], bins=15, alpha=0.7, label="No diabéticos", color="darkgreen")
plt.title("Distribución de IMC por diagnóstico")
plt.xlabel("IMC")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 🧠 ANÁLISIS CON NUMPY
# ===============================

# Convertir algunas columnas a matriz NumPy
valores = df[["age", "bmi", "blood_glucose_level"]].values

# Normalización simple
valores_normalizados = (valores - np.mean(valores, axis=0)) / np.std(valores, axis=0)

# Guardar como nuevo DataFrame
df_norm = pd.DataFrame(valores_normalizados, columns=["age_norm", "bmi_norm", "glucose_norm"])

# Concatenar con el DataFrame original
df = pd.concat([df, df_norm], axis=1)

# Promedios por grupo
promedios = df.groupby("diabetes")[["age_norm", "bmi_norm", "glucose_norm"]].mean()

# Gráfico de barras comparando promedios normalizados
promedios.T.plot(kind="bar", figsize=(10, 6))
plt.title("Promedios normalizados por diagnóstico")
plt.ylabel("Valor normalizado")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()
plt.show()


# ===============================
# 🔢 Estadísticas con NumPy y pandas
# ===============================
numericas = ["age", "bmi", "hbA1c_level", "blood_glucose_level"]

# Convertir a NumPy
matriz = df[numericas].values

medias = np.mean(matriz, axis=0)
desviaciones = np.std(matriz, axis=0)

print("\nMedia por columna:", dict(zip(numericas, medias)))
print("Desviación estándar:", dict(zip(numericas, desviaciones)))

# ===============================
# 🧼 Transformación con pandas
# ===============================

# Normalizar variables numéricas
for col in numericas:
    df[f"{col}_norm"] = (df[col] - df[col].mean()) / df[col].std()

# Clasificar riesgo de glucosa
df["glucose_risk"] = pd.cut(
    df["blood_glucose_level"],
    bins=[0, 99, 125, np.inf],
    labels=["Normal", "Prediabetes", "Diabetes"]
)

# Clasificar riesgo de IMC
df["bmi_risk"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 24.9, 29.9, np.inf],
    labels=["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]
)

print("\nRiesgo por glucosa:\n", df["glucose_risk"].value_counts())
print("\nRiesgo por IMC:\n", df["bmi_risk"].value_counts())

# ===============================
# 📊 Visualizaciones con matplotlib
# ===============================


# 🔹 Histograma de edad por grupo de diabetes
plt.figure(figsize=(10, 5))
plt.hist(df[df["diabetes"] == 1]["age"], bins=10, alpha=0.7, label="Diabéticos", color="crimson")
plt.hist(df[df["diabetes"] == 0]["age"], bins=10, alpha=0.7, label="No diabéticos", color="skyblue")
plt.title("Distribución de edad según diagnóstico")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 🔹 Scatter: glucosa vs. IMC (color por diagnóstico)
plt.figure(figsize=(8, 6))
plt.scatter(df["blood_glucose_level"], df["bmi"], c=df["diabetes"], cmap="bwr", alpha=0.7, edgecolor="k")
plt.xlabel("Glucosa en sangre")
plt.ylabel("IMC")
plt.title("Relación Glucosa - IMC")
plt.colorbar(label="0 = No diabético, 1 = Diabético")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🔹 Boxplot de hbA1c_level por diagnóstico
df.boxplot(column="hbA1c_level", by="diabetes", grid=False)
plt.title("HbA1c por grupo de diagnóstico")
plt.suptitle("")
plt.xlabel("Diabetes")
plt.ylabel("HbA1c (%)")
plt.tight_layout()
plt.show()

# 🔹 Gráfico de barras: promedio normalizado por grupo
cols_norm = ["age_norm", "bmi_norm", "hbA1c_level_norm", "blood_glucose_level_norm"]
promedios = df.groupby("diabetes")[cols_norm].mean().T

promedios.plot(kind="bar", figsize=(10, 6))
plt.title("Promedios normalizados por grupo de diagnóstico")
plt.ylabel("Valor normalizado")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
