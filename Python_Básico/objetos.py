#Una clases es como un plano de una casa
#El plano representa las clases y la casa construida representa a los objetos.
#PRIMER PLANO O PRIMERA CLASE

# class Usuario: #Primera letra en mayúsculas
#     nombre = "Felipe"
#     apellido = "Feliz"


# #INSTANCIA
# usuario = Usuario()  #La instancia irá en minusculas
# print(usuario) #Nos imprime el mensaje de que es una clase
# print(usuario.nombre) #Imprime el nombre que tiene el atributo nombre en la variable
# print(usuario.nombre, usuario.apellido) #Imprime los 2 elementos de la clase

#Las clases sirven para reutilizar código
#Clase Padre
class Usuario: #Primera letra en mayúsculas
    def __init__(self, nombre, apellido): #SELF es la referencia del objeto cuando lo instanciamos. Instancia separada para n instancias.
        self.nombre = nombre
        self.apellido = apellido

    #METODO_INICIO
    def saludo(self):
        print('Hola!, mi nombre es: ', self.nombre, self.apellido)
    #METODO_FINAL

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')
print(usuario.nombre, usuario.apellido)
#METODO_INICIO
usuario.saludo()
usuario2.saludo()
#METODO_FINAL

#SELF, ELIMINAR PROPIEDADES Y OBJETOS
#La convención de self sirve para tener código limpio y que se vea legible ante otros desarrolladores
usuario.nombre = 'Chanchito' #renombra una propiedad de la clase
usuario.saludo()
#Eliminar atributos
# del usuario.nombre
# usuario.saludo() #Mandará error porque el atributo ha sido borrado
# del usuario   #Elimina toda la instancia del objeto
# print(usuario)

#HERENCIA
#Se puede reutilizar aún más el código
#Clase hijo
class Admin(Usuario): #Adentro de los corchetes redondos se pone la clase a heredar
    def superSaludo(self):
        print('Hola!, me llamo: ', self.nombre, ' y soy adminstrador')
    
admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()

#EJERCICIO DE HERENCIA
class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola, soy un ', self.tipo, 'y mi sonido es el ',self.onomatopeya)

class Gato (Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): #Ignora el init de la clase Padre si no se pone lo siguiente
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')


class Perro (Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolín', 'silbido')
canario.saludo()