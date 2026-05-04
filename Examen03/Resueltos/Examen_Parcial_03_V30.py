import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V30
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
# Título: Clasificar Ventas con Columna Derivada
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Product' (strings) y 'Sales'
#   (enteros), crea un DataFrame, agrega una columna 'Status' con el
#   valor "ALTO" si Sales >= 100 y "BAJO" en otro caso, y retorna el
#   DataFrame completo (con las tres columnas). Índice reiniciado.
#
# Entrada:  dict con claves "Product" y "Sales"
# Salida:   DataFrame con columnas Product, Sales, Status
#
# Ejemplo:
#   Entrada:  {"Product":["A","B"], "Sales":[80,120]}
#   Salida:   DataFrame con Status ["BAJO","ALTO"]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    df["Status"] = np.where(df["Sales"] >= 100, "ALTO", "BAJO")
    return df.reset_index(drop=True)

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Product":["A","B"],"Sales":[80,120]},
           {"Product":["X"],"Sales":[100]},
           {"Product":["P","Q","R"],"Sales":[50,100,200]},
           {"Product":["M","N"],"Sales":[0,99]},
           {"Product":["Z"],"Sales":[101]},
           {"Product":["C","D","E","F"],"Sales":[100,100,99,101]},
           {"Product":["G"],"Sales":[0]},
           {"Product":["H","I"],"Sales":[200,50]},
           {"Product":["J","K","L"],"Sales":[99,100,101]},
           {"Product":["W"],"Sales":[100]}]
_p2_exp_status = [["BAJO","ALTO"],["ALTO"],["BAJO","ALTO","ALTO"],["BAJO","BAJO"],
                  ["ALTO"],["ALTO","ALTO","BAJO","ALTO"],["BAJO"],["ALTO","BAJO"],
                  ["BAJO","ALTO","ALTO"],["ALTO"]]
_p2_ok = 0
for data,exp_s in zip(_p2_in,_p2_exp_status):
    try:
        res = problem_02(data)
        if isinstance(res,pd.DataFrame) and "Status" in res.columns and res["Status"].tolist()==exp_s:
            _p2_ok += 1
    except: pass
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
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
    df = pd.DataFrame(data)
    scores = df["Score"].to_numpy(dtype=float)
    sd = scores.std()
    if sd == 0:
        df["zscore"] = 0.0
    else:
        df["zscore"] = np.round((scores - scores.mean())/sd, 2)
    return df.sort_values("zscore", ascending=False).head(n)["Item"].tolist()

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
