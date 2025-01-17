"""
Crear una función que  genere un personaje, le pedimos al usuario un nombre y un tipo de personaje
apartir de ahi usamos la funcion de tirar dados para sacar las estadisticas de salud del personaje
(cara + lanzamiento) * (numero_caras / 2) + 10
tambien crear una funcion para gnerar las estadisticas de fuerza del personaje
(cara + lanzamiento) * (numero_caras / 2) + 12
Sumado a eso usamos las librerias time y os para manejar los tiempos en pantalla
Todo esto debe estar en un bucle while para que el juego no termine hasta que el usuario decida salir y pueda seguir creando personajes
"""

import time, os, random

print("""Bienvenido al generador de personajes
Aqui podras crear personajes con estadisticas aleatorias
Comencemos!!!!""")
time.sleep(3)
os.system("Clear")

play = "yes"  # Definimos una variable para que el juego no se repita
while play == "yes":  #Hacemos un ciclo while para que el juego no se repita
    nombre = input("Ingrese el nombre del personaje: ")
    time.sleep(2)
    os.system("Clear")
    tipo = input("Ingrese el tipo de personaje: ")
    time.sleep(2)
    os.system("Clear")
    def personaje(nombre):
        return nombre

    def tipo_personaje(tipo):
        return tipo

    numero_caras = int(input("Ingrese un numero de caras del dado:  "))
    time.sleep(2)
    os.system("Clear")
    def dado_1(numero_caras):  #Definimos la funcion dado_1 que es el dado de 6 caras
        result = random.randint(1,numero_caras)  #Esto hace que el programa elija un numero random entre 1 y el numero de caras del dado
        return result  #Retornamos el resultado del lanzamiento

    def salud():
        cara = dado_1(numero_caras)
        lanzamiento = dado_1(numero_caras)
        result = (cara + lanzamiento) * (numero_caras / 2) + 10
        return int(result)

    def fuerza():
        cara = dado_1(numero_caras)
        lanzamiento = dado_1(numero_caras)
        result = (cara + lanzamiento) * (numero_caras / 2) + 12
        return int(result)
    print(f"""Tu personaje: {personaje(nombre).title()} 
        Tipo: {tipo_personaje(tipo).title()}
        tiene
        salud: {salud()}
        fuerza: {fuerza()}""")
    time.sleep(5)

    play = input("Quieres crear otro personaje? (yes/no): ")  #Preguntamos si quiere crear otro personaje
    time.sleep(1)
    os.system("clear")
    if play == "yes":
        continue
    elif play != "yes":
        print("Goodbye!")
        time.sleep(2)
        os.system("clear")
    exit()


"""
Solucion del curso 100 dias de python
"""

# import os, random, time

# def rolldice(side):
#     result =  random.randint(1, side)
#     return result

# def health():
#     health_stat = ((rolldice(6) * rolldice(12)) / 2) + 10
#     return int(health_stat)

# def strength():
#     strength_stat = ((rolldice(6) * rolldice(8)) / 2 + 12)
#     return int(strength_stat)

# while True:
#     print("CHARACTER BUILDER")
#     print()
#     name = input("Enter your character's name: ")
#     type = input("Enter your character's type: ")
#     print()
#     print(name)
#     print(f"HEALTH: {health()}")
#     print(type)
#     print(f"STRENGTH: {strength()}")
#     print()
#     print("May your name go down in history!")
#     print()
#     again = input("Again ? ")
#     if again == "yes":
#         continue
#     else:
#         break
# print("Good bye!")
