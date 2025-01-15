#Basicamente es la misma cosa que el ejemplo anterior, pero con un poco más de estructura y el parametro se lo pedimos al usuario 
# def wich_cake(ingredient):
#     if ingredient == "leche":
#         print("Mmmmm que rico, un pastel de leche")
#     elif ingredient == "chocolate":
#         print("Ummm esto va a quedar muy dulce")
#     elif ingredient == "brocoli":
#         print("Ugh no sabe muy bien")
#     else:
#         print("No tengo idea de que tipo de pastel es")
# ingredient = input("Ingresa el ingrediente para tu pastel:  ")
# wich_cake(ingredient)


#   # Define una función llamada "wich_cake" que recibe tres parámetros: ingredient, base y coating
# def wich_cake(ingredient, base, coating):
#     # Verifica si el ingrediente es "chocolate"
#     if ingredient == "chocolate":
#       # Si es "chocolate", imprime un mensaje de aprobación
#       print("Mmmm, chocolate cake is amazing")
#     # Verifica si el ingrediente es "brocoli"
#     elif ingredient == "brocoli":
#       # Si es "brocoli", imprime un mensaje de sorpresa
#       print("You what mate?")
#     # Si el ingrediente no es ni "chocolate" ni "brocoli"
#     else:
#       # Imprime un mensaje de aprobación moderada
#       print("Yeah, that's great I suppose...")
#     # Imprime un mensaje que incluye los tres parámetros
#     print(f"So want a {ingredient}, cake on a {base}, base whit, {coating} on top")
# ingredient = input("Name an ingredient:  ")
# base = input("What base do you want:  ")
# coating = input("Fave cake topping:  ")
#   # Llama a la función "wich_cake" con los parámetros ingresados por el usuario
# wich_cake(ingredient, base, coating)

# number_1 = int(input("Ingrese un numero para compararlo con otro:  "))
# number_2 = int(input("Ingrese otro numero para compararlo con el primero:  "))
# def bigger_number(number_1, number_2):
#     if (number_1 > number_2):
#         print(f"The number {number_1} is bigger")
#     else:
#         print(f"The number {number_2} is bigger")
# bigger_number(number_1, number_2)


"""
Crear una funcion que lance un dado de x numero de caras como parametro que ingresa el usuario
debe tener un loop para preguntar al usuario si desea continuar
Y luego dar el numero que saca en el lanzamiento 
"""
import random
def dado(caras):
    while True:
        lanzamiento = random.randint(1, caras)
        print(f"Has sacado un {lanzamiento}")
        continuar = input("Desea continuar? (Yes/No):  ")
        if continuar.lower() != "yes":
            break
    print("Saliendo del juego de dados")
caras = int(input("Ingrese el numero de caras del dado:  "))
dado(caras)