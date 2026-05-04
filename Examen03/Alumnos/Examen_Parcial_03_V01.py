import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V01
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Normalización Min-Max
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros, normaliza sus valores con la fórmula
#   min-max:  x_norm = (x - min) / (max - min)
#   Si todos los elementos son iguales (max == min), retorna una lista de
#   ceros del mismo tamaño.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de floats redondeados a 2 decimales
#
# Ejemplo:
#   Entrada:  [0, 5, 10]
#   Salida:   [0.0, 0.5, 1.0]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,2,3,4],[5,5,5],[0,10,20],[-1,0,1],[100,200,300,400],
           [3,3,6,9],[7],[2,4,6,8,10],[10,0,10,0],[5,15,25]]
_p1_exp = [[0.0,0.33,0.67,1.0],[0.0,0.0,0.0],[0.0,0.5,1.0],[0.0,0.5,1.0],
           [0.0,0.33,0.67,1.0],[0.0,0.0,0.5,1.0],[0.0],[0.0,0.25,0.5,0.75,1.0],
           [1.0,0.0,1.0,0.0],[0.0,0.5,1.0]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Filtrar Adultos
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Name' (strings) y 'Age' (enteros),
#   crea un DataFrame y retorna sólo las filas donde Age >= 18.
#   El índice debe ser continuo (reset_index).
#
# Entrada:  dict con claves "Name" y "Age"
# Salida:   DataFrame filtrado (columnas Name, Age), índice reiniciado
#
# Ejemplo:
#   Entrada:  {"Name":["Ana","Bob","Lia"], "Age":[17,20,18]}
#   Salida:   DataFrame con Bob (20) y Lia (18)
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Name":["Alice","Bob","Charlie"],"Age":[17,18,19]},
           {"Name":["Tom"],"Age":[18]},
           {"Name":["Anna","Ben"],"Age":[16,17]},
           {"Name":["X","Y","Z"],"Age":[20,15,30]},
           {"Name":["P","Q","R","S"],"Age":[18,18,18,18]},
           {"Name":["A","B"],"Age":[0,100]},
           {"Name":["John","Doe","Smith"],"Age":[21,17,22]},
           {"Name":["M","N","O"],"Age":[17,16,15]},
           {"Name":["U","V","W"],"Age":[19,19,17]},
           {"Name":["K"],"Age":[10]}]
_p2_exp = [{"Name":["Bob","Charlie"],"Age":[18,19]},{"Name":["Tom"],"Age":[18]},
           {"Name":[],"Age":[]},{"Name":["X","Z"],"Age":[20,30]},
           {"Name":["P","Q","R","S"],"Age":[18,18,18,18]},{"Name":["B"],"Age":[100]},
           {"Name":["John","Smith"],"Age":[21,22]},{"Name":[],"Age":[]},
           {"Name":["U","V"],"Age":[19,19]},{"Name":[],"Age":[]}]
_p2_ok = 0
for data,exp in zip(_p2_in,_p2_exp):
    try:
        res = problem_02(data)
        exp_df = pd.DataFrame(exp,columns=["Name","Age"])
        res = res.reset_index(drop=True)
        try: exp_df = exp_df.astype(res.dtypes.to_dict())
        except: pass
        if res.equals(exp_df): _p2_ok += 1
    except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas 
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
    pass

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
