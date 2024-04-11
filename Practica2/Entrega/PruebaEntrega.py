import misFunciones

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, 
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, 
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

#/_______________________________________________________________

# limpio las comas y divido por nombre
nombres = names.replace(',','').split()
# creo un diccionario (key: nombre | dato: estadisticas de dicho nombre)
datosJugadores= {}

# cargo los datos en el diccionario :p
for i in range(len(nombres)):
    datos = {'Goles a favor': goals[i],'Goles evitados': goals_avoided[i],'Asistencias': assists[i]}
    datosJugadores[nombres[i]] = datos

# chequeo que se cargo correctamente 
print(datosJugadores)

print() # separo cosas solamente :p
#/_______________________________________________________________

goleador,maxGoles = misFunciones.buscarGoleador(datosJugadores)

print(f'La persona con mas goles fue {goleador} con {maxGoles} goles !!')

print() # separo cosas solamente :p
#/_______________________________________________________________

influyente,puntos = misFunciones.buscarInfluyente(datosJugadores)

print(f'La persona mas influyente fue {influyente} con {puntos} pts')

print() # separo cosas solamente :p
#/_______________________________________________________________

partidos=25 
promedio = misFunciones.calcularPromedioEquipo(datosJugadores,partidos)

print(f'El promedio de goles del equipo fue {promedio}')

print() # separo cosas solamente :p
#/_______________________________________________________________

print(f'El promedio del goleador ({goleador}) fue de {misFunciones.calcularPromedioGoleador(maxGoles,partidos)} goles por partido')

print() # separo cosas solamente :p