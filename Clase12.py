# Manejo de cadenas y listas

#CADENAS
cadena = "Programación en python"
print("Cadena orignial:", cadena)

print("Número de palabras en la cadena:", len(cadena.split()))

print("Cadena sin espacios:",cadena.replace(" ",""))

print("Subcadena 'Python' en cadena:",cadena.find("python"))

#Función para contar vocales
def contar_vocales_corto(texto):
    vocales = "aeiouáéíóú"
    conteo = sum(1 for i in texto.lower() if i in vocales)
    return conteo

def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    texto = texto.lower()
    contador = 0
    for i in range(len(texto)):
        if texto[i] in vocales:
            contador += 1
    return contador
#Equipo 1 38
texto1 = "El océano iluminado era increíblemente vasto y profundo, lleno de emociones, ideas y aventuras."


#Equipo 2 62
texto2 = "El universo es amplio, y aunque a veces pareciera que las estrellas brillan lejos, el cielo azul sigue mostrando luces, ideas, y emociones únicas en cada etapa."
def contar_vocales(x):
    return sum(i in {"a","e","i","o","u","á","é","í","ó","ú","ü"} for i in x.lower())
print(contar_vocales(texto2))

#LISTAS
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

#Añadir elemento
lista.append(0)
lista.append(6)
print("Lista después de añadir un elemento:",lista)

lista.insert(0,3.5)
lista
print("Lista después de insertar elemento en posición", lista) 

lista.pop(0) #Quita el valor en la posición que le doy
lista
lista.remove(5) #Quita el valor
lista
lista.sort() # Lista ordenada ascendentemente
lista
lista.sort(reverse= True) # Lista ordenada descendentemente
lista

new_list = list(range(0,11))
new_list