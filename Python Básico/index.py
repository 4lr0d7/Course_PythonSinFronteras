#Sirve para hacer comparaciones
#La identación sirve para que el programa
#sirva bien
if 5 > 3:
    print("5 es mayor de 3")

#Los comentarios sirven para ayudarnos en un futuro a saber cómo funciona una línea de código
#VARIABLES
x = 5
y = "chanchito feliz"
print(x, y) #Imprime n argumentos separados por coma
#Valor primitivo = número, letra, frase [sin guardar en variables]

email = "chanchito@feliz.com"
print(email)
mi_var = "chanchito"
#MIVAR = constantes [TODO MAYUSCULA]

#MULTIPLES VARIABLES
a,b,c = "lala", "lele", "lili"
print(a,b,c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'
print(valor1, valor2, valor3)
#CONCATENACIÓN
inicio = 'Hola ' #Sin separación, se juntan las palabras
final = 'mundo'
print(inicio + final)

#SECCIÓN 5: TIPOS DE DATOS
#Strings y Números
palabra = 'hola mundo' #string
oracion = "Hola mundo con comilla doble" #string

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j #Números complejos

print(palabra, oracion, entero, conDecimales, complejo)

#INTRODUCCIÓN A LAS LISTAS
lista = [1,2,3] #Corchetes vacias = listas vacias
print(lista)
lista2 = lista.copy() #Copia una lista a otra
print('lista 2 [Copia de la lista 1]: ', lista2)
lista.append(4) #Agregar más elementos a la lista
print('lista 1 [Con nuevo elementos]: ', lista)
#lista.clear() #Elimianr todos los elementos de la lista

#CONTANDO ELEMENTOS Y CALCULANDO EL LARGO DE UNA LISTA
print (lista.count(1), lista2.count(5)) #Cuenta elementos repetidos que están dentro de "()"
print(len(lista)) #Imprime la longitud de una lista
print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)
print(largoLista, largoLista2)
#ACCEDIENDO A ELEMENTOS DE LAS LISTAS
lista = ['Hola', 'Mundo', 'Chanchito feliz']
print(lista[0]) #Indice 0 = primer dato del arreglo
#ELIMINANDO ELEMENTOS DE UNA LISTA
lista.pop() #Elimina el último elemento de la lista
print(lista)
lista.append("Chanchito Feliz")
lista.remove('Hola') #lista.remover('string a eliminar')
print(lista)
#REVERSE Y SORT
lista.reverse() #Pone la lista al revés
print(lista)
#lista.sort() #Acomoda la lista de manera ordenada, sólo datos núméricos o sólo datos string, no juntos

#TUPLAS
#Las tuplas se declaran con () en lugar de []
#Las tuplas tienen pocos métodos
tupla = ('hola', 'mundo', 'somos', 'tupla')
print(tupla)
print(tupla.count('hola')) #Cuenta todos los elementos que contengan la palabra 'hola'
print(tupla.index('mundo')) #Busca la posición donde se encuentra ese elemento / dato que queramos encontrar
print(tupla[0]) #Regresa el primer valor de la tupla
# tupla.append('chanchito') #Las tuplas no son modificables, por lo tanto el append no sirve
listaDeTupla = list(tupla) #Transforma la tupla en lista
print(listaDeTupla)
listaDeTupla.append('chanchito')
#RANGE
rango = range(6) #RANGO DE (0,6)
print(rango)
#DICCIONARIOS
diccionario = {
    "nombre" : "Chanchito Feliz",
    "raza" : "Persa",
    "edad" : 5
}
print(diccionario)
#Imprime el valor en el indice de "nombre"
print(diccionario['nombre'])
#Imprime el valor en el indice de "raza"
print(diccionario['raza'])
#Consigue el valor del indice de "nombre" y lo imprime
print(diccionario.get("nombre"))
#Renombra el valor que tiene nombre
diccionario['nombre'] = 'Fluffly' 
print(diccionario)
print("La longitud del diccionario es de: ", len(diccionario))
#PROFUNDIZAR EN LOS DICCIONARIOS
#Para añadir un elemento al diccionario se debe de seguir la siguiente sintaxis:
#NombreDelDiccionario['NombreVariableDelIndice'] = 'ValorQueSePiensaAgregar'
diccionario['ronronea'] = 'Si'
print(diccionario)
#Eliminar valor del diccionario
#diccionario.pop('indice a eliminar')
diccionario.pop('ronronea')
print(diccionario)
diccionario['ronronea'] = 'Si'
print(diccionario)
diccionario.popitem() #Se elimina el último elemento del diccionario
print(diccionario)
diccionario['ronronea'] = 'Si'
print(diccionario)
copiaGatito = diccionario.copy()
del diccionario['ronronea'] #Con la palabra reservada 'del' se puede hacer lo mismo como con el .pop
print(diccionario, copiaGatito)
#Limpiar un diccionario:
#diccionario.clear()
copiaGatito1 = dict(diccionario)
print(copiaGatito1)
#DICCIONARIOS ANIDADOS Y CONSTRUCTOR DICT
# gatitos = {
#     "Fluffy" : {
#         "nombre": "Fluffy",
#         "edad": 4
#     },
#     "Mamba" : {
#         "nombre" : "Black Mamba",
#         "edad": 12
#     }
# }
fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}
mamba = {
    "nombre" : "Black Mamba", 
    "edad": 12
}
gatitos = {
    "Fluffy" : fluffy,
    "Mamba" : mamba
}

print(gatitos)
#DICT
#Alternativa de crear diccionarios
perritos = dict(nombre = "Chanchito Feliz", edad = 6)
print(perritos)
#BOOLEANOS
Verdadero = True #Verdadero
falso = False
print(Verdadero, falso)
#CONTROL DE FLUJOS
#IF Y CONDICIONES

#IF, ELIF Y ELSE

#IF CORTOS Y TERNARIOS

#AND Y OR