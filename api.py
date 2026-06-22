import json

# URL ficticia utilizada para simular un servicio API.
# Actualmente no se realizan peticiones reales a internet;
# únicamente se muestra en consola para dar la apariencia
# de una consulta a una API.
API_URL = "https://api.worldcupsimulator2026.com"


# Función que obtiene la información de los equipos.
#
# En una versión futura podría realizar una petición HTTP
# real al endpoint /equipos.
#
# Actualmente:
# 1. Muestra en consola la ruta consultada.
# 2. Lee los datos desde equipos.json.
# 3. Devuelve el contenido del archivo.
def obtener_equipos():

    # Simulación de una petición GET.
    print(f"GET {API_URL}/equipos")

    # Abre el archivo local con los equipos.
    with open("datos/equipos.json", "r", encoding="utf-8") as archivo:

        # Convierte el JSON en un diccionario de Python
        # y lo devuelve.
        return json.load(archivo)

# Función que obtiene la distribución de grupos.
#
# En una versión futura podría consultar un endpoint real
# llamado /grupos.
#
# Actualmente:
# 1. Muestra en consola la ruta consultada.
# 2. Lee los grupos desde grupos.json.
# 3. Devuelve el contenido del archivo.
def obtener_grupos():

    # Simulación de una petición GET.
    print(f"GET {API_URL}/grupos")

    # Abre el archivo local con la distribución
    # de los grupos del Mundial.
    with open("datos/grupos.json", "r", encoding="utf-8") as archivo:

        # Convierte el JSON en un diccionario de Python
        # y lo devuelve.
        return json.load(archivo)