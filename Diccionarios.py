'''Diccionarios en Python: Definición y Conceptos Fundamentales
📌 Definición de un Diccionario
Un diccionario en Python es una estructura de datos que almacena pares clave-valor. 
Es mutable, lo que significa que sus valores pueden modificarse, 
pero sus claves deben ser únicas e inmutables (cadenas, números o tuplas inmutables).

🔹 Ejemplo de un Diccionario
'''

persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero"
}

print(persona)  
# {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'}
'''
📌 Creación de Diccionarios
'''
# Diccionario vacío
diccionario_vacio = {}

# Diccionario con claves y valores
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Creación con la función dict()
auto = dict(marca="Toyota", modelo="Corolla", año=2020)
print(auto)  
# {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020}

'''
📌 Acceder a Elementos de un Diccionario
'''
persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

# Acceder usando la clave
print(persona["nombre"])  # "Carlos"

# Usar get() para evitar errores si la clave no existe
print(persona.get("profesion", "No especificado"))  # "No especificado"

'''
🔹 Diferencia entre [] y get():

persona["clave"] lanza un KeyError si la clave no existe.
persona.get("clave", "valor_por_defecto") devuelve el valor por defecto si la clave no existe.
'''

'''
📌 Modificar Valores en un Diccionario
'''
persona = {"nombre": "Carlos", "edad": 28}

# Modificar un valor
persona["edad"] = 29
print(persona)  # {'nombre': 'Carlos', 'edad': 29}
'''
📌 Agregar Nuevas Claves
'''

persona["profesion"] = "Arquitecto"
print(persona)
# {'nombre': 'Carlos', 'edad': 29, 'profesion': 'Arquitecto'}

'''
📌 Eliminar Elementos de un Diccionario
'''

persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

# Eliminar una clave con del
del persona["ciudad"] #del no es un comando exclusivo de diccionarios
print(persona)  # {'nombre': 'Carlos', 'edad': 28}

# Usar pop() para eliminar y obtener el valor eliminado
edad = persona.pop("edad")
print(edad)  # 28
print(persona)  # {'nombre': 'Carlos'}

# Vaciar el diccionario
persona.clear()
print(persona)  # {}
'''
📌 Comprobar si una Clave Existe
'''
persona = {"nombre": "Carlos", "edad": 28}

print("edad" in persona)  # True
print("altura" in persona)  # False
'''
📌 Recorrer un Diccionario
🔹 Recorrer Claves
'''

persona = {"nombre": "Carlos", "edad": 28}

for clave in persona:
    print(clave, ":", persona[clave])

'''
🔹 Recorrer Valores
'''
for valor in persona.values():
    print(valor)

'''
🔹 Recorrer Claves y Valores
'''

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
'''
📌 Copiar un Diccionario
'''
persona = {"nombre": "Carlos", "edad": 28}

# Copia superficial
persona_copia = persona.copy()
persona_copia["edad"] = 30

print(persona)  # {'nombre': 'Carlos', 'edad': 28}
print(persona_copia)  # {'nombre': 'Carlos', 'edad': 30}

'''
📌 Diccionarios Anidados
'''

empresa = {
    "empleado1": {"nombre": "Ana", "edad": 25},
    "empleado2": {"nombre": "Luis", "edad": 30}
}

# Acceder a un valor dentro del diccionario anidado
print(empresa["empleado1"]["nombre"])  # Ana


'''MÉTODOS COMÚNES'''

'''1️⃣ keys() → Obtener todas las claves
Devuelve un objeto dict_keys con todas las claves del diccionario.'''

persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

# Obtener las claves
claves = persona.keys()
print(claves)  # dict_keys(['nombre', 'edad', 'ciudad'])

# Convertir a lista si es necesario
print(list(claves))  # ['nombre', 'edad', 'ciudad']

'''
✅ Útil cuando necesitas recorrer solo las claves del diccionario.
'''

'''
2️⃣ values() → Obtener todos los valores
Devuelve un objeto dict_values con todos los valores del diccionario.
'''
persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

# Obtener los valores
valores = persona.values()
print(valores)  # dict_values(['Carlos', 28, 'Barcelona'])

# Convertir a lista si es necesario
print(list(valores))  # ['Carlos', 28, 'Barcelona']
'''
✅ Útil cuando solo necesitas los valores, sin preocuparte por las claves.
'''

'''
3️⃣ items() → Obtener pares clave-valor
Devuelve un objeto dict_items con tuplas (clave, valor).
'''

persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

# Obtener clave-valor
pares = persona.items()
print(pares)  
# dict_items([('nombre', 'Carlos'), ('edad', 28), ('ciudad', 'Barcelona')])

# Convertir a lista si es necesario
print(list(pares))  
# [('nombre', 'Carlos'), ('edad', 28), ('ciudad', 'Barcelona')]
'''
✅ Útil cuando necesitas recorrer claves y valores juntos en un for.
'''

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
'''📝 Salida:
nombre: Carlos
edad: 28
ciudad: Barcelona
'''

