import globales
import os
import ventas
import estadisticas

def menu_estadisticas():
    while True:
        os.system("cls")



def Menu():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Salir del programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar montos aleatorios") # funcion no asignada
            ventas.asignar_montos
        elif opcion == 2:
            input("2. Ver estadísticas")
        elif opcion == 3:
            return
    

Menu()