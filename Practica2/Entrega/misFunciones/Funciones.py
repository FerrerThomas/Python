
def buscarGoleador(datosJugadores):
    goleador = max(datosJugadores, key=lambda jugador: datosJugadores[jugador]['Goles a favor'])
    maxGoles = datosJugadores[goleador]['Goles a favor']
    return goleador,maxGoles

def crearEstructura(names, goals,goals_avoided,assists):
    datosJugadores= {}
    nombres = names.replace(',','').split()
    for i in range(len(nombres)):
        datos = {'Goles a favor': goals[i],'Goles evitados': goals_avoided[i],'Asistencias': assists[i]}
        datosJugadores[nombres[i]] = datos
    return datosJugadores


def calcularPromedioEquipo(datosJugadores,partidos):
    goles=0
    for datos in datosJugadores.values():
        goles += datos['Goles a favor']
    promedio = goles/partidos
    return promedio

def buscarInfluyente(datosJugadores):
    influyente=''
    puntos = 0.0
    for jugador, datos in datosJugadores.items():
        total = lambda  datos: (datos['Goles a favor'] * 1.5) + (datos['Goles evitados']* 1.25) + (datos['Asistencias'])
        if total(datos) > puntos:
            puntos = total(datos)
            influyente = jugador
    return influyente,puntos

calcularPromedioGoleador = lambda maxGoles,partidos: maxGoles/partidos
