#Pandas en Python: Teoría + Ejemplos + Ejercicios

'''
1. ¿Qué es pandas?
pandas es una biblioteca de Python para análisis y manipulación de datos tabulares. Está basada en NumPy y se utiliza en ciencia de datos, análisis financiero, ingeniería, y mucho más.

Ventajas de pandas
Trabaja con datos tabulares (como Excel o bases de datos).

Limpieza y transformación de datos.

Acceso sencillo a filas y columnas.

Soporte para lectura y escritura de archivos (CSV, Excel, SQL).
'''

'''
2. Estructuras principales
Series (1D)
'''

import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
'''
DataFrames (2D)
'''
datos = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 35]
}
df = pd.DataFrame(datos)
print(df)

'''
3. Exploración de datos
'''

df.head()        # Primeras 5 filas
df.tail()        # Últimas 5 filas
df.shape         # (filas, columnas)
df.columns       # Nombres de columnas
df.index         # Índices de las filas
df.info()        # Resumen general
df.describe()    # Estadísticas básicas

'''
4. Acceso a datos
Acceder a columnas
'''

df["Edad"]           # Serie (columna)
df[["Nombre", "Edad"]]  # Varias columnas
'''
Acceder a filas
'''

df.iloc[0]          # Por índice (entero)
df.loc[0]           # Por etiqueta (si el índice no es entero)

df.loc[0, "Edad"]   # Valor específico

'''
5. Filtrado de datos
'''
# Personas mayores de 30
df[df["Edad"] > 30]

# Personas que se llaman Ana
df[df["Nombre"] == "Ana"]

'''
6. Modificación de datos
Agregar columnas
'''

df["Salario"] = [30000, 35000, 40000]

'''
Modificar valores
'''

df.loc[1, "Edad"] = 31

'''
Eliminar columnas o filas
'''

df.drop("Salario", axis=1, inplace=True)   # Columna
df.drop(2, axis=0, inplace=True)           # Fila

'''
7. Métodos comunes
Resumen y estadísticas
'''

df.mean()             # Promedio de columnas numéricas
df["Edad"].max()      # Máximo de una columna
df["Edad"].min()      # Mínimo
df["Edad"].value_counts()  # Frecuencias

'''
Detección de nulos
'''
df.isnull()         # Devuelve True donde hay nulos
df.isnull().sum()   # Cuenta de nulos por columna

'''
Rellenar o eliminar nulos
'''

df.fillna(0)        # Reemplaza nulos por 0
df.dropna()         # Elimina filas con nulos

'''
Ordenar
'''

df.sort_values("Edad")               # Ascendente
df.sort_values("Edad", ascending=False)  # Descendente

'''
Agrupar (groupby)
'''
# Promedio por ciudad
df.groupby("Ciudad").mean()

# Contar cuántos por grupo
df.groupby("Ciudad").size()

'''
Lectura y escritura de archivos
'''
# Leer CSV o Excel
df = pd.read_csv("archivo.csv")
df = pd.read_excel("archivo.xlsx")

# Escribir a archivo
df.to_csv("resultado.csv", index=False)
df.to_excel("resultado.xlsx", index=False)

'''
8. Ejemplos para clase
✅ Crear un DataFrame y explorar datos
'''

data = {
    "Nombre": ["Ana", "Luis", "Carlos", "Lucía"],
    "Edad": [25, 30, 35, 28],
    "Ciudad": ["CDMX", "Guadalajara", "CDMX", "Monterrey"]
}
df = pd.DataFrame(data)

print(df.head())
print(df.describe())

'''
✅ Filtrar personas mayores de 30
'''

print(df[df["Edad"] > 30])

'''
✅ Agregar columna con salario y calcular promedio
'''

df["Salario"] = [30000, 40000, 50000, 35000]
print("Promedio de salario:", df["Salario"].mean())

'''
✅ Agrupar por ciudad y contar cuántos hay en cada una
'''

conteo = df.groupby("Ciudad").size()
print(conteo)

'''
✅ Ordenar por salario
'''

df_ordenado = df.sort_values("Salario", ascending=False)
print(df_ordenado)

'''
9. Práctica (Ejercicios de fácil a intermedio)
Fáciles
Crear un DataFrame con nombres, edades y ciudades.

Mostrar las primeras 3 filas y las últimas 2.

Acceder a la columna “Edad”.

Mostrar la edad promedio del grupo.

Crear una nueva columna con un salario aleatorio.

Intermedios
Filtrar los registros con edad mayor a 30 años.

Ordenar el DataFrame por edad de forma descendente.

Crear una columna “Categoría” que diga “Mayor” si la edad > 30, y “Menor” en caso contrario.

Eliminar todas las filas con salario menor a 35000.

Agrupar por ciudad y mostrar el promedio de salarios por ciudad.
'''

'''
Resumen de métodos clave
Método	Descripción
df.head()	Primeras filas
df.info()	Información del DataFrame
df.describe()	Estadísticas numéricas
df.loc[], iloc[]	Acceso a filas y columnas
df["col"]	Acceder a una columna
df.sort_values()	Ordenar por columna
df.groupby()	Agrupar por categoría
df.isnull()	Detectar nulos
df.fillna()	Rellenar nulos
df.dropna()	Eliminar nulos
'''