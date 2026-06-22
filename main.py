import json

# Funciones que consultan la API y generan los archivos
# necesarios para la simulación.
from api import obtener_equipos, obtener_grupos

# Funciones auxiliares para cargar equipos desde archivos
# y buscar un equipo específico por nombre.
from utilidades.cargador import cargar_equipos, buscar_equipo

# Función que simula todos los partidos de un grupo
# y devuelve la tabla final ordenada.
from simulacion.grupos import simular_grupo

# Función que obtiene los equipos clasificados
# (primeros y segundos lugares de cada grupo).
from simulacion.clasificacion import obtener_clasificados


# Mensaje de inicio del programa.
print("===== SIMULADOR MUNDIAL 2026 =====")

# Obtiene los equipos desde la API y genera
# el archivo correspondiente.
obtener_equipos()

# Obtiene la distribución de grupos desde la API
# y genera el archivo grupos.json.
obtener_grupos()

# Carga todos los equipos almacenados localmente.
equipos = cargar_equipos()

# Diccionario donde se guardarán las tablas finales
# de cada grupo después de la simulación.
resultados_grupos = {}


# Recorre cada grupo cargado.
#
# nombre_grupo -> A, B, C, etc.
# lista_equipos -> equipos pertenecientes al grupo.
for nombre_grupo, lista_equipos in equipos.items():
    print(f"\n=== Grupo {nombre_grupo} ===")

    # Simula todos los partidos del grupo.
    tabla = simular_grupo(lista_equipos)

    # Guarda la tabla final del grupo.
    resultados_grupos[nombre_grupo] = tabla

    # Muestra en consola la clasificación final
    # del grupo simulado.
    for equipo in tabla:
        print(equipo)

# ---------------------------------------------------
# CARGA DE GRUPOS BASE DESDE EL ARCHIVO JSON
# ---------------------------------------------------
#
# Esta sección sirve para recorrer nuevamente los grupos
# definidos en grupos.json y verificar que todos los equipos
# existan correctamente dentro de los datos cargados.
#
# Funciona como una validación de integridad de datos.
#
with open("datos/grupos.json", "r", encoding="utf-8") as archivo:
    grupos = json.load(archivo)

# Recorre cada grupo definido en el archivo.
for letra, nombres in grupos.items():

    print(f"\n\n########## GRUPO {letra} ##########")

    # Lista temporal para almacenar los equipos
    # encontrados en este grupo.
    grupo = []

    # Recorre los nombres de los equipos.
    for nombre in nombres:

        # Busca el equipo dentro de los datos cargados.
        equipo = buscar_equipo(nombre, equipos)

        # Si no existe, muestra una advertencia.
        if equipo is None:
            print("NO ENCONTRADO:", nombre)
        # Si existe, lo agrega al grupo.
        else:
            grupo.append(equipo)


# ---------------------------------------------------
# OBTENER CLASIFICADOS
# ---------------------------------------------------
#
# Se seleccionan los primeros y segundos lugares
# de cada grupo según las tablas generadas.
#
clasificados = obtener_clasificados(resultados_grupos)


# ---------------------------------------------------
# MOSTRAR CLASIFICADOS EN CONSOLA
# ---------------------------------------------------
print("\n\n===== CLASIFICADOS =====")

# Encabezado de la tabla.
print(f"{'EQUIPO':25} {'PTS':>5} {'GF':>5}")

# Línea decorativa.
print("-" * 40)

# Muestra cada equipo clasificado.
for equipo in clasificados:
    print(equipo)