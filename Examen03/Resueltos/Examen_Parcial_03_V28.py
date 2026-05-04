import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V28
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Rectificación (ReLU) con Máscara
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números, aplica la función ReLU:
#   sustituye todos los valores negativos por 0.0 (los positivos y
#   ceros se conservan). Usa una máscara booleana de NumPy.
#   Retorna una lista de floats redondeados a 2 decimales.
#
# Entrada:  lista de números  →  arr
# Salida:   lista de floats (valores rectificados, 2 decimales)
#
# Ejemplo:
#   Entrada:  [-3, 0, 5, -1, 2]
#   Salida:   [0.0, 0.0, 5.0, 0.0, 2.0]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    a = np.array(arr, dtype=float)
    a[a < 0] = 0.0
    return [round(v, 2) for v in a.tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[-3,0,5,-1,2],[1,2,3],[0,0,0],[-1,-2,-3],[-5,10,-15,20],
           [0.5,-0.5,1.5],[100,-100],[3.14,-2.72,0],[0,-0.01,0.01],[-7,-7,-7]]
_p1_exp = [[0.0,0.0,5.0,0.0,2.0],[1.0,2.0,3.0],[0.0,0.0,0.0],
           [0.0,0.0,0.0],[0.0,10.0,0.0,20.0],[0.5,0.0,1.5],
           [100.0,0.0],[3.14,0.0,0.0],[0.0,0.0,0.01],[0.0,0.0,0.0]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Calcular Bono con apply
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Employee' (strings) y 'Salary'
#   (números), crea un DataFrame y agrega una columna 'Bonus' usando
#   apply (axis=1). El bono se calcula así:
#     - Si Salary >= 5000 → Bonus = Salary * 0.10
#     - Si Salary >= 3000 → Bonus = Salary * 0.07
#     - Otro caso         → Bonus = Salary * 0.05
#   Los valores de 'Bonus' deben estar redondeados a 2 decimales.
#   Retorna la lista de valores de la columna 'Bonus'.
#
# Entrada:  dict con claves "Employee" y "Salary"
# Salida:   lista de floats (bonos redondeados a 2 decimales)
#
# Ejemplo:
#   Entrada:  {"Employee":["A","B","C"],"Salary":[2000,3500,6000]}
#   Salida:   [100.0, 245.0, 600.0]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    def bono(row):
        s = row["Salary"]
        if s >= 5000: return round(s*0.10, 2)
        if s >= 3000: return round(s*0.07, 2)
        return round(s*0.05, 2)
    df["Bonus"] = df.apply(bono, axis=1)
    return df["Bonus"].tolist()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Employee":["A","B","C"],"Salary":[2000,3500,6000]},
           {"Employee":["X"],"Salary":[5000]},
           {"Employee":["M","N"],"Salary":[1000,3000]},
           {"Employee":["P","Q","R"],"Salary":[4999,5000,5001]},
           {"Employee":["G"],"Salary":[0]},
           {"Employee":["H","I"],"Salary":[2999,3000]},
           {"Employee":["J","K","L"],"Salary":[3000,4000,5000]},
           {"Employee":["U"],"Salary":[10000]},
           {"Employee":["V","W"],"Salary":[500,5500]},
           {"Employee":["T","S"],"Salary":[2500,7500]}]
_p2_exp = [[100.0,245.0,600.0],[500.0],[50.0,210.0],
           [349.93,500.0,500.1],[0.0],[149.95,210.0],
           [210.0,280.0,500.0],[1000.0],[25.0,550.0],[125.0,750.0]]
_p2_ok = sum(1 for i,e in zip(_p2_in,_p2_exp) if problem_02(i)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
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
    df = pd.DataFrame(data)
    v = df["Value"].to_numpy(dtype=float)
    mn, mx = v.min(), v.max()
    if mx == mn:
        df["norm"] = 0.0
    else:
        df["norm"] = np.round((v - mn)/(mx - mn), 2)
    return df.groupby("Segment")["norm"].mean().round(2).to_dict()

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
