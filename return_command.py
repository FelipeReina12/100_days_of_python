# def pin_picker(number):  #Definimos la funcion pin_picker
#     import random  #Importamos la libreria random
#     pin = ""  #Creamos la variable donde almacenaremos el pin por eso está vacía
#     for i in range(number):  #Aqui estamos diciendo que el pin tenga tantos digitos como el número que le pasemos
#         pin += str(random.randint(0, 9))  #Usamos el += para ir agregando los digitos al pin tambien el str para que sea un string
#     return pin  #Retornamos la variable pin con el pin ya establecido
# print(pin_picker(8))  #Por último llamamos a la función y le pasamos el número de digitos que queremos que tenga


def area_of_tringle(base, height):
    area = 0.5 * base * height
    return area
base = int(input("Ingresa la base del triangulo:  "))
height = int(input("Ingresa la altura del triangulo:  "))
print(f"El area del triangulo es: {round(area_of_tringle(base, height), 2)}")  


"""
Generador de caracteristicas de personajes 
Crear una funcion que tire un dado de cualquier tamaño y devuelve
ese numero, luego crear una funcion que tira un dado de 6 caras y un dado de 8 caras y multiplica esos dos numeros 
y devuelve el resultado como la salud de un personaje
"""