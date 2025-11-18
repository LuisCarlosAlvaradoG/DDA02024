
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
s = pd.Series([10,20,30], index=["a","b","c"])
print("Series s:\n", s)

df = pd.DataFrame({"id":[1,2,3],"name":["Ana","Luis","Marta"],"age":[21,19,22]})
print("DataFrame df:\n", df)
print("dtypes:\n", df.dtypes)

# Acceder a elementos del DataFrame de la columna age
df["age"]
df.age
df.loc[0, "age"]
df.iloc[1, 2]

df.iloc[1:3, 1:3]
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
# Supongamos que el students.csv lo hice a mano
df = pd.read_csv("students.csv")
print(df.head(2))
df.to_csv("students.csv", index=False)

# ---------------------------------------------------------------
# D) SELECCIÓN, FILTRADO, ASIGNACIÓN; NA/ASTYPE
# ---------------------------------------------------------------
df["avg"] = (df["math"] + df["prog"]) / 2.0
df["status"] = np.where(df["avg"] >= 80, "1", "0")
# Agregar una nueva fila
df.loc[len(df)] = [6, "Eva", 20, 85, 90, "CDMX", 87.5, "1"]

# df.to_csv("students_copy.csv", index=False)
print(df[df["city"]=="CDMX"])

print(df[df["age"]>20])

# El AND es & y el OR es | NOT es ~
print(df[(df["status"] == "OK") & (df["math"] > 80)])

df["avg"] = df["avg"].astype(int)
df["city"] = df["city"].fillna(df["city"].mode())

# ---------------------------------------------------------------
# E) value_counts, sort_values, describe
# ---------------------------------------------------------------
print(df["city"].value_counts())
print(df.sort_values(by="avg", ascending=True))
print(df.describe())

df_copy = df.drop(columns = ["status"])

# ---------------------------------------------------------------
# F) GROUPBY + AGG; PIVOT_TABLE
# ---------------------------------------------------------------
print(df.groupby("city")["age"].mean())
print(df.groupby("city").min())
print(df.groupby("city").value_counts())
print(df.groupby("city").get_group("Guadalajara"))
pt = pd.pivot_table(df, values="age", index="status", aggfunc="mean")
print(pt)



# ---------------------------------------------------------------
# G) MERGE/JOIN Y CONCAT
# ---------------------------------------------------------------
def create_sales_customers_csv(sales_path, customers_path):
    srows = ["sid,cid,amount,city","10,1,120,CDMX","11,2,50,Monterrey","12,4,210,CDMX","13,5,90,Guadalajara"]
    crows = ["cid,name,city","1,Ana,CDMX","2,Luis,Monterrey","3,Marta,Guadalajara","4,Juan,CDMX","5,Lia,Guadalajara"]
    with open(sales_path,"w",encoding="utf-8") as f:
        for r in srows: f.write(r+"\n")
    with open(customers_path,"w",encoding="utf-8") as f:
        for r in crows: f.write(r+"\n")

create_sales_customers_csv("sales.csv","customers.csv")
sales = pd.read_csv("sales.csv"); customers = pd.read_csv("customers.csv")
print(sales)
print(customers)
merged = pd.merge(sales, customers, on="cid", suffixes=("_sale","_cust"))
print(merged)

def create_sales_customers_csv2(sales_path):
    srows = ["sid,cid,amount,city","20,8,120,Puebla","21,9,50,Veracruz","22,10,210,CDMX","23,11,90,Monterrey"]
    with open(sales_path,"w",encoding="utf-8") as f:
        for r in srows: f.write(r+"\n")
create_sales_customers_csv2("sales2.csv")
sales2 = pd.read_csv("sales2.csv")


print(pd.concat([sales, sales2], ignore_index=True))

# ---------------------------------------------------------------
# H) INTEROPERABILIDAD PANDAS + NUMPY
# ---------------------------------------------------------------
arr = df[["math","prog"]].to_numpy(dtype=float)
z = (arr - arr.mean(axis=0)) / arr.std(axis=0)
df["z_math"], df["z_prog"] = z[:,0], z[:,1]

# ---------------------------------------------------------------
# I) CASOS GUIADOS
# ---------------------------------------------------------------
def case_students_pipeline(in_path, out_path):
    df = pd.read_csv(in_path)
    df["avg"] = (df["math"] + df["eng"]) / 2.0
    df["status"] = np.where(df["avg"] >= 80, "OK", "LOW")
    rep = df.groupby("city")["avg"].mean().reset_index()
    rep.to_csv(out_path, index=False)
    return rep

def case_sales_merge(sales_path, customers_path):
    sales = pd.read_csv(sales_path)
    customers = pd.read_csv(customers_path)
    merged = pd.merge(sales, customers, on="cid", suffixes=("_sale","_cust"))
    top = merged.groupby("city_sale")["amount"].sum().reset_index().sort_values("amount", ascending=False)
    return merged, top

# ---------------------------------------------------------------
# J) BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Usa dtypes correctos (astype) antes de cálculos.
# - Prefiere operaciones vectorizadas y groupby/agg nativos.
# - Documenta supuestos (columnas presentes, NA permitidos).
# - Genera datasets de ejemplo dentro del .py para reproducibilidad.