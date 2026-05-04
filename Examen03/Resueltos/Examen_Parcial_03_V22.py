import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V22
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Filtrar con Máscara Booleana
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de enteros y un umbral, usa una máscara booleana
#   de NumPy para conservar sólo los elementos estrictamente mayores al
#   umbral. Retorna la lista de esos elementos en su orden original.
#   Si ningún elemento supera el umbral, retorna lista vacía.
#
# Entrada:  lista de enteros arr, entero threshold
# Salida:   lista de enteros (elementos > threshold)
#
# Ejemplo:
#   Entrada:  arr=[3,7,2,9,1],  threshold=4
#   Salida:   [7, 9]
# ──────────────────────────────────────────────────────────

def problem_01(arr, threshold):
    # TU CÓDIGO AQUÍ
    a = np.array(arr)
    mask = a > threshold
    return a[mask].tolist()

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [([3,7,2,9,1],4),([1,2,3],10),([5,5,5],4),([0,-1,-5],-3),
           ([10,20,30],15),([],[]),([100],99),([1,1,1,1],1),
           ([-10,0,10],0),([2,4,6,8],5)]
_p1_exp = [[7,9],[],[5,5,5],[0,-1],[20,30],[],[100],[],
           [10],[6,8]]
_p1_ok = 0
for (arr,thr),exp in zip(_p1_in,_p1_exp):
    try:
        res = problem_01(arr,thr)
        if res == exp:
            _p1_ok += 1
    except: pass
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
    df = pd.DataFrame(data)
    return df.sort_values("Amount", ascending=False).head(n)["Seller"].tolist()

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
# Problema 03 — NumPy + Pandas  (mayor dificultad)
# Título: Índice Compuesto por Grupo con Normalización
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Group' (strings), 'A' y 'B'
#   (números):
#   1. Crea un DataFrame con pandas.
#   2. Usa NumPy para normalizar (min-max) las columnas 'A' y 'B'
#      globalmente (sobre todo el DataFrame).
#   3. Calcula 'index' = 0.6 * A_norm + 0.4 * B_norm (redondeado a 2).
#   4. Agrupa por 'Group' y calcula la media de 'index'.
#   5. Retorna un diccionario {group: round(mean_index, 2)}.
#
# Entrada:  dict con claves "Group", "A" y "B"
# Salida:   dict {str: float}
#
# Ejemplo:
#   Entrada: {"Group":["X","X","Y","Y"],"A":[0,10,5,15],"B":[0,0,10,10]}
#   Salida:  {"X":0.18,"Y":0.62}
# ──────────────────────────────────────────────────────────

def problem_03(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    def norm(x):
        mn,mx = x.min(), x.max()
        if mx == mn: return np.zeros(len(x))
        return (x-mn)/(mx-mn)
    a_n = norm(df["A"].to_numpy(dtype=float))
    b_n = norm(df["B"].to_numpy(dtype=float))
    df["index"] = np.round(0.6*a_n + 0.4*b_n, 2)
    return df.groupby("Group")["index"].mean().round(2).to_dict()

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_in = [{"Group":["X","X","Y","Y"],"A":[0,10,5,15],"B":[0,0,10,10]},
          {"Group":["A","B"],"A":[0,10],"B":[0,10]},
          {"Group":["M","M","N"],"A":[0,10,5],"B":[5,5,5]},
          {"Group":["P"],"A":[7],"B":[3]},
          {"Group":["G","H","G","H"],"A":[0,0,10,10],"B":[0,10,0,10]},
          {"Group":["Z","Z","Z"],"A":[5,5,5],"B":[5,5,5]},
          {"Group":["R","S","R"],"A":[0,10,20],"B":[0,5,10]},
          {"Group":["C","D","E"],"A":[0,5,10],"B":[10,5,0]},
          {"Group":["U","U","V","V"],"A":[0,0,10,10],"B":[0,10,0,10]},
          {"Group":["L","M","N","L"],"A":[0,10,20,30],"B":[30,20,10,0]}]
_p3_exp = [{"X":0.2,"Y":0.8},{"A":0.0,"B":1.0},{"M":0.3,"N":0.3},
           {"P":0.0},{"G":0.3,"H":0.7},{"Z":0.0},
           {"R":0.5,"S":0.5},{"C":0.4,"D":0.5,"E":0.6},
           {"U":0.2,"V":0.8},{"L":0.5,"M":0.47,"N":0.53}]
_p3_ok = sum(1 for i,e in zip(_p3_in,_p3_exp) if problem_03(i)==e)
print(f"Problema 03: {_p3_ok}/10")
