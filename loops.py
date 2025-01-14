# counter = 0  #Inicializamos el contador
# while counter < 101:  #Mientras el contador esta menor a 11 entonces haga una accion
#     print(counter)
#     counter += 2  #Incrementamos el contador en 2


# exit = ""
# while exit.capitalize() != "Yes":
#     print("🤯")
#     exit = input("¿Quieres salir? (Yes/No): ")
#     print("¡Hasta luego!")  #Imprime un mensaje de despedida


while True:
    #Preguntar al usuario qué animal quiere ver
    animal = input("¿Qué animal quieres ver? (Escribe 'Salir' para terminar): ").capitalize()
    if animal == "Vaca":
        print("🐮")
    elif animal == "Perro":
        print("🐶")
    elif animal == "Gato":
        print("🐱")
    elif animal == "Pájaro":
        print("🐦")
    elif animal == "Salir":
        break  # Salir del bucle si el usuario escribe "Salir"
    else:
        print("Animal no reconocido. Intenta con otro.")
    
    continuar = input("¿Quieres ver otro animal? (Yes/No): ").capitalize()
    if continuar == "No":
        break  # Salir del bucle si el usuario no quiere continuar

