# def pin_picker(number):  #Definimos la funcion pin_picker
#     import random  #Importamos la libreria random
#     pin = ""  #Creamos la variable donde almacenaremos el pin por eso está vacía
#     for i in range(number):  #Aqui estamos diciendo que el pin tenga tantos digitos como el número que le pasemos
#         pin += str(random.randint(0, 9))  #Usamos el += para ir agregando los digitos al pin tambien el str para que sea un string
#     return pin  #Retornamos la variable pin con el pin ya establecido
# print(pin_picker(8))  #Por último llamamos a la función y le pasamos el número de digitos que queremos que tenga


# def area_of_tringle(base, height):
#     area = 0.5 * base * height
#     return area
# base = int(input("Ingresa la base del triangulo:  "))
# height = int(input("Ingresa la altura del triangulo:  "))
# print(f"El area del triangulo es: {round(area_of_tringle(base, height), 2)}")  


"""
Generador de caracteristicas de personajes 
Crear una funcion que tire un dado de cualquier tamaño y devuelve
ese numero, luego crear una funcion que tira un dado de 6 caras y un dado de 8 caras y multiplica esos dos numeros 
y devuelve el resultado como la salud de un personaje
"""

# import random

# def tirar_dado(tamano):
#     lanzamiento_1 = random.randint(1, tamano)
#     print(f"Haz sacado un: {lanzamiento_1}")
# tamano = int(input("Ingrese el numero de caras del dado:  "))
# tirar_dado(tamano)

import random

play = "yes"

def rollDie(sides):
  result = random.randint(1,sides)
  return result

def roll3die():
  die1 = rollDie(6)
  die2 = rollDie(6)
  die3 = rollDie(6)
  return die1 * die2 * die3

while play == "yes":
  character = input("Name ur character:")
  health = roll3die()
  strength = roll3die()
  print("Health:", health)
  print("Strength:", strength)
  play = input("Do u want to play again?")
  if play != "yes":
    print("Goodbye!")
    exit()