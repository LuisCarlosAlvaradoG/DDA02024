
# ===============================================================
# 18.- ARCHIVOS: PANDAS — BASES + INTEGRACIÓN CON NUMPY
# ===============================================================

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# A) OBJETIVOS
# ---------------------------------------------------------------
# - Manejar tablas con DataFrame y Series.
# - Cargar/guardar CSV con control de tipos y NA.
# - Transformar, agrupar y combinar datos.
# - Interoperar con NumPy en operaciones numéricas.

# ---------------------------------------------------------------
# B) SERIES Y DATAFRAMES
# ---------------------------------------------------------------
s = pd.Series([10, 20, 30], index = ["a", "b", "c"]) # Estructura básica
print(s)

df = pd.DataFrame({
     "id" : [1, 2, 3],
     "nombre" : ["Alina", "Beto", "Adri"],
     "edad" : [19, 19, 18]
    })
print(df)

# Asignar nombres a las filas
df.index = ["fila1", "fila2", "fila3"] # Tratar de no cambiar los nombres de las filas
print(df)

# Acceder a elementos del DataFrame de la columna edad
df.edad
df["edad"]
df.loc[:, "edad"] # Con .loc hacemos referencia a las columnas/filas por su nombre
df.iloc[:, 2] # Con .iloc hacemos referencia a las columnas/filas por su indice

df.iloc[1 , 1:] # Beto 19
df.loc["fila2", ["nombre", "edad"]] # Beto 19

df.loc[:, "nombre"]

# ---------------------------------------------------------------
# C) READ/WRITE CSV (DATASETS PRE-CARGADOS)
# ---------------------------------------------------------------
def create_students_csv(path):
    rows = [
        "id,name,age,math,prog,city",
        "1,Ana,21,88,92,",
        "2,Luis,19,75,81,Monterrey",
        "3,Marta,22,95,89,Guadalajara",
        "4,Juan,20,62,70,CDMX",
        "5,Lia,21,70,85,Guadalajara"
    ]
    with open(path, "w", encoding="utf-8") as f:
        for r in rows: f.write(r+"\n")

create_students_csv("students.csv")
df = pd.read_csv("students.csv") # Para leer un excel tipo csv ya existente
df.head(2)

df.to_csv("students_out.csv", index= False) # Guardar de DataFrame a Excel

# ---------------------------------------------------------------
# D) SELECCIÓN, FILTRADO, ASIGNACIÓN; NA/ASTYPE
# ---------------------------------------------------------------
df["promedio"] = (df["math"] + df["prog"]) / 2
# Mover la columna promedio a la posición 3
cols = df.columns.tolist()
cols.insert(3, cols.pop(cols.index("promedio"))) # Petición de Uriel
df = df[cols]
df

df["status"] = np.where(df["promedio"] >= 80, "OK", np.where(df["promedio"] < 60, "REPROBADO", "MEJORAR"))
df

df["city"] = df["city"].fillna("Faltante") # Para llenar los datos nulos
df
# ---------------------------------------------------------------
# E) value_counts, sort_values, describe
# ---------------------------------------------------------------
df["status"].value_counts()

df.sort_values(by = "promedio", ascending= False) # Reordena el DataFrame

df.describe()
# ---------------------------------------------------------------
# F) GROUPBY + AGG; PIVOT_TABLE
# ---------------------------------------------------------------
df.groupby("city") # Queda como un objeto
df.groupby("city")["age"].mean()

df.groupby("city").get_group("Guadalajara")
df[df["city"] == "Guadalajara"] # Equivalente al groupby anterior

df.groupby("city")["age"].max()

df.groupby("city")["city"].value_counts() / len(df) * 100
# Para agregarle el signo de porcentaje a cada valor, se puede usar el método .apply() con una función lambda:
(df.groupby("city")["city"].value_counts() / len(df) * 100).apply(lambda x: f"{x:.2f}%") 

# ---------------------------------------------------------------
# G) MERGE/JOIN Y CONCAT
# ---------------------------------------------------------------
def create_sales_customers_csv(sales_path, customers_path):
    srows = ["sid,cid,amount,city","10,1,120,CDMX","11,2,50,Monterrey","23,3,500,Guadalajara","12,4,210,CDMX","13,5,90,Guadalajara"]
    crows = ["cid,name,city","1,Ana,CDMX","2,Luis,Monterrey","3,Marta","4,Juan,CDMX","5,Lia,Guadalajara"]
    with open(sales_path,"w",encoding="utf-8") as f:
        for r in srows: f.write(r+"\n")
    with open(customers_path,"w",encoding="utf-8") as f:
        for r in crows: f.write(r+"\n")

create_sales_customers_csv("sales.csv","customers.csv")

sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
print(sales)
print(customers)

# Merge
merged = pd.merge(sales, customers, on = "cid", suffixes= ("_sales", "_cust"))
print(merged)

# Concat
pd.concat([sales.head(2), sales.tail(1)], ignore_index= True) # Concat necesita que los df sean idénticos en sus columnas

# ---------------------------------------------------------------
# H) INTEROPERABILIDAD PANDAS + NUMPY
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# I) BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Usa dtypes correctos (astype) antes de cálculos.
# - Prefiere operaciones vectorizadas y groupby/agg nativos.
# - Documenta supuestos (columnas presentes, NA permitidos).
# - Genera datasets de ejemplo dentro del .py para reproducibilidad.