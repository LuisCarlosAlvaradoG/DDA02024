import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V05
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Suma por Filas de una Matriz
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D (lista de listas de enteros), usa NumPy para
#   calcular la suma de cada fila. Retorna una lista de enteros con las
#   sumas, en el mismo orden que las filas originales.
#
# Entrada:  lista de listas de enteros  →  mat
# Salida:   lista de enteros (suma de cada fila)
#
# Ejemplo:
#   Entrada:  [[1,2,3],[4,5,6]]
#   Salida:   [6, 15]
# ──────────────────────────────────────────────────────────

def problem_01(mat):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[[1,2,3],[4,5,6]],[[0,0],[0,0]],[[5]],
           [[1,2,3,4]],[[10,-10],[3,7]],[[1,1,1],[2,2,2],[3,3,3]],
           [[-1,-2],[3,4]],[[100,200,300]],[[0,1],[1,0],[1,1]],[[7,7]]]
_p1_exp = [[6,15],[0,0],[5],[10],[0,10],[3,6,9],[-3,7],[600],[1,1,2],[14]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Filtrar Clientes Frecuentes
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Client' (strings) y 'Purchases'
#   (enteros, número de compras realizadas), crea un DataFrame y retorna
#   sólo las filas donde Purchases >= 5. Índice reiniciado.
#
# Entrada:  dict con claves "Client" y "Purchases"
# Salida:   DataFrame filtrado (columnas Client, Purchases), índice reiniciado
#
# Ejemplo:
#   Entrada:  {"Client":["A","B","C"], "Purchases":[4,5,6]}
#   Salida:   DataFrame con B (5) y C (6)
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Client":["A","B","C"],"Purchases":[4,5,6]},
           {"Client":["Tom"],"Purchases":[5]},
           {"Client":["Anna","Ben"],"Purchases":[1,2]},
           {"Client":["X","Y","Z"],"Purchases":[10,3,8]},
           {"Client":["P","Q","R","S"],"Purchases":[5,5,5,5]},
           {"Client":["A","B"],"Purchases":[0,100]},
           {"Client":["John","Doe","Smith"],"Purchases":[6,4,7]},
           {"Client":["M","N","O"],"Purchases":[1,2,3]},
           {"Client":["U","V","W"],"Purchases":[4,5,5]},
           {"Client":["K"],"Purchases":[0]}]
_p2_exp = [{"Client":["B","C"],"Purchases":[5,6]},{"Client":["Tom"],"Purchases":[5]},
           {"Client":[],"Purchases":[]},{"Client":["X","Z"],"Purchases":[10,8]},
           {"Client":["P","Q","R","S"],"Purchases":[5,5,5,5]},{"Client":["B"],"Purchases":[100]},
           {"Client":["John","Smith"],"Purchases":[6,7]},{"Client":[],"Purchases":[]},
           {"Client":["V","W"],"Purchases":[5,5]},{"Client":[],"Purchases":[]}]
_p2_ok = 0
for data,exp in zip(_p2_in,_p2_exp):
    try:
        res = problem_02(data)
        exp_df = pd.DataFrame(exp,columns=["Client","Purchases"])
        res = res.reset_index(drop=True)
        try: exp_df = exp_df.astype(res.dtypes.to_dict())
        except: pass
        if res.equals(exp_df): _p2_ok += 1
    except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  
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
    pass

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
