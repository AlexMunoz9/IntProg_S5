import datetime as dt
fecha_ingreso = input("Fecha ingreso yyyy-mm-dd: ")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
fecha_actual    = dt.date.now()

dias    = fecha_actual - fecha_ingreso. days
print(fecha_actual)
print(fecha_ingreso)
print("dias", dias)

if dias > 30:
    print("Cuenta inactiva")
    