n = int(input())
lista = [i**2 for i in range(1,n+1)]
print(str(lista).replace(" ",""))

lista = eval(input().strip())
pares = [i for i in lista if i % 2 == 0]
print(str(lista).replace(" ",""))

