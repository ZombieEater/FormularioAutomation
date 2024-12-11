import time
import csv
from selenium import webdriver

driver = None
############################## Funciones del driver
def nuevo_driver(navegador):
    global driver
    if navegador == 'Chrome':
        driver = webdriver.Chrome()
        return driver
    elif navegador == 'Firefox':
        driver = webdriver.Firefox()
        return driver
    elif navegador == 'Edge':
        driver = webdriver.Edge()
        return driver

def maximiza():
    global driver
    driver.maximize_window()

def navegar():
    global driver
    driver.get("https://institutoweb.com.ar/test/test2024/checkout/")


###################################### Funciones de Elementos

# obtener elemento
#def obtener()

# reemplaza al click
def mi_click(elemento):
    elemento.click()

#reemplaza el send.keys
def escribir(selector,dato_a_escribir):
    selector.send_keys(dato_a_escribir)
    #time.sleep(1)

def selecciona(by,selector):
    global driver
    return driver.find_element(by, selector) 

###################################### Funciones de espera
#reemplaza al sleep de python
def espera(tipo_espera):
    if tipo_espera == 'WAIT_CORTO':
        time.sleep(1)
    elif tipo_espera == 'WAIT_MEDIO':
        time.sleep(2)
    elif tipo_espera == 'WAIT_LARGO':
        time.sleep(3)

class esperar():
    def corto():
        print("esperando corto")
        time.sleep(1)
    def medio():
        print("esperando medio")
        time.sleep(2)
    def largo():
        print("esperando largo")
        time.sleep(4)

    
###################################
import datetime

def log_evento(tipo_evento, evento):
    """
    Registra un evento en un archivo de texto con la fecha y hora actuales.

    :param evento: (str) Descripción del evento a registrar.
    :param archivo: (str) Nombre del archivo donde se guardará el registro. Por defecto es 'registro_eventos.txt'.
    """
    output_file = "log.txt"

    try:
        # Obtener la fecha y hora actuales
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Crear el mensaje de registro
        mensaje = f"[{timestamp}] {evento}\n"
        # Escribir el mensaje en el archivo
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(mensaje)
        print("Evento registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el evento: {e}")

# Ejemplos de uso
#log_evento ('Evento', 'Inicio del programa.')
#log_evento ('Error', 'Elemento no encontrado.')


# función para leer el csv y pasarlo a un diccionario
def leer_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de registros.
    :param nombre_archivo: (str) Nombre del archivo CSV.
    :return: (list) Lista de registros (filas como diccionarios).
    """
    registros = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo_csv:
            cursor = csv.DictReader(archivo_csv)
            #next(cursor, None)  # Omitir el primer registro
            for row in cursor:
                print(row['first_name'])
                registros.append(row)
        print(f"Se leyeron {len(registros)} registros del archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return registros

# función para procesar el formulario con cada línea obtenida del archivo csv

def completa_form (listado):
    
    global driver