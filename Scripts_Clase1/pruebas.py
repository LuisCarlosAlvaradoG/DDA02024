# Pedir números enteros al usuario, hasta que ingrese el 0.
# Saca la suma y promedio de los números ingresados.
i = 0
suma = 0

while True:
    val = int(input())
    suma += val
    if val == 0:
        break
    i += 1
print(f"Suma {suma} | Promedio {suma/i}")