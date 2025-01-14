# while True:
#     print("This program is running")
#     go_again = input("Go again?: ").capitalize()
#     if go_again == "No":
#         break
# print("Aww, I was having a good time!")


# counter = 0
# while True:
#     answer = int(input("Enter a number:  "))
#     print("Adding it up!")
#     counter += answer
#     print(f"Counter total is {counter}")
#     add_another = input("Add another number?: ").capitalize()
#     if add_another == "No":
#         break
# print("Bye")


print("ADIVINA LA PALABRA!!!!!!")
print("""Si la vida fuera estable todo el tiempo
Yo no bebería ni malgastaria la _____""")

intentos = 1  #Asignamos un valor al contador 

while True:
    palabra  = input("Ingresa la palabra que falta:  ")
    if palabra.capitalize() == "Plata":
        break  #Si la palabra que ingresaste es la Plata , el programa se detiene y muestra el mensaje de victoria 
    else:
        print("No es esa palabra vuleve a intentarlo")  #Si no es la plabra, vuelve a preguntar y suma un intento al contador
        intentos += 1
print(f"""Lo lograste! 
despues de {intentos} intentos""")