'''
4️⃣ get(clave, valor_por_defecto) → Obtener un valor sin error
Si la clave no existe, devuelve None o un valor por defecto.
'''

persona = {"nombre": "Carlos", "edad": 28}

print(persona.get("edad"))  # 28
print(persona.get("profesion", "No especificado"))  # "No especificado"
'''
✅ Evita errores si la clave no existe, a diferencia de persona["clave"].
'''

# persona["profesion"]  # ❌ KeyError: 'profesion'
'''
5️⃣ update(otro_diccionario) → Actualizar o agregar claves
Añade o actualiza los valores con otro diccionario.
'''

persona = {"nombre": "Carlos", "edad": 28}

# Actualizar con otro diccionario
persona.update({"edad": 30, "ciudad": "Madrid"})
print(persona)
# {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Madrid'}

'''
✅ Útil para fusionar diccionarios sin sobrescribir completamente el original.
'''

'''
6️⃣ pop(clave, valor_por_defecto) → Eliminar una clave y devolver su valor
Elimina la clave y devuelve el valor eliminado.
'''

persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

edad = persona.pop("edad")
print(edad)  # 28
print(persona)  # {'nombre': 'Carlos', 'ciudad': 'Barcelona'}

'''
Si la clave no existe, evita errores usando un valor por defecto:
'''

print(persona.pop("profesion", "No encontrado"))  # "No encontrado"

'''
7️⃣ popitem() → Eliminar y devolver el último par clave-valor
'''
persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}

ultimo = persona.popitem()
print(ultimo)  # ('ciudad', 'Barcelona')
print(persona)  # {'nombre': 'Carlos', 'edad': 28}

'''
✅ Útil cuando quieres eliminar elementos de un diccionario de manera secuencial.
'''

'''
8️⃣ setdefault(clave, valor_por_defecto) → Obtener o agregar una clave
Si la clave existe, devuelve su valor.
Si no existe, la crea con el valor por defecto.
'''

persona = {"nombre": "Carlos", "edad": 28}

# Si "ciudad" no existe, se añade con "Desconocido"
ciudad = persona.setdefault("ciudad", "Desconocido")
print(ciudad)  # "Desconocido"
print(persona)  # {'nombre': 'Carlos', 'edad': 28, 'ciudad': 'Desconocido'}

# Si la clave ya existe, no se modifica
nombre = persona.setdefault("nombre", "Otro")
print(nombre)  # "Carlos"

'''
✅ Útil cuando quieres asegurarte de que una clave tenga un valor sin sobrescribir valores existentes.
'''
'''
9️⃣ clear() → Vaciar el diccionario
'''

persona = {"nombre": "Carlos", "edad": 28}
persona.clear()
print(persona)  # {}

'''
✅ Elimina todos los elementos sin borrar la variable.
'''
'''
🔟 copy() → Crear una copia del diccionario
'''

original = {"a": 1, "b": 2}
copia = original.copy()

copia["c"] = 3
print(original)  # {'a': 1, 'b': 2}
print(copia)  # {'a': 1, 'b': 2, 'c': 3}

'''
✅ Evita modificar el diccionario original al hacer cambios en la copia.
'''
'''
📌 Ejemplo Completo Combinando Métodos
'''
datos = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera"
}

# Obtener claves y valores
print("Claves:", list(datos.keys()))  # ['nombre', 'edad', 'profesion']
print("Valores:", list(datos.values()))  # ['Ana', 30, 'Ingeniera']

# Agregar una clave si no existe
datos.setdefault("ciudad", "Desconocida")

# Actualizar valores
datos.update({"edad": 31, "pais": "España"})

# Eliminar una clave
datos.pop("profesion")

# Recorrer el diccionario
for clave, valor in datos.items():
    print(f"{clave}: {valor}")

'''
📌 Salida:

Claves: ['nombre', 'edad', 'profesion']
Valores: ['Ana', 30, 'Ingeniera']
nombre: Ana
edad: 31
ciudad: Desconocida
pais: España
'''


'''
📌 Resumen de Métodos de Diccionarios

Método	                        Descripción	                                Ejemplo
keys()	                        Devuelve las claves del diccionario	        diccionario.keys()
values()	                    Devuelve los valores	                    diccionario.values()
items()	                        Devuelve los pares clave-valor	            diccionario.items()
get(clave, valor_por_defecto)	Obtiene un valor sin error	                diccionario.get("clave")
update(otro_diccionario)	    Fusiona otro diccionario	                diccionario.update(otro)
pop(clave, valor_por_defecto)	Elimina y devuelve un valor	                diccionario.pop("clave")
popitem()	                    Elimina el último elemento	                diccionario.popitem()
setdefault(clave, valor)	    Obtiene o crea una clave	                diccionario.setdefault("clave", valor)
clear()	                        Vacía el diccionario	                    diccionario.clear()
copy()	                        Crea una copia	                            copia = diccionario.copy()
'''
