# ---------------------------------------------------------------
# Ejercicio 24 - Extracto de iniciales
# Enunciado: Lee nombre y apellido y muestra iniciales en mayúsculas (solo slicing).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------
nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
iniciales = nombre[0].upper() + apellido[0].upper()
print("Tus iniciales son:", iniciales)

nombre = "Leo"
print("Hola nombre")
print(f"Hola {nombre}")