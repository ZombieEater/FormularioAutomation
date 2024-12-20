20241211 V 1.0

- Reorganizado de archivos.
- Repo publico.
- Clases para reutilizar código.
- Log a archivo de texto.
- Procesar archivo csv.
- Se adiciona config para las constantes.

Funcionamiento:

- Se lee el archivo CSV y se lo almacena en un diccionario de Python. Se registra el evento y cantidad de registros leidos. (El archivo CSV fu'e creado con mockaroo.com)

- Se instancia el driver de chrome.

- Se procesa el diccionario invocando al driver con una función.

- Las funciones de LOG y PRINT son sobreescritas con las mias, para poder gestionarlo desde la configuración

- El llenado del formulario se hace desde una función. Si algún elemento no se encontrase, se salta el registro y continúa la ejecución.

- El click del boton principal y la espera de la página de OK, se gestionan desde el script principal por comodidad de lectura.

- Se debería agregar la captura de errores de obtención del elemento antes de intentar llenarlo, hacerlo todo en un solo paso.

- Uno de los elementos de prueba, tiene error en el email para verificar la captura de error.



20241220 - Ejemplo en el script "ejemplo-assert.py" de como corta la ejecución al usar el assert directo, y como la continua al estar dentro de un TRY.



---------------
Cosas útiles:

Shift + alt + F (embellece el código)

ctrl + } (comenta en grupo linea por linea)

shift + LAlt + Down (duplica la linea del cursor)

where python

https://googlechromelabs.github.io/chrome-for-testing/