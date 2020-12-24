def miFuncion():
    print("Mi primera función")

# miFuncion()

def imprimirDato(argumentoUno): #Entre menos argumentos tenga, más entendible será.
    print("Mi argumento es", argumentoUno)

imprimirDato('Parametro Uno') #Llama a la función y pasamos el parámetro

def nombreCompleto(nombre, apellido): #Se deben de usar sí o sí los 2 argumentos
    print(f'El nombre completo es:{nombre} {apellido}')

# nombreCompleto('Chanchito') #Manda ERROR

def nombreCompleto2(*nombre): #Guarda los datos que se arrojan en una Tupla, por lo que no se puede modificar nada de ahí
    print('El nombre completo es: ', nombre[0]) #[n] es el indice dentro del arreglo

nombreCompleto2("Chanchito", "Feliz", "lala", "lele")

def nombreComplete(apellido, nombre):
    print(nombre, apellido)

nombreComplete(nombre = "Chanchito", apellido = "Feliz")

def nombreComplete2(**kwargs): #Argumento por llave
    print(kwargs['nombre'], kwargs['apellido'])

nombreComplete2(nombre = "Chanchito", apellido = "Feliz")

#MÁS FUNCIONES 
def miFuncion2(argumento = "Chanchito"): #Podemos poner un valor predeterminado al argumento
    print(argumento)

miFuncion2('Batman')
miFuncion2()

def miFuncionLista(lista): #Podemos pasar una Lista completa
    for elemento in lista:
        print(elemento)

miFuncionLista(['Chanchito', 'Feliz'])

def concatenarNombre(lista):
    i = ''
    for el in lista:
        i = i + el + ''
    return i #Si regresa un valor se debe de guardar en una variable
nombres = concatenarNombre(['Chanchito', 'Feliz'])
print(nombres)

def recursion(i):
    if(i < 1):
        return i
    else:
        print(i)
        recursion(i-1)

recursion(6)