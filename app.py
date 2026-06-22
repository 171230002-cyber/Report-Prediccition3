from flask import Flask, render_template

# Funciones para cargar los equipos desde el archivo JSON
# y buscar un equipo específico por nombre.
from utilidades.cargador import cargar_equipos, buscar_equipo

# Función encargada de simular todos los partidos de un grupo.
from simulacion.grupos import simular_grupo

# Funciones para obtener los equipos clasificados
# y calcular los mejores terceros lugares.
from simulacion.clasificacion import (obtener_clasificados,mejores_terceros)
import json

# Creación de la aplicación Flask.
app = Flask(__name__)

# Ruta principal del sitio.
# Muestra la página inicial con el botón para iniciar la simulación.
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta encargada de ejecutar toda la simulación del Mundial.
# Se activa cuando el usuario presiona el botón "Simular".
@app.route("/simular", methods=["POST"])
def simular():

    # Variable global donde se almacenarán las tablas finales
    # de cada grupo para enviarlas posteriormente al HTML.
    global resultados_grupos
    # Carga todos los equipos registrados en equipos.json.
    equipos = cargar_equipos()

    # Carga la distribución de los grupos desde grupos.json.
    with open("datos/grupos.json", "r", encoding="utf-8") as archivo:
        grupos = json.load(archivo)

    # Diccionario donde se guardará la tabla final de cada grupo.
    resultados_grupos = {}

    # Lista auxiliar para almacenar todos los equipos simulados.
    clasificados_totales = []

    # Recorre cada grupo (A, B, C, etc.)
    for letra, nombres in grupos.items():

        # Lista donde se guardarán los objetos completos
        # de los equipos pertenecientes al grupo actual.
        grupo = []

        # Recorre cada nombre de equipo del grupo.
        for nombre in nombres:

            # Busca la información completa del equipo
            equipo = buscar_equipo(nombre, equipos)

            # Si el equipo existe, se agrega al grupo.
            if equipo is not None:
                grupo.append(equipo)

        # Simula todos los partidos del grupo y genera la tabla final.
        tabla = simular_grupo(grupo)

        # Mensajes de control para verificar que la simulación
        # se realizó correctamente en la consola.
        print(f"\nGRUPO {letra}")
        print(f"Cantidad de equipos: {len(tabla)}")

        for e in tabla:
            print(e["nombre"])

        # Guarda la tabla final del grupo utilizando
        # la letra del grupo como clave.
        resultados_grupos[letra] = tabla
        # Agrega los equipos del grupo a la lista general.
        clasificados_totales.extend(tabla)

    # Obtiene automáticamente los primeros y segundos lugares
    # de cada grupo.
    clasificados = obtener_clasificados(resultados_grupos)

    # Calcula los 8 mejores terceros lugares de los 12 grupos.
    mejores_terceros_lista = mejores_terceros(resultados_grupos)

    # Agrega los mejores terceros a la lista de clasificados.
    clasificados.extend(mejores_terceros_lista)

    # Envía toda la información al archivo resultado.html:
    # - clasificados: 32 equipos que avanzan
    # - grupos: tablas completas de los 12 grupos
    # - mejores_terceros: lista de los 8 mejores terceros
    return render_template(
        "resultado.html",
        clasificados=clasificados,
        grupos = resultados_grupos,
        mejores_terceros=mejores_terceros_lista
    )

# Punto de inicio de la aplicación.
# debug=True permite que Flask recargue automáticamente
# los cambios realizados durante el desarrollo.
if __name__ == "__main__":
    app.run(debug=True)