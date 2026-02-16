n = int(input())

millares = n // 1000
n = n%1000
centenas = n // 100
n = n%100
decenas = n // 10
unidades = n % 10
suma = millares + centenas + decenas + unidades
print(millares, centenas, decenas, unidades)
print(suma)

n = input()
print(int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]))


