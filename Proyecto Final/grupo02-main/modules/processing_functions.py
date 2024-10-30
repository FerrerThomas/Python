import csv
import re

TYPES_OF_CONECTIVITIES=["ADSL", "CABLEMODEM", "DIALUP", "FIBRAOPTICA", "SATELITAL", "WIRELESS", "TELEFONIAFIJA", "3G", "4G"]
'''Contiene variables de tipos de conectividad'''

def define_size(num):

    """
    Retorna una cadena string segun el tamaño de la superficie del lago.
    args:
        num (int) : Tamaño de la superficie del lago.
     returns
        string.
    """

    if (num <= 17):
        return 'chico'
    elif (num > 17 and num <= 59):
            return 'medio'
    else:
        return 'grande'
        
def calculate_coordinate(coordinate):

    """
    Retorna la coordenada en formato de grados decimales (GD).
    args:
        coordinate (string) : Cadena de caracteres que representa una coordenada (longitud o latitud).
     returns
        float.
    """

    numbers = re.findall(r'\d+', coordinate)
    return int (numbers[0]) + (int(numbers[1]) / 60) + (int(numbers[2]) / 3600)

def processing_3(reader_path, writer_path):

    """
    Recorre el archivo original de lagos mientras crea uno nuevo modificado agregando 3 columnas ("Sup Tamaño","latitud","longitud")
    y los valores que rellenan dichas columnas.
    args:
        reader_path (string) : Ruta del archivo de lagos original.
        writer_path (string) : Ruta del archivo de lagos modificado.
    """

    # Apertura punto 1 {

    with (
            reader_path.open(mode='r', encoding='utf-8') as file_r,
            writer_path.open(mode='w', encoding='utf-8', newline='') as file_w
        ):
        reader = csv.reader (file_r)
        writer = csv.writer (file_w)

    # } Cierre punto 1
    # Apertura punto 2 { 

        SUPERFICIE = 2
        COORDENADAS = 5

    # } Cierre punto 2
    # Apertura punto 3 {

        header = next (reader)
        header.append('Sup Tamaño')
        header.append('Latitud')
        header.append('Longitud')
        writer.writerow (header)

    # } Cierre punto 3
    # Apertura punto 4 {

        for line in reader:
            num = int (line[SUPERFICIE])
            coord = line[COORDENADAS].split(' ')
            line.append(define_size(num))
            line.append(calculate_coordinate(coord[0]))
            line.append(calculate_coordinate(coord[1]))
            writer.writerow (line)

    # } Cierre punto 4 y fin del procesamiento.
        

def load_headers(headers):
    """
    Carga dos nuevos datos a los indices

    args:
        headers (list): lista de con los indices del archivo
    """
    headers.append('elevation_name') 
    headers.append('prov_name')
    return headers

def calculate_height(height):
    """
    Compara el dato recibido y retorna x resultado segun en que sector este dicho dato

    args:
        height (int): altura a compar
    """
    if (not height):
        return 'Sin Datos'
    height = int(height)
    if (height <= 131):
        return 'bajo'
    elif (131 < height <= 903):
        return 'medio'
    else:
        return 'altos'

def search_province(municipality,citys):
    """
    Compara dos datos, si son iguales retorna la provincia de la ciudad, sino recortan que no se la encontro

    args:
        municipality(string): municipalidad del aeropuerto
        citys(list): lista de ciudades con tus respectivos datos
    """
    end = False
    for city in citys[1:]:
        if municipality.lower() == city[0].lower():  
            province = city[5]  
            end = True
            return province
    if not end:
        return 'No encontrada'

