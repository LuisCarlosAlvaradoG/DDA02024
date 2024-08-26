import numpy as np

def funcion(x,y):
    suma = x + y
    return suma

class Coche:
    def __init__(self, marca, año, color):
        self.marca = marca
        self.año = año
        self.color = color

    def moverse(self, velocidad):
        self.velocidad = velocidad
        print("El coche se mueve a:", self.velocidad)

micoche = Coche("Volkswagen","2010","blanco", )
micoche.moverse("150 km/h")