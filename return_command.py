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

import random

play = "yes"  # Definimos una variable para que el juego no se repita

def dado_1(sides):  #Definimos la funcion dado_1 que es el dado de 6 caras
  result = random.randint(1,sides)  #Esto hace que el programa elija un numero random entre 1 y el numero de caras del dado
  return result  #Retornamos el resultado

def health_personaje():  #Definimos la función healt  
  die1 = dado_1(6)  #Usamos la función dado_1 que acabamos de crear para tirar un dado de 6 caras 
  die2 = dado_1(8)  #Usamos la función dado_1 para tirar un dado esta ves de 8 caras
  return die1 * die2 #Multiplicamos las dos tiradas y retornamos el resultado

def strength_personaje():  #Definimos la función strength_personaje 
  die3 = (health_personaje() * dado_1(6)) /2  #Creamos un tercer lanzamiento usando la función healt y la función dado_1
  return die3

while play == "yes":  #Hacemos un ciclo while para que el juego no se repita
  character = input("Name ur character:")  #Pedimos al usuario un nombre de personaje
  health = health_personaje()  #Llamamos a la función health_personaje y lmacenamos el resultado en una variable llamada health
  strength = strength_personaje()  #Llamamos a la función strength_personaje y almacenamos el resultado en una variable llamada strength
  print("Health:", health)
  print("Strength:", strength)
  play = input("Do you want to play again?")
  if play != "yes":
    print("Goodbye!")
    exit()
    