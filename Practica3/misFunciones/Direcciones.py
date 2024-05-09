import pathlib

AEROPUERTOS = pathlib.Path('Datasets','ar-airports.csv')
LAGOS = pathlib.Path('Datasets','lagos_arg.csv')
CITY = pathlib.Path('Datasets','ar.csv')
POBLACION = pathlib.Path('Datasets','c2022_tp_c_resumen_adaptado.csv')
CONECTIVIDAD = pathlib.Path('Datasets','Conectividad_Internet.csv')

def traerDireccion(dato):
    match dato.lower():
        case 'aeropuertos':
            return AEROPUERTOS
        case 'lagos':
            return LAGOS
        case 'ciudades':
            return CITY
        case 'conectividad':
            return CONECTIVIDAD
        case 'poblacion':
            return POBLACION
        

def traerOriginal(dato):
    archivo = pathlib.Path('Datasets',dato)
    return archivo

def traerModificado(dato):
    archivo = pathlib.Path('Datasets Modificados',dato)
    return archivo


readOriginal = traerOriginal('aeropuertos.csv')
readModificado = traerModificado('aeropuertos.csv')