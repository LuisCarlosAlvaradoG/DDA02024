# ===============================================================
# 1.- ESTRUCTURAS SECUENCIALES: CONSTANTES Y VARIABLES, ENTRADA Y SALIDA
# ---------------------------------------------------------------
# B) TEORÍA: CONSTANTES, VARIABLES E IDENTIFICADORES
# ---------------------------------------------------------------
# ¿Qué es una VARIABLE?
# - Es un nombre (identificador) que REFERENCIA un valor en memoria.
# - En Python el tipeado es dinámico: el mismo nombre puede referenciar
#   a valores de diferente tipo en momentos distintos.
#
# ¿Qué es una CONSTANTE?
# - En Python no existen constantes "estrictas" a nivel de lenguaje.
# - Por CONVENCIÓN utilizamos nombres con MAYÚSCULAS y GUIONES_BAJOS
#   para indicar "no modificar este valor". Ejemplo: PI = 3.14159
# - Disciplina del equipo: respetar que las constantes no cambian.
#
# IDENTIFICADORES (nombres válidos para variables/constantes)
# - Pueden contener letras (A-z), dígitos (0-9) y guion bajo (_).
# - NO pueden empezar con dígito.
# - Son sensibles a mayúsculas/minúsculas: nombre != Nombre != NOMBRE
# - NO pueden ser palabras reservadas del lenguaje (keywords).

# TIPOS BÁSICOS EN ESTA SESIÓN
# - int   (enteros): 0, 1, -3, 42
# - float (reales):  3.14, -0.5, 2.0
# - str   (cadenas): "hola", 'Python', ""
# - bool  (booleanos): True, False
#
# OBSERVACIÓN SOBRE INMUTABILIDAD (ideas introductorias)
# - Las cadenas (str) son INMUTABLES: no se puede cambiar un carácter por índice.

# Asignación simple (variable -> valor)
course_name = "Algoritmos y Programación"   # str
credits = 6                                  # int
average_grade = 9.1                          # float
is_active = True                             # bool

# Mostrar valores y sus tipos
print("course_name:", course_name, "| type:", type(course_name))
print("credits:", credits, "| type:", type(credits))
print("average_grade:", average_grade, "| type:", type(average_grade))
print("is_active:", is_active, "| type:", type(is_active))

# Constante por convención (no se debe modificar)
PI = 3.14159
MAX_STUDENTS = 40
print("PI:", PI, "| MAX_STUDENTS:", MAX_STUDENTS)

# Identificadores válidos/ inválidos (solo comentarios):
# válido: user_name, _hidden_value, age2, TOTAL_SUM
# inválido: 2age (no puede empezar con dígito), user-name (guion NO permitido), class (keyword)

# Palabras reservadas (keywords): nombres que NO pueden usarse como identificadores.
# Las listamos solo para referencia visual.

import keyword
print("Python keywords:", keyword.kwlist)
print("Total keywords:", len(keyword.kwlist))

# ---------------------------------------------------------------
# C) TEORÍA: ENTRADA Y SALIDA (input/print)
# ---------------------------------------------------------------
# FUNCIÓN print(*objetos, sep=' ', end='\n')
# - Imprime los objetos separados por 'sep' y finaliza con 'end'.
# - Ejemplos de parámetros útiles:
#   - sep: cambia el separador entre objetos impresos.
#   - end: cambia el final de línea (por defecto es salto de línea).
# - Soporta diferentes formas de formateo: concatenación, format(), f-strings.
#
# FUNCIÓN input(prompt)
# - Muestra el mensaje 'prompt' y LEE una línea desde el teclado.
# - SIEMPRE retorna un str (cadena). Si se requieren números, hay que convertir.
#
# CONVERSIÓN DE TIPOS (CASTING):
# - int("10") -> 10
# - float("3.5") -> 3.5
# - str(10) -> "10"
# - bool(""), bool("hola")
#   Nota: bool('') es False, bool('0') es True (cualquier cadena no vacía -> True).
#
# FORMATEO DE SALIDA (básico en esta sesión)
# - Concatenación con + (requiere str en ambos lados).
# - print con múltiples argumentos separados por coma (automatiza espacios).
# - str.format("... {0} ... {1} ...".format(a,b))
# - f-strings: f"Hola {nombre}, edad {edad}"
#   (f-strings requieren Python 3.6+).

# --- Código ilustrativo: print ---
print("Hola", "mundo")                     # usa sep por defecto = " "
print("A", "B", "C", sep="-")              # sep cambia el separador
print("Sin salto al final...", end="")     # end="" evita salto de línea
print(" <- Continuación de la misma línea")

