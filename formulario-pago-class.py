import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from includes.funciones import escribir,mi_click,nuevo_driver,navegar,maximiza, esperar, log_evento, leer_csv, completa_form
from includes.selectores_class import Locator, Messages

'''
Leer el historial de cambios en el README.md

'''
log_evento('evento', 'Lectura del archivo de datos.')
nombre_archivo = 'datos/datos.csv'
listado = leer_csv(nombre_archivo)
log_evento('evento',f'Se leyeron {len(listado)} registros del archivo.')

# abro el navegador
driver = nuevo_driver('Chrome')
# maximiza la pantalla
maximiza()

#esperar.corto()

for i, registro in enumerate(listado):
    try:
        # Crear una URL personalizada utilizando los datos del registro
        # abre el site requerido
        navegar()        
        #esperar.corto()
        #print (i['first_name'])

        completa_form(registro)

        # Ejemplo: verificar el título de la página
        #print(f'Título de la página: {driver.title}')
        #log_evento('event',f'Procesando {i['first_name']}.')
    except Exception as e:
        log_evento('error', f'Error al procesar el registro {i + 1}: {e}')
        print(f'Error al procesar el registro {i + 1}: {e}')




quit()


#body = driver.find_element(By.TAG_NAME, 'body')
#str_nombre = driver.find_element(By.ID, Locator.nombre)
#str_apellido = driver.find_element(By.ID, Locator.apellido)
#str_nombre_usuario = driver.find_element(By.ID, Locator.nombre_usuario)
#str_email = driver.find_element(By.ID, Locator.email)
#str_direccion1 = driver.find_element(By.ID, Locator.direccion1)
#str_direccion2 = driver.find_element(By.ID, Locator.direccion2)

# Select de Pais
# El indice empieza en 1
cbo_pais_option = "2" # lo defino como string para contatenarlo al llamar al selector
cbo_pais = driver.find_element(By.CSS_SELECTOR, Locator.pais(cbo_pais_option))

#cbo_pais = driver.find_element(By.CSS_SELECTOR, '#country > option:nth-child('+ cbo_pais_option +')')

# Select de la provincia
cbo_provincia_option = "2"
cbo_provincia = driver.find_element(By.CSS_SELECTOR, Locator.provincia(cbo_provincia_option))

str_cod_postal = driver.find_element(By.ID, Locator.codigo_postal)
chk_dir_envio = driver.find_element(By.ID, Locator.dir_envio)
chk_guarda_info = driver.find_element(By.ID, Locator.guarda_info)
str_nombre_tarjeta = driver.find_element(By.ID, Locator.nombre_tarjeta)
str_numero_tarjeta = driver.find_element(By.ID, Locator.numero_tarjeta)
str_fecha_expiracion = driver.find_element(By.ID, Locator.fecha_expiracion)
int_cvv = driver.find_element(By.ID, Locator.cvv)
btn_continuar = driver.find_element(By.CSS_SELECTOR, Locator.boton_continuar)



escribir(str_nombre, "Marcelito")
escribir(str_apellido, "Kaos")
escribir(str_nombre_usuario, "ZombieEater")
escribir(str_email, "kaosinc@gmail.com")
escribir(str_direccion1, "Av. del Libertador 666")
escribir(str_direccion2, "Suite Emperador")
cbo_pais.click()
cbo_provincia.click()
escribir(str_cod_postal, "1702")

body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

chk_dir_envio.click()
chk_guarda_info.click()

esperar.corto()

escribir(str_nombre_tarjeta, 'Mongo Aurelio')
escribir(str_numero_tarjeta, '5411 1234 5678 9100')
escribir(str_fecha_expiracion,'12/29')
escribir(int_cvv,'432')

esperar.largo()

btn_continuar.click()


esperar.medio()

# Proceso página de resultados
btn_resultado = driver.find_element(By.CSS_SELECTOR, Locator.boton_resultado)

#print (btn_resultado.text)

assert btn_resultado.text == Messages.resultado_ok, Messages.mensaje_error

if btn_resultado.text == Messages.resultado_ok:
    print('-----' + Messages.mensaje_ok +'-----')
else:
    print('-----'+ Messages.mensaje_error +'-----')

esperar.corto()
driver.quit()