# tv_show = input("What's your favourite tv show?  ")
# if tv_show.capitalize() == "Pepa pig":
#     print("Ugh, why?")
#     character = input("What's your favourite character?  ")  #Esto lo preguntará si el usuario dice que su show favorito es Pepa Pig
#     if character.capitalize() == "Daddy pig":
#         print("Right answer")
#     else:
#         print("Nah, Daddy Pig is the best")
# elif tv_show.capitalize() == "Spongebob squarepants":
#     print("Good choice")
# else:
#     print("Yeah, that's cool and all...")


"""
Crear un programa que pregunte al usuario ¿Cual es su anime favorito? y hacerele varias preguntas para saber si es un fan o no lo es
"""
your_anime = input("Cual es tu anime favorito?:  ")
if your_anime.capitalize() == "Dragon ball z" or your_anime.capitalize() == "Dragon ball": 
    print("Eres un fan de Goku?")
    personaje = input("Como se llama el personaje principal?:  ")
    if personaje.capitalize() == "Goku":
        print("Pasas a la siguiente pregunta")
        transformaciones = input("Cuantas trnasformaciones tiene Vegeta?:  ")
        if transformaciones == "5":
            print("Pasas a la siguiente pregunta")
            poderes = input("Cual es el poder que le enseñó el maestro Roshi a goku?:  ")
            if poderes.capitalize() == "Kamehameha":
                print("Pasas a la siguiente pregunta")
                novia = input("Como se llama la novia de Gohan?:  ")
                if novia.capitalize() == "Videl":
                    print("Eres un verdadero fan de Dragon Ball")
else:
    print("No eres fan de Dragon Ball Z, no pasa nada")
