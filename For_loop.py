# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1

# print("Ahora con un For")
# #Lo mismo pero con un for
# for counter in range(10):
#     print(counter)


# for days in range(1,8):
#     print(f"day {days}")


# for j in range(11):
#     print(f"{j} * 2 = {j * 2}")


"""
Dinero prestado = 1000 dolares
Interés anual = 5%
años = 10
"""

dinero = 1000
interes = 0.05
años = 10



total = dinero  # Inicializa la variable 'total' con el valor de 'dinero'
for i in range(años):  # Itera sobre el número de años especificado en la variable 'años'
    interes_anual = round(total * interes, 2)  # Calcula el interés anual multiplicando el 'total' actual por la tasa de interés 'interes'
    total += interes_anual  # Suma el interés anual al 'total' actual
    print(f"El interés en el año {i + 1} es: {round(total,2)}")  # Imprime el total acumulado hasta el año actual, redondeado a 2 decimales
print(f"Debes pagar {round(total, 2)} de intereses")