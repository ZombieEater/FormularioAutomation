import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from includes.funciones import escribir,mi_click,nuevo_driver,navegar,maximiza, esperar
from includes.selectores_class import Locator, Messages

'''
DISCLAIMER:
Por costumbre, todo lo que sean funciones o fragmentos reusables, suelo meterlos en una carpeta que lo diferencia de los archivos principales, en este caso INCLUDES, contiene las funciones, los selectores y demás.

Modifiqué, con idea de que me corrijan si está mal o no es buena práctica, en vez de usar el diccionario de "SELECTORES", que me incomodaba que no los autocompletaba, pasé los selectores como una CLASE de Python, que cada valor, es una propiedad, entonces me lo autocompleta cuando pongo Locator.****

PERO para el caso el menú desplegable, yo le tengo que indicar el índice para que seleccione lo que quiero...entonces es un método (una función dentro de la clase), y así le puedo pasar EN MODO TEXTO (con comillas), el índice del pais o provincia a seleccionar (aun no lo clickea, solo lo selecciona).

De la misma forma, la funcion espera, la cambié por una clase dentro de las funciones, donde el tiempo a esperar, tambien se lo mando como una propiedad.

Como mala práctica, pero para no marear, los mensajes que espero de un boton, a presentar en pantalla, etc, los puse dentro de selectores (deberia ir a otro lado, porque no son selectores, pero la idea es esa...)...entonces también limpié el código usando "variables" en vez de texto hardcodeado.

Si mareé: 0-800-666-HELP  jaja

'''

# abro el navegador
driver = nuevo_driver('Chrome')
# maximiza la pantalla
maximiza()
# abre el site requerido
navegar()

esperar.corto()

body = driver.find_element(By.TAG_NAME, 'body')

str_nombre = driver.find_element(By.ID, Locator.nombre)
str_apellido = driver.find_element(By.ID, Locator.apellido)
str_nombre_usuario = driver.find_element(By.ID, Locator.nombre_usuario)
str_email = driver.find_element(By.ID, Locator.email)
str_direccion1 = driver.find_element(By.ID, Locator.direccion1)
str_direccion2 = driver.find_element(By.ID, Locator.direccion2)
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