# Importa la función encargada de simular un partido
# entre dos equipos y actualizar sus estadísticas.
from simulacion.partido import jugar_partido
# Actualmente random no se utiliza en este archivo,
# pero quedó importado posiblemente para pruebas
# o versiones anteriores de la simulación.
import random

# Función encargada de simular completamente un grupo.
#
# Recibe una lista de equipos pertenecientes a un grupo
# y devuelve la tabla final ordenada.
def simular_grupo(equipos):

    # Lista donde posteriormente se almacenará
    # la clasificación final del grupo.
    resultados = []


    # ---------------------------------------------------
    # REINICIO DE ESTADÍSTICAS
    # ---------------------------------------------------
    #
    # Antes de comenzar una nueva simulación es necesario
    # limpiar todas las estadísticas de los equipos para
    # evitar que acumulen datos de simulaciones anteriores.
    #
    for equipo in equipos:
        equipo.puntos = 0
        equipo.goles_favor = 0
        equipo.goles_contra = 0
        equipo.victorias = 0
        equipo.derrotas = 0
        equipo.empates = 0

    # ---------------------------------------------------
    # FASE DE GRUPOS
    # ---------------------------------------------------
    #
    # Se utiliza el formato "todos contra todos".
    #
    # Cada equipo juega una sola vez contra los demás
    # equipos de su grupo.
    #
    # Ejemplo para un grupo de 4 equipos:
    #
    # A vs B
    # A vs C
    # A vs D
    # B vs C
    # B vs D
    # C vs D
    #
    for i in range(len(equipos)):
        for j in range(i + 1, len(equipos)):
            # Simula el partido y actualiza automáticamente
            # puntos, goles y demás estadísticas.
            jugar_partido(equipos[i], equipos[j])

    # ---------------------------------------------------
    # CONSTRUCCIÓN DE LA TABLA FINAL
    # ---------------------------------------------------
    #
    # Convierte los objetos Equipo en diccionarios más
    # fáciles de mostrar en HTML o procesar posteriormente.
    #
    resultados = []

    for equipo in equipos:
        resultados.append({
            "nombre": equipo.nombre,
            "nivel": equipo.nivel,
            "puntos": equipo.puntos,
            "gf": equipo.goles_favor,
            "gc": equipo.goles_contra,
            "dg": equipo.goles_favor - equipo.goles_contra
        })

    # ---------------------------------------------------
    # ORDENAMIENTO DE LA TABLA
    # ---------------------------------------------------
    #
    # Criterios utilizados:
    #
    # 1. Mayor cantidad de puntos.
    # 2. Mejor diferencia de goles.
    # 3. Mayor cantidad de goles a favor.
    #
    # reverse=True permite ordenar de mayor a menor.
    #
    resultados.sort(
             key=lambda x: (x["puntos"], x["dg"], x["gf"]),
            reverse=True
        )

    # Devuelve la tabla final ya ordenada.
    return resultados