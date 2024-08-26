# Sesión 3: Estructuras condicionales múltiples y anidadas

# Condicional múltiple
dia_semana = int(input("Introduce un número del 1 al 7 para indicar el día de la semana (1 = Lunes, 7 = Domingo): "))

if dia_semana == 1:
    dia = "Lunes"
elif dia_semana == 2:
    dia = "Martes"
elif dia_semana == 3:
    dia = "Miércoles"
elif dia_semana == 4:
    dia = "Jueves"
elif dia_semana == 5:
    dia = "Viernes"
elif dia_semana == 6:
    dia = "Sábado"
elif dia_semana == 7:
    dia = "Domingo"
else:
    dia = "Número de día inválido"

print(f"El día de la semana es: {dia}")

# Condicional anidado
numero = int(input("Introduce un número: "))

if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.")
elif numero < 0:
    if numero % 2 == 0:
        print("El número es negativo y par.")
    else:
        print("El número es negativo e impar.")
else:
    print("El número es cero.")

# Clasificación de edades
edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Edad inválida.")
elif edad < 2:
    print("Eres un bebé.")
elif edad < 12:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# Ejercicio: Sistema de recomendación de actividades según la temperatura
temperatura = float(input("Introduce la temperatura actual en grados Celsius: "))

if temperatura < 0:
    actividad = "Esquiar"
elif temperatura < 10:
    actividad = "Leer un libro en casa"
elif temperatura < 20:
    actividad = "Ir a caminar"
elif temperatura < 30:
    actividad = "Ir a nadar"
else:
    actividad = "Ir a la playa"

print(f"Te recomendamos: {actividad}")

# Ejercicio: Conversión de notas a letras
nota = float(input("Introduce tu nota (0 a 100): "))

if nota >= 90:
    calificacion = 'A'
elif nota >= 80:
    calificacion = 'B'
elif nota >= 70:
    calificacion = 'C'
elif nota >= 60:
    calificacion = 'D'
else:
    calificacion = 'F'

print(f"Tu calificación es: {calificacion}")

# Ejercicio: Calculadora básica con menú de opciones
print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Selecciona una opción (1-4): "))

if opcion >= 1 and opcion <= 4:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == 1:
        resultado = num1 + num2
        operacion = "suma"
    elif opcion == 2:
        resultado = num1 - num2
        operacion = "resta"
    elif opcion == 3:
        resultado = num1 * num2
        operacion = "multiplicación"
    else:
        if num2 != 0:
            resultado = num1 / num2
            operacion = "división"
        else:
            resultado = "indefinido (división por cero)"
            operacion = "división"

    print(f"El resultado de la {operacion} es: {resultado}")
else:
    print("Opción no válida")
