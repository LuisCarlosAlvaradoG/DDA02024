import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V23
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
# Título: Combinar Tablas y Sumar por Cliente (merge + groupby)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Se reciben dos diccionarios:
#     orders: claves "order_id", "client_id", "amount"
#     clients: claves "client_id", "name"
#   Crea un DataFrame por cada uno, realiza un merge inner por
#   "client_id" y calcula la suma total de "amount" agrupada por
#   "name". Retorna un diccionario {name: total_amount}.
#
# Entrada:  dict orders, dict clients
# Salida:   dict {str: número}
#
# Ejemplo:
#   orders  = {"order_id":[1,2,3],"client_id":[10,10,20],"amount":[50,30,80]}
#   clients = {"client_id":[10,20],"name":["Ana","Luis"]}
#   Salida:   {"Ana":80, "Luis":80}
# ──────────────────────────────────────────────────────────

def problem_02(orders, clients):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_orders = [{"order_id":[1,2,3],"client_id":[10,10,20],"amount":[50,30,80]},
              {"order_id":[1],"client_id":[1],"amount":[100]},
              {"order_id":[1,2],"client_id":[1,2],"amount":[200,300]},
              {"order_id":[1,2,3,4],"client_id":[1,1,2,2],"amount":[10,20,30,40]},
              {"order_id":[1,2],"client_id":[99,99],"amount":[5,5]},
              {"order_id":[1,2,3],"client_id":[1,2,3],"amount":[100,200,300]},
              {"order_id":[1,2],"client_id":[1,2],"amount":[50,50]},
              {"order_id":[1,2,3],"client_id":[1,1,1],"amount":[10,10,10]},
              {"order_id":[1,2],"client_id":[1,2],"amount":[0,0]},
              {"order_id":[1,2,3],"client_id":[1,2,1],"amount":[100,200,50]}]
_p2_clients= [{"client_id":[10,20],"name":["Ana","Luis"]},
              {"client_id":[1],"name":["Tom"]},
              {"client_id":[1,2],"name":["A","B"]},
              {"client_id":[1,2],"name":["X","Y"]},
              {"client_id":[99],"name":["Z"]},
              {"client_id":[1,2,3],"name":["P","Q","R"]},
              {"client_id":[1,2],"name":["M","N"]},
              {"client_id":[1],"name":["Solo"]},
              {"client_id":[1,2],"name":["U","V"]},
              {"client_id":[1,2],"name":["Alpha","Beta"]}]
_p2_exp = [{"Ana":80,"Luis":80},{"Tom":100},{"A":200,"B":300},{"X":30,"Y":70},
           {"Z":10},{"P":100,"Q":200,"R":300},{"M":50,"N":50},{"Solo":30},
           {"U":0,"V":0},{"Alpha":150,"Beta":200}]
_p2_ok = sum(1 for o,c,e in zip(_p2_orders,_p2_clients,_p2_exp) if problem_02(o,c)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  
# Título: Moda Global y Frecuencia Relativa por Región
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings) y 'Rating'
#   (enteros del 1 al 5):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.unique con return_counts) para encontrar el
#      Rating que aparece más veces en todo el dataset (moda global).
#      En empate, usa el valor más pequeño.
#   3. Usa una máscara booleana de NumPy para filtrar las filas cuyo
#      Rating == moda global.
#   4. Cuenta cuántas filas quedan por Region en ese subconjunto
#      (usando pandas value_counts).
#   5. Retorna una tupla (moda, dict{region: count}).
#
# Entrada:  dict con claves "Region" y "Rating"
# Salida:   tupla (int, dict{str:int})
#
# Ejemplo:
#   Entrada: {"Region":["N","S","N","E","S","N"],"Rating":[5,3,5,3,5,3]}
#   moda=5  →  filas con Rating==5: N×2, S×1
#   Salida: (5, {"N":2,"S":1})
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Region":["N","S","N","E","S","N"],"Rating":[5,3,5,3,5,3]},
          {"Region":["A","B","A"],"Rating":[1,2,1]},
          {"Region":["X","Y","Z"],"Rating":[3,3,3]},
          {"Region":["M","N"],"Rating":[4,5]},
          {"Region":["P","Q","P","Q","P"],"Rating":[2,2,2,3,3]},
          {"Region":["G","H","G"],"Rating":[1,1,2]},
          {"Region":["R","S","T","R"],"Rating":[5,4,5,4]},
          {"Region":["U","V","U","V"],"Rating":[3,3,4,4]},
          {"Region":["C","D","C","D","C"],"Rating":[2,3,2,2,3]},
          {"Region":["L","M","N","L"],"Rating":[1,2,1,3]}]
_p3_exp = [(3,{"S":1,"E":1,"N":1}),(1,{"A":2}),(3,{"X":1,"Y":1,"Z":1}),
           (4,{"M":1}),(2,{"P":2,"Q":1}),(1,{"G":1,"H":1}),
           (4,{"S":1,"R":1}),(3,{"U":1,"V":1}),
           (2,{"C":2,"D":1}),(1,{"L":1,"N":1})]
_p3_ok = 0
for i,e in zip(_p3_in,_p3_exp):
    try:
        r = problem_03(i)
        if r[0]==e[0] and r[1]==e[1]: _p3_ok+=1
    except: pass
print(f"Problema 03: {_p3_ok}/10")
