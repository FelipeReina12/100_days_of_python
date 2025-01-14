# def roll_dice():
#     import random
#     dice = random.randint(1,6)
#     print(f"Your rolled {dice}")
# roll_dice()


#Otra forma de hacerlo es la siguiente
# import random  # Importa el módulo random para generar números aleatorios
# num = random.randint(1,6)  # Genera un número aleatorio entre 1 y 6 y lo almacena en la variable num
# def dado(num):  # Define una función llamada dado que toma un argumento num
#     return num  # Devuelve el valor de num
# print(f"Has sacado un: {dado(num)}")  # Imprime el resultado de la función dado con el número generado


# name = "Felipe"  # Asigna el valor "Felipe" a la variable name
# def saludar(name):  # Define una función llamada saludar que toma un argumento name
#     return f"Hola {name}".lower()  # Devuelve un saludo en minúsculas con el nombre proporcionado
# print(saludar(name))  # Imprime el resultado de la función saludar con el nombre "Felipe"


# def count_to_five():
#     for i in range(1,6):
#         print(i) 
# count_to_five()


"""
Inicio de sesion con username y contraseña
Hacer una función que los coloque dentro de un loop para que siga preguntando por si el usuario se equivoca
"""

user_name = "Zetawise"
password = "kamehameha"
intentos = 0

def valid_user():
    global intentos  # Se declara como global para modificar la variable fuera de la función
    while True:
        user = input("Ingrese su nombre de usuario: ")
        password_user = input("Ingrese su contraseña: ")
        if user == user_name and password_user == password:
            intentos += 1
            print("Bienvenido")
            break
        else:
            intentos += 1
            print("Usuario o contraseña incorrectos")
    print(f"Has realizado: {intentos} intentos")

valid_user()




