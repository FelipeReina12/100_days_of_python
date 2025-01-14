"""
les pide al usuario que ingrese una tabla de multiplicar
Se le pregunta al usuario cada tabla es decie x * x asi hasta 10
Si la respuesta es correcta recivirá un punto, de lo contrario tendra 0 puntos
Al final le mostrará cual ha sido su puntiación
"""

print("Math Game!")
tabla = int(input("Ingresa la tabla de multiplicar que deseas:  "))
puntaje = 0

for i in range(1, 11):
    pregunta = int(input(f"¿Cuánto es {i} * {tabla}? "))
    if pregunta == i * tabla:
        print("Bien hecho!!!")
        puntaje += 1
    else:
        print(f"Lo siento, la respuesta correcta es {i * tabla}")
print("Tu puntaje es: ", puntaje)