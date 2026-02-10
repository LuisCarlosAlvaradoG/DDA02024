# ===============================================================
# 1.- ESTRUCTURAS SECUENCIALES: CONSTANTES Y VARIABLES, ENTRADA Y SALIDA
# ---------------------------------------------------------------
# A) TEORÍA: CONSTANTES, VARIABLES E IDENTIFICADORES
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


nombre_curso = "Algoritmos y Programación" # str
creditos = 8                               # int
calificacion_promedio = 7.5                # float (decimal)
alumno_activo = True                       # bool (boolean)

print(nombre_curso)
print("El nombre del curso es:", nombre_curso)

# Asignación simple (variable -> valor)

# Mostrar valores y sus tipos
type(nombre_curso)
type(creditos)
type(calificacion_promedio)
type(alumno_activo)
not alumno_activo


# Constante por convención (no se debe modificar)
PI = 3.14159


# Identificadores válidos/ inválidos (solo comentarios):
# válido: user_name, _hidden_value, age2, TOTAL_SUM
# inválido: 2age (no puede empezar con dígito), user-name (guion NO permitido), class (keyword)

# Palabras reservadas (keywords): nombres que NO pueden usarse como identificadores.
# Las listamos solo para referencia visual.
import keyword
print(keyword.kwlist)
len(keyword.kwlist)
# ---------------------------------------------------------------
# B) TEORÍA: ENTRADA Y SALIDA (input/print)
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

# Formatos:
nombre = "Luis"
edad = 25
print("El alumno se llama", nombre, "y tiene", edad, "años") # Impresión múltiple
print("El alumno se llama" + nombre + "y tiene" + str(edad) + "años") # Concatenación
print(f"El alumno se llama {nombre} y tiene {edad} años") # f-string


# --- Código ilustrativo: input ---
name = input("Ingresa tu nombre:")
print(f"Hola {name}")

# Lectura y conversión básica
año = int(input("Ingresa un año:"))
print(f"El año actual es: {año} | Tipo de dato {type(año)}")

estatura = float(input("Ingresa tu estatura en mts: "))
print(f"La estatura del usuario es {estatura:.2f}")

activo = bool(input("Ingresa si el alumno está activo: "))
print(f"¿El alumno está activo? {activo} ")

# Advertencia: Si el usuario ingresa algo no convertible (ej. 'uno' en int) se lanzará


# ---------------------------------------------------------------
# C) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
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
# Ejercicio 04 - Parámetros de print
# Enunciado: Imprime tres palabras en una sola línea separadas por ' - ' usando sep.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Ejercicio 06 - Conversión básica
# Enunciado: Lee un año como texto, conviértelo a int y muestra su 
# tipo antes y después.
# --- Plantilla de inicio ---
# (Escribe tu solución debajo, respeta la ejecución secuencial)
# ---------------------------------------------------------------
