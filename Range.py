# for i in range(100, 111):  #Imprimir numeros del 100 al 110
#     print(i)


# for i in range(100, 111, 2):  #Imprimir numeros del 100 al 110 en un paso de 2 en 2
#     print(i)

for i in range(10, 0, -1):  #Imprimir del 10 al 1 de uno en uno 
    print(i)

print("Thirteen times table: ")
for i in range(1, 14):  #Imprimir la tabla del 13
    print(f"{i} x 13 = {i * 13}")


print("List Generator")
start = int(input("Con que numero quieres empezar: "))
end = int(input("Con que numero quieres terminar: "))
step = int(input("Con que paso quieres avanzar: "))

for i in range(start, end + 1, step):
    print(i)