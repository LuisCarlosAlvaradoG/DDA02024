def examen_A():
    print("Examen Tipo A")
    # Preguntas teóricas
    print("1)  Pseudocódigo (g)")
    print("2)  Ordenado (i)")
    print("3)  Lenguaje de programación (f)")
    print("4)  De procesos (h)")
    print("5)  Orientado a objetos(a)")
    print("6)  Variable (b)")
    print("7)  Lógico (d)")
    print("8)  Type() (k)")
    print("9)  Precedencia (c)")
    print("10) Identación (l)")
    # Precedencia de operadores
    a = 3  
    b = 2  
    c = - 1  
    d = 1
    r1_a = a - c + 2 * 5 / b * d
    print(f"Desarrollo = 3 - -1 + 2 * 5 / 2 * 1 = 4 + 10 / 2 * 1 = 4 + 5 * 1 = {r1_a}")

    a = 4
    b = 1
    c = - 2
    d = 1
    r2_a = 8 % b - a * c ** 4 + d / 5
    print(f"Desarrollo = 8 % 1 - 4 * -2 ** 4 + 1 / 5 = 0 - 4 * 16 + 0.2 = {r2_a}")
          

    # Examen tipo A
    # 1) Torneo e-sports: acceso e inscripción 
    edad = 17
    ranking = 420
    tutor = True

    if (edad >= 18 or tutor) and ranking <= 500:
        print("Puede competir")
    else:
        print("No cumple los requisitos")

    if (ranking <= 100 and edad >= 16) or (tutor and ranking <= 400):
        print("Inscripción con bonificación")
    else:
        print("Inscripción estándar")

    # 2) Tienda online: envío y descuento
    total = 1350
    cupon = "VIP"          
    destino = "Nacional"   

    if (total >= 800 and destino == "Nacional") or cupon == "ENVIOFREE":
        print("Envío gratis")
    else:
        print("Envío con costo")

    if (cupon == "VIP" and total >= 1500) or (destino == "Internacional" and total >= 2000):
        print("Descuento adicional aplicado")
    else:
        print("Sin descuento adicional")

examen_A()

def examen_B():
    print("Examen Tipo B")
    # Preguntas teóricas
    print("1)  De procesos (j) ")
    print("2)  Lenguaje de programación (f)")
    print("3)  Ordenado (a)")
    print("4)  Pseudocódigo (i)")
    print("5)  Type (k)")
    print("6)  Variable (e)")
    print("7)  Logico (ñ)")
    print("8)  Orientado a objetos(g)")
    print("9)  Identacion (l)")
    print("10) Precedencia (c)")
    a = 2
    b = 3
    c = 1
    d = -1
    r1_b = a + b - c ** 2 + d / 4
    print("2 + 3 - 1 ** 2 + -1 / 4 = 5 - 1 + -0.25 = 4 - 0.25 = ", r1_b)

    a = 1
    b = 4
    c = 3
    d = -1
    r2_b = b + c * 5 / 4 ** d * a
    print("4 + 3 * 5 / 4 ** -1 * 1 = 4 + 15 / 0.25 * 1 = 4 + 60 * 1 = ", r2_b)
    #Examen tipo B
    # 1) Estatus académico y servicios
    promedio = 8.7
    faltas = 3
    adeudo = False

    if (promedio >= 8.5 and faltas <= 5) or promedio >= 9.5:
        print("Estatus: Alumno regular")
    else:
        print("Estatus: En seguimiento")

    if (not adeudo) and (promedio >= 8 or faltas < 2):
        print("Acceso a biblioteca habilitado")
    else:
        print("Acceso a biblioteca restringido")

    # 2) Sistema de seguridad y ventilación
    temperatura = 41     
    humedad = 25        
    puerta_cerrada = False

    if (temperatura > 40 and humedad < 30) or (not puerta_cerrada):
        print("Alarma activada")
    else:
        print("Sistema estable")

    if (temperatura >= 35 and humedad < 50) or puerta_cerrada:
        print("Activar ventilación")
    else:
        print("Ventilación normal")

examen_B()

# --- Entradas (ajústalas para tus pruebas) ---
clase = "economy"
equipaje_kg = 24
membresia = "Gold"
documento = "vigente"
asiento = "12A"

# --- Normalización de texto ---
cls = clase.strip().upper()
mem = membresia.strip().upper()
doc = documento.strip().lower()
asnt = asiento.strip().upper()

msg = ""

# Regla 1: Denegación por documento
if doc != "vigente":
    msg = "Embarque denegado"

# Regla 2: Embarque prioritario
if (msg == "") and (
    (cls == "BUSINESS") or
    (cls == "FIRST") or
    (cls == "ECONOMY" and (mem == "GOLD" or mem == "PLATINUM") and (equipaje_kg <= 25))
):
    msg = "Embarque prioritario"

# Regla 3: Exceso de equipaje (solo ECONOMY)
if (msg == "") and (cls == "ECONOMY") and (equipaje_kg > 23):
    msg = "Pagar exceso de equipaje"

# Regla 4: Ventana confirmada (solo ECONOMY)
if (msg == "") and (cls == "ECONOMY") and ((asnt[-1:] == "A") or (asnt[-1:] == "F")):
    msg = "Embarque estándar (asiento de ventana confirmado)"

# Regla 5: Por defecto
if msg == "":
    msg = "Embarque estándar"

print(msg)

#Función que devuelve una calificación con base a 15 puntos, según un número del 0 al 10.
def calificador():
    nota = float(input("Ingrese la calificación (o 'FIN' para terminar): "))
    while nota != "FIN":
        nota = nota
        nota_15 = (nota / 10) * 15
        print(round(nota_15, 2))
        nota = float(input("Ingrese la calificación (o 'FIN' para terminar): "))
calificador()