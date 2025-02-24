# # Rodrigo 1
# # print("Hola")
# var = 5
# type(var)

# var = 5.5
# type(var)

# var = "5"
# type(var)

# var = 5 == 5
# type(var)


# var = 5
# var = str(var)
# print(var)
# type(var)

# var + 5
# var * 5

# type(5.0)
# 5.1 == 5
# '5' == 5

# 5**(1/3)

# 5/2
# 5//2


a = int(input("Ingresa el valor de a:"))
# print("El valor de a es ", a)
print(f"El valor de a es {a}")
b = int(input("Ingresa el valor de b:"))
print(f"El valor de b es {b}")

# Operaciones aritméticas básicas
suma = a + b
resta = a - b
mult = a * b
div = a / b
exp = a ** b
div_ent = a//b
mod = a % b

# Dos clicks seleccionan la palabra, 3 clicks seleccionan la línea completa
print(suma)
print(resta)
print(mult)
print(div)
print(exp)
print(div_ent)
print(mod)

# Funciones de entrada y de salida
nombre = input("Introduce tu nombre: ") # El nombre es un string
edad = int(input("Introduce tu edad: ")) # La edad, al ser un número entero, necesita tener int
print(f"Hola {nombre}. Tienes {edad} años")

# Más operaciones de entrada y de salida
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
print(f"Tu índice de masa corporal (IMC) es: {peso/altura**2}")
print(f"Tu índice de masa corporal (IMC) es: {peso/altura**2:.3f}")
