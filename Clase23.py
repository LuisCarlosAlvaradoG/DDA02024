'''
NumPy
NumPy (Numerical Python) es un biblioteca especializada en cálculo numérico y análisis de datos

Principal estructura: 
ndarray

Ventajas: 
* Uso eficiente de memoria
* Operaciones vectorizadas (sin usar ciclo for)
* Funciones matemáticas, estadísticas, algebra lineal, etc.
* Soporte de datos multidimensionales
'''
import numpy as np

a = np.array([1,2,3]) #1D
print(a)

b = np.array([[1, 2, 3],[4, 5, 6]]) #2D
print(b)

c = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]]) #3D
print(c)

'''
Atributos importantes
'''
c.shape # filas, columnas
c.ndim #número de dimensiones
c

c.size #Total de elementos
c.dtype #Tipo de valores que tienes en tu arreglo

matriz = np.array([[1,2],[3,4]])
matriz
matriz.T #Obtiene la matriz/vector transpuest@

'''
Indexación y sclicing
'''
array = np.array([[10,20,30],[40,50,60]])
print(array[0]) # [10,20,30]
print(array[0][1]) # 20
print(array[1, 2]) # 60
 
#[filas, columnas]
print(array)
print(array[0, :]) #Primera fila
print(array[:, 1]) #Segunda columna

print(array[0:1, 1:2]) 

'''
Operaciones vectorizadas
'''
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a)
print(b)

print(a + b)
print(a * b)
print(a ** 2)
print(np.sqrt(b[0]))
np.sqrt(9,order = "C") #Raíz cúbica

'''
Métodos de creación útiles
'''
np.zeros((2,3), dtype="int") # Matriz de zeros
np.zeros((5, 1))
np.ones((2,3))
np.ones((2,3), dtype = "int")
np.full((2,2), 7)
np.full((2,2), int(input()))

np.full((int(input()),int(input())), int(input()))
np.eye(3)

np.arange(0, 10, 2) # Inicio, Fin sin incluir, Paso
np.linspace(0, 1, 5) #Inicio, Fin, Divisiones
np.linspace(0, 100, 1000)
np.linspace(0, 100, 101, retstep=True)

np.random.rand(2,3)

np.random.randint(1,10)
np.random.uniform(1,10)
np.random.uniform(1,10, 2)
np.random.randint(1,10, (3,3))

np.random.normal() #Datos de una distribucion normal

'''
Funciones estadísticas
'''

array = np.array([[10,20,30],[40,50,60]])
array.mean()
array.mean(axis=0) #Media por columna
array.mean(axis=1) #Media por fila

array.sum()
array.max()
array.min()
array.std()
array.var()