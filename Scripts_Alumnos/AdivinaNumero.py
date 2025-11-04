import random

def main():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He seleccionado un número entre 1 y 100.")
    print("Tienes 7 intentos para adivinarlo. ¡Buena suerte!")
    x = random.randint(1, 100)

    num = int(input("Introduce tu primer intento: "))
    i = 1

    while i <= 7:
        if num == x:
            print("¡Felicidades! ¡Adivinaste el número en", i, "intentos!")
            break
        elif num < x:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")
        num = int(input())
        i += 1
    else:
        print("Lo siento, has agotado tus intentos. El número era:", x)

if __name__ == "__main__":
    main()