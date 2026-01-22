
# ===============================================================
# 19.- ARCHIVOS: MATPLOTLIB — BÁSICOS + INTEGRACIÓN CON NUMPY/PANDAS
# ===============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# B) FUNDAMENTOS PYLOT (plt) — (plt.show() comentado para scripts)
# ---------------------------------------------------------------

# Scatter

# Barras

# Histograma

# Boxplot

# Subplots

# ---------------------------------------------------------------
# C) INTEGRACIÓN CON NUMPY/PANDAS + DATASETS PRE-CARGADOS
# ---------------------------------------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = np.array([12, 14, 15, 18, 22, 25, 23, 20, 19, 17, 16, 18], dtype=float)

# Con NumPy (línea):

# Con pandas (barras):

# Guardar figura:

#Generar un gráfico 3d de muestra:
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()



# ---------------------------------------------------------------
# D) BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Una figura por idea; títulos y etiquetas claras.
# - Leyendas legibles; grid/ticks cuando aporten.
# - Guardar con savefig para reportes reproducibles.