import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V09
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
# Título: Tabla Pivote de Promedios
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings), 'Quarter'
#   (strings, p.ej. "Q1") y 'Revenue' (números), crea un DataFrame y
#   construye una tabla pivote con pd.pivot_table donde:
#     - index = 'Region'
#     - columns = 'Quarter'
#     - values = 'Revenue'
#     - aggfunc = 'mean'
#   Retorna el DataFrame resultante (tabla pivote).
#
# Entrada:  dict con claves "Region", "Quarter", "Revenue"
# Salida:   DataFrame (tabla pivote)
#
# Ejemplo:
#   Entrada:  {"Region":["N","N","S"],"Quarter":["Q1","Q2","Q1"],
#              "Revenue":[100,200,150]}
#   Salida:   pivot con N→Q1=100,Q2=200 y S→Q1=150
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    return pd.pivot_table(df, values="Revenue", index="Region",
                          columns="Quarter", aggfunc="mean")

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in = [{"Region":["N","N","S"],"Quarter":["Q1","Q2","Q1"],"Revenue":[100,200,150]},
          {"Region":["E","W","E","W"],"Quarter":["Q1","Q1","Q2","Q2"],"Revenue":[10,20,30,40]},
          {"Region":["A"],"Quarter":["Q1"],"Revenue":[50]},
          {"Region":["X","X"],"Quarter":["Q1","Q1"],"Revenue":[10,20]},
          {"Region":["N","S","E","W"],"Quarter":["Q1","Q1","Q1","Q1"],"Revenue":[1,2,3,4]}]
_p2_ok = 0
for data in _p2_in:
    try:
        res = problem_02(data)
        if isinstance(res, pd.DataFrame): _p2_ok += 2
    except: pass
_p2_ok = min(_p2_ok, 10)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
# Título: Categorizar Ventas con Máscara y Resumir
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Region' (strings) y 'Sales' (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy (np.where) para agregar columna 'Category':
#        "ALTA"  si Sales >= 200
#        "MEDIA" si Sales >= 100 (y < 200)
#        "BAJA"  si Sales < 100
#   3. Agrupa por 'Category' y cuenta cuántas filas hay en cada categoría.
#   4. Retorna un diccionario {category: count}.
#
# Entrada:  dict con claves "Region" y "Sales"
# Salida:   dict {str: int}  (sólo categorías presentes)
#
# Ejemplo:
#   Entrada: {"Region":["N","S","E","W"],"Sales":[50,150,250,80]}
#   Salida:  {"BAJA":2,"MEDIA":1,"ALTA":1}
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    s = df["Sales"].to_numpy(dtype=float)
    df["Category"] = np.where(s >= 200,"ALTA", np.where(s >= 100,"MEDIA","BAJA"))
    counts = df.groupby("Category")["Category"].count()
    return {k:int(v) for k,v in counts.items()}

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Region":["N","S","E","W"],"Sales":[50,150,250,80]},
          {"Region":["A"],"Sales":[200]},
          {"Region":["B","C"],"Sales":[99,100]},
          {"Region":["D","E","F"],"Sales":[0,199,200]},
          {"Region":["G","H","I","J"],"Sales":[100,100,200,200]},
          {"Region":["K"],"Sales":[50]},
          {"Region":["L","M"],"Sales":[200,200]},
          {"Region":["N","O","P"],"Sales":[100,150,200]},
          {"Region":["Q","R"],"Sales":[0,0]},
          {"Region":["S","T","U","V"],"Sales":[50,150,250,350]}]
_p3_exp = [{"ALTA":1,"BAJA":2,"MEDIA":1},{"ALTA":1},{"BAJA":1,"MEDIA":1},
           {"ALTA":1,"BAJA":1,"MEDIA":1},{"ALTA":2,"MEDIA":2},{"BAJA":1},
           {"ALTA":2},{"ALTA":1,"MEDIA":2},{"BAJA":2},{"ALTA":2,"BAJA":1,"MEDIA":1}]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