# Formatos:
student = "Luis"
age = 24
print("Alumno:", student, "| Edad:", age)                  # múltiple con coma
print("Alumno: " + student + " | Edad: " + str(age))       # concatenación
print("Alumno: {} | Edad: {}".format(student, age))        # format()
print(f"Alumno: {student} | Edad: {age}")                  # f-string (recomendado)

# --- Código ilustrativo: input ---
# Nota: Descomenta para probar interactivamente en clase.
# name = input("Ingresa tu nombre: ")
# print("Hola,", name)

# Lectura y conversión básica
# year_str = input("Ingresa un año (entero): ")
# year = int(year_str)     # conversión str -> int
# print("Año leído (int):", year, "| type:", type(year))

# height_str = input("Ingresa tu estatura en metros (ej. 1.75): ")
# height = float(height_str)  # conversión str -> float
# print("Estatura:", height, "| type:", type(height))

# Advertencia: Si el usuario ingresa algo no convertible (ej. 'uno' en int) se lanzará
# ValueError. El manejo de errores (try/except) se estudiará en la Sesión 4.

# ---------------------------------------------------------------
# D) CASOS DE USO (scripts SECUENCIALES simples, sin if/for/while)
# ---------------------------------------------------------------

# Caso 1) Ficha de registro simple (eco de datos)
full_name = input("Nombre completo: ")
student_id = input("Matrícula/ID: ")
degree = input("Programa académico (ej. 'Ing. Civil', 'Ing. en Nanotecnología'): ")
semester = input("Semestre (texto o número): ")
print("\n--- RESUMEN ---")
print(f"Nombre: {full_name}")
print(f"ID: {student_id}")
print(f"Programa: {degree}")
print(f"Semestre: {semester}")

# Caso 2) Tarjeta de presentación (formateo de salida)
first_name = input("Nombre: ")
last_name = input("Apellido: ")
email = input("Correo institucional: ")
print("\n----- TARJETA -----")
print(f"{last_name}, {first_name}")
print(email)

# Caso 3) Comprobante de inscripción (composición de cadenas)
curso = input("Curso: ")
grupo = input("Grupo: ")
aula = input("Aula/Laboratorio: ")
horario = input("Horario (ej. 'Lun-Mié 7:00-9:00'): ")
print("\n*** COMPROBANTE ***")
print("Curso:", curso, "| Grupo:", grupo, "| Aula:", aula, "| Horario:", horario)

# Caso 4) Eco numérico con conversión (sin operaciones avanzadas)
horas_str = input("Horas inscritas (entero): ")
horas = int(horas_str)
creditos_str = input("Créditos (entero): ")
creditos = int(creditos_str)
print("\nResumen numérico -> horas:", horas, ", créditos:", creditos)
# (Operaciones detalladas se verán en la Sesión 2).

# ---------------------------------------------------------------
# E) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas de las variables en programas secuenciales:
# - Facilitan almacenar y reutilizar valores (evitar "números mágicos").
# - Mejoran la legibilidad y el mantenimiento del código.
# - Permiten separar "entrada" de "cálculo" y "salida".
#
# Desventajas / riesgos comunes:
# - Nombres poco descriptivos generan confusión (evitar 'a', 'b', 'c' sin contexto).
# - Cambiar el tipo de una variable accidentalmente (por tipado dinámico) puede
#   causar errores lógicos. Mantener coherencia de tipos.
# - Con input(), TODO llega como str. Si se necesitan números, convertir explícitamente.
#
# Buenas prácticas:
# - Usar identificadores descriptivos y seguir PEP 8.
# - Definir "constantes" en UPPER_SNAKE_CASE al inicio del archivo si aplican.
# - Agrupar la lectura de datos (input) al principio, el "proceso" al centro
#   (se verá más en Sesión 2) y la presentación (print) al final.
# - Comentar el código teórico con claridad (como en este documento).

# ---------------------------------------------------------------
# F) BANCO DE EJERCICIOS (SECUENCIALES, sin if/for/while)
# ---------------------------------------------------------------
# Indicaciones:
# - Cada ejercicio puede resolverse con asignaciones, input(), print(),
#   conversiones básicas y, cuando sea necesario, operaciones simples.
# - NO uses decisiones ni ciclos en esta sesión.
# - Las soluciones están COMENTADAS debajo de cada enunciado; descoméntalas
#   solo después de haber intentado resolverlos con tus estudiantes.

