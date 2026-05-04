import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V19
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Normalización Min-Max
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros, normaliza sus valores con la fórmula
#   min-max:  x_norm = (x - min) / (max - min)
#   Si todos los elementos son iguales (max == min), retorna una lista de
#   ceros del mismo tamaño.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de floats redondeados a 2 decimales
#
# Ejemplo:
#   Entrada:  [0, 5, 10]
#   Salida:   [0.0, 0.5, 1.0]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    a = np.array(arr, dtype=float)
    mn, mx = a.min(), a.max()
    if mx == mn:
        return [0.0] * len(a)
    return [round(v, 2) for v in ((a - mn) / (mx - mn)).tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,2,3,4],[5,5,5],[0,10,20],[-1,0,1],[100,200,300,400],
           [3,3,6,9],[7],[2,4,6,8,10],[10,0,10,0],[5,15,25]]
_p1_exp = [[0.0,0.33,0.67,1.0],[0.0,0.0,0.0],[0.0,0.5,1.0],[0.0,0.5,1.0],
           [0.0,0.33,0.67,1.0],[0.0,0.0,0.5,1.0],[0.0],[0.0,0.25,0.5,0.75,1.0],
           [1.0,0.0,1.0,0.0],[0.0,0.5,1.0]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Promedio por Grupo (groupby)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'City' (strings) y 'Score' (números),
#   crea un DataFrame, agrupa por 'City' y calcula la media de 'Score'
#   por ciudad. Retorna un diccionario {city: round(mean,2)}.
#
# Entrada:  dict con claves "City" y "Score"
# Salida:   dict {str: float}  (media redondeada a 2 decimales)
#
# Ejemplo:
#   Entrada:  {"City":["A","A","B"], "Score":[10,20,30]}
#   Salida:   {"A": 15.0, "B": 30.0}
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    return df.groupby("City")["Score"].mean().round(2).to_dict()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"City":["A","A","B"],"Score":[10,20,30]},
           {"City":["X","X","X"],"Score":[5,10,15]},
           {"City":["M","N","M","N"],"Score":[1,2,3,4]},
           {"City":["Z"],"Score":[100]},
           {"City":["A","B","C"],"Score":[0,0,0]},
           {"City":["P","P","Q","Q"],"Score":[10,30,20,40]},
           {"City":["R","S","R","S","R"],"Score":[3,6,9,12,15]},
           {"City":["T","T"],"Score":[7,7]},
           {"City":["U","V","W"],"Score":[5,10,15]},
           {"City":["A","B","A","B"],"Score":[1,3,5,7]}]
_p2_exp = [{"A":15.0,"B":30.0},{"X":10.0},{"M":2.0,"N":3.0},{"Z":100.0},
           {"A":0.0,"B":0.0,"C":0.0},{"P":20.0,"Q":30.0},{"R":9.0,"S":9.0},
           {"T":7.0},{"U":5.0,"V":10.0,"W":15.0},{"A":3.0,"B":5.0}]
_p2_ok = sum(1 for i,e in zip(_p2_in,_p2_exp) if problem_02(i)==e)
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
