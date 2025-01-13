"""
+ se utiliza para sumar, - se utiliza para restar, * se utiliza para multiplicar, 
/ se utiliza para dividir, % se utiliza para obtener el residuo, // se utiliza para obtener el cociente
"""

# adding = 4 + 3
# print(adding)

# substraction = 8 - 2
# print(substraction)

# multiplication = 7.45 * 9.485
# print(round(multiplication,2))

# division = 85.45 / 5.8
# print(round(division,2))

# squared = 6 ** 2
# print(squared)

# modulo = 17 % 5
# print(modulo)

# divisor = 15 // 3
# print(divisor)


costo = float(input("Cual es el costo de la compra: $"))
numero_de_amigos = int(input("cuantos amigos estuvieron en la fiesta?: "))
propina = float(input("Ingrese la propina que desea dar 5%, 10%, o 15%: "))
if propina == 5:
    propina = 0.05
    total = (costo / numero_de_amigos) + (costo * propina) / numero_de_amigos
    print(f"El costo por persona es: ${round(total,2)}")
elif propina == 10:
    propina = 0.10
    total = (costo / numero_de_amigos) + (costo * propina) / numero_de_amigos
    print(f"El costo por persona es: ${round(total,2)}")
elif propina == 15:
    propina = 0.15
    total = (costo / numero_de_amigos) + (costo * propina) / numero_de_amigos
    print(f"El costo por persona es: ${round(total,2)}")
 #Para redondear siempre ponemos round("la variable donde almaceamos el dato", "el numero de decimales que queremos")
