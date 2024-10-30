import csv
from unidecode import unidecode
from tabulate import tabulate

TYPE = 2

def inform_airports_by_province (province, airport_data):

    """
    Imprime los nombres de aeropuertos de la provincia 'province'
    args:
        province (string) : Una provincia de la lista de provincias con mayor/menor poblacion que la solicitada por el usuario.
        airport_data (list) : Es la lista de aeropuertos en la cual se buscan e informan los que se encuentren en la provincia 'province'
    """

    print ('')
    airport_results = map(lambda line: f'Aeropuerto {line["name"]} de {line["prov_name"]}', filter(lambda line: unidecode(line["prov_name"].lower()) == province, airport_data))
    for item in airport_results:
        print(item)
    print ('')

def inform_lakes_by_province (province, lake_data):

    """
    Imprime los nombres de lagos de la provincia 'province'
    args:
        province (string) : Una provincia de la lista de provincias con mayor/menor poblacion que la solicitada por el usuario.
        lake_data (list) : Es la lista de lagos en la cual se buscan e informan los que se encuentren en la provincia 'province'
    """

    print ('')
    lake_results = map(lambda line: f'{line["Nombre"]} de {line["Ubicación"]}', filter(lambda line: unidecode(line["Ubicación"].lower()) == province, lake_data))
    for item in lake_results:
        print(item)
    print ('')

def inform_connectivity_by_province (province, connectivity_data, types_of_conectivities):

    """
    Imprime los tipos de conectividad de la provincia 'province'
    args:
        province (string) : Una provincia de la lista de provincias con mayor/menor poblacion que la solicitada por el usuario.
        connectivity_data (list) : Es la lista de conectividad en la cual se busca e informa la conectividad de la provincia 'province'
        types_of_conectivities (list) : Es una lista con los tipos de conectividades posibles.
    """

    connectivity_by_province = {}
    for line in connectivity_data:
        if (unidecode(line["Provincia"].lower()) == province):
            for connectivity in types_of_conectivities:  # Iterar a través de tipos de conectividad
                if connectivity not in connectivity_by_province or line[connectivity] == "SI":
                    connectivity_by_province[connectivity] = line[connectivity]
    print (f'Tipos de conectividad en {province}: {connectivity_by_province}')
    print ('')


def querie_4 (airport_path, lake_path, connectivity_path, census_path, types_of_conectivities):

    """
    Recorre el archivo del censo 2022 buscando las provincias con mayor/menor poblacion que la solicitada por el usuario, luego recorre los archivos
    de aeropuertos lagos y conectividad e informa lo requerido.
    args:
        airport_path (string) : Ruta del archivo de aeropuertos modificado.
        lake_path (string) : Ruta del archivo de lagos modificado.
        connectivity_path (string) : Ruta del archivo de conectividad modificado.
        census_path (string) : Ruta del archivo de censo modificado.
        types_of_conectivities (list) : Es una lista con los tipos de conectividades posibles.
    """
    population_to_search = int (input ("Ingrese la cantidad de poblacion que desea comparar: "))
    higher_or_lower = input ("Ingrese - mayor - , si desea buscar los mayores a la cantidad ingresada o - menor - si desea buscar los menores: ")
    while (higher_or_lower != "mayor" and higher_or_lower != "menor"):
        higher_or_lower = input ("ERROR --> Ingrese - mayor - , si desea buscar los mayores a la cantidad ingresada o - menor - si desea buscar los menores: ")
    # Apertura punto 1 {

    with (
        airport_path.open(mode='r', encoding='utf-8') as file_r1,
        lake_path.open(mode='r', encoding='utf-8') as file_r2,
        connectivity_path.open(mode='r', encoding='utf-8') as file_r3,
        census_path.open(mode='r', encoding='utf-8') as file_r4
    ):
        airport_reader = csv.DictReader(file_r1)
        airport_data = list(airport_reader)
        lake_reader = csv.DictReader(file_r2)
        lake_data = list(lake_reader)
        connectivity_reader = csv.DictReader(file_r3)
        connectivity_data = list(connectivity_reader)
        header = file_r4.readline().strip().split(",")      # Guardo el header del archivo.
        next (file_r4)                                      # Salteo la linea "Total del país" ya que solo me interesa el total de las provincias.
        census_reader = csv.DictReader(file_r4,fieldnames=header)


        # } Cierre punto 1 
        # Apertura punto 2 {

        filtered_provinces = [line["Jurisdicción"].strip().lower() for line in census_reader
                            if (higher_or_lower == "mayor" and int(line["Total de población"]) > population_to_search) or
                            (higher_or_lower == "menor" and int(line["Total de población"]) < population_to_search)]
            
        # } Cierre punto 2
        # Apertura punto 3 {
        
        for province in filtered_provinces:

            print (f" ---- Aeropuertos de {province} que poseen {higher_or_lower} poblacion a {population_to_search} ---- ")
            inform_airports_by_province (province, airport_data)

            print (f" ---- Lagos de {province} que poseen {higher_or_lower} poblacion a {population_to_search} ---- ")
            inform_lakes_by_province (province, lake_data)

            inform_connectivity_by_province (province, connectivity_data, types_of_conectivities)
                   
        # } Cierre punto 3




