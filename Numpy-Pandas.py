import numpy as np
import pandas as pd

'''1. Numpy: Principales Funciones y Ejemplos
Crear un arreglo de Numpy
Los arreglos en numpy son similares a las listas, pero con capacidades matemáticas avanzadas.'''

# Crear un arreglo de 1D (vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print("Arreglo 1D:", arr_1d)

# Crear un arreglo de 2D (matriz)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Arreglo 2D:\n", arr_2d)

'''Funciones comunes de Numpy
Generación de números: arange, linspace, random.
Operaciones matemáticas: sum, mean, std, max, min.
Reshape: Cambiar la forma de un arreglo.'''

# Generar un arreglo de números con np.arange()
arr_range = np.arange(0, 10, 2)
print("Arreglo con np.arange:", arr_range)

# Operaciones matemáticas
print("Suma del arreglo:", np.sum(arr_1d))
print("Media del arreglo:", np.mean(arr_1d))
print("Desviación estándar:", np.std(arr_1d))

# Cambiar forma de un arreglo
arr_reshaped = np.reshape(arr_2d, (3, 2))
print("Arreglo con nueva forma:\n", arr_reshaped)

'''2. Pandas: Principales Funciones y Ejemplos
Crear un DataFrame
Un DataFrame es una tabla de datos bidimensional que contiene columnas con etiquetas, similar a una hoja de cálculo.'''
# Crear un DataFrame a partir de un diccionario
data = {
    "Nombre": ["Ana", "Juan", "Luis", "Marta"],
    "Edad": [23, 34, 45, 22],
    "Salario": [50000, 60000, 75000, 45000]
}
df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)

'''Principales funciones en Pandas
Selección y Filtrado: Seleccionar filas, columnas, y aplicar filtros.
Resumen de Datos: Obtener estadísticas descriptivas de las columnas.
Manipulación de Datos: Crear, eliminar y actualizar columnas.'''
# Selección de columnas
print("Columna 'Nombre':\n", df["Nombre"])

# Filtrado de filas
print("Filtrar personas con Salario > 50000:\n", df[df["Salario"] > 50000])

# Resumen de datos
print("Resumen estadístico:\n", df.describe())

# Agregar una nueva columna
df["Años de Experiencia"] = [1, 10, 15, 2]
print("DataFrame con nueva columna:\n", df)

# Eliminar una columna
df = df.drop(columns=["Años de Experiencia"])
print("DataFrame después de eliminar columna:\n", df)

'''3. Ejemplos Comunes en Análisis de Datos
Agrupación de datos y cálculo de estadísticas
pandas permite agrupar datos y calcular estadísticas fácilmente con groupby.'''

# Crear un DataFrame de ejemplo
data = {
    "Departamento": ["Ventas", "Ventas", "Marketing", "Marketing", "IT", "IT"],
    "Empleado": ["Carlos", "María", "Ana", "Pedro", "Luis", "Juan"],
    "Salario": [50000, 60000, 55000, 52000, 60000, 65000]
}
df = pd.DataFrame(data)

# Agrupar por 'Departamento' y calcular salario promedio
salario_promedio = df.groupby("Departamento")["Salario"].mean()
print("Salario promedio por departamento:\n", salario_promedio)

'''Operaciones de Tiempo y Fechas
pandas maneja bien datos temporales, como fechas y horas.'''

# Convertir una lista de fechas en una serie de Pandas
fechas = pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"])
df_fechas = pd.DataFrame({"Fecha": fechas, "Valores": [10, 20, 30]})

# Calcular la diferencia de días entre fechas
df_fechas["Días desde inicio"] = (df_fechas["Fecha"] - df_fechas["Fecha"].min()).dt.days
print("DataFrame con diferencias de días:\n", df_fechas)

'''Funciones y Métodos de Numpy
Creación de Arreglos'''

# Arreglo de ceros y unos
print("Arreglo de ceros:", np.zeros(5))
print("Arreglo de unos:", np.ones((2, 3)))

