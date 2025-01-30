'''¿Qué es una función en programación?
Una función en programación es un bloque de código reutilizable que realiza una tarea específica. Nos permite dividir el código en partes más pequeñas y organizadas, lo que facilita la lectura, el mantenimiento y la reutilización del código.

Las funciones pueden recibir entradas llamadas parámetros y devolver un resultado utilizando la palabra clave return.
'''

# Definición de una función que suma dos números
def suma(a, b):
    return a + b  # Devuelve la suma de los dos números

# Llamando a la función e imprimiendo el resultado
resultado = suma(3, 5)
print("La suma de 3 y 5 es:", resultado)

#Función sin parámetros
def saludar():
    print("¡Hola, bienvenido a la clase!")

saludar()  # Llamamos a la función

# Ejemplo con una función que devuelve un valor

def cuadrado(numero):
    return numero ** 2  # Calcula el cuadrado de un número

print("El cuadrado de 4 es:", cuadrado(4))

# Parámetros opcionales

def presentar(nombre, edad=18):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

presentar("Carlos", 25)  # Llamada con dos parámetros
presentar("Ana")  # Llamada con un solo parámetro, usa el valor por defecto 18

