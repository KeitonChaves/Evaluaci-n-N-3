import globales
import random


producto = globales.leer_archivo_json("productos.json")
valor = globales.leer_archivo_json("venta_productos.json")
iva = 0.19


def asignar_montos():
    while True:
        todos_los_productos = producto["nombre"]
        for producto in todos_los_productos:
            nombre_producto = ""
            print()

    


