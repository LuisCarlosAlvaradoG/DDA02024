# Problema 1
total = 0
while True:
    num = int(input().strip())
    if num == -1:
        break
    total += num
print(total)

# Problema 2
odd_count = 0
even_count = 0

while True:
    num = int(input().strip())
    if num == -1:
        break
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count, even_count)

#Problema 3
prime_count = 0

while True:
    num = int(input().strip())
    if num == -1:
        break
    if num > 1:
        is_prime = True
        # Se recorre desde 2 hasta la raíz cuadrada de num (convertida a entero)
        for i in range(2, int(num ** (1/2)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

print(prime_count)
#Problema 4

total = 0
count = 0

while True:
    num = int(input().strip())
    if num == -1:
        break
    total += num
    count += 1

print(total / count)


#Problema 5
max_value = None

while True:
    num = int(input().strip())
    if num == -1:
        break
    if max_value is None or num > max_value:
        max_value = num

print(max_value)


#Problema 6
min_value = None

while True:
    num = int(input().strip())
    if num == -1:
        break
    if min_value is None or num < min_value:
        min_value = num

print(min_value)


#Problema 7
count3 = 0
count5 = 0
count7 = 0

while True:
    num = int(input().strip())
    if num == -1:
        break
    if num % 3 == 0:
        count3 += 1
    if num % 5 == 0:
        count5 += 1
    if num % 7 == 0:
        count7 += 1

print(count3, count5, count7)

#Problema 8
total = 0

while True:
    num = int(input().strip())
    if num == -1:
        break
    total += num ** 2

print(total)

#Problema 9
num = int(input())
mcd = num 

while True:
    num = int(input())
    if num == -1:
        break

    a, b = abs(mcd), abs(num)
    
    while b:
        print(a, b)
        a, b = b, a % b
        
    mcd = a  

print(mcd)
#Problema 10
producto = 1
i = 0 

while True:
    num = int(input())
    if num == -1:
        break
    producto *= num
    i += 1
    
if i  == 0:
    print()
else:
    print(producto)
