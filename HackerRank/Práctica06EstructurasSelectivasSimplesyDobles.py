# Problema 1
n = int(input())
if n == 0:
    print("CERO")
elif n > 0 and n % 2 == 0:
    print("POSITIVO_PAR")
elif n > 0:
    print("POSITIVO_IMPAR")
elif n % 2 == 0:
    print("NEGATIVO_PAR")
else:
    print("NEGATIVO_IMPAR")

# Problema 2
edad = int(input())
if 0 <= edad <= 2:
    print("BEBE")
elif edad <= 12:
    print("NIÑO")
elif edad <= 17:
    print("ADOLESCENTE")
elif edad <= 64:
    print("ADULTO")
else:
    print("MAYOR")

# Problema 3
h = int(input())
m = int(input())
if h == 0:
    hh, suf = 12, "AM"
elif h < 12:
    hh, suf = h, "AM"
elif h == 12:
    hh, suf = 12, "PM"
else:
    hh, suf = h - 12, "PM"
print(f"{hh:02d}:{m:02d} {suf}")

# Problema 4
a = int(input())
b = int(input())
if a <= b:
    print(a, b)
else:
    print(b, a)

# Problema 5
total = float(input())
if total < 100:
    pago = total
elif total < 500:
    pago = total * 0.95
elif total < 1000:
    pago = total * 0.90
else:
    pago = total * 0.85
print(f"{pago:.2f}")

# Problema 6
peso = float(input())
altura = float(input())
imc = peso / (altura * altura)
if imc < 18.5:
    print("BAJO_PESO")
elif imc < 25:
    print("NORMAL")
elif imc < 30:
    print("SOBREPESO")
else:
    print("OBESIDAD")

# Problema 7
a = float(input())
b = float(input())
c = float(input())
if a == b and b == c:
    print("EQUILATERO")
elif a == b or a == c or b == c:
    print("ISOCELES")
else:
    print("ESCALENO")

# Problema 8
año = int(input())
if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
    print("BISIESTO")
else:
    print("NO_BISIESTO")

# Problema 9
h1 = int(input()); m1 = int(input())
h2 = int(input()); m2 = int(input())
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
if t2 >= t1:
    dur = t2 - t1
else:
    dur = (24 * 60 - t1) + t2
print(dur)

# Problema 10
kwh = float(input())
if kwh <= 100:
    costo = 0.50 * kwh
elif kwh <= 200:
    costo = 0.50 * 100 + 0.75 * (kwh - 100)
else:
    costo = 0.50 * 100 + 0.75 * 100 + 1.20 * (kwh - 200)
print(f"{costo:.2f}")
