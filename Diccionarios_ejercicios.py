'''📌 Ejercicios Fáciles
1️⃣ Crear un diccionario de una persona y mostrar su información'''

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Imprimir cada clave y valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

'''📌 Salida esperada:
nombre: Juan
edad: 30
ciudad: Madrid
profesion: Ingeniero'''


'''
2️⃣ Comprobar si una clave existe en un diccionario
'''
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

clave = input("Ingresa la clave a buscar: ")

if clave in coche:
    print(f"La clave '{clave}' está en el diccionario con el valor: {coche[clave]}")
else:
    print(f"La clave '{clave}' no está en el diccionario.")

'''📌 Ejemplo de entrada/salida:

Ingresa la clave a buscar: color
La clave 'color' no está en el diccionario.
'''

'''
3️⃣ Contar la frecuencia de palabras en una frase
'''

frase = input("Ingresa una frase: ")
palabras = frase.split()

# Crear un diccionario de frecuencias
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)

'''
📌 Ejemplo de entrada/salida:

Ingresa una frase: hola mundo hola
{'hola': 2, 'mundo': 1}
'''


'''
📌 Ejercicios Nivel Medio
4️⃣ Fusionar dos diccionarios
'''

dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}

dic1.update(dic2)
print(dic1)

'''
📌 Salida esperada:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''

'''
5️⃣ Invertir un diccionario (Intercambiar claves y valores)
'''

diccionario = {'a': 1, 'b': 2, 'c': 3}

invertido = {valor: clave for clave, valor in diccionario.items()}
print(invertido)
'''
📌 Salida esperada:
{1: 'a', 2: 'b', 3: 'c'}
'''

'''
6️⃣ Contar la cantidad de cada letra en una palabra
'''
palabra = input("Ingresa una palabra: ")

conteo = {}

for letra in palabra:
    conteo[letra] = conteo.get(letra, 0) + 1

print(conteo)
'''
📌 Ejemplo de entrada/salida:
Ingresa una palabra: banana
{'b': 1, 'a': 3, 'n': 2}
'''

'''
7️⃣ Crear un diccionario de cuadrados de números
'''

n = int(input("Ingresa un número: "))

cuadrados = {i: i**2 for i in range(1, n+1)}
print(cuadrados)

'''
📌 Ejemplo de entrada/salida:
Ingresa un número: 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''


'''
8️⃣ Sumar los valores de un diccionario
'''
notas = {'matemáticas': 85, 'historia': 90, 'física': 78}

suma_total = sum(notas.values())
print(f"Suma total: {suma_total}")
'''
📌 Salida esperada:
Suma total: 253
'''

'''
9️⃣ Encontrar la clave con el valor máximo
'''
ventas = {'Juan': 1200, 'Ana': 2500, 'Luis': 1800}

mejor_vendedor = max(ventas, key=ventas.get)
print(f"Mejor vendedor: {mejor_vendedor} con {ventas[mejor_vendedor]} ventas.")
'''
📌 Salida esperada:
Mejor vendedor: Ana con 2500 ventas.
'''