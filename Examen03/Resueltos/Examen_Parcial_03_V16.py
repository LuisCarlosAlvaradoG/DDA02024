import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V16
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Desviación Estándar por Filas
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D de números, calcula la desviación estándar
#   poblacional (ddof=0) de cada FILA usando NumPy (axis=1).
#   Retorna una lista de floats redondeados a 2 decimales.
#
# Entrada:  lista de listas de números  →  mat
# Salida:   lista de floats (std de cada fila, 2 decimales)
#
# Ejemplo:
#   Entrada:  [[2,4,4,4,5,5,7,9]]
#   Salida:   [2.0]
# ──────────────────────────────────────────────────────────

def problem_01(mat):
    # TU CÓDIGO AQUÍ
    a = np.array(mat, dtype=float)
    return [round(v, 2) for v in a.std(axis=1, ddof=0).tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[[2,4,4,4,5,5,7,9]],[[1,1],[2,2]],[[0,0,0]],
           [[10,20],[30,40]],[[1,2,3],[4,5,6]],[[5,5,5]],
           [[-1,1],[-2,2]],[[3,7]],[[100,0],[50,50]],[[1,3,5,7]]]
_p1_exp = [[2.0],[0.0,0.0],[0.0],[5.0,5.0],[0.82,0.82],[0.0],
           [1.0,2.0],[2.0],[50.0,0.0],[2.24]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if [round(v,2) for v in problem_01(i)]==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Filtrar Empleados de Tiempo Completo
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Name' (strings) y 'Hours' (enteros,
#   horas semanales trabajadas), crea un DataFrame y retorna sólo las
#   filas donde Hours >= 40. Índice reiniciado.
#
# Entrada:  dict con claves "Name" y "Hours"
# Salida:   DataFrame filtrado (columnas Name, Hours), índice reiniciado
#
# Ejemplo:
#   Entrada:  {"Name":["Ana","Beto","Caro"], "Hours":[35,40,45]}
#   Salida:   DataFrame con Beto (40) y Caro (45)
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    return df[df["Hours"] >= 40].reset_index(drop=True)

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Name":["Ana","Beto","Caro"],"Hours":[35,40,45]},
           {"Name":["Tom"],"Hours":[40]},{"Name":["L1","L2"],"Hours":[10,20]},
           {"Name":["X","Y","Z"],"Hours":[50,39,60]},
           {"Name":["P","Q","R","S"],"Hours":[40,40,40,40]},
           {"Name":["A","B"],"Hours":[0,100]},
           {"Name":["John","Doe","Smith"],"Hours":[41,39,42]},
           {"Name":["M","N","O"],"Hours":[10,20,30]},
           {"Name":["U","V","W"],"Hours":[39,40,41]},
           {"Name":["K"],"Hours":[10]}]
_p2_exp = [{"Name":["Beto","Caro"],"Hours":[40,45]},{"Name":["Tom"],"Hours":[40]},
           {"Name":[],"Hours":[]},{"Name":["X","Z"],"Hours":[50,60]},
           {"Name":["P","Q","R","S"],"Hours":[40,40,40,40]},{"Name":["B"],"Hours":[100]},
           {"Name":["John","Smith"],"Hours":[41,42]},{"Name":[],"Hours":[]},
           {"Name":["V","W"],"Hours":[40,41]},{"Name":[],"Hours":[]}]
_p2_ok = 0
for data,exp in zip(_p2_in,_p2_exp):
    try:
        res = problem_02(data)
        exp_df = pd.DataFrame(exp,columns=["Name","Hours"])
        res = res.reset_index(drop=True)
        try: exp_df = exp_df.astype(res.dtypes.to_dict())
        except: pass
        if res.equals(exp_df): _p2_ok += 1
    except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
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
    df = pd.DataFrame(data)
    ratings = df["Rating"].to_numpy()
    vals, counts = np.unique(ratings, return_counts=True)
    moda = int(vals[np.argmax(counts)])
    mask = ratings == moda
    sub = df[mask]
    freq = sub["Region"].value_counts().to_dict()
    return (moda, freq)

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
