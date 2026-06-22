# Función que obtiene automáticamente los clasificados directos.
# De cada grupo pasan:
# - Primer lugar
# - Segundo lugar
def obtener_clasificados(resultados_grupos):

    # Lista donde se almacenarán todos los equipos clasificados.
    clasificados = []


    # Recorre cada grupo y su tabla final.
    # Ejemplo:
    # grupo = "A"
    # tabla = [equipo1, equipo2, equipo3, equipo4]
    for grupo, tabla in resultados_grupos.items():
        # Agrega el primer lugar del grupo.
        clasificados.append(tabla[0])  # primero
        # Agrega el segundo lugar del grupo.
        clasificados.append(tabla[1])  # segundo

    # Retorna los 24 clasificados directos
    # (2 equipos por cada uno de los 12 grupos).
    return clasificados

# Función que determina los mejores terceros lugares
# de todos los grupos del Mundial.
def mejores_terceros(resultados_grupos):

    # Lista donde se almacenarán los terceros lugares
    # de los 12 grupos.
    terceros = []

    # Recorre todos los grupos.
    for letra, tabla in resultados_grupos.items():
        # El tercer lugar siempre se encuentra
        # en la posición 2 de la tabla ordenada.
        terceros.append(tabla[2])

    #1. Puntos
    # 2. Diferencia de goles (dg)
    # 3. Goles a favor (gf)
    #
    # reverse=True permite ordenar de mayor a menor.
    terceros.sort(
        key=lambda x: (x["puntos"], x["dg"], x["gf"]),
        reverse=True
    )

    # Devuelve únicamente los 8 mejores terceros,
    # que completan los 32 clasificados a la fase eliminatoria.
    return terceros[:8]