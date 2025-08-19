
# ===============================================================
# 18.- ARCHIVOS: PANDAS — BASES + INTEGRACIÓN CON NUMPY
# Curso: Algoritmos y Programación (Python) — Sesión (~3 horas)
# Teoría: español | Código: inglés
# Reglas: Pandas + NumPy (sin matplotlib aquí).
# ===============================================================

"""
A) Objetivos
B) Series y DataFrame: creación, dtypes, index
C) Read/Write CSV (datasets precargados)
D) Selección: loc/iloc, filtrado, asignación, NA, astype
E) value_counts, sort_values, describe
F) GroupBy + agg; pivot_table
G) Merge/Join (inner/left/outer), concat
H) Interoperabilidad con NumPy: to_numpy, np.where
I) Casos guiados
J) Buenas prácticas
K) Banco de ejercicios (SOLUCIONES incluidas)
"""

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

# ---------------------------------------------------------------
# C) READ/WRITE CSV (DATASETS PRE-CARGADOS)
# ---------------------------------------------------------------
def create_students_csv(path):
    rows = [
        "id,name,age,math,eng,city",
        "1,Ana,21,88,92,CDMX",
        "2,Luis,19,75,81,Monterrey",
        "3,Marta,22,95,89,Guadalajara",
        "4,Juan,20,62,70,CDMX",
        "5,Lia,21,70,85,Guadalajara"
    ]
    with open(path, "w", encoding="utf-8") as f:
        for r in rows: f.write(r+"\n")

# create_students_csv("students.csv")
# df = pd.read_csv("students.csv"); print(df.head())
# df.to_csv("students_out.csv", index=False)

# ---------------------------------------------------------------
# D) SELECCIÓN, FILTRADO, ASIGNACIÓN; NA/ASTYPE
# ---------------------------------------------------------------
# df["avg"] = (df["math"] + df["eng"]) / 2.0
# df["status"] = np.where(df["avg"] >= 80, "OK", "LOW")
# print(df[df["city"]=="CDMX"])
# df["age"] = df["age"].astype(int)
# df["city"] = df["city"].fillna("NA")

# ---------------------------------------------------------------
# E) value_counts, sort_values, describe
# ---------------------------------------------------------------
# print(df["city"].value_counts())
# print(df.sort_values(by="avg", ascending=False))
# print(df.describe(numeric_only=True))

# ---------------------------------------------------------------
# F) GROUPBY + AGG; PIVOT_TABLE
# ---------------------------------------------------------------
# print(df.groupby("city")["avg"].mean())
# pt = pd.pivot_table(df, values="avg", index="city", aggfunc="mean"); print(pt)

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

# create_sales_customers_csv("sales.csv","customers.csv")
# sales = pd.read_csv("sales.csv"); customers = pd.read_csv("customers.csv")
# merged = pd.merge(sales, customers, on="cid", suffixes=("_sale","_cust")); print(merged.head())
# print(pd.concat([sales.head(2), sales.tail(2)], ignore_index=True))

# ---------------------------------------------------------------
# H) INTEROPERABILIDAD PANDAS + NUMPY
# ---------------------------------------------------------------
# arr = df[["math","eng"]].to_numpy(dtype=float)
# z = (arr - arr.mean(axis=0)) / arr.std(axis=0)
# df["z_math"], df["z_eng"] = z[:,0], z[:,1]

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

# ---------------------------------------------------------------
# K) BANCO DE EJERCICIOS (SOLUCIONES) — 25 EJERCICIOS
# ---------------------------------------------------------------

# 01) Series y DataFrame básicos
s = pd.Series([100,200], index=["x","y"]); df = pd.DataFrame({"a":[1,2],"b":[3,4]}); print(s); print(df)

# 02) Crear/leer CSV
rows = ["id,name,age,math,eng,city","1,Ana,21,88,92,CDMX","2,Luis,19,75,81,Monterrey","3,Marta,22,95,89,Guadalajara"]
with open("pd_ex2.csv","w",encoding="utf-8") as f:
    for r in rows: f.write(r+"\n")
df = pd.read_csv("pd_ex2.csv"); print(df.head())