# Arreglo de valores en un rango
print("Arreglo con arange:", np.arange(0, 10, 2))

# Arreglo de valores espaciados linealmente
print("Arreglo con linspace:", np.linspace(0, 1, 5))

'''Propiedades de Arreglos'''
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Forma del arreglo:", arr.shape)
print("Dimensiones del arreglo:", arr.ndim)
print("Tamaño total del arreglo:", arr.size)

'''Manipulación de Forma'''
# Reshape
print("Reshape del arreglo:", arr.reshape(3, 2))

# Transposición
print("Transposición del arreglo:", arr.T)

# Aplanamiento (flatten)
print("Arreglo aplanado:", arr.flatten())

'''Indexación Avanzada'''
arr = np.array([10, 20, 30, 40, 50])
print("Elementos mayores a 25:", arr[arr > 25])

# Indexación booleana
print("Elementos menores a 40 multiplicados por 2:", arr[arr < 40] * 2)

'''Operaciones Matemáticas'''
arr = np.array([1, 2, 3, 4])
print("Suma:", np.sum(arr))
print("Media:", np.mean(arr))
print("Desviación estándar:", np.std(arr))
print("Producto acumulado:", np.cumprod(arr))

'''Funciones Universales (ufuncs)'''
# Seno, coseno, exponencial y logaritmo
arr = np.array([0, np.pi / 2, np.pi])
print("Seno:", np.sin(arr))
print("Coseno:", np.cos(arr))
print("Exponencial:", np.exp(arr))
print("Logaritmo natural:", np.log(np.array([1, np.e, np.e**2])))

'''Álgebra Lineal'''
# Producto punto
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Producto punto:", np.dot(a, b))

# Inversa y determinante
print("Inversa de a:", np.linalg.inv(a))
print("Determinante de a:", np.linalg.det(a))

'''Generación de Números Aleatorios'''

# Generación de números aleatorios
print("Aleatorio uniforme [0,1):", np.random.rand(3))
print("Aleatorio normal (media=0, sigma=1):", np.random.randn(3))
print("Aleatorio entero:", np.random.randint(1, 10, 3))

'''Funciones y Métodos de Pandas
Creación de Series y DataFrames'''

# Serie
serie = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("Serie:\n", serie)

# DataFrame
data = {'Nombre': ['Ana', 'Luis', 'Juan'], 'Edad': [25, 35, 50]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

'''Propiedades de DataFrames'''

print("Columnas:", df.columns)
print("Índices:", df.index)
print("Tipos de datos:", df.dtypes)
print("Tamaño:", df.shape)

'''Selección y Filtrado de Datos'''
# Selección de una columna
print("Columna 'Edad':\n", df['Edad'])

# Selección de filas por índice
print("Primera fila:\n", df.iloc[0])

# Filtrado condicional
print("Filtrar donde Edad > 30:\n", df[df['Edad'] > 30])

'''Operaciones de Agregación'''
print("Suma por columna:\n", df.sum())
print("Media de edad:", df['Edad'].mean())
print("Estadísticas descriptivas:\n", df.describe())

'''Manejo de Datos Faltantes'''
# Identificar valores nulos
df['Salario'] = [50000, None, 60000]
print("Valores nulos:\n", df.isna())

# Llenar valores nulos
df['Salario'].fillna(df['Salario'].mean(), inplace=True)
print("Valores nulos llenados:\n", df)

'''Manipulación de Columnas'''
# Agregar columna
df['Experiencia'] = [5, 10, 15]
print("DataFrame con columna 'Experiencia':\n", df)

# Eliminar columna
df.drop('Experiencia', axis=1, inplace=True)
print("DataFrame sin columna 'Experiencia':\n", df)

'''Ordenar y Reordenar Datos'''
# Ordenar por una columna
df = df.sort_values('Edad', ascending=False)
print("DataFrame ordenado por Edad:\n", df)

'''Agrupación de Datos'''
data = {
    'Departamento': ['Ventas', 'Ventas', 'IT', 'IT'],
    'Salario': [50000, 60000, 65000, 70000]
}
df = pd.DataFrame(data)
print("Salario promedio por Departamento:\n", df.groupby('Departamento')['Salario'].mean())

'''Operaciones de Fusión y Unión de DataFrames'''
# DataFrames de ejemplo
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Ana', 'Luis', 'Pedro']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salario': [50000, 60000, 70000]})

