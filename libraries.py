import random 

# my_number = random.randint(1,100)
# print(my_number)


# for i in range(1, 10):
#     my_number = random.randint(1,100)
#     print(f"Numero aleatorio: {my_number}")


"""
Generar un numero aleatorio entre 1 y 1.000.000
"""

print("uno en un millon")
intentos = 0

while True:
    numero = int(input("Ingresa el numero que crees:  "))
    intentos += 1
    num_random = random.randint(1, 1000000)
    if numero == num_random:
        break
    elif numero < num_random:
        print("Estás por debajo del numero sigue intentando")
    elif numero > num_random:
        print("Estás por encima del número sigue intentando")
    else:
        print("Entrada no valida")
print(f"""Has adivinado
despues de {intentos} intentos""")