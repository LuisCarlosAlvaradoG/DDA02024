import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V12
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Índices del Valor más Frecuente (Máscara)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros, encuentra el valor que aparece más
#   veces (moda). En caso de empate, usa el valor más pequeño.
#   Luego, usa una máscara booleana para retornar la lista de ÍNDICES
#   donde ese valor aparece.
#
# Entrada:  lista de enteros  →  arr
# Salida:   lista de enteros (índices donde aparece la moda)
#
# Ejemplo:
#   Entrada:  [3, 1, 3, 2, 3, 1]
#   Salida:   [0, 2, 4]
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    a = np.array(arr)
    vals, counts = np.unique(a, return_counts=True)
    moda = vals[np.argmax(counts)]
    mask = a == moda
    return np.where(mask)[0].tolist()

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[3,1,3,2,3,1],[1,2,3],[5,5,5,5],[2,1,2,1,2],
           [0,0,1,1,0],[9,8,9,7,8,9],[1],[4,4,4,1,1,1],
           [2,2,3,3,4],[6,6,6,7,7,7]]
_p1_exp = [[0,2,4],[0],[0,1,2,3],[0,2,4],[0,1,4],[0,2,5],[0],
           [3,4,5],[0,1],[0,1,2]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
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
# Título: Ventas Acumuladas y Día de Meta
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Day' (strings) y 'Sales' (enteros)
#   y un entero goal:
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.cumsum) para calcular la columna 'cumulative'.
#   3. Usa una máscara booleana para encontrar el primer día en que
#      la venta acumulada supera (>) el goal.
#   4. Retorna el nombre del día (string) o "No alcanzado" si nunca
#      se supera el goal.
#
# Entrada:  dict con claves "Day" y "Sales", entero goal
# Salida:   string (nombre del día o "No alcanzado")
#
# Ejemplo:
#   Entrada: {"Day":["Lun","Mar","Mié","Jue"],"Sales":[30,40,20,50]},
#            goal=80
#   Salida:  "Mié"    # cumsum=[30,70,90,140] → 90>80 en Mié
# ──────────────────────────────────────────────────────────

def problem_03(data, goal):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    sales = df["Sales"].to_numpy()
    df["cumulative"] = np.cumsum(sales)
    mask = df["cumulative"] > goal
    if not mask.any():
        return "No alcanzado"
    return df[mask].iloc[0]["Day"]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [({"Day":["Lun","Mar","Mié","Jue"],"Sales":[30,40,20,50]},80),
          ({"Day":["D1","D2","D3"],"Sales":[10,10,10]},100),
          ({"Day":["A","B","C"],"Sales":[50,50,50]},100),
          ({"Day":["M","T","W"],"Sales":[100,100,100]},50),
          ({"Day":["X"],"Sales":[200]},100),
          ({"Day":["D1","D2","D3","D4"],"Sales":[25,25,25,25]},99),
          ({"Day":["W1","W2","W3"],"Sales":[0,0,1]},0),
          ({"Day":["P","Q","R","S"],"Sales":[10,20,30,40]},55),
          ({"Day":["U","V"],"Sales":[5,5]},100),
          ({"Day":["L","M","X","J","V"],"Sales":[20,20,20,20,20]},79)]
_p3_exp = ["Mié","No alcanzado","C","M","X","D4","W3","R","No alcanzado","J"]
_p3_ok = sum(1 for (d,g),e in zip(_p3_in,_p3_exp) if problem_03(d,g)==e)
print(f"Problema 03: {_p3_ok}/10")