def querie_6(lake_path):

    """
    Imprime los lagos del tamaño ingresado por el usuario.
    args:
        lake_mod_path (string) : Ruta del archivo de lagos modificado.
    """
    size = input ('Ingrese el tamaño (chico, medio, grande) de los lagos que desea informar: ')
    while (size != "chico" and size != "medio" and size != "grande"):
        size = input ('ERROR --> Ingrese el tamaño (chico, medio, grande) de los lagos que desea informar: ')
    # Apertura punto 1 {

    with (
            lake_path.open(mode='r', encoding='utf-8') as file_r
        ):
        reader = csv.reader(file_r)

    # } Cierre punto 1
    # Apertura punto 2 {
        
        NOMBRE = 0
        UBICACION = 1
        SUP_TAMAÑO = 6

    # } Cierre punto 2
    # Apertura punto 3 {

        for line in reader:
            if (line[SUP_TAMAÑO] == size):
                print (f'Nombre: {line[NOMBRE]} | Ubicación: {line[UBICACION]} | Tamaño: {line[SUP_TAMAÑO]}')

    # } Cierre punto 3 y fin de la funcion.

#____________________________________________________________________________________________________

def querie_1(address):
    """
    Crea una lista con los aeropuertos, filtra solo los tipos y los muestra en pantalla

    args:
        address(address): direccion del archivo de aeropuertos a procesar
    """
    with open(address, mode='r', encoding='utf-8') as archive:
        airports = csv.reader(archive)
        next(airports) 
        list_zip = list(zip(*airports)) 
        types_airports = set(list_zip[TYPE])
    
    print('| Tipos de airports |')
    for one_type in types_airports:
        print(f'•{one_type}')

#____________________________________________________________________________________________________

def show_airports(address,selected_option): 
    """
    Recibe un string, e imprime los aeropuertos que con una elavation_name igual a dicho string

    args:
        address(address): direccion del archivo de aeropuertos a procesar
        selected_option(string): opcion elegida por el usuario (bajo,medio,altos) a filtrar
    """
    with open(address, mode='r', encoding='utf-8') as archive:
        airports = csv.DictReader(archive)
        print_airports(filter(lambda airport: airport['elevation_name'] == selected_option, airports))


def querie_2(address):
    """
    Menu de opciones, segun la opcion elegida se filtra y se muestran los aeropuertos con esa caracteristica

    args:
        address(address): direccion del archivo de aeropuertos a procesar
    """
    end=False
    while not end:
        selected_option = (input("""Ingresar que elevacion quiere buscar: 
                          bajo: menos o igual a 131 ft
                          medio: mayor a 131 pero menos o igual a 903 ft
                          altos: mayor a 903 ft
                        
                          end: terminar programa
                Opcion:""")).lower()
        if selected_option == 'fin':
            end=True
            print('| Impresión terminada |')
        elif selected_option in ['bajo','medio','altos']:
            print(f'Mostrando airport con height {selected_option}')
            show_airports(address,selected_option)
        else:
            print('| ERROR | Opcion invalida... Ingrese de nuevo')

#____________________________________________________________________________________________________

def search_minor_major(address,height):
    """
    Recibe una altura y filtra en dos listas diferentes los aeropuertos que tengan menor y mayor altura  a la recibida

    args:
        address(address): direccion del archivo de aeropuertos a procesar
        height(int): altura a filtrar ingresada por el usuario
    """
    with open(address, mode='r', encoding='utf-8') as archive:
        airports = csv.DictReader(archive)
        airportss = list(airports)
        major = list(filter(lambda airport: int(airport['elevation_ft'] or 0) > height, airportss ))
        minor = list(filter(lambda airport: int(airport['elevation_ft'] or 0) < height, airportss ))
        return major,minor


