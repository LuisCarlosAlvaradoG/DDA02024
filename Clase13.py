num = 12345
lista_num = str(num)
i = len(lista_num) - 1
new_list = []
while i >= 0:
    new_list.append(lista_num[i])
    i -= 1
numero = int("".join(new_list))


lista = input()
lista = lista.strip("[]")  
lista = lista.replace('"', '') 
lista = lista.split(",")
# ["apple","cat","banana"]
i = 0
concat = ""
while i < len(lista):
    if len(lista[i]) > 3:
        concat += " " + lista[i]
    i += 1
print(concat)