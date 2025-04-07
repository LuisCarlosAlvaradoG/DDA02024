#NumPy en Python: Guía Teórica + Ejemplos para Clase

'''
1. ¿Qué es NumPy?
NumPy (Numerical Python) es una biblioteca de Python especializada en cálculo numérico y análisis de datos. Su principal estructura de datos es el ndarray, un arreglo n-dimensional, similar a una lista pero mucho más eficiente y poderoso.

Ventajas de usar NumPy:
Uso eficiente de memoria

Operaciones vectorizadas rápidas (sin for)

Funciones matemáticas, estadísticas, lógicas, álgebra lineal, etc.

Soporte para datos multidimensionales
'''

'''
2. Importación
'''
import numpy as np

'''
3. Creación de Arrays
1D (Vector)
'''

a = np.array([1, 2, 3])

'''
2D (Matriz)
'''

b = np.array([[1, 2, 3], [4, 5, 6]])

'''
3D o más dimensiones
'''

c = np.array([[[1], [2]], [[3], [4]]])

'''
4. Atributos importantes
'''

arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape    # (2, 3) → filas, columnas
arr.ndim     # 2      → número de dimensiones
arr.size     # 6      → total de elementos
arr.dtype    # tipo de datos (int64, float64, etc.)
arr.T        # transpuesta

'''
5. Indexación y slicing
Indexación simple
'''
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr[0][1])     # 20
print(arr[1, 2])     # 60

'''
Slicing
'''

print(arr[0, :])     # Primera fila: [10, 20, 30]
print(arr[:, 1])     # Segunda columna: [20, 50]
print(arr[0:2, 1:3]) # Submatriz

'''
6. Operaciones Vectorizadas
Evitan el uso de bucles y son mucho más rápidas.
'''

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # [5, 7, 9]
print(a * 2)        # [2, 4, 6]
print(a ** 2)       # [1, 4, 9]
print(np.sqrt(b))   # [2.0, 2.236, 2.449]

'''
7. Métodos de creación útiles
'''

np.zeros((2, 3))           # Matriz de ceros
np.ones((3, 2))            # Matriz de unos
np.full((2, 2), 7)         # Matriz llena de 7
np.eye(3)                  # Matriz identidad
np.arange(0, 10, 2)        # [0 2 4 6 8]
np.linspace(0, 1, 5)       # 5 números entre 0 y 1
np.random.rand(2, 3)       # Aleatorios en [0, 1)
np.random.randint(1, 10, (3, 3))  # Enteros aleatorios

'''
8. Métodos y funciones comunes
Estadísticas
'''

arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.mean()       # Media total
arr.mean(axis=0) # Media por columna
arr.mean(axis=1) # Media por fila

arr.sum(), arr.max(), arr.min(), arr.std(), arr.var()

'''
Algebra lineal
'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

np.dot(A, B)     # Producto matricial
np.linalg.inv(A) # Inversa
np.linalg.det(A) # Determinante
np.linalg.eig(A) # Valores y vectores propios

'''
9. Indexación booleana y filtrado
'''

arr = np.array([10, 20, 30, 40, 50])

# Filtrar los elementos mayores a 25
print(arr[arr > 25])  # [30 40 50]

# Asignar nuevos valores condicionalmente
arr[arr < 30] = 0
print(arr)  # [ 0  0 30 40 50]

'''
10. Cambiar forma (reshape, flatten)
'''

arr = np.arange(12)          # [0 1 2 3 4 5 6 7 8 9 10 11]
mat = arr.reshape((3, 4))    # 3x4 matriz
print(mat)

# Convertir en vector
vec = mat.flatten()
'''
11. Concatenación y separación
'''

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

np.concatenate((a, b), axis=0)  # Vertical
np.concatenate((a.T, b.T), axis=1)  # Horizontal

# Separar
np.split(np.arange(10), 2)     # Divide en 2 partes
'''
12. Ejemplos para clase
✅ Crear una matriz 3x3 con valores del 1 al 9
'''

matriz = np.arange(1, 10).reshape(3, 3)
print(matriz)
'''
✅ Sumar dos matrices y multiplicarlas elemento a elemento
'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Suma:\n", A + B)
print("Multiplicación elemento a elemento:\n", A * B)

'''
✅ Normalizar una matriz
'''

M = np.random.randint(10, 100, (3, 3))
media = M.mean()
desv = M.std()
normalizada = (M - media) / desv
print(normalizada)

'''
13. Práctica (Ejercicios de fácil a medio)
Fáciles
Crear un array del 1 al 20.

Crear una matriz 4x4 de ceros.

Crear una matriz identidad de 5x5.

Calcular la suma y media de los números del 1 al 100.

Crear un array con 10 números aleatorios entre 0 y 1.

Intermedios
Crear una matriz 5x5 con valores enteros aleatorios entre 1 y 100, y encontrar el máximo por fila.

Calcular la media por columna y filtrar las columnas cuya media sea mayor a 50.

Dada una matriz, reemplazar los valores pares por 0.

Generar dos vectores aleatorios y calcular el ángulo entre ellos.

Crear una matriz 6x6 y extraer la diagonal principal e inversa.
'''

