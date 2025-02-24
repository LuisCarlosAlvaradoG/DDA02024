'''
Métodos de str comunes

En Python, los objetos de tipo str tienen varios métodos incirporados para realizar diversas operaciones. 
Aquí algunos de los métodos más utilizados para manipular cadenas

'''

'''
str.upper()
Convierte todos los caracteres en mayúsculas
'''
s = "hola"
# s = s.upper() #Se va a guardar la variable s en mayúsculas
print(s.upper())
# HOLA

'''
str.lower()
convierte todos los caracteras a minúsculas
'''
s = "Hola"
print(s.lower())
# hola

'''
str.capitalize()
Convierte el primer caracter en mayúsculas y el resto en minúsculas
'''
s = "hola mundo"
print(s.capitalize())

'''
str.title()
'''
s = "hola mundo"
print(s.title())

'''
s.strip()
Quita el espacio al principio de la cadena si es que existe
'''
s = " hola mundo"
print(s.strip())

'''
s.replace()
'''
s = " hola mundo"
print(s.replace("mundo","python"))

'''
s.split()
'''
s = " hola mundo"
print(s.split())

'''
str.join(iterable)
'''
s = " "
lista = ['hola','mundo']
print(s.join(lista))

'''
s.find(sub)
'''
s = "hola alumnos"
print(s.find('alumnos'))  

# Posición e índices
pos = s[5]
print(pos)

pos = s[-1]
print(pos)

ind = s[5:7]
print(ind)

ind = s[5:] #Del índice hasta el final
print(ind)

ind = s[:5] #Del índice hasta el final
print(ind)

ind = s[-5:-2]
print(ind)

ind = s[-2:-5]
print(ind)

inverso = s[::-1]
print(inverso)

# Determinar dada una palabra 
# ingresada por el usuario si es un palíndromo
palabra = input("Dame una palabra: ")

if (palabra == palabra[::-1]):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

palabra = "anita lava la tina"
palabra = palabra.replace(" ","")

'''
str.isdigit()
'''
s = '12345'
print(s.isdigit())

'''
str.isalpha()
'''
s = 'abc'
print(s.isalpha())

'''
str.isalnum()
'''
s = 'abc123'
print(s.isalnum())

# Estructuras selectivas anidadas

'''
Problema: Categoría de seguro médico
Si el cliente tiene más de 40 años y fuma, 
se le asigna la categoría "Riesgo Alto".
Si tiene más de 40 años y no fuma: "Riesgo"
Si es es menor de 40 y fuma: "Riesgo Medio"
Si es menor de 40 y no fuma: "Riesgo Bajo"

Las entradas son: edad (int), fuma(boolean)
'''
edad = int(input("Dame tu edad: "))
fumas = input("¿Fumas? SI/NO :")

if edad >= 40:
    if fumas.upper() == "SI":
        print("Riesgo Alto")
    else:
        print("Riesgo Medio")
else:
    if fumas.upper() == "SI":
        print("Riesgo Medio")
    else:
        print("Riesgo Bajo")

# LÓGICA CORRECTA
if edad >= 40 and fumas.upper() == "SI":
    print("Riesgo Alto")
elif edad < 40 and fumas.upper() == "NO":
    print("Riesgo Bajo")
else: 
    print("Riesgo Medio")
    

'''Problema 6: Sistema de Descuentos en un Supermercado
Descripción: Un supermercado ofrece diferentes descuentos según el tipo de cliente. 
Si el cliente es un "Cliente Premium",recibe un 10% de descuento en compras superiores a $100. 
Si es "Cliente Frecuente", recibe un 5% de descuento en compras superiores a $50. 
 Si es "Nuevo Cliente", no tiene descuentos. 
 El programa debe calcular el total a pagar después del descuento si aplica.

 ENTRADA: Tipo de cliente (str) Monto de compra (float)
'''
cliente = input("¿Qué tipo de cliente eres?: ")
monto = float(input("Monto de compra: "))

if cliente == "Premium":
    if monto > 100:
        total = monto * .9
        print(f"El monto total es {total}")
    else:
        total = monto
        print(f"El monto total es {total}")
elif cliente == "Frecuente":
    if monto > 50:
        total = monto * .95
        print(f"El monto total es {total}")
    else:
        total = monto
        print(f"El monto total es {total}")
else:
    total = monto
    print(f"El monto total es {total}")