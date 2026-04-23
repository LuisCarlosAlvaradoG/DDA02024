
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
s = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(s)

df = pd.DataFrame({
    "id" : [1, 2, 3],
    "nombre" : ["Regina", "Vero", "Bruno"],
    "edad" : [19, 20, 18]
})
print(df)

df.index = ["A", "B", "C"] # Cambia el nombre de las filas.  INDEX -> FILAS 
df

# Acceder a elementos del DataFrame de la columna edad
df.edad
df["edad"]
df.loc[:, "edad"]  # .loc necesita los nombres de las filas/columnas
df.iloc[:, 2] # .iloc necesita los índices de las filas/columnas

# Extraer Vero 20
df.loc["B", ["nombre", "edad"]]  # filas, columnas
df.iloc[1, 1:] #filas, columnas

# Extraer 3 Bruno
df.iloc[2, :2]

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

df = pd.read_csv("students.csv")  # Para leer un archivo de Excel del tipo csv que ya existe
df

df.head(2) # Para ver la parte superior del DataFrame

df.to_csv("students_out.csv", index = False) # Para convertir un DataFrame de pandas en un Excel

# ---------------------------------------------------------------
# D) SELECCIÓN, FILTRADO, ASIGNACIÓN; NA/ASTYPE
# ---------------------------------------------------------------
df["promedio"] = (df["math"] + df["prog"]) / 2
df

df["status"] = np.where(df["promedio"] >= 80, "OK", "MEJORAR")
df

df["city"] = df["city"].fillna("Faltante")
df
# df.to_csv("students_out.csv", index = False) 

# ---------------------------------------------------------------
# E) value_counts, sort_values, describe
# ---------------------------------------------------------------
df["city"].value_counts()

df.sort_values(by = "promedio", ascending= False)

df.describe()
# ---------------------------------------------------------------
# F) GROUPBY + AGG; PIVOT_TABLE
# ---------------------------------------------------------------
df.groupby("city") # Queda como un objeto
df.groupby("city")["age"].mean()

df.groupby("city").get_group("Guadalajara")
df[ df["city"] == "Guadalajara"] # Equivalente al groupby anterior
# and    - >  &
# or     - >  |      Traducción de condicionales a Numpy y Pandas
# not    - >  ~

df[ (df["city"] == "Guadalajara") & (df["status"] == "OK")]
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

merged = pd.merge(sales, customers, on = "cid", suffixes=("_sales", "_cust"))
print(merged)

pd.concat([sales.head(2), sales.tail(1)], ignore_index= True)
# concat necesita que los DataFrames sean idénticos en sus columnas
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