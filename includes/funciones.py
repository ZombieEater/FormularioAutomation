import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from includes.selectores_class import Locator, Messages
from includes.config import config


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

# reemplaza al click
def mi_click(elemento):
    elemento.click()

#reemplaza el send.keys
def escribir (selector, dato_a_escribir):
    #if (selector != None):
    selector.send_keys(dato_a_escribir)
    #else:
    #    print('No se pudo escribir el elemento.')
    
def selecciona (by, selector):
    global driver
    try:
        return driver.find_element(by, selector)
    except NoSuchElementException:
        printKaos(f'Error: No se encontró el elemento {selector} en la página.')
        log_evento('error', f'Error: No se encontró el elemento {selector} en la página.')
    except WebDriverException as e:
        printKaos('WebDriver error occurred: {e}')
        log_evento('error', 'WebDriver error occurred: {e}')


###################################### Funciones de espera
#reemplaza al sleep de python
'''
def espera(tipo_espera):
    if tipo_espera == 'WAIT_CORTO':
        time.sleep(1)
    elif tipo_espera == 'WAIT_MEDIO':
        time.sleep(2)
    elif tipo_espera == 'WAIT_LARGO':
        time.sleep(3)
'''

# Funciones Kaos

def printKaos(mensaje):
    if (config.PRINT):
        print(mensaje)

class esperar():
    def corto():
        printKaos("esperando corto")
        time.sleep(1)
    def medio():
        printKaos("esperando medio")
        time.sleep(2)
    def largo():
        printKaos("esperando largo")
        time.sleep(4)

    
###################################
import datetime

def log_evento(tipo_evento, evento):
    """
    Registra un evento en un archivo de texto con la fecha y hora actuales si el flag LOG de la clase CONFIG es verdadero. Sino pasa de largo.

    :param evento: (str) Descripción del evento a registrar.
    :param archivo: (str) Nombre del archivo donde se guardará el registro. Por defecto es 'registro_eventos.txt'.
    """
    if (config.LOG or tipo_evento == 'error'):
        output_file = "log.txt"

        #print(config.LOG)

        try:
            # Obtener la fecha y hora actuales
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Crear el mensaje de registro
            mensaje = f"[{timestamp}] {evento}\n"
            # Escribir el mensaje en el archivo
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(mensaje)
            #print("Evento registrado exitosamente.")
        except Exception as e:
            printKaos(f"Error al registrar el evento: {e}")

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

def completa_form (registro):
    
    global driver
    body = driver.find_element(By.TAG_NAME, 'body')

    str_nombre = selecciona(By.ID, Locator.nombre)
    str_apellido = selecciona(By.ID, Locator.apellido)
    str_nombre_usuario = selecciona(By.ID, Locator.nombre_usuario)
    str_email = selecciona(By.ID, Locator.email)
    str_direccion1 = selecciona(By.ID, Locator.direccion1)
    str_direccion2 = selecciona(By.ID, Locator.direccion2)
    # Select de Pais
    # El indice empieza en 1
    cbo_pais_option = registro['country'] # lo defino como string para contatenarlo al llamar al selector
    cbo_pais = selecciona(By.CSS_SELECTOR, Locator.pais(cbo_pais_option))
    # Select de la provincia
    cbo_provincia_option = registro['province']
    cbo_provincia = selecciona (By.CSS_SELECTOR, Locator.provincia(cbo_provincia_option))

    str_cod_postal =  selecciona (By.ID, Locator.codigo_postal)
    chk_dir_envio =  selecciona (By.ID, Locator.dir_envio)
    chk_guarda_info =  selecciona (By.ID, Locator.guarda_info)
    str_nombre_tarjeta =  selecciona (By.ID, Locator.nombre_tarjeta)
    str_numero_tarjeta =  selecciona (By.ID, Locator.numero_tarjeta)
    str_fecha_expiracion =  selecciona (By.ID, Locator.fecha_expiracion)
    int_cvv =  selecciona (By.ID, Locator.cvv)
    btn_continuar =  selecciona (By.CSS_SELECTOR, Locator.boton_continuar)

    # Está hecho de esta forma, pero realmente la función que obtiene el elemento, si no pudo, ya debería devolver el error al loop del script original en vez de continuar con los elementos. Entiendo que es regla de negocio o análisis de log.

    escribir(str_nombre, registro['first_name'])
    escribir(str_apellido, registro['last_name'])
    escribir(str_nombre_usuario, registro['user_name'])
    escribir(str_email, registro['email'])
    escribir(str_direccion1, registro['address_1'])
    escribir(str_direccion2, registro['address_2'])
    cbo_pais.click()
    cbo_provincia.click()
    escribir(str_cod_postal, registro['zip'])

    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)

    if (registro['send_to'] == '1'):
        chk_dir_envio.click()
    if (registro['save_address'] == '1'):        
        chk_guarda_info.click()

    escribir(str_nombre_tarjeta, registro['card_first_name'])
    escribir(str_numero_tarjeta, registro['card_number'])
    escribir(str_fecha_expiracion,registro['card_exp'])
    escribir(int_cvv,registro['card_cvv'])
    
    #esperar.medio()