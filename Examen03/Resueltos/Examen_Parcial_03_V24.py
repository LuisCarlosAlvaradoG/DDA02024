import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V24
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
#   1. Calcular el percentil 90 del arreglo.
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
    a = np.array(arr, dtype=float)
    p90 = np.percentile(a, 90)
    mask = a > p90
    return int(mask.sum())

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
# Título: Tabla Pivote de Promedios
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings), 'Quarter'
#   (strings, p.ej. "Q1") y 'Revenue' (números), crea un DataFrame y
#   construye una tabla pivote con pd.pivot_table donde:
#     - index = 'Region'
#     - columns = 'Quarter'
#     - values = 'Revenue'
#     - aggfunc = 'mean'
#   Retorna el DataFrame resultante (tabla pivote).
#
# Entrada:  dict con claves "Region", "Quarter", "Revenue"
# Salida:   DataFrame (tabla pivote)
#
# Ejemplo:
#   Entrada:  {"Region":["N","N","S"],"Quarter":["Q1","Q2","Q1"],
#              "Revenue":[100,200,150]}
#   Salida:   pivot con N→Q1=100,Q2=200 y S→Q1=150
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    return pd.pivot_table(df, values="Revenue", index="Region",
                          columns="Quarter", aggfunc="mean")

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in = [{"Region":["N","N","S"],"Quarter":["Q1","Q2","Q1"],"Revenue":[100,200,150]},
          {"Region":["E","W","E","W"],"Quarter":["Q1","Q1","Q2","Q2"],"Revenue":[10,20,30,40]},
          {"Region":["A"],"Quarter":["Q1"],"Revenue":[50]},
          {"Region":["X","X"],"Quarter":["Q1","Q1"],"Revenue":[10,20]},
          {"Region":["N","S","E","W"],"Quarter":["Q1","Q1","Q1","Q1"],"Revenue":[1,2,3,4]}]
_p2_ok = 0
for data in _p2_in:
    try:
        res = problem_02(data)
        if isinstance(res, pd.DataFrame): _p2_ok += 2
    except: pass
_p2_ok = min(_p2_ok, 10)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
# Título: Filtrar Filas por Suma con NumPy y Pandas
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D de enteros y un umbral:
#   1. Usa NumPy para calcular la suma de cada fila.
#   2. Usa pandas para construir un DataFrame con las filas originales
#      más una columna 'row_sum' con esa suma.
#   3. Filtra las filas donde row_sum >= threshold.
#   4. Retorna la lista de filas filtradas (incluida la suma al final).
#
# Entrada:  mat (lista de listas de enteros), threshold (entero)
# Salida:   lista de listas de enteros (filas + suma al final)
#
# Ejemplo:
#   mat=[[1,2,3],[4,5,6],[7,8,9]], threshold=10
#   Salida: [[4,5,6,15],[7,8,9,24]]
# ──────────────────────────────────────────────────────────

def problem_03(mat, threshold):
    # TU CÓDIGO AQUÍ
    arr = np.array(mat)
    row_sums = arr.sum(axis=1)
    df = pd.DataFrame(arr)
    df["row_sum"] = row_sums
    filtered = df[df["row_sum"] >= threshold]
    return [row.tolist() for row in filtered.values]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_mat = [[[1,2,3],[4,5,6],[7,8,9]],[[0,0],[1,1],[2,2]],[[5]],
           [[1,2],[3,4],[5,6],[7,8]],[[10,20,30]],[[-1,-2,-3],[-4,-5,-6]],
           [[1,1,1],[2,2,2],[3,3,3]],[[5,5],[5,5],[5,5]],
           [[1,0,1],[0,1,0],[1,1,1]],[[100,200],[300,400]]]
_p3_thr = [10,3,5,10,50,-10,6,10,2,500]
_p3_exp = [[[4,5,6,15],[7,8,9,24]],[[2,2,4]],[[5,5]],[[5,6,11],[7,8,15]],
           [[10,20,30,60]],[[-1,-2,-3,-6]],[[2,2,2,6],[3,3,3,9]],
           [[5,5,10],[5,5,10],[5,5,10]],[[1,0,1,2],[1,1,1,3]],[[300,400,700]]]
_p3_ok = sum(1 for (m,t,e) in zip(_p3_mat,_p3_thr,_p3_exp) if problem_03(m,t)==e)
print(f"Problema 03: {_p3_ok}/10")