# Fusión (join) por columna 'ID'
df_merged = pd.merge(df1, df2, on='ID', how='inner')
print("DataFrame fusionado:\n", df_merged)

'''Trabajo con Fechas y Tiempos'''
# Convertir una columna a tipo datetime
fechas = pd.Series(['2024-01-01', '2024-02-01', '2024-03-01'])
df['Fecha'] = pd.to_datetime(fechas)
print("DataFrame con fechas:\n", df)

# Extraer año y mes
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
print("DataFrame con año y mes extraídos:\n", df)

'''Operaciones de Texto'''
# Crear columna de texto
df = pd.DataFrame()
df['Nombre'] = ['Ana López', 'Luis Pérez', 'Juan Ramírez']
df

# Operaciones de texto
df['Nombre en mayúsculas'] = df['Nombre'].str.upper()
df['Inicial'] = df['Nombre'].str[0]
print("DataFrame con operaciones de texto:\n", df)

'''Ejercicios Básicos de Numpy'''

'''Crear un arreglo de números del 1 al 10
Genera un arreglo de numpy que contenga los números del 1 al 10, ambos incluidos.
'''
# Ejemplo de solución
arr = np.arange(1, 11)

'''Crear una matriz de ceros de 3x3
Crea una matriz de numpy de 3x3 que solo contenga ceros.'''
# Ejemplo de solución
matriz_ceros = np.zeros((3, 3))

'''Reemplazar los valores de un arreglo
Crea un arreglo de numpy con los números del 1 al 5 y luego cambia todos los valores a 10.'''
# Ejemplo de solución
arr = np.array([1, 2, 3, 4, 5])
arr[:] = 10

'''Generar un arreglo con valores aleatorios entre 0 y 1
Genera un arreglo de 5 números aleatorios entre 0 y 1.'''
# Ejemplo de solución
arr_aleatorio = np.random.rand(5)

'''Sumar todos los elementos de un arreglo
Crea un arreglo de numpy con los números del 1 al 10 y calcula la suma total.'''
# Ejemplo de solución
arr = np.arange(1, 11)
suma_total = np.sum(arr)

'''Calcular la media de un arreglo
Crea un arreglo de numpy con los números del 1 al 10 y calcula la media.'''
# Ejemplo de solución
media = np.mean(arr)

'''Seleccionar elementos mayores a 5
Dado el arreglo arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), selecciona solo los elementos mayores a 5.'''
# Ejemplo de solución
seleccion = arr[arr > 5]

'''Crear una matriz de identidad de 4x4
Crea una matriz identidad de 4x4.'''
# Ejemplo de solución
matriz_identidad = np.eye(4)

'''Calcular el producto punto de dos matrices
Crea dos matrices de numpy de 2x2 y calcula su producto punto.'''
# Ejemplo de solución
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
producto_punto = np.dot(matriz1, matriz2)

'''Obtener los índices de los elementos no nulos
Dado el arreglo arr = np.array([0, 2, 0, 3, 5]), encuentra los índices de los elementos no nulos.'''
# Ejemplo de solución
indices_no_nulos = np.nonzero(arr)

'''Ejercicios Básicos de Pandas'''

'''Crear un DataFrame a partir de un diccionario
Crea un DataFrame de pandas que contenga nombres de estudiantes y sus calificaciones en matemáticas.'''

# Ejemplo de solución
data = {'Nombre': ['Ana', 'Luis', 'Juan'], 'Matemáticas': [80, 90, 75]}
df = pd.DataFrame(data)

