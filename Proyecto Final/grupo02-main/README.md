# Trabajo Integrador
El trabajo integrador es una aplicacion simple que consta de 2 modulos:
- El primero de ellos encargado del procesamiento de cada dataset (dados por la catedra) donde cada funcion recibe dos direcciones, la primera con el archivo dado y la segunda con un nuevo archivo que contiene la informacion procesada y modificada del primero. 
- El segundo modulo consta de una pagina creada utilizando principalmente las librerias streamlit y pandas, en la cual se desarrolla un juego estilo trivia de preguntas sobre los datasets modificados en la primera parte, tambien mostrando ranking y estadisticas sobre el mismo.

## Integrantes:
- Aixa Charif | 21882/4
- Facundo Peri | 17939/5
- Tomas Ferrer | 17818/6
- Martin Stampone | 17940/7


### Requisitos Previos:
- Python 3.11.x

### Instalacion:
1.  Clona este repositorio en tu máquina local:
    git clone git@gitlab.catedras.linti.unlp.edu.ar:python2024/code/grupo02.git

2.  Accede al directorio del proyecto con una ventana de comandos (La ruta puede variar dependiendo donde se haya descargado/clonado el repositorio):
    cd grupo02

3.  Crear el entorno virtual:
    python -m venv venv

4.  Activar el entorno virtual:
    venv\Scripts\activate  # windows
    source venv/bin/activate  # Linux

5.  Instala las dependencias necesarias:
    pip install -r requirements.txt

6.  Desactive el entorno si asi lo desea:
    deactivate

### Uso:

1.  Activar el entorno virtual: 
    venv\Scripts\activate  # windows
    source venv/bin/activate  # Linux

2.  Ejecutar entorno de Jupyter
    python -m notebook .

3.  Ejecutar las instrucciones dentro del archivo "processing.ipynb" para realizar el procesamiento de los datasets.

4.  Realizar las consultas ejecutando las instrucciones del archivo "queries.ipynb"

5.  Para ejecutar la aplicación web:
    streamlit run streamlit\Inicio.py


## Licencia
Este proyecto cuenta con licencia **GNU GENERAL PUBLIC LICENSE** Version 3, 29 June 2007. Consulta el archivo `LICENSE` para más detalles.
