c = open("chanchito.txt") #Sí funciona pero debe de estar afuera de esa carpeta
print(c.read()) #Devuelve todo el archivo txt
# c = open('chanchito.txt', 'r') #Lee el archivo
# c = open('chanchito.txt', 'a') #Agregar más cosas al archivo
# c = open('chanchito.txt', 'x || w') #Crear el archivo en caso de no existir el txt, pero el "w" lo abre en caso de existir, la "x" manda error en caso de que exista ya el archivo
print(c.readline()) #Lee la primera linea
print(c.readline()) #Lee la segundia linea

for x in c:
    print(x) #Imprime cada línea del archivo

c.close() #Se cierra el archivo

#NOTA: Si se pona la "w" en lugar de la "a" se reescribe el txt en sí
#Si se usa para registros, es preferible el uso de la "a" porque es menos riesgoso para los datos
c = open ("chanchito.txt", 'a') #Abre el archivo para poder editarlo
c.write("Agregamos una nueva línea a nuestro archivo") #Añade una nueva línea de texto en el archivo de ChanchitoFeliz.txt.
#NOTA: Si se sigue ejecutando el código anterior se juntará todo el texto nuevo con el viejo sin un salto de linea
c.write("\nAgregamos una nueva línea a nuestro archivo")
#Hace un salto de línea al principio del nuevo texto
c.close()
#Cierra el archivo
#Se abre el archivo de nuevo
x = open('chanchito.txt') 
#Aparece lo nuevo que se añadió recientemente
print(x.read())

import os #Libreria interna de Python que viene integrado la eliminación de archivos y carpetas
# os.remove('chanchito.txt') #Elimina el txt de chanchito.txt

if os.path.exists("chanchito.txt"):
    os.remove("chanchito.txt")
else:
    print("El archivo no existe")

# os.rmdir ("NOMBRE DE LA CARPETA") #rm dir = remove direction || Sirve para eliminar carpetas