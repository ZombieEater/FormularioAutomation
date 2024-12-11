class Locator():
    nombre = "firsdtName"
    apellido = "lastName"
    nombre_usuario = "username"
    email = "email"
    direccion1 = "address"
    direccion2 = "address2"
    
    def pais(indice):
        return '#country > option:nth-child('+ indice +')'
    
    def provincia(indice):
        return '#state > option:nth-child('+ indice +')'
    
    codigo_postal = "zip"
    dir_envio = 'same-address'
    guarda_info = 'save-info'
    nombre_tarjeta = 'cc-name'
    numero_tarjeta = 'cc-number'
    fecha_expiracion = 'cc-expiration'
    cvv = 'cc-cvv'
    boton_continuar = 'body > div > main > div.row.g-5 > div.col-md-7.col-lg-8 > form > button'
    boton_resultado = 'body > form > button'

    

    def kaos(pepe):
        return ('hola ' + pepe)
    
class Messages():
    resultado_ok = 'El pago fue procesado correctamente!'
    mensaje_ok = 'TODO SALIO BIEN'
    mensaje_error = 'A CAMBIAR DE RUBRO'