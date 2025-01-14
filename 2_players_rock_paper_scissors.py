from getpass import getpass as input

# Inicializar los puntajes
player_1_score = 0
player_2_score = 0

print("EPIC 🪨   🧻   ✂️")
print("El juego termina cuando un jugador alcance 3 puntos.")

while player_1_score < 5 and player_2_score < 5:
    print("\nSelecciona tu movimiento (R, P or S): ")
    
    player_1 = input("Jugador 1 Ingresa tu movimiento:  ")
    player_2 = input("Jugador 2 Ingresa tu movimiento:  ")
    

    if player_1.capitalize() == "R" and player_2.capitalize() == "R":
        print("Ambos jugadores han seleccionado Roca, ¡Es un empate!")
    elif player_1.capitalize() == "P" and player_2.capitalize() == "P":
        print("Ambos jugadores han seleccionado Papel, ¡Es un empate!")
    elif player_1.capitalize() == "S" and player_2.capitalize() == "S":
        print("Ambos jugadores han seleccionado Tijeras, ¡Es un empate!")
    elif player_1.capitalize() == "R" and player_2.capitalize() == "P":
        print("Papel cubre Roca, Jugador 2 gana!")
        player_2_score += 1
    elif player_1.capitalize() == "R" and player_2.capitalize() == "S":
        print("Roca rompe Tijeras, Jugador 1 gana!")
        player_1_score += 1
    elif player_1.capitalize() == "P" and player_2.capitalize() == "R":
        print("Papel cubre Roca, Jugador 1 gana!")
        player_1_score += 1
    elif player_1.capitalize() == "P" and player_2.capitalize() == "S":
        print("Tijeras rompe Papel, Jugador 2 gana!")
        player_2_score += 1
    elif player_1.capitalize() == "S" and player_2.capitalize() == "R":
        print("Roca rompe Tijeras, Jugador 2 gana!")
        player_2_score += 1
    elif player_1.capitalize() == "S" and player_2.capitalize() == "P":
        print("Tijeras rompe Papel, Jugador 1 gana!")
        player_1_score += 1
    else:
        print("Movimiento no válido, ¡inténtalo de nuevo!")

    # Mostrar el puntaje actual
    print(f"Puntaje actual: Jugador 1 = {player_1_score}, Jugador 2 = {player_2_score}")

# Determinar al ganador
if player_1_score == 5:
    print("\n¡Jugador 1 ha ganado el juego!")
else:
    print("\n¡Jugador 2 ha ganado el juego!")

print("Gracias por jugar. ¡Hasta la próxima!")

