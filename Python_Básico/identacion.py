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