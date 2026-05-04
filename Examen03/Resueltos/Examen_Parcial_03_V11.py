import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V11
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
# Título: Mapear Categorías y Contar
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con clave 'Code' (lista de strings abreviados,
#   p.ej. "M"/"F") y un diccionario de mapeo, crea una Serie de pandas,
#   mapea cada código a su descripción completa y retorna un diccionario
#   con el conteo de cada categoría mapeada.
#
# Entrada:  dict con clave "Code" (lista de strings),
#           dict mapping {code: descripción}
# Salida:   dict {descripción: conteo}
#
# Ejemplo:
#   Entrada:  {"Code":["M","F","M","F","M"]},
#             {"M":"Male","F":"Female"}
#   Salida:   {"Male":3,"Female":2}
# ──────────────────────────────────────────────────────────

def problem_02(data, mapping):
    # TU CÓDIGO AQUÍ
    s = pd.Series(data["Code"]).map(mapping)
    return s.value_counts().to_dict()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in = [({"Code":["M","F","M","F","M"]},{"M":"Male","F":"Female"}),
          ({"Code":["A","B","A"]},{"A":"Alpha","B":"Beta"}),
          ({"Code":["X","X","X"]},{"X":"Xray"}),
          ({"Code":["P","Q","P","Q","P","P"]},{"P":"Plus","Q":"Quick"}),
          ({"Code":["Y","N","Y","N","Y"]},{"Y":"Yes","N":"No"}),
          ({"Code":["L","M","H","L","M","H","H"]},{"L":"Low","M":"Med","H":"High"}),
          ({"Code":["A","B","C","A","B","A"]},{"A":"Alfa","B":"Bravo","C":"Charlie"}),
          ({"Code":["R","G","B","R","G","R"]},{"R":"Red","G":"Green","B":"Blue"}),
          ({"Code":["S","S","S","S"]},{"S":"Sold"}),
          ({"Code":["U","D","U","U","D"]},{"U":"Up","D":"Down"})]
_p2_exp = [{"Male":3,"Female":2},{"Alpha":2,"Beta":1},{"Xray":3},{"Plus":4,"Quick":2},
           {"Yes":3,"No":2},{"High":3,"Low":2,"Med":2},{"Alfa":3,"Bravo":2,"Charlie":1},
           {"Red":3,"Green":2,"Blue":1},{"Sold":4},{"Up":3,"Down":2}]
_p2_ok = sum(1 for (d,m),e in zip(_p2_in,_p2_exp) if problem_02(d,m)==e)
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
