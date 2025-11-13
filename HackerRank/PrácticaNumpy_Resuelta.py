# Practica de NumPy - 10 Problemas (Nivel Fácil)
# Cada sección contiene:
# 1) Descripción del problema (en comentarios)
# 2) Un espacio para que el alumno pegue su solución usando NumPy
# 3) Un conjunto de test cases y un conteo de aciertos ("Problema X: correctos/10")

'''
Modifica únicamente el código dentro de cada función donde leas "Escribe aquí tu código", no modifiques ni elimines el resto
'''

import numpy as np

# -----------------------------
# Problema 1: Sumar Elementos del Array
# --------------------------------
def problem1(arr):
    # Esta es la solución, para que la tengas como ejemplo.
    arreglo = np.array(arr)
    resultado = np.sum(arreglo)
    return resultado

# TESTS Problema 1
_t1_in = [[1,2,3],[10,20,30,40],[5],[0,0,0],[1,1,1,1,1],[2,4,6,8],[100,200],[7,3,5],[10,0,10,0],[9,9,9,9]]
_t1_exp = [6,100,5,0,5,20,300,15,20,36]
correct = 0
for inp, exp in zip(_t1_in, _t1_exp):
    res = None
    try:
        res = problem1(inp)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 1: {correct}/10")

# -----------------------------
# Problema 2: Media del Array
# --------------------------------
def problem2(arr):
    arreglo = np.array(arr)
    media = np.mean(arreglo)
    return round(float(media), 2)

# TESTS Problema 2
_t2_in = [[1,2,3,4],[10,20,30],[5],[0,0,0,0],[2,4],[1,1,1,1,1],[7,3,5],[10,0,10],[9,9,9,9,9],[3,7,5,10]]
_t2_exp = [2.50,20.00,5.00,0.00,3.00,1.00,5.00,6.67,9.00,6.25]
correct = 0
for inp, exp in zip(_t2_in, _t2_exp):
    res = None
    try:
        res = problem2(inp)
    except:
        pass
    if isinstance(res, float) and abs(res - exp) < 0.01:
        correct += 1
print(f"Problema 2: {correct}/10")

# -----------------------------
# Problema 3: Desviación Estándar
# --------------------------------
def problem3(arr):
    # Escribe aquí tu código
    arreglo = np.array(arr)
    desvest = np.std(arreglo)   # ddof=0 (poblacional), coincide con los tests
    return round(float(desvest), 2)

# TESTS Problema 3
_t3_in = [[1,2,3,4,5],[10,10,10],[1,2],[4,4,4,4],[1,3,5,7],[2,4,6,8,10],[0,0,1,1],[5,6,7,8],[3,3,5,7],[9,8,7,6]]
_t3_exp = [1.41,0.00,0.50,0.00,2.24,2.83,0.50,1.12,1.66,1.12]
correct = 0
for inp, exp in zip(_t3_in, _t3_exp):
    res = None
    try:
        res = problem3(inp)
    except:
        pass
    if isinstance(res, float) and abs(res - exp) < 0.01:
        correct += 1
print(f"Problema 3: {correct}/10")

# -----------------------------
# Problema 4: Transponer una Matriz
# --------------------------------
def problem4(mat):
    arreglo = np.array(mat)
    # Regresamos lista de listas (más amigable para el alumno)
    return arreglo.T.tolist()

# TESTS Problema 4
_t4_in = [ [[1,2],[3,4]], [[1]], [[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]], [[7,8,9]], [[1],[2],[3]], [[2,4,6],[8,10,12],[14,16,18]], [[5,6],[7,8]], [[1,2,3],[4,5,6],[7,8,9]], [[1,2],[3,4],[5,6],[7,8]] ]
_t4_exp = [ [[1,3],[2,4]], [[1]], [[1,4],[2,5],[3,6]], [[1,3,5],[2,4,6]], [[7],[8],[9]], [[1,2,3]], [[2,8,14],[4,10,16],[6,12,18]], [[5,7],[6,8]], [[1,4,7],[2,5,8],[3,6,9]], [[1,3,5,7],[2,4,6,8]] ]
correct = 0
for inp, exp in zip(_t4_in, _t4_exp):
    res = None
    try:
        res = problem4(inp)
    except:
        pass
    if np.all(np.array(res) == np.array(exp)):
        correct += 1
print(f"Problema 4: {correct}/10")

# -----------------------------
# Problema 5: Redimensionar un Array
# --------------------------------
def problem5(arr, r, c):
    #Escribe aquí tu código
    arreglo = np.array(arr)
    reshaped = arreglo.reshape(r, c)
    # Tests esperan lista de listas
    return reshaped.tolist()

# TESTS Problema 5
_t5_arr = [[1,2,3,4],[5,6,7,8,9,10],[1,2,3],[1,2,3,4,5,6,7,8],[9,8,7,6,5,4],[10,20,30,40,50,60],[1,1,1,1],[2,4,6,8,10,12],[7,8,9,10],[5,5,5,5,5,5]]
_t5_dims = [(2,2),(2,3),(3,1),(4,2),(3,2),(2,3),(1,4),(3,2),(2,2),(3,2)]
_t5_exp = [ [[1,2],[3,4]], [[5,6,7],[8,9,10]], [[1],[2],[3]], [[1,2],[3,4],[5,6],[7,8]], [[9,8],[7,6],[5,4]], [[10,20,30],[40,50,60]], [[1,1,1,1]], [[2,4],[6,8],[10,12]], [[7,8],[9,10]], [[5,5],[5,5],[5,5]] ]
correct = 0
for arr, (r,c), exp in zip(_t5_arr, _t5_dims, _t5_exp):
    res = None
    try:
        res = problem5(arr, r, c)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 5: {correct}/10")

