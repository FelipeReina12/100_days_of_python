print("Examen calculator")
examen = input("Nombre del examen:  ")
score = float(input("Ingresa el puntaje máximo: "))
your_score = float(input("Ingresa tu puntaje: "))

result = your_score / score * 100
print(f"Tu puntaje es: {round(result,2)}%")
if result >= 90:
    print("Tu calificación es A+")
elif result >= 80 and result < 90:
    print("Tu calificación es A-")
elif result >= 70 and result < 80:
    print("Tu calificación es B")
elif result >= 60 and result < 70:
    print("Tu calificación es C")
elif result >= 50 and result < 60:
    print("Tu calificación es D")
elif result >= 40 and result < 50:
    print("Tu calificación es U")
else:
    print("Puntaje no valido")