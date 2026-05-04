import numpy as np
import pandas as pd

# ======================================================================
# EXAMEN PARCIAL 03  —  Versión V13
# Módulo 3: NumPy y Pandas
# ======================================================================
# Instrucciones generales:
#   1. Completa el cuerpo de cada función donde dice "TU CÓDIGO AQUÍ".
#   2. No modifiques los bloques de prueba (Test).
#   3. No importes librerías adicionales.
# ======================================================================

# ──────────────────────────────────────────────────────────
# Problema 01 — NumPy
# Título: Porcentaje de Valores Positivos
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un arreglo 1-D de números, usa una máscara booleana en NumPy
#   para calcular qué porcentaje de los elementos son estrictamente
#   positivos (> 0). Retorna el porcentaje como float redondeado a 2
#   decimales (escala 0–100).
#
# Entrada:  lista de números  →  arr
# Salida:   float (porcentaje, 2 decimales)
#
# Ejemplo:
#   Entrada:  [1, -2, 3, 0, -1]
#   Salida:   40.0     # 2 de 5 son positivos
# ──────────────────────────────────────────────────────────

def problem_01(arr):
    # TU CÓDIGO AQUÍ
    a = np.array(arr, dtype=float)
    if len(a) == 0:
        return 0.0
    mask = a > 0
    return round(float(mask.sum()) / len(a) * 100, 2)

# ── Test Problema 01 (NO MODIFICAR) ──
_p1_in  = [[1,-2,3,0,-1],[1,2,3,4,5],[0,0,0],[-1,-2,-3],
           [10,-10,10,-10],[0.5,-0.5],[100],[1,2,0,-1,-2],
           [-5,-4,-3,-2,-1,1],[0,1,2,3,4,5,6,7,8,9]]
_p1_exp = [40.0,100.0,0.0,0.0,50.0,50.0,100.0,40.0,16.67,90.0]
_p1_ok = sum(1 for i,e in zip(_p1_in,_p1_exp) if problem_01(i)==e)
print(f"Problema 01: {_p1_ok}/10")

# ──────────────────────────────────────────────────────────
# Problema 02 — Pandas
# Título: Calcular Bono con apply
# ──────────────────────────────────────────────────────────
# Descripción:
#   Dado un diccionario con claves 'Employee' (strings) y 'Salary'
#   (números), crea un DataFrame y agrega una columna 'Bonus' usando
#   apply (axis=1). El bono se calcula así:
#     - Si Salary >= 5000 → Bonus = Salary * 0.10
#     - Si Salary >= 3000 → Bonus = Salary * 0.07
#     - Otro caso         → Bonus = Salary * 0.05
#   Los valores de 'Bonus' deben estar redondeados a 2 decimales.
#   Retorna la lista de valores de la columna 'Bonus'.
#
# Entrada:  dict con claves "Employee" y "Salary"
# Salida:   lista de floats (bonos redondeados a 2 decimales)
#
# Ejemplo:
#   Entrada:  {"Employee":["A","B","C"],"Salary":[2000,3500,6000]}
#   Salida:   [100.0, 245.0, 600.0]
# ──────────────────────────────────────────────────────────

def problem_02(data):
    # TU CÓDIGO AQUÍ
    df = pd.DataFrame(data)
    def bono(row):
        s = row["Salary"]
        if s >= 5000: return round(s*0.10, 2)
        if s >= 3000: return round(s*0.07, 2)
        return round(s*0.05, 2)
    df["Bonus"] = df.apply(bono, axis=1)
    return df["Bonus"].tolist()

# ── Test Problema 02 (NO MODIFICAR) ──
_p2_in  = [{"Employee":["A","B","C"],"Salary":[2000,3500,6000]},
           {"Employee":["X"],"Salary":[5000]},
           {"Employee":["M","N"],"Salary":[1000,3000]},
           {"Employee":["P","Q","R"],"Salary":[4999,5000,5001]},
           {"Employee":["G"],"Salary":[0]},
           {"Employee":["H","I"],"Salary":[2999,3000]},
           {"Employee":["J","K","L"],"Salary":[3000,4000,5000]},
           {"Employee":["U"],"Salary":[10000]},
           {"Employee":["V","W"],"Salary":[500,5500]},
           {"Employee":["T","S"],"Salary":[2500,7500]}]
_p2_exp = [[100.0,245.0,600.0],[500.0],[50.0,210.0],
           [349.93,500.0,500.1],[0.0],[149.95,210.0],
           [210.0,280.0,500.0],[1000.0],[25.0,550.0],[125.0,750.0]]
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
