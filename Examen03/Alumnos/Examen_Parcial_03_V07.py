import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V07
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Producto Punto entre Vectores
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dados dos arreglos 1-D de igual longitud, calcula su producto punto
#   usando NumPy (np.dot(a, b)). Retorna el resultado como float redondeado
#   a 2 decimales.
#
# Entrada:  listas de números  →  a, b   (misma longitud)
# Salida:   float (producto punto, 2 decimales)
#
# Ejemplo:
#   Entrada:  a=[1,2,3],  b=[4,5,6]
#   Salida:   32.0        # 1*4 + 2*5 + 3*6
# ──────────────────────────────────────────────────────────

def problem_01(a, b):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([1,2,3],[4,5,6]),([0,0,0],[1,2,3]),([1,1,1],[1,1,1]),
           ([2,4],[3,5]),([1,0],[0,1]),([3,3,3],[1,1,1]),
           ([-1,2,-3],[4,-5,6]),([10,20],[0.5,0.5]),([1,2,3,4],[4,3,2,1]),
           ([5,5],[2,2])]
_p1_exp = [32.0,0.0,3.0,26.0,0.0,9.0,-32.0,15.0,20.0,20.0]
_p1_ok = sum(1 for (a,b),e in zip(_p1_in,_p1_exp) if problem_01(a,b)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Top Vendedores por Monto
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Seller' (strings) y 'Amount'
#   (números), crea un DataFrame, ordena de mayor a menor por 'Amount'
#   y retorna una lista con los nombres de los primeros n vendedores.
#
# Entrada:  dict con claves "Seller" y "Amount", entero n
# Salida:   lista de strings (nombres de los top-n vendedores)
#
# Ejemplo:
#   Entrada:  {"Seller":["Ana","Bob","Lia"], "Amount":[200,350,150]}, n=2
#   Salida:   ["Bob","Ana"]
# ──────────────────────────────────────────────────────────

def problem_02(data, n):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [({"Seller":["Ana","Bob","Lia"],"Amount":[200,350,150]},2),
           ({"Seller":["X","Y","Z"],"Amount":[100,200,300]},1),
           ({"Seller":["A","B","C"],"Amount":[50,50,50]},3),
           ({"Seller":["M"],"Amount":[999]},1),
           ({"Seller":["P","Q","R","S"],"Amount":[10,40,30,20]},2),
           ({"Seller":["G","H"],"Amount":[0,0]},1),
           ({"Seller":["D","E","F"],"Amount":[300,100,200]},3),
           ({"Seller":["U","V","W"],"Amount":[5,15,10]},2),
           ({"Seller":["L","M","N","O"],"Amount":[1,4,3,2]},3),
           ({"Seller":["T"],"Amount":[42]},1)]
_p2_exp = [["Bob","Ana"],["Z"],["A","B","C"],["M"],["Q","R"],["G"],
           ["D","F","E"],["V","W"],["M","N","O"],["T"]]
_p2_ok = sum(1 for (d,n),e in zip(_p2_in,_p2_exp) if problem_02(d,n)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas
# Título: Detectar Outliers con Z-Score y Pandas
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Product' (strings) y 'Price'
#   (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy para calcular el z-score de la columna 'Price'.
#   3. Agrega la columna 'zscore' al DataFrame (redondeada a 2 dec).
#   4. Usa una máscara booleana para filtrar las filas donde
#      abs(zscore) >= 2.0 (outliers).
#   5. Retorna la lista de productos identificados como outliers.
#
# Entrada:  dict con claves "Product" y "Price"
# Salida:   lista de strings (productos outliers, en orden original)
#
# Ejemplo:
#   Entrada: {"Product":["A","B","C","D","E"],"Price":[5,5,5,5,50]}
#   Salida:  ["E"]      # 50 tiene z-score >= 2
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Product":["A","B","C","D","E"],"Price":[5,5,5,5,50]},
          {"Product":["X","Y","Z"],"Price":[50,50,50]},
          {"Product":["P","Q","R","S","T"],"Price":[1,2,2,2,50]},
          {"Product":["M","N"],"Price":[100,200]},
          {"Product":["G","H","I","J","K"],"Price":[10,10,10,10,100]},
          {"Product":["A","B","C"],"Price":[1,2,3]},
          {"Product":["U","V","W","X","Y"],"Price":[5,5,5,5,50]},
          {"Product":["L","M","N","O"],"Price":[100,105,95,500]},
          {"Product":["D","E","F"],"Price":[20,21,22]},
          {"Product":["C1","C2","C3","C4","C5"],"Price":[10,10,10,10,200]}]
_p3_exp = [["E"],[],["T"],[],["K"],[],["Y"],[],[],["C5"]]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
