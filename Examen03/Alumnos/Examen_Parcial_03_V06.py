import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V06
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Detección de Outliers con Percentil
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números, usa NumPy para:
#   1. Calcular el percentil 90 del arreglo (np.percentile(array, 90)).
#   2. Crear una máscara booleana que identifique los elementos que
#      superan dicho percentil (outliers superiores).
#   3. Retornar la cantidad de outliers encontrados (entero).
#
# Entrada:  lista de números  →  arr
# Salida:   entero (cantidad de outliers)
#
# Ejemplo:
#   Entrada:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
#   Salida:   1          # sólo el 100 supera el percentil 90
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,2,3,4,5,6,7,8,9,100],
           [10,10,10,10,10,10,10,10,10,200],
           [1,1,1,1,1,1,1,1,1,1],
           [5,10,15,20,25,30,35,40,45,50],
           [0,0,0,0,0,0,0,0,0,1000],
           [3,3,3,3,3,3,3,3,3,4],
           [100,1,2,3,4,5,6,7,8,9],
           [2,4,6,8,10,12,14,16,18,20],
           [-5,-4,-3,-2,-1,0,1,2,3,4],
           [50,50,50,50,50,50,50,50,50,51]]
_p1_exp = [1,1,0,1,1,1,1,1,1,1]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
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
# Título: Moda Global y Frecuencia Relativa por Región
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings) y 'Rating'
#   (enteros del 1 al 5):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.unique con return_counts) para encontrar el
#      Rating que aparece más veces en todo el dataset (moda global).
#      En empate, usa el valor más pequeño.
#   3. Usa una máscara booleana de NumPy para filtrar las filas cuyo
#      Rating == moda global.
#   4. Cuenta cuántas filas quedan por Region en ese subconjunto
#      (usando pandas value_counts).
#   5. Retorna una tupla (moda, dict{region: count}).
#
# Entrada:  dict con claves "Region" y "Rating"
# Salida:   tupla (int, dict{str:int})
#
# Ejemplo:
#   Entrada: {"Region":["N","S","N","E","S","N"],"Rating":[5,3,5,3,5,3]}
#   moda=5  →  filas con Rating==5: N×2, S×1
#   Salida: (5, {"N":2,"S":1})
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Region":["N","S","N","E","S","N"],"Rating":[5,3,5,3,5,3]},
          {"Region":["A","B","A"],"Rating":[1,2,1]},
          {"Region":["X","Y","Z"],"Rating":[3,3,3]},
          {"Region":["M","N"],"Rating":[4,5]},
          {"Region":["P","Q","P","Q","P"],"Rating":[2,2,2,3,3]},
          {"Region":["G","H","G"],"Rating":[1,1,2]},
          {"Region":["R","S","T","R"],"Rating":[5,4,5,4]},
          {"Region":["U","V","U","V"],"Rating":[3,3,4,4]},
          {"Region":["C","D","C","D","C"],"Rating":[2,3,2,2,3]},
          {"Region":["L","M","N","L"],"Rating":[1,2,1,3]}]
_p3_exp = [(3,{"S":1,"E":1,"N":1}),(1,{"A":2}),(3,{"X":1,"Y":1,"Z":1}),
           (4,{"M":1}),(2,{"P":2,"Q":1}),(1,{"G":1,"H":1}),
           (4,{"S":1,"R":1}),(3,{"U":1,"V":1}),
           (2,{"C":2,"D":1}),(1,{"L":1,"N":1})]
_p3_ok = 0
for i,e in zip(_p3_in,_p3_exp):
    try:
        r = problem_03(i)
        if r[0]==e[0] and r[1]==e[1]: _p3_ok+=1
    except: pass
print(f"Problema 03: {_p3_ok}/10")
