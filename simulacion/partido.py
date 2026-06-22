import random

# Función encargada de simular un partido entre dos equipos.
#
# Recibe:
# - equipo1
# - equipo2
#
# Actualiza automáticamente:
# - puntos
# - goles a favor
# - goles en contra
# - victorias
# - derrotas
# - empates
#
# Además devuelve el marcador final.
def jugar_partido(equipo1, equipo2):

    # Calcula la diferencia de nivel entre ambos equipos.
    #
    # Si el resultado es positivo:
    # equipo1 es más fuerte.
    #
    # Si es negativo:
    # equipo2 es más fuerte.
    ventaja = equipo1.nivel - equipo2.nivel

    # Generación aleatoria de goles base.
    #
    # Cada equipo puede anotar entre 0 y 3 goles.
    goles1 = random.randint(0, 3)
    goles2 = random.randint(0, 3)

    # Se otorga una pequeña ventaja al equipo
    # con mejor nivel.
    #
    # Esto hace que los equipos fuertes tengan
    # mayores probabilidades de ganar.
    if ventaja > 0:
        goles1 += random.randint(0, 1)
    elif ventaja < 0:
        goles2 += random.randint(0, 1)


    # ---------------------------------------------------
    # INICIALIZACIÓN DE ESTADÍSTICAS
    # ---------------------------------------------------
    #
    # Verifica que ambos equipos tengan creados
    # los atributos necesarios.
    #
    # Esto evita errores si un equipo aún no tiene
    # estadísticas registradas.
    #
    for equipo in (equipo1, equipo2):

        if not hasattr(equipo, "goles_favor"):
            equipo.goles_favor = 0

        if not hasattr(equipo, "goles_contra"):
            equipo.goles_contra = 0

        if not hasattr(equipo, "puntos"):
            equipo.puntos = 0

        if not hasattr(equipo, "victorias"):
            equipo.victorias = 0

        if not hasattr(equipo, "derrotas"):
            equipo.derrotas = 0

        if not hasattr(equipo, "empates"):
            equipo.empates = 0

    # ---------------------------------------------------
    # ACTUALIZACIÓN DE GOLES
    # ---------------------------------------------------
    #
    # Se registran los goles anotados y recibidos
    # por ambos equipos.
    #
    equipo1.goles_favor += goles1
    equipo1.goles_contra += goles2

    equipo2.goles_favor += goles2
    equipo2.goles_contra += goles1

    # ---------------------------------------------------
    # ASIGNACIÓN DE PUNTOS
    # ---------------------------------------------------
    #
    # Victoria = 3 puntos
    # Empate = 1 punto
    # Derrota = 0 puntos
    #
    if goles1 > goles2:
        # Gana equipo1.
        equipo1.puntos += 3
        equipo1.victorias += 1
        equipo2.derrotas += 1

    elif goles2 > goles1:
        # Gana equipo2.
        equipo2.puntos += 3
        equipo2.victorias += 1
        equipo1.derrotas += 1

    else:
        # Ambos equipos empatan.
        equipo1.puntos += 1
        equipo2.puntos += 1

        equipo1.empates += 1
        equipo2.empates += 1

    # ---------------------------------------------------
    # MOSTRAR RESULTADO DEL PARTIDO
    # ---------------------------------------------------
    #
    # Ejemplo:
    #
    # México 2 - 1 Brasil
    #
    print(f"\n{equipo1.nombre} {goles1} - {goles2} {equipo2.nombre}")

    # Devuelve el marcador generado.
    return goles1, goles2
