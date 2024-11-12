# ESTRUCTURAS SECUENCIALES

print("¡Hola Mundo!")

nombre = "Luis"
edad = 24

print("Hola:", nombre, "tienes", edad, "años")

n1 = 10
n2 = 20
n3 = 30

suma = n1 + n2 + n3
suma
resta = n3 - n2 - n1
print(resta)
n3 # el valor de la variable no se modifica, a pesar de haber hecho una operación con esa variable

multiplicacion = n1 * n2 * n3
multiplicacion

division = n1/ n2 / n3
division

cadena = "Hola, buenos días. ¿Cómo estás?"
cadena
print(cadena)

print("Cadena en mayúsculas:", cadena.upper())
print("Cadena en mayúsculas:", cadena.lower())

#Ejercicio examen 1
celsius = 30
conversion = 3 #1 hace referencia a Fahrenheit, 2 hace referencia a Klevin 
if conversion == 1:
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en Fahrenheint es:", fahrenheit)
elif conversion == 2:
    kelvin = 273.15 + celsius
    print("La temperatura en Kelvin es:", kelvin)
else:
    print("Valor no reconocido")

#Ejercicio examen 1
peso = 80
altura = 1.80
imc = peso / altura ** 2
if imc >= 30:
    print("Tu IMC es:", imc,"Obesidad")
elif 30 > imc >= 25:
    print("Tu IMC es:", imc,"Sobrepeso")
elif 25 > imc >= 18.5:
    print("Tu IMC es:", imc,"Peso normal")
else:
    print("Tu IMC es:", imc,"Bajo peso")
    
#Funciones
def saludar(nombre, edad = 18):
    return f"Hola, {nombre}"

saludar("German", 20)

def promedio_edades(lista_edades):
    promedio = sum(lista_edades) / len(lista_edades)
    return promedio #f"El promedio de edades es, {promedio}"
promedio_edades([19, 18, 18, 18])
promedio = promedio_edades([19, 18, 18, 18])
promedio

