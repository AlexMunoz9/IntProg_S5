# Cálculo del consumo de agua por persona

litros_totales = float(input("Ingrese el total de litros consumidos en un mes en la vivienda: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que viven en la casa: "))


consumo_mensual_por_persona = litros_totales / cantidad_personas

consumo_diario_por_persona = consumo_mensual_por_persona / 30

print(f"Consumo total del mes: {litros_totales:.2f} litros")
print(f"Cantidad de personas en la vivienda: {cantidad_personas}")
print(f"Consumo mensual por persona: {consumo_mensual_por_persona:.2f} litros")
print(f"Consumo diario por persona: {consumo_diario_por_persona:.2f} litros")