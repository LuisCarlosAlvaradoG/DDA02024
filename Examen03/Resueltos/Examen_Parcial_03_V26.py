import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V26
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Contar Valores en Rango (Máscara Compuesta)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros y dos límites (lo, hi), usa una
#   máscara booleana compuesta en NumPy para contar cuántos elementos
#   caen en el rango cerrado [lo, hi] (ambos extremos inclusive).
#
# Entrada:  lista de enteros arr, enteros lo y hi
# Salida:   entero (cantidad de elementos en [lo, hi])
#
# Ejemplo:
#   Entrada:  arr=[1,5,3,8,2,6],  lo=3,  hi=6
#   Salida:   3        # elementos: 5, 3, 6
# ──────────────────────────────────────────────────────────

def problem_01(arr, lo, hi):
    # TU CÓDIGO AQUÍ
    a = np.array(arr)
    mask = (a >= lo) & (a <= hi)
    return int(mask.sum())

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([1,5,3,8,2,6],3,6),([10,20,30],15,25),([1,2,3,4,5],1,5),
           ([0,0,0],1,5),([7,3,9,1,5],5,9),([-3,-1,0,1,3],-1,1),
           ([100,200,300],150,250),([5,5,5,5],5,5),
           ([1,2,3,4,5,6,7,8,9,10],3,7),([0,10,20,30,40],0,20)]
_p1_exp = [3,1,5,0,3,3,1,4,5,3]
_p1_ok = sum(1 for (arr,lo,hi),e in zip(_p1_in,_p1_exp) if problem_01(arr,lo,hi)==e)
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
# Título: Filtrar Filas por Máximo de Fila
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D de enteros y un umbral:
#   1. Usa NumPy para calcular el máximo de cada fila.
#   2. Usa pandas para agregar esa información como columna 'row_max'.
#   3. Filtra las filas donde row_max >= threshold.
#   4. Retorna la lista de filas filtradas (con el máximo al final).
#
# Entrada:  mat (lista de listas de enteros), threshold (entero)
# Salida:   lista de listas de enteros (filas + máximo al final)
#
# Ejemplo:
#   mat=[[1,2,3],[4,5,6],[7,8,9]], threshold=8
#   Salida: [[7,8,9,9]]
# ──────────────────────────────────────────────────────────

def problem_03(mat, threshold):
    # TU CÓDIGO AQUÍ
    arr = np.array(mat)
    row_max = arr.max(axis=1)
    df = pd.DataFrame(arr)
    df["row_max"] = row_max
    filtered = df[df["row_max"] >= threshold]
    return [row.tolist() for row in filtered.values]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_mat = [[[1,2,3],[4,5,6],[7,8,9]],[[0,0],[1,1],[2,2]],[[5]],
           [[1,2],[3,4],[5,6],[7,8]],[[10,20,30]],[[-1,-2,-3],[-4,-5,-6]],
           [[1,1,1],[2,2,2],[3,3,3]],[[5,5],[5,5],[5,5]],
           [[1,0,1],[0,1,0],[1,1,1]],[[100,200],[300,400]]]
_p3_thr = [8,1,5,6,25,-2,2,5,1,350]
_p3_exp = [[[7,8,9,9]],[[1,1,1],[2,2,2]],[[5,5]],[[5,6,6],[7,8,8]],
           [[10,20,30,30]],[[-1,-2,-3,-1]],[[2,2,2,2],[3,3,3,3]],
           [[5,5,5],[5,5,5],[5,5,5]],[[1,0,1,1],[0,1,0,1],[1,1,1,1]],
           [[300,400,400]]]
_p3_ok = sum(1 for (m,t,e) in zip(_p3_mat,_p3_thr,_p3_exp) if problem_03(m,t)==e)
print(f"Problema 03: {_p3_ok}/10")
