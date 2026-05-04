import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V03
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
    a = np.array(arr, dtype=float)
    s = a.sum()
    if s == 0:
        return [0.0] * len(a)
    return [round(v, 2) for v in (a / s).tolist()]

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,1,2],[0,0,0],[2,2],[1,2,3,4],[5],[0,5],[3,3,3],[2,3,5],[10,0,0],[4,6]]
_p1_exp = [[0.25,0.25,0.5],[0.0,0.0,0.0],[0.5,0.5],[0.1,0.2,0.3,0.4],
           [1.0],[0.0,1.0],[0.33,0.33,0.33],[0.2,0.3,0.5],[1.0,0.0,0.0],[0.4,0.6]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
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
# Título: Filtrar Filas por Promedio de Fila
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D y un umbral numérico:
#   1. Usa NumPy para calcular la media de cada fila.
#   2. Usa pandas para construir un DataFrame con las columnas de la
#      matriz original más una columna 'row_mean'.
#   3. Filtra las filas donde row_mean >= threshold.
#   4. Retorna la lista de filas filtradas (con el promedio al final,
#      como float).
#
# Entrada:  mat (lista de listas), threshold (número)
# Salida:   lista de listas (filas + promedio al final como float)
#
# Ejemplo:
#   mat=[[1,3],[5,7],[9,11]], threshold=5
#   Salida: [[5.0,7.0,6.0],[9.0,11.0,10.0]]
# ──────────────────────────────────────────────────────────

def problem_03(mat, threshold):
    # TU CÓDIGO AQUÍ
    arr = np.array(mat, dtype=float)
    means = arr.mean(axis=1)
    df = pd.DataFrame(arr)
    df["row_mean"] = means
    filtered = df[df["row_mean"] >= threshold]
    return [row.tolist() for row in filtered.values]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_mat = [[[1,3],[5,7],[9,11]],[[0,0],[2,2],[4,4]],[[5]],
           [[1,2,3],[3,3,3],[10,0,0]],[[10,20,30]],[[-1,-3],[-4,-6]],
           [[1,1,1],[2,2,2],[3,3,3]],[[5,5],[5,5],[5,5]],
           [[1,0,1,0],[0,0,0,0],[2,2,2,2]],[[100,200],[300,400]]]
_p3_thr = [5,1,5,4,15,-3,2,5,0.5,200]
_p3_exp = [[[5.0,7.0,6.0],[9.0,11.0,10.0]],[[2.0,2.0,2.0],[4.0,4.0,4.0]],
           [[5.0,5.0]],[],[[10.0,20.0,30.0,20.0]],[[-1.0,-3.0,-2.0]],
           [[2.0,2.0,2.0,2.0],[3.0,3.0,3.0,3.0]],[[5.0,5.0,5.0],[5.0,5.0,5.0],[5.0,5.0,5.0]],
           [[1.0,0.0,1.0,0.0,0.5],[2.0,2.0,2.0,2.0,2.0]],[[300.0,400.0,350.0]]]
_p3_ok = sum(1 for (m,t,e) in zip(_p3_mat,_p3_thr,_p3_exp) if problem_03(m,t)==e)
print(f"Problema 03: {_p3_ok}/10")
