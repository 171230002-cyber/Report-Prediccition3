# Clase que representa una selección nacional dentro
# del simulador del Mundial.
#
# Cada objeto Equipo almacena:
# - Información general del equipo.
# - Nivel de habilidad.
# - Estadísticas acumuladas durante la simulación.
class Equipo:

    # Constructor de la clase.
    #
    # Se ejecuta automáticamente cada vez que se crea
    # un nuevo objeto Equipo.
    #
    # Parámetros:
    # nombre  -> nombre de la selección.
    # ranking -> posición en el ranking FIFA.
    # nivel   -> valor utilizado para influir en los partidos.
    def __init__(self,nombre,ranking,nivel):

        # Información básica del equipo.
        self.nombre = nombre
        self.ranking = ranking
        self.nivel = nivel

        # ---------------------------------------------------
        # ESTADÍSTICAS DE COMPETENCIA
        # ---------------------------------------------------
        #
        # Estas variables se actualizan durante la simulación
        # de los partidos y la fase de grupos.
        #

        # Puntos acumulados.
        self.puntos = 0
        # Goles anotados.
        self.goles_favor = 0
        # Goles recibidos.
        self.goles_contra = 0

        # Cantidad de partidos ganados.
        self.victorias = 0
        # Cantidad de empates.
        self.empates = 0
        # Cantidad de derrotas.
        self.derrotas = 0

    # ---------------------------------------------------
    # DIFERENCIA DE GOLES
    # ---------------------------------------------------
    #
    # Property que calcula automáticamente la diferencia
    # de goles cuando se consulta.
    #
    # Fórmula:
    # GF - GC
    #
    # Ejemplo:
    # GF = 8
    # GC = 3
    #
    # diferencia = 5
    #
    @property
    def diferencia(self):
        return self.goles_favor - self.goles_contra