'''
Pandas

Pandas es una librería para análisis y manipulación de datos tabulares.

Está basada un Numpy y se utiliza en ciencia de datos, análisis financiero, ingeniería, etc.

Ventajas: 
* Trabaja con datos tabulares (como Excel)
* Acceso sencillo a filas y columnas
* Limpieza y transformación de datos
* Soporte para lectura y escritura de archivos (CSV, Excel, SQL)
'''

'''
Estructura principal
Serie (1D)
'''

#pip install pandas
#pip3 install pandas

import pandas as pd

serie = pd.Series([10,20,30], index=["a","b","c"])
print(serie)

'''
Estructura DataFrame (2D)
'''

datos = {
    "Nombre": ["Ariane", "David", "Diego", "Barba", "Gael", "Mariana", "Ari", "Alex", "Regina", "Jesús"],
    "Edad": [ 18, 20, 21, 18, 18, 20, 18, 19, 21, 18]
}

df = pd.DataFrame(datos)
df

'''
Exploración de datos
'''

df.head() #Primeras 5 filas
df.head(3) #Primeras 3 filas

df.tail() # Últimas 5 filas
df.tail(3) # Últimas 3 filas

df.shape # (filas, columnas)

df.columns # Nombres de columnas

df.index #Índice de las filas

df.info() #Resumen general

df.describe() #Estadísticas básicas

estadisticas = df.describe()
type(estadisticas)
print(estadisticas)
#Media de la edad
print(f"La edad promedio del grupo es {estadisticas.loc['mean', 'Edad']}")

'''
Acceso a datos
'''
df

# Columnas
df["Edad"] # Serie(Columna)
df[["Nombre", "Edad"]] #Múltiples columnas

#Filas
df.iloc[0] # Uso iloc para acceder por índice
df.iloc[0][0] #Warning Future deprecated

df.loc[0] # Uso loc para acceder por etiqueta (si el indice no es un entero)

estadisticas
estadisticas.loc["mean"] # .loc con uso de etiqueta en un DataFrame 

# Valores específicos
df
df.loc[0, "Edad"]
df.iloc[0, 1] # fila , columna
df.iloc[0:5, 1] # Múltiples datos
df.iloc[0:5, 0:2] # Sub matriz

'''
Filtrado de datos
'''
#Filtrando a los que son mayores de 20 años
df[df["Edad"] > 20]
#Filtrado a personas que se llamen David
df[df["Nombre"] == "David"]
#Combinaciones de condiciones
df[(df["Edad"] > 20) & (df["Nombre"] == "David")] # and se sustituye por & y el or por | y las condiciones van entre paréntesis
df[(df["Edad"] > 20) | (df["Nombre"] == "David")] 

'''
Eliminar columnas o filas
'''

# Axis 0 son filas, axis 1 son columnas
df.drop("Nombre", axis = 1, inplace=True) #Eliminar la columna nombre
df

df.drop(5, axis = 0, inplace= True)
df

df.drop(8, axis = 0, inplace = False)
df