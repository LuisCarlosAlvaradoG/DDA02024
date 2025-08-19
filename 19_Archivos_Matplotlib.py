
# ===============================================================
# 19.- ARCHIVOS: MATPLOTLIB — BÁSICOS + INTEGRACIÓN CON NUMPY/PANDAS
# Curso: Algoritmos y Programación (Python) — Sesión (~3 horas)
# Teoría: español | Código: inglés
# Librerías: matplotlib + NumPy + pandas (sin seaborn).
# ===============================================================

"""
A) Objetivos
B) Fundamentos pyplot: figure, axes, plot, scatter, bar, hist, box, subplots
C) Etiquetas/títulos/leyendas/ticks; savefig
D) Integración con NumPy y pandas (datasets precargados)
E) Casos guiados
F) Buenas prácticas
G) Banco de ejercicios (SOLUCIONES incluidas)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# A) OBJETIVOS
# ---------------------------------------------------------------
# - Graficar líneas, dispersión, barras, histogramas, boxplots.
# - Personalizar etiquetas, títulos, leyendas y ejes.
# - Usar subplots y guardar figuras.
# - Consumir datos desde NumPy y pandas.

# ---------------------------------------------------------------
# B) FUNDAMENTOS PYLOT (plt) — (plt.show() comentado para scripts)
# ---------------------------------------------------------------
x = np.linspace(0, 2*np.pi, 100); y = np.sin(x)
# plt.figure(); plt.plot(x, y, label="sin(x)"); plt.xlabel("x"); plt.ylabel("y"); plt.title("Sine"); plt.legend(); # plt.show()

# Scatter
# xs = np.array([1,2,3,4,5]); ys = np.array([2,1,3,5,4])
# plt.figure(); plt.scatter(xs, ys, label="points"); plt.legend(); plt.title("Scatter demo"); # plt.show()

# Barras
# labels = ["A","B","C"]; vals = [10, 15, 7]
# plt.figure(); plt.bar(labels, vals); plt.title("Bar chart"); # plt.show()

# Histograma
# data = np.random.randn(200)
# plt.figure(); plt.hist(data, bins=20); plt.title("Histogram"); # plt.show()

# Boxplot
# plt.figure(); plt.boxplot([np.random.randn(100), np.random.randn(100)+1.5]); plt.title("Two-box comparison"); # plt.show()

# Subplots
# fig, ax = plt.subplots(1,2, figsize=(8,3))
# ax[0].plot(x, y); ax[0].set_title("Sin")
# ax[1].plot(x, np.cos(x)); ax[1].set_title("Cos")
# fig.suptitle("Trigonometry"); # plt.show()

# ---------------------------------------------------------------
# C) INTEGRACIÓN CON NUMPY/PANDAS + DATASETS PRE-CARGADOS
# ---------------------------------------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = np.array([12, 14, 15, 18, 22, 25, 23, 20, 19, 17, 16, 18], dtype=float)
df_sales = pd.DataFrame({"month": months, "sales": sales})

# Con NumPy (línea):
# plt.figure(); plt.plot(np.arange(12), sales, marker="o"); plt.xticks(np.arange(12), months); plt.title("Monthly Sales (NumPy)"); # plt.show()

# Con pandas (barras):
# ax = df_sales.plot(x="month", y="sales", kind="bar", legend=False, title="Monthly Sales (pandas)"); # plt.show()

# Guardar figura:
# plt.figure(); plt.plot(sales); plt.title("Savefig example"); plt.savefig("sales_plot.png")

# ---------------------------------------------------------------
# D) CASOS GUIADOS CON DATASETS
# ---------------------------------------------------------------
def create_people_dataset():
    rows = [
        "id,age,height,weight,city,gender",
        "1,21,1.65,60,CDMX,F",
        "2,19,1.72,72,Monterrey,M",
        "3,22,1.58,55,Guadalajara,F",
        "4,20,1.80,80,CDMX,M",
        "5,21,1.70,65,Guadalajara,F",
        "6,23,1.75,77,CDMX,M"
    ]
    with open("people_mpl.csv","w",encoding="utf-8") as f:
        for r in rows: f.write(r+"\n")

# create_people_dataset()
# df = pd.read_csv("people_mpl.csv")
# # Dispersión altura vs. peso por género:
# plt.figure()
# m = df["gender"]=="M"
# plt.scatter(df.loc[m,"height"], df.loc[m,"weight"], label="M")
# plt.scatter(df.loc[~m,"height"], df.loc[~m,"weight"], label="F")
# plt.xlabel("height"); plt.ylabel("weight"); plt.legend(); plt.title("Height vs Weight")
# # plt.show()

# # Boxplot de peso por ciudad
# plt.figure()
# groups = [df[df["city"]=="CDMX"]["weight"], df[df["city"]=="Monterrey"]["weight"], df[df["city"]=="Guadalajara"]["weight"]]
# plt.boxplot(groups, labels=["CDMX","Monterrey","Guadalajara"])
# plt.title("Weight by City")
# # plt.show()

# ---------------------------------------------------------------
# E) BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Una figura por idea; títulos y etiquetas claras.
# - Leyendas legibles; grid/ticks cuando aporten.
# - Guardar con savefig para reportes reproducibles.

# ---------------------------------------------------------------
# F) BANCO DE EJERCICIOS (SOLUCIONES) — 25 EJERCICIOS
# ---------------------------------------------------------------

# 01) Línea NumPy: sin(x)
x = np.linspace(0, 2*np.pi, 200); y = np.sin(x)
# plt.figure(); plt.plot(x, y, label="sin(x)"); plt.legend(); plt.title("Sine")

# 02) Dos curvas en el mismo eje
# plt.figure(); plt.plot(x, np.sin(x), label="sin"); plt.plot(x, np.cos(x), label="cos"); plt.legend(); plt.title("Sin & Cos")

# 03) Scatter aleatorio
# np.random.seed(0); xr = np.random.randn(200); yr = 0.5*xr + np.random.randn(200)*0.5
# plt.figure(); plt.scatter(xr, yr); plt.title("Random Scatter")

# 04) Barras categóricas
# labels = ["A","B","C"]; vals = [10,5,7]
# plt.figure(); plt.bar(labels, vals); plt.title("Bars")

# 05) Histograma
# data = np.random.randn(300)
# plt.figure(); plt.hist(data, bins=20); plt.title("Histogram")

# 06) Boxplot dos distribuciones
# A = np.random.randn(100); B = np.random.randn(100)+1.5
# plt.figure(); plt.boxplot([A,B], labels=["A","B"]); plt.title("Boxplot")

# 07) Subplots 1x2
# fig, ax = plt.subplots(1,2, figsize=(8,3)); ax[0].plot(x, np.sin(x)); ax[0].set_title("Sin"); ax[1].plot(x, np.cos(x)); ax[1].set_title("Cos"); fig.suptitle("Trig")

# 08) Guardar figura con savefig
# plt.figure(); plt.plot(np.linspace(0,1,50), np.linspace(0,1,50)**2); plt.title("Quadratic"); plt.savefig("quadratic.png")

# 09) Barras apiladas
# labels = ["Jan","Feb","Mar"]; A = [5,3,4]; B = [2,4,1]
# plt.figure(); plt.bar(labels, A, label="A"); plt.bar(labels, B, bottom=A, label="B"); plt.legend(); plt.title("Stacked Bars")

# 10) Ticks personalizados
# xv = np.linspace(0, 10, 50); yv = np.log1p(xv)
# plt.figure(); plt.plot(xv,yv); plt.xticks([0,5,10], ["zero","five","ten"]); plt.title("Custom Ticks")

# 11) Línea con marcadores
# plt.figure(); plt.plot(x, np.sin(x), marker="o"); plt.title("Line with markers")

# 12) Error bars
# xv = np.arange(5); yv = np.array([10,12,9,14,11]); e = np.array([1,2,1,1,2])
# plt.figure(); plt.errorbar(xv, yv, yerr=e, fmt="-o"); plt.title("Error Bars")

# 13) Scatter por categoría
# xx = np.linspace(0, 1, 30); yy = xx + np.random.randn(30)*0.1; c = np.array(["A"]*15 + ["B"]*15)
# plt.figure(); plt.scatter(xx[c=="A"], yy[c=="A"], label="A"); plt.scatter(xx[c=="B"], yy[c=="B"], label="B"); plt.legend(); plt.title("Two categories")

# 14) Hist comparación
# A = np.random.randn(300); B = np.random.randn(300)+1
# plt.figure(); plt.hist(A, bins=25, alpha=0.5, label="A"); plt.hist(B, bins=25, alpha=0.5, label="B"); plt.legend(); plt.title("Two Hists")

# 15) Subplots 2x2
# fig, ax = plt.subplots(2,2, figsize=(8,6))
# ax[0,0].plot(x, np.sin(x)); ax[0,0].set_title("sin")
# ax[0,1].plot(x, np.cos(x)); ax[0,1].set_title("cos")
# ax[1,0].plot(x, np.tan(x)); ax[1,0].set_title("tan")
# ax[1,1].plot(x, np.sinh(x)); ax[1,1].set_title("sinh")
# fig.suptitle("Functions")

# 16) Barras desde pandas
# dfb = pd.DataFrame({"city":["A","B","C"],"sales":[10,15,7]})
# ax = dfb.plot(x="city", y="sales", kind="bar", legend=False, title="Sales by City")

# 17) Línea pandas con fechas
# days = pd.date_range("2023-01-01", periods=10, freq="D"); vals = np.cumsum(np.random.randn(10))
# dft = pd.DataFrame({"day":days,"value":vals}); ax = dft.plot(x="day", y="value", legend=False, title="Trend")

# 18) Barras horizontales
# labels = ["A","B","C"]; vals = [4,7,2]
# plt.figure(); plt.barh(labels, vals); plt.title("Horizontal Bars")

# 19) Múltiples líneas
# t = np.arange(6); plt.figure(); plt.plot(t, t, label="x"); plt.plot(t, t**2, label="x^2"); plt.plot(t, t**3, label="x^3"); plt.legend(); plt.title("Powers")

# 20) Boxplot por grupos (pandas)
# dfb = pd.DataFrame({"group":["A"]*50 + ["B"]*50, "val": np.r_[np.random.randn(50), np.random.randn(50)+1]})
# plt.figure(); plt.boxplot([dfb[dfb["group"]=="A"]["val"], dfb[dfb["group"]=="B"]["val"]], labels=["A","B"]); plt.title("Box by Group")

# 21) Hist densidad
# data = np.random.randn(500); plt.figure(); plt.hist(data, bins=30, density=True); plt.title("Density Hist")

# 22) Scatter con tamaño variable
# xx = np.linspace(0, 1, 30); yy = xx + np.random.randn(30)*0.1; sizes = (np.arange(30)+1)*10
# plt.figure(); plt.scatter(xx, yy, s=sizes); plt.title("Sizes")

# 23) Anotar máximo
# yy = np.sin(x); mx_i = yy.argmax()
# plt.figure(); plt.plot(x,yy); plt.scatter([x[mx_i]],[yy[mx_i]]); plt.text(x[mx_i], yy[mx_i], " max", va="bottom", ha="left"); plt.title("Annotate Max")

# 24) Grid
# xv = np.linspace(0,1,50); yv = np.sqrt(xv)
# plt.figure(); plt.plot(xv,yv); plt.grid(True); plt.title("Grid")

# 25) Subplots sharex
# fig, ax = plt.subplots(2,1, sharex=True); ax[0].plot(x, np.sin(x)); ax[1].plot(x, np.cos(x)); fig.suptitle("Share X")
