# Bucle infinito que se ejecutará hasta que se produzca una interrupción explícita
while True:
    # Mensaje de bienvenida y solicitud de dirección
    print("""You are in a coridoor,
do you go left or right?""")
    # Lectura de la dirección del usuario y conversión a mayúsculas
    direction = input(">: " ).capitalize()
    # Evaluación de la dirección
    if direction == "Left":
        # Si la dirección elegida es "Left", se imprime un mensaje que indica que el jugador ha muerto y se sale del bucle
        print("You have fallen to your death")
        break  #Este break nos permite salir del bucle infinito e imprime el mensaje de muerte
    # Evaluación de la dirección (continuación)
    elif direction == "Right":
        # Si la dirección elegida es "Right", se continúa con la siguiente iteración del bucle
        continue  #Continue hace que el programa se repita desde el comienzo y no imprima el mensaje de muerte
    # Evaluación de la dirección (otras opciones)
    else:
        # Si la dirección elegida no es ni "Left" ni "Right", se imprime un mensaje que indica que el jugador ha ganado y se sale del programa
        print("Ahh! You're a genius, You've won")
        exit()  #Exit sirve para detener el programa y no seguir ejecutándolo. Es similar al break pero sale del programa
print("The game is over, You've feiled!")