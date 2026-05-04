import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V10
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Rectificación (ReLU) con Máscara
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números, aplica la función ReLU:
#   sustituye todos los valores negativos por 0.0 (los positivos y
#   ceros se conservan). Usa una máscara booleana de NumPy.
#   Retorna una lista de floats redondeados a 2 decimales.
#
# Entrada:  lista de números  →  arr
# Salida:   lista de floats (valores rectificados, 2 decimales)
#
# Ejemplo:
#   Entrada:  [-3, 0, 5, -1, 2]
#   Salida:   [0.0, 0.0, 5.0, 0.0, 2.0]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[-3,0,5,-1,2],[1,2,3],[0,0,0],[-1,-2,-3],[-5,10,-15,20],
           [0.5,-0.5,1.5],[100,-100],[3.14,-2.72,0],[0,-0.01,0.01],[-7,-7,-7]]
_p1_exp = [[0.0,0.0,5.0,0.0,2.0],[1.0,2.0,3.0],[0.0,0.0,0.0],
           [0.0,0.0,0.0],[0.0,10.0,0.0,20.0],[0.5,0.0,1.5],
           [100.0,0.0],[3.14,0.0,0.0],[0.0,0.0,0.01],[0.0,0.0,0.0]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Eliminar Duplicados por Columna Clave
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'ID' (enteros) y 'Value' (números),
#   crea un DataFrame y elimina filas con 'ID' duplicado conservando la
#   PRIMERA aparición (keep='first'). Retorna la lista de IDs únicos
#   en el orden resultante.
#
# Entrada:  dict con claves "ID" y "Value"
# Salida:   lista de enteros (IDs únicos, en orden de primera aparición)
#
# Ejemplo:
#   Entrada:  {"ID":[1,2,1,3], "Value":[10,20,30,40]}
#   Salida:   [1, 2, 3]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"ID":[1,2,1,3],"Value":[10,20,30,40]},
           {"ID":[5,5,5],"Value":[1,2,3]},
           {"ID":[1,2,3],"Value":[4,5,6]},
           {"ID":[10,20,10,30,20],"Value":[0,0,0,0,0]},
           {"ID":[1],"Value":[100]},
           {"ID":[3,2,1,3,2,1],"Value":[1,1,1,1,1,1]},
           {"ID":[7,8,9,7,8],"Value":[0,0,0,0,0]},
           {"ID":[4,4,4,4],"Value":[1,2,3,4]},
           {"ID":[1,2,1,2,3],"Value":[5,6,7,8,9]},
           {"ID":[100,200,100],"Value":[1,2,3]}]
_p2_exp = [[1,2,3],[5],[1,2,3],[10,20,30],[1],[3,2,1],[7,8,9],[4],[1,2,3],[100,200]]
_p2_ok = sum(1 for i,e in zip(_p2_in,_p2_exp) if problem_02(i)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas 
# Título: Top-N Filas por Z-Score Más Alto
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Item' (strings) y 'Score' (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy para calcular el z-score de 'Score' (ddof=0).
#   3. Agrega la columna 'zscore' al DataFrame (redondeada a 2 dec).
#   4. Ordena de mayor a menor por 'zscore'.
#   5. Retorna la lista de los nombres de los primeros n ítems
#      (los de z-score más alto).
#   Si std == 0, retorna los primeros n ítems en el orden original.
#
# Entrada:  dict con claves "Item" y "Score", entero n
# Salida:   lista de strings (top-n ítems por z-score)
#
# Ejemplo:
#   Entrada: {"Item":["A","B","C","D"],"Score":[10,50,30,20]}, n=2
#   Salida:  ["B","C"]
# ──────────────────────────────────────────────────────────

def problem_03(data, n):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [({"Item":["A","B","C","D"],"Score":[10,50,30,20]},2),
          ({"Item":["X","Y","Z"],"Score":[1,2,3]},1),
          ({"Item":["P","Q"],"Score":[5,5]},1),
          ({"Item":["M","N","O","P"],"Score":[0,0,0,100]},1),
          ({"Item":["G","H","I"],"Score":[100,200,300]},3),
          ({"Item":["A","B","C"],"Score":[3,2,1]},2),
          ({"Item":["U","V","W","X"],"Score":[10,40,20,30]},3),
          ({"Item":["D","E"],"Score":[50,100]},1),
          ({"Item":["R","S","T"],"Score":[7,7,7]},2),
          ({"Item":["L","M","N","O","P"],"Score":[1,5,3,4,2]},3)]
_p3_exp = [["B","C"],["Z"],["P"],["P"],["I","H","G"],["A","B"],
           ["V","X","W"],["E"],["R","S"],["M","O","N"]]
_p3_ok = sum(1 for (d,n),e in zip(_p3_in,_p3_exp) if problem_03(d,n)==e)
print(f"Problema 03: {_p3_ok}/10")
