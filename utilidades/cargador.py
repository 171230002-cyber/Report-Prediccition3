import json

# Importa la clase Equipo, que representa a cada selección
# participante del Mundial.
from modelos.equipo import Equipo

# Función encargada de cargar todos los equipos
# almacenados en el archivo equipos.json.
def cargar_equipos():

    # Abre el archivo JSON que contiene la información
    # de todos los equipos participantes.
    with open("datos/equipos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    # Lista donde se almacenarán los objetos Equipo.
    equipos = []

    # Recorre cada equipo encontrado dentro del JSON.
    for e in datos["equipos"]:


        # Crea un objeto Equipo utilizando los datos
        # obtenidos del archivo.
        #
        # nombre  -> nombre de la selección
        # ranking -> posición en el ranking FIFA
        # nivel   -> nivel de habilidad utilizado en la simulación
        equipo = Equipo(
            e["nombre"],
            e["ranking"],
            e["nivel"]
        )

        # Agrega el objeto a la lista de equipos.
        equipos.append(equipo)

    # Devuelve la lista completa de objetos Equipo.
    return equipos

# Función que busca un equipo por nombre dentro
# de una lista de objetos Equipo.
def buscar_equipo(nombre, equipos):

    # Recorre todos los equipos disponibles.
    for equipo in equipos:

        # Si encuentra una coincidencia exacta,
        # devuelve el objeto Equipo correspondiente.
        if equipo.nombre == nombre:
            return equipo

    # Si no encuentra el equipo, devuelve None.
    # Esto permite detectar errores o equipos faltantes
    return None