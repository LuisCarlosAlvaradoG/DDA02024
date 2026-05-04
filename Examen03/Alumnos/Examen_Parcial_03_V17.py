import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V17
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Media Móvil de Ventana k
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números y un entero k (tamaño de ventana),
#   calcula la media móvil: para cada posición i >= k-1, calcula la
#   media de arr[i-k+1 : i+1]. Las primeras k-1 posiciones se omiten.
#   Retorna la lista de medias redondeadas a 2 decimales.
#   Si k > len(arr), retorna lista vacía.
#
# Entrada:  lista de números arr, entero k
# Salida:   lista de floats (medias móviles, 2 decimales)
#
# Ejemplo:
#   Entrada:  arr=[1,2,3,4,5],  k=3
#   Salida:   [2.0, 3.0, 4.0]
# ──────────────────────────────────────────────────────────

def problem_01(arr, k):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([1,2,3,4,5],3),([10,20,30],2),([5],1),([1,2,3,4],5),
           ([0,0,0,0],2),([1,3,5,7,9],2),([10,10,10,10],3),
           ([2,4,6,8,10],4),([1,2,3],3),([100,200,300,400],2)]
_p1_exp = [[2.0,3.0,4.0],[15.0,25.0],[5.0],[],
           [0.0,0.0,0.0],[2.0,4.0,6.0,8.0],[10.0,10.0],
           [5.0,7.0],[2.0],[150.0,250.0,350.0]]
_p1_ok = sum(1 for (arr,k),e in zip(_p1_in,_p1_exp) if problem_01(arr,k)==e)
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