def print_airports(airports):
    """
    Recibe e imprime con formato de tabla

    args:
        airports(list): lista de aeropuertos a mostrar
    """
    print(tabulate(airports, headers='keys',tablefmt='psql'))


def querie_3(address):
    """
    Menu de opciones, segun al opcion busca, filtra e imprime mayores o menos a una altura ingresada

    args:
        address(address): direccion del archivo de aeropuertos a procesar
    """
    end=False
    while not end:
        try:
            height_elegida = int(input("Ingresar la elevacion con la cual quiere trabajar:"))
            while not end:
                selected_option = input(f"""Ingresar que airports quiere mostrar: 
                                1: airports con elevacion menor a {height_elegida}
                                2: airports con elevacion mayor a {height_elegida}
                                3: airports con elevacion menor y mayor a {height_elegida}
                        Opcion:""")
                if selected_option in ['1','2','3']:
                    end=True
                    major,minor = search_minor_major(address,height_elegida)
                    if selected_option == '1':
                        print(f'| airports con elevacion MENOR a {height_elegida} |')
                        print_airports(minor)
                    elif selected_option == '2':
                        print(f'| airports con elevacion MAYOR a {height_elegida} |')
                        print_airports(major)
                    else:
                        print(f'| airports con elevacion MENOR a {height_elegida} |')
                        print_airports(minor)
                        print(f'| airports con elevacion MAYOR a {height_elegida} |')
                        print_airports(major)
                else:
                    print('Opcion no valida, ingrese de nuevo')
        except ValueError:
            print('No ingreso un valor valido (numerico)')
    print('| Impresión terminada |')

def inform_airport(airport):
    """
    Imprime por pantalla la informacion de un aeropuerto
    args:
        airport (dict): Diccionario con informacion del aeropuerto.
    """
    print("-"*40)
    print(f"Aeropuerto {airport['name']}: ")
    print(f"    - Tipo: {airport['type']} ")
    print(f"    - Continente: {airport['continent']} ")
    print(f"    - Pais: {airport['country_name']} ")
    print(f"    - Provincia: {airport['region_name']} ")
    print(f"    - Ciudad: {airport['municipality']} ")
    print("-"*40)


def querie_5(AIRPORTS_PATH,CITYS_PATH):
    """
    Filtra las capitales de cada provincia y obtiene los aeropuertos de cada
    una de estas.
    args:
        AIRPORTS_PATH (string): Ruta del archivo de aeropuertos.
        CITYS_PATH (string): Ruta del archivo de ciudades.
    """
    with (
        AIRPORTS_PATH.open(mode = 'r', encoding='utf-8') as a_r,
        CITYS_PATH.open(mode = 'r', encoding='utf-8') as c_r
    ):
        airports_reader = csv.DictReader(a_r)
        citys_reader = csv.DictReader(c_r)

        capitals = [city["city"] for city in citys_reader if ((city["capital"] == "admin") or (city["capital"] == "primary"))]
        filtered_airports = list(filter(lambda d: d.get('municipality') in capitals, airports_reader))

        print("Se muestran los aeropuertos de las capitales: ")
        for airport in filtered_airports:
            inform_airport(airport)


def inform_jurisdiction(jurisdiction):
    """
    Imprime por pantalla la informacion de una jurisdiccion.
    args:
        jurisdiction (dict): Diccionario con informacion de una jurisdiccion.
    """
    print("-"*30)
    print(f"Jurisdiccion :{jurisdiction['Jurisdicción']}")
    print(f"    - Porcentaje de poblacion en situacion de calle: {jurisdiction['Porcentaje en Situacion de Calle']}")
    print("-"*30)

def querie_7(POPULATION_PATH):
    """
    Ordena el archivo de poblaciones por porcentaje de poblacion en situacion de calle
    de mayor a menor e imprime los primeros 5.
    args:
        POPULATION_PATH (string): Diccionario con informacion de una jurisdiccion.
    """
    with(
        POPULATION_PATH.open(mode = "r",encoding="utf-8") as p_r
    ):
        population_reader = csv.DictReader(p_r)
        next(population_reader)

        ordered_list = sorted(population_reader, key=lambda x: x['Porcentaje en Situacion de Calle'], reverse=True)

        print("Se imprimiran las jurisdicciones con mayor cantidad de poblacion en situacion de calle.: ")
        for jurisdiction in ordered_list[:5]:
            inform_jurisdiction(jurisdiction)


