import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V08
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
    pass

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
# Título: Normalizar y Agrupar por Segmento
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Segment' (strings) y 'Value'
#   (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy para calcular la normalización min-max de 'Value'
#      y agrégala como columna 'norm' (redondeada a 2 dec).
#   3. Agrupa por 'Segment' y calcula la media de 'norm' por grupo.
#   4. Retorna un diccionario {segment: round(mean_norm, 2)}.
#
# Entrada:  dict con claves "Segment" y "Value"
# Salida:   dict {str: float}
#
# Ejemplo:
#   Entrada: {"Segment":["A","A","B","B"],"Value":[0,10,5,15]}
#   Salida:  {"A":0.25,"B":0.67}
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    pass

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Segment":["A","A","B","B"],"Value":[0,10,5,15]},
          {"Segment":["X","Y"],"Value":[1,1]},
          {"Segment":["M","N","M","N"],"Value":[0,5,10,15]},
          {"Segment":["A","A","A"],"Value":[2,4,6]},
          {"Segment":["P","Q","P","Q"],"Value":[0,0,10,10]},
          {"Segment":["G","H","G"],"Value":[1,3,5]},
          {"Segment":["Z","Z"],"Value":[0,100]},
          {"Segment":["R","S","R"],"Value":[10,20,30]},
          {"Segment":["C","D","E"],"Value":[0,50,100]},
          {"Segment":["U","U","V","V"],"Value":[5,15,10,20]}]
_p3_exp = [{"A":0.34,"B":0.66},{"X":0.0,"Y":0.0},{"M":0.34,"N":0.66},
           {"A":0.5},{"P":0.5,"Q":0.5},{"G":0.5,"H":0.5},
           {"Z":0.5},{"R":0.5,"S":0.5},{"C":0.0,"D":0.5,"E":1.0},
           {"U":0.34,"V":0.66}]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
