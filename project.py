"""
Crear una función que  genere un personaje, le pedimos al usuario un nombre y un tipo de personaje
apartir de ahi usamos la funcion de tirar dados para sacar las estadisticas de salud del personaje
(cara + lanzamiento) * (numero_caras / 2) + 10
tambien crear una funcion para gnerar las estadisticas de fuerza del personaje
(cara + lanzamiento) * (numero_caras / 2) + 12
Sumado a eso usamos las librerias time y os para manejar los tiempos en pantalla
Todo esto debe estar en un bucle while para que el juego no termine hasta que el usuario decida salir y pueda seguir creando personajes
"""

import time 
import os
import random

nombre = input("Ingrese el nombre del personaje: ")
tipo = input("Ingrese el tipo de personaje: ")
# def personaje():    
#     return nombre, tipo
def personaje(nombre):
  return nombre

def tipo_personaje(tipo):
  return tipo



numero_caras = int(input("Ingrese un numero de caras del dado:  "))
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





# import random



# def health_personaje():  #Definimos la función healt  
#   die1 = dado_1(6)  #Usamos la función dado_1 que acabamos de crear para tirar un dado de 6 caras 
#   die2 = dado_1(8)  #Usamos la función dado_1 para tirar un dado esta ves de 8 caras
#   return die1 * die2 #Multiplicamos las dos tiradas y retornamos el resultado

# def strength_personaje():  #Definimos la función strength_personaje 
#   die3 = (health_personaje() * dado_1(6)) /2  #Creamos un tercer lanzamiento usando la función healt y la función dado_1
#   return die3

# play = "yes"  # Definimos una variable para que el juego no se repita
# while play == "yes":  #Hacemos un ciclo while para que el juego no se repita
#   character = input("Name ur character:")  #Pedimos al usuario un nombre de personaje
#   health = health_personaje()  #Llamamos a la función health_personaje y lmacenamos el resultado en una variable llamada health
#   strength = strength_personaje()  #Llamamos a la función strength_personaje y almacenamos el resultado en una variable llamada strength
#   print("Health:", health)
#   print("Strength:", strength)
#   play = input("Do you want to play again?")
#   if play != "yes":
    
#     print("Goodbye!")
#     exit()