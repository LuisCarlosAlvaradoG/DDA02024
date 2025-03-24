'''
Ciclos FOR

El ciclo for es una estructura de control que permite iterar sobre elementos de una secuencia
(listas, cadena, tuplas, diccionarios y rangos)
'''

# Sintaxis básica
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

'''
elemento: Es la variable que tomará el valor de cada item en la secuencia
secuencia: Puede ser una lista, cadena, range, tupla, diccionario, etc.
'''

texto = "¡Hola!"
for i in texto:
    print(i)

frutas = ["manzana", "plátano", "uva"]
for i in frutas:
    print("La fruta es:", i)

#Ejercicio 1
'''
Calcular el cuadrado de cada elemento de una lista con ciclo for
'''
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento**2)
'''
Calcular el cuadrado de cada elemento de una lista 
con ciclo for y guardarlo en una nueva lista
'''
lista = [1, 2, 3, 4, 5]
lista2 = []
for elemento in lista:
    lista2.append(elemento**2)
print(lista2)

# list(map(lambda x: x**2,lista))

'''
Uso de la función range()
La función range() es muy util para generar secuencias de números,
especialmente cuando se desea iterar un número determinado de veces
'''
#Ejemplo básico
for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(start=2, stop=10, step=2):
    print(i)

lista2 = [1, 4, 9, 16, 25]
len(lista2)
for i in range(len(lista2)):
    print(lista2[i])

'''
enumerate()
La función enumerate() permite obtener tanto el índice como el elemento
al iterar sobre una secuencia
Esto es útil cuando necesitas conocer la posición de cada elemento
'''
colores = ["rojo","verde","azul"]
for indice, color in enumerate(colores):
    print(f"Indice: {indice}, Color: {color}")

colores = ["rojo","verde","azul"]
for indice, color in enumerate(colores, start=1):
    print(f"Indice: {indice}, Color: {color}")

colores = ["rojo","verde","azul"]
lista_nueva = []
for indice, color in enumerate(colores, start=1):
    lista_nueva.append([indice, color])

'''
zip()
zip() permite iterar en paralelo sobre 2 o más secuencias
Cada iteración devuelve una tupla con un elemento de cada secuencia
'''
nombres = ["Santiago","Alex","Jesús","Mariana","Chávez"]
edades = [19, 19, 18, 20, 23]
# tupla() , lista[]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

nombres = ["Santiago","Alex","Jesús","Mariana","Chávez"]
edades = [19, 19, 18, 20, 23]
estaturas = [190, 186, 180, 166, 185]
for nombre, edad, estatura in zip(nombres, edades, estaturas):
    print(f"{nombre} tiene {edad} años y mide {estatura} cms")

# Tip práctica 9
lista = eval(input())
type(lista)
# [1, 2, 3, 4, 5]
    
