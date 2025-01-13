# num = float(input("Ingrese un número: "))
# print(round(num,2))


# my_socore = int(input("Your score:  "))
# if my_socore > 100000:
#     print("Winner!")
# else:
#     print("Loser!")

# pi = float(input("Ingrese el valor de pi"))
# reduce = input("Desea reducir el valor de pi a 4 decimales?:  ")
# if reduce == "si":
#     print(round(pi,4))


age = int(input("Ingrese su año de nacimiento: "))
if age >= 1883 and age <= 1900:
    print(f"{age} is Lost Generation")
elif age >= 1901 and age <= 1927:
    print(f"{age} is Greatest Generation")
elif age >= 1928 and age <= 1945:
    print(f"{age} is Silent Generation")
elif age >= 1946 and age <= 1964:
    print(f"{age} is Baby Boomer")
elif age >= 1965 and age <= 1980:
    print(f"{age} is Generation X")
elif age >= 1981 and age <= 1996:
    print(f"{age} is Millennials")
elif age >= 1997 and age <= 2012:
    print(f"{age} is Generation Z")
elif age >= 2013 and age <= 2025:
    print(f"{age} is Generation Alpha")
else:
    print("No Generation")