# 03) loc/iloc
df = pd.DataFrame({"id":[1,2,3],"x":[10,20,30],"y":[5,6,7]}); print(df.loc[0,"x"], df.iloc[1,2]); print(df[["x","y"]])

# 04) Filtrado
df = pd.DataFrame({"id":[1,2,3],"math":[70,85,90]}); print(df[df["math"]>=80])

# 05) Columna derivada + estado
df = pd.DataFrame({"math":[70,85,90],"eng":[80,78,92]})
df["avg"]=(df["math"]+df["eng"])/2.0; df["status"]=np.where(df["avg"]>=80,"OK","LOW"); print(df)

# 06) fillna
df = pd.DataFrame({"city":["CDMX",None,"Monterrey"]}); df["city"]=df["city"].fillna("NA"); print(df)

# 07) groupby mean
df = pd.DataFrame({"city":["A","A","B"],"val":[10,20,30]}); print(df.groupby("city")["val"].mean())

# 08) value_counts
df = pd.DataFrame({"city":["A","B","A","C","B","B"]}); print(df["city"].value_counts())

# 09) sort_values
df = pd.DataFrame({"id":[1,2,3],"avg":[70,90,80]}); print(df.sort_values(by="avg", ascending=False))

# 10) merge inner
A = pd.DataFrame({"id":[1,2], "x":[10,20]}); B = pd.DataFrame({"id":[1,3], "y":[5,7]}); print(pd.merge(A,B,on="id", how="inner"))

# 11) concat vertical
A = pd.DataFrame({"id":[1,2]}); B = pd.DataFrame({"id":[3,4]}); print(pd.concat([A,B], ignore_index=True))

# 12) astype int
df = pd.DataFrame({"age":["21","19","22"]}); df["age"]=df["age"].astype(int); print(df.dtypes)

# 13) to_numpy + z-score
df = pd.DataFrame({"a":[1,2,3],"b":[4,6,8]}); arr=df[["a","b"]].to_numpy(float); z=(arr-arr.mean(0))/arr.std(0); df["za"]=z[:,0]; df["zb"]=z[:,1]; print(df)

# 14) rename
df = pd.DataFrame({"A":[1], "B":[2]}); print(df.rename(columns={"A":"a","B":"b"}))

# 15) drop columnas
df = pd.DataFrame({"a":[1], "b":[2], "c":[3]}); print(df.drop(columns=["b"]))

# 16) set_index/reset_index
df = pd.DataFrame({"id":[1,2],"x":[10,20]}).set_index("id"); print(df, "\n", df.reset_index())

# 17) drop_duplicates
df = pd.DataFrame({"id":[1,1,2,3]}); print(df.drop_duplicates())

# 18) apply didáctico
def f(row): return row["a"]*2 + row["b"]
df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6]}); print(df.apply(f, axis=1))

# 19) pivot_table
df = pd.DataFrame({"city":["A","A","B","B"],"kind":["x","y","x","y"],"val":[10,15,7,9]}); print(pd.pivot_table(df, values="val", index="city", columns="kind", aggfunc="mean"))

# 20) value_counts normalizado
df = pd.DataFrame({"city":["A","A","B","C","B","B"]}); print(df["city"].value_counts(normalize=True))

# 21) merge left + faltantes
A = pd.DataFrame({"id":[1,2,3]}); B = pd.DataFrame({"id":[2], "x":[10]}); M = pd.merge(A,B,on="id", how="left"); print(M, "\nmissing:", M["x"].isna().sum())

# 22) groupby multicolumna + agg dict
df = pd.DataFrame({"city":["A","A","B","B"],"kind":["x","x","y","y"],"val":[5,7,9,11]}); print(df.groupby(["city","kind"]).agg({"val":["mean","sum"]}))

# 23) ordenar por varias columnas
df = pd.DataFrame({"a":[2,1,2],"b":[3,1,2]}); print(df.sort_values(by=["a","b"], ascending=[True,False]))

# 24) map categorías
df = pd.DataFrame({"g":["M","F","M"]}); m = {"M":"Male","F":"Female"}; df["g2"]=df["g"].map(m); print(df)

# 25) cut en bins
df = pd.DataFrame({"x":[5,15,25,35]}); print(pd.cut(df["x"], bins=[0,10,20,30,40], labels=["A","B","C","D"]))
