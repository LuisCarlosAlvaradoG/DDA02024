'''
Problema 01
Title: Normalizar Array

Description:
Dado un array unidimensional, normaliza los valores con min-max normalization.

Problem Statement:
Se recibe un array de enteros en formato literal, p.ej. [1,2,3,4].
Utiliza NumPy para convertirlo en un array y aplicar la fórmula:
   (x - min(arr)) / (max(arr) - min(arr))
Retorna una lista de floats redondeados a dos decimales.
Si todos los elementos son iguales, retorna una lista de ceros.

Input Format:
  Una línea con un array literal.

Output Format:
  Lista de floats (redondeados a 2 decimales).
'''
import numpy as np
import pandas as pd

def problem_01(arr):
    a = np.array(arr, dtype=float)
    mn = a.min()
    mx = a.max()
    if mx == mn:
        res = np.zeros_like(a)
    else:
        res = (a - mn) / (mx - mn)
    return np.round(res, 2)

# Test Problem 01 (NO MODIFICAR)
_np_in = [
    [1,2,3,4],
    [5,5,5],
    [0,10,20],
    [-1,0,1],
    [100,200,300,400],
    [3,3,6,9],
    [7],
    [2,4,6,8,10],
    [10,0,10,0],
    [5,15,25]
]
_np_exp = [
    [0.0,0.33,0.67,1.0],
    [0.0,0.0,0.0],
    [0.0,0.5,1.0],
    [0.0,0.5,1.0],
    [0.0,0.33,0.67,1.0],
    [0.0,0.0,0.5,1.0],
    [0.0],
    [0.0,0.25,0.5,0.75,1.0],
    [1.0,0.0,1.0,0.0],
    [0.0,0.5,1.0]
]
correct = 0

for inp, exp in zip(_np_in, _np_exp):
    res = problem_01(inp)
    if np.all(res == exp):
        correct += 1
print(f"Problema 01 Parcial 03: {correct}/10")

'''
Problema 02
Title: Filtrar Adultos

Description:
Dado un diccionario con 'Name' y 'Age', retorna el DataFrame con las personas cuya edad >= 18.

Problem Statement:
Se recibe un dict con las claves:
  'Name': lista de strings
  'Age': lista de enteros
Utiliza pandas para crear un DataFrame y filtrar las filas donde Age >= 18.
Retorna un DataFrame con los nombres en el orden original.

Input Format:
  Una línea con un dict literal.

Output Format:
  DataFrame filtrado.
'''

def problem_02(data):
    df = pd.DataFrame(data)
    filtered = df[df['Age'] >= 18]
    return filtered

# Test Problem 02 (NO MODIFICAR)
_pd_in = [
    {'Name':['Alice','Bob','Charlie'],'Age':[17,18,19]},
    {'Name':['Tom'],'Age':[18]},
    {'Name':['Anna','Ben'],'Age':[16,17]},
    {'Name':['X','Y','Z'],'Age':[20,15,30]},
    {'Name':['P','Q','R','S'],'Age':[18,18,18,18]},
    {'Name':['A','B'],'Age':[0,100]},
    {'Name':['John','Doe','Smith'],'Age':[21,17,22]},
    {'Name':['M','N','O'],'Age':[17,16,15]},
    {'Name':['U','V','W'],'Age':[19,19,17]},
    {'Name':['K'],'Age':[10]}
]

_pd_exp = [
    {'Name':['Bob','Charlie'],'Age':[18,19]},
    {'Name':['Tom'],'Age':[18]},
    {'Name':[],'Age':[]},
    {'Name':['X','Z'],'Age':[20,30]},
    {'Name':['P','Q','R','S'],'Age':[18,18,18,18]},
    {'Name':['B'],'Age':[100]},
    {'Name':['John','Smith'],'Age':[21,22]},
    {'Name':[],'Age':[]},
    {'Name':['U','V'],'Age':[19,19]},
    {'Name':[],'Age':[]}
]

correct = 0
for data, exp in zip(_pd_in, _pd_exp):
    res = None
    try:
        res = problem_02(data)
    except:
        pass
    exp_df = pd.DataFrame(exp, columns=["Name", "Age"])
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
Title: Filtrar Filas por Suma

Description:
Dada una matriz, filtra filas cuya suma >= umbral combinando NumPy y pandas.

Problem Statement:
Se recibe en dos líneas:
1) Una matriz 2D en formato literal (lista de listas de ints).
2) Un entero umbral.
Usa NumPy para calcular la suma de cada fila y luego pandas para filtrar filas
donde la suma es mayor o igual al umbral.
Retorna la lista de filas filtradas (listas de ints).

Input Format:
  Línea 1: matriz literal.
  Línea 2: entero umbral.

Output Format:
  Lista de listas (filas filtradas).
'''
def problem_03(mat, threshold):
    arr = np.array(mat)
    sums = arr.sum(axis=1)
    df = pd.DataFrame(mat)
    df['sum'] = sums
    filt = df[df['sum'] >= threshold]
    return filt.values.tolist()


_comb_mat = [
    [[1,2,3],[4,5,6],[7,8,9]],  
    [[0,0],[1,1],[2,2]],       
    [[5]],                      
    [[1,2],[3,4],[5,6],[7,8]],  
    [[10,20,30]],               
    [[-1,-2,-3],[-4,-5,-6]],     
    [[1,1,1],[2,2,2],[3,3,3]],  
    [[5,5],[5,5],[5,5]],         
    [[1,0,1],[0,1,0],[1,1,1]],   
    [[100,200],[300,400]]
]
_comb_thr = [10,3,5,10,50,-10,6,10,2,500]
_comb_exp = [
    [[4,5,6,15],[7,8,9,24]],
    [[2,2,4]],
    [[5,5]],
    [[5,6,11],[7,8,15]],
    [[10,20,30,60]],
    [[-1,-2,-3,-6]],
    [[2,2,2,6],[3,3,3,9]],
    [[5,5,10],[5,5,10],[5,5,10]],
    [[1,0,1,2],[1,1,1,3]],
    [[300,400,700]]
]
correct = 0
for mat, thr, exp in zip(_comb_mat, _comb_thr, _comb_exp):
    res = problem_03(mat, thr)
    if res == exp:
        correct += 1
print(f"Problema 03 Parcial 03: {correct}/10")
