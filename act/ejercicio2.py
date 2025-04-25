sueldo = float(input("Introduce el sueldo: "))
bono = 0
if sueldo > 3000:

    bono = sueldo * 0.10
elif sueldo > 1500 and sueldo <= 3000:
    bono = sueldo * 0.05
elif sueldo < 1500:
    bono = sueldo
    
    
    
print( "El sueldo es: {sueldo: .2F}")
print( "El bono es: {bono: .2f}")
print(f"Salario total: {sueldo + bono: .2f}")
            

        