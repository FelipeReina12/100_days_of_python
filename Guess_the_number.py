print("uno en un millon")
intentos = 0

while True:
    numero = int(input("Ingresa el numero que crees:  "))
    intentos += 1
    if numero == 53845:
        break
    elif numero < 53845:
        print("Estás por debajo del numero sigue intentando")
    elif numero > 53845:
        print("Estás por encima del número sigue intentando")
    else:
        print("Entrada no valida")
print(f"""Has adivinado
despues de {intentos} intentos""")