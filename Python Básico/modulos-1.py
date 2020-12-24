# import modulos #Importa el código del archivo "modulos.py"
# import modulos as xs #Importa el código de modulos.py bajo el nombre "xs"
from modulos import saludo, mascotas
#MODULO IMPORTADO
# from camelcase import CamelCase

#Renombrar modulos: import nombreModulo as nombreNuevoModulo
print(mascotas)  #IMPRIME EL ARREGLO DE LAS MASCOTAS
#Los módulos ayudan repartir código de un .py a otro .py
saludo('Nicolas')
#SELECCIONANDO LO IMPORTADO
#No todo lo que se importa se debe de usar

# INSTRUCCIONES DEL CAMELCASE
# c = CamelCase()
# s = "Esta oración necesita camelcase!"
# camelcased = c.hump(s)
# print(camelcased)