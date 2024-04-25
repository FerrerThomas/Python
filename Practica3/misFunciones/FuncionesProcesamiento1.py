
def Procesamiento1(rutaAirports,rutaCitys,rutaCustom):
    
    import pathlib
    import csv

    def cargarNuevosIndices(indices):
        print(indices)  # como el next obtiene el siguiente elemento del lector osea le primero
        indices.append('elevation_name') #agrego el nuevo dato
        indices.append('prov_name')
        print(indices)

    def calcularAltura(altura):
        if (not altura):
            return 'Sin Datos'
        altura = int(altura)
        if (altura <= 131):
            return 'bajo'
        elif (131 < altura <= 903):
            return 'medio'
        else:
            return 'alto'
    
    def buscarProvincia(municipalidad,ciudades):
        encontre = False
        for ciudad in ciudades[1:]:
            if municipalidad.lower() == ciudad[0].lower():  # Comparar e ignorando mayúsculas por si las dudas
                prov = ciudad[5]  # saco el nombre de la provincia 
                encontre = True
                return prov
        if not encontre:
            return 'No encontrada'

    readAirports = pathlib.Path(rutaAirports) # direcciono cada archivo
    writeAirports = pathlib.Path(rutaCustom)
    readCity = pathlib.Path(rutaCitys)
    with (readAirports.open(mode='r', encoding='utf 8') as archivoReadAirports,
          readCity.open(mode='r', encoding='utf 8') as archivoReadCitys, #abro cada uno con 
        writeAirports.open(mode='w', encoding='utf 8',newline='') as archivoWrile): #lectura y escritura
        readerAirports = csv.reader(archivoReadAirports) # readerAirports seria un lector y writer un escritor xd
        readerCitys = csv.reader(archivoReadCitys)  
        writer = csv.writer(archivoWrile) #creo una variable con el contenido
        
        ciudades = []
        for i in readerCitys:
            ciudades.append(i)
        print(ciudades)

        #estos contenidos quedaran en listas por lo tanto se la puede tratar como una lista de lista
        indices = cargarNuevosIndices(next(readerAirports)) # obtengo el primer elemento que serian los indices
        writer.writerow(indices) #escribo en el csv del garaje del drift
        
        for unAeropuerto in readerAirports: #que seria los aeropuertos xd
            altura = (unAeropuerto[6]) #saco la altura y la convierto en entera
            municipalidad = unAeropuerto[13]
            provincia = buscarProvincia(municipalidad,ciudades)
            newDato = calcularAltura(altura) # calculo
            unAeropuerto.append(newDato) #le agrego el dato al aeropuerto
            unAeropuerto.append(provincia)
            writer.writerow(unAeropuerto) #cargo el aeropuerto con el dato nuevo


def imprimirOpcion(rutaCustom):
    import csv
    
    def mostrarAeropueros(opcionElegida):   
        with open(rutaCustom, mode='r', encoding='utf-8') as archivo:
            garage = csv.DictreaderAirports(archivo)
            for aeropuerto in garage:
                if aeropuerto['elevation_name'] == opcionElegida:
                    print(aeropuerto)
    
    fin=False
    while not fin:
        opcionElegida = input("Ingrese una opción ('bajo', 'medio', 'alto') o 'fin' para salir: ")
        if opcionElegida == 'fin':
            fin=True
        elif opcionElegida in ['bajo','medio','alto']:
            print(f'Mostrando Aeropuerto con altura {opcionElegida}')
            mostrarAeropueros(opcionElegida)
        else:
            if fin:
                print('| Impresión terminada |')
            else:
                print('| ERROR | Opcion invalida... Ingrese de nuevo')

def imprimirOpcion2(rutaCustom):
    import csv 
    import pathlib

    def mostrarAeropueros2(opcionElegida,rutaCustom):
        Aeropuertos = pathlib.Path(rutaCustom)   
        with Aeropuertos.open(mode='r', encoding='utf-8') as archivo:
            garage = csv.DictreaderAirports(archivo)
            for aeropuerto in garage:
                if aeropuerto['elevation_name'] == opcionElegida:
                    print(aeropuerto)

    opciones = ['bajo','medio','alto']
    opcionElegida = input("""Ingresar que elevacion quiere buscar: \n
                          bajo: menos o igual a 131 ft
                          medio: mayor a 131 pero menos o igual a 903 ft
                          altos: mayor a 903 ft
                        
                          fin: terminar programa""")
    
    while opcionElegida != 'fin':
        if (opcionElegida in opciones):
            mostrarAeropueros2(opcionElegida,rutaCustom)
        else:
            print('| ERROR | Opcion invalida... Ingrese de nuevo')
        opcionElegida = input("""Ingresar que elevacion quiere buscar: 
                          bajo: menos o igual a 131 ft
                          medio: mayor a 131 pero menos o igual a 903 ft
                          altos: mayor a 903 ft
                        
                          fin: terminar programa""")
    print('| Impresión terminada |')


