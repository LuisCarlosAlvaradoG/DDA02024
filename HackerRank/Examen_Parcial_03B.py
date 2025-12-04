import numpy as np
import pandas as pd

'''
Problema 01
Title: Normalizar Participaciones

Description:
Dado un array unidimensional con cantidades (por ejemplo, unidades vendidas
por producto), normaliza los valores para obtener la participación relativa
de cada elemento respecto al total.

Problem Statement:
Se recibe un array de enteros en formato literal, p.ej. [10, 20, 30].
Utiliza NumPy para convertirlo en un array y aplicar la fórmula:

    x_i / sum(arr)

Retorna una lista de floats redondeados a dos decimales.
Si la suma total es 0, retorna una lista de ceros.

Input Format:
  Una línea con un array literal.

Output Format:
  Lista de floats (redondeados a 2 decimales).
'''

def problem_01(arr):
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    pass

# Test Problem 01 (NO MODIFICAR)
_np_in = [
    [1,1,2],
    [0,0,0],
    [2,2],
    [1,2,3,4],
    [5],
    [0,5],
    [3,3,3],
    [2,3,5],
    [10,0,0],
    [4,6]
]
_np_exp = [
    [0.25, 0.25, 0.5],
    [0.0, 0.0, 0.0],
    [0.5, 0.5],
    [0.1, 0.2, 0.3, 0.4],
    [1.0],
    [0.0, 1.0],
    [0.33, 0.33, 0.33],
    [0.2, 0.3, 0.5],
    [1.0, 0.0, 0.0],
    [0.4, 0.6]
]
correct = 0

for inp, exp in zip(_np_in, _np_exp):
    res = problem_01(inp)
    if np.all(res == exp):
        correct += 1
print(f"Problema 01 Parcial 03: {correct}/10")


'''
Problema 02
Title: Filtrar Empleados de Tiempo Completo

Description:
Dado un diccionario con 'Name' y 'Hours' (horas trabajadas a la semana),
retorna el DataFrame con las personas cuya Hours >= 40 (tiempo completo).

Problem Statement:
Se recibe un dict con las claves:
  'Name': lista de strings
  'Hours': lista de enteros
Utiliza pandas para crear un DataFrame y filtrar las filas donde Hours >= 40.
Retorna un DataFrame con los nombres en el orden original.

Input Format:
  Una línea con un dict literal.

Output Format:
  DataFrame filtrado.
'''

def problem_02(data):
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    pass

# Test Problem 02 (NO MODIFICAR)
_pd_in = [
    {'Name':['Ana','Beto','Caro'],'Hours':[35,40,45]},
    {'Name':['Tom'],'Hours':[40]},
    {'Name':['L1','L2'],'Hours':[10,20]},
    {'Name':['X','Y','Z'],'Hours':[50,39,60]},
    {'Name':['P','Q','R','S'],'Hours':[40,40,40,40]},
    {'Name':['A','B'],'Hours':[0,100]},
    {'Name':['John','Doe','Smith'],'Hours':[41,39,42]},
    {'Name':['M','N','O'],'Hours':[10,20,30]},
    {'Name':['U','V','W'],'Hours':[39,40,41]},
    {'Name':['K'],'Hours':[10]}
]

_pd_exp = [
    {'Name':['Beto','Caro'],'Hours':[40,45]},
    {'Name':['Tom'],'Hours':[40]},
    {'Name':[],'Hours':[]},
    {'Name':['X','Z'],'Hours':[50,60]},
    {'Name':['P','Q','R','S'],'Hours':[40,40,40,40]},
    {'Name':['B'],'Hours':[100]},
    {'Name':['John','Smith'],'Hours':[41,42]},
    {'Name':[],'Hours':[]},
    {'Name':['V','W'],'Hours':[40,41]},
    {'Name':[],'Hours':[]}
]

correct = 0
for data, exp in zip(_pd_in, _pd_exp):
    res = None
    try:
        res = problem_02(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Name", "Hours"])
    if isinstance(res, pd.DataFrame):
        res = res.reset_index(drop=True)
        try:
            exp_df = exp_df.astype(res.dtypes.to_dict())
        except TypeError:
            pass

        if res.equals(exp_df):
            correct += 1
print(f"Problema 02 Parcial 03: {correct}/10")


'''
Problema 03
Title: Filtrar Filas por Promedio

Description:
Dada una matriz, calcula el promedio de cada fila usando NumPy y luego usa
pandas para filtrar sólo las filas cuyo promedio sea mayor o igual a un
umbral dado.

Problem Statement:
Se recibe en dos líneas:
1) Una matriz 2D en formato literal (lista de listas de ints).
2) Un número (int o float) umbral.
Usa NumPy para calcular el promedio de cada fila y luego pandas para filtrar
las filas donde el promedio es mayor o igual al umbral.
Retorna la lista de filas filtradas (listas de números), incluyendo el
promedio al final de cada fila.

Input Format:
  Línea 1: matriz literal.
  Línea 2: número umbral.

Output Format:
  Lista de listas (filas filtradas con su promedio al final).
'''

def problem_03(mat, threshold):
    #TU CÓDIGO AQUÍ (Recuerda quitar "pass")
    pass


_comb_mat = [
    [[1,3],[5,7],[9,11]],
    [[0,0],[2,2],[4,4]],
    [[5]],
    [[1,2,3],[3,3,3],[10,0,0]],
    [[10,20,30]],
    [[-1,-3],[-4,-6]],
    [[1,1,1],[2,2,2],[3,3,3]],
    [[5,5],[5,5],[5,5]],
    [[1,0,1,0],[0,0,0,0],[2,2,2,2]],
    [[100,200],[300,400]]
]
_comb_thr = [5,1,5,4,15,-3,2,5,0.5,200]
_comb_exp = [
    [[5.0, 7.0, 6.0], [9.0, 11.0, 10.0]],
    [[2.0, 2.0, 2.0], [4.0, 4.0, 4.0]],
    [[5.0, 5.0]],
    [],
    [[10.0, 20.0, 30.0, 20.0]],
    [[-1.0, -3.0, -2.0]],
    [[2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]],
    [[5.0, 5.0, 5.0], [5.0, 5.0, 5.0], [5.0, 5.0, 5.0]],
    [[1.0, 0.0, 1.0, 0.0, 0.5], [2.0, 2.0, 2.0, 2.0, 2.0]],
    [[300.0, 400.0, 350.0]]
]

correct = 0
for mat, thr, exp in zip(_comb_mat, _comb_thr, _comb_exp):
    res = problem_03(mat, thr)
    if res == exp:
        correct += 1
print(f"Problema 03 Parcial 03: {correct}/10")