'''Seleccionar una columna
Usando el DataFrame anterior, selecciona solo la columna de calificaciones.'''
# Ejemplo de solución
calificaciones = df['Matemáticas']

'''Filtrar filas
Filtra los estudiantes que tienen una calificación mayor a 80.'''
# Ejemplo de solución
filtro = df[df['Matemáticas'] > 80]

'''Calcular la media de una columna
Calcula la calificación media en la columna de matemáticas.'''
# Ejemplo de solución
media_calificaciones = df['Matemáticas'].mean()

'''Agregar una nueva columna
Agrega una columna de inglés con las calificaciones [85, 70, 90].'''
# Ejemplo de solución
df['Inglés'] = [85, 70, 90]

'''Eliminar una columna
Elimina la columna de inglés que agregaste en el ejercicio anterior.'''
# Ejemplo de solución
df = df.drop('Inglés', axis=1)

'''Ordenar el DataFrame
Ordena el DataFrame por la columna de matemáticas en orden descendente.'''
# Ejemplo de solución
df_ordenado = df.sort_values(by='Matemáticas', ascending=False)

'''Agrupar datos
Crea un DataFrame con columnas Departamento y Salario. Agrupa los datos por departamento y calcula el salario promedio.'''
# Ejemplo de solución
data = {'Departamento': ['Ventas', 'Ventas', 'IT', 'IT'],
        'Salario': [50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)
salario_promedio = df.groupby('Departamento')['Salario'].mean()

'''Manejo de valores nulos
Añade una columna Bono con algunos valores nulos [1000, None, 500]. Luego llena los valores nulos con 0.'''
# Ejemplo de solución
df['Bono'] = [1000, None, 500]
df['Bono'].fillna(0, inplace=True)

'''Convertir una columna a tipo datetime y extraer el año
Crea una columna Fecha con las fechas ['2024-01-01', '2024-02-01', '2024-03-01'], conviértela a tipo datetime y extrae el año en una nueva columna Año.'''
# Ejemplo de solución
df['Fecha'] = pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01'])
df['Año'] = df['Fecha'].dt.year

# LOC Y ILOC
'''Ejemplo de DataFrame para Demostración
Para explicar estos métodos, primero crearemos un DataFrame simple de ejemplo.'''
# Crear un DataFrame de ejemplo
data = {
    "Nombre": ["Ana", "Luis", "Carlos", "Marta"],
    "Edad": [23, 34, 45, 22],
    "Salario": [50000, 60000, 70000, 65000]
}
df = pd.DataFrame(data)
df.index = ["A", "B", "C", "D"]  # Asignar etiquetas personalizadas a las filas
print("DataFrame de ejemplo:\n", df)

'''Acceso Básico con .loc y .iloc
Seleccionar una Fila por Etiqueta (.loc) o por Índice (.iloc)'''

'''.loc usa las etiquetas de índice de la fila.
.iloc usa la posición de la fila (0 para la primera fila, 1 para la segunda, etc.).'''
# Seleccionar fila con etiqueta "B" usando .loc
print("Fila con etiqueta 'B' (loc):\n", df.loc["B"])

# Seleccionar segunda fila (índice 1) usando .iloc
print("Segunda fila (iloc):\n", df.iloc[1])

'''Seleccionar una Columna por Nombre (.loc) o por Índice (.iloc)'''
# Seleccionar columna 'Edad' usando .loc
print("Columna 'Edad' (loc):\n", df.loc[:, "Edad"])

# Seleccionar segunda columna usando .iloc
print("Segunda columna (iloc):\n", df.iloc[:, 1])

'''Selección de Rango de Filas y Columnas
Seleccionar un Rango de Filas con .loc y .iloc'''

'''.loc incluye el valor final en el rango.
.iloc excluye el valor final en el rango (funciona como el slicing estándar de Python).'''
# Seleccionar filas con etiquetas "A" a "C" usando .loc
print("Filas de 'A' a 'C' (loc):\n", df.loc["A":"C"])

# Seleccionar primeras dos filas usando .iloc
print("Primeras dos filas (iloc):\n", df.iloc[0:2])

'''Seleccionar un Rango de Filas y Columnas'''
# Seleccionar filas "A" a "C" y columnas "Nombre" y "Edad" usando .loc
print("Filas 'A' a 'C', columnas 'Nombre' y 'Edad' (loc):\n", df.loc["A":"C", "Nombre":"Edad"])

# Seleccionar primeras dos filas y primeras dos columnas usando .iloc
print("Primeras dos filas, primeras dos columnas (iloc):\n", df.iloc[0:2, 0:2])

'''Selección con Condiciones
Filtrar con Condiciones usando .loc

Puedes usar .loc para aplicar filtros basados en condiciones.'''
# Seleccionar todas las filas donde 'Edad' > 30
print("Filas donde 'Edad' > 30 (loc):\n", df.loc[df["Edad"] > 30])

# Seleccionar filas donde 'Salario' > 60000 y solo mostrar 'Nombre' y 'Salario'
print("Filas con 'Salario' > 60000, columnas 'Nombre' y 'Salario' (loc):\n", df.loc[df["Salario"] > 60000, ["Nombre", "Salario"]])

'''Actualización de Valores con .loc y .iloc
Actualizar Valores en una Sola Celda'''
# Cambiar la edad de "Luis" a 35 usando .loc
df.loc["B", "Edad"] = 35
print("DataFrame actualizado (loc):\n", df)

# Cambiar la edad en la segunda fila a 36 usando .iloc
df.iloc[1, 1] = 36
print("DataFrame actualizado (iloc):\n", df)

'''Actualizar Múltiples Filas con Condiciones'''
# Incrementar el salario en un 10% para empleados con edad mayor a 30 usando .loc
df.loc[df["Edad"] > 30, "Salario"] *= 1.10
print("DataFrame con salario incrementado:\n", df)

'''Selección de Múltiples Columnas y Filas Específicas
Seleccionar Filas y Columnas Específicas'''
# Seleccionar filas "A" y "C" y columnas "Nombre" y "Salario" usando .loc
print("Filas 'A' y 'C', columnas 'Nombre' y 'Salario' (loc):\n", df.loc[["A", "C"], ["Nombre", "Salario"]])

# Seleccionar primera y tercera fila, y primera y tercera columna usando .iloc
print("Primera y tercera fila, primera y tercera columna (iloc):\n", df.iloc[[0, 2], [0, 2]])

'''Comparación de .loc y .iloc
.loc funciona con etiquetas y puede ser más intuitivo cuando el índice es significativo (por ejemplo, un nombre o fecha).
.iloc es útil para seleccionar datos por posiciones, especialmente en casos donde se desconoce o no se utilizan etiquetas específicas de índice.'''

'''Ejercicios de Práctica
Usando .loc, selecciona todas las filas donde Edad sea mayor a 25 y muestra solo las columnas Nombre y Salario.

Usando .iloc, selecciona las últimas dos filas y las primeras dos columnas.

Usando .loc, cambia el Salario de Carlos a 75000.

Usando .iloc, incrementa la Edad de la primera fila en 5 años.

Usando .loc, selecciona las filas con etiquetas “B” y “D” y las columnas Nombre y Edad.

Usando .iloc, selecciona el valor en la tercera fila y segunda columna y reemplázalo por 99.

Usando .loc, selecciona las filas donde Salario sea mayor a 60000 y multiplica la Edad de esas filas por 1.1.

Usando .iloc, selecciona todas las filas y columnas desde la segunda fila y columna en adelante.

Usando .loc, selecciona las filas donde Edad sea menor de 30 y cambia el valor de Salario a 55000.

Usando .iloc, selecciona todas las filas excepto la última y muestra solo las columnas Nombre y Edad.'''