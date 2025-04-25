sueldo = float(input("Introduce el sueldo: "))
bono = 0
if sueldo > 3000:
    print("El bono sera el 10% del sueldo")
    bono = sueldo * 0.10
elif sueldo >= 1500 and sueldo <= 3000:
    print("El bono sera el 5% del sueldo")
    bono = sueldo * 0.05
elif sueldo <= 1500:
    print("No hay bono")