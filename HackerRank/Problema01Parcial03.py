'''
Problema 01
Title: Normalizar Array

Description (140 caracteres):
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

def problem_01(arr):
    pass

# Test harness NumPy
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
    if res == exp:
        correct += 1
print(f"Problema 01 Parcial 03: {correct}/10")