import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lista de nombres
nombres = [
    "BARBA", "CHAVEZ", "GAEL DLF", 
    "DIEGO", "ARIANE", "JESUS", 
    "GAEL J", "MAGA", "SANTIAGO", 
    "JUAN PABLO", "MARIANA", "ALAN", 
    "DAVID", "ROBERTO", "ARIANA", 
    "IKER", "ALEJANDRO", "RODRIGO"
]

# Dimensiones de la matriz
filas, columnas = 5, 6

# Crear matriz vacía con "VACÍO" en las filas 2 y 4
matriz = np.full((filas, columnas), "VACÍO", dtype=object)

# Mezclar los nombres
random.shuffle(nombres)

# Distribuir nombres en filas 1, 3 y 5 (índices 0, 2, 4)
nombre_idx = 0
for i in [0, 2, 4]:  # Filas 1, 3 y 5
    for j in range(columnas):
        if nombre_idx < len(nombres):
            matriz[i, j] = nombres[nombre_idx]
            nombre_idx += 1

# Agregar fila superior con "Escritorio" en la primera columna y espacios vacíos en las demás
fila_escritorio = np.array(["---ESCRITORIO---"] + ["" for _ in range(columnas - 1)])
matriz = np.vstack([fila_escritorio, matriz])

# Crear DataFrame para visualización
df_matriz = pd.DataFrame(matriz)

# Función para plotear la matriz
def plot_matriz(matriz):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            ax.text(j, -i, matriz[i, j], ha='center', va='center', fontsize=8, bbox=dict(facecolor='white', edgecolor='black'))
    
    plt.xlim(-0.5, matriz.shape[1]-0.5)
    plt.ylim(-matriz.shape[0]+0.5, 0.5)
    plt.show()

# Mostrar la matriz en texto
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
print(df_matriz.to_string(index=False, header=False))

# Plotear la matriz
plot_matriz(matriz)