# ---------------------------------------------------------------
# Ejercicio 01 - Saludo personalizado
# Enunciado: Lee el nombre del usuario y muestra: Hola, <nombre>!
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Ingresa tu nombre: ")
# print("Hola, " + name + "!")


# ---------------------------------------------------------------
# Ejercicio 02 - Nombre y apellido
# Enunciado: Pide nombre y apellido por separado y muéstralos como 'Apellido, Nombre'.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# first = input("Nombre: ")
# last = input("Apellido: ")
# print(last + ", " + first)


# ---------------------------------------------------------------
# Ejercicio 03 - Tarjeta simple
# Enunciado: Solicita nombre completo, correo y carrera. Imprime en tres líneas.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# full_name = input("Nombre completo: ")
# email = input("Correo: ")
# career = input("Carrera: ")
# print(full_name)
# print(email)
# print(career)


# ---------------------------------------------------------------
# Ejercicio 04 - Parámetros de print
# Enunciado: Imprime tres palabras en una sola línea separadas por ' - ' usando sep.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# w1 = input("Palabra 1: ")
# w2 = input("Palabra 2: ")
# w3 = input("Palabra 3: ")
# print(w1, w2, w3, sep=" - ")


# ---------------------------------------------------------------
# Ejercicio 05 - Sin salto de línea
# Enunciado: Imprime dos mensajes en la MISMA línea usando end=''.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# msg1 = input("Mensaje 1: ")
# msg2 = input("Mensaje 2: ")
# print(msg1, end="")
# print(msg2)


# ---------------------------------------------------------------
# Ejercicio 06 - Conversión básica
# Enunciado: Lee un año como texto, conviértelo a int y muestra su tipo antes y después.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# year_str = input("Año: ")
# print("Antes:", type(year_str))
# year = int(year_str)
# print("Después:", type(year))


# ---------------------------------------------------------------
# Ejercicio 07 - Eco de números
# Enunciado: Lee dos números reales (como texto), conviértelos a float y muéstralos.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# a = float(input("Número real A: "))
# b = float(input("Número real B: "))
# print("A:", a, "B:", b)


# ---------------------------------------------------------------
# Ejercicio 08 - Tipo booleano
# Enunciado: Lee una cadena y muestra bool(cadena). Explica el resultado.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# s = input("Cadena: ")
# print(bool(s))


# ---------------------------------------------------------------
# Ejercicio 09 - Formato con format()
# Enunciado: Lee nombre y edad, y muestra con str.format().
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Nombre: ")
# age = int(input("Edad: "))
# print("Alumno: {} | Edad: {}".format(name, age))


# ---------------------------------------------------------------
# Ejercicio 10 - Formato con f-string
# Enunciado: Lee ciudad y país y muestra f"Ciudad: <ciudad>, País: <país>".
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# city = input("Ciudad: ")
# country = input("País: ")
# print(f"Ciudad: {city}, País: {country}")


# ---------------------------------------------------------------
# Ejercicio 11 - Multilínea con \n
# Enunciado: Lee tres palabras y muéstralas cada una en su propia línea con un solo print.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# p1 = input("Palabra 1: ")
# p2 = input("Palabra 2: ")
# p3 = input("Palabra 3: ")
# print(p1 + "\n" + p2 + "\n" + p3)


# ---------------------------------------------------------------
# Ejercicio 12 - Recibo simple (eco)
# Enunciado: Lee concepto, cantidad y precio (como texto) y muéstralos en una línea.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# concept = input("Concepto: ")
# qty = input("Cantidad: ")
# price = input("Precio: ")
# print("Concepto:", concept, "| Cantidad:", qty, "| Precio:", price)


# ---------------------------------------------------------------
# Ejercicio 13 - Tipos básicos
# Enunciado: Lee un entero, un real y una cadena; imprime cada valor con su tipo.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# x = int(input("Entero: "))
# y = float(input("Real: "))
# z = input("Cadena: ")
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))


# ---------------------------------------------------------------
# Ejercicio 14 - Plantilla fija
# Enunciado: Pide nombre y semestre y muestra: 'Estudiante <nombre> cursa semestre <semestre>'.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Nombre: ")
# sem = input("Semestre: ")
# print("Estudiante " + name + " cursa semestre " + sem)


# ---------------------------------------------------------------
# Ejercicio 15 - Separador personalizado
# Enunciado: Lee cuatro palabras y muéstralas separadas por ' | ' sin espacios extra.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# a = input("Palabra A: ")
# b = input("Palabra B: ")
# c = input("Palabra C: ")
# d = input("Palabra D: ")
# print(a, b, c, d, sep=" | ")


