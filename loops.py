# counter = 0  #Inicializamos el contador
# while counter < 101:  #Mientras el contador esta menor a 11 entonces haga una accion
#     print(counter)
#     counter += 2  #Incrementamos el contador en 2


# exit = ""
# while exit.capitalize() != "Yes":
#     print("🤯")
#     exit = input("¿Quieres salir? (Yes/No): ")
#     print("¡Hasta luego!")  #Imprime un mensaje de despedida


# while True:
#     #Preguntar al usuario qué animal quiere ver
#     animal = input("¿Qué animal quieres ver? (Escribe 'Salir' para terminar): ").capitalize()
#     if animal == "Vaca":
#         print("🐮")
#     elif animal == "Perro":
#         print("🐶")
#     elif animal == "Gato":
#         print("🐱")
#     elif animal == "Pájaro":
#         print("🐦")
#     elif animal == "Salir":
#         break  # Salir del bucle si el usuario escribe "Salir"
#     else:
#         print("Animal no reconocido. Intenta con otro.")
    
#     continuar = input("¿Quieres ver otro animal? (Yes/No): ").capitalize()
#     if continuar == "No":
#         break  # Salir del bucle si el usuario no quiere continuar


# numero = 0
# print("Tabla del 3")
# while numero < 11:
#     print(f"{numero * 3}")
#     numero += 1
# print("Fin")


# want_greet = "S"  #Siempre dar un valor inicial
# while want_greet == "S":  #Mientras que want_greet sea igual a "S" entonces haga una accion, en este caso imprimir "Hola que tal"
#     print("Hola que tal")
#     want_greet = input("¿Quieres saludar a alguien? (S/N): ").upper()  #Tenemos la opcion de continiar con el bucle o salir con "N"  
#     #Si el usuario escribe "S" entonces continua, de lo contrario sale del bucle
# print("Adiós")  #Este print se ejecuta una vez que el bucle se detiene por eso no está sangrado


# max_saludos = 4  #Inicializamos el numero maximo de saludos
# num_saludos = 0  #Asigaamos un valor inicial
# saludos = "S"

# while saludos == "S":
#     print("Hola que tal! ")
#     num_saludos += 1  #Sumamos un saludo a la cuenta
#     if num_saludos == max_saludos:  #Si llegamos al valor maximo de saludos ya establecido 
#         print("Maximo numero de saludos alcanzados")
#         break  #Esto significa que ya no podemos seguir saludo por lo tanto sale del bucle
#     saludos = input("Desea saludar a alguien? (S/N): ").upper()
#     print(f"vas {num_saludos} saludos")
# print("Que tengas un buen dia")


# max_saludos = 4  #Inicializamos el numero maximo de saludos
# num_saludos = 0  #Asigaamos un valor inicial
# saludos = "S"

# while saludos == "S":
#     print("Hola que tal! ")
#     num_saludos += 1  #Sumamos un saludo a la cuenta
#     if num_saludos == max_saludos:  #Si llegamos al valor maximo de saludos ya establecido 
#         print("Maximo numero de saludos alcanzados")
#         break  #Esto significa que ya no podemos seguir saludo por lo tanto sale del bucle
#     saludos = input("Desea saludar a alguien? (S/N): ").upper()
#     print(f"vas {num_saludos} saludos")
# else:
#     print("Usted no quiere mas saludos")
# print("Que tengas un buen dia")


# want_greets = "S"  # Definición de la variable `want_greets` con el valor inicial "S"
# valid_options = 0  # Definición de la variable `valid_options` con el valor inicial 0

# # Inicio de un bucle `while` que se ejecuta mientras `want_greets` sea igual a "S"
# while want_greets == "S":
#     # Imprime un saludo en la consola
#     print("Hola que tal! ")
#     # Solicita al usuario que ingrese "S" o "N" para continuar o detener los saludos
#     want_greets = input("Quiere otro saludo [S/N]:  ").capitalize()
#     # Verifica si la entrada del usuario no es "S" ni "N"
#     if want_greets not in ["S", "N"]:
#         # Si la entrada no es válida, imprime un mensaje de error
#         print("No le he entendido pero le saludo")
#         # Reinicia `want_greets` a "S" para continuar el bucle
#         want_greets = "S"
#         # Salta a la siguiente iteración del bucle sin ejecutar el código restante
#         continue
#     # Incrementa el contador de respuestas válidas en 1
#     valid_options += 1
# # Imprime el número total de respuestas válidas ingresadas por el usuario
# print(f"{valid_options} respuestas validas")
# # Imprime un mensaje de despedida
# print("Que tengas un buen dia")


while True:
    mark = float(input("Introduzca una nueva nota:  "))
    if not(0 <= mark <= 10):
        print("Nota fuera de rango")
        break
    print(round(mark,2))

