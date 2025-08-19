'''
Problema 02
Title: Filtrar Adultos

Description (140 caracteres):
Dado un diccionario con 'Name' y 'Age', retorna la lista de nombres con edad >= 18.

Problem Statement:
Se recibe un dict con las claves:
  'Name': lista de strings
  'Age': lista de enteros
Utiliza pandas para crear un DataFrame y filtrar las filas donde Age >= 18.
Retorna una lista de strings con los nombres en el orden original.

Input Format:
  Una línea con un dict literal.

Output Format:
  Lista de strings.
'''

def problem_pd(data):
    pass

# Test harness pandas
_pd_in = [
    {'Name':['Alice','Bob','Charlie'],'Age':[17,18,19]},
    {'Name':['Tom'],'Age':[18]},
    {'Name':['Anna','Ben'],'Age':[16,17]},
    {'Name':['X','Y','Z'],'Age':[20,15,30]},
    {'Name':['P','Q','R','S'],'Age':[18,18,18,18]},
    {'Name':['A','B'],'Age':[0,100]},
    {'Name':['John','Doe','Smith'],'Age':[21,17,22]},
    {'Name':['M','N','O'],'Age':[17,16,15]},
    {'Name':['U','V','W'],'Age':[19,19,17]},
    {'Name':['K'],'Age':[10]}
]
_pd_exp = [
    ['Bob','Charlie'],
    ['Tom'],
    [],
    ['X','Z'],
    ['P','Q','R','S'],
    ['B'],
    ['John','Smith'],
    [],
    ['U','V'],
    []
]

correct = 0
for inp, exp in zip(_pd_in, _pd_exp):
    if problem_pd(inp) == exp:
        correct += 1
print(f"Problema 02 Parcial 03: {correct}/10")