def processing_1(airports_original,citys_original,airports_modified): 
    """
    Procesa el archivo original de aeropuertos y realiza los cambios necesarios utilizando datos ingresados
    por teclado, comparando en otro archivo (ciudades) y guarda la informacion modificada en el nuevo archivo

    args:
        airports_original(string): ruta del archivo original de aeropuertos
        citys_original(string): ruta del archivo original de ciudades
        airports_modified(string): ruta del nuevo archivo modificado de aeropuertos
    """
    with (airports_original.open(mode='r', encoding='utf 8') as read_airports,
          citys_original.open(mode='r', encoding='utf 8') as read_citys, 
          airports_modified.open(mode='w', encoding='utf 8',newline='') as wrile_new_airports): 
        reader_airports = csv.reader(read_airports) 
        reader_citys = csv.reader(read_citys)  
        writer = csv.writer(wrile_new_airports) 

        citys = []
        for i in reader_citys:
            citys.append(i)

        headers = load_headers(next(reader_airports)) 
        writer.writerow(headers) 
        
        for airports in reader_airports: 
            height = (airports[6]) 
            municipality = airports[13]
            provincia = search_province(municipality,citys)
            dato_height = calculate_height(height) 
            airports.append(dato_height) 
            airports.append(provincia)
            writer.writerow(airports) 

def conectivity (line):
        '''
         Determina si una línea tiene conectividad en alguna de las categorías especificadas.

        Recibe:
        - line: Diccionario que representa una línea de datos del archivo CSV original.

        Retorna:
        - "SI" si alguna columna tiene un valor diferente de "--", o "NO" de lo contrario.
        '''
        return "SI" if any(line[key].strip() != "--" for key in TYPES_OF_CONECTIVITIES) else "NO"

def change (line):
        '''
        Reemplaza los valores "--" por "NO" en todas las columnas de una línea.

        Recibe:
        - line: Un diccionario que representa una línea de datos del archivo CSV original.

        Retorna:
        - Una versión modificada de la línea con los valores "--" reemplazados por "NO".
        '''
        for key in line:
                if line[key].strip() == "--":
                        line[key]="NO"
        return line               

def processing_2(read_dataset,write_dataset):
        '''
        Toma un archivo CSV y genera un nuevo archivo CSV modificado y con una columna adicional ("posee_conectividad").
        
        Recibe:
        - read_dataset: El Pathlib con la ruta del archivo de entrada CSV.
        - write_dataset: El Pathlib con la ruta del archivo de salida CSV.
        '''
        with (
                read_dataset.open (mode = "r", encoding = "utf-8") as read_file,\
                write_dataset.open (mode = "w", encoding = "utf-8", newline='') as write_file
                ):

                reader = csv.DictReader(read_file)
                writer = csv.DictWriter(write_file, fieldnames=reader.fieldnames + ["posee_conectividad"])

                writer.writeheader()

                for line in reader:
                        line["posee_conectividad"] = conectivity(line)
                        line = change (line)
                   
                        writer.writerow(line)

def replace_simbols(line):
    """
    Reemplaza los simbolos /// y - de la fila del archivo recibida
    por 0
    args:
        line (list): Lista con una fila del archivo
    """
    return [0 if elem in ['///', '-'] else elem for elem in line]

def calc_percentage(total_population, total_homeless):
    """
    Calcula el porcentaje de poblacion en situacion de calle
    args:
        total_population (int): Cantidad total de poblacion
        total_homeless (int): Cantidad de poblacion en situacion de calle
    """
    if (total_homeless == 0):
        return 0
    return ((total_homeless / total_population) * 100)

def processing_4(original_path,new_path):
    """
    Procesa el archivo original realizando los cambios solicitados
    y guarda la informacion modificada dentro del nuevo archivo
    args:
        original_path (string): Ruta del archivo original
        new_path (string): Ruta del nuevo archivo
    """
    POPULATION_POS = 1 # Constante - Posicion de la columna Poblacion Total
    HOMELESS_POS = 4 # Constante - Posicion de la columna Poblacion en Situacion de Calle
    
    with (
        original_path.open(mode = 'r', encoding='utf-8') as file_r,
        new_path.open(mode = 'w', encoding='utf-8', newline='') as file_w
    ):
        reader = csv.reader(file_r)
        writer = csv.writer(file_w)
        
        header = next(reader)
        header.append('Porcentaje en Situacion de Calle')
        writer.writerow(header)
        for line in reader:
            line = replace_simbols(line)

            percentage = calc_percentage(int(line[POPULATION_POS]),int(line[HOMELESS_POS]))
            line.append(f"{percentage:.2f}%")

            writer.writerow(line)
        
