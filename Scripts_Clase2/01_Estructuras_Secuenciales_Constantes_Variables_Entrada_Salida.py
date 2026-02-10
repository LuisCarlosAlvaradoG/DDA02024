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

# Asignación simple (variable -> valor)
nombre_curso = "Algoritmos y programación"  #str
creditos = 8                                #int
calificacion_promedio = 6.5                 #float
activo = True                               #bool

# Mostrar valores y sus tipos
type(nombre_curso)
type(creditos)
type(calificacion_promedio)
type(activo)

# Constante por convención (no se debe modificar)
PI = 3.14159
print(PI)

# Identificadores válidos/ inválidos (solo comentarios):
# válido: user_name, _hidden_value, age2, TOTAL_SUM
# inválido: 2age (no puede empezar con dígito), user-name (guion NO permitido), class (keyword)

# Palabras reservadas (keywords): nombres que NO pueden usarse como identificadores.
# Las listamos solo para referencia visual.
import keyword
keyword.kwlist
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
print("Hola", "mundo")
print("Hola", "mundo", sep="*")
print("Hola mundo", sep="*")
print("Hola", 5, sep="*")

print("Sin salto al final", end="")
print("Continuación de la misma línea")
# Formatos:
alumno = "Luis"
edad = 25

print("Alumno:", alumno, "| Edad:", edad)              # Separado por comas
print("Alumno:" + alumno + "| Edad:" + str(edad))      # Concatenación
print(f"Alumno: {alumno} | Edad: {edad}")              # f-string

# --- Código ilustrativo: input ---

# Lectura y conversión básica


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