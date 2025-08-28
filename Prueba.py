A = int(input("Ingrese A: "))
B = int(input("Ingrese B: "))
C = int(input("Ingrese C: "))

if A > B and A > C:
    MAYOR = A
elif B > A and B > C:
    MAYOR = B
else:
    MAYOR = C

print("El mayor es:", MAYOR)

