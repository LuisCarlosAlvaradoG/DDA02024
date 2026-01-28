p_tacos = 15
p_hamburguesas = 80
p_postres = 35

c_tacos = int(input("Ingresa el número de tacos vendidos "))
c_hamburguesas = int(input("Ingresa el número de hamburguesas vendidas "))
c_postres = int(input("Ingresa el número de postres vendidos "))

total = p_tacos * c_tacos + p_hamburguesas * c_hamburguesas + p_postres * c_postres
print("El total de la venta es:", total, "pesos")