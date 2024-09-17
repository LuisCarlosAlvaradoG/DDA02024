lista1 = [1, 2, 3, 4, 5]
lista1

lista1.pop() # Quita el último valor de la lista
lista1.pop(0) #Quita el valor, dependiendo del índice que le doy

lista1.append(1) # Función para meter valores a una lista

lista1[2] = 1 # Cambio valor en el índice de una lista
lista1

# Operaciones de cadenas
cadena = "Hola, buenos días"
cadena_separada = cadena.split() # Separar valores en cadenas
cadena_separada[2] # Importante recordar que el índice tiene un valor menos que la posición

cadena = cadena.replace("buenos","buenas") #Replace, cambia una palabra por otra
cadena.replace("días", 'noches') # Necesito guardar la variable para poder hacer más cambios

cadena = "Hola, mi nombre es Luis"
cadena.find("Luis") #Me permite encontrar una palabra dentro de un string o una cadena, y me devuelve el
                    # indice dónde inicia la palabra buscada
cadena[19]

len(cadena) # Me da el total de caracteres que tiene mi cadena, considerando espacios

# Funciones
def promedio(lista):
    suma = sum(lista) # Me suma los valores dentro de una lista
    prom = suma / len(lista) # Me da la longitud de la lista
    return prom


edades = [17, 18,18, 18, 27, 17, 18, 18, 18, 19, 19]
promedio(edades)