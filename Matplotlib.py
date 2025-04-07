# Matplotlib.pyplot: Teoría + Ejemplos + Ejercicios

'''
1. ¿Qué es matplotlib.pyplot?
matplotlib.pyplot es un módulo de la biblioteca matplotlib que proporciona una interfaz sencilla y similar a MATLAB para crear gráficos estáticos en 2D. Es ampliamente usado en visualización de datos, análisis estadístico y ciencia de datos.

Ventajas
Crea gráficos de líneas, barras, pastel, dispersión, histogramas, etc.

Totalmente personalizable (colores, etiquetas, estilos).

Compatible con pandas y NumPy.

Se integra bien en Jupyter Notebooks.
'''

'''
2. Importación estándar
'''

import matplotlib.pyplot as plt

'''
3. Flujo básico para crear gráficos
'''

# 1. Preparar los datos
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# 2. Graficar
plt.plot(x, y)

# 3. Mostrar
plt.show()

'''
4. Gráficos comunes
Línea
'''

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Gráfico de línea")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid()
plt.show()

'''
Barras
'''

nombres = ["Ana", "Luis", "Carlos"]
valores = [10, 15, 7]

plt.bar(nombres, valores)
plt.title("Ventas por persona")
plt.ylabel("Ventas")
plt.show()

'''
Barras horizontales
'''

plt.barh(nombres, valores)
plt.title("Ventas por persona (horizontal)")
plt.xlabel("Ventas")
plt.show()

'''
Gráfico de pastel
'''

etiquetas = ["Python", "Java", "C++"]
tamaños = [50, 30, 20]

plt.pie(tamaños, labels=etiquetas, autopct="%1.1f%%")
plt.title("Lenguajes más usados")
plt.show()

'''
Dispersión (scatter)
'''

x = [1, 2, 3, 4]
y = [10, 15, 13, 17]

plt.scatter(x, y)
plt.title("Gráfico de dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

'''
Histograma
'''

import numpy as np

datos = np.random.randn(1000)

plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

'''
5. Personalización básica
'''

plt.plot(x, y, color="red", linestyle="--", marker="o", label="línea roja")
plt.legend()
plt.title("Ejemplo completo")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

'''
6. Guardar una gráfica como imagen
'''

plt.plot(x, y)
plt.savefig("grafico.png")  # También puedes usar .jpg, .svg, etc.
plt.show()

'''
7. Varios gráficos en una figura
Subplots (1 fila, 2 columnas)
'''

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Gráfico 1")

plt.subplot(1, 2, 2)
plt.bar([1, 2, 3], [4, 5, 6])
plt.title("Gráfico 2")

plt.tight_layout()
plt.show()

'''
8. Ejemplos para clase
✅ Gráfico combinado de líneas
'''

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

plt.plot(x, y1, label="Cuadrado")
plt.plot(x, y2, label="Inverso")
plt.legend()
plt.title("Comparación de funciones")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

'''
✅ Comparar ingresos por ciudad
'''

ciudades = ["CDMX", "Monterrey", "Guadalajara"]
ingresos = [50000, 48000, 51000]

plt.bar(ciudades, ingresos, color="green")
plt.title("Ingresos por ciudad")
plt.ylabel("Ingreso promedio")
plt.show()

'''
✅ Pie chart de participación de mercado
'''

etiquetas = ["Apple", "Samsung", "Huawei", "Otros"]
valores = [35, 30, 20, 15]

plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90)
plt.title("Participación de mercado")
plt.axis("equal")  # Hacer el círculo perfecto
plt.show()

'''
9. Ejercicios de práctica
Fáciles
Crear un gráfico de línea que muestre el crecimiento de ventas durante 6 meses.

Graficar un histograma de 1000 números aleatorios.

Hacer un gráfico de barras con las edades de 5 personas.

Mostrar un gráfico de pastel con distribución de calificaciones.

Intermedios
Graficar dos líneas en la misma figura con leyenda.

Crear un subplot con un gráfico de barras y un gráfico de línea.

Exportar un gráfico como imagen .png.

Hacer un gráfico de dispersión que compare altura y peso de personas.

Personalizar un gráfico con títulos, etiquetas, líneas punteadas y marcadores.

Crear un gráfico donde se muestre la evolución de dos países en exportaciones (líneas superpuestas).
'''

'''
10. Resumen de funciones clave
Función	Descripción

plt.plot()	Gráfico de líneas
plt.bar() / barh()	Gráfico de barras
plt.pie()	Gráfico de pastel
plt.scatter()	Gráfico de dispersión
plt.hist()	Histograma
plt.title()	Título del gráfico
plt.xlabel()	Etiqueta del eje X
plt.ylabel()	Etiqueta del eje Y
plt.legend()	Mostrar leyenda
plt.grid()	Mostrar cuadrícula
plt.savefig()	Guardar gráfico como imagen
plt.subplot()	Dividir la figura en subgráficos
plt.show()	Mostrar la figura
'''