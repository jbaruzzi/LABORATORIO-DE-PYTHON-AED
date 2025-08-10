# Importo las funciones que va a usar la app
from funciones import agregar_viajes, registrar_nuevo_viaje, almacenar_viaje, analizar_contaminacion, mostrar_historial

opciones_menu = [1, 2, 3, 4]

# Estructura del menú
def mostrar_menu():
    print("-----------------------------")
    print("Not Pollution")
    print("-----------------------------")
    print("1. Registrar nuevo viaje.")
    print("2. Ver contaminación total.")
    print("3. Ver historial de viajes.")
    print("4. Salir.")
    print("-----------------------------")

# Bloque principal de la app
def app():
    viaje_guardado_momentaneamente = agregar_viajes()
    viajes_nuevos = []
    while True:
        mostrar_menu()
        opcion = int(input("Elija una opción: "))
        if opcion not in opciones_menu:
            print("Esa opción no es válida. Ingrese la opción nuevamente.")
            continue

        if opcion == 1:
            nuevo_viaje = registrar_nuevo_viaje()
            viaje_guardado_momentaneamente.append(nuevo_viaje)
            viajes_nuevos.append(nuevo_viaje)
            viaje_guardado_momentaneamente.append(nuevo_viaje)
        elif opcion == 2:
            analizar_contaminacion(viaje_guardado_momentaneamente)
        elif opcion == 3:
            mostrar_historial(viaje_guardado_momentaneamente)
        elif opcion == 4:
            if viajes_nuevos:
                print("Guardando cambios...")
                almacenar_viaje(viaje_guardado_momentaneamente)
            print("Hasta la próxima...")
            break

# Ejecuta la app
app()
