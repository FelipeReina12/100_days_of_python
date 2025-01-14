"""
Cuantos segundos tiene un año
"""

segundos_dia = 24 * 60 * 60
año = input("El año es bisiesto? si/no: ")
if(año == "si"):
    segundos_año = (366 * segundos_dia) 
    print(f"Un año bisiesto tiene {segundos_año} segundos")
else:
    segundos_año = 365 * segundos_dia
    print(f"Un año que no es bisiesto tiene: {segundos_año}, segundos")
    