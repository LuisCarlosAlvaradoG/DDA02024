
# ===============================================================
# 19.- ARCHIVOS: MATPLOTLIB — BÁSICOS + INTEGRACIÓN CON NUMPY/PANDAS
# ===============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# B) FUNDAMENTOS PYLOT (plt) — (plt.show() comentado para scripts)
# ---------------------------------------------------------------
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure() # Aquí empieza la figura
plt.plot(x, y, label = "Sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sin")
plt.legend()
plt.show() # Aquí termina la figura

# Scatter
xs = np.array([1, 2, 3, 4, 5])
ys = np.array([2, 1, 3, 5, 4])

plt.figure() 
plt.plot(xs, ys, label = "Linea", color = "#37F308")
plt.scatter(xs, ys, label = "Puntos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter PLot")
plt.legend()
plt.savefig("Puntos_y_lineas") # Guarda la imagen con el nombre que le dé
plt.show()

# Barras
nombres = np.array(["A", "B", "C"])
vals = np.array([15, 20, 12])

plt.figure() 
plt.bar(nombres, vals, label = "Barras", color = "#E2DFDF")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")
plt.title("Gráfico de Barras")
plt.legend()
plt.show()

# Histograma
data = np.random.randn(100_000)

plt.figure() 
plt.hist(data, bins = 1000, label= "Dist. Normal Estándar")
plt.xlabel("Datos")
plt.ylabel("Frecuencias")
plt.title("Histograma")
plt.legend()
plt.show()

# Boxplot
x1 = np.random.randn(100)
x2 = np.random.randn(100) + 1.5
x3 = np.random.randn(100) - 1.5

plt.figure() 
plt.boxplot(label=["X1", "X2", "X3"], x = [x1, x2, x3])
plt.xlabel("Grupo")
plt.ylabel("Cantidad")
plt.title("Boxplot")
plt.legend()
plt.show()

# Subplots
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(1, 2, figsize = (8, 3))
ax[0].plot(x, y1)
ax[0].set_title("Sin(x)")
ax[1].plot(x, y2)
ax[1].set_title("Cos(x)")
fig.title("Trigonometría")
plt.show()


# ---------------------------------------------------------------
# C) INTEGRACIÓN CON NUMPY/PANDAS + DATASETS PRE-CARGADOS
# ---------------------------------------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = np.array([12, 14, 15, 18, 22, 25, 23, 20, 19, 17, 16, 18], dtype=float)
df_sales = pd.DataFrame({
    "Months" : months,
    "Sales" : sales
})
df_sales

# Con NumPy (línea):
plt.figure() 
plt.plot(np.arange(12), sales, marker = "o")
plt.xticks(np.arange(12), months)
plt.title("Ventas Mensuales")
plt.show()

# Con pandas (barras):
plt.figure() 
plt.bar(df_sales["Months"], df_sales["Sales"], label =  "Ventas")
plt.title("Ventas Mensuales")
plt.legend()
plt.show()

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