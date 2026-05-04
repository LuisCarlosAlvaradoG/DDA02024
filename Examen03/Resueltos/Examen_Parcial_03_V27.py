import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V27
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Suma Acumulada y Punto de Cruce
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros positivos y un umbral, calcula la
#   suma acumulada con np.cumsum y retorna el ÍNDICE (base 0) del primer
#   elemento donde la suma acumulada supera el umbral.
#   Si la suma total nunca supera el umbral, retorna -1.
#
# Entrada:  lista de enteros arr, entero threshold
# Salida:   entero (índice del primer cruce, o -1)
#
# Ejemplo:
#   Entrada:  arr=[10,20,30,40],  threshold=35
#   Salida:   2       # cumsum=[10,30,60,100] → índice 2 supera 35
# ──────────────────────────────────────────────────────────

def problem_01(arr, threshold):
    # TU CÓDIGO AQUÍ
    a = np.array(arr)
    cs = np.cumsum(a)
    mask = cs > threshold
    if not mask.any():
        return -1
    return int(np.argmax(mask))

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([10,20,30,40],35),([1,1,1,1,1],3),([100],50),
           ([5,5,5],100),([1,2,3,4,5],10),([10,10,10],25),
           ([50,50],40),([1,1,1,1,1,1,1,1,1,1],8),([7,3,5],9),([20,5,5],19)]
_p1_exp = [2,3,0,-1,4,2,0,8,1,0]
_p1_ok = sum(1 for (arr,thr),e in zip(_p1_in,_p1_exp) if problem_01(arr,thr)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Clasificar Edades en Rangos con pd.cut
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con clave 'Age' (lista de enteros), crea una
#   Serie de pandas y usa pd.cut para clasificar cada edad en los
#   siguientes rangos (etiquetas dadas):
#     [0, 17]  → "Menor"
#     [18, 64] → "Adulto"
#     [65, 120]→ "Mayor"
#   Retorna un diccionario {etiqueta: conteo} con los totales por
#   categoría. Sólo incluye etiquetas con conteo > 0.
#
# Entrada:  dict con clave "Age" (lista de enteros)
# Salida:   dict {str: int}
#
# Ejemplo:
#   Entrada:  {"Age":[10,20,70,30,15]}
#   Salida:   {"Menor":2,"Adulto":2,"Mayor":1}
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    s = pd.Series(data["Age"])
    bins = [0, 17, 64, 120]
    labels = ["Menor","Adulto","Mayor"]
    cats = pd.cut(s, bins=bins, labels=labels, include_lowest=True)
    counts = cats.value_counts()
    return {k:int(v) for k,v in counts.items() if v > 0}

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in = [{"Age":[10,20,70,30,15]},
          {"Age":[18,64,65]},{"Age":[0,17,120]},
          {"Age":[25,35,45]},{"Age":[66,70,80,90]},
          {"Age":[17,18]},{"Age":[64,65]},
          {"Age":[10,10,10]},{"Age":[50,50,50,50]},
          {"Age":[1,18,65]}]
_p2_exp = [{"Menor":2,"Adulto":2,"Mayor":1},
           {"Adulto":2,"Mayor":1},{"Menor":2,"Mayor":1},
           {"Adulto":3},{"Mayor":4},
           {"Menor":1,"Adulto":1},{"Adulto":1,"Mayor":1},
           {"Menor":3},{"Adulto":4},
           {"Menor":1,"Adulto":1,"Mayor":1}]
_p2_ok = sum(1 for i,e in zip(_p2_in,_p2_exp) if problem_02(i)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
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
    df = pd.DataFrame(data)
    prices = df["Price"].to_numpy(dtype=float)
    sd = prices.std()
    if sd == 0:
        return []
    z = (prices - prices.mean()) / sd
    df["zscore"] = np.round(z, 2)
    mask = np.abs(df["zscore"]) >= 2.0
    return df[mask]["Product"].tolist()

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
