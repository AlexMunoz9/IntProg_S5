#Control de inventario de un producto
cantidad_inicial = int(input("Ingrese la cantidad inicial de producto: "))
productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

suma = productos_recibidos + cantidad_inicial
total= productos_vendidos - suma
 
inventario_actual = suma - productos_vendidos

print(f"""Cantidad inicial: {cantidad_inicial:5}
Productos recibidos: {productos_recibidos:>2} 
Productos vendidos: {productos_vendidos:>3}
{"Inventario actual:" } {inventario_actual:>4}""")