# ---------------------------------------------------------------
# Ejercicio 16 - Conversión str -> float
# Enunciado: Lee una temperatura (texto), conviértela a float y repórtala.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# t = float(input("Temperatura (ej. 22.5): "))
# print("Temperatura:", t)


# ---------------------------------------------------------------
# Ejercicio 17 - str() de números
# Enunciado: Lee dos enteros y construye la cadena 'a y b son enteros'.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# a = int(input("a: "))
# b = int(input("b: "))
# msg = str(a) + " y " + str(b) + " son enteros"
# print(msg)


# ---------------------------------------------------------------
# Ejercicio 18 - Boleta mínima (solo texto)
# Enunciado: Lee nombre, materia y calificación (texto) y muéstralo en 3 líneas.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Nombre: ")
# subject = input("Materia: ")
# cal = input("Calificación (texto): ")
# print(name)
# print(subject)
# print(cal)


# ---------------------------------------------------------------
# Ejercicio 19 - Ancho de campo (básico)
# Enunciado: Lee nombre y alinéalo en un ancho de 20 usando format().
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Nombre: ")
# print("[" + "{:20}".format(name) + "]")


# ---------------------------------------------------------------
# Ejercicio 20 - Eco mixto
# Enunciado: Lee un texto, un entero y un real, conviértelos y preséntalos en una línea.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# text = input("Texto: ")
# n = int(input("Entero: "))
# r = float(input("Real: "))
# print("text:", text, "| n:", n, "| r:", r)


# ---------------------------------------------------------------
# Ejercicio 21 - Título de proyecto
# Enunciado: Lee título y autor; muestra: '<título>' por <autor>.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# title = input("Título: ")
# author = input("Autor: ")
# print("'" + title + "' por " + author + ".")


# ---------------------------------------------------------------
# Ejercicio 22 - Mini hoja de vida
# Enunciado: Lee nombre, edad (int), ciudad; repórtalo con f-string en 1 línea.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# name = input("Nombre: ")
# age = int(input("Edad: "))
# city = input("Ciudad: ")
# print(f"{name} | {age} | {city}")


# ---------------------------------------------------------------
# Ejercicio 23 - Línea con end
# Enunciado: Lee dos frases y muéstralas en una línea usando end=' '.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# a = input("Frase 1: ")
# b = input("Frase 2: ")
# print(a, end=" ")
# print(b)


# ---------------------------------------------------------------
# Ejercicio 24 - Echo de booleano
# Enunciado: Lee cualquier texto y muestra (solo) True/False con bool(texto).
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# t = input("Texto: ")
# print(bool(t))


# ---------------------------------------------------------------
# Ejercicio 25 - Ficha de curso
# Enunciado: Lee curso, grupo y horario; imprímelos con separador ' - '.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# c = input("Curso: ")
# g = input("Grupo: ")
# h = input("Horario: ")
# print(c, g, h, sep=" - ")


# ---------------------------------------------------------------
# Ejercicio 26 - ID y tipo
# Enunciado: Lee un valor y muestra su representación y su tipo (solo una línea).
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# v = input("Valor: ")
# print(v, type(v))


# ---------------------------------------------------------------
# Ejercicio 27 - Eco numérico estricto
# Enunciado: Lee 3 números como int y muéstralos bajo etiquetas A, B y C.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
# print("A:", A, "| B:", B, "| C:", C)


# ---------------------------------------------------------------
# Ejercicio 28 - Formato decimal básico
# Enunciado: Lee un real y muéstralo con 2 decimales usando format().
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# x = float(input("Real: "))
# print("{:.2f}".format(x))


# ---------------------------------------------------------------
# Ejercicio 29 - Recibo alineado (texto)
# Enunciado: Lee 3 conceptos (texto) y muéstralos uno debajo del otro con viñetas.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# c1 = input("Concepto 1: ")
# c2 = input("Concepto 2: ")
# c3 = input("Concepto 3: ")
# print("- " + c1)
# print("- " + c2)
# print("- " + c3)


# ---------------------------------------------------------------
# Ejercicio 30 - Encabezado y pie
# Enunciado: Lee un título y rodéalo con líneas de '=' arriba y abajo (solo prints).
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# (tu código aquí)

# --- SOLUCIÓN (comentada) ---

# title = input("Título: ")
# print("====================")
# print(title)
# print("====================")

