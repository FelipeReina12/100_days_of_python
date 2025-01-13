nombre = input("Ingresa tu nombre:  ")
print(f"Hola, {nombre.capitalize()} un gusto saludarte")
animo = input("Cuentame, ¿Como te sientes el dia de hoy?:  ")
if animo.capitalize() == "Bien":
    print("Genial, espero que el dia siga siendo tan agradable para ti")
elif animo.capitalize() == "Mal":
    print("Ugh, espero que las cosas mejoren para ti")
    motivacion = input("Quieres que te de una frase motivacional?:  ")
    if motivacion.capitalize() == "Si":
        print("¡Claro! La vida es un viaje, no un destino. aprovecha cada oportunidad para ser feliz")
    else:
        print("Ok, espero que te haya gustado nuestra conversacion")    
    otra = input("Quieres otra frase que te motive?:  ")
    if otra.capitalize() == "Si":
            print("¡Claro! La vida es un regalo, y tu decides como sacarle el mayor provecho")
    else:
            print("Ok, espero que te haya gustado nuestra conversacion")
    nueva_frase = input("Deseas otra frase para motivarte aun mas?:  ")
    if nueva_frase.capitalize() == "Si":
         print("¡Claro! La vida es un juego, y tu decides como jugarlo")
    else:
         print("Ok, espero que te haya gustado nuestra conversacion")
else:
     print("Ok nos vemos luego")
    

