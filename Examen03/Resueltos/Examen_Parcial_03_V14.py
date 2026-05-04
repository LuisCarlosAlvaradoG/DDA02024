import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V14
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Rango por Filas (Max - Min)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D de enteros, calcula el rango (max - min) de cada
#   fila usando NumPy. Retorna una lista de enteros, uno por fila.
#
# Entrada:  lista de listas de enteros  →  mat
# Salida:   lista de enteros (rango de cada fila)
#
# Ejemplo:
#   Entrada:  [[1,5,3],[10,2,8]]
#   Salida:   [4, 8]
# ──────────────────────────────────────────────────────────

def problem_01(mat):
    # TU CÓDIGO AQUÍ
    a = np.array(mat)
    return (a.max(axis=1) - a.min(axis=1)).tolist()

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[[1,5,3],[10,2,8]],[[0,0],[0,0]],[[5]],
           [[1,2,3,4]],[[10,-10],[3,7]],[[1,1,1],[2,2,2]],
           [[-5,5]],[[100,1]],[[3,3,3,10]],[[1,2],[3,5],[6,9]]]
_p1_exp = [[4,8],[0,0],[0],[3],[20,4],[0,0],[10],[99],[7],[1,2,3]]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Unir Tablas y Eliminar Duplicados (concat)
# ──────────────────────────────────────────────────────────
# Descripción:
#   Se reciben dos diccionarios con claves 'ID' (enteros) y 'Name'
#   (strings). Crea un DataFrame por cada uno, únelos verticalmente con
#   pd.concat, elimina filas con 'ID' duplicado (queda la primera
#   aparición) y retorna la lista de IDs resultantes.
#
# Entrada:  dict df1, dict df2  (ambos con claves "ID" y "Name")
# Salida:   lista de enteros (IDs únicos en orden de aparición)
#
# Ejemplo:
#   df1 = {"ID":[1,2],"Name":["Ana","Luis"]}
#   df2 = {"ID":[2,3],"Name":["Luis","Marta"]}
#   Salida:   [1, 2, 3]
# ──────────────────────────────────────────────────────────

def problem_02(d1, d2):
    # TU CÓDIGO AQUÍ
    df = pd.concat([pd.DataFrame(d1), pd.DataFrame(d2)], ignore_index=True)
    return df.drop_duplicates(subset="ID", keep="first")["ID"].tolist()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_d1 = [{"ID":[1,2],"Name":["Ana","Luis"]},
          {"ID":[10,20],"Name":["A","B"]},
          {"ID":[1],"Name":["X"]},
          {"ID":[5,6,7],"Name":["P","Q","R"]},
          {"ID":[1,2,3],"Name":["A","B","C"]},
          {"ID":[100],"Name":["Z"]},
          {"ID":[1,2],"Name":["M","N"]},
          {"ID":[9,8],"Name":["U","V"]},
          {"ID":[3,4],"Name":["G","H"]},
          {"ID":[1,1],"Name":["D","D"]}]
_p2_d2 = [{"ID":[2,3],"Name":["Luis","Marta"]},
          {"ID":[20,30],"Name":["B","C"]},
          {"ID":[1,2],"Name":["X","Y"]},
          {"ID":[7,8],"Name":["R","S"]},
          {"ID":[4,5],"Name":["D","E"]},
          {"ID":[200],"Name":["W"]},
          {"ID":[3,2],"Name":["O","N"]},
          {"ID":[8,7],"Name":["V","T"]},
          {"ID":[4,5],"Name":["H","I"]},
          {"ID":[2,3],"Name":["E","F"]}]
_p2_exp = [[1,2,3],[10,20,30],[1,2],[5,6,7,8],[1,2,3,4,5],
           [100,200],[1,2,3],[9,8,7],[3,4,5],[1,2,3]]
_p2_ok = sum(1 for d1,d2,e in zip(_p2_d1,_p2_d2,_p2_exp) if problem_02(d1,d2)==e)
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
