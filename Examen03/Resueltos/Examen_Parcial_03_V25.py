import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V25
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
#   usando NumPy (np.dot). Retorna el resultado como float redondeado
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
    return round(float(np.dot(np.array(a, dtype=float), np.array(b, dtype=float))), 2)

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
# Título: Eliminar Duplicados por Columna Clave
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'ID' (enteros) y 'Value' (números),
#   crea un DataFrame y elimina filas con 'ID' duplicado conservando la
#   PRIMERA aparición (keep='first'). Retorna la lista de IDs únicos
#   en el orden resultante.
#
# Entrada:  dict con claves "ID" y "Value"
# Salida:   lista de enteros (IDs únicos, en orden de primera aparición)
#
# Ejemplo:
#   Entrada:  {"ID":[1,2,1,3], "Value":[10,20,30,40]}
#   Salida:   [1, 2, 3]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    return df.drop_duplicates(subset="ID", keep="first")["ID"].tolist()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"ID":[1,2,1,3],"Value":[10,20,30,40]},
           {"ID":[5,5,5],"Value":[1,2,3]},
           {"ID":[1,2,3],"Value":[4,5,6]},
           {"ID":[10,20,10,30,20],"Value":[0,0,0,0,0]},
           {"ID":[1],"Value":[100]},
           {"ID":[3,2,1,3,2,1],"Value":[1,1,1,1,1,1]},
           {"ID":[7,8,9,7,8],"Value":[0,0,0,0,0]},
           {"ID":[4,4,4,4],"Value":[1,2,3,4]},
           {"ID":[1,2,1,2,3],"Value":[5,6,7,8,9]},
           {"ID":[100,200,100],"Value":[1,2,3]}]
_p2_exp = [[1,2,3],[5],[1,2,3],[10,20,30],[1],[3,2,1],[7,8,9],[4],[1,2,3],[100,200]]
_p2_ok = sum(1 for i,e in zip(_p2_in,_p2_exp) if problem_02(i)==e)
print(f"Problema 02: {_p2_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 03 — NumPy + Pandas  (mayor dificultad)
# Título: Filtrar Filas por Promedio de Fila
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dada una matriz 2-D y un umbral numérico:
#   1. Usa NumPy para calcular la media de cada fila.
#   2. Usa pandas para construir un DataFrame con las columnas de la
#      matriz original más una columna 'row_mean'.
#   3. Filtra las filas donde row_mean >= threshold.
#   4. Retorna la lista de filas filtradas (con el promedio al final,
#      como float).
#
# Entrada:  mat (lista de listas), threshold (número)
# Salida:   lista de listas (filas + promedio al final como float)
#
# Ejemplo:
#   mat=[[1,3],[5,7],[9,11]], threshold=5
#   Salida: [[5.0,7.0,6.0],[9.0,11.0,10.0]]
# ──────────────────────────────────────────────────────────

def problem_03(mat, threshold):
    # TU CÓDIGO AQUÍ
    arr = np.array(mat, dtype=float)
    means = arr.mean(axis=1)
    df = pd.DataFrame(arr)
    df["row_mean"] = means
    filtered = df[df["row_mean"] >= threshold]
    return [row.tolist() for row in filtered.values]

# ── Test Problema 03 (NO MODIFICAR) ──
_p3_mat = [[[1,3],[5,7],[9,11]],[[0,0],[2,2],[4,4]],[[5]],
           [[1,2,3],[3,3,3],[10,0,0]],[[10,20,30]],[[-1,-3],[-4,-6]],
           [[1,1,1],[2,2,2],[3,3,3]],[[5,5],[5,5],[5,5]],
           [[1,0,1,0],[0,0,0,0],[2,2,2,2]],[[100,200],[300,400]]]
_p3_thr = [5,1,5,4,15,-3,2,5,0.5,200]
_p3_exp = [[[5.0,7.0,6.0],[9.0,11.0,10.0]],[[2.0,2.0,2.0],[4.0,4.0,4.0]],
           [[5.0,5.0]],[],[[10.0,20.0,30.0,20.0]],[[-1.0,-3.0,-2.0]],
           [[2.0,2.0,2.0,2.0],[3.0,3.0,3.0,3.0]],[[5.0,5.0,5.0],[5.0,5.0,5.0],[5.0,5.0,5.0]],
           [[1.0,0.0,1.0,0.0,0.5],[2.0,2.0,2.0,2.0,2.0]],[[300.0,400.0,350.0]]]
_p3_ok = sum(1 for (m,t,e) in zip(_p3_mat,_p3_thr,_p3_exp) if problem_03(m,t)==e)
print(f"Problema 03: {_p3_ok}/10")
