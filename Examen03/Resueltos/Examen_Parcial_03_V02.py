import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V02
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Estandarización Z-Score
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros, estandariza sus valores con z-score:
#       z = (x - media) / desv_std
#   Usa desviación estándar poblacional (ddof=0).
#   Si la desviación estándar es 0, retorna una lista de ceros.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de floats redondeados a 2 decimales
#
# Ejemplo:
#   Entrada:  [1, 2, 3]
#   Salida:   [-1.22, 0.0, 1.22]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    a = np.array(arr, dtype=float)
    sd = a.std()
    if sd == 0:
        return [0.0] * len(a)
    return [round(v, 2) for v in ((a - a.mean()) / sd).tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,2,3],[5,5,5],[0,10,20],[-1,0,1],[100,200,300,400],
           [3,3,6,9],[7],[2,4,6,8,10],[10,0,10,0],[5,15,25]]
_p1_exp = [[-1.22,0.0,1.22],[0.0,0.0,0.0],[-1.22,0.0,1.22],[-1.22,0.0,1.22],
           [-1.34,-0.45,0.45,1.34],[-0.9,-0.9,0.3,1.51],[0.0],
           [-1.41,-0.71,0.0,0.71,1.41],[1.0,-1.0,1.0,-1.0],[-1.22,0.0,1.22]]
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
# Título: Ventas Acumuladas y Día de Meta
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Day' (strings) y 'Sales' (enteros)
#   y un entero goal:
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.cumsum) para calcular la columna 'cumulative'.
#   3. Usa una máscara booleana para encontrar el primer día en que
#      la venta acumulada supera (>) el goal.
#   4. Retorna el nombre del día (string) o "No alcanzado" si nunca
#      se supera el goal.
#
# Entrada:  dict con claves "Day" y "Sales", entero goal
# Salida:   string (nombre del día o "No alcanzado")
#
# Ejemplo:
#   Entrada: {"Day":["Lun","Mar","Mié","Jue"],"Sales":[30,40,20,50]},
#            goal=80
#   Salida:  "Mié"    # cumsum=[30,70,90,140] → 90>80 en Mié
# ──────────────────────────────────────────────────────────

def problem_03(data, goal):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    sales = df["Sales"].to_numpy()
    df["cumulative"] = np.cumsum(sales)
    mask = df["cumulative"] > goal
    if not mask.any():
        return "No alcanzado"
    return df[mask].iloc[0]["Day"]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [({"Day":["Lun","Mar","Mié","Jue"],"Sales":[30,40,20,50]},80),
          ({"Day":["D1","D2","D3"],"Sales":[10,10,10]},100),
          ({"Day":["A","B","C"],"Sales":[50,50,50]},100),
          ({"Day":["M","T","W"],"Sales":[100,100,100]},50),
          ({"Day":["X"],"Sales":[200]},100),
          ({"Day":["D1","D2","D3","D4"],"Sales":[25,25,25,25]},99),
          ({"Day":["W1","W2","W3"],"Sales":[0,0,1]},0),
          ({"Day":["P","Q","R","S"],"Sales":[10,20,30,40]},55),
          ({"Day":["U","V"],"Sales":[5,5]},100),
          ({"Day":["L","M","X","J","V"],"Sales":[20,20,20,20,20]},79)]
_p3_exp = ["Mié","No alcanzado","C","M","X","D4","W3","R","No alcanzado","J"]
_p3_ok = sum(1 for (d,g),e in zip(_p3_in,_p3_exp) if problem_03(d,g)==e)
print(f"Problema 03: {_p3_ok}/10")
