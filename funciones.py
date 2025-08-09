# En este archivo solo se almacenan las funciones/ procedimientos utilizadas para los distintos menus de la aplicación principal
import datetime
from collections import defaultdict

# Cada valor corresponde a la contaminación por kilometro
CONTAMINACION = {
    "A": 0.192,  # Auto
    "M": 0.1,  # Moto
    "C": 0.089,  # Colectivo
    "B": 0,  # Bicicleta
    "P": 0,  # Caminando/apata
}

def registrar_nuevo_viaje():
    print("-------------------------------------------------------------------")
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Ingrese los datos del viaje realizado: ")
    inicio = input("Ingrese desde donde parte su viaje: ")
    destino = input("Ingrese el destino: ")
    kilometros = int(input("Cuántos kilometros recorrió?"))
    print("Al momento de ingresar el medio de transporte tener en cuenta \n" \
    "A = Auto, M = Moto, C = Colectivo, B = Bicicleta, P = Caminando")
    transporte = input("Ingrese el medio de transporte: ")
    print("-------------------------------------------------------------------")

    # Almaceno la información momentaneamente para no tener que estar leyendo constantemente del disco la información para las demás funciones
    viaje_guardado_momentaneamente = {
        "fecha_hora": fecha_hora,
        "inicio": inicio,
        "destino": destino,
        "kilometros": kilometros,
        "transporte": transporte,
    }
    return viaje_guardado_momentaneamente


# Esta función se encarga de poner en memoria la información del archivo VIAJES.txt, ahorrandose el trabajar continuamente con el with open(VIAJES.txt)
def agregar_viajes():
    viajes = []
    try:
        with open("VIAJES.txt", "r") as archivo:
            for linea in archivo:
                # Separar la línea por comas
                partes = linea.strip().split(",")
                if len(partes) == 5:
                    viaje = {
                        "fecha_hora": partes[0],
                        "inicio": partes[1],
                        "destino": partes[2],
                        "kilometros": int(partes[3]),
                        "transporte": partes[4],
                    }
                    viajes.append(viaje)
    except FileNotFoundError:
        print("El archivo VIAJES.txt no fue encontrado.")
    return viajes


# Almacena todos los viajes cargados en el archivo de texto
def almacenar_viaje(viaje_guardado_momentaneamente):
    with open("VIAJES.txt", "a") as archivo:
        for viaje in viaje_guardado_momentaneamente:
            linea = f"{viaje['fecha_hora']},{viaje['inicio']},{viaje['destino']},{viaje['kilometros']},{viaje['transporte']}\n"
            archivo.write(linea)


# Devuelve lo contaminado por día, semana y mes
def analizar_contaminacion(viaje_guardado_momentaneamente):
    contaminacion_dia = defaultdict(float)
    contaminacion_semana = defaultdict(float)
    contaminacion_mes = defaultdict(float)

    for viaje in viaje_guardado_momentaneamente:
        try:
            # Extraer fecha y hora
            fecha = datetime.datetime.strptime(
                viaje["fecha_hora"], "%Y-%m-%d %H:%M:%S"
            ).date()

            # Extraer transporte y kilometraje
            transporte = viaje["transporte"].upper()
            km = viaje["kilometros"]

            # Calcular contaminación
            contaminacion = km * CONTAMINACION.get(transporte, 0)

            # Agrupar por día, semana y mes
            contaminacion_dia[fecha] += contaminacion
            contaminacion_semana[
                fecha.isocalendar()[1]
            ] += contaminacion  # Número de semana
            contaminacion_mes[fecha.month] += contaminacion

        except Exception as e:
            # Esta línea es útil para ver si hay otros errores
            print(f"Error al procesar el viaje: {viaje} - Error: {e}")
            continue

    print("\n--- Contaminación por Día ---")
    for fecha, total in sorted(contaminacion_dia.items()):
        print(f"{fecha}: {total:.3f} kg CO2")

    print("\n--- Contaminación por Semana ---")
    for semana, total in sorted(contaminacion_semana.items()):
        print(f"Semana {semana}: {total:.3f} kg CO2")

    print("\n--- Contaminación por Mes ---")
    for mes, total in sorted(contaminacion_mes.items()):
        print(f"Mes {mes}: {total:.3f} kg CO2")


def mostrar_historial(viaje_guardado_momentaneamente):
    print("-----------------------------------")
    print("HISTORIAL DE FORMA DE TRANSPORTE: ")
    for viaje in reversed(viaje_guardado_momentaneamente):
        transporte = viaje["transporte"].upper()
        if transporte in CONTAMINACION:
            if transporte == "A":
                print("AUTO")
            elif transporte == "M":
                print("MOTO")
            elif transporte == "C":
                print("COLECTIVO")
            elif transporte == "B":
                print("BICICLETA")
            elif transporte == "P":
                print("CAMINANDO")
    print("-----------------------------------")
    volver_menu = input(print("Para volver al menu principal presione enter"))
