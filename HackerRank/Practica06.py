# Problema 1
secret = 50

while True:
    guess = int(input().strip())
    if guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Higher")
    else:
        print("Lower")

# Problema 2
balance = 0

while True:
    command = input().strip()
    if command == "E":
        break
    
    parts = command.split()
    action = parts[0]
    amount = int(parts[1])
    
    if action == "D":
        balance += amount
        print(balance)
    elif action == "W":
        if amount > balance or balance == 0:
            print("Insufficient funds")
        else:
            balance -= amount
            print(balance)


# Problema 3
while True:
    password = input().strip()
    if password == "stop":
        break
    if len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
        print("Strong")
    else:
        print("Weak")


# Problema 4
total = 0

while True:
    item = input().strip()
    if item == "done":
        break
    if item == "burger":
        total += 5
    elif item == "fries":
        total += 2
    elif item == "soda":
        total += 1
    else:
        print("Item not found")

print("Total:", total)

# Problema 5
balance = float(input().strip())
rate = float(input().strip())
years = int(input().strip())
year = 1

while year <= years:
    balance *= (1 + rate / 100)
    rounded_balance = int(balance * 100 + 0.5) / 100
    print("Year {}: {:.2f}".format(year, rounded_balance))
    year += 1

# Problema 6
cadena = input().strip()
i = len(cadena) - 1
cadena_invertida = ""

while i >= 0:
    cadena_invertida += cadena[i]
    i -= 1

print(cadena_invertida)


# Problema 7
texto = input().strip()
contador = 0
i = 0

while i < len(texto):
    caracter = texto[i]
    if caracter.lower() in "aeiou":
        contador += 1
    i += 1

print(contador)

# Problema 8
n = int(input().strip())
n = abs(n)

# Caso especial: si el número es 0, consideramos que tiene 1 dígito par (el 0)
if n == 0:
    print("1 0")
else:
    pares = 0
    impares = 0
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        n //= 10
    print(pares, impares)

# Problema 9
n = int(input().strip())
suma = 0
i = 1

while i < n:
    if n % i == 0:
        suma += i
    i += 1

if suma == n:
    print("Perfect")
else:
    print("Not Perfect")

# Problema 10
n = int(input().strip())
max_digit = -1
frequency = 0

while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
        frequency = 1
    elif digit == max_digit:
        frequency += 1
    n //= 10

print(max_digit, frequency)
