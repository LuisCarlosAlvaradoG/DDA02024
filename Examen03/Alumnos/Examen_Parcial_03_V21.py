import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V21
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Participación Relativa
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros no negativos, calcula la participación
#   relativa de cada elemento respecto al total:
#       p_i = x_i / sum(arr)
#   Si la suma total es 0, retorna una lista de ceros.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de floats redondeados a 2 decimales
#
# Ejemplo:
#   Entrada:  [1, 1, 2]
#   Salida:   [0.25, 0.25, 0.5]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,1,2],[0,0,0],[2,2],[1,2,3,4],[5],[0,5],[3,3,3],[2,3,5],[10,0,0],[4,6]]
_p1_exp = [[0.25,0.25,0.5],[0.0,0.0,0.0],[0.5,0.5],[0.1,0.2,0.3,0.4],
           [1.0],[0.0,1.0],[0.33,0.33,0.33],[0.2,0.3,0.5],[1.0,0.0,0.0],[0.4,0.6]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Promedio de Calificaciones con Datos Faltantes
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Student' (strings), 'Math' y 'Eng'
#   (números o None), crea un DataFrame. Sustituye los None con 0
#   (fillna). Agrega una columna 'Avg' = (Math + Eng) / 2.
#   Retorna el DataFrame completo con columnas Student, Math, Eng, Avg.
#   Todos los valores de Avg redondeados a 2 decimales.
#
# Entrada:  dict con claves "Student", "Math", "Eng"
# Salida:   DataFrame con columnas Student, Math, Eng, Avg
#
# Ejemplo:
#   Entrada:  {"Student":["Ana","Luis"],"Math":[80,None],"Eng":[90,70]}
#   Salida:   DataFrame con Ana Avg=85.0, Luis Avg=35.0
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in = [{"Student":["Ana","Luis"],"Math":[80,None],"Eng":[90,70]},
          {"Student":["A"],"Math":[100],"Eng":[100]},
          {"Student":["B","C"],"Math":[None,None],"Eng":[None,None]},
          {"Student":["D","E"],"Math":[60,80],"Eng":[70,90]},
          {"Student":["F"],"Math":[50],"Eng":[None]},
          {"Student":["G","H","I"],"Math":[70,None,90],"Eng":[80,60,None]},
          {"Student":["J","K"],"Math":[None,100],"Eng":[100,None]},
          {"Student":["L"],"Math":[0],"Eng":[0]},
          {"Student":["M","N"],"Math":[55,75],"Eng":[65,85]},
          {"Student":["O"],"Math":[None],"Eng":[None]}]
_p2_exp_avg = [85.0,100.0,0.0,65.0,25.0,85.0]  # not used directly below
_p2_ok = 0
for data in _p2_in:
    try:
        res = problem_02(data)
        if isinstance(res,pd.DataFrame) and "Avg" in res.columns and "Math" in res.columns:
            _p2_ok += 1
    except: pass
# Spot check: first case
try:
    r0 = problem_02(_p2_in[0])
    if round(r0.iloc[0]["Avg"],2)==85.0 and round(r0.iloc[1]["Avg"],2)==35.0:
        pass
    else:
        _p2_ok = max(0, _p2_ok-1)
except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas 
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
    pass

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
