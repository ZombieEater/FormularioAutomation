
# Utilizando el try, no corta la ejecución, y podemos asignar a una variable el mensaje requerido.
# En mi proyecto ejemplo, la función "log_evento" es la que guarda el evento al TXT


resultado_ok = 'Todo Ok sin try'
resultado_assert = 'Falló el assert sin try'

# Este ejemplo de código, corta la ejecución.


# Probar comentando el assert de la linea 15 para notar que la ejecución sigue.

#try:
assert 'pepe' == 'dpepe', resultado_assert
#except Exception as e:
#    print (e)



resultado_ok = 'Todo Ok CON try'
resultado_assert = 'Falló el assert CON try'

try:
    assert 'pepe' == 'dpepe', resultado_assert
except Exception as e:
    print (e)
