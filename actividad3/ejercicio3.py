# Cálculo de interés compuesto
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_anual = float(input("Ingrese la tasa de interés anual en porcentaje: "))
años = int(input("Ingrese el número de años: "))

valor =(1 + tasa_anual)**años
monto_final = valor * capital_inicial
interes_ganado = monto_final - capital_inicial
print(f"Capital inicial: {capital_inicial:.2f}")
print(f"Tasa de interés anual: {tasa_anual:.2f}%")
print(f"Años: {años}")
print(f"Monto final: {monto_final:.2f}")
print(f"Interés ganado: {interes_ganado:.2f}")
