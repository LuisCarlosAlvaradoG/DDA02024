import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V18
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Cambio Porcentual Consecutivo
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números positivos, calcula el cambio
#   porcentual entre cada par de elementos consecutivos:
#       pct_i = (arr[i+1] - arr[i]) / arr[i] * 100
#   Retorna una lista de floats redondeados a 2 decimales de longitud
#   len(arr) - 1.  Si el arreglo tiene 1 o 0 elementos, retorna [].
#
# Entrada:  lista de números positivos  →  arr
# Salida:   lista de floats (cambios porcentuales, 2 decimales)
#
# Ejemplo:
#   Entrada:  [100, 110, 99, 120]
#   Salida:   [10.0, -10.0, 21.21]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[100,110,99,120],[200,100],[50,50,50],[1,2,4,8],
           [10],[1,10,100],[5,4,3,2,1],[100,200,400],
           [3,6],[10,9,8,7]]
_p1_exp = [[10.0,-10.0,21.21],[-50.0],[0.0,0.0],[100.0,100.0,100.0],
           [],[900.0,900.0],[-20.0,-25.0,-33.33,-50.0],[100.0,100.0],
           [100.0],[-10.0,-11.11,-12.5]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Clasificar Ventas con Columna Derivada
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Product' (strings) y 'Sales'
#   (enteros), crea un DataFrame, agrega una columna 'Status' con el
#   valor "ALTO" si Sales >= 100 y "BAJO" en otro caso, y retorna el
#   DataFrame completo (con las tres columnas). Índice reiniciado.
#
# Entrada:  dict con claves "Product" y "Sales"
# Salida:   DataFrame con columnas Product, Sales, Status
#
# Ejemplo:
#   Entrada:  {"Product":["A","B"], "Sales":[80,120]}
#   Salida:   DataFrame con Status ["BAJO","ALTO"]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Product":["A","B"],"Sales":[80,120]},
           {"Product":["X"],"Sales":[100]},
           {"Product":["P","Q","R"],"Sales":[50,100,200]},
           {"Product":["M","N"],"Sales":[0,99]},
           {"Product":["Z"],"Sales":[101]},
           {"Product":["C","D","E","F"],"Sales":[100,100,99,101]},
           {"Product":["G"],"Sales":[0]},
           {"Product":["H","I"],"Sales":[200,50]},
           {"Product":["J","K","L"],"Sales":[99,100,101]},
           {"Product":["W"],"Sales":[100]}]
_p2_exp_status = [["BAJO","ALTO"],["ALTO"],["BAJO","ALTO","ALTO"],["BAJO","BAJO"],
                  ["ALTO"],["ALTO","ALTO","BAJO","ALTO"],["BAJO"],["ALTO","BAJO"],
                  ["BAJO","ALTO","ALTO"],["ALTO"]]
_p2_ok = 0
for data,exp_s in zip(_p2_in,_p2_exp_status):
    try:
        res = problem_02(data)
        if isinstance(res,pd.DataFrame) and "Status" in res.columns and res["Status"].tolist()==exp_s:
            _p2_ok += 1
    except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  
# Título: Normalizar y Agrupar por Segmento
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Segment' (strings) y 'Value'
#   (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy para calcular la normalización min-max de 'Value'
#      y agrégala como columna 'norm' (redondeada a 2 dec).
#   3. Agrupa por 'Segment' y calcula la media de 'norm' por grupo.
#   4. Retorna un diccionario {segment: round(mean_norm, 2)}.
#
# Entrada:  dict con claves "Segment" y "Value"
# Salida:   dict {str: float}
#
# Ejemplo:
#   Entrada: {"Segment":["A","A","B","B"],"Value":[0,10,5,15]}
#   Salida:  {"A":0.25,"B":0.67}
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Segment":["A","A","B","B"],"Value":[0,10,5,15]},
          {"Segment":["X","Y"],"Value":[1,1]},
          {"Segment":["M","N","M","N"],"Value":[0,5,10,15]},
          {"Segment":["A","A","A"],"Value":[2,4,6]},
          {"Segment":["P","Q","P","Q"],"Value":[0,0,10,10]},
          {"Segment":["G","H","G"],"Value":[1,3,5]},
          {"Segment":["Z","Z"],"Value":[0,100]},
          {"Segment":["R","S","R"],"Value":[10,20,30]},
          {"Segment":["C","D","E"],"Value":[0,50,100]},
          {"Segment":["U","U","V","V"],"Value":[5,15,10,20]}]
_p3_exp = [{"A":0.34,"B":0.66},{"X":0.0,"Y":0.0},{"M":0.34,"N":0.66},
           {"A":0.5},{"P":0.5,"Q":0.5},{"G":0.5,"H":0.5},
           {"Z":0.5},{"R":0.5,"S":0.5},{"C":0.0,"D":0.5,"E":1.0},
           {"U":0.34,"V":0.66}]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
