
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

# Acceder a elementos del DataFrame de la columna age

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


# ---------------------------------------------------------------
# D) SELECCIÓN, FILTRADO, ASIGNACIÓN; NA/ASTYPE
# ---------------------------------------------------------------



# ---------------------------------------------------------------
# E) value_counts, sort_values, describe
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# F) GROUPBY + AGG; PIVOT_TABLE
# ---------------------------------------------------------------

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