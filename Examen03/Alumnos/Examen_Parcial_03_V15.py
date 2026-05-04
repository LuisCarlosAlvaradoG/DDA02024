import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V15
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Clasificación en Tres Categorías con np.where
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros (calificaciones 0–100) y dos umbrales
#   (bajo y alto), clasifica cada elemento:
#     - "BAJO"   si valor < bajo
#     - "MEDIO"  si bajo <= valor < alto
#     - "ALTO"   si valor >= alto
#   Usa np.where anidado o condiciones con NumPy.
#   Retorna una lista de strings.
#
# Entrada:  lista de enteros arr, enteros bajo y alto
# Salida:   lista de strings ("BAJO", "MEDIO" o "ALTO")
#
# Ejemplo:
#   Entrada:  arr=[30,60,90],  bajo=50,  alto=80
#   Salida:   ["BAJO", "MEDIO", "ALTO"]
# ──────────────────────────────────────────────────────────

def problem_01(arr, bajo, alto):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([30,60,90],50,80),([0,50,100],50,80),([50,80],50,80),
           ([10,20,30],20,25),([100,100,100],50,80),([0],50,80),
           ([49,50,79,80],50,80),([25,75],50,100),([60],50,80),
           ([1,51,81,100],50,80)]
_p1_exp = [["BAJO","MEDIO","ALTO"],["BAJO","MEDIO","ALTO"],["MEDIO","ALTO"],
           ["BAJO","MEDIO","ALTO"],["ALTO","ALTO","ALTO"],["BAJO"],
           ["BAJO","MEDIO","MEDIO","ALTO"],["BAJO","MEDIO"],["MEDIO"],
           ["BAJO","MEDIO","ALTO","ALTO"]]
_p1_ok = sum(1 for (arr,b,a),e in zip(_p1_in,_p1_exp) if problem_01(arr,b,a)==e)
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
