import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V29
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Media por Columnas de una Matriz
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D (lista de listas de números), calcula la media
#   aritmética de cada COLUMNA usando NumPy (axis=0). Retorna una lista
#   de floats redondeados a 2 decimales, uno por columna.
#
# Entrada:  lista de listas de números  →  mat
# Salida:   lista de floats (media de cada columna, 2 decimales)
#
# Ejemplo:
#   Entrada:  [[1,2],[3,4],[5,6]]
#   Salida:   [3.0, 4.0]
# ──────────────────────────────────────────────────────────

def problem_01(mat):
    # TU CÓDIGO AQUÍ
    a = np.array(mat, dtype=float)
    return [round(v, 2) for v in a.mean(axis=0).tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[[1,2],[3,4],[5,6]],[[0,0],[0,0]],[[5,10,15]],
           [[1,2,3],[4,5,6]],[[10],[20],[30]],[[1,1],[2,2],[3,3],[4,4]],
           [[-1,1],[-2,2]],[[100,0],[0,100]],[[3,6,9],[6,12,18]],
           [[7,14],[14,28]]]
_p1_exp = [[3.0,4.0],[0.0,0.0],[5.0,10.0,15.0],[2.5,3.5,4.5],[20.0],
           [2.5,2.5],[-1.5,1.5],[50.0,50.0],[4.5,9.0,13.5],[10.5,21.0]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if [round(v,2) for v in problem_01(i)]==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Unir Tablas y Eliminar Duplicados (concat)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Se reciben dos diccionarios con claves 'ID' (enteros) y 'Name'
#   (strings). Crea un DataFrame por cada uno, únelos verticalmente con
#   pd.concat, elimina filas con 'ID' duplicado (queda la primera
#   aparición) y retorna la lista de IDs resultantes.
#
# Entrada:  dict df1, dict df2  (ambos con claves "ID" y "Name")
# Salida:   lista de enteros (IDs únicos en orden de aparición)
#
# Ejemplo:
#   df1 = {"ID":[1,2],"Name":["Ana","Luis"]}
#   df2 = {"ID":[2,3],"Name":["Luis","Marta"]}
#   Salida:   [1, 2, 3]
# ──────────────────────────────────────────────────────────

def problem_02(d1, d2):
    # TU CÓDIGO AQUÍ
    df = pd.concat([pd.DataFrame(d1), pd.DataFrame(d2)], ignore_index=True)
    return df.drop_duplicates(subset="ID", keep="first")["ID"].tolist()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_d1 = [{"ID":[1,2],"Name":["Ana","Luis"]},
          {"ID":[10,20],"Name":["A","B"]},
          {"ID":[1],"Name":["X"]},
          {"ID":[5,6,7],"Name":["P","Q","R"]},
          {"ID":[1,2,3],"Name":["A","B","C"]},
          {"ID":[100],"Name":["Z"]},
          {"ID":[1,2],"Name":["M","N"]},
          {"ID":[9,8],"Name":["U","V"]},
          {"ID":[3,4],"Name":["G","H"]},
          {"ID":[1,1],"Name":["D","D"]}]
_p2_d2 = [{"ID":[2,3],"Name":["Luis","Marta"]},
          {"ID":[20,30],"Name":["B","C"]},
          {"ID":[1,2],"Name":["X","Y"]},
          {"ID":[7,8],"Name":["R","S"]},
          {"ID":[4,5],"Name":["D","E"]},
          {"ID":[200],"Name":["W"]},
          {"ID":[3,2],"Name":["O","N"]},
          {"ID":[8,7],"Name":["V","T"]},
          {"ID":[4,5],"Name":["H","I"]},
          {"ID":[2,3],"Name":["E","F"]}]
_p2_exp = [[1,2,3],[10,20,30],[1,2],[5,6,7,8],[1,2,3,4,5],
           [100,200],[1,2,3],[9,8,7],[3,4,5],[1,2,3]]
_p2_ok = sum(1 for d1,d2,e in zip(_p2_d1,_p2_d2,_p2_exp) if problem_02(d1,d2)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
# Título: Categorizar Ventas con Máscara y Resumir
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings) y 'Sales' (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.where) para agregar columna 'Category':
#        "ALTA"  si Sales >= 200
#        "MEDIA" si Sales >= 100 (y < 200)
#        "BAJA"  si Sales < 100
#   3. Agrupa por 'Category' y cuenta cuántas filas hay en cada categoría.
#   4. Retorna un diccionario {category: count}.
#
# Entrada:  dict con claves "Region" y "Sales"
# Salida:   dict {str: int}  (sólo categorías presentes)
#
# Ejemplo:
#   Entrada: {"Region":["N","S","E","W"],"Sales":[50,150,250,80]}
#   Salida:  {"BAJA":2,"MEDIA":1,"ALTA":1}
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    s = df["Sales"].to_numpy(dtype=float)
    df["Category"] = np.where(s >= 200,"ALTA", np.where(s >= 100,"MEDIA","BAJA"))
    counts = df.groupby("Category")["Category"].count()
    return {k:int(v) for k,v in counts.items()}

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Region":["N","S","E","W"],"Sales":[50,150,250,80]},
          {"Region":["A"],"Sales":[200]},
          {"Region":["B","C"],"Sales":[99,100]},
          {"Region":["D","E","F"],"Sales":[0,199,200]},
          {"Region":["G","H","I","J"],"Sales":[100,100,200,200]},
          {"Region":["K"],"Sales":[50]},
          {"Region":["L","M"],"Sales":[200,200]},
          {"Region":["N","O","P"],"Sales":[100,150,200]},
          {"Region":["Q","R"],"Sales":[0,0]},
          {"Region":["S","T","U","V"],"Sales":[50,150,250,350]}]
_p3_exp = [{"ALTA":1,"BAJA":2,"MEDIA":1},{"ALTA":1},{"BAJA":1,"MEDIA":1},
           {"ALTA":1,"BAJA":1,"MEDIA":1},{"ALTA":2,"MEDIA":2},{"BAJA":1},
           {"ALTA":2},{"ALTA":1,"MEDIA":2},{"BAJA":2},{"ALTA":2,"BAJA":1,"MEDIA":1}]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
