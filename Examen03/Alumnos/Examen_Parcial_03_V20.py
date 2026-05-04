import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V20
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Estandarización Z-Score
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros, estandariza sus valores con z-score:
#       z = (x - media) / desv_std
#   Usa desviación estándar poblacional (ddof=0).
#   Si la desviación estándar es 0, retorna una lista de ceros.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de floats redondeados a 2 decimales
#
# Ejemplo:
#   Entrada:  [1, 2, 3]
#   Salida:   [-1.22, 0.0, 1.22]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,2,3],[5,5,5],[0,10,20],[-1,0,1],[100,200,300,400],
           [3,3,6,9],[7],[2,4,6,8,10],[10,0,10,0],[5,15,25]]
_p1_exp = [[-1.22,0.0,1.22],[0.0,0.0,0.0],[-1.22,0.0,1.22],[-1.22,0.0,1.22],
           [-1.34,-0.45,0.45,1.34],[-0.9,-0.9,0.3,1.51],[0.0],
           [-1.41,-0.71,0.0,0.71,1.41],[1.0,-1.0,1.0,-1.0],[-1.22,0.0,1.22]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if np.all(np.round(np.array(problem_01(i),dtype=float),2)==np.array(e)))
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Top-N Valores más Frecuentes
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con clave 'Category' (lista de strings) y un
#   entero n, crea una Serie de pandas, aplica value_counts y retorna
#   una lista con los n valores más frecuentes (sólo los nombres,
#   en orden descendente de frecuencia). En caso de empate, el orden
#   es el que pandas devuelva naturalmente.
#
# Entrada:  dict con clave "Category" (lista de strings), entero n
# Salida:   lista de strings (los n más frecuentes)
#
# Ejemplo:
#   Entrada:  {"Category":["A","B","A","C","B","A"]},  n=2
#   Salida:   ["A","B"]
# ──────────────────────────────────────────────────────────

def problem_02(data, n):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [({"Category":["A","B","A","C","B","A"]},2),
           ({"Category":["X","X","X","Y","Y"]},1),
           ({"Category":["M","N","M","N","M","N"]},2),
           ({"Category":["Z"]},1),
           ({"Category":["A","B","C","A","B","A"]},3),
           ({"Category":["P","Q","P","Q","P"]},1),
           ({"Category":["R","S","T","R","S","R"]},2),
           ({"Category":["U","U","V","V","W"]},2),
           ({"Category":["A","A","B","B","C","C","D"]},1),
           ({"Category":["X","Y","X","Y","X","Y"]},2)]
_p2_exp = [["A","B"],["X"],["M","N"],["Z"],["A","B","C"],["P"],
           ["R","S"],["U","V"],["A"],["X","Y"]]
_p2_ok = sum(1 for (d,n),e in zip(_p2_in,_p2_exp) if problem_02(d,n)==e)
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
