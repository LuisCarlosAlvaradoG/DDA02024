'''
1. Introducción a la compresión de listas
La compresión de listas es una forma concisa y legible de crear listas a partir de iterables existentes. 
Permite generar nuevas listas aplicando una expresión y, opcionalmente, filtrando elementos mediante condiciones, 
en una sola línea de código. Esta técnica no solo hace el código más compacto, 
sino que también puede resultar en mejoras de rendimiento frente a los bucles tradicionales.

2. Sintaxis de la compresión de listas
La estructura general de una compresión de listas es:
'''

# [ expresión for elemento in iterable if condición ]

'''
expresión: Es la transformación o cálculo que se aplicará a cada elemento.
for elemento in iterable: Recorre cada elemento del iterable.
if condición (opcional): Permite incluir solo aquellos elementos que cumplan la condición especificada.
'''

'''
Ejemplo básico:
'''

cuadrados = [x**2 for x in range(10)]
print(cuadrados)
# Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
3. Ejemplos prácticos
3.1. Compresión sin condición
Si queremos transformar cada elemento de un iterable, podemos hacerlo directamente:
'''

# Convertir una lista de números a sus dobles
numeros = [1, 2, 3, 4, 5]
dobles = [num * 2 for num in numeros]
print(dobles)
# Salida: [2, 4, 6, 8, 10]

'''
3.2. Compresión con condición (filtrado)
Podemos filtrar elementos utilizando una condición después del ciclo for:
'''

# Crear una lista con solo números pares
pares = [x for x in range(20) if x % 2 == 0]
print(pares)
# Salida: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

'''
3.3. Uso de if-else dentro de la expresión
Cuando se requiere aplicar una transformación diferente según una condición, 
se puede usar la expresión if-else dentro de la compresión. 
Es importante notar que la sintaxis difiere ligeramente: el if-else se coloca antes del for:
'''

# Asignar "Par" o "Impar" dependiendo de cada número
clasificacion = ["Par" if x % 2 == 0 else "Impar" for x in range(10)]
print(clasificacion)
# Salida: ['Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar']

'''
3.4. Compresiones anidadas
Las compresiones de listas también se pueden anidar para trabajar con estructuras 
de datos multidimensionales o combinar varios iterables.
'''

'''
Ejemplo: Crear una matriz (lista de listas)
'''

# Generar una matriz 3x3 con números del 0 al 8
matriz = [[j + i * 3 for j in range(3)] for i in range(3)]
for fila in matriz:
    print(fila)
# Salida:
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

'''
Ejemplo: Combinación de dos listas con zip
'''

nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 22]
info = [f"{nombre} tiene {edad} años" for nombre, edad in zip(nombres, edades)]
print(info)
# Salida: ['Ana tiene 25 años', 'Luis tiene 30 años', 'Pedro tiene 22 años']

'''
4. Consideraciones prácticas
Legibilidad: Aunque las comprensiones de listas hacen el código más compacto, 
en casos de lógica compleja o anidamientos muy profundos, 
puede resultar menos legible que un bucle for tradicional. 
Es importante balancear la concisión con la claridad del código.

Eficiencia: Las comprensiones de listas son generalmente más rápidas que los bucles for convencionales, 
ya que están optimizadas en Python. 
Sin embargo, para tareas muy pesadas, 
es posible considerar el uso de generadores (expresiones generadoras) para ahorrar memoria.

Uso de variables temporales: Dentro de la compresión, 
es recomendable utilizar nombres de variables descriptivos para evitar confusiones, 
especialmente en comprensiones anidadas.

Anidamiento excesivo: Si se detecta que la compresión se vuelve muy anidada o difícil de entender, 
es preferible refactorizar el código en funciones o bucles separados para mejorar la mantenibilidad.
'''

'''
5. Comparación con bucles for tradicionales
Mientras que un bucle for tradicional permite escribir pasos intermedios, 
imprimir mensajes o realizar múltiples operaciones en cada iteración, 
la compresión de listas se enfoca en transformar y filtrar datos en una sola expresión. 
Por ejemplo, el siguiente código con un bucle for:
'''

result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)
print(result)
'''
Se puede reescribir de forma compacta como:
'''

result = [x**2 for x in range(10) if x % 2 == 0]
print(result)

'''
La compresión de listas favorece la escritura de código declarativo, 
donde se especifica el resultado deseado en lugar de detallar el proceso paso a paso.
'''