'''
Problema 03
Title: Filtrar Filas por Suma

Description (140 caracteres):
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
    pass

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
    [[4,5,6],[7,8,9]],
    [[2,2]],
    [[5]],
    [[5,6],[7,8]],
    [[10,20,30]],
    [[-1,-2,-3]],
    [[2,2,2],[3,3,3]],
    [[5,5],[5,5],[5,5]],
    [[1,0,1],[1,1,1]],
    [[300,400]]
]
correct = 0
for mat, thr, exp in zip(_comb_mat, _comb_thr, _comb_exp):
    res = problem_03(mat, thr)
    if res == exp:
        correct += 1
print(f"Problema 03 Parcial 03: {correct}/10")