def inform_max_breach(population_breachs):
    """
    Imprime por pantalla la informacion de la jurisdiccion con mayor brecha poblacional
    args:
        population_breachs (dict): diccionario con jurisdicciones y sus brechas.
    """
    max_breach = max(population_breachs,key = population_breachs.get)
    print()
    print("-"*40)
    print("Jurisdiccion con mayor brecha de poblacion segun el sexo:")
    print(f"    - Juridiccion: {max_breach}")
    print(f"    - Brecha: {population_breachs[max_breach]}")
    print("-"*40)


def querie_8(POPULATION_PATH):
    """
    Genera un diccionario con cada jurisdiccion y su breacha poblacional entre hombres y mujeres.
    args:
        POPULATION_PATH (dict): diccionario con jurisdicciones y sus brechas.
    """
    with(
        POPULATION_PATH.open(mode = "r",encoding="utf-8") as population_reader
    ):
        p_r = csv.DictReader(population_reader)
        next(p_r)

        population_breachs = {j['Jurisdicción']: abs(int(j['Varones Total de población']) - int(j['Mujeres Total de población'])) for j in p_r}
        inform_max_breach(population_breachs)

#____________________________________________________________________________________________________

def check_connectivity (dic,connectivity):
    for line in connectivity:
        if dic["Capital"].lower() in line["Localidad"].lower() and unidecode(dic["Provincia"].lower()) in line["Provincia"].lower():
            return line["posee_conectividad"]
    return "Conectividad desconocida"


def querie_9 (connectivities):
    '''
    Imprime los tipos de conectividades que se encuentran en la lista.

    Recibe:
    - connectivities: Lista que contiene los tipos de conectividad.
    '''
    print ("Los tipos de conectividades son:",", ".join(connectivities ))


def querie_10 (connectivity_dataset, types):
    '''
    Identifica la cantidad de localidades con cada tipo de conectividad del dataset y las imprime.

    Recibe:
    - types: Lista que contiene los tipos de conectividad.
    - connectivity_dataset: Dataset que contiene los datos de conectividad en Argentina.
    '''
    with connectivity_dataset.open (mode = "r", encoding = "utf-8", newline='') as read_dataset:
        
        connectivity = csv.DictReader(read_dataset)
    
        connectivities = dict.fromkeys(types, 0)
        
        for line in connectivity:
            for type in types:
                if line[type] == "SI":
                    connectivities[type] += 1
    
    table_data = [[key, value] for key, value in connectivities.items()]
    print(tabulate(table_data, headers=['Tipo de conectividad', 'Cantidad'], tablefmt='psql', stralign='center'))


def querie_11 (connectivity_dataset):
    """
    Identifica las provincias del dataset de conectividad que tienen fibra óptica en todas sus ciudades y las imprime.

    Recibe: 
    connectivity_dataset: Dataset que contiene los datos de conectividad en Argentina.
    """
    provinces = {}

    with connectivity_dataset.open (mode = "r", encoding = "utf-8", newline='') as read_dataset:
        connectivity = csv.DictReader(read_dataset)

        for line in connectivity:
            province = line['Provincia']
            city = line['Localidad']
            fiber_optic = line['FIBRAOPTICA']
            
            if province not in provinces:
                provinces[province] = {}
            
            provinces[province][city] = fiber_optic
        
        print ("Las provincias que tienen fibra óptica en todas sus ciudades son:")
        for province, cities in provinces.items():
            if all(fibra_optica == 'SI' for fibra_optica in cities.values()):
                print(province)


def querie_12 (ar_dataset, connectivity_dataset):
    """
    Identifica si las capitales de las provincias poseen conectividad y las imprime.

    Recibe: 
    ar_dataset: Dataset que contiene la composición de cada provincia de Argentina con el listado de ciudades de cada una.
    connectivity_dataset: Dataset que contiene los datos de conectividad en Argentina.
    """
    ar = []
    with ar_dataset.open (mode = "r", encoding = "utf-8", newline='') as read_dataset:
        ar_dat = csv.DictReader(read_dataset)

        for line in ar_dat:
            if line["capital"] == "admin":
                ar.append({"Provincia": line["admin_name"].split(",")[0], "Capital": line["city"]})

    with connectivity_dataset.open (mode = "r", encoding = "utf-8", newline='') as read_dataset:
        connectivity = list(csv.DictReader(read_dataset))

    for dic in ar:
        dic["Posee Conectividad"] = check_connectivity(dic,connectivity)

    headers = ar[0].keys()
    table_data = [[row[header] for header in headers] for row in ar]
    print(tabulate(table_data, headers=headers, tablefmt='psql', stralign='center'))
