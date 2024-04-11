
def buscarGoleador(datosJugadores):
    goleador=''
    maxGoles=0
    for jugador,datos in datosJugadores.items(): #key: juagdor   datos: datos 
        if (datos['Goles a favor'])> maxGoles:
            maxGoles= datos['Goles a favor']
            goleador = jugador
    return goleador,maxGoles

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