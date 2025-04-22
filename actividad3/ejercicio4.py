# Cálculo del consumo de combustible


distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros = float(input("Ingrese la cantidad de litros consumidos: "))
precio_por_litro = float(input("Ingrese el precio por litro de combustible: "))

rendimiento = distancia / litros

gasto_total = litros * precio_por_litro

print(f"Distancia recorrida: {distancia:.2f} km")
print(f"Litros consumidos: {litros:.2f} L")
print(f"Precio por litro: {precio_por_litro:.2f} $/L")
print(f"Rendimiento del vehículo: {rendimiento:.2f} km/L")
print(f"Gasto total en combustible: {gasto_total:.2f} $")