# -----------------------------
# Problema 6: Element-wise Maximum de Dos Arrays
# --------------------------------
def problem6(arr1, arr2):
    #Escribe aquí tu código
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    max_arr = np.maximum(a1, a2)
    return max_arr.tolist()

# TESTS Problema 6
_t6_arr1 = [[1,3,5],[10,20],[0,0,0],[7,8,9],[1,2,3,4],[5],[6,6,6],[100,50],[1,2,3],[0,9,8]]
_t6_arr2 = [[2,2,6],[5,25],[1,2,3],[7,8,9],[4,3,2,1],[10],[6,5,7],[90,60],[3,2,1],[9,0,10]]
_t6_exp = [[2,3,6],[10,25],[1,2,3],[7,8,9],[4,3,3,4],[10],[6,6,7],[100,60],[3,2,3],[9,9,10]]
correct = 0
for a1, a2, exp in zip(_t6_arr1, _t6_arr2, _t6_exp):
    res = None
    try:
        res = problem6(a1, a2)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 6: {correct}/10")

# -----------------------------
# Problema 7: Extraer Diagonal Principal
# --------------------------------
def problem7(mat):
    #Escribe aquí tu código
    m = np.array(mat)
    diagonal = np.diag(m)
    return diagonal.tolist()

# TESTS Problema 7
_t7_mat = [[[1,2,3],[4,5,6],[7,8,9]],[[10]],[[2,3],[4,5]],[[1,2],[3,4]],[[5,6,7],[8,9,10],[11,12,13]],[[0,1],[2,3]],[[4,5,6],[7,8,9],[10,11,12]],[[1,3],[2,4]],[[7,8,9],[10,11,12],[13,14,15]],[[2,2],[2,2]]]
_t7_exp = [[1,5,9],[10],[2,5],[1,4],[5,9,13],[0,3],[4,8,12],[1,4],[7,11,15],[2,2]]
correct = 0
for mat, exp in zip(_t7_mat, _t7_exp):
    res = None
    try:
        res = problem7(mat)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 7: {correct}/10")

# -----------------------------
# Problema 8: Crear Matriz Identidad
# --------------------------------
def problem8(n):
    #Escribe aquí tu código
    identidad = np.eye(n, dtype=int)
    return identidad.tolist()

# TESTS Problema 8
_t8_in = [1,2,3,4,5,2,3,4,5,3]
_t8_exp = [ [[1]],[[1,0],[0,1]],[[1,0,0],[0,1,0],[0,0,1]],[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],[[1,0],[0,1]],[[1,0,0],[0,1,0],[0,0,1]],[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],[[1,0,0],[0,1,0],[0,0,1]] ]
correct = 0
for n, exp in zip(_t8_in, _t8_exp):
    res = None
    try:
        res = problem8(n)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 8: {correct}/10")

# -----------------------------
# Problema 9: Contar Ocurrencias en un Array
# --------------------------------
def problem9(arr, k):
    #Escribe aquí tu código
    a = np.array(arr)
    conteo = np.sum(a == k)
    return int(conteo)

# TESTS Problema 9
_t9_arr = [[1,2,2,3],[5,5,5],[1,2,3,4],[7,8,9,7],[10,20,10,30,10],[1,1,2,2,3,3],[2,2,2,2],[4,5,6,7],[9,9,9,0],[8,7,6,5,4]]
_t9_k   = [2,5,0,7,10,1,2,5,0,8]
_t9_exp = [2,3,0,2,3,2,4,1,1,1]
correct = 0
for arr, k, exp in zip(_t9_arr, _t9_k, _t9_exp):
    res = None
    try:
        res = problem9(arr, k)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 9: {correct}/10")

# -----------------------------
# Problema 10: Índices de Elementos Mayores a k
# --------------------------------
def problem10(arr, k):
    #Escribe aquí tu código
    a = np.array(arr)
    indices = np.where(a > k)[0]
    return indices.tolist()

# TESTS Problema 10
_t10_arr = [[1,4,6,3],[10,20,30],[5,5,5,5],[0,1,2,3,4],[7,8,9],[3,3,3],[100,50,75,80],[1,2,3,4,5],[9,8,7,6],[2,4,2,4,2]]
_t10_k   = [3,25,5,2,10,2,70,5,6,3]
_t10_exp = [[1,2],[2],[],[3,4],[],[0,1,2],[0,2,3],[],[0,1,2],[1,3]]
correct = 0
for arr, k, exp in zip(_t10_arr, _t10_k, _t10_exp):
    res = None
    try:
        res = problem10(arr, k)
    except:
        pass
    if res == exp:
        correct += 1
print(f"Problema 10: {correct}